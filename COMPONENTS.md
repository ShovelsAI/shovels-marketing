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

**Architectural decision**: we're staying on the `shovels-*` palette
+ Tailwind defaults indefinitely. The token system would be a one-day
search-and-replace if dark mode or multi-brand theming ever lands as
a real product requirement — until then, YAGNI. See Decisions log →
*"Stay on `shovels-*` palette; defer the oklch token system"*.

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
| `logo_strip` | `pb-24` only | Same hero-hugging pattern as `soc2_trust`. The hero's bottom padding provides all the breathing room above; the strip's own bottom padding separates it from the next section |
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

### Eyebrow convention

Eyebrow chips appear above the H2 in most sections (Use Cases, Data
Delivery, Coverage, etc.). The hero deliberately has no eyebrow — see
**Decisions log** → *"Hero eyebrow chip removed"*.

**Always write eyebrow text in ALL CAPS at the source** — both in
Notion copy and in macro/include calls. The CSS `uppercase` utility is
applied to the chip regardless, but writing the source in caps avoids
any drift between "what the writer typed" and "what renders." Examples
of correct source values:

- `USE CASES`
- `DATA DELIVERY`
- `COVERAGE`
- `STRATEGIC INSIGHTS`

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

Top-of-page hero for Industry and Solutions pages: H1, lead paragraph,
primary CTA button, and a side illustration. The text column and the
illustration column are equal width on `md+` (6/12 each). A subtle
crossing-gradient grid pattern with a radial fade sits behind the
content (per the design spec). The hero deliberately has no eyebrow
chip — see Decisions log.

#### Signature

```jinja
hero(h1, description, illustration_src, illustration_alt,
     cta_label='Get started',
     cta_href='https://app.shovels.ai/signup/',
     illustration_position='right')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
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
    h1='Property intelligence for insurance providers',
    description='Underwrite with verified property data…',
    illustration_src='/images/industries/insurance/hero.svg',
    illustration_alt='Insurance hero illustration') }}
```

#### Notes

- **No eyebrow**: per team decision. Other sections on the page still
  use eyebrow chips — only the hero opts out.
- **Column split**: `md:col-span-6` for both the text column and the
  illustration column. Equal split.
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

#### Recommended usage — dynamic per-industry articles

Industry and Solutions pages should pass the result of
`get_industry_articles(tag)` rather than hardcoding URLs. The helper
is exposed as a Jinja global from `pelicanconf.py` — see the
**`get_industry_articles` helper** section below for details and the
canonical `tag` values per industry.

```jinja
{% import 'macros/resources.html' as ui_res %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Insurance')) }}
```

#### Manual override (hardcoded list)

You can still pass an explicit list when curation matters more than
automation — e.g., a launch announcement page where the three featured
posts are chosen by hand.

```jinja
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

Explicit lists beat the helper — pass whichever shape works for the
page.

#### Notes

- **Filtering is the caller's responsibility.** This macro is
  intentionally agnostic about *which* articles appear. Pass the list
  in the order you want them shown.
- **Card hover**: image scales 5% and title shifts to
  `text-shovels-primary` on hover. Whole card is one `<a>` link.
- **Image aspect ratio**: `aspect-video` (16:9), `object-cover` so any
  featured image fits cleanly.
- **Header layout**: H2 left, "View all posts →" link right (flex
  container with `justify-between`). Both align to the same baseline.
  The view-all link uses `underline-on-hover` per the inline-link
  convention.

---

### `icons` macro module

**Location**: `themes/shovels/templates/macros/icons.html`

Vendored Lucide icons exposed as small parameterized Jinja macros.
Each macro takes a Tailwind `class` string (for size and color via
`currentColor`) and an optional `stroke_width` override. SVG markup is
build-time inlined, so there's no extra HTTP request per icon and no
JS dependency.

#### Usage

```jinja
{% import 'macros/icons.html' as icons %}

