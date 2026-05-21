# Shovels Marketing — Components & Design System

A living reference for the reusable building blocks used across the
Shovels marketing site, the decisions behind them, and the conventions
that keep them consistent.

This document is not the design source of truth — that's the
designer's Figma file and the accompanying spec PDF. This document
captures **implementation** and **decisions** that supplement the
designer's spec, including anything the spec leaves open.

---

## How to use this doc

- Designer's spec is canonical for *visual* design (color tokens,
  typography roles, spacing rhythm, hero patterns).
- This doc is canonical for *implementation* (macro signatures, file
  organization, component APIs, fallback values).
- When the spec and implementation diverge, the spec wins — update the
  implementation, then update this doc.
- When something isn't in the spec, decide here. Log the decision.

## Scope of change: industry pages vs site-wide

The Industry-page redesign is **the spearhead of the broader 2026 site
refresh**, but the intent is **not** to cascade every Industry-page
design decision across the entire site automatically. The other pages
(homepage, blog, audiences, careers, etc.) will be updated as part of
their own design rounds.

That said, some changes legitimately need to be global (typography
choices, brand color tokens, base CSS rules). Track those carefully
here so we know what's been intentionally cascaded vs. what stays
scoped to the new components.

### Global changes log

Every change that touches `base.html`, `input.css`, or otherwise
affects pages outside the Industry-page template should be logged
here with the reason and the date the decision was made. Append new
entries; don't rewrite old ones.

- **Body copy font: Scandia → system font stack.** Designer
  recommendation — brand identity is carried by headings; longer-form
  reading is calmer in a neutral web-oriented typeface. Headings
  (`h1`-`h6`, `dt`) explicitly retain Scandia via an `@layer base`
  rule in `input.css`. Affects every page on the site, including blog
  posts, homepage, audiences, careers. Decision is reversible by
  putting `'Scandia'` back into the `body` font-family in `base.html`
  inline CSS and `input.css` base layer.

---

## Tokens & colors

The designer's spec defines colors as CSS custom properties in oklch
(`--primary`, `--foreground`, `--muted-foreground`, etc.) consumed via
semantic Tailwind utilities (`bg-primary`, `text-foreground`).

The current site does not yet implement that token system. It uses
Tailwind's default palette plus a small custom `shovels-*` set defined
in `tailwind.config.js`. Components currently use:

| Role in spec | What we use today | Defined in |
|---|---|---|
| `bg-primary` / `text-primary` | `bg-shovels-primary` / `text-shovels-primary` | `tailwind.config.js` (`rgb(1 101 77 / <alpha-value>)`) |
| `bg-secondary` / `text-secondary` | `bg-shovels-secondary` (yellow) | `tailwind.config.js` (`#E9BE51`) |
| `text-foreground` | `text-gray-900` | Tailwind default |
| `text-muted-foreground` | `text-gray-500` | Tailwind default |
| `border-border` | `border-gray-200` | Tailwind default |

**Open architectural question**: whether to adopt the oklch token
system site-wide. See **Open questions** below.

### Raw hex values currently in components

A handful of components use raw hex literals because the designer
chose specific values that don't map cleanly to Tailwind's palette.
Each is documented in the relevant macro file.

| Value | Where | Purpose |
|---|---|---|
| `#111727` | `browser_frame` ring | Outer outline of the mock-up frame (near-black) |
| `#F26662` | `browser_frame` dot | Red traffic-light dot |
| `#F4DA86` | `browser_frame` dot | Yellow traffic-light dot |
| `#71A78C` | `browser_frame` dot | Green traffic-light dot |
| `#E1ECE9` | `browser_frame` backing | Offset backing rectangle (Shovels sage) |

When the token system lands, these become CSS variable references.

---

## Section padding convention

Every middle section uses `py-24` (96px top and bottom) per the design
spec. The gap between any two stacked sections is therefore ~192px,
which the designer prefers for a clean visual chapter break.

