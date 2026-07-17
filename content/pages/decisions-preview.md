Title: Decisions Data
Description: Track zoning and land use decisions from US city councils and planning boards, months before permits are filed. AI-extracted, structured, and linked to permits.
slug: data/decisions-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/use_case.html' as ui_uc %}
{% import 'macros/record_fields.html' as ui_rec %}
{% import 'macros/data_delivery.html' as ui_dd %}
{% import 'macros/data_types.html' as ui_dt %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{# ── §1 HERO ─────────────────────────────────────────────────────────── #}
{{ ui_hero.hero(
    eyebrow='Data · Decisions',
    h1='Zoning and land use decisions, before permits are filed',
    description='The earliest signal that a project is coming. Shovels Decisions turns city council agendas, planning commission meetings, and meeting minutes into structured records of rezonings, entitlements, and land use decisions.',
    illustration_src='/images/data/decisions/hero.svg',
    illustration_alt='Illustration of council decisions turned into structured records',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    secondary_cta_label='See our data dictionary',
    secondary_cta_href='/data-dictionary#decisions') }}

{# ── §2 SOC 2 TRUST BANNER (generic body) ───────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{# ── §3 PROCESS ─────────────────────────────────────────────────────── #}
{{ ui_hiw.how_it_works(
    eyebrow='Our process',
    heading='From council minutes to Shovel-ready data',
    anchor='process',
    steps=[
        {'number': '1', 'title': 'Collected at the source',
         'description': 'We track agendas and official meeting minutes from city councils and planning boards. Sourced directly from jurisdictions, not third-party aggregators.'},
        {'number': '2', 'title': 'Extracted by AI',
         'description': 'Our language models turn long meeting documents into structured records: the decision, the vote, the parties, and the location.'},
        {'number': '3', 'title': 'Connected across datasets',
         'description': 'Decisions link to permits, properties, and jurisdictions, so you can follow a project from first council mention to certificate of occupancy.'},
        {'number': '4', 'title': 'Constantly expanding',
         'description': 'New decisions arrive with every twice-monthly release, and jurisdiction coverage grows each month toward our full permit footprint.'},
    ]) }}

{# ── §4 WHAT'S IN EVERY DECISION RECORD ──────────────────────────────── #}
{{ ui_rec.record_fields(
    heading="What's in every decision record",
    illustration_src='/images/illustrations/shovels-guy.svg',
    illustration_alt='Shovels field worker',
    cta_label='See more in our data dictionary',
    cta_href='/data-dictionary#decisions',
    fields=[
        {'name': 'Category', 'description': 'What kind of decision: spot and area rezonings, final plats, infrastructure development, annexations, and more.'},
        {'name': 'Zoning change', 'description': 'The previous and new zoning designations, so you see exactly what changed.'},
        {'name': 'Parties', 'description': 'The owner, applicant, developer, architect, and engineer behind the project, with contact details when named.'},
        {'name': 'Project size &amp; value', 'description': 'Building area, lot size, unit count, and project value.'},
        {'name': 'Location', 'description': 'Standardized address, lat/long geocode, and asset class, from multifamily to commercial to raw land.'},
        {'name': 'Why it matters', 'description': 'An AI-written summary and significance score for every decision, with a link to the source document.'},
    ]) }}

{# ── §5 USE CASES ───────────────────────────────────────────────────── #}
{{ ui_uc.use_case_section(
    eyebrow='The data',
    heading='See projects before they break ground',
    cases=[
        {
            'number': '01',
            'title': 'Reach projects before construction begins',
            'description': 'By the time a permit is filed, building plans are likely locked. Decisions get you into the conversation while the project is still being planned.',
            'bullets': [
                'Monitor rezonings and infrastructure decisions in your target geographies',
                'Reach owners and developers early enough to impact plans',
                'Follow up with the contacts named in the decision record',
            ],
            'image_src': '/images/industries/telecommunications/uc4-council-intelligence.png',
            'image_alt': 'Recommended signals to monitor — decisions panel',
        },
        {
            'number': '02',
            'title': 'Forecast where markets are heading',
            'description': 'Rezonings and infrastructure approvals show where cities are growing, months before construction data catches up.',
            'bullets': [
                'Track data center, energy, and industrial rezonings as they happen',
                'Gauge momentum in a new market before you enter it',
                'Feed decisions into demand models alongside permit history',
            ],
            'image_src': '/images/industries/telecommunications/uc1-new-developments.svg',
            'image_alt': 'New-developments map with pins and a list panel',
            'framed': True,
        },
        {
            'number': '03',
            'title': 'Track land and entitlement moves',
            'description': "Density changes, land entitlements, and plat approvals move land values before anything is built. See them the moment they're decided.",
            'bullets': [
                'Follow zoning changes from previous to new designation',
                'Watch plats, annexations, and density decisions in your markets',
                'Understand jurisdiction approval patterns before you buy',
            ],
            'image_src': '/images/industries/real-estate/uc4-upzoning-decisions.svg',
            'image_alt': 'Decision feed of upcoming approvals with a map',
            'framed': False,
        },
        {
            'number': '04',
            'title': 'Follow the full project lifecycle',
            'description': 'Decisions connect to permits and jurisdictions, so one project can be tracked from first city council mention to final certificate of occupancy.',
            'bullets': [
                'Link pre-permit decisions to the permits that follow',
                'Pair with Shovels Permits for the complete picture',
                'Query both from the same API',
            ],
            'image_src': '',
            'image_alt': 'NEW illustration: decision → permit → completion lifecycle timeline',
            'framed': False,
        },
    ]) }}

{# ── §6 DATA DELIVERY (dark) ─────────────────────────────────────────── #}
{{ ui_dd.data_delivery(
    eyebrow='Delivery',
    heading='One unified dataset, three ways to access it',
    dark=True,
    cards=[
        ('Shovels Online', 'Explore, filter, and export permit, contractor, and decision data in our self-serve web app.', '/permit-database', 'shovels-globe'),
        ('Shovels API', 'Build construction intelligence into your product, CRM, or internal tools with our REST API.', '/api', 'data-api'),
        ('Enterprise', 'Get the full dataset as parquet files or table shares in Snowflake, Databricks, or BigQuery.', '/data-feed', 'enterprise-box'),
    ]) }}

{# ── §7 INDUSTRIES STRIP ────────────────────────────────────────────── #}
{{ ui_ind.industries_strip() }}

{# ── §8 COVERAGE ────────────────────────────────────────────────────── #}
{% include 'sections/coverage.html' %}

{# ── §9 EXPLORE THE CONNECTED DATASETS (minus Decisions) ─────────────── #}
{{ ui_dt.data_types(
    eyebrow='Data types',
    heading='Explore the connected datasets',
    description='Decisions link across datasets, so you can follow a project from the first council mention through permits, properties, and the people involved.',
    exclude='Decisions') }}

{# ── §10 FAQ ────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {'q': 'What are zoning and land use decisions?', 'a': "They're the actions a city council or planning board takes before construction can start: rezonings, plat approvals, annexations, variances, and infrastructure decisions. Shovels extracts them from official agendas and meeting minutes and turns them into structured, searchable records."},
        {'q': 'How are Decisions different from permit data?', 'a': "Permits document construction that's already been decided. Decisions come first: the rezoning, the planning sign-off, the demolition approval. If you need to reach a project before ground breaks, decisions get you there months earlier."},
        {'q': 'Where does the data come from?', 'a': 'Official agendas and meeting minutes published by city councils and planning boards. We create a record once the minutes are posted, so every decision reflects the official record. Shovels is a first-party provider: we collect, enrich, and own the data outright.'},
        {'q': 'What fields are included in a decision record?', 'a': 'Category and subcategory, previous and new zoning designations, the parties involved (owner, applicant, developer, architect, engineer), project size and value, location, an AI-written summary of why it matters, and a link to the source document. Full list in the data dictionary.'},
        {'q': 'Do decisions link to permits?', 'a': 'Yes. When applicable, decisions are linked to properties, jurisdictions, and the permits that follow, so you can track a project from first council mention to certificate of occupancy.'},
        {'q': 'How do I access Decisions?', 'a': 'Three ways: search and export in Shovels Online, integrate the Shovels API, or license the full dataset via Snowflake, Databricks, or BigQuery. The free trial includes decision search, no credit card required.'},
    ]) }}

{# ── §11 FINAL CTA ──────────────────────────────────────────────────── #}
{{ ui_cta.final_cta(
    heading="See what's coming before permits are filed",
    description='Search for free, or talk to us about API and enterprise delivery.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/') }}
