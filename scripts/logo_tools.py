#!/usr/bin/env python3
"""Logo-wall asset tooling: audit padding, trim to content, preview a wall.

Logos are rendered flat-grey by the `logo_grid` / `logo_strip` macros
(`filter: brightness(0) invert(0.7)`), and sized by a per-logo `height`.
For that height to mean the same thing across logos, every file must be
*tight-cropped* — no transparent padding baked into the canvas. A logo
with 30% vertical padding renders ~30% smaller than a tight one at the
same `height`, which is what makes an untuned wall look uneven.

This tool keeps logos in that tight-cropped state and lets you eyeball a
wall the way the macro will actually render it (grey, on white) before
committing height values.

Commands
--------
  audit                 Report transparent-padding % for every logo.
  trim FILE [FILE...]   Crop PNG(s) to their content bounding box, in place.
  knockout FILE [TOL]   Make the background (sampled from the corners)
                        transparent, in place. TOL is the color-match
                        tolerance (default 36). Needed when a logo ships on
                        an opaque white/colored fill — otherwise the macro's
                        brightness(0) filter renders the whole tile as a grey
                        block. Re-run `preview` afterward to confirm.
  preview PAGE [OUT]    Render PAGE's logo wall as the grey composite the
                        macro produces. PAGE is a slug (e.g. 'insurance')
                        or a path to a content/pages/*.md file. Writes a
                        PNG (default /tmp/<slug>_wall.png) for you to open.

SVGs are left alone: they scale by viewBox and our set is already tight
(verify with `audit`). Only raster PNGs accumulate baked padding.

Requires Pillow. Run via uv so the dependency is gated and reproducible:

    uv run --with "pillow" --exclude-newer "7 days" \
        python scripts/logo_tools.py audit
"""

import glob
import os
import re
import subprocess
import sys

from PIL import Image

LOGO_DIR = os.path.join("content", "images", "logos")
PAGES_DIR = os.path.join("content", "pages")

# The .logo-grey CSS chain resolves opaque pixels to this cool grey
# (target #9CA3AF, Tailwind gray-400); alpha is preserved. Keep in sync
# with the .logo-grey class in themes/shovels/static/css/input.css.
GREY = (156, 163, 175)
PAD_FLAG_PCT = 5  # report/trim threshold for "meaningful" padding


def _padding_pct(im):
    """Return (vpad%, hpad%, content_box) for an RGBA image, or None if empty."""
    im = im.convert("RGBA")
    box = im.getbbox()
    if not box:
        return None
    w, h = im.size
    cw, ch = box[2] - box[0], box[3] - box[1]
    return round(100 * (h - ch) / h), round(100 * (w - cw) / w), box


def audit():
    files = sorted(glob.glob(os.path.join(LOGO_DIR, "*.png")))
    print(f"{'file':30} {'canvas':>11} {'vpad':>5} {'hpad':>5}  flag")
    for path in files:
        im = Image.open(path)
        w, h = im.size
        res = _padding_pct(im)
        if res is None:
            print(f"{os.path.basename(path):30} {f'{w}x{h}':>11}  EMPTY")
            continue
        vpad, hpad, _ = res
        flag = "TRIM" if (vpad >= PAD_FLAG_PCT or hpad >= PAD_FLAG_PCT) else "ok"
        print(f"{os.path.basename(path):30} {f'{w}x{h}':>11} "
              f"{f'{vpad}%':>5} {f'{hpad}%':>5}  {flag}")
    print("\nSVGs scale by viewBox and are assumed tight; spot-check by eye.")


def trim(paths):
    for path in paths:
        if path.lower().endswith(".svg"):
            print(f"skip {path} (SVG — crop via viewBox, not this tool)")
            continue
        im = Image.open(path).convert("RGBA")
        box = im.getbbox()
        if not box:
            print(f"skip {path} (fully transparent)")
            continue
        before = im.size
        im.crop(box).save(path)
        print(f"{os.path.basename(path):30} {before} -> {im.crop(box).size}")


def knockout(path, tol=36):
    """Make the corner-sampled background color transparent. For logos that
    ship on an opaque fill, which the grey filter would otherwise flatten
    into a solid block."""
    if path.lower().endswith(".svg"):
        sys.exit("knockout is for raster PNGs; edit the SVG's background rect")
    im = Image.open(path).convert("RGBA")
    px = im.load()
    w, h = im.size
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    opaque = [c for c in corners if c[3] > 200]
    if opaque:
        br, bg, bb = max(opaque, key=opaque.count)[:3]
    else:
        # Transparent corners but an interior opaque fill (a white plate or a
        # tinted badge behind the mark). Target the most common light opaque
        # color — that's the fill, not the (usually dark) lettering.
        from collections import Counter
        light = Counter(
            (r, g, b) for r, g, b, a in im.getdata()
            if a > 200 and (r + g + b) / 3 > 180
        )
        if not light:
            print(f"{path}: no light fill found, nothing to knock out")
            return
        br, bg, bb = light.most_common(1)[0][0]
    removed = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a and abs(r - br) <= tol and abs(g - bg) <= tol and abs(b - bb) <= tol:
                px[x, y] = (r, g, b, 0)
                removed += 1
    box = im.getbbox()
    if box:
        im = im.crop(box)
    im.save(path)
    print(f"{os.path.basename(path)}: removed bg ~rgb({br},{bg},{bb}), "
          f"{removed} px -> {im.size}")


