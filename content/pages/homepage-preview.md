Title: The Intelligence Layer for the Built World
Description: Shovels turns fragmented permit data into construction intelligence. Access nationwide permit and contractor data via API, web app, or data warehouse.
slug: homepage-preview
status: hidden

{% import 'macros/logo_strip.html' as ui_logos %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/icons.html' as icons %}

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

{{ ui_logos.logo_strip(logos=customer_logos) }}

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
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">DATA TYPES</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Five datasets, deeply connected</h2>
      <p class="mt-6 text-base/7 text-gray-600">Permits, decisions, contractors, residents, and properties—linked together so you can trace a project from its first filing to the people and businesses behind it.</p>
    </div>

    {# Links point at KB articles until the dedicated /data/* pages ship.
       First tuple field is the icons.html macro name, dispatched via
       icons[name] in the loop. #}
    {% set data_types = [
        ('file_text', 'Permits', 'Every building permit we can source, AI-classified into clean, structured records.', 'https://docs.shovels.ai/docs/knowledge-base/data/permits/permit-lifecycle'),
        ('clipboard_check', 'Decisions', 'The approvals, inspections, and status changes that move a project forward.', 'https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview'),
        ('hard_hat', 'Contractors', 'Contractor profiles with licenses, work history, and contact details.', 'https://docs.shovels.ai/docs/knowledge-base/data/contractors/contractor-data-overview'),
        ('users', 'Residents', 'Residents and homeowners tied to properties, with contact information.', 'https://docs.shovels.ai/docs/knowledge-base/data/residents/resident-data'),
        ('map_pin', 'Properties', 'Parcels and addresses connected to their full permit and ownership history.', 'https://docs.shovels.ai/docs/knowledge-base/data/geographic/coverage-areas'),
    ] %}
    <dl class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:max-w-none lg:grid-cols-5">
      {% for icon, title, body, href in data_types %}
      <div class="flex flex-col rounded-xl bg-gray-50 p-5">
        <dt class="flex items-center gap-3">
          <span class="flex size-9 flex-none items-center justify-center rounded-lg bg-shovels-primary/10">
            {{ icons[icon](class='size-5 text-shovels-primary') }}
          </span>
          <span class="text-base font-semibold text-gray-900">{{ title }}</span>
        </dt>
        <dd class="mt-4 flex-auto text-sm/6 text-gray-600">{{ body }}</dd>
        <dd class="mt-4">
          <a href="{{ href }}" class="text-sm/6 font-semibold text-gray-900 hover:text-shovels-primary">Learn more <span aria-hidden="true">→</span></a>
        </dd>
      </div>
      {% endfor %}
    </dl>
  </div>
</div>

{# ── How we're different ───────────────────────────────────────────── #}
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-5">
      <div class="col-span-2">
        <h2 class="text-base/7 font-semibold text-shovels-primary">How we're different</h2>
        <p class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Our data is Shovel-ready</p>
        <p class="mt-6 text-base/7 text-gray-600">We make building permits easy to understand and use for market research, go-to-market, and sales. No data engineering required.</p>
      </div>
      <dl class="col-span-3 grid grid-cols-1 gap-x-8 gap-y-10 text-base/7 text-gray-600 sm:grid-cols-2 lg:gap-y-16">
        {% set differentiators = [
            ('Fanatical customer service', "We're a small company with a big heart. We're here to help you succeed."),
            ('Constant innovation', 'We ship fast. We ship often. We ship quality. We use the latest technology to make your life easier.'),
            ('Transparency', "We're not afraid to show you exactly where our coverage gaps are. We're the only company that's fully transparent about our data."),
            ('Residents and employees', 'We go beyond just the properties and contractors. We also include residents and employees with contact information.'),
            ('Helpful documentation', 'Our documentation is comprehensive and easy to understand. We keep our API documentation and data dictionary up to date.'),
            ('AI-powered from the start', 'We run hundreds of millions of records through our AI to make sure our data is accurate.'),
            ('Pricing for everyone', 'We work with all budgets. Our customers range from climate and proptech startups to publicly-traded companies.'),
            ('Multiple interfaces', "We're more than just a data provider. We're both a data platform and a software company."),
        ] %}
        {% for title, body in differentiators %}
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            {# Round-backed check badge — same treatment as the Industry
               use-case bullets (20x20 tinted-primary circle, Lucide check). #}
            <span class="absolute left-0 top-0.5 flex size-5 items-center justify-center rounded-full bg-shovels-primary/10">
              {{ icons.check(class='size-3 text-shovels-primary', stroke_width=3) }}
            </span>
            {{ title }}
          </dt>
          <dd class="mt-2">{{ body }}</dd>
        </div>
        {% endfor %}
      </dl>
    </div>
  </div>
</div>

{# ── Work with us (3 product interfaces) — new icons ───────────────── #}
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2 class="text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl">Data delivery options</h2>
      <p class="mt-6 text-lg/8 text-gray-300">Three ways to access our building permit, contractor, and government decision data—self-serve online, via API, or as a licensed enterprise feed.</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
        <div class="flex flex-col">
          <dt class="text-base/7 font-semibold text-white">
            <div class="mb-6 flex size-20 items-center justify-center rounded-lg">
              <img src="/images/home/shovels-online.svg" alt="Shovels Online" class="size-20">
            </div>
            Shovels Online
          </dt>
          <dd class="mt-1 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">Purchase single or multiple seats to explore and download our building permit, contractor, and local government decision data.</p>
            <p class="mt-6">
              <a href="/permit-database" class="text-sm/6 font-semibold text-shovels-secondary">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="text-base/7 font-semibold text-white">
            <div class="mb-6 flex size-20 items-center justify-center rounded-lg">
              <img src="/images/home/shovels-api.svg" alt="Shovels API" class="size-20">
            </div>
            Shovels API
          </dt>
          <dd class="mt-1 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">Automate access and integrate with other applications like CRMs, custom web apps, and more.</p>
            <p class="mt-6">
              <a href="/api" class="text-sm/6 font-semibold text-shovels-secondary">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="text-base/7 font-semibold text-white">
            <div class="mb-6 flex size-20 items-center justify-center rounded-lg">
              <img src="/images/home/shovels-enterprise.svg" alt="Enterprise Data License" class="size-20">
            </div>
            Enterprise Data License
          </dt>
          <dd class="mt-1 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">Get parquet files or private table shares into Snowflake, Databricks, or Big Query.</p>
            <p class="mt-6">
              <a href="/data-feed" class="text-sm/6 font-semibold text-shovels-secondary">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>

{# ── Industries strip — eyebrow + pill links to all Industry pages.
   Drop bottom padding so the following "From the blog" section's top
   padding owns the single gap (avoids doubled vertical space). #}
{{ ui_ind.industries_strip(wrapper_class='!pb-0') }}

{# ── From the blog — three most-recent posts ───────────────────────── #}
{{ ui_res.resources_section(
    articles=get_recent_articles(3),
    heading='From the blog') }}
