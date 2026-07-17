Title: The Intelligence Layer for the Built World
Description: Shovels turns fragmented public records into construction intelligence. Access nationwide permit, contractor, and property data via API, web app, or data warehouse.
slug: homepage-preview
status: hidden

{% import 'macros/logo_strip.html' as ui_logos %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}
{% import 'macros/data_delivery.html' as ui_dd %}
{% import 'macros/data_types.html' as ui_dt %}

{# ── Hero ──────────────────────────────────────────────────────────────
   Redesigned hero treatment from the Industry pages: crossing-gradient
   grid background with a radial fade, balanced font-medium headline.
   Homepage keeps its two CTAs (primary button + secondary text link)
   and its side illustration. #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-24 px-6 md:pt-28 md:pb-32 md:px-10">

  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>

  <div class="relative mx-auto max-w-6xl">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-10 md:gap-16 items-center">

      <div class="md:col-span-6">
        <h1 class="text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">The intelligence layer for the built world</h1>
        <p class="mt-6 text-lg text-gray-500">Shovels captures the first signal of construction—using AI to turn fragmented public records into Shovel-ready intelligence. Access via API, web app, or direct data warehouse integration.</p>
        <div class="mt-8">
          <a href="https://app.shovels.ai" class="inline-block rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Search for free</a>
        </div>
      </div>

      <div class="md:col-span-6">
        <img src="/images/home/hero.svg" alt="Shovels building permit data" class="block w-full h-auto" />
      </div>

    </div>
  </div>
</section>

{# ── Customer logo strip (scrolling marquee) ───────────────────────────
   Customer logos in Domain Authority order — see the Shovels_Logo_Ranking
   sheet for the ranking and COMPONENTS.md → logo_strip for the swap process.
   Legal gate: cross-check the Notion "Logo Use" column before launch. #}
{# Heights scaled down ~13% from the original tuning (designer: reduce
   logo size 10–15%); relative sizing preserved for optical balance. #}
{% set customer_logos = [
    {'src': '/images/logos/aws.svg', 'alt': 'AWS', 'height': 30},
    {'src': '/images/logos/google.svg', 'alt': 'Google', 'height': 26},
    {'src': '/images/logos/oracle.svg', 'alt': 'Oracle', 'height': 19},
    {'src': '/images/logos/redfin.svg', 'alt': 'Redfin', 'height': 23},
    {'src': '/images/logos/owens-corning.svg', 'alt': 'Owens Corning', 'height': 28},
    {'src': '/images/logos/houzz.svg', 'alt': 'Houzz', 'height': 26},
    {'src': '/images/logos/angi.svg', 'alt': 'Angi', 'height': 26},
    {'src': '/images/logos/schneider-electric.svg', 'alt': 'Schneider Electric', 'height': 31},
    {'src': '/images/logos/thumbtack.png', 'alt': 'Thumbtack', 'height': 24},
    {'src': '/images/logos/energysage.svg', 'alt': 'EnergySage', 'height': 23},
    {'src': '/images/logos/jll.png', 'alt': 'JLL', 'height': 26},
    {'src': '/images/logos/generator-supercenter.png', 'alt': 'Generator Supercenter', 'height': 21},
    {'src': '/images/logos/dr-horton.svg', 'alt': 'D.R. Horton', 'height': 31},
    {'src': '/images/logos/ownwell.png', 'alt': 'Ownwell', 'height': 24},
    {'src': '/images/logos/pretium.png', 'alt': 'Pretium', 'height': 19},
    {'src': '/images/logos/qxo.svg', 'alt': 'QXO', 'height': 23},
] %}

{# Zero the strip's bottom padding so the Stats section's top padding owns
   the single gap below the logos (avoids doubled white-on-white space). #}
{{ ui_logos.logo_strip(logos=customer_logos, wrapper_class='!pb-0') }}

{# Divider — hairline in the stats-card border grey (gray-200), fading at
   both ends. The wrapper mirrors the stats section's container
   (max-w-7xl + padding) so the fade completes exactly at the outer edge
   of the stats cards below. #}
<div class="mx-auto mt-14 max-w-7xl px-6 lg:px-8" aria-hidden="true">
  <div class="h-px bg-gradient-to-r from-transparent via-gray-200 to-transparent"></div>
</div>

{# ── Stats ─────────────────────────────────────────────────────────── #}
{# Top padding reduced (designer: tighten divider→stats gap ~20%); bottom
   kept on the section rhythm. Heading→stats gap trimmed mt-16→mt-14. #}
<div class="bg-white pt-16 pb-24 sm:pt-24 sm:pb-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-3xl text-center">
      <img src="/images/illustrations/map-hat.svg" alt="" class="mx-auto h-12 w-auto">
      <h2 class="mt-6 text-balance text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Nationwide construction data, ready to use</h2>
      <p class="mt-4 text-lg/8 text-gray-600">Get insights from public records without wrangling raw data.</p>
    </div>
    <dl class="mx-auto mt-14 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:max-w-none lg:grid-cols-4">
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Building permits</dt>
        <dd class="order-first text-4xl font-bold tracking-tight text-shovels-primary">{{ STATS.permits }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Licensed contractors</dt>
        <dd class="order-first text-4xl font-bold tracking-tight text-shovels-primary">{{ STATS.contractors }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Jurisdictions covered</dt>
        <dd class="order-first text-4xl font-bold tracking-tight text-shovels-primary">{{ STATS.jurisdictions }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">New permits added monthly</dt>
        <dd class="order-first text-4xl font-bold tracking-tight text-shovels-primary">{{ STATS.monthly_permits }}</dd>
      </div>
    </dl>
  </div>
</div>

{# ── Data types — the five connected datasets (shared macro).
   Homepage keeps its KB-article links (passed explicitly) until the
   dedicated /data/* pages ship; the macro default links to /data/*. #}
{{ ui_dt.data_types(
    eyebrow='DATA TYPES',
    heading='Five datasets, deeply connected',
    description='Every record is linked across datasets, so you get the full picture. See the project, property, and people behind it, then move from insight to action.',
    datasets=[
        ('permit-clip-board', 'Permits', 'Every building permit we cover, AI-classified into structured records.', 'https://docs.shovels.ai/docs/knowledge-base/data/permits/permit-lifecycle'),
        ('check-shield', 'Decisions', 'Zoning and development decisions, before a permit is filed.', 'https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview'),
        ('api-hat', 'Contractors', 'Contractor profiles with licenses, work history, and contact details.', 'https://docs.shovels.ai/docs/knowledge-base/data/contractors/contractor-data-overview'),
        ('map-house', 'Properties', 'Parcels and addresses with full permit and ownership history.', 'https://docs.shovels.ai/docs/knowledge-base/data/geographic/coverage-areas'),
        ('avatars', 'Residents', 'Residents and homeowners tied to properties, with contacts.', 'https://docs.shovels.ai/docs/knowledge-base/data/residents/resident-data'),
    ]) }}

{# "How we're different" section removed during the homepage redesign
   (not in the mock; needs rework). Archived at
   archive/homepage-how-were-different.html. #}

{# ── Data delivery options — shared macro (icon cards, light variant).
   Links use the working flat slugs; repoint to /solutions/ at launch. #}
{{ ui_dd.data_delivery(
    heading='Data delivery options',
    description='One unified dataset. Three ways to access it. Choose the integration that fits your workflow.',
    cards=[
        ('Shovels Online', 'Explore, filter, and export permit, contractor, and decision data in our self-serve web app.', '/permit-database', 'shovels-globe'),
        ('Shovels API', 'Build construction intelligence into your product, CRM, or internal tools with our REST API.', '/api', 'data-api'),
        ('Enterprise', 'Get the full dataset as parquet files or table shares in Snowflake, Databricks, or BigQuery.', '/data-feed', 'enterprise-box'),
    ]) }}

{# ── Coverage — same include as the Industry pages. Now the first section
   after Data delivery (designer reorder): !pt-0 lets Data delivery's bottom
   padding own the gap above; sm:pb-32 provides the gap down to the
   Industries strip (white-on-white dedup). #}
{% set coverage_wrapper_class = '!pt-0 sm:pb-32' %}
{% include 'sections/coverage.html' %}

{# ── Industries strip — eyebrow + pill links to all Industry pages. Moved
   below Coverage (designer: alternate image/text density for better
   rhythm). Zero its own vertical padding so the neighbors (Coverage above,
   From the blog below) own the gaps. #}
{{ ui_ind.industries_strip(wrapper_class='!py-0') }}

{# ── From the blog — three most-recent posts. Bottom padding zeroed so
   the final CTA's top padding owns the closing gap. #}
{{ ui_res.resources_section(
    articles=get_recent_articles(3),
    heading='From the blog',
    wrapper_class='sm:py-32 !pb-0') }}

{# ── Final CTA — closing ask, mirrors the hero's self-serve CTA and
   carries the sales path for enterprise buyers. #}
{{ ui_cta.final_cta(
    heading='Ready to put our Shovel-ready data to work?',
    description='Search our clean and enriched public-record data for free, or talk to us about API access and enterprise data delivery.',
    cta_label='Search for free',
    cta_href='https://app.shovels.ai',
    wrapper_class='sm:py-32') }}