def _resolve_page(page):
    if os.path.isfile(page):
        return page
    cand = os.path.join(PAGES_DIR, f"{page}-preview.md")
    if os.path.isfile(cand):
        return cand
    cand = os.path.join(PAGES_DIR, f"{page}.md")
    if os.path.isfile(cand):
        return cand
    sys.exit(f"page not found: {page}")


def _parse_logos(md_path):
    """Pull (src, height) pairs from the page's logo dict list."""
    text = open(md_path, encoding="utf-8").read()
    logos = []
    for src in re.finditer(r"'src':\s*'([^']*?/logos/[^']+)'[^}]*?}", text):
        block = src.group(0)
        path = src.group(1)
        m = re.search(r"'height':\s*(\d+)", block)
        logos.append((path, int(m.group(1)) if m else 30))
    return logos


def _shape_mask(im):
    """Alpha mask of the logo shape. Transparent PNGs use their own alpha;
    opaque rasters (e.g. SVGs rendered on white by qlmanage) fall back to
    'anything not near-white is the logo'."""
    im = im.convert("RGBA")
    alpha = im.split()[3]
    if alpha.getextrema()[0] < 250:  # has real transparency
        return alpha
    # opaque on white: near-white -> background (0), everything else -> logo
    grey = im.convert("L")
    return Image.eval(grey, lambda v: 0 if v >= 245 else 255)


def _silhouette(im):
    """Crop to content and return a flat-grey RGBA tile, matching the macro's
    CSS filter. White interior knockouts read as transparent (show through)."""
    mask = _shape_mask(im)
    box = mask.getbbox()
    if box:
        mask = mask.crop(box)
    tile = Image.new("RGBA", mask.size, GREY + (0,))
    tile.putalpha(mask)
    return tile


def _load_raster(fpath):
    """Open any logo as an RGBA image. SVGs are rasterized with macOS
    QuickLook (qlmanage) since the preview only needs pixels, not vectors."""
    if fpath.lower().endswith(".svg"):
        outdir = "/tmp/logo_tools_svg"
        os.makedirs(outdir, exist_ok=True)
        subprocess.run(["qlmanage", "-t", "-s", "1600", "-o", outdir, fpath],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        png = os.path.join(outdir, os.path.basename(fpath) + ".png")
        if not os.path.exists(png):
            raise RuntimeError(f"qlmanage failed to rasterize {fpath}")
        return Image.open(png).convert("RGBA")
    return Image.open(fpath).convert("RGBA")


def preview(page, out=None):
    md_path = _resolve_page(page)
    slug = os.path.splitext(os.path.basename(md_path))[0]
    out = out or os.path.join("/tmp", f"{slug}_wall.png")
    logos = _parse_logos(md_path)
    if not logos:
        sys.exit(f"no logos found in {md_path}")

    scale = 4  # blow up so small px differences are visible on screen
    gap, pad, band = 64 * scale // 2, 70, 80
    tiles = []
    for src, height in logos:
        fname = os.path.basename(src)
        fpath = os.path.join(LOGO_DIR, fname)
        if not os.path.isfile(fpath):
            print(f"  WARNING missing {fname}")
            continue
        sil = _silhouette(_load_raster(fpath))
        h = height * scale
        w = max(1, round(sil.width * h / sil.height))
        tiles.append((fname, height, sil.resize((w, h))))

    total_h = max(t[2].height for t in tiles) + band
    total_w = pad * 2 + sum(t[2].width for t in tiles) + gap * (len(tiles) - 1)
    canvas = Image.new("RGBA", (total_w, total_h), (255, 255, 255, 255))
    x = pad
    for _, _, tile in tiles:
        canvas.alpha_composite(tile, (x, (total_h - tile.height) // 2))
        x += tile.width + gap
    canvas.convert("RGB").save(out)
    print(f"{slug}: " + ", ".join(f"{n}@{h}" for n, h, _ in tiles))
    print(f"wrote {out}")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd, rest = argv[0], argv[1:]
    if cmd == "audit":
        audit()
    elif cmd == "trim":
        if not rest:
            sys.exit("trim needs at least one file")
        trim(rest)
    elif cmd == "knockout":
        if not rest:
            sys.exit("knockout needs a file")
        knockout(rest[0], int(rest[1]) if len(rest) > 1 else 36)
    elif cmd == "preview":
        if not rest:
            sys.exit("preview needs a page slug or path")
        preview(rest[0], rest[1] if len(rest) > 1 else None)
    else:
        sys.exit(f"unknown command: {cmd}\n{__doc__}")


if __name__ == "__main__":
    main(sys.argv[1:])