| Section | Padding | Notes |
|---|---|---|
| `hero` | `pt-20 pb-24 md:pt-28 md:pb-32` | First section, owns its full vertical balance |
| `soc2_trust` | `pb-8` only | Hugs the hero; reads as a continuation rather than a new section |
| Middle sections | `py-24` | Use cases, enterprise teams, coverage, resources, FAQ, final CTA — all the same |

The middle-section rule applies to both content-bearing macros
(`use_case_section`, `faq_section`, etc.) and static includes
(`sections/coverage.html`, `sections/enterprise_teams.html`).

## Spacing rhythm

Per the designer's spec — using Tailwind's 4px scale.

| Where | Class | Computed |
|---|---|---|
| Section container max width | `max-w-6xl` | 1152px |
| Section horizontal padding | `px-6 md:px-10` | 24px / 40px |
| Section vertical padding | `py-24` | 96px |
| Hero vertical padding | `pt-20 pb-24 md:pt-28 md:pb-32` | 80→112 / 96→128px |
| Use cases — heading to first case | `mt-16` | 64px |
| Use cases — between cases | `space-y-24` | 96px |
| Use case — text/image columns gap | `gap-10 md:gap-16` | 40px / 64px |
| Bullets list | `space-y-3` | 12px |
| Eyebrow → H2 | `mt-4` | 16px |
| H2 → lead paragraph | `mt-6` | 24px |
| CTA card padding | `p-10 md:p-16` | 40px / 64px |
| Card / button radius | `rounded-2xl`, `rounded-3xl`, `rounded-full` | 16, 24, full |

---

## Typography

**Headings**: Scandia webfont, applied globally to `h1`-`h6` and `dt`
via input.css `@layer base`. All headings render at weight 500
(`font-medium`) — the next-lightest Scandia weight available below
Bold (700). Scandia does not include a Semibold (600) file; using
`font-medium` is the designer-approved choice.

**Body copy**: system sans stack — `system-ui, -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, ...`. Per the designer, the
brand identity is carried by the headings; longer-form reading is
calmer in a neutral web-oriented typeface. Applied globally on `body`
via input.css.

| Element | Tailwind classes |
|---|---|
| Hero H1 | `text-4xl md:text-6xl font-medium tracking-tight` |
| Section H2 | `text-3xl md:text-4xl font-medium tracking-tight` |
| Use case H3 | `text-2xl md:text-3xl font-medium tracking-tight` |
| Eyebrow chip | `text-xs font-medium uppercase tracking-wider` |
| Use case index ("01", "02") | `text-sm font-mono text-gray-500` |
| Body / lead | `text-base text-gray-500` or `text-lg text-gray-500` |
| Bullets | `text-sm text-gray-900/90` |
| Mock-up caption | `text-xs italic text-gray-500` |

### Inline link convention

Inline anchor tags inside body copy (e.g., links in Coverage bullets,
the "View all posts" link in Resources) use:

```
text-shovels-primary hover:text-shovels-primary/80 hover:underline
```

Green color signals "this is a link" by default; the underline only
appears on hover. Cleaner default state per designer.

### Hero eyebrow convention

