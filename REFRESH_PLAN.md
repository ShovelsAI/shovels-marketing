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
| Footer | **Global** | 🟡 preview built | New `footer-refresh.html` (5 columns: Industry/Solutions/Features/Data/Resources, left newsletter, slim bottom bar). Gated in `base.html` to `*-preview` pages only — live footer untouched. Open: HubSpot form wiring, Data go-live handling, mobile treatment, final link/column curation |
| Top nav (header) | **Global** | ⬜ to do | Same: add Insurance + Research; refresh treatment; ships site-wide |
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
- **Footer** redesign (in progress) — add Insurance + Research, apply
  refresh treatment.
- **Top nav / header** redesign — same additions + treatment.
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

## Open decisions / parking lot

- **Footer & nav deploy timing** — backward-compatible now, or coupled
  with the page launch? (Leaning coupled, since they cross-reference.)
- **Homepage launch mechanics** — convert `index.html` to use the
  preview content; reconcile `STATS`/helper globals and the `dates`
  blog loop (preview uses `get_recent_articles`).
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
