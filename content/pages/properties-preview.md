Title: Properties Data
Description: Look up any US property's permit history: standardized addresses, parcels, contractors, and residents, with assessor attributes for enterprise customers.
slug: data/properties-preview
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
    eyebrow='Data · Properties',
    h1='Every property, tied to its full permit history',
    description='Shovels ties permits, contractors, and residents to standardized addresses and parcels, so you can look up any US property and see the work behind it.',
    illustration_src='/images/data/properties/hero.svg',
    illustration_alt='Illustration of a property linked to its permit history',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    secondary_cta_label='See our data dictionary',
    secondary_cta_href='/data-dictionary#properties') }}

{# ── §2 SOC 2 TRUST BANNER (generic body) ───────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{# ── §3 PROCESS ─────────────────────────────────────────────────────── #}
{{ ui_hiw.how_it_works(
    eyebrow='Our process',
    heading='From messy addresses to one clean property record',
    anchor='process',
    steps=[
        {'number': '1', 'title': 'Sourced from permit records',
         'description': 'Every property starts as an address on a permit, published by cities and counties in hundreds of inconsistent formats.'},
        {'number': '2', 'title': 'Standardized and deduplicated',
         'description': 'Addresses are USPS-standardized and merged with variants into canonical records with persistent geo IDs.'},
        {'number': '3', 'title': 'Geocoded and resolved to parcels',
         'description': 'Each property is pinned to lat/long coordinates and linked to its parcel (APN) using multiple authoritative sources.'},
        {'number': '4', 'title': 'Enriched with assessor records',
         'description': 'County tax assessor data adds property type, year built, size, and value. Every field is documented in our data dictionary.'},
    ]) }}

{# ── §4 WHAT'S IN EVERY PROPERTY RECORD ──────────────────────────────── #}
{{ ui_rec.record_fields(
    heading="What's in every property record",
    illustration_src='/images/illustrations/shovels-guy.svg',
    illustration_alt='Shovels field worker',
    cta_label='See more in our data dictionary',
    cta_href='/data-dictionary#properties',
    fields=[
        {'name': 'Address', 'description': 'USPS-standardized and geocoded, with a persistent geo ID.'},
        {'name': 'Parcel', 'description': 'Parcel data including parcel number (APN), boundaries, and county identifiers.'},
        {'name': 'Permit history', 'description': 'Every permit filed at the address, with status and work type.'},
        {'name': 'People', 'description': 'The contractors who did the work and the residents who live there.'},
        {'name': 'Attributes', 'description': 'Property type, year built, size, and assessed value from tax assessor records (Enterprise).'},
    ]) }}

{# ── §5 USE CASES ───────────────────────────────────────────────────── #}
{{ ui_uc.use_case_section(
    eyebrow='The data',
    heading='One address, one complete story',
    cases=[
        {
            'number': '01',
            'title': 'Verify property history before you act',
            'description': 'See exactly what was permitted at any address before you underwrite, buy, or close.',
            'bullets': [
                'Pull complete permit history by address in seconds',
                'Spot unpermitted work by comparing records against property condition',
                'Check the age of the roof, HVAC, or water heater from past permits',
            ],
            'image_src': '/images/industries/real-estate/uc1-property-history.png',
            'image_alt': 'Property history record with a permit timeline',
        },
        {
            'number': '02',
            'title': 'Screen properties at scale',
            'description': 'Match entire portfolios against permit history instead of checking addresses one by one.',
            'bullets': [
                'Match your portfolio or book of business via the API',
                'Find properties with no recent permits',
                'Monitor addresses for new filings with every release',
            ],
            'image_src': '/images/industries/insurance/uc4-close-gap.png',
            'image_alt': 'Book-of-business address list matched to permit records',
        },
        {
            'number': '03',
            'title': 'Build property-level features',
            'description': 'Persistent geo IDs and geocodes make Shovels data easy to join with other datasets.',
            'bullets': [
                'Address-level metrics via the API',
                'Geocodes and geo IDs for clean joins with internal data',
                'Assessor attributes like year built and assessed value in Enterprise',
            ],
            'image_src': '/images/industries/software/uc1-integration-ready.svg',
            'image_alt': 'Laptop showing permit, property, and contractor data-object cards',
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

{# ── §9 EXPLORE THE CONNECTED DATASETS (minus Properties) ────────────── #}
{{ ui_dt.data_types(
    eyebrow='Data types',
    heading='Explore the connected datasets',
    description='Every property is linked across datasets, so you see the full picture — the permits, the contractors, and the people behind each address.',
    exclude='Properties') }}

{# ── §10 FAQ ────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {'q': 'What property data does Shovels have?', 'a': 'Every property in our dataset has a standardized address, geocode, and parcel linkage, plus its full permit history and the contractors and residents connected to it. Enterprise customers can add tax assessor attributes like property type, year built, size, and assessed value.'},
        {'q': 'How do I look up permit history by address?', 'a': 'Search the address in Shovels Online, or resolve it to a geo ID with the API and pull every permit filed there: work type, status, dates, values, and the contractors who did the work.'},
        {'q': 'Can I tell what condition a property is in?', 'a': 'Permit history is a strong proxy. You can see when the roof was last replaced, whether the HVAC or water heater has been updated, and whether renovations were permitted.'},
        {'q': 'What property attributes are included?', 'a': 'Standardized address, lat/long geocode, parcel number, and geographic IDs on every record. Assessor attributes such as property type, year built, building area, and assessed value are available through an Enterprise Data License.'},
        {'q': 'How do I access property data?', 'a': 'Three ways: search any address in Shovels Online, integrate the Shovels API, or license the full dataset via Snowflake, Databricks, or BigQuery.'},
    ]) }}

{# ── §11 FINAL CTA ──────────────────────────────────────────────────── #}
{{ ui_cta.final_cta(
    heading="Look up any property's history",
    description='Search for free, or talk to us about API and enterprise delivery.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/') }}
