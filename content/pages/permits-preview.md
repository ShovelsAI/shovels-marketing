Title: Permits Data
Description: Search AI-classified building permits from thousands of US jurisdictions. Standardized, deduplicated, and interconnected between permits, contractors, properties, decisions and residents.
slug: permits-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/use_case.html' as ui_uc %}
{% import 'macros/record_fields.html' as ui_rec %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{# ── §1 HERO ─────────────────────────────────────────────────────────── #}
{{ ui_hero.hero(
    eyebrow='Data · Permits',
    h1='Building permit data, cleaned and ready to use',
    description='Shovels turns fragmented permit data across the US into one clean dataset. AI-classified, deduplicated, geocoded, and linked to contractors, properties, decisions and residents.',
    illustration_src='/images/data/permits/hero.svg',
    illustration_alt='Illustration of permit records being organized into a clean dataset',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    secondary_cta_label='See our data dictionary',
    secondary_cta_href='/data-dictionary') }}

{# ── §2 SOC 2 TRUST BANNER ───────────────────────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{# ── §3 PROCESS ─────────────────────────────────────────────────────── #}
{{ ui_hiw.how_it_works(
    eyebrow='Our process',
    heading='From city records to Shovel-ready data',
    anchor='process',
    steps=[
        {'number': '1', 'title': 'Collected at the source',
         'description': 'Permits come from jurisdiction portals online and public records requests offline. We source directly from cities and counties, not third-party aggregators.'},
        {'number': '2', 'title': 'Cleaned and classified by AI',
         'description': 'Every record is deduplicated, USPS-standardized, geocoded, and tagged with 98% accuracy. Every field is documented in our data dictionary.'},
        {'number': '3', 'title': 'Connected across datasets',
         'description': 'Permits link to contractors, properties, and residents. A unified record tells the whole story.'},
        {'number': '4', 'title': 'Released 2x a month',
         'description': 'Millions of new permits and status updates each cycle, documented in our release notes.'},
    ]) }}

{# ── §4 WHAT'S IN EVERY PERMIT RECORD ───────────────────────────────── #}
{{ ui_rec.record_fields(
    heading="What's in every permit record",
    description='A consistent shape across every jurisdiction — so your team writes one integration, not a thousand.',
    illustration_src='/images/data/permits/shovels-guy.svg',
    illustration_alt='Shovels field worker',
    cta_label='See more in our data dictionary',
    cta_href='/data-dictionary',
    fields=[
        {'name': 'Work type', 'description': 'What the permit is for, AI-classified from the permit description: roofing, HVAC, solar, ADU, and hundreds more.'},
        {'name': 'Contractor', 'description': 'The licensed business that pulled the permit, linked to its full Shovels profile.'},
        {'name': 'Location', 'description': 'Where the work happened: standardized address, lat/long geocode, and parcel number (APN).'},
        {'name': 'Status &amp; dates', 'description': 'Where the permit is in its lifecycle (filed, issued, finaled, inactive), with the date of each step.'},
        {'name': 'Value &amp; description', 'description': 'The reported value of the work and the original permit text.'},
    ]) }}

{# ── §5 USE CASES ───────────────────────────────────────────────────── #}

{# UC4 visual — coded "export moment": a results panel with a Download CSV
   button and a download-complete row, in the same browser chrome as the
   screenshot rows. Reused from the Shovels Online page (Notion calls for
   the Permit Database CSV-export visual, which is coded, not a file). #}
{% set uc4_media %}
<div class="relative">
  <div class="absolute inset-0 translate-x-3 translate-y-3 rounded-xl bg-[#E1ECE9]" aria-hidden="true"></div>
  <div class="relative overflow-hidden rounded-xl bg-white ring-1 ring-[#111727]">
    <div class="flex items-center gap-1.5 border-b border-gray-200 px-4 py-3">
      <span class="size-3 rounded-full bg-[#F26662]"></span>
      <span class="size-3 rounded-full bg-[#F4DA86]"></span>
      <span class="size-3 rounded-full bg-[#71A78C]"></span>
      <span class="ml-3 text-sm text-gray-600">Shovels.ai</span>
    </div>
    <div class="flex items-center justify-between px-5 pt-4">
      <span class="text-sm font-medium text-gray-500">124 results</span>
      <span class="inline-flex items-center gap-2 rounded-lg border border-gray-200 bg-white px-3 py-1.5 text-sm font-medium text-gray-700 shadow-sm">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-gray-500" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
        Download CSV
      </span>
    </div>
    <div class="px-5 pb-5 pt-4">
      <table class="w-full text-left text-sm">
        <thead>
          <tr class="text-xs uppercase tracking-wide text-gray-400">
            <th class="pb-2 font-medium">Address</th>
            <th class="pb-2 font-medium">Type</th>
            <th class="pb-2 text-right font-medium">Value</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          <tr><td class="py-2 text-gray-700">2341 Dusan Dr</td><td class="py-2 text-gray-500">New construction</td><td class="py-2 text-right tabular-nums text-gray-700">$4,000</td></tr>
          <tr><td class="py-2 text-gray-700">705 Daniel Way</td><td class="py-2 text-gray-500">Solar</td><td class="py-2 text-right tabular-nums text-gray-700">$51,990</td></tr>
          <tr><td class="py-2 text-gray-700">3818 Baldwin Dr</td><td class="py-2 text-gray-500">Reroof</td><td class="py-2 text-right tabular-nums text-gray-700">$8,400</td></tr>
          <tr><td class="py-2 text-gray-700">691 Enright Ave</td><td class="py-2 text-gray-500">Addition</td><td class="py-2 text-right tabular-nums text-gray-700">$22,500</td></tr>
        </tbody>
      </table>
    </div>
    <div class="flex items-center gap-2.5 border-t border-gray-100 bg-gray-50 px-5 py-3">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5 shrink-0 text-shovels-primary" aria-hidden="true"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v5h5"/><path d="M8 13h2"/><path d="M14 13h2"/><path d="M8 17h2"/><path d="M14 17h2"/></svg>
      <span class="text-sm font-medium text-gray-700">shovels-permits.csv</span>
      <span class="text-xs text-gray-400">124 rows</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="ml-auto size-4 shrink-0 text-shovels-primary" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
    </div>
  </div>
</div>
{% endset %}

{% set permit_cases = [
    {
        'number': '01',
        'title': 'AI classification you can filter on',
        'description': 'Our models tag every permit by type of work. Filter by new construction, solar, roofing, ADUs, EV chargers, and more.',
        'bullets': [
            'See hundreds of tags across trades, systems, and project types',
            'Separate residential and commercial new construction from tax assessor records',
            'Review metrics like approval duration and inspection outcomes',
        ],
        'image_src': '/images/industries/home-services/uc5-high-intent-homeowners.png',
        'image_alt': 'Permit list with AI tags, statuses, and job values',
        'framed': True,
    },
    {
        'number': '02',
        'title': 'Links to contractors, properties, and people',
        'description': 'Every permit is linked to contractor, property, and resident data, so you can see who did the work, where, and for whom.',
        'bullets': [
            'Full permit history for every parcel and address',
            'Connect permits to contractor profiles with licenses, work history, and contacts',
            'Find homeowner and resident contacts',
        ],
        'image_src': '/images/data/permits/UC2.svg',
        'image_alt': 'Linked-records diagram: a permit connected to contractor, property, and resident',
        'framed': False,
    },
    {
        'number': '03',
        'title': 'Track permit activity across the US',
        'description': "Filter by geography, work type, value, and permit status to see what's being built, down to the ZIP code.",
        'bullets': [
            'Monthly permit metrics by city, county, jurisdiction, and ZIP',
            'History back to 2010 for trend and market analysis',
            'Pair with <a href="/data/decisions" class="font-semibold text-shovels-primary hover:underline">Shovels Decisions</a> to see projects before permits are filed',
        ],
        'image_src': '/images/industries/building-materials/uc5-market-comparative.png',
        'image_alt': 'Permit volume by work type bar chart',
        'framed': True,
    },
    {
        'number': '04',
        'title': 'Turn permit filings into pipeline',
        'description': 'New permits are valuable buying signals for building materials suppliers, home builders, telecom providers, and others. Use Shovels to reach decision-makers early.',
        'bullets': [
            'Filter to your trade and territory, then export to CSV or directly to your CRM',
            'Match your own address list, or find homes with no recent permits',
            'Receive fresh filings with every data release',
        ],
        'media': uc4_media,
        'image_alt': 'Export panel with a Download CSV button and a completed shovels-permits.csv row',
    },
] %}

{{ ui_uc.use_case_section(
    eyebrow='The data',
    heading='Data-driven insights, made easy',
    cases=permit_cases) }}

{# ── §6 DATA DELIVERY (dark, 3 cards) — BUILD FRESH. Slots in here;
      building in the review round as a reusable section. ────────────── #}

{# ── §7 INDUSTRIES STRIP ────────────────────────────────────────────── #}
{{ ui_ind.industries_strip() }}

{# ── §8 COVERAGE (shared section; uses the macro's own copy) ─────────── #}
{% include 'sections/coverage.html' %}

{# ── §9 EXPLORE RELATED DATASETS (4 cards) — BUILD FRESH. Slots in here;
      building in the review round as a reusable section. ────────────── #}

{# ── §10 FAQ ────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What is building permit data?',
            'a': 'Building permit data is the public record of construction activity: every project a city or county approves, from water heater swaps to high-rises. Records include work description, status, dates, job value, address, and contractor. Shovels collects them directly from thousands of US jurisdictions and standardizes them into one dataset.',
        },
        {
            'q': 'How much of the US does Shovels cover?',
            'a': STATS.jurisdictions ~ ' jurisdictions covering roughly 85% of the US population, including all major metros. We add new jurisdictions monthly, and you can check per-field fill rates for any geography. See the coverage dashboard for a live view.',
        },
        {
            'q': 'How current is the permit data?',
            'a': 'We refresh the dataset twice a month with millions of new permits and status updates. Every release is documented in our release notes.',
        },
        {
            'q': 'What fields are included in a permit record?',
            'a': 'Permit number and persistent Shovels ID, status and lifecycle dates, work description, AI tags, job value, fees, standardized address with geocode, property type, and linked contractor details. Full list in the data dictionary.',
        },
        {
            'q': 'How far back does the data go?',
            'a': "Generally back to 2010, further in some jurisdictions. Depth depends on how far back each jurisdiction's records are digitized. Bulk historical backfills and sample records are available on request.",
        },
        {
            'q': 'How do I access the permit data?',
            'a': 'Three ways: search and export in Shovels Online, integrate the Shovels API, or license the full dataset via Snowflake, Databricks, or BigQuery. The free trial includes permit search with full history, no credit card required.',
        },
    ]) }}

{# ── §11 FINAL CTA ──────────────────────────────────────────────────── #}
{{ ui_cta.final_cta(
    heading='Ready to dig into ' ~ STATS.permits ~ ' permits?',
    description='Search for free, or talk to us about API and enterprise delivery.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/') }}