Industry-page hero eyebrows use the bare industry name in uppercase
(rendered automatically by the chip's `uppercase` class).

- Insurance → `eyebrow='INSURANCE'`
- Real Estate → `eyebrow='REAL ESTATE'`
- Climate → `eyebrow='CLIMATE'`
- Construction Tech → `eyebrow='CONSTRUCTION TECH'`
- etc.

No "FOR" prefix — the industry context is implicit.

### Headline weight history

The design spec originally called for `font-semibold` (600). Scandia
Web (both self-hosted and Adobe Fonts) does not ship a 600-weight file
— only 400, 500, and 700 — so `font-semibold` was silently falling
back to Bold (700) and rendering heavier than the designer intended.
After confirming the designer's intent was a lighter feel, the
canonical heading weight is now `font-medium` (500). If Scandia
Semibold is later licensed and self-hosted, all heading classes can
flip back to `font-semibold` in one pass.

---

## Components

### `browser_frame` macro

**Location**: `themes/shovels/templates/macros/mockup.html`

Wraps a product screenshot in a browser-style chrome (traffic-light
dots + title bar) with an offset sage-green backing rectangle behind
the frame.

#### Signature

```jinja
browser_frame(src, alt,
              title='Shovels.ai',
              max_width='max-w-5xl',
              offset='translate-x-3 translate-y-3',
              image_padding='p-[30px]',
              wrapper_class='')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
| `src` | _required_ | Image path, e.g. `/images/industries/insurance/uc1.png` |
| `alt` | _required_ | Alt text for accessibility |
| `title` | `'Shovels.ai'` | Text in the chrome title bar |
| `max_width` | `'max-w-5xl'` | Tailwind max-w-* class. Pass `''` to let parent control width |
| `offset` | `'translate-x-3 translate-y-3'` | How far the backing rectangle sits down/right (default 12px) |
| `image_padding` | `'p-[30px]'` | Internal padding around the image — designer-approved value |
| `wrapper_class` | `''` | Extra classes on the outer wrapper |

#### Basic usage

```jinja
{% import 'macros/mockup.html' as ui %}

{{ ui.browser_frame('/images/industries/insurance/uc1.png',
                    'Underwriting view in Shovels') }}
```

#### Inside a two-column grid (parent controls width)

```jinja
<div class="grid grid-cols-1 md:grid-cols-2 gap-10">
  <div>...copy...</div>
  <div>
    {{ ui.browser_frame('/images/industries/insurance/uc1.png',
                        'Underwriting view',
                        max_width='') }}
  </div>
</div>
```

#### What the macro renders

1. An outer wrapper (`max_width` + any `wrapper_class`).
2. A relative-positioned container holding two siblings:
   - An offset backing rectangle (`#E1ECE9`, 12px down/right by default).
   - A foreground frame with white background, dark outline (`#111727`),
     traffic-light dot chrome (`#F26662`, `#F4DA86`, `#71A78C`), and
     the image wrapped in 30px padding.

---

### `hero` macro

**Location**: `themes/shovels/templates/macros/hero.html`

Top-of-page hero for Industry pages: eyebrow chip, H1, lead paragraph,
primary CTA button, and a side illustration. A subtle crossing-gradient
grid pattern with a radial fade sits behind the content (per the design
spec).

#### Signature

```jinja
hero(eyebrow, h1, description, illustration_src, illustration_alt,
     cta_label='Get started',
     cta_href='https://app.shovels.ai/signup/',
     illustration_position='right')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
| `eyebrow` | _required_ | Small uppercase label above the H1 (e.g. `'STRATEGIC INSIGHTS'`) |
| `h1` | _required_ | Hero headline |
| `description` | _required_ | One- or two-sentence lead paragraph below the H1 |
| `illustration_src` | _required_ | Path to the SVG illustration (typically in the industry folder) |
| `illustration_alt` | _required_ | Alt text |
| `cta_label` | `'Get started'` | Button text |
| `cta_href` | `'https://app.shovels.ai/signup/'` | Button destination. Canonical signup URL, shared with `final_cta` |
| `illustration_position` | `'right'` | `'right'` or `'left'` |

#### Example

```jinja
{% import 'macros/hero.html' as ui_hero %}

{{ ui_hero.hero(
    eyebrow='STRATEGIC INSIGHTS',
    h1='Property intelligence for insurance providers',
    description='Underwrite with verified property data…',
    illustration_src='/images/industries/insurance/hero.svg',
    illustration_alt='Insurance hero illustration') }}
```

#### Notes

- **Grid background**: two crossing CSS gradients (1px lines, 56px cells)
  with a radial mask that fades the pattern toward the edges. Line color
  is `#ebf0ed` (approximates the spec's `--grid-line` token). The section
  must be `position: relative` for the absolute grid layer.
- **Section padding**: `pt-20 pb-24 md:pt-28 md:pb-32` per spec.
- **Typography**: H1 is `text-4xl md:text-6xl` per spec.

---

### `soc2_trust` macro

**Location**: `themes/shovels/templates/macros/soc2_trust.html`

Horizontal trust banner with the AICPA SOC 2 seal, heading, body, and a
link CTA on the right. Sits between the hero and the use cases section
on every Industry page.

#### Signature

```jinja
soc2_trust(heading, body,
           cta_label='Read more about our security practices →',
           cta_href='https://trust.shovels.ai/')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
| `heading` | _required_ | One-liner like "Shovels is SOC 2® Type II certified" — typically same across industries |
| `body` | _required_ | Industry-specific descriptive paragraph |
| `cta_label` | `'Read more about our security practices →'` | Link text |
| `cta_href` | `'https://trust.shovels.ai/'` | Link destination |

#### Example

```jinja
{% import 'macros/soc2_trust.html' as ui_soc2 %}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise insurance carriers...') }}
```

#### Notes

- **Heading vs. body**: per the Notion source of truth, the heading is
  consistent across Industry pages but the body varies by audience.
- **Badge**: the SOC 2 seal at `/theme/images/soc2-seal.png`. Rendered
  at `size-16` (64px).
- **Background**: soft green `#F9FCFB` (per designer). Reads as a
  trust-tinted card rather than a neutral gray notice.
- **Layout**: horizontal on `md+`, stacked on mobile.

---

### `use_case_section` macro

**Location**: `themes/shovels/templates/macros/use_case.html`

Renders a full "Use Cases" section for an Industry page — eyebrow chip,
section heading, optional intro paragraph, and an alternating set of
two-column rows (text/image) for each use case.

#### Signature

```jinja
use_case_section(eyebrow, heading, cases, intro=None)
```

#### Parameters

| Parameter | Type | Notes |
|---|---|---|
| `eyebrow` | string | Small uppercase label above the heading (e.g. `'USE CASES'`) |
| `heading` | string | The section H2 |
| `cases` | list of dicts | One entry per use case, see structure below |
| `intro` | string (optional) | Lead paragraph below the heading |

#### Each case dict

| Key | Required | Notes |
|---|---|---|
| `number` | yes | Label like `'01'`, `'02'` — renders as monospace gray |
| `title` | yes | Use case heading (H3) |
| `description` | yes | One- or two-sentence body |
| `bullets` | no | List of strings; each renders with a check badge |
| `image_src` | yes | Path to the screenshot or illustration |
| `image_alt` | yes | Alt text |
| `framed` | no | Default `True` — image renders inside the browser_frame chrome. Set `False` for non-screenshot imagery like illustrations |
| `caption` | no | Small italic caption rendered below the image |

#### Example usage

```jinja
{% import 'macros/use_case.html' as ui %}

{% set insurance_cases = [
    {
        'number': '01',
        'title': 'Underwrite what was actually built',
        'description': 'Permit records show exactly what was built…',
        'bullets': [
            'Flag aging roofs and high-risk properties',
            'Verify contractor licenses with standardized CSL data',
        ],
        'image_src': '/images/industries/insurance/uc1-underwrite.png',
        'image_alt': 'Underwriting view in Shovels',
    },
    {
        'number': '02',
        'title': 'Generate insurance leads from permit activity',
        'description': 'Reach contractors and homeowners…',
        'bullets': ['…'],
        'image_src': '/images/industries/insurance/uc2-leads.png',
        'image_alt': 'Lead generation view',
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What insurance teams can do with Shovels',
    cases=insurance_cases) }}
```

#### Alternation behavior

The macro alternates image position by `loop.index`:

- Case 1 (index 1, odd): text-left, image-right
- Case 2 (index 2, even): image-left, text-right
- Case 3: text-left, image-right
- …and so on.

Page authors don't pass an `image_position` parameter — alternation is
handled internally. To reorder cases visually, reorder the list.

#### Eyebrow chip

The eyebrow renders as a pill (rounded-full border at 20% opacity of
brand green, background at 5% opacity, text-shovels-primary). Per the
designer's spec.

#### Bullet check badge

Each bullet renders with a small circular badge (20×20, rounded-full,
`bg-shovels-primary/10`) containing a Lucide-style stroked Check icon
(12×12, `stroke-width="3"`, `text-shovels-primary`). 12px gap between
badge and bullet text. Per designer's spec (and added to the spec doc
after our review).

