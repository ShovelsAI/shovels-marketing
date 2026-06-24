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
| Footer | **Global** | 🟡 preview built | New `footer-refresh.html` (6 columns: Industries/Solutions/Features/Data/Resources/Company, left newsletter, mobile accordions w/ carats, newsletter hidden on mobile, slim bottom bar). DRY `footer_sections` data drives both mobile + desktop. Gated in `base.html` to `*-preview` pages only — live footer untouched. HubSpot form wired ✓. Decided: drop the DATA column at launch (pages won't be ready); restore when /data/* ships. Open: final link/column curation |
| Top nav (header) | **Global** | 🟡 preview built | New `header-refresh.html` (Industries/Solutions/Features/Resources + Sign In/Get Started; **Data omitted** until those pages ship). DRY `nav_menus` data drives desktop mega-dropdowns + mobile accordions. Dropdowns are icon link columns + Contact Sales row, two balanced columns at ≥6 items; open on hover (and on focus for keyboard users); caret flips up, panel beak points to trigger (seam-merged with the panel border), rightmost menu right-anchored; rounded-full Get Started. Gated in `base.html` to `*-preview` pages — live header untouched. Open: Solutions/Features links use planned `/solutions/` `/features/` slugs (404 until moved); promo panel intentionally dropped; icons are Lucide stand-ins |
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
Map Gallery (built behind `features/gis/gallery-preview` — six live
Esri ArcGIS embeds; the GIS hero's secondary CTA target), Brand,
Partners, Pricing (tentative). Build behind `hidden`; launch
independently.

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

## Launch runbook — exactly what must happen to go live

The launch is one coupled deploy, but several gates must be green first.
In order:

### Gate 0 — Merge unblock (NEW; hard blocker, settle this first)
The refresh branch requires **verified-signature** commits, but `main`
carries unsigned commits, so a normal branch↔`main` sync/merge is
rejected by the repository ruleset (`GH013`: "Commits must have verified
signatures"). The JSON-LD fix was **cherry-picked in as a signed
stopgap**, but the **final branch→`main` merge at launch will hit the
same wall.** An admin must resolve this before launch — either grant a
ruleset **bypass** for the launch merge, or **scope/adjust** the
verified-signatures rule. Without it, nothing ships. (Review:
`github.com/ShovelsAI/shovels-marketing/rules`.)

### Gate 1 — Everything green on the branch (the NOW + PREP work)
- All preview pages approved — designer walkthroughs, FAQ accuracy,
  **zero TBDs** (only the GIS "how it works" step maps remain)
- Rounded-CTA rollout done; blog-sidebar newsletter form restyled
- Redirects authored + homepage `index.html` migration drafted (PREP)
- Mobile QA passed; staging deploy reviewed by stakeholders at real URLs
- Branch synced with `main` (depends on Gate 0)

### The flip — one coupled deploy (interdependent; ship together)
1. **Slug swaps**: industry `*-preview` → live (drop `-preview` +
   `status: hidden`, delete legacy file); Solutions → `/solutions/*`;
   Features → `/features/*`; promote Insurance + Research.
2. **Homepage**: move preview content into theme `index.html` (reconcile
   `STATS`/helper globals + the `dates` vs `get_recent_articles` blog loop).
3. **Un-gate chrome**: promote `footer-refresh`/`header-refresh` → global
   (remove the `-preview` gate); drop the footer DATA column; repoint the
   header Solutions/Features links (they resolve once pages move); final
   header icons.
4. **Repoint interim links**: Solutions/Features cross-sell CTAs, homepage
   data-type/delivery links, and the GIS hero CTA
   (`/features/gis/gallery-preview` → `/features/gis/gallery`).
5. **Enable redirects**: 301s for all 6 moved pages (`/permit-database`,
   `/api`, `/data-feed`, `/charlie`, `/gis`, `/cli`) + the
   `charlie.shovels.ai` subdomain → `app.shovels.ai`. (Redirects ARE
   needed — earlier "none needed" assumed industry-only, slugs-unchanged.)
6. **Positioning sweep**: `base.html` fallback meta/OG/Twitter + the
   Organization JSON-LD ("fragmented permit data" → "fragmented public
   records").
7. **Build**: `make publish` → regenerate `sitemap.xml` (confirm the
   `sitemap` plugin is present in the deploy env).

### Right after the flip — verify
- Every link resolves (no 404s, no stale `-preview`); redirects 301 correctly
- Sitemap lists the new `/solutions/*` `/features/*` + net-new pages and
  excludes hidden/preview; **resubmit in Google Search Console**
- Tracking intact — final diff of GA / GoSquared / HubSpot / UTM
- Spot-check untouched pages render unchanged except intended typography
- Future pages (Data, Brand, Partners, Pricing) launch later on their own
  cadence; add to nav/footer as each ships

A **staging deploy** of the whole branch at real URLs before flipping
production is strongly recommended given the scope.

---

## Global changes that reach unrefreshed pages

This refresh is mostly new/redesigned pages staged behind `-preview`
slugs, but a few decisions cascade to the **untouched** live pages
(blog, `/about`, `/terms`, careers, audiences, etc.). Consolidated here
so none are missed. Status: ✅ already live on the branch · 🔧 decided,
work pending · 🔗 launch-coupled.

1. **Body font — Scandia → system stack** ✅
   In `base.html` + `input.css`, **ungated**, so every page already
   renders body copy in the system font on this branch (headings keep
   Scandia). Ships at merge. *Pre-launch:* spot-check a few legacy pages
   render cleanly (e.g. `/about`, `/terms`, a blog post).

2. **Global chrome (header + footer)** 🔗
   Promoting `header-refresh` / `footer-refresh` (dropping the
   `-preview` gate in `base.html`) swaps nav + footer on **every** page.
   Launch-coupled — the new nav links to `/solutions/*` `/features/*`,
   which must exist first.

3. **URL moves + inbound links** 🔧🔗
   Solutions → `/solutions/*`, Features → `/features/*`. ~72 internal
   links across `content/` + `themes/` — in ~32 blog posts — point at the
   old URLs (`/permit-database` ×29, plus `/api`, `/data-feed`,
   `/charlie`, `/gis`, `/cli`; a mix of absolute `shovels.ai/...` and
   `{{ SITEURL }}/...`). Needs old→new **redirects** (safety net) and
   ideally **repointing**. See the site-wide inbound-link audit item.

4. **Rounded CTA rollout** 🔧
   `rounded-md` → `rounded-full` primary buttons site-wide (~43 primary
   buttons across ~21 live pages + `header.html` + `index.html`), to
   match the refreshed pages. Includes:
   - **Blog sidebar newsletter subscription form** — restyle to the new
     rounded-button treatment, matching the refreshed footer subscribe
     form.

5. **Positioning sweep — `base.html` fallback meta + JSON-LD** 🔧
   Fallback `meta` / `og:` / `twitter:` descriptions and the
   Organization JSON-LD still say "fragmented permit data"; update to
   "fragmented public records." Affects the default snippet on every
   page that doesn't set its own.

**Contained — does NOT reach unrefreshed pages:** the coverage-include
copy change, the new macros (`callout` / `code_window` / `how_it_works`),
the marquee keyframes, and the `pelicanconf` STATS / article helpers —
all preview-only or additive/opt-in.

**Safe to do before launch (no sequencing dependency):** the positioning
sweep, the rounded-CTA rollout (incl. the blog sidebar newsletter form),
drafting the redirect map from the link audit, and the legacy-page
spot-check. **Launch-coupled:** header/footer promotion and activating
the redirects.

---

## Pre-launch checklist

The go/no-go list. Tick items as they're done; add your own under
"More (your ideas)". Nothing here is a one-way door until the final
production deploy, so we can keep iterating on the branch.

### Sequencing: do now vs. at launch
Shrink launch day to just the *flip*. Everything below is one of:
**NOW** (do anytime on the branch) · **PREP** (build now, enable at
launch) · **LAUNCH** (coupled to the go-live deploy) · ✅ done.

**NOW — front-load these (decoupled from launch):**
- Rounded-CTA rollout + blog-sidebar form restyle (biggest single reducer)
- ✅ Inbound-link audit run — targets live in ~15 blog posts + the live
  chrome; redirects will cover them, so direct repoint is optional
- Branch rebase on `main` (after PR #146 merges, to pick up the JSON-LD fix)
- FAQ accuracy review + blog pull-in category/tag check
- Designer passes (8 industry, homepage, Research), logo sourcing/heights,
  white-on-hover logos, Trinh Insurance logo (4/4)
- Verifications: meta descriptions, canonical/OG, UTM script, FAQ JSON-LD,
  trial `make publish`
- Cleanups: drop footer DATA column, final header icons, delete
  `data-delivery-options-preview.md`, legal logo clearance
- Body-font cascade + shared-change reach audit + spot-check untouched pages
- Mobile QA + stand up staging for stakeholder review

**PREP now → enable at launch:**
- Author the 301s (6 moved pages + `/charlie` + the `charlie.shovels.ai`
  subdomain) so launch just switches them on
- Draft the homepage `index.html` migration (STATS/helpers + blog-loop reconcile)

**LAUNCH only — the flip:**
- Slug swaps (industry + Solutions `/solutions/*` + Features `/features/*`),
  drop `status: hidden`, delete legacy files
- Promote Insurance + Research; move homepage content into theme `index.html`
- Un-gate the chrome (promote `footer-refresh`/`header-refresh` → global)
- Redirects go live + repoint interim links (Solutions/Features/homepage cross-links)
- Regenerate + resubmit sitemap, positioning sweep, final tracking diff,
  full link verification (no 404s / no stale `-preview`), go/no-go

**Open dependency:** GIS "how it works" step maps (3 TBDs) — left as TBD
for now; revisit before launch.

### Content & pages
- [ ] Designer walkthrough of all 8 industry preview pages
- [ ] Designer walkthrough of homepage preview
- [ ] Research page reviewed (UC1 framed vs unframed call confirmed)
- [ ] Trinh Insurance logo sourced → Insurance grid 4/4
- [ ] Logo heights tuned across all grids (designer pass)
- [ ] White-on-hover logos resolved or accepted (Hawkins, Avenue Roofing)
- [ ] Every page renders with no `TBD` placeholders
- [ ] FAQ accuracy review — read every FAQ question and answer on each
      page and verify claims are current and correct (coverage numbers,
      product names, pricing/delivery details, links)
- [ ] Blog pull-ins use the correct category/tag combo per page —
      each industry page's `get_industry_articles('<Category>')` matches
      its industry (and resolves enough posts), and the homepage pulls
      most-recent via `get_recent_articles`. Confirm Research has a
      blog pull (no `get_industry_articles` call found yet)

### URLs, routing & redirects
- [ ] Move Solutions pages to `/solutions/*` (permit-database, api, data-feed).
      All three redesign previews built: `permit-database-preview.md`
      (Shovels Online), `api-preview.md` (Shovels API), and
      `data-feed-preview.md` (Shovels Enterprise). Promote each (slug →
      `solutions/<name>`, drop `status: hidden`), delete the legacy
      `permit-database.md` / `api.md` / `data-feed.md`, add old→new
      redirects. Promoting `data-feed` also resolves the API page's
      Enterprise cross-sell link (`/solutions/data-feed`)
- [ ] Move Features pages to `/features/*` (charlie, gis, cli)
- [ ] Old → new redirects for all 6 moved pages
- [ ] **Charlie now lives in Shovels Online** — redirect the entire
      `https://charlie.shovels.ai/` subdomain to `https://app.shovels.ai/`,
      and point all Charlie page CTAs at `app.shovels.ai` (the
      `/features/charlie` page is marketing only; the product is in the
      app). Also 301 the old `/charlie` → `/features/charlie`. Audit for
      any `charlie.shovels.ai` links in content/themes during the
      site-wide inbound-link sweep
- [ ] Repoint internal links/CTAs to new URLs (footer, nav, cross-page, blog)
- [ ] **Site-wide inbound-link audit** — before launch, grep the entire
      repo for every internal link to a page that is moving or being
      replaced, so no reference is missed when we add redirects/repoint.
      Don't rely on the obvious sources — check ALL of them:
      - `content/posts/*` blog articles (often link to `/api`,
        `/permit-database`, `/data-feed`, `/charlie`, `/cli`, `/coverage`,
        industry pages)
      - other Solutions/Features pages, all Industry pages, Audiences,
        Research, Data Dictionary, Coverage, About/Careers/Contact
      - footer + nav (refresh chrome) and the SOC 2 / coverage includes
      - JSON-LD blocks and meta/canonical/OG URLs in `base.html`
      Method: `grep -rn` for each old slug (e.g. `/permit-database`,
      `/api`, `/data-feed`, `/charlie`, `/gis`, `/cli`) across `content/`
      and `themes/`, build the full list, then confirm each is either
      repointed or covered by a redirect. Re-run the grep after repointing
      to prove zero stragglers remain.
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
- [ ] Footer: **remove the DATA column for launch** — designed with it
      in, but the /data/* pages likely won't be ready for the initial
      launch (decided 2026-06-11; double-check before shipping). Restore
      the column when the Data pages go live (post-launch item below)
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
- [x] FAQ `FAQPage` JSON-LD renders on every industry page (verified:
      all 14 FAQ pages emit valid `FAQPage` JSON-LD on the production build)
- [ ] **Sitemap reflects the new IA** — after the slug swaps + un-hiding,
      regenerate `sitemap.xml` (auto-built by the `sitemap` plugin on
      `make publish`) and confirm it: (a) includes every net-new page
      (Map Gallery `/features/gis/gallery`, Research, Insurance, …),
      (b) lists the new `/solutions/*` and `/features/*` URLs — not the
      old flat slugs (`/permit-database`, `/api`, `/data-feed`, `/charlie`,
      `/gis`, `/cli`) or any `-preview` slug, and (c) excludes anything
      still `hidden`. Then resubmit the sitemap in Google Search Console
      so the moved URLs get recrawled and the old ones de-indexed via the
      301s.
- [x] Meta descriptions present on all launched pages (verified: 0
      missing across the full production build; also canonical + OG
      title/image present on every page)
- [ ] Branch synced with `main` — **blocked by the verified-signatures
      ruleset** (`main` has unsigned commits → `GH013` rejects the
      merge/push). The JSON-LD fix (PR #146) was cherry-picked in as a
      signed stopgap (`0f69a292`); the full sync + the final branch→`main`
      launch merge need an admin ruleset bypass/adjust first. See **Launch
      runbook → Gate 0**.

### SEO, analytics & legal
- [ ] Redirects preserve SEO equity for any existing inbound links
- [ ] Canonical URLs + OG images correct per page
- [ ] **Positioning sweep at launch** — base.html's fallback meta /
      og: / twitter: descriptions and the Organization JSON-LD still
      say "fragmented permit data"; update to the "fragmented public
      records" line when the homepage ships (live index.html hero
      carries the old line too and is replaced at launch anyway)
- [x] UTM-persistence script present on the new footer/pages (ported
      the utility from `footer.html` into `footer-refresh.html`; verified
      it renders on preview pages with no double-include)
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
- [ ] Delete `data-delivery-options-preview.md` (designer comparison
      scaffolding — Option 3 chosen and live on the homepage; kept
      around for reference until launch)
- [ ] **Homepage interim links** — Data types cards point at KB
      articles (`docs.shovels.ai/.../data/*`) until the `/data/*` pages
      ship; repoint when those launch. Data delivery cards point at
      `/permit-database`, `/api`, `/data-feed`; repoint if those move
      under `/solutions/`
- [ ] **Solutions page interim links** — cross-sell CTAs on the built
      Solutions previews point at not-yet-live targets:
      - Shovels Online (`permit-database-preview`): Charlie callout →
        `/charlie` (URL expected to change as that page is built); API
        callout → `/solutions/api` (404 until promoted)
      - Shovels API (`api-preview`): CLI callout → `/cli` (resolves
        today; moves to `/features/cli`); Enterprise callout →
        `/solutions/data-feed` (404 until page 3 ships)
      Confirm / repoint each when the target pages are finalized.
- [ ] **Features page interim links** — built Features previews point
      at not-yet-live targets:
      - GIS (`gis-preview`): hero secondary CTA "View map gallery" →
        `/features/gis/gallery-preview` (the staged gallery, so it's
        clickable in preview); **repoint to `/features/gis/gallery` at
        launch**. Enterprise callout → `/data-feed` (moves to
        `/solutions/data-feed`)
      - CLI (`cli-preview`): green callout → `/api` (moves to
        `/solutions/api`)
      - Charlie (`charlie-preview`): warm callout → Shovels Online
        (`/permit-database`, moves to `/solutions/permit-database`)
      Confirm / repoint each when the target pages are finalized.

### Site-wide consistency & global impact
- [x] **Rounded CTA rollout** — give the old `rounded-md` primary
      buttons the new `rounded-full` treatment. **Scoped to survivor
      pages only** — pages with no `-preview` replacement, so they stay
      live through launch. The 12 legacy industry/feature pages +
      `index.html` + `header.html` are skipped (replaced at launch by
      their `-preview` / `*-refresh` versions, which already use
      `rounded-full`), to avoid churning files that get deleted.
      Survivor pages (16 CTA buttons total):
      `about.md`, `contact.md`, `contact-research.md`, `audiences.md`
      (pending the Audiences keep/deprecate decision),
      `solutions-policy-research.md`, `solutions-asset-management.md`,
      `solutions-acquisition.md`, `solutions-sister-city-tracker.md`,
      `solutions-thesis-agent.md`.
      Treatment = full refresh button style: `rounded-full` + `px-6 py-3`
      + drop `shadow-sm` + `hover:bg-shovels-primary/90`. Staged on the
      branch; goes live with the launch deploy like everything else.
- [x] **Blog sidebar newsletter form restyle** — rounded-full pill input
      + solid green pill Subscribe button, matching the refreshed footer
      and the rounded-CTA treatment. Note: the real styling lived in the
      `.newsletter-form` rules in `input.css` (they override the inline
      classes in `article.html`), so both were updated. Site-wide across
      all blog posts; live at launch.
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
