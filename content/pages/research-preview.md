Title: Building Permit Data for Academic Research
Description: Building permit data for academic research. 130M+ AI-classified permits across 20,000+ U.S. jurisdictions, with academic pricing and flexible data delivery.
slug: research-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Building permit data for academic research',
    description='Study housing, electrification, and permitting policy with clean, AI-classified permit data — at researcher-friendly terms.',
    illustration_src='/images/industries/research/hero.svg',
    illustration_alt='Research hero illustration') }}

{# University logo wall — 6 of 6. #}
{% set research_logos = [
    {'src': '/images/logos/mit.svg', 'alt': 'MIT', 'height': 28},
    {'src': '/images/logos/stanford-university.png', 'alt': 'Stanford University', 'height': 26},
    {'src': '/images/logos/princeton.svg', 'alt': 'Princeton University', 'height': 24},
    {'src': '/images/logos/berkeley.svg', 'alt': 'UC Berkeley', 'height': 28},
    {'src': '/images/logos/purdue.svg', 'alt': 'Purdue University', 'height': 26},
    {'src': '/images/logos/university-of-michigan.svg', 'alt': 'University of Michigan', 'height': 34},
] %}

{{ ui_grid.logo_grid(logos=research_logos, heading='TRUSTED BY RESEARCHERS AT') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and data governance requirements of universities, research institutions, and grant-funded projects. Our independently audited controls are built to satisfy institutional procurement and data management plan requirements.') }}

{% set research_cases = [
    {
        'number': '01',
        'title': 'Track housing production and ADU adoption nationwide',
        'description': 'Count new construction, multifamily, and ADU permits across thousands of jurisdictions with AI-classified, deduplicated records — no manual text mining required.',
        'bullets': [
            'Count new single-family, multifamily, and ADU permits by state, county, or ZIP',
            'Compare housing production year over year with a consistent classification methodology',
            'Validate or extend survey- and text-mining-based estimates with permit-level records',
            'Drill down from national trends to individual jurisdictions and addresses',
        ],
        'image_src': '/images/industries/research/uc1-housing-production.jpg',
        'image_alt': 'Chart from the Shovels ADU report — ADU permits by state',
    },
    {
        'number': '02',
        'title': 'Measure electrification and the energy transition',
        'description': 'Study heat pump, solar, EV charger, battery, and electrical panel upgrade adoption with pre-classified permits spanning 20+ years of history.',
        'bullets': [
            'Track electrification permit volume by technology, market, and time period',
            'Measure the impact of policy changes and rebate programs on adoption',
            'Link permits to contractors to study installer markets and labor effects',
            'Read the research: <a href="https://convention2.allacademic.com/one/appam/appam25/index.php?program_focus=view_paper&selected_paper_id=2260676&cmd=online_program_direct_link&sub_action=online_program" class="font-semibold text-shovels-primary hover:underline">Spatial Diffusion and Neighboring Effects of Residential EV Charger Adoption (APPAM 2025)</a>',
        ],
        'image_src': '/images/industries/research/uc2-electrification.png',
        'image_alt': 'Chart from the Shovels EV report — EV charger permits by year',
        'framed': False,
    },
    {
        'number': '03',
        'title': 'Benchmark permitting timelines, fees, and policy outcomes',
        'description': 'Compare how long permits take and what they cost across jurisdictions to identify bottlenecks and evaluate the effects of streamlining legislation.',
        'bullets': [
            'Compare approval and construction durations across cities, counties, and states',
            'Analyze permit fees by project type to surface the best and worst jurisdictions',
            'Evaluate permitting reform with before-and-after evidence',
            "Read the research: <a href='https://siepr.stanford.edu/publications/policy-brief/overcoming-roadblocks-californias-public-ev-charging-infrastructure' class='font-semibold text-shovels-primary hover:underline'>Overcoming Roadblocks in California's Public EV Charging Infrastructure (Stanford SIEPR)</a> and <a href='https://energyathaas.wordpress.com/2025/10/27/the-fast-lane-to-electric-vehicle-charging/' class='font-semibold text-shovels-primary hover:underline'>The Fast Lane to Electric Vehicle Charging (UC Berkeley Energy Institute)</a>",
        ],
        'image_src': '/images/industries/research/uc3-permitting-timelines.png',
        'image_alt': 'Chart from the UC Berkeley Energy Institute analysis of EV charging permit timelines',
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Study disaster recovery and climate resilience',
        'description': 'Track rebuild, repair, and retrofit permits after hurricanes, wildfires, and floods to model how communities recover — down to the address level.',
        'bullets': [
            'Measure rebuild and repair activity after natural disasters by region',
            'Model recovery timelines with 20+ years of address-level permit history',
            'Identify resilience retrofits like roofing, hardening, and elevation projects',
            'Join permits to property attributes for richer risk and recovery models',
        ],
        'image_src': '/images/industries/research/uc4-disaster-recovery.jpg',
        'image_alt': 'Chart from the Shovels hurricane report — total storm-recovery permits over time',
        'framed': False,
    },
    {
        'number': '05',
        'title': 'Analyze construction markets and home improvement trends',
        'description': "Use permit and contractor records to study market structure, firm behavior, and renovation trends that surveys and annual reports can't capture.",
        'bullets': [
            'Study contractor behavior, industry consolidation, and subcontractor networks',
            'Match permits to firms for market and investment research',
            'Combine permit data with survey data for generational and demographic studies',
            'Read the research: <a href="https://arxiv.org/abs/2508.09513" class="font-semibold text-shovels-primary hover:underline">The Market Effects of Algorithms (Raymond, MIT, 2025)</a>',
        ],
        'image_src': '/images/industries/research/uc5-construction-markets.png',
        'image_alt': 'Chart from the Shovels Florida report — new construction permits by jurisdiction',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What researchers can do with Shovels',
    cases=research_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Research', fallback_category='Data'),
    heading='Explore the research') }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What building permit data does Shovels provide for academic research?',
            'a': 'Shovels provides more than 130 million geocoded building permits from 20,000+ U.S. jurisdictions, each AI-classified by project type and linked to contractor and property records. Researchers use it to study housing production, electrification, permitting policy, disaster recovery, and construction markets.',
        },
        {
            'q': 'Does Shovels offer academic pricing?',
            'a': 'Yes. Our academic pricing program offers discounted rates for universities and research institutions, including one-time bulk data purchases with perpetual licensing for research use. Datasets can be scoped by geography, permit category, and time period to fit grant budgets.',
        },
        {
            'q': 'How do researchers access Shovels data?',
            'a': 'However your research workflow requires: API access for programmatic queries, or bulk delivery as CSV or parquet files via S3, Snowflake, BigQuery, or Databricks. Sample files are available so you can evaluate the schema and fill rates before purchasing.',
        },
        {
            'q': 'How far back does the permit data go?',
            'a': 'Historical depth varies by jurisdiction, with up to 20+ years of permit history in many markets. That makes long-run analyses possible — from electrification adoption curves to multi-decade disaster recovery studies.',
        },
        {
            'q': 'How is the permit data cleaned and classified?',
            'a': "Shovels ingests raw permits from thousands of jurisdiction systems, then normalizes, deduplicates, and geocodes every record. AI classification reads each permit's type and description and assigns it to standardized categories and tags — so you can query heat pumps, ADUs, or roof repairs directly instead of parsing free text.",
        },
        {
            'q': 'Can I publish research using Shovels data?',
            'a': 'Yes. Researchers can analyze and publish findings built on Shovels data with attribution — we simply ask that you credit Shovels as the data source. We are happy to support publications with methodology documentation, data dictionaries, and co-marketing when your work goes live.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to bring Shovels data into your research?',
    description='Join researchers at MIT, Stanford, Berkeley, and beyond who use permit data to answer questions about housing, energy, and policy.',
    cta_label='Request academic access',
    cta_href='https://www.shovels.ai/contact') }}