---

### `faq_section` macro

**Location**: `themes/shovels/templates/macros/faq.html`

Renders an expandable FAQ list using native `<details>`/`<summary>`
elements **and** a matching `FAQPage` JSON-LD schema block from the
same data. AI answer engines (Google, ChatGPT, Perplexity, etc.) read
the schema to surface Shovels content in answer-style results.

#### Signature

```jinja
faq_section(heading, items, intro=None)
```

#### Parameters

| Parameter | Type | Notes |
|---|---|---|
| `heading` | string | Section H2 |
| `items` | list of dicts | One entry per question, see below |
| `intro` | string (optional) | Short paragraph below the heading |

#### Each item dict

| Key | Notes |
|---|---|
| `q` | Question text |
| `a` | Answer text — **plain text only**, no markdown links (the schema's `Answer.text` field expects plain text) |

#### Example

```jinja
{% import 'macros/faq.html' as ui_faq %}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {'q': 'What data is included?',
         'a': 'Shovels data includes building permits...'},
        {'q': 'How is it delivered?',
         'a': 'You can access Shovels via our online platform...'},
    ]) }}
```

#### Notes

- **Single source of truth**: both the human-visible accordion and the
  FAQPage JSON-LD schema render from the same `items` list. Edit a
  question once and both stay in sync.
- **Accordion mechanism**: native `<details>`/`<summary>` — no JS
  dependency. The default disclosure marker is hidden via
  `[&::-webkit-details-marker]:hidden` + `list-none`.
- **Chevron**: `group-open:rotate-180` animates the chevron when the
  item opens.
- **AEO**: the JSON-LD block uses schema.org `FAQPage` with a
  `Question`/`Answer` pair per item. Keep answers plain text — rich
  text may not index cleanly.

---

### `resources_section` macro

**Location**: `themes/shovels/templates/macros/resources.html`

Renders a left-justified H2 heading with a "View all posts →" link
on the right, followed by a 3-up grid of blog-post cards (rounded
featured image + title, whole card clickable). Importance flows left
to right — the macro renders `articles` in the order it receives them.

#### Signature

```jinja
resources_section(articles,
                  heading='Related content',
                  view_all_url='/blog/',
                  view_all_label='View all posts →')
```

#### Parameters

| Parameter | Type | Notes |
|---|---|---|
| `articles` | list of dicts | One entry per card |
| `heading` | string | Default `'Related content'`. Renders as section H2 |
| `view_all_url` | string | Default `'/blog/'`. Destination for the upper-right link |
| `view_all_label` | string | Default `'View all posts →'`. Link text |

#### Each article dict

| Key | Notes |
|---|---|
| `url` | Blog post URL (e.g. `/blog/post-slug/`) |
| `title` | Post title |
| `image_src` | Path to the featured image |
| `image_alt` | Alt text for the image |

#### Example

```jinja
{% import 'macros/resources.html' as ui_res %}

{{ ui_res.resources_section(
    articles=[
        {
            'url': '/blog/roofing-permit-data-insurance-roof-age/',
            'title': "The Roof Age Problem: What Permit Data Reveals",
            'image_src': '/images/blog_images/roofing-permit-data-insurance-roof-age-hero.png',
            'image_alt': 'Aerial view of a neighborhood',
        },
    ]) }}
```

#### Notes

- **Filtering is the caller's responsibility.** This macro is
  intentionally agnostic about *which* articles appear. Pass the list
  in the order you want them shown.
- **Dynamic filtering is deferred.** The current Insurance preview
  hardcodes three insurance-relevant posts. The plan is to add a
  `pelicanconf.py` helper that filters by `tag2` (primary) and `tags`
  (secondary check), with a most-recent fallback. See **Open
  questions** below.
- **Card hover**: image scales 5% and title shifts to
  `text-shovels-primary` on hover. Whole card is one `<a>` link.
- **Image aspect ratio**: `aspect-video` (16:9), `object-cover` so any
  featured image fits cleanly.
- **Header layout**: H2 left, "View all posts →" link right (flex
  container with `justify-between`). Both align to the same baseline.
  The view-all link uses `underline-on-hover` per the inline-link
  convention.

---

### `final_cta` macro

**Location**: `themes/shovels/templates/macros/final_cta.html`

Closing CTA banner for every Industry page. Centered card with
heading, description, and a primary CTA button. Sits inside the same
`max-w-6xl` content area as other sections.

#### Signature

```jinja
final_cta(heading, description,
          cta_label='Get started',
          cta_href='https://app.shovels.ai/signup/')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
| `heading` | _required_ | The closing headline (e.g. "Ready to underwrite what was actually built?") |
| `description` | _required_ | One- or two-sentence supporting text |
| `cta_label` | `'Get started'` | Button text |
| `cta_href` | `'https://app.shovels.ai/signup/'` | Button destination — matches hero default |

#### Example

```jinja
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_cta.final_cta(
    heading='Ready to underwrite what was actually built?',
    description='See how permit and contractor data fits into your underwriting, claims, and growth workflows.') }}
