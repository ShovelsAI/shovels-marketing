Title: Contractor Intelligence for Building Materials Suppliers
Description: Home builder leads for building materials suppliers. Find the most active contractors, surface new construction leads, and plan territories around real demand.
slug: building-materials-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Contractor intelligence for building materials suppliers',
    description='See which contractors are active, track new construction leads in every market, and act before your competitors do.',
    illustration_src='/images/industries/building-materials/hero.svg',
    illustration_alt='Building materials hero illustration') }}

{# Static 5-logo industry strip — full set, pending legal sign-off. #}
{% set building_materials_logos = [
    {'src': '/images/logos/qxo.svg', 'alt': 'QXO', 'height': 26},
    {'src': '/images/logos/owens-corning.svg', 'alt': 'Owens Corning', 'height': 36},
    {'src': '/images/logos/heidelberg-materials.svg', 'alt': 'Heidelberg Materials', 'height': 30},
    {'src': '/images/logos/avenue-roofing.svg', 'alt': 'Avenue Roofing', 'height': 30},
    {'src': '/images/logos/automate-works.png', 'alt': 'Automate', 'height': 28},
] %}

{{ ui_grid.logo_grid(logos=building_materials_logos, heading='TRUSTED BY BUILDING MATERIALS SUPPLIERS') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise building products companies and their procurement teams. Our SOC 2 Type II certification reflects controls independently audited over a sustained period.') }}

{% set building_materials_cases = [
    {
        'number': '01',
        'title': 'Find the most active contractors in your market',
        'description': 'Find contractor leads and uncover wallet share gaps with contractors you already sell to.',
        'bullets': [
            'Identify high-volume contractors in your industry',
            'Filter by trade, region, and recent permit activity',
            'Export lists for sales outreach or CRM enrichment',
            'Track contractor activity over time to prioritize follow-up',
        ],
        'image_src': '/images/industries/building-materials/uc1-trade-metro.png',
        'image_alt': 'Shovels app — contractor search filtered by trade type and metro, sorted by permit count',
    },
    {
        'number': '02',
        'title': 'Plan territories around real construction activity',
        'description': 'Map permit density by region to align rep territories with real-time construction activity.',
        'bullets': [
            'Map permit volume by trade type and ZIP, county, or metro',
            'Align sales territories with real construction demand',
            'Identify underserved markets with high permit activity',
            'Rebalance coverage as regional activity shifts',
        ],
        'image_src': '/images/industries/building-materials/uc2-target-metro.png',
        'image_alt': 'Shovels app — map showing permit density in a target metro',
    },
    {
        'number': '03',
        'title': 'Give your dealer network up-to-date builder intel',
        'description': 'Share leads and market insights with dealers, so they can prioritize outreach to the contractors driving the most home builder leads in their area.',
        'bullets': [
            'Surface active local contractors for dealer outreach',
            'Show dealers which trades are growing in their area',
            'Support dealer QBRs with real market data',
            'Strengthen dealer relationships with up-to-date market insights',
        ],
        'image_src': '/images/industries/building-materials/uc3-dealer-intel.svg',
        'image_alt': 'A materials rep and dealer at a showroom counter, reviewing local contractor activity on a tablet — intel flowing from supplier to dealer network',
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Forecast demand before it reaches the supply chain',
        'description': 'Anticipate where demand will grow. See new construction starts to renovation surges before orders hit your supply chain.',
        'bullets': [
            'Track permit starts by product category and region',
            'Detect renovation clusters before demand reaches distributors',
            'Align inventory and production planning to construction cycles',
            'Give sales teams early signals on priority areas',
        ],
        'image_src': '/images/industries/building-materials/uc4-forecast-demand.svg',
        'image_alt': 'A supply chain planner looking at permit activity appearing ahead on a production calendar — staging inventory before orders arrive',
        'framed': False,
    },
    {
        'number': '05',
        'title': 'Size the market for your products',
        'description': 'Quantify permit volume by product type to validate expansion decisions, set quotas, and make the case for new market investment.',
        'bullets': [
            'Measure addressable permit volume in any market',
            'Compare opportunity across regions and product categories',
            'Support board and investor reporting with real market data',
            'Benchmark your share of wallet against total market activity',
        ],
        'image_src': '/images/industries/building-materials/uc5-market-comparative.png',
        'image_alt': 'Hex/Sheets — bar chart of permit volume by work type across two target metros',
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What building materials companies can do with Shovels',
    cases=building_materials_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Building Materials')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What types of permits does Shovels cover?',
            'a': 'Shovels covers residential and commercial permits across all major trade categories, including roofing, HVAC, electrical, plumbing, framing, and more, sourced from jurisdictions nationwide.',
        },
        {
            'q': 'How accurate is the contractor contact data?',
            'a': 'Shovels matches permit records to licensed contractor profiles and enriches them with contact information. Match rates vary by region and trade, with typical rates in the 60-80% range for active contractors.',
        },
        {
            'q': 'Can we use Shovels data in our existing CRM?',
            'a': 'Yes. Shovels offers a REST API and structured exports that integrate with Salesforce, HubSpot, and other CRM platforms. Your team can enrich existing records or build new outreach lists directly.',
        },
        {
            'q': 'How often is the data updated?',
            'a': 'Permit data is updated continuously as jurisdictions publish new records, typically within days of issuance. Contractor records are refreshed on a rolling basis.',
        },
        {
            'q': 'How do building materials suppliers find home builder leads using permit data?',
            'a': 'Building materials companies use Shovels to surface active home builders and contractors by filtering permit activity on trade type, project category, and geography. This turns permit data into a live pipeline of home builder leads and supports ongoing home builder lead generation, connecting your sales team to the builders currently pulling permits for the projects that need your products most.',
        },
        {
            'q': 'How can sales teams identify new construction leads before projects break ground?',
            'a': 'Building permits are filed 2–6 weeks before ground breaks and months before a project appears in industry reports or distributor surveys. Shovels gives material suppliers early access to this signal, showing which new construction projects are starting, which contractors are active, and where demand will be concentrated well ahead of your competitors.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to find your next contractor customer?',
    description='See how Shovels helps building materials suppliers turn permit data into pipeline.',
    cta_label='Get Started') }}
