# Website Refresh 2026 — Action Plan

A living tracker for the site refresh. Started as a single Insurance
page, became an Industry-page template, then a site-wide refresh
(homepage, footer, nav, and new pages). This doc keeps the moving
parts and their dependencies in one place.

Companion docs: **COMPONENTS.md** (design system / macros),
**IMAGE_MANIFEST.md** (per-page image + logo tracking).

---

## The one thing to keep straight: staged vs. global changes

Two fundamentally different change types, with different blast radius
and launch mechanics:

### 1. Staged changes (safe to build now, invisible until launch)
Content pages built behind a `-preview` slug with `status: hidden`.
They don't affect the live site until we do the launch swap
(`<page>-preview.md` → `<page>.md`, drop the `-preview` slug, remove
`status: hidden`). Build freely, review on dev, ship when ready.

- All Industry preview pages, the Research page, the homepage preview.

### 2. Global changes (affect the LIVE site the moment they deploy)
Shared theme files have **no preview gate**. The next production build
ships them to every page immediately:

- `themes/shovels/templates/footer.html` → every page
- `themes/shovels/templates/header.html` (top nav) → every page
- `themes/shovels/templates/base.html` → every page
- `themes/shovels/static/css/input.css` (+ Tailwind config) → every page
- Shared macros / `sections/*` → every page that imports them

**Implication:** a redesigned footer or nav can't hide behind a
preview slug. Either (a) it must be backward-compatible with the
*current* live pages, or (b) it ships in the same deploy as the page
launches. Decide per element — see Launch sequencing below.

---

## Affected-pages register

What the refresh touches, and why.

| Surface | Type | Status | Notes |
|---|---|---|---|
| Insurance | Staged page | ✅ preview built | New page; `insurance-preview` → `/insurance` at launch |
| Energy & Climate | Staged page | ✅ preview built | Redesign of live `/climate` |
| Building Materials | Staged page | ✅ preview built | Redesign of live `/building-materials` |
| Home Services | Staged page | ✅ preview built | Redesign of live `/home-services` |
| Real Estate | Staged page | ✅ preview built | Redesign of live `/real-estate` |
| Construction Tech | Staged page | ✅ preview built | Redesign of live `/software` |
| Telecommunications | Staged page | ✅ preview built | Redesign of live `/telecommunications` |
| Research | Staged page | ✅ preview built | New page; `/research` at launch |
| Homepage | Staged-ish | ✅ preview built | Lives in theme `index.html`, not a content page — preview content moves into the template at launch (not a simple rename) |
| Footer | **Global** | 🟡 preview built | New `footer-refresh.html` (6 columns: Industries/Solutions/Features/Data/Resources/Company, left newsletter, mobile accordions w/ carats, newsletter hidden on mobile, slim bottom bar). DRY `footer_sections` data drives both mobile + desktop. Gated in `base.html` to `*-preview` pages only — live footer untouched. Open: HubSpot form wiring, Data go-live handling, final link/column curation |
| Top nav (header) | **Global** | 🟡 preview built | New `header-refresh.html` (Industries/Solutions/Features/Resources + Sign In/Get Started; **Data omitted** until those pages ship). DRY `nav_menus` data drives desktop mega-dropdowns + mobile accordions. Dropdowns are icon link columns + Contact Sales row, two balanced columns at ≥6 items; caret flips up, panel beak points to trigger, rightmost menu right-anchored; rounded-full Get Started. Gated in `base.html` to `*-preview` pages — live header untouched. Open: Solutions/Features links use planned `/solutions/` `/features/` slugs (404 until moved); promo panel intentionally dropped; icons are Lucide stand-ins |
| Typography / base CSS | **Global** | ✅ already cascaded | Scandia headings + system body stack (logged in COMPONENTS.md) |
| New pages (future) | Staged page | ⬜ to design/build | Build behind `hidden`; may not launch with this wave |

**Known content gap (launch dependency):** the live nav AND footer
list only six industries — **Insurance and Research are missing from
both.** They must be added when those pages go live.

