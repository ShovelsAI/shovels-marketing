Title: Development Intelligence for Real Estate Teams
Description: Real estate data analytics powered by permits. Track development pipelines, score neighborhood momentum, and find emerging markets before listings appear.
slug: real-estate-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Development intelligence for real estate teams',
    description='Track development pipelines, apply predictive analytics to neighborhood momentum, and identify emerging markets before they show up in listings.',
    illustration_src='/images/industries/real-estate/hero.svg',
    illustration_alt='Real estate hero illustration') }}

{# Static logo grid (POC) — 4 of 6 sourced; TRC Companies + Ownwell pending. #}
{% set real_estate_logos = [
    {'src': '/images/logos/aws.svg', 'alt': 'AWS', 'height': 34},
    {'src': '/images/logos/redfin.svg', 'alt': 'Redfin', 'height': 26},
    {'src': '/images/logos/dr-horton.svg', 'alt': 'D.R. Horton', 'height': 36},
    {'src': '/images/logos/jll.png', 'alt': 'JLL'},
] %}

{{ ui_grid.logo_grid(logos=real_estate_logos, heading='TRUSTED BY REAL ESTATE TEAMS') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise real estate firms and proptech platforms. Property data, permit records, and market intelligence are protected by independently audited controls built to hold up to enterprise security reviews.') }}

{% set real_estate_cases = [
    {
        'number': '01',
        'title': 'Verify property history before you close',
        'description': 'See every remodel, addition, and repair on the property. Know exactly what was permitted and built.',
        'bullets': [
            'Pull complete permit history by address in seconds',
            'Identify unpermitted additions and renovation work',
            'Verify job values and contractor credentials for past work',
            'Use permit records to inform due diligence and appraisal review',
            'Look up APN and parcel records alongside permit history for a complete property profile',
        ],
        'image_src': '/images/industries/real-estate/uc1-property-history.png',
        'image_alt': 'Shovels app — property detail showing full permit history with work type, contractor, and status',
    },
    {
        'number': '02',
        'title': 'Track development pipelines before listings appear',
        'description': 'Grading and demolition permits signal early-stage construction months before a project appears on MLS or CoStar. Follow individual developments from start to finish.',
        'bullets': [
            'Monitor demolition and grading permits for new developments',
            'Filter by permit type to track residential, commercial, and mixed-use projects',
            'Follow individual projects from first permit pull through final inspection',
            'Set alerts for construction activity in your target markets',
        ],
        'image_src': '/images/industries/real-estate/uc2-development-pipeline.png',
        'image_alt': 'Shovels app — map filtered to demolition and grading permits in a target area',
    },
    {
        'number': '03',
        'title': 'Score neighborhood momentum with permit data',
        'description': 'See which neighborhoods are improving, and by which parcel-level metrics, before price appreciation catches up.',
        'bullets': [
            'Access permit-based neighborhood scores by parcel, census tract, and ZIP',
            'Compare NVI trends across markets for portfolio and acquisition decisions',
            'Spot improving neighborhoods before price appreciation reflects permit activity',
            'Distinguish new construction from renovation activity by permit type',
        ],
        'image_src': '',
        'image_alt': 'A street where a few homes show active renovation — NVI score badges rising above them, an investor spotting the momentum before prices move',
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Invest and deploy capital before zoning changes move the market',
        'description': 'Shovels Decisions offers access to city council decisions on upzoning, development approvals, and housing mandates, so you can see where permit density will rise before land values move.',
        'bullets': [
            'Monitor upzoning discussions before land values adjust',
            'Assess political viability of large developments before committing capital',
            'Identify pro-development councils versus restrictive planning environments',
            'Track housing decisions that affect project economics',
        ],
        'image_src': '/images/industries/real-estate/uc4-upzoning-decisions.svg',
        'image_alt': 'Shovels Decisions — feed filtered for upzoning and development approval decisions',
    },
    {
        'number': '05',
        'title': 'Read market trends from permit filings, not lagging reports',
        'description': 'Property data analytics tools typically depend on closed transactions and listing history. Shovels gives you real-time construction activity from permit filings.',
        'bullets': [
            'Track permit volume trends by geography, property type, and work type',
            'Identify markets where construction activity is accelerating or slowing',
            'Quantify renovation activity as a proxy for housing market health',
            'Model construction cycles to inform investment timing and market entry',
        ],
        'image_src': '/images/industries/real-estate/uc5-market-trends.png',
        'image_alt': 'Two analysts side by side — one reading a thick printed report, one on a live permit dashboard — one clearly ahead of the market',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What real estate teams can do with Shovels',
    cases=real_estate_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Real Estate')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What is the Neighborhood Vitality Index?',
            'a': 'NVI is a permit-based score calculated by Shovels in partnership with Esri and Regrid. It compares permit density for home improvement projects by census tract across major metro areas, giving you a quantifiable measure of neighborhood improvement activity.',
        },
        {
            'q': 'How does Shovels track zoning and entitlement decisions?',
            'a': 'Shovels Decisions aggregates zoning changes, conditional use permits, upzoning discussions, and development approvals from 200+ city council meetings into a searchable database of 30,000+ decisions nationwide.',
        },
        {
            'q': 'Can we use permit data in our existing GIS workflow?',
            'a': 'Yes. Shovels integrates with Esri and Regrid for GIS-based workflows, including parcel boundary and ownership data. Deliver via property data API or Snowflake, BigQuery, or Databricks.',
        },
        {
            'q': 'How current is the permit data?',
            'a': 'Permit records are updated bi-weekly, with millions of new records added each cycle. NVI scores are refreshed monthly. Decisions data is updated continuously as city council meetings are processed.',
        },
        {
            'q': 'How do real estate investors use predictive analytics on permit data?',
            'a': 'Shovels lets investors and analysts apply a predictive analytics approach to real estate by tracking permit activity as a leading indicator of neighborhood change. Rising permit volume in a ZIP code — especially for ADUs, renovations, or multi-family conversions — often precedes price appreciation by 6–18 months. Shovels surfaces these signals so you can move before the market catches up, whether for investment decisions or commercial real estate lead generation.',
        },
        {
            'q': "What's the market data approach in real estate that Shovels supports?",
            'a': "Shovels enables a permit-first market data approach in real estate: instead of analyzing closed sales or price trends (lagging data), users identify development momentum from permit filings the moment they're recorded. This gives investors, developers, and data platforms a months-long head start on where capital is flowing and which neighborhoods are on the move.",
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to track development before it shows up in listings?',
    description='See how Shovels gives real estate teams the permit and decisions intelligence to move earlier than the market.',
    cta_label='Get Started') }}
