Title: Shovels GIS: Building Permit Data for Esri ArcGIS & QGIS
Description: Shovels delivers {{ STATS.permits }} geocoded building permits as hosted feature layers for Esri ArcGIS and QGIS. Site selection, market intelligence, and risk analysis—with parcels via Regrid.
slug: features/gis-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/icons.html' as icons %}
{% import 'macros/mockup.html' as ui_mockup %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/callout.html' as ui_callout %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    eyebrow='Shovels GIS',
    h1='The earliest signal of market growth',
    description="Building permits are the first sign of what's getting built, and where. Shovels delivers " ~ STATS.permits ~ " geocoded, AI-enriched permits as hosted feature layers, ready to load into Esri ArcGIS, QGIS, or any modern GIS platform.",
    cta_label='Talk to us',
    cta_href='https://www.shovels.ai/contact',
    secondary_cta_label='View map gallery →',
    secondary_cta_href='/features/gis/gallery-preview',
    illustration_src='/images/features/gis/hero.svg',
    illustration_alt='Shovels permit data as map layers in ArcGIS') }}

{# Canonical geospatial-partner logo set (matches the live /gis page). #}
{% set gis_logos = [
    {'src': '/images/esri.png', 'alt': 'Esri', 'height': 30},
    {'src': '/images/logos/regrid.png', 'alt': 'Regrid', 'height': 26},
    {'src': '/images/pargoai.svg', 'alt': 'ParGo AI', 'height': 28},
    {'src': '/images/logos/berkeley.svg', 'alt': 'UC Berkeley', 'height': 30},
    {'src': '/images/mit.svg', 'alt': 'MIT', 'height': 26},
] %}
{{ ui_grid.logo_grid(logos=gis_logos, heading='TRUSTED ACROSS THE GEOSPATIAL COMMUNITY') }}

{# F3 visual — GIS-stack compatibility cards (not a screenshot). #}
{% set f3_media %}
<div class="space-y-3">
  {% for name, desc in [
      ('ArcGIS Online', 'Hosted feature layers'),
      ('ArcGIS Pro', 'Desktop GIS analysis'),
      ('QGIS', 'Open-source friendly'),
  ] %}
  <div class="flex items-center justify-between gap-4 rounded-xl border border-gray-200 bg-white p-5 shadow-sm">
    <div>
      <p class="text-sm font-semibold text-gray-900">{{ name }}</p>
      <p class="mt-0.5 text-sm text-gray-500">{{ desc }}</p>
    </div>
    <span class="inline-flex shrink-0 items-center gap-1.5 rounded-full bg-shovels-primary/10 px-2.5 py-1 text-xs font-medium text-shovels-primary">
      {{ icons.check(class='size-3.5', stroke_width=3) }} compatible
    </span>
  </div>
  {% endfor %}
</div>
{% endset %}

{# F1 / F4 ArcGIS map screenshots wrapped in the browser-chrome frame. #}
{% set f1_media %}
{{ ui_mockup.browser_frame(
    '/images/features/gis/uc1-hvac-map.webp',
    'HVAC permits styled as a map layer in ArcGIS',
    title='ArcGIS Pro — HVAC permits',
    max_width='', image_padding='') }}
{% endset %}
{% set f4_media %}
{{ ui_mockup.browser_frame(
    '/images/features/gis/uc4-homebuilder-map.webp',
    'Homebuilder permit activity heat-styled by density in ArcGIS',
    title='ArcGIS — homebuilder activity',
    max_width='', image_padding='') }}
{% endset %}

{% set features = [
    {
        'number': '01',
        'title': 'See construction activity as map layers',
        'description': 'Every Shovels permit is geocoded and enriched with AI-derived attributes—project type, value, contractor, inspection outcome.',
        'bullets': [
            STATS.permits ~ ' permits as hosted feature layers',
            'Style, filter, and join like any native layer',
            'Updated twice monthly, no ETL required',
        ],
        'media': f1_media,
    },
    {
        'number': '02',
        'title': 'Join permits to parcels and properties',
        'description': 'Through our Regrid partnership, permits connect directly to parcels, bringing site selection and risk analysis into one view.',
        'bullets': [
            STATS.parcels ~ ' parcels via Regrid',
            'Linked addresses, residents, and contractor records',
            'Built for site selection and de-risking major investments',
        ],
        'image_src': '/images/industries/climate/uc5-oregon-map.svg',
        'image_alt': 'A region-wide map with permit activity lighting up across markets',
        'framed': False,
    },
    {
        'number': '03',
        'title': 'Works in the GIS stack you already use',
        'description': 'Use our hosted feature layers in ArcGIS Online and ArcGIS Pro, or import the data into QGIS and other GIS platforms.',
        'bullets': [
            'Esri ArcGIS Online and ArcGIS Pro compatible',
            'QGIS and open-source-friendly formats',
            'No data engineering required',
        ],
        'media': f3_media,
    },
    {
        'number': '04',
        'title': 'Turn permit layers into market decisions',
        'description': "Permits are the earliest geospatial signal of what's getting built, so teams can act before construction starts.",
        'bullets': [
            'Site selection: rank locations by permit density and contractor activity',
            'Market-growth signals: spot emerging development patterns first',
            'Competitive monitoring: track where competitors are pulling permits',
            'De-risk investments: validate market conditions before you commit',
        ],
        'media': f4_media,
    },
] %}

{{ ui.use_case_section(
    eyebrow='GEOSPATIAL DATA',
    heading='AI-powered permit data, delivered as a spatial format',
    cases=features) }}

{# Benefit strip — three-up, check icon + label + one line. #}
<section class="w-full bg-white px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <h2 class="text-center text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Hosted layers, zero data engineering</h2>
    <div class="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3">
      {% for title, body in [
          ('No ETL', 'Layers load straight into ArcGIS or QGIS—no bulk uploads, no data wrangling.'),
          ('No storage cost', "We host the geodatabase, so you don't pay to store " ~ STATS.permits ~ " permit records."),
          ('Always current', 'Permit layers refresh automatically twice a month—no re-importing.'),
      ] %}
      <div class="rounded-2xl border border-gray-200 bg-gray-50 p-6">
        <span class="flex size-9 items-center justify-center rounded-lg bg-shovels-primary/10">{{ icons.check(class='size-5 text-shovels-primary', stroke_width=3) }}</span>
        <p class="mt-4 text-base font-medium text-gray-900">{{ title }}</p>
        <p class="mt-1 text-sm text-gray-500">{{ body }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

{# How it works — CLI-style numbered stepper (left rail + flush connector),
   each step a card with text left + map visual right (visuals TBD). #}
<section id="how-it-works" class="w-full bg-gray-50 px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">HOW IT WORKS</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">From first call to live layers in three steps</h2>
    </div>
    <div class="mx-auto mt-12 max-w-5xl space-y-6">
      {% for num, title, desc, imgnote in [
          ('1', 'Tell us your coverage area', "Talk to our GIS team about the geographies, permit types, and layers you need. We'll scope coverage against your markets.", 'US map with a highlighted coverage area'),
          ('2', 'We provision your layers', 'We publish your hosted feature layers and share credentials within days, not months.', 'ArcGIS portal item view of a Shovels layer'),
          ('3', 'Add them to your map', 'Load the layers into ArcGIS or QGIS and start analyzing. Updates ship automatically twice a month.', 'Permit layer rendered on a web map'),
      ] %}
      <div class="flex items-stretch gap-5 md:gap-6">
        <div class="relative flex w-10 shrink-0 flex-col items-center pt-1">
          {% if not loop.last %}<span class="absolute left-1/2 top-6 -bottom-12 w-0.5 -translate-x-1/2 bg-gray-200" aria-hidden="true"></span>{% endif %}
          <span class="relative z-10 flex size-10 items-center justify-center rounded-full bg-shovels-primary text-sm font-semibold text-white">{{ num }}</span>
        </div>
        <div class="flex-1 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="grid grid-cols-1 items-center gap-6 md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-xl font-medium text-gray-900">{{ title }}</h3>
              <p class="mt-2 text-base text-gray-500">{{ desc }}</p>
            </div>
            <div class="flex aspect-video w-full flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed border-red-400 bg-red-50 p-4 text-center">
              <span class="text-2xl font-semibold uppercase tracking-widest text-red-500">TBD</span>
              <span class="text-xs text-red-400">{{ imgnote }}</span>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

{# Links to /data-feed (Shovels Enterprise) — moves to /solutions/data-feed at launch. #}
{{ ui_callout.callout(
    variant='green',
    heading='Need the full geodatabase in your warehouse?',
    body='GIS layers are one delivery format. The Shovels Data Feed delivers all seven core tables—permits, contractors, parcels, decisions, and more—to Snowflake, BigQuery, or Databricks.',
    cta_label='Explore Enterprise',
    cta_href='/data-feed') }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'How does Shovels integrate with Esri ArcGIS?',
            'a': 'Shovels delivers building permit data as hosted feature layers that work natively in ArcGIS. The geodatabase, which contains ' ~ STATS.permits ~ ' building permits, plugs directly into your existing workflows in both ArcGIS Online and ArcGIS Pro.',
        },
        {
            'q': 'Can I use Shovels data in QGIS?',
            'a': 'Yes. Shovels data ships in standard geospatial formats that QGIS and other open-source tools read natively. Most teams work with our hosted feature layers in ArcGIS, but file-based delivery is available if your stack is built on open tooling.',
        },
        {
            'q': 'How many permits are in the Shovels geodatabase?',
            'a': 'The Shovels geodatabase contains ' ~ STATS.permits ~ ' geocoded building permits from across the United States. Each permit is enriched with AI-derived attributes—like project type, value, and inspection outcomes—and linked to its contractor and property records.',
        },
        {
            'q': 'Does Shovels include parcel data for GIS users?',
            'a': 'Yes. Through our partnership with Regrid, Shovels integrates parcel data with permit records using linked address identifiers. That means you can analyze property and permit information together in one view, which is especially powerful for site selection and market intelligence.',
        },
        {
            'q': 'How often is the GIS data updated?',
            'a': "Permit layers update twice a month, and the updates flow into your maps automatically. There's no re-importing or manual refreshing required—once your layers are set up, they simply stay current.",
        },
        {
            'q': 'Who uses Shovels GIS data?',
            'a': 'Shovels GIS data is used by real estate investors, site selection analysts, utility and telecom companies, building material suppliers, government agencies, and academic researchers—anyone who needs to see construction activity as geospatial intelligence.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to put permits on the map?',
    description='Talk to our GIS team about coverage, layers, and pricing for your use case.',
    cta_label='Talk to us',
    cta_href='https://www.shovels.ai/contact') }}