---

## Proposed information architecture (refreshed sitemap)

Top nav: **Industry · Solutions · Features · Data · Resources** +
**Get Started** / **Sign In** (CTAs).

### Industry (8) — slugs unchanged
Building Materials & Equipment Suppliers, Construction Technology,
Energy & Climate, Home Services, Real Estate, Telecommunications,
**Research** (new), **Insurance** (new).

### Solutions (3) — ⚠ NEW URL PREFIXES
The current flat "Solutions" group is split. These three move under
`/solutions/`:

| Page | Current URL | New URL |
|---|---|---|
| Shovels Online | `/permit-database` | `/solutions/permit-database` |
| API | `/api` | `/solutions/api` |
| Enterprise (data feed) | `/data-feed` | `/solutions/data-feed` |

### Features (3) — ⚠ NEW URL PREFIXES, new top-level section
| Page | Current URL | New URL |
|---|---|---|
| Charlie AI | `/charlie` | `/features/charlie` |
| GIS | `/gis` | `/features/gis` |
| CLI | `/cli` | `/features/cli` |

**Audiences** (`/audiences`) is NOT in the new nav — confirm whether
it's deprecated, kept unlinked, or relocated.

**The URL moves require redirects** (old → new) — the first part of
this refresh that genuinely needs them. Slug changes also mean the
page files / `Slug:` frontmatter get updated, and any internal links
(incl. cross-page CTAs) repointed.

### Data (5) — ALL NEW, post-launch
Permits, Decisions, Contractors, Residents, Properties (Properties
tentative). Not built yet; ships **after** the main refresh goes live.