```

#### Notes

- **Card**: `rounded-3xl`, tinted-primary background (`bg-shovels-primary/5`),
  thin primary-tinted border, `p-10 md:p-16` per spec.
- **Layout**: text and button center-aligned within the card.
- **Button**: rounded-full, primary background — matches hero CTA exactly.

---

## Static includes

Static includes are whole HTML chunks that get pulled into a page with
`{% include 'sections/<name>.html' %}`. They take no parameters — copy
is hardcoded inside the include file. Use them for sections that are
truly identical across pages; when content needs to vary, prefer a
macro instead.

### `sections/coverage.html`

**Location**: `themes/shovels/templates/sections/coverage.html`

The "Coverage across the U.S." section: light-background two-column
layout with eyebrow chip, heading, body paragraph, and two checkmarked
bullets containing inline links. The U.S. coverage illustration sits
in the right column.

#### Usage

```jinja
{% include 'sections/coverage.html' %}
```

Place after the "Built for enterprise teams" section.

#### Notes

- **Copy is hardcoded**, including the two inline-link bullets pointing
  to the coverage dashboard, release notes, and GIS layer page. Edit
  here once and every page that includes it updates.
- **Layout**: text-left / illustration-right on `md+`, single-column on
  mobile.
- **Bullets**: same circular check badge as `use_case_section`. Inline
  links use `text-shovels-primary underline` with a hover opacity dim.
- **Illustration**: `/images/illustrations/coverage-us.svg` — shared
  across all Industry pages.

---

### `sections/enterprise_teams.html`

**Location**: `themes/shovels/templates/sections/enterprise_teams.html`

The "Built for enterprise teams" dark section: full-bleed dark
background, left-aligned eyebrow chip + heading, 3-up grid of
icon + yellow title + description.

#### Usage

```jinja
{% include 'sections/enterprise_teams.html' %}
```

Place after the use-cases section in an Industry page.

#### Notes

- **Background**: `bg-shovels-dark` (`#101727`).
- **Eyebrow + heading**: left-aligned (not centered) — title aligns with
  the icons in the grid below.