{{ icons.check(class='size-3 text-shovels-primary', stroke_width=3) }}
{{ icons.chevron_down(class='size-5 text-gray-400') }}
```

#### Currently vendored

| Icon | Macro | Used by |
|---|---|---|
| Lucide `check` | `icons.check(class, stroke_width=2)` | `use_case_section` bullet check badges (passes `stroke_width=3` for the heavier look) |
| Lucide `chevron-down` | `icons.chevron_down(class, stroke_width=2)` | `faq_section` accordion (uses `group-open:rotate-180` on the class to animate on open) |

#### Parameters (all macros)

| Parameter | Default | Notes |
|---|---|---|
| `class` | `'size-5'` | Tailwind class string. Use `size-*` to set the icon size and `text-*` to color via `currentColor`. Animation utilities (e.g., `group-open:rotate-180`, `transition-transform`) compose normally. |
| `stroke_width` | `2` | Lucide's default. Pass `3` for a heavier look (matches the bullet check badge's spec'd visual). |

#### How to add a new icon

1. Go to <https://lucide.dev/icons/> and find the icon you need.
2. Click **Copy SVG** to get the raw SVG markup.
3. Open `themes/shovels/templates/macros/icons.html` and add a new
   macro at the bottom following the existing pattern:
   - Macro name = Lucide icon name in `snake_case`
   (e.g., `arrow_right`, `shield_check`).
   - Replace the SVG's hard-coded `class` with `class="{{ class }}"`.
   - Replace the hard-coded `stroke-width` with `stroke-width="{{ stroke_width }}"`.
   - Keep `aria-hidden="true"` on purely decorative icons; remove it
     and add a `<title>` element if the icon conveys standalone
     meaning.
4. Document the new icon in the **Currently vendored** table above.
5. Call it from your template: `{{ icons.<name>(class='size-* text-*') }}`.

#### Notes

- **Visual consistency**: all macros share the Lucide attribute set
  (`viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`,
  rounded line caps + joins), so icons of different sizes still read
  as a coherent family.
- **Why macros over SVG sprite or plugin**: see Decisions log →
  *"Lucide icons as Jinja macros"*.

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

### `logo_strip` macro

**Location**: `themes/shovels/templates/macros/logo_strip.html`

Infinite-scrolling customer logo marquee ("Trusted by teams at"),
modeled on streamyard.com's strip. Ships **full-color** logo files;
the flat-grey treatment is applied at render time with a CSS filter
(`brightness(0) invert(0.7)`), so logos never need greyscale
pre-processing. Logos regain full color on hover, and the marquee
pauses while hovered.

#### Signature

```jinja
logo_strip(logos,
           heading='TRUSTED BY TEAMS AT',
           grey=0.7,
           duration='40s',
           wrapper_class='')
```

#### Parameters

| Parameter | Default | Notes |
|---|---|---|
| `logos` | _required_ | List of logo dicts, see below. Order = display order |
| `heading` | `'TRUSTED BY TEAMS AT'` | Centered uppercase label above the strip. ALL CAPS at the source per the eyebrow convention |
| `grey` | `0.7` | Grey level: `0` = black, `1` = white. `0.7` ≈ `#B3B3B3` (StreamYard's value). Designer may tune |
| `duration` | `'40s'` | Time for one full loop. Lower = faster |
| `wrapper_class` | `''` | Extra classes on the `<section>` |

#### Each logo dict

| Key | Required | Notes |
|---|---|---|
| `src` | yes | Path under `/images/logos/`, e.g. `'/images/logos/aws.svg'` |
| `alt` | yes | Company name |
| `height` | no | Display height in px, default `30`. See *height tuning* below |

#### Example

```jinja
{% import 'macros/logo_strip.html' as ui_logos %}

{% set customer_logos = [
    {'src': '/images/logos/aws.svg', 'alt': 'AWS', 'height': 34},
    {'src': '/images/logos/google.svg', 'alt': 'Google'},
    {'src': '/images/logos/oracle.svg', 'alt': 'Oracle', 'height': 22},
] %}

{{ ui_logos.logo_strip(logos=customer_logos) }}
```

#### How to swap a logo in or out (the fast path)