### Resources
Blog, Knowledge Base, Data Dictionary, Data Coverage Dashboard, About,
Careers. (Note: About + Careers sit under Resources here, vs. the
current footer's "Company" column.)

### Net-new pages (right rail — own cadence)
Map Gallery, Brand, Partners, Pricing (tentative). Build behind
`hidden`; launch independently.

---

## Phased plan

### Phase 1 — Refresh template & preview pages ✅ (essentially done)
- Design system locked (COMPONENTS.md), macros + sections built.
- 8 industry preview pages + homepage preview built and image-complete.
- Remaining: Trinh Insurance logo (Insurance grid 3/4); first-pass
  logo-height tuning; designer walkthrough.

### Phase 2 — Global chrome (current)
- **Footer** redesign (preview built) — `footer-refresh.html`, gated.
- **Top nav / header** redesign (preview built) — `header-refresh.html`,
  gated to `*-preview` pages, mirrors the footer pattern.
- Decide backward-compatibility vs. launch-coupled deploy for each.

### Phase 3 — Designer review
- Walk every `*-preview` page + the new footer/nav on dev.
- Tune logo heights, framing, spacing. Resolve the open flags.

### Phase 4 — Launch sequencing
- Decide what ships together (see below).
- Execute slug swaps (industry + research), move homepage preview into
  `index.html`, deploy footer/nav, add new pages to nav/footer.

### Phase 5 — Future pages (build now, launch later)
- Design + build net-new pages behind `status: hidden`.
- Hold until their own go-live; keep out of nav/footer until then.

---

## Launch sequencing (draft — to finalize in Phase 4)

The launch is not one atomic action. Rough order of operations:

1. **Pre-launch**: confirm all preview pages approved; nav + footer
   updated to include every launching page (incl. Insurance, Research).
2. **Coupled deploy** (single merge): industry slug swaps + homepage
   into `index.html` + new global footer/nav. These are
   interdependent — the new nav/footer link to the redesigned pages,
   and the redesigned pages assume the new chrome.
3. **Post-launch**: verify every live URL, FAQ schema, redirects (none
   needed — slugs unchanged for redesigns), and the homepage.
4. **Future pages**: launch on their own cadence; add to nav/footer
   when each goes live.

Open question: do we want a **staging deploy** of the whole branch
(so stakeholders see the full new site at real URLs) before flipping
production? Recommended given the scope.

---

## Pre-launch checklist

The go/no-go list. Tick items as they're done; add your own under
"More (your ideas)". Nothing here is a one-way door until the final
production deploy, so we can keep iterating on the branch.

### Content & pages
- [ ] Designer walkthrough of all 8 industry preview pages
- [ ] Designer walkthrough of homepage preview
- [ ] Research page reviewed (UC1 framed vs unframed call confirmed)
- [ ] Trinh Insurance logo sourced → Insurance grid 4/4
- [ ] Logo heights tuned across all grids (designer pass)
- [ ] White-on-hover logos resolved or accepted (Hawkins, Avenue Roofing)
- [ ] Every page renders with no `TBD` placeholders
- [ ] Blog pull-ins use the correct category/tag combo per page —
      each industry page's `get_industry_articles('<Category>')` matches
      its industry (and resolves enough posts), and the homepage pulls
      most-recent via `get_recent_articles`. Confirm Research has a
      blog pull (no `get_industry_articles` call found yet)

### URLs, routing & redirects
- [ ] Move Solutions pages to `/solutions/*` (permit-database, api, data-feed)
- [ ] Move Features pages to `/features/*` (charlie, gis, cli)
- [ ] Old → new redirects for all 6 moved pages
- [ ] Repoint internal links/CTAs to new URLs (footer, nav, cross-page, blog)
- [ ] Audiences decision executed (deprecate / keep / relocate)
- [ ] Industry slug swaps: `*-preview.md` → live slug, drop `-preview`,
      remove `status: hidden`, delete legacy file (climate, real-estate,
      building-materials, software, home-services, telecommunications)
- [ ] Insurance + Research promoted to `/insurance`, `/research`
- [ ] Homepage: preview content moved into theme `index.html`
      (reconcile `STATS`/helper globals + the `dates` blog loop vs.
      `get_recent_articles`)

### Global chrome
- [ ] Footer: promote `footer-refresh.html` → global `footer.html`
      (remove the `-preview` gate in `base.html`)
- [x] Footer: HubSpot newsletter form wired into the custom design
      (`footer-refresh.html` posts to the Submissions API, "Footer
      Newsletter Signup" form; test submission confirmed in HubSpot)
- [ ] Footer: Data column go-live handling decided + applied
- [x] Top nav rebuilt for new IA — `header-refresh.html` (Industries/
      Solutions/Features/Resources + Sign In/Get Started; Insurance +
      Research included; mobile accordions). Gated to `*-preview`
- [ ] Header: promote `header-refresh.html` → global `header.html`
      (remove the `-preview` gate in `base.html`)
- [ ] Header: repoint Solutions/Features links once those pages move
      under `/solutions/` `/features/` (currently 404 in preview)
- [ ] Header: add the Data top-level once the Data pages ship (omitted now)
- [ ] Header: swap Lucide stand-in icons for final marks (designer)

### Build & technical
- [ ] Production build passes (`make publish`)
- [ ] CSS compiled fresh — no missing utilities (the footer-overlap bug)
- [ ] FAQ `FAQPage` JSON-LD renders on every industry page
- [ ] Sitemap includes launched pages, excludes `hidden`/`-preview`
- [ ] Meta descriptions present on all launched pages
- [ ] Branch rebased/merged with `main` (currently well behind)

### SEO, analytics & legal
- [ ] Redirects preserve SEO equity for any existing inbound links
- [ ] Canonical URLs + OG images correct per page
- [ ] **Positioning sweep at launch** — base.html's fallback meta /
      og: / twitter: descriptions and the Organization JSON-LD still
      say "fragmented permit data"; update to the "fragmented public
      records" line when the homepage ships (live index.html hero
      carries the old line too and is replaced at launch anyway)
- [ ] UTM-persistence script present on the new footer/pages
- [ ] Legal: Notion `Logo Use` cleared for every logo shown (footer +
      industry grids)

### Tracking / analytics integrity (design refresh — keep tracking intact)
- [x] No tracking code edited on the branch — VERIFIED vs `main`:
      `base.html` changed only the body-font line + footer include;
      `footer.html` (HubSpot embed + UTM script) and `gosquared.html`
      untouched; no GA/gtag changes. (Re-verify just before launch.)
- [ ] Re-confirm GA / GoSquared / HubSpot / UTM intact at launch
      (diff the final branch one more time)
- [ ] Newsletter: new footer form posts to the correct HubSpot
      endpoint (same list as the current embed)

### URL / link verification
- [ ] Every link resolves to the correct page — footer, top nav,
      in-page CTAs, cross-page links, blog — no 404s, correct targets
      after the `/solutions/` `/features/` moves + redirects
- [ ] No stale `-preview` URLs left in any link
- [ ] **Homepage interim links** — Data types cards point at KB
      articles (`docs.shovels.ai/.../data/*`) until the `/data/*` pages
      ship; repoint when those launch. Data delivery cards point at
      `/permit-database`, `/api`, `/data-feed`; repoint if those move
      under `/solutions/`

### Site-wide consistency & global impact
- [ ] **Rounded CTA rollout** — replace the old `rounded-md` primary
      buttons with the new `rounded-full` treatment across the whole
      site (~43 instances on ~21 live pages + `header.html` +
      `index.html`), not just the redesigned pages
- [ ] **Body font cascade** — confirm Scandia→system-stack body copy
      is intended on ALL pages (it already cascades site-wide via
      `base.html` + `input.css`), incl. untouched legacy pages
- [ ] Audit other shared changes for unintended reach: `tailwind.config.js`
      (marquee keyframes — additive, safe), shared macros/`sections`
      (preview-only today), `pelicanconf.py` globals (opt-in)
- [ ] Spot-check a few untouched pages (e.g. /about, /terms) render
      unchanged except the intended global typography

### Sign-off
- [ ] Staging deploy reviewed at real URLs by stakeholders
- [ ] Mobile QA — top nav (mobile menu), footer (accordions, no
      newsletter), and every redesigned page on a real device / narrow
      viewport
- [ ] Final go/no-go

### More (your ideas)
- [ ] _(add here — tell Claude or edit directly)_

### Explicitly post-launch (not blocking this wave)
- [ ] Data section pages: Permits, Decisions, Contractors, Residents,
      Properties → then add the Data column links + nav entry
- [ ] Net-new pages: Map Gallery, Brand, Partners, Pricing(?)

---

## Open decisions / parking lot

- **Footer & nav deploy timing** — backward-compatible now, or coupled
  with the page launch? (Leaning coupled, since they cross-reference.)
- **Homepage launch mechanics** — convert `index.html` to use the
  preview content; reconcile `STATS`/helper globals and the `dates`
  blog loop (preview uses `get_recent_articles`).
- **Data delivery options layout** — `data-delivery-options-preview`
  holds three live directions (current dark/illustration, dark bordered
  cards w/ "best for" tag, light numbered tiers) for designer sign-off.
  Once a direction is chosen: fold it into the homepage section, drop
  the other two, and delete the comparison page.
- **Which net-new pages** are in scope for Phase 5, and their copy.
- **Solutions/Features URL moves + redirects** — moving 6 pages under
  `/solutions/` and `/features/` needs: updated `Slug:` per page,
  repointed internal links/CTAs, and old→new redirects. New
  workstream; sequence it with the launch.
- **Audiences** — deprecate, keep unlinked, or relocate? Not in the
  new nav.
- **Data section** — all-new pages, post-launch. Footer/nav for the
  *this-wave* launch likely omit Data until those pages exist.
- **Net-new pages** (Map Gallery, Brand, Partners, Pricing?) — scope,
  copy, and cadence TBD; launch independently.
- **Stale `main`** — this branch is now well behind `main` (blog posts,
  telecom copy edits merged). Plan a rebase/merge before launch.
- Trinh Insurance logo; designer logo-height pass; white-on-hover
  logos (Hawkins, Avenue Roofing) — minor, deferred.
