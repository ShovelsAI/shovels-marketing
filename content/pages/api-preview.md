Title: Shovels API: Building Permit and Contractor Data for Developers
Description: Access {{ STATS.permits }} building permits and {{ STATS.contractors }} contractors via API. Query by address, geography, or permit type. Normalized data from {{ STATS.jurisdictions }} jurisdictions.
slug: solutions/api-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/icons.html' as icons %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/code_window.html' as ui_code %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/callout.html' as ui_callout %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    eyebrow='Shovels API',
    h1='Permit and contractor data for developers',
    description='Access construction activity, contractor intelligence, and local government decisions through a single API. Query by address, geography, contractor, or permit type with sub-second response times.',
    cta_label='Get your API key',
    cta_href='https://app.shovels.ai',
    illustration_src='/images/solutions/api/hero.svg',
    illustration_alt='Shovels API — one API connecting permit, contractor, and property data') }}

{# ── Coded feature visuals ───────────────────────────────────────────────
   DRAFT CONTENT FOR REVIEW. The code/JSON/endpoints below are modeled on
   real Shovels API conventions but must be verified against the live API
   (exact base URL, geo_id format, endpoint paths, response shapes). #}

{% set f1_media %}
<div class="overflow-hidden rounded-xl bg-gray-900 shadow-sm ring-1 ring-white/10">
  {{ ui_code.window_header('geo resolution', tone='dark') }}
  <div class="p-5">
    <div class="flex items-center gap-2 rounded-lg bg-white/5 px-3 py-2.5 ring-1 ring-white/10">
      {{ icons.map_pin(class='size-4 shrink-0 text-amber-300') }}
      <span class="font-mono text-sm text-white">1042 Oak St, Lafayette CA</span>
    </div>
    <p class="mt-3 flex items-center gap-2 font-mono text-xs text-gray-400">
      <span aria-hidden="true">↓</span> resolve → <span class="text-gray-300">geo_id:</span> <span class="font-semibold text-amber-300">"ZIP94549"</span>
    </p>
    <div class="mt-3 space-y-2">
      {% for path in ['/v2/permits/search', '/v2/contractors/search', '/v2/decisions/search'] %}
      <div class="flex items-center justify-between gap-3 rounded-lg bg-white/5 px-3 py-2.5 ring-1 ring-white/10">
        <span class="font-mono text-sm"><span class="text-green-400">GET</span> <span class="text-white">{{ path }}</span></span>
        <span class="font-mono text-xs text-amber-300">?geo_id=ZIP94549</span>
      </div>
      {% endfor %}
    </div>
    <p class="mt-4 text-center font-mono text-xs text-gray-500">one key &middot; consistent response structure across every endpoint</p>
  </div>
</div>
{% endset %}

{% set f2_media %}{% call ui_code.code_window(title='permits/search · AND filters', copyable=True) %}
<span class="text-green-400">GET</span> <span class="text-white">/v2/permits/search</span>
  <span class="text-sky-300">?permit_status</span>=<span class="text-amber-300">final</span>
  <span class="text-sky-300">&permit_tags</span>=<span class="text-amber-300">solar</span>
  <span class="text-sky-300">&permit_min_job_value</span>=<span class="text-amber-300">25000</span>
  <span class="text-sky-300">&property_type</span>=<span class="text-amber-300">residential</span>
  <span class="text-sky-300">&size</span>=<span class="text-amber-300">100</span>

<span class="text-green-400">200 OK</span>
{ <span class="text-sky-300">"total_count"</span>: <span class="text-amber-300">847</span>,
  <span class="text-sky-300">"next_cursor"</span>: <span class="text-amber-300">"eyJvIjoxMDB9"</span> }
{% endcall %}{% endset %}

{% set f3_media %}
<div class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
  {{ ui_code.window_header('contractor endpoints', tone='light') }}
  <ul class="px-6 py-2">
    {% for ep, desc, icon in [
        ('/contractors/search', 'Find by trade, location, or license', 'building'),
        ('/contractors/{id}/permits', 'Linked permit and project history', 'file_text'),
        ('/contractors/{id}/employees', 'Crew and license holders', 'users'),
        ('/contractors/{id}/metrics', 'Pass rates, volume, performance', 'gauge'),
    ] %}
    <li class="flex items-start gap-4 py-3">
      <span class="flex size-9 shrink-0 items-center justify-center rounded-lg bg-shovels-primary/10">
        {{ icons[icon](class='size-4 text-shovels-primary') }}
      </span>
      <div>
        <p class="font-mono text-sm font-medium text-shovels-primary">{{ ep }}</p>
        <p class="text-sm text-gray-500">{{ desc }}</p>
      </div>
    </li>
    {% endfor %}
  </ul>
</div>
{% endset %}

{% set f5_media %}{% call ui_code.code_window(title='meta/release') %}
<span class="text-green-400">GET</span> <span class="text-white">/v2/meta/release</span>

<span class="text-green-400">200 OK</span>
{ <span class="text-sky-300">"released_at"</span>: <span class="text-amber-300">"2026-06-15"</span> }

<span class="text-gray-500"># new release on the 1st and 15th</span>
<span class="text-gray-500"># 5–10M new permit records each</span>
{% endcall %}{% endset %}

{% set f6_media %}
<div class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
  {{ ui_code.window_header('permit record', tone='light') }}
  <div class="p-6">
  <div class="flex items-center justify-between gap-4">
    <span class="font-medium text-gray-900">1042 Oak St, Lafayette, CA</span>
    <span class="inline-flex items-center gap-1.5 rounded-full bg-shovels-primary/10 px-2.5 py-1 text-xs font-medium text-shovels-primary">
      <span class="size-1.5 rounded-full bg-shovels-primary"></span>Active
    </span>
  </div>
  <p class="mt-1 text-sm text-gray-500">Reroof + 6.4 kW rooftop solar &middot; $64,200</p>
  <div class="mt-4 flex flex-wrap gap-2">
    <span class="rounded-full bg-shovels-primary/10 px-2.5 py-1 font-mono text-xs text-shovels-primary">solar</span>
    <span class="rounded-full bg-shovels-primary/10 px-2.5 py-1 font-mono text-xs text-shovels-primary">residential</span>
    <span class="rounded-full bg-shovels-primary/10 px-2.5 py-1 font-mono text-xs text-shovels-primary">green_permit</span>
    <span class="rounded-full bg-shovels-primary/10 px-2.5 py-1 font-mono text-xs text-shovels-primary">rooftop_pv</span>
  </div>
  <p class="mt-3 text-xs text-gray-400">AI-applied tags &middot; normalized on ingestion</p>
  </div>
</div>
{% endset %}

{% set features = [
    {
        'number': '01',
        'title': 'One geographic key for every endpoint',
        'description': 'Query permits, contractors, and local government decisions using the same geographic hierarchy, from a single address to an entire state. Analyze local markets or build nationwide applications without changing your integration.',
        'bullets': [
            'Resolve any address to a single geo_id',
            'Search by address, ZIP, city, county, or state',
            'Consistent response structure on every endpoint',
        ],
        'media': f1_media,
    },
    {
        'number': '02',
        'title': 'Filter permits without post-processing',
        'description': 'Filter construction activity by permit type, project value, status, property type, contractor, and more. Flexible search tools make it easy to narrow large datasets down to the records that matter.',
        'bullets': [
            'Combine status, work type, value, type, and tags',
            'AND logic across every filter',
            'Cursor pagination, up to 100 records per request',
        ],
        'media': f2_media,
    },
    {
        'number': '03',
        'title': 'Access contractor records with project history',
        'description': 'Search contractors by location, license, or specialty and connect them to permits, inspections, employees, and project history. Build a complete view of company activity, performance, and market presence.',
        'bullets': [
            'Search by work type, location, or license number',
            'Link to permits, inspections, and employee data',
            'Analyze project history and market activity together',
        ],
        'media': f3_media,
    },
    {
        'number': '04',
        'title': 'Track early construction signals with decisions data',
        'description': 'Planning, zoning, and land-use decisions often happen months before permitting. Surface activity early in the lifecycle with Shovels Decisions, so you can spot opportunities before competitors do.',
        'image_src': '/images/industries/software/uc3-upcoming-projects.svg',
        'image_alt': 'Lifecycle timeline — zoning and entitlement decisions surfacing months before a permit is filed',
        'framed': False,
    },
    {
        'number': '05',
        'title': 'Reliable, consistent release schedules',
        'description': 'Shovels publishes on a regular, predictable release schedule.',
        'bullets': [
            '5–10 million new permit records per release',
            'Monitor data availability through the API',
            'Sync your apps with the latest data',
        ],
        'media': f5_media,
    },
    {
        'number': '06',
        'title': "Structured data that's ready to use",
        'description': 'Every permit is standardized, classified, and enriched during ingestion.',
        'bullets': [
            'Filter, analyze, and build on construction data immediately',
            'No time lost cleaning or categorizing records',
            'View our <a href="/data-dictionary" class="font-semibold text-shovels-primary hover:text-shovels-primary/80 hover:underline">Data Dictionary</a> for all fields in the dataset',
        ],
        'media': f6_media,
    },
] %}

{{ ui.use_case_section(
    eyebrow='',
    heading='One API for permits, contractors, and local government decisions',
    cases=features) }}

{# Links to /cli (live today; moves to /features/cli at launch). #}
{{ ui_callout.callout(
    variant='warm',
    heading='Prefer working from the terminal?',
    body='The Shovels CLI gives you access to the same data from the command line.',
    cta_label='Check out the Shovels CLI',
    cta_href='/cli') }}

{{ ui_hiw.how_it_works(
    eyebrow='How it works',
    heading='Up and running in minutes',
    steps=[
        {
            'number': '1',
            'title': 'Sign up and get your API key',
            'description': 'Create a free account at app.shovels.ai. Access your API key and full documentation from the dashboard.',
            'icon': 'sparkles',
        },
        {
            'number': '2',
            'title': 'Query by address, geography, or contractor',
            'description': 'Use RESTful endpoints to pull exactly the data you need. Filter by permit type, geography, work category, and more.',
            'icon': 'code',
        },
        {
            'number': '3',
            'title': 'Ship to your product',
            'description': 'Integrate into your application, pipeline, or warehouse. Most teams are in production within a sprint.',
            'icon': 'app_window',
        },
    ]) }}

{{ ui_ind.industries_strip(heading='USED BY DEVELOPERS IN') }}

{% include 'sections/coverage.html' %}

{# Links to /solutions/data-feed — 404 in preview until that page ships. #}
{{ ui_callout.callout(
    variant='green',
    heading='Need this data delivered directly to Snowflake, BigQuery, or Databricks?',
    body='Shovels Enterprise Data License drops permit and contractor data straight into your warehouse with no ETL required.',
    cta_label='Explore Shovels Enterprise',
    cta_href='/solutions/data-feed') }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What data does the Shovels API provide?',
            'a': 'The Shovels API provides building permit records, contractor profiles, property details, and government decisions data from ' ~ STATS.jurisdictions ~ ' jurisdictions across all 50 states. All records are AI-enriched and normalized to a single schema, with derived metrics like inspection pass rates and green permit classification included.',
        },
        {
            'q': 'How do I get started?',
            'a': 'Sign up at app.shovels.ai to get your API key. The REST API uses standard HTTP methods and returns JSON. Full documentation, quickstart guides, and endpoint references are at docs.shovels.ai.',
        },
        {
            'q': 'Can I integrate Shovels with Snowflake, BigQuery, or Databricks?',
            'a': 'Yes. Beyond the REST API, Shovels offers native data delivery to Snowflake, BigQuery, and Databricks through our Enterprise plan. If you want to trial permit data in your own warehouse environment before committing, talk to our team.',
        },
        {
            'q': 'How often is the data updated?',
            'a': 'The database is refreshed on the 1st and 15th of each month. Each cycle adds 5–10 million new records and up to 1–5 million status updates. Processing takes up to a week after each refresh.',
        },
        {
            'q': 'Can I resell or redistribute Shovels data?',
            'a': 'Yes. Our terms are designed to give developers maximum flexibility, including the right to reuse and resell API output. No lengthy legal negotiations required.',
        },
        {
            'q': 'Are there privacy or compliance concerns with using Shovels data?',
            'a': 'All Shovels data is sourced from public government records. Building permits are public documents filed with and maintained by local jurisdictions. Shovels is also SOC 2 Type II certified, and our team is happy to discuss security questionnaires or DPAs. Just let us know.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Start building with Shovels',
    description='Get your API key, read the docs, and make your first query in minutes. No sales call required.',
    cta_label='Get your API key',
    cta_href='https://app.shovels.ai/signup') }}
