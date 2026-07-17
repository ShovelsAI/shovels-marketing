Title: Residents Data
Description: Homeowner and resident data linked to US properties and permits: validated contacts, homeowner status, and household attributes.
slug: data/residents-preview
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
    eyebrow='Data · Residents',
    h1='Homeowner and resident data, tied to real properties',
    description='Shovels links residents and homeowners to our property and permit data. Get validated contacts for addresses where work is happening.',
    illustration_src='/images/data/residents/hero.svg',
    illustration_alt='Illustration of residents linked to properties and permits',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    secondary_cta_label='See our data dictionary',
    secondary_cta_href='/data-dictionary#residents') }}

{# ── §2 SOC 2 TRUST BANNER (generic body) ───────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{# ── §3 PROCESS ─────────────────────────────────────────────────────── #}
{{ ui_hiw.how_it_works(
    eyebrow='Our process',
    heading='From address to verified resident',
    anchor='process',
    steps=[
        {'number': '1', 'title': 'Anchored to the address',
         'description': 'Every resident record starts with a property in our permit dataset, linked by a persistent address ID.'},
        {'number': '2', 'title': 'Assembled from multiple sources',
         'description': 'Names, workplaces, addresses, and contact details are connected across independent data signals.'},
        {'number': '3', 'title': 'Validated by consensus',
         'description': 'A data point makes the record only when three or more signals agree.'},
        {'number': '4', 'title': 'Tracked for freshness',
         'description': "Contacts carry validation status and last-seen dates, so you know what's current."},
    ]) }}

{# ── §4 WHAT'S IN EVERY RESIDENT RECORD ──────────────────────────────── #}
{{ ui_rec.record_fields(
    heading="What's in every resident record",
    illustration_src='/images/illustrations/shovels-guy.svg',
    illustration_alt='Shovels field worker',
    cta_label='See more in our data dictionary',
    cta_href='/data-dictionary#residents',
    fields=[
        {'name': 'Contacts', 'description': 'Phone, personal and business emails with validation status, and LinkedIn profile.'},
        {'name': 'Homeowner flag', 'description': 'Whether the resident owns the home, so you can target owners, not tenants.'},
        {'name': 'Household', 'description': 'Age range, income range, net worth, marital status, and children in the home.'},
        {'name': 'Profession', 'description': 'Job title, seniority, and employer details like industry and company size.'},
        {'name': 'Address link', 'description': 'A persistent address ID connecting the resident to the property and its full permit history.'},
    ]) }}

{# ── §5 USE CASES ───────────────────────────────────────────────────── #}
{{ ui_uc.use_case_section(
    eyebrow='The data',
    heading="Know who's at every address",
    cases=[
        {
            'number': '01',
            'title': 'Reach the homeowner connected to a project',
            'description': 'Permits tell you where work is happening, and resident data tells you who to talk to about it.',
            'bullets': [
                'Find owners at addresses with (or without) recent permits',
                'Use validated emails and phones, with last-seen dates',
                'Filter homeowners from renters with the homeowner flag',
            ],
            'image_src': '/images/industries/climate/uc2-solar-permits.png',
            'image_alt': 'Homeowner permit list with addresses and tags',
        },
        {
            'number': '02',
            'title': 'Qualify projects before you make the call',
            'description': 'Household attributes help you prioritize the addresses that are valuable to your business.',
            'bullets': [
                'Prioritize by income range, net worth, and household profile',
                'Segment by age range, family status, and profession',
                'Focus territories where your ideal customers live',
            ],
            'image_src': '/images/industries/climate/uc4-solar-map.png',
            'image_alt': 'Household-attribute targeting map and panel',
        },
        {
            'number': '03',
            'title': 'Enrich the addresses you already have',
            'description': 'Pass any address into the residents endpoint and see the people associated with it.',
            'bullets': [
                'Enrich CRM records with resident contacts at scale',
                'Match your address lists via the API',
                'Combine with permit history for full context on every address',
            ],
            'image_src': '',
            'image_alt': 'Shovels API console showing an address enrichment call',
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

{# ── §9 EXPLORE THE CONNECTED DATASETS (minus Residents) ─────────────── #}
{{ ui_dt.data_types(
    eyebrow='Data types',
    heading='Explore the connected datasets',
    description='Every resident is tied to a property, so you see the full picture — the permits, the contractors, and the work happening at each address.',
    exclude='Residents') }}

{# ── §10 FAQ ────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {'q': 'What is resident data?', 'a': 'Resident data identifies the people living at a property: names, validated contact details, homeowner status, and household attributes like age range, income range, and net worth. Shovels ties each resident to a property in our permit dataset.'},
        {'q': 'Where does resident data come from?', 'a': 'We assemble resident records from multiple independent data sources, linking names, workplaces, addresses, and contact details. A data point is included only when three or more signals agree, and every contact carries a validation status and last-seen date.'},
        {'q': 'Can I tell homeowners from renters?', 'a': 'Yes. Every resident record includes a homeowner flag, so you can filter for owners when your product or service is for the person who makes decisions about the home.'},
        {'q': 'What fields are included in a resident record?', 'a': 'Contacts (phone, personal and business email, LinkedIn), homeowner status, household attributes like age range, income range, net worth, marital status, and children, plus job title, seniority, and employer details. Full list in the data dictionary.'},
        {'q': 'How do I access resident data?', 'a': 'Three ways: search and export in Shovels Online, integrate the Shovels API (pass any address from a permit into the residents endpoint), or license the full dataset via Snowflake, Databricks, or BigQuery.'},
    ]) }}

{# ── §11 FINAL CTA ──────────────────────────────────────────────────── #}
{{ ui_cta.final_cta(
    heading='Connect addresses to residents',
    description='Search for free, or talk to us about API and enterprise delivery.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/') }}
