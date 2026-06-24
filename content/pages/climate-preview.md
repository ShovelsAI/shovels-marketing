Title: Electrification Intelligence for Energy & Climate Companies
Description: Solar lead generation from permit data. Find active solar, EV charger, and heat pump installers, reach in-market homeowners, and track electrification policy.
slug: climate-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Electrification intelligence for energy and climate companies',
    description='Generate solar leads from permit data, find active installers, and track new policies driving adoption.',
    illustration_src='/images/industries/climate/hero.svg',
    illustration_alt='Energy and Climate hero illustration') }}

{# Static 6-logo industry strip — full set, pending legal sign-off
   (Notion Logo Use column) before launch. #}
{% set climate_logos = [
    {'src': '/images/logos/schneider-electric.svg', 'alt': 'Schneider Electric', 'height': 31},
    {'src': '/images/logos/energysage.svg', 'alt': 'EnergySage', 'height': 23},
    {'src': '/images/logos/rewiring-america.png', 'alt': 'Rewiring America'},
    {'src': '/images/logos/frontline-wildfire.svg', 'alt': 'Frontline Wildfire Defense'},
    {'src': '/images/logos/base-power.png', 'alt': 'Base Power', 'height': 24},
    {'src': '/images/logos/permit-power.svg', 'alt': 'PermitPower', 'height': 24},
] %}

{{ ui_grid.logo_grid(logos=climate_logos, heading='TRUSTED BY ENERGY & CLIMATE TEAMS') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of utilities, energy companies, and climate technology platforms. Our independently audited controls are built to satisfy the expectations of regulated industries and enterprise procurement processes.') }}

{% set climate_cases = [
    {
        'number': '01',
        'title': 'Find every active electrification installer in your market',
        'description': 'Access solar, EV charger, heat pump, and battery permits at the contractor level to support partnerships, lead generation, or network growth.',
        'bullets': [
            'Filter contractors by electrification permit type, geography, and volume',
            'Identify active solar, heat pump, EV charger, and battery installers',
            'Access contact information for installer outreach and network recruitment',
            'Track rebate program affiliations for targeted contractor engagement',
        ],
        'image_src': '/images/industries/climate/uc1-electrification.png',
        'image_alt': 'Shovels app — contractor search filtered to solar, EV charger, and heat pump trade types, showing permit count',
    },
    {
        'number': '02',
        'title': 'Reach homeowners with active electrification permits',
        'description': 'When a homeowner pulls a solar permit, they’re signaling intent for vendors. Turn filings into residential and commercial solar leads, updated weekly.',
        'bullets': [
            'Identify homeowners with active electrification permits by type and geography',
            'Filter by permit type and job value for precise audience targeting',
            'Layer resident contact data for direct homeowner outreach',
            'Reach homeowners before competitors know a project has started',
        ],
        'image_src': '/images/industries/climate/uc2-solar-permits.png',
        'image_alt': 'Shovels app — permit search filtered to solar permits in a target ZIP, showing address, filed date, and contractor',
    },
    {
        'number': '03',
        'title': 'Track electrification policy before permits are filed',
        'description': 'Shovels Decisions tracks debates and code updates from municipalities nationwide so you can identify demand before it shows up in permits.',
        'bullets': [
            'Monitor reach code adoption and natural gas restriction debates',
            'Identify markets where electrification policy is creating contractor demand',
            'Track local rebate and incentive programs before they drive permit activity',
            'Spot favorable markets months before competition intensifies',
        ],
        'image_src': '/images/industries/climate/uc3-policy.svg',
        'image_alt': 'A city council chamber with a reach code vote underway — an energy analyst capturing the policy signal in real time, months before it drives permit activity',
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Find green mortgage candidates before the appraisal',
        'description': 'Homeowners often pull permits before financing is in place. Surface recent home permits by geography so lenders and financing platforms can reach prospects at exactly the right moment.',
        'bullets': [
            'Identify homeowners with active improvement permits who may need financing',
            'Filter by permit type, job value, and geography for targeted outreach',
            'Layer resident data for direct mail, email, and phone outreach',
            'Use permit signals to pre-qualify high-intent borrowers at scale',
        ],
        'image_src': '/images/industries/climate/uc4-solar-map.png',
        'image_alt': 'Shovels app — map filtered to solar permits in a target metro, showing recent filings by location',
    },
    {
        'number': '05',
        'title': 'Measure electrification progress across any market',
        'description': 'Don’t wait for annual reports. Know where electrification is accelerating by accessing a real-time view of adoption rates and installation trends.',
        'bullets': [
            'Track solar, EV charger, heat pump, and battery permit volume by market',
            'Compare electrification adoption rates across states, counties, and ZIPs',
            'Measure the impact of policy changes and rebate programs on permit activity',
            'Report on electrification progress with permit-backed data, not surveys',
        ],
        'image_src': '/images/industries/climate/uc5-oregon-map.svg',
        'image_alt': 'A region-wide map with solar installs, EV chargers, and heat pumps lighting up in distinct colors — adoption visible at a glance across markets',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What energy and climate teams can do with Shovels',
    cases=climate_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Energy & Climate'),
    heading='Further reading') }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What electrification permit types does Shovels track?',
            'a': 'Shovels identifies and classifies permits for solar installations, EV chargers, heat pump HVAC systems, heat pump water heaters, and battery storage systems using AI-enhanced classification across jurisdictions nationwide.',
        },
        {
            'q': 'How does Shovels track electrification policy?',
            'a': 'Shovels Decisions monitors city council meetings for reach code adoption, natural gas restriction debates, heat pump mandate discussions, and local incentive program approvals, giving you visibility into policy-driven demand before it shows up in permits.',
        },
        {
            'q': 'Do homeowners need a permit to install an EV charger?',
            'a': 'In most US jurisdictions, yes. Shovels tracks EV charger permits nationwide, so energy companies, utilities, and charging network operators can identify properties with active permits, find the installers pulling them, and measure adoption rates by market.',
        },
        {
            'q': 'How current is the electrification permit data?',
            'a': 'Permit data is updated bi-weekly with millions of new records added each cycle. AI classification is applied continuously so new solar, EV charger, and heat pump permits are tagged and queryable as they are ingested.',
        },
        {
            'q': 'How can energy companies use permit data for solar lead generation?',
            'a': 'Solar installation permits are the clearest signal that a homeowner or business is installing solar. Shovels aggregates these permits from thousands of US jurisdictions, so energy companies, solar financiers, and hardware manufacturers can power solar lead generation programs based on actual installation activity rather than ad responses or survey-based intent data. Filter by geography, permit recency, system size, and contractor to build targeted solar lead gen lists, updated weekly.',
        },
        {
            'q': 'What data does Shovels provide as a solar lead generation data provider?',
            'a': 'Shovels delivers structured solar permit data including homeowner address, permit date, contractor of record, permit type (residential vs. commercial), and jurisdiction. Energy companies and solar platforms use this as the core data source for solar lead gen programs — identifying homeowners with active permits, tracking competitor installer activity, and measuring solar adoption rates by market. Data is available via API or bulk delivery into your data warehouse.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to find every electrification contractor and homeowner in your market?',
    description='See how Shovels helps energy and climate teams track installations, reach buyers, and stay ahead of policy.',
    cta_label='Get Started') }}