Logos are expected to rotate as customers come and go. The process:

1. **Get the logo file.** Best sources in order: Wikimedia Commons
   (official SVGs for recognizable brands), the company's press/brand
   page, or an inline SVG extracted from their site header. Prefer SVG;
   PNG is fine for raster-only brands.
2. **Clean it.** Tight-crop (no baked-in padding — same rule as the
   illustration export spec) and knock out any solid background so the
   file is transparent. The color of the artwork doesn't matter; the
   CSS filter flattens everything to grey. A white-on-transparent logo
   works too (`brightness(0)` turns white to black before inverting).
   ImageMagick one-liners: `convert in.png -trim +repage out.png`,
   background removal `convert in.png -fuzz 18% -transparent '#f9de7a' out.png`.
3. **Drop it in `content/images/logos/`** following filename
   conventions (lowercase, hyphens, company name as slug).
4. **Edit the `customer_logos` list** on the page — add/remove/reorder
   the dict. Display order is list order.
5. **Eyeball the height.** Default 30px; tune per logo (see below).

**Legal gate**: before a logo ships to production, cross-check the
Notion "Logo Use" column (Approved / Consent Required / Disapprove).
The ranking sheet (Shovels_Logo_Ranking, Google Sheets) scores
*importance*; Notion gates *permission*. Both must pass.

#### Height tuning for optical balance

A uniform pixel height makes logos look mismatched — a wide wordmark
(Oracle) at 30px reads much "bigger" than a compact mark (the Michigan
M) at 30px. Tune each logo so they carry similar visual weight:

| Logo shape | Typical height |
|---|---|
| Very wide wordmark (Oracle, Thumbtack) | 22–28px |
| Standard wordmark (Google, Angi, Houzz) | 26–30px |
| Square-ish or stacked mark (Michigan M, AWS, Schneider, D.R. Horton) | 34–36px |

This mirrors what StreamYard does (measured: 18–56px across their
strip). There's no formula — set the default 30, then adjust by eye
against neighbors.

#### Notes

- **Section padding**: `pb-24` only (no top padding). The strip hugs
  the hero above — the hero's `pb-24 md:pb-32` provides all the
  breathing room before the "TRUSTED BY…" heading. Same pattern as
  `soc2_trust`. See *Section padding convention* up top.
- **The grey trick**: `filter: brightness(0) invert(0.7)` — `brightness(0)`
  flattens any logo to a black silhouette (alpha preserved), `invert(0.7)`
  lifts it to a uniform 70% grey. One declaration recolors any logo,
  any source color, including white.
- **Marquee mechanics**: the logo group renders twice (second copy
  `aria-hidden`); the track animates `translateX(-50%)` on an infinite
  linear loop, so the seam is invisible. Keyframes + animation are
  defined in `tailwind.config.js` (`logo-scroll`); duration comes from
  the `--logo-scroll-duration` CSS variable set by the macro.
- **Edge fades**: 96px white gradients on both sides. If the strip
  ever sits on a non-white background, those gradients (and the hover
  reveal) need a `from-{color}` adjustment — parameterize when needed.
- **Logo count**: 12–16 recommended, hard ceiling ~18. Visitors watch
  a marquee for ~5–10 seconds (6–8 logos at default speed); below-the-
  threshold logos dilute the recognizable ones. Current set = top 16
  usable logos by SEMrush Domain Authority from the ranking sheet.
- **Reduced motion**: not yet handled — see Open questions.

---

## Build helpers (`pelicanconf.py`)

### `get_industry_articles(tag, limit=3)` helper

**Location**: defined in `pelicanconf.py`, exposed to all content
pages and templates via `JINJA_GLOBALS`.

Returns up to `limit` blog posts for an industry, with three filter
tiers that fill remaining slots without duplicates:

1. **Tier 1** — posts whose `tag2` frontmatter exactly matches `tag`.
2. **Tier 2** — posts whose `tags` list contains `tag`
   (case-insensitive substring).
