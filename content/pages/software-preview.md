Title: Contractor Intelligence for Construction Technology Companies
Description: Construction data analytics for proptech companies. Add permit data, contractor verification, and predictive intelligence to your platform — via API.
slug: software-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Contractor intelligence for construction technology companies',
    description='Add permit insights and predictive analytics to your product without building your own data pipeline.',
    illustration_src='/images/industries/software/hero.svg',
    illustration_alt='Construction technology hero illustration') }}

{# Static industry strip — full set, pending legal sign-off. #}
{% set software_logos = [
    {'src': '/images/logos/planhub.png', 'alt': 'PlanHub', 'height': 28},
    {'src': '/images/logos/handle.svg', 'alt': 'Handle', 'height': 28},
    {'src': '/images/logos/nuvo.svg', 'alt': 'Nuvo', 'height': 28},
    {'src': '/images/logos/toolbelt.png', 'alt': 'ToolBelt', 'height': 28},
    {'src': '/images/logos/algoma.png', 'alt': 'Algoma', 'height': 28},
    {'src': '/images/logos/fuse-service.svg', 'alt': 'Fuse Service', 'height': 28},
] %}

{{ ui_grid.logo_grid(logos=software_logos, heading='TRUSTED BY CONSTRUCTION TECHNOLOGY TEAMS') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of construction technology companies and their enterprise customers. SOC 2 Type II means our controls were audited over time, giving your security team and enterprise buyers the assurance they need to approve us as a vendor.') }}

{% set software_cases = [
    {
        'number': '01',
        'title': 'Enrich your platform with permit data that’s integration-ready',
        'description': 'Get clean property data via API that supports analytics, location intelligence, and contractor-facing insights.',
        'bullets': [
            'Permit and contractor data delivered via Snowflake, BigQuery, Databricks, or API',
            'Bi-weekly refresh with millions of new records added each cycle',
            'AI-classified permit types with clean, structured data out of the box',
            'Changelog tracking for permit status updates over time',
        ],
        'image_src': '/images/industries/software/uc1-integration-ready.svg',
        'image_alt': 'A developer receiving clean, structured permit data flowing into their platform — labeled fields slotting into place, no raw parsing required',
        'framed': False,
    },
    {
        'number': '02',
        'title': 'Add contractor verification to your product',
        'description': 'Permit history linked to state license data gives your platform a multi-signal view of every contractor. Know who is active, licensed, and where they work.',
        'bullets': [
            'Match permit records to state license files across the US',
            'Verify trade classification, license status, and geographic coverage',
            'Access employee names and contact info for decision-maker outreach',
            'Enrich contractor profiles without building a verification pipeline',
        ],
        'image_src': '/images/industries/software/uc2-contractor-verification.png',
        'image_alt': 'Shovels app — contractor detail showing permit history, license status, and active permits by date',
    },
    {
        'number': '03',
        'title': 'Show your users upcoming projects before permits are filed',
        'description': 'Use Shovels Decisions data to surface approvals and zoning decisions, giving your users valuable early signals to beat out competitors.',
        'bullets': [
            'Surface development approvals and zoning decisions before permits are filed',
            'Help your customers engage prospects earlier in the project lifecycle',
            'Track projects from entitlement through permit issuance',
            'Access Decisions data and permit records in a single pipeline',
        ],
        'image_src': '/images/industries/software/uc3-upcoming-projects.svg',
        'image_alt': "A contractor using their platform to see upcoming projects on a map — already reaching out while competitors don't know the jobs exist",
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Offer permit tracking features without building the infrastructure',
        'description': 'Shovels refreshes permit status bi-weekly with changelog tracking. Give your users accurate, current permit data without managing a single scraper.',
        'bullets': [
            'Bi-weekly permit status refresh across all jurisdictions',
            'Changelog tracking for status changes over time',
            'REST API with permit lookup by address, contractor, or jurisdiction',
            'AI-classified permit types eliminate raw text parsing for your team',
        ],
        'image_src': '/images/industries/software/uc4-permit-tracking.png',
        'image_alt': 'Shovels app — permit detail showing status, filing date, approval date, and inspection milestones',
    },
    {
        'number': '05',
        'title': 'Surface full property permit history for compliance and due diligence',
        'description': 'Every permit on record for a given address, with dates, work types, job values, permit status, and APN. Link any address to parcel records in GIS or underwriting workflows.',
        'bullets': [
            'Pull full permit history by address in jurisdictions across the US',
            'Identify unpermitted work gaps and compliance timelines',
            'Filter by work type, permit status, and date range',
            'Integrate property history into underwriting, lending, or inspection workflows',
        ],
        'image_src': '/images/industries/software/uc5-property-history.png',
        'image_alt': 'Shovels app — property detail showing all historical permits by date with work type, contractor, and value',
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What construction technology teams can do with Shovels',
    cases=software_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Construction Tech')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'Do I need to build a data pipeline to use Shovels?',
            'a': 'No. Shovels delivers permit and contractor data directly to Snowflake, BigQuery, Databricks, or via API. Your engineering team gets clean, structured data without building or maintaining jurisdiction scrapers.',
        },
        {
            'q': 'How does Shovels handle permit status updates?',
            'a': 'Shovels refreshes permit data bi-weekly across 5,000+ jurisdictions and tracks status changes via changelog. Your platform always has current permit status without polling individual jurisdictions.',
        },
        {
            'q': 'Can Shovels data power contractor verification in our product?',
            'a': 'Yes. Shovels matches permit records to state contractor license files from 37 states, giving you a multi-signal verification layer including trade classification, license status, geographic coverage, and permit history.',
        },
        {
            'q': 'How does Shovels fit into the proptech stack?',
            'a': 'Shovels is a data layer for proptech companies building on construction and property activity. Proptech companies use Shovels for contractor verification, project discovery, and market analytics. Proptech software development teams get clean data via API or directly into Snowflake, BigQuery, or Databricks.',
        },
        {
            'q': 'How can construction technology platforms use predictive analytics in construction workflows?',
            'a': 'Shovels provides two data layers for predictive analytics: permit data (filed permits with contractor, location, and project details) and Shovels Decisions (pre-permit intelligence from city council agendas and project applications). Together, these let construction technology platforms surface project signals weeks or months before ground breaks, giving users a genuine predictive advantage in project discovery, contractor targeting, and territory planning.',
        },
        {
            'q': 'What geospatial analytics in construction does Shovels permit data enable?',
            'a': 'Shovels permit data is structured for geospatial analysis — each record includes jurisdiction, address, geocode, contractor, trade, and project type. Construction technology platforms use this for geospatial analytics in construction including permit density mapping, territory heat maps, market sizing by region, and location-based project discovery features. Data is available via API or direct delivery into Snowflake, BigQuery, or Databricks for integration into existing geospatial stacks.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to power your platform with the most complete permit dataset?',
    description='See how Shovels helps construction technology teams build better products with permit and contractor data.',
    cta_label='Get Started') }}