- **Titles**: yellow (`text-shovels-secondary`) for accent against the
  dark background.
- **Descriptions**: `text-gray-300`.
- **Icons**: at `size-16` (64px). Source SVGs live in
  `content/images/illustrations/`.
- **Copy is hardcoded.** If/when this content needs to vary by industry,
  convert to a parameterized macro.

---

## File organization

### Image assets

```
content/images/
├── industries/
│   ├── building-materials/
│   ├── climate/
│   ├── construction-tech/
│   ├── home-services/
│   ├── insurance/          ← Insurance page-specific assets
│   ├── real-estate/
│   └── telecommunications/
└── illustrations/          ← Shared assets used on multiple pages
    ├── coverage-us.svg
    ├── enterprise-icon-ai-classified.svg
    ├── enterprise-icon-api-feed.svg
    └── enterprise-icon-updates.svg
```

Each folder slug matches the corresponding Pelican page slug, which in
turn matches the Notion `Slug` field for that industry (e.g.
`industries/climate/` ↔ `content/pages/climate.md` ↔ Notion slug
`/climate`).

**When to place where**:

- An asset used on **only one page** → that page's industry folder.
- An asset **shared across multiple pages** → `illustrations/`.

### Filename conventions

- All lowercase.
- Hyphens between words. No spaces. No underscores. No camelCase.
- Descriptive slugs, not bare numbers (`uc1-underwrite.png`, not `uc1.png`).
- Don't repeat folder context (`industries/insurance/uc1.png`, not
  `industries/insurance/insurance-uc1.png`).