3. **Tier 3** — most-recent topical posts overall. Excludes the
   `Newsletter` and `Podcast` categories so they don't crowd out
   industry-relevant content on pages that don't yet have a deep
   tagged backlog. If you want a newsletter to appear, give it an
   industry `tag2`.

Posts without an `image:` or `date:` field are skipped during the
scan, so the resources card never renders a broken image.

#### Output shape

Returns a list of dicts matching the `articles` parameter of
`resources_section`:

```python
[
    {'url': '/blog/<slug>/',
     'title': '<post title>',
     'image_src': '<image path from frontmatter>',
     'image_alt': '<image_alt frontmatter or post title>'},
    ...
]
```

#### Canonical `tag` values per industry

Use these strings exactly (case-sensitive — they match `tag2`
frontmatter values).

| Industry page | `tag` to pass | Coverage as of latest scan |
|---|---|---|
| Insurance | `'Insurance'` | 1 tag2 match; tier 3 fills the rest |
| Real Estate | `'Real Estate'` | 7 tag2 matches (plenty) |
| Energy & Climate | `'Energy & Climate'` | 2 tag2 matches (note the ampersand) |
| Telecommunications | `'Telecommunications'` | 1 tag2 match |
| Construction Tech | `'Construction Tech'` | 0 tag2 matches → tier 3 fallback |
| Building Materials | `'Building Materials'` | 0 tag2 matches → tier 3 fallback |
| Home Services | `'Home Services'` | 0 tag2 matches → tier 3 fallback |

Three industries currently rely entirely on the tier-3 fallback. The
right long-term fix is to add `tag2: Construction Tech` (etc.) to
relevant existing posts, not to extend the helper.

#### Why an eager scan rather than a Pelican signal

`jinja2content` renders `.md` page content as a Jinja2 template at
**read time**, before any article generator runs. Hooking
`signals.article_generator_finalized` would populate the cache too
late — the page content would already be rendered with empty results.

So `pelicanconf.py` scans `content/posts/*.md` frontmatter directly at
config load time. The cache is populated before jinja2content reads
any page. The parser is a small regex over the metadata block, not a
full Pelican reader — enough to extract `title`, `slug`, `tag2`,
`tags`, `image`, `image_alt`, `date`, `category`, and `status`.

The scan reads all 146 posts on a cold start; this adds a few hundred
milliseconds to the build and runs once.

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
background, **centered** eyebrow chip + heading, 3-up grid of subtly
bordered translucent cards. Each card has a centered icon, a yellow
title, and a short description.

#### Usage

```jinja
{% include 'sections/enterprise_teams.html' %}
```

Place after the use-cases section in an Industry or Solutions page.

#### Notes

- **Background**: `bg-shovels-dark` (`#101727`).
- **Eyebrow + heading**: centered inside a `max-w-3xl` container.
- **Cards**: `rounded-lg border border-white/10 bg-white/5 p-8 text-center backdrop-blur-sm`
  — subtle translucent panels for visual separation against the dark
  section background.
- **Icons**: centered inside each card via a `flex justify-center`
  wrapper. Rendered at `size-16` (64px). Source SVGs live in
  `content/images/illustrations/`.
- **Titles**: yellow (`text-shovels-secondary`) for accent against the
  dark background.
- **Descriptions**: `text-gray-300`. Card 2 contains an inline link to
  the data dictionary using the standard inline-link convention.
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
│   ├── home-services/
│   ├── insurance/          ← Insurance page-specific assets
│   ├── real-estate/
│   ├── software/           ← Construction Tech audience (page slug is /software/)
│   └── telecommunications/
├── illustrations/          ← Shared assets used on multiple pages
│   ├── coverage-us.svg
│   ├── enterprise-icon-ai-classified.svg
│   ├── enterprise-icon-api-feed.svg
│   └── enterprise-icon-updates.svg
└── logos/                  ← Customer logos for the logo_strip macro
    ├── aws.svg             ← full-color originals; grey applied via CSS
    ├── google.svg
    └── ...                 ← one file per customer, named by company slug
