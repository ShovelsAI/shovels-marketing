Title: The Intelligence Layer for the Built World
Description: Shovels turns fragmented permit data into construction intelligence. Access nationwide permit and contractor data via API, web app, or data warehouse.
slug: homepage-preview
status: hidden

{% import 'macros/logo_strip.html' as ui_logos %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/resources.html' as ui_res %}

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
        <p class="mt-6 text-lg text-gray-500">Shovels captures the first signal of construction—using AI to turn fragmented permit data into Shovel-ready intelligence. Access via API, web app, or direct data warehouse integration.</p>
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
{% set customer_logos = [
    {'src': '/images/logos/aws.svg', 'alt': 'AWS', 'height': 34},
    {'src': '/images/logos/google.svg', 'alt': 'Google'},
    {'src': '/images/logos/oracle.svg', 'alt': 'Oracle', 'height': 22},
    {'src': '/images/logos/redfin.svg', 'alt': 'Redfin', 'height': 26},
    {'src': '/images/logos/owens-corning.svg', 'alt': 'Owens Corning', 'height': 32},
    {'src': '/images/logos/houzz.svg', 'alt': 'Houzz'},
    {'src': '/images/logos/angi.svg', 'alt': 'Angi'},
    {'src': '/images/logos/schneider-electric.svg', 'alt': 'Schneider Electric', 'height': 36},
    {'src': '/images/logos/thumbtack.png', 'alt': 'Thumbtack', 'height': 28},
    {'src': '/images/logos/energysage.svg', 'alt': 'EnergySage', 'height': 26},
    {'src': '/images/logos/jll.png', 'alt': 'JLL'},
    {'src': '/images/logos/generator-supercenter.png', 'alt': 'Generator Supercenter', 'height': 24},
    {'src': '/images/logos/dr-horton.svg', 'alt': 'D.R. Horton', 'height': 36},
    {'src': '/images/logos/ownwell.png', 'alt': 'Ownwell', 'height': 28},
    {'src': '/images/logos/pretium.png', 'alt': 'Pretium', 'height': 22},
    {'src': '/images/logos/qxo.svg', 'alt': 'QXO', 'height': 26},
] %}

{# Zero the strip's bottom padding so the Stats section's top padding owns
   the single gap below the logos (avoids doubled white-on-white space). #}
{{ ui_logos.logo_strip(logos=customer_logos, wrapper_class='!pb-0') }}

{# ── Stats ─────────────────────────────────────────────────────────── #}
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-3xl text-center">
      <img src="/images/illustrations/map-hat.svg" alt="" class="mx-auto h-12 w-auto">
      <h2 class="mt-6 text-balance text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Clean and useful building permit data that's easy to understand</h2>
      <p class="mt-4 text-lg/8 text-gray-600">Because you want to get insights from building permits, not wrangle with raw data.</p>
    </div>
    <dl class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:max-w-none lg:grid-cols-4">
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Building permits in our database</dt>
        <dd class="order-first text-4xl font-semibold tracking-tight text-shovels-primary">{{ STATS.permits }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Contractors in our database</dt>
        <dd class="order-first text-4xl font-semibold tracking-tight text-shovels-primary">{{ STATS.contractors }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">Jurisdictions covered</dt>
        <dd class="order-first text-4xl font-semibold tracking-tight text-shovels-primary">{{ STATS.jurisdictions }}</dd>
      </div>
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <dt class="text-sm/6 font-medium text-gray-600">New permits added monthly</dt>
        <dd class="order-first text-4xl font-semibold tracking-tight text-shovels-primary">{{ STATS.monthly_permits }}</dd>
      </div>
    </dl>
  </div>
</div>

{# ── Data types — the five connected datasets ──────────────────────────
   Counts pull from the canonical STATS dict (pelicanconf.py). Links point
   at the future /data/* pages (net-new in the sitemap), wired now so the
   nav is in place at launch. Copy is a first draft for review. #}
<div class="bg-shovels-dark py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-white/15 bg-white/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-gray-200">DATA TYPES</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-white md:text-4xl">Five datasets, deeply connected</h2>
      <p class="mt-6 text-base/7 text-gray-300">Permits, decisions, contractors, residents, and properties—linked together so you can trace a project from its first filing to the people and businesses behind it.</p>
    </div>

    {# Links point at KB articles until the dedicated /data/* pages ship.
       First tuple field is the illustration filename in
       content/images/illustrations/. #}
    {% set data_types = [
        ('permit-clip-board', 'Permits', 'Every building permit we can source, AI-classified into clean, structured records.', 'https://docs.shovels.ai/docs/knowledge-base/data/permits/permit-lifecycle'),
        ('check-shield', 'Decisions', 'The approvals, inspections, and status changes that move a project forward.', 'https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview'),
        ('api-hat', 'Contractors', 'Contractor profiles with licenses, work history, and contact details.', 'https://docs.shovels.ai/docs/knowledge-base/data/contractors/contractor-data-overview'),
        ('avatars', 'Residents', 'Residents and homeowners tied to properties, with contact information.', 'https://docs.shovels.ai/docs/knowledge-base/data/residents/resident-data'),
        ('map-house', 'Properties', 'Parcels and addresses connected to their full permit and ownership history.', 'https://docs.shovels.ai/docs/knowledge-base/data/geographic/coverage-areas'),
    ] %}
    <dl class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:max-w-none lg:grid-cols-5">
      {% for illustration, title, body, href in data_types %}
      <div class="flex flex-col rounded-2xl border border-white/10 bg-white/5 p-6">
        <dt>
          <img src="/images/illustrations/{{ illustration }}.svg" alt="" class="h-12 w-auto">
          <span class="mt-5 block text-base font-semibold text-white">{{ title }}</span>
        </dt>
        <dd class="mt-2 flex-auto text-sm/6 text-gray-400">{{ body }}</dd>
        <dd class="mt-4">
          <a href="{{ href }}" class="text-sm/6 font-semibold text-shovels-secondary hover:text-shovels-secondary/80">Learn more <span aria-hidden="true">→</span></a>
        </dd>
      </div>
      {% endfor %}
    </dl>
  </div>
</div>

{# "How we're different" section removed during the homepage redesign
   (not in the mock; needs rework). Archived at
   archive/homepage-how-were-different.html. #}

{# ── Data delivery options — numbered tiers (mock option 3). Links use
   the working flat slugs; repoint to /solutions/ at launch. #}
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2 class="text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Data delivery options</h2>
    </div>
    {% set delivery = [
        ('Shovels Online', 'Explore &amp; export', 'Purchase single or multiple seats to explore and download our building permit, contractor, and local government decision data.', '/permit-database'),
        ('Shovels API', 'Build into your product', 'Automate access and integrate with other applications like CRMs, custom web apps, and more.', '/api'),
        ('Enterprise Data License', 'Pipe into your warehouse', 'Get parquet files or private table shares into Snowflake, Databricks, or Big Query.', '/data-feed'),
    ] %}
    <dl class="mx-auto mt-16 grid max-w-xl grid-cols-1 gap-8 sm:mt-20 lg:mt-24 lg:max-w-none lg:grid-cols-3">
      {% for name, best, body, href in delivery %}
      <div class="flex flex-col border-t-2 border-shovels-primary pt-6">
        <dt>
          <span class="block text-3xl font-semibold text-shovels-primary">0{{ loop.index }}</span>
          <span class="mt-1 block text-3xl font-semibold text-shovels-primary">{{ name }}</span>
          <span class="mt-3 block text-xs font-medium uppercase tracking-wider text-shovels-primary">{{ best }}</span>
        </dt>
        <dd class="mt-3 flex flex-auto flex-col text-base/7 text-gray-600">
          <p class="flex-auto">{{ body }}</p>
          <p class="mt-6">
            <a href="{{ href }}" class="text-sm/6 font-semibold text-shovels-primary hover:text-shovels-primary/80">Learn more <span aria-hidden="true">→</span></a>
          </p>
        </dd>
      </div>
      {% endfor %}
    </dl>
  </div>
</div>

{# ── Industries strip — eyebrow + pill links to all Industry pages.
   Zero its own vertical padding so the neighbors (Data delivery above,
   From the blog below) own the gaps, keeping the section rhythm uniform. #}
{{ ui_ind.industries_strip(wrapper_class='!py-0') }}

{# ── From the blog — three most-recent posts ───────────────────────── #}
{{ ui_res.resources_section(
    articles=get_recent_articles(3),
    heading='From the blog',
    wrapper_class='sm:py-32') }}