- Extensions: `.svg` for illustrations and icons; `.png` for product
  screenshots; `.jpg` for photos.

### Page slugs

The folder name under `industries/` matches the Pelican page slug. The
page at `content/pages/insurance.md` references images at
`/images/industries/insurance/...`.

### Sandbox/preview pages

Sandboxes use `status: hidden` in their front matter. URL exists, but
they don't appear in nav. Delete or unhide when promoting to production.

| Page | URL | Purpose |
|---|---|---|
| `content/pages/mockup-test.md` | `/mockup-test` | Stress-test the `browser_frame` macro at varying widths and aspect ratios |
| `content/pages/insurance-preview.md` | `/insurance-preview` | Preview of the Insurance page as components come online |

---

## Decisions log

Architectural / design decisions we've made, with their rationale.
Append new entries; don't rewrite old ones.

### Offset backing rectangle instead of CSS `box-shadow`

The browser_frame uses a real `<div>` filled with `#E1ECE9` (sage) and
offset 12px down/right behind the frame, rather than a CSS box-shadow.

**Why**: a real shape reads identically on any page background (white,
gray, colored heroes). A box-shadow drops opacity for the soft fade,
which can vanish on dark or strongly colored backgrounds. The designer's
Figma also composes shadows this way.

### Code-controlled image padding (30px)

Screenshots are exported tight-cropped (no padding inside the file).
The frame adds 30px internal padding via `p-[30px]` on a wrapper div
around the `<img>`.

**Why**: one canonical value, change once site-wide. Smaller image
files. The same screenshot can be reused at different padding without
re-export. Designer signed off after comparing 15 / 30 / 60px samples.

### Stand-in for design tokens (deferred adoption)

We use `shovels-primary` and Tailwind defaults (`text-gray-900`, etc.)
as stand-ins for the spec's semantic tokens (`bg-primary`, `text-foreground`).

**Why**: adopting the oklch token system fully would require migrating
~25 existing pages or accepting a two-tone codebase for an indefinite
period. Decision deferred pending team input. See **Open questions**.

### `use_case_section` takes a list-of-dicts, not multiple macro calls

We chose `use_case_section(cases=[...])` over separate `use_case_open`
/ `use_case` / `use_case_close` macro calls.