```

Each folder name matches the corresponding Pelican page slug, which
in turn matches the live URL. The page's editorial framing (H1,
eyebrow, Notion copy) can differ from the folder name — the
`software/` folder backs the page that addresses the **Construction
Tech** audience, because the live URL is `/software/`.

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

### Illustration export spec

Use-case illustrations (the `framed=False` images) are sized by a single
canonical cap — `max-width: 420px`, applied automatically by the
`use_case` macro (see Decisions log → *Illustration max-width*). For that
cap to read consistently across pages, illustrations must be exported to
a shared standard:

- **SVG format.** Vector, so the 420px cap scales crisply on any display.
- **Tight-cropped to the artwork.** No baked-in transparent padding /
  whitespace around the drawing. The macro caps the *canvas*, so any
  internal margin makes the visible art look smaller than its neighbors.
- **Consistent canvas across the set.** Export all use-case illustrations
  at the same width (and ideally a shared aspect ratio) so they line up
  visually when capped at 420px.

Screenshots follow a different path — exported tight-cropped as `.png`,
then wrapped in the `browser_frame` chrome (30px internal padding). Do
not export screenshots as illustrations or vice versa; the macro picks
the rendering path from the `framed` flag.

### Page slugs

The folder name under `industries/` matches the Pelican page slug. The
page at `content/pages/insurance.md` references images at
`/images/industries/insurance/...`.

### Sandbox / preview pages

`status: hidden` keeps a page out of nav and the sitemap while its
URL still resolves. Two use cases:

- **Component sandboxes** — pages built to stress-test specific
  macros at different sizes and configurations.
- **Redesign previews** — temporary `<page>-preview.md` files that
  stand alongside a live page during a redesign and get folded back
  into the canonical filename + slug at launch (see *How to redesign
  an existing Industry page* below).

| Page | URL | Purpose | Type |
|---|---|---|---|
| `content/pages/mockup-test.md` | `/mockup-test` | Stress-test the `browser_frame` macro at varying widths and aspect ratios | Sandbox |
| `content/pages/insurance-preview.md` | `/insurance-preview` | Preview of the new Insurance page (no legacy predecessor; the page is brand-new). Will be renamed to `insurance.md` with `slug: insurance` at launch. | Greenfield preview |
| `content/pages/homepage-preview.md` | `/homepage-preview` | Preview of the redesigned homepage. Currently hosts the customer `logo_strip`; other homepage sections land here as the redesign progresses. **Launch swap differs from industry pages**: the live homepage is the theme template (`themes/shovels/templates/index.html`), not a content page, so at launch the preview's content moves into that template (or the homepage is converted to a page) rather than a simple file rename. Decide at launch time. | Redesign preview |

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

### Illustration max-width (420px, macro-controlled)

Use-case **illustrations** (`framed=False`) are capped at a canonical
`420px` max-width by the `use_case` macro itself — page authors do not
set a width per illustration. The `image_max_width` key remains as an
optional per-case override for genuine exceptions. **Screenshots**
(`framed=True`) are unaffected; their sizing comes from the
`browser_frame` chrome.

**Why**: the same reasoning as the 30px padding — one canonical value,
applied in one place. Per-page widths drifted: some illustrations got
a 420px cap and others none, so uncapped ones rendered at full column
width and looked oversized next to their capped siblings.

**Dependency on the export spec**: a uniform 420px cap only reads as
uniform if the SVGs are exported **tight-cropped to their content** at
a consistent canvas. An illustration with baked-in whitespace will look
small inside the 420px box even though the box is identical. The crop
discipline is the designer's half of this system; the macro cap is the
code half. See *File organization → Illustration export spec*.

### Stand-in for design tokens

We use `shovels-primary` and Tailwind defaults (`text-gray-900`, etc.)
as stand-ins for the spec's semantic tokens (`bg-primary`, `text-foreground`).

**Why**: the Shovels brand is five colors. The forcing functions for
adopting a token system (dark mode, multi-brand theming, an exploding
palette) aren't on the table. See the later decision *"Stay on
`shovels-*` palette; defer the oklch token system"* for the full
reasoning.

### `use_case_section` takes a list-of-dicts, not multiple macro calls

We chose `use_case_section(cases=[...])` over separate `use_case_open`
/ `use_case` / `use_case_close` macro calls.

**Why**: one call site per section, alternation handled internally,
adding/removing/reordering cases is a list edit. Tradeoff: the dict
structure is verbose, but it's the same structure every time.

### Bullet check badge styling

20×20 circular badge with `bg-shovels-primary/10`, containing a
Lucide Check icon at 12×12 with `stroke-width="3"`. The Check icon is
rendered via the `icons.check` macro (see the `icons` macro module).

**Why**: matches the designer's Figma. Originally missing from the
spec PDF — designer confirmed and is adding it to the spec.

### Lucide icons as Jinja macros

Lucide icons are vendored as small parameterized Jinja macros in
`themes/shovels/templates/macros/icons.html`, called with a Tailwind
`class` string and an optional `stroke_width` override. We considered
three approaches before settling on this one:

| Approach | Why we passed |
|---|---|
| Continue inlining raw SVG in each template | Scales poorly — the same SVG ends up duplicated across files, and updating one means hunting them down. Already painful at 2 icons. |
| SVG sprite sheet (`<svg><use href="#name"/></svg>`) | Slightly worse call-site ergonomics than a macro; `currentColor` plumbing has to be added to every symbol; less greppable. Real upside (single HTTP request) is small for inlined assets. |
| Pelican plugin / Jinja filter | More moving parts and a new dependency. Magical syntax (`{{ 'check' \| icon }}`) but harder to debug when something doesn't render. |

**Why macros**: zero new dependencies, fully under our control,
Tailwind classes work natively, `currentColor` makes coloring free,
build-time inlining keeps the bundle clean, and the call site reads
exactly like every other macro on the site (`{{ icons.check(...) }}`).
Adding a new icon is a 30-second copy/paste from lucide.dev. Scales
fine to ~50 icons for a marketing site this size.

### Hero eyebrow chip removed

The hero no longer renders an eyebrow chip above the H1. After
reviewing two variants on `insurance-preview` (with and without the
chip), the team decided the hero reads cleaner without it.

**Why**: the H1 is doing the wayfinding work, and the SOC 2 trust
banner immediately below already signals "this page is for serious
buyers." A second chip above the H1 felt redundant. Other eyebrow
chips on the page (Use Cases, Data Delivery, etc.) are unchanged.

### Hero column split: 6/12 + 6/12

The hero text column and illustration column are now equal width.
Previously the text column was wider (7/12) than the illustration (5/12).

**Why**: the equal split gives the illustration enough room to breathe
without making the text column feel cramped. Reviewed on
`insurance-preview` side-by-side with the 7/5 variant.

### Stay on `shovels-*` palette; defer the oklch token system

The designer's spec is built around CSS custom properties in oklch
(`--primary`, `--foreground`, `--muted-foreground`, `--border`, etc.).
We use a stand-in translation: `shovels-primary` for `--primary`,
`text-gray-900` for `--foreground`, `text-gray-500` for
`--muted-foreground`, `border-gray-200` for `--border`.

**Why we're staying on the stand-in**: the usual forcing functions
for adopting a token system — dark mode, multi-brand theming, an
exploding palette — aren't on the table. The Shovels brand is primary
green, secondary yellow, dark navy, and a handful of grays. Five-line
config, not a token system.

**The translation table is documented** under *Tokens & colors* above
so designers and engineers stay aligned when reading specs side by
side with the code.

**When to revisit**: if dark mode or a second brand theme ever
becomes a product requirement, switch to Option C (full migration to
semantic tokens). The mechanical search-and-replace is a one-day
lift; doing it under deadline pressure is the only thing to avoid.
YAGNI applies until then.

### Per-industry resources via `get_industry_articles`

Industry and Solutions pages call `get_industry_articles(tag)` to pull
related blog posts dynamically instead of hardcoding URLs on each
page. Helper lives in `pelicanconf.py` and is exposed to all templates
via `JINJA_GLOBALS`. See **Build helpers → `get_industry_articles`**.

**Why an eager scan in `pelicanconf.py` instead of a Pelican signal**:
`jinja2content` renders `.md` page content at read time, before any
article generator runs. A signal-based cache would populate too late.
The eager scan reads `content/posts/*.md` frontmatter once at config
load with a small regex parser, which is fast enough (≈100ms on the
current ~150-post backlog).

**Why three filter tiers, with newsletters/podcasts excluded from the
fallback**: three industries (Construction Tech, Building Materials,
Home Services) currently have zero `tag2`-tagged blog coverage. Without
a fallback their resources sections would be empty. Without category
exclusions the fallback would be dominated by newsletters (29% of the
post backlog), which dilutes topical focus on industry pages. The fix
is to add `tag2` values to existing posts — that's a content-team
task, not a code-team task.

### Eyebrows are written ALL CAPS at the source

Eyebrow chip text is written in uppercase in the source — both in
Notion copy and in macro/include calls (`USE CASES`, `DATA DELIVERY`,
`COVERAGE`, etc.). The CSS `uppercase` utility would render lowercase
source as uppercase visually, but writing the source in caps removes
ambiguity for editors and keeps the source string and the rendered
chip identical.

**Why**: a writer scanning the Notion source for "Use cases" and "USE
CASES" can never be sure which one renders. Forcing the source to
match the rendered output eliminates that drift.

This decision does not apply to the hero — the hero has no eyebrow.

### "Built for enterprise teams" adopts the card-based layout

`sections/enterprise_teams.html` was updated from a left-aligned
heading + plain 3-column grid to a centered heading + 3-up grid of
subtly bordered translucent cards.

**Why**: the team reviewed three variants on `insurance-preview` (V1
left-aligned plain columns, V2 centered plain columns, V3 centered
cards) and selected V3. The card treatment gives each feature its own
visual container without dominating the dark section.

**Status**: shipped. `insurance-preview.md` now uses
`{% include 'sections/enterprise_teams.html' %}`. Any other Industry
or Solutions page that includes the section automatically picks up the
new layout.

### Logo strip: CSS filter instead of pre-processed grey assets

Customer logos are stored as full-color originals in
`content/images/logos/` and flattened to grey at render time via
`filter: brightness(0) invert(0.7)` in the `logo_strip` macro. We
explicitly rejected pre-processing logos to grey with ImageMagick
(which works — proven in a spike) in favor of the CSS approach.

**Why**: this is how streamyard.com (the design reference) does it.
One CSS declaration recolors any logo regardless of source color; the
grey value is a single variable the designer can tune; reverting to
full color (or adding the color-on-hover reveal) costs nothing; and
swapping a logo means dropping in one file + one list edit — no image
pipeline to re-run. Pre-processed assets would couple every design
tweak to a batch re-export.

**Tradeoff**: original brand colors ship to the client even though
they render grey by default (that's what powers the hover reveal).
File sizes are trivial (most logos < 10KB SVG).

### Logo strip animation keyframes live in `tailwind.config.js`

The marquee's `logo-scroll` keyframes + animation are defined in
`tailwind.config.js` `theme.extend` rather than `input.css`.

**Why**: Tailwind only emits the animation class when a template
actually uses it, so the addition has zero effect on pages that don't
render the strip — unlike `input.css` base-layer rules, which are
global by nature. Loop duration stays flexible via the
`--logo-scroll-duration` CSS variable so per-page speed never requires
a config edit.

---

## Open questions

- **Logo strip + `prefers-reduced-motion`**: the marquee currently
  animates for all users. Decide whether to pause it (and show a
  static wrapped grid?) under `prefers-reduced-motion: reduce` before
  the homepage launch.
- **Logo strip on non-white backgrounds**: edge fades and hover reveal
  assume a white section background. Parameterize the fade color if
  the homepage design places the strip on a tinted section.

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

## How to add a new (greenfield) Industry page

For a brand-new Industry page that doesn't have a live predecessor:

1. Create the image folder at `content/images/industries/<slug>/`.
2. Drop in `hero.svg` and tight-cropped use-case screenshots.
3. Create the page at `content/pages/<slug>.md` with front matter
   metadata and a body that composes the macros (hero, SOC 2 trust,
   use cases, enterprise teams, coverage, resources, FAQ, final CTA).
4. Use `status: hidden` and a unique slug while iterating; remove
   when ready to ship.
5. Copy is sourced from the **"Industry Pages Copy" Notion database**.
   See *Frontmatter sourcing* below for the field mapping.

### Frontmatter sourcing (Notion DB → Pelican)

The Pelican page's frontmatter fields map to specific Notion DB columns
on the matching row. **Pull from Notion every time** — don't write
ad-hoc descriptions inline.

| Pelican frontmatter | Notion column | Notes |
|---|---|---|
| `Title:` | (derived from `Page Name` + positioning) | Used in `<title>` tag; matches the H1 positioning |
| `Description:` | `Meta description` | Becomes `<meta name="description">` — the Google snippet. ~150–160 chars, written for SEO with target-keyword cluster from `SEO: Target Keywords` |
| `slug:` | (derived from `Slug`) | `<slug>` for production, `<slug>-preview` during build-out |
| `status:` | n/a | `hidden` during build-out; removed at launch |

The Notion DB rows are the source of truth for all body copy too —
Hero H1, Hero Description, SOC 2 body, all 5 use cases, FAQ items,
and Final CTA. See the matching row in the *Industry Pages Copy*
database.

---

## How to redesign an existing Industry page

The live pages (`climate.md`, `real-estate.md`, `telecommunications.md`,
`software.md`, `building-materials.md`, `home-services.md`) need to
stay live and at the same URL through the entire redesign. The
workflow uses a **preview-slug page alongside the live one**, then
swaps at launch.

### Build phase

For each redesigned page, two files coexist on the feature branch:

| File | Slug | URL | Status |
|---|---|---|---|
| `content/pages/climate.md` (legacy) | `climate` | `/climate/` | live |
| `content/pages/climate-preview.md` (new design) | `climate-preview` | `/climate-preview/` | `hidden` |

The preview file must include `status: hidden` so it stays out of nav
and the sitemap. The URL still resolves — stakeholders can compare
`/climate/` (legacy) and `/climate-preview/` (new) in the same
browser session.

Image assets for the new design go in the existing image folder
(`content/images/industries/climate/`). The legacy page may
already reference some assets there; new and old can share the
folder during build-out.

### Launch phase (one PR per page, or one PR for all)

When the preview is approved and ready to flip live:

1. **Delete the legacy file** — `git rm content/pages/climate.md`.
2. **Rename the preview** — `git mv content/pages/climate-preview.md content/pages/climate.md`.
3. **Edit the renamed file** — change `slug: climate-preview` →
   `slug: climate`, and remove `status: hidden` so the page appears
   in nav.
4. **Commit, merge, deploy.** The URL `/climate/` now serves the new
   design. No redirects needed. No SEO impact.

### What to remember at launch

- **The `slug:` change is non-optional.** If you forget to edit it,
  the page will keep responding at `/climate-preview/` after merge
  and `/climate/` will 404.
- **Verify the FAQ schema didn't regress.** Each Industry page emits
  a `FAQPage` JSON-LD block via `faq_section`. Production rich-results
  caching can hold the old schema for a few hours; that's expected.
- **Resources section auto-updates** via `get_industry_articles(...)`,
  so no per-page maintenance is required after launch.
- **Look at the live page in prod** for at least the hero, eyebrows,
  use case alternation, and dark cards before declaring it shipped.
  Dev mode masks a few production-only behaviors (relative URLs,
  asset minification).

### Telcomm rename note

`telcomm.md` was renamed to `telecommunications.md` to match the live
URL (`/telecommunications/`) and the image folder name. The slug was
already `telecommunications`, so the rename had zero URL impact.
Other pages don't need a similar rename — they already match.