**Why**: one call site per section, alternation handled internally,
adding/removing/reordering cases is a list edit. Tradeoff: the dict
structure is verbose, but it's the same structure every time.

### Bullet check badge styling

20×20 circular badge with `bg-shovels-primary/10`, containing a
Lucide-style stroked Check icon at 12×12 with `stroke-width="3"`.

**Why**: matches the designer's Figma. Originally missing from the
spec PDF — designer confirmed and is adding it to the spec.

---

## Open questions

Things deferred for team input.

### Adopt the spec's oklch token system?

The designer's spec is built around CSS custom properties in oklch.
We currently use a `shovels-*` palette + Tailwind defaults as a
translation. Three paths:

- **A**: Status quo. Stand-in translation; works fine, slow drift risk.
- **B**: Set up tokens for new pages only. Existing pages keep their
  current classes; new components use semantic names. Low-effort,
  introduces a transitional two-tone codebase.
- **C**: Full migration. Tokens for everything; rewrite all 25+ pages
  to semantic utilities. Highest effort, most consistent end state.

Awaiting team decision.

### Dynamic resources filtering (deferred)

The `resources_section` macro currently takes a hardcoded list of
articles. To make it dynamic per industry, we need:

1. A signal hook in `pelicanconf.py` that captures `generator.articles`
   when Pelican finishes processing them (signal:
   `article_generator_finalized`).
2. A helper function `get_industry_articles(tag, limit=3)` that filters
   captured articles by `tag2` (primary) and `tags` (secondary check),
   sorts by recency, and falls back to most-recent overall if no
   matches.
3. The helper exposed via `JINJA_GLOBALS` so the macro can call it
   from inside a content `.md` page.

Open sub-questions:

- **Canonical tag names per industry.** Insurance → `tag2: Insurance`
  is confirmed. Need to confirm the exact `tag2` value for each of:
  Real Estate, Climate, Telecommunications, Construction Tech,
  Building Materials, Home Services.
- **Sort order for matches.** Most recent first (default), or is there
  a "priority/featured" field somewhere?
- **Architectural sign-off** on modifying `pelicanconf.py` before any
  edit lands.

Reference: Notion taxonomy doc — Shovels Blog Categories & Tags.

### Eyebrow capitalization

Currently using uppercase (`USE CASES`, `STRATEGIC INSIGHTS`) per the
Figma. CSS adds `uppercase` regardless of source case, but content
typed in lowercase reads more naturally in the Notion DB. Decide: should
the Notion source be lowercase ("Use cases") and the CSS uppercase it,
or should both be uppercase?

### Whether to vendor Lucide icons

The bullet check badge uses an inline SVG version of Lucide's `Check`
icon. If we need more Lucide icons elsewhere, options are: keep inlining
(scales poorly past 3–4 icons), copy SVG sources into `themes/shovels/static/icons/`,
or add a Pelican plugin to embed by name. Decide when the count exceeds three.

---

## How to add a new component

1. Build the macro in `themes/shovels/templates/macros/<name>.html`.
   - Include a top-of-file docstring describing parameters and a basic
     example.
2. Reference the macro from a sandbox page (`/<name>-test` or similar)
   with placeholder data.
3. Run `npm run build:css:prod` and confirm new Tailwind classes
   compile. Reload `make devserver`.
4. Send screenshots to the designer for review. Iterate until approved.
5. Add the macro to this doc — signature, parameters, example, any
   non-obvious decisions.
6. Wire it into real pages when the designer signs off.

---

## How to add a new Industry page

1. Create the image folder at `content/images/industries/<slug>/`.
2. Drop in `hero.svg` and tight-cropped use-case screenshots.
3. Create the page at `content/pages/<slug>.md` with front matter
   metadata and a body that composes the macros (hero, use cases,
   coverage, FAQ, final CTA, etc.).
4. Use `status: hidden` and a unique slug while iterating; remove
   when ready to ship.
5. Copy is sourced from the "Industry Pages Copy" Notion database.
