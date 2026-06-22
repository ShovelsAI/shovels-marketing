Title: Shovels Online: Permit and Contractor Data, No Code Required
Description: Search {{ STATS.permits }} U.S. building permits and {{ STATS.contractors }} contractors from your browser. Filter by location, permit type, or specialty. Export to CSV in one click.
slug: solutions/permit-database-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/callout.html' as ui_callout %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    eyebrow='Shovels Online',
    h1='Permit and contractor data, no code required',
    description='Search permits and contractors from your browser. Spot active projects, track market trends, and export to your CRM. No SQL. Zero dev time.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    illustration_src='/images/solutions/permit-database/hero.svg',
    illustration_alt='Shovels Online — permit and contractor search interface') }}

{# ── Features (F1–F6) — same layout as industry use cases; numbers are
   F1…F6 instead of 01…02. Images reuse existing industry-page screenshots
   where the Notion copy calls for it; F5 (CSV export) is net-new → TBD. #}
{% set features = [
    {
        'number': '01',
        'title': 'Track construction activity',
        'description': 'Search nationwide permits by address, city, state, contractor, permit type, project value, and more. Filter large datasets in seconds and uncover the construction activity that matters to your business.',
        'image_src': '/images/industries/real-estate/uc2-development-pipeline.png',
        'image_alt': 'Shovels app — permit search results filtered across a target area',
    },
    {
        'number': '02',
        'title': 'Find the right contractors',
        'description': 'Find contractors by specialty, location, license, or performance and map them to permits, inspections, and project history. Evaluate companies and identify new opportunities from a single profile.',
        'image_src': '/images/industries/home-services/uc1-contractor-marketplace.png',
        'image_alt': 'Shovels app — contractor detail showing license status, permit history, and trade type',
    },
    {
        'number': '03',
        'title': 'Understand your market',
        'description': 'Analyze permit volume, approval times, active contractors, and construction trends across cities, counties, and ZIP codes. Compare markets to understand where activity is growing.',
        'image_src': '/images/industries/building-materials/uc5-market-comparative.png',
        'image_alt': 'Bar chart of permit volume by work type across two target metros',
    },
    {
        'number': '04',
        'title': 'Reach decision-makers faster',
        'description': 'Access phone numbers, emails, websites, and property-level contact data for millions of contractors and residential properties. Build prospect lists faster and export directly into your existing workflow.',
        'image_src': '/images/industries/insurance/uc2-leads.png',
        'image_alt': 'Lead generation view — permit search with contractor contact data',
    },
    {
        'number': '05',
        'title': 'Export data instantly',
        'description': 'Export permit, contractor, and market data to CSV in seconds. Move data into spreadsheets, CRM systems, BI tools, or internal workflows without writing a single line of code.',
        'image_src': '',
        'image_alt': 'CSV export / download dialog in Shovels Online (net-new screenshot)',
    },
    {
        'number': '06',
        'title': 'Track future development',
        'description': 'Track planning, zoning, and land-use decisions months before permits are filed. Decisions data surfaces development activity early, so you can identify opportunities before competitors do.',
        'image_src': '/images/solutions/permit-database/development.svg',
        'image_alt': 'Decisions timeline — zoning and land-use stages ahead of a permit filing',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='',
    heading='Discover more opportunities, faster',
    cases=features) }}

{{ ui_callout.callout(
    variant='warm',
    heading='Not sure where to start? Just ask Charlie.',
    body='Charlie, your AI research assistant, finds exactly what you need from the Shovels data network—just ask in plain English, no SQL or filters required.',
    cta_label='Meet Charlie',
    cta_href='/charlie',
    media_src='/images/shovels-Charlie-pose1.png',
    media_alt='Charlie, the Shovels AI research assistant') }}

{{ ui_hiw.how_it_works(
    eyebrow='How it works',
    heading='From search to export in three steps',
    steps=[
        {
            'number': '1',
            'title': 'Sign up for free',
            'description': 'Create an account at app.shovels.ai. Start exploring permits and contractors right away.',
            'icon': 'sparkles',
        },
        {
            'number': '2',
            'title': 'Search and filter',
            'description': 'Enter a city, ZIP code, or address. Filter by permit type, contractor specialty, job value, and date range.',
            'icon': 'map_pin',
        },
        {
            'number': '3',
            'title': 'Export to CSV or your CRM',
            'description': 'Download filtered results with one click. Import into Salesforce, HubSpot, or any spreadsheet instantly.',
            'icon': 'file_text',
        },
    ]) }}

{{ ui_ind.industries_strip() }}

{% include 'sections/coverage.html' %}

{# Links to /solutions/api — 404 in preview until that page ships. #}
{{ ui_callout.callout(
    variant='green',
    heading='Need to bring this data into your own product or workflow?',
    body='The Shovels API gives you programmatic access to the same permit and contractor data, queryable by address or contractor name, with no scraping or manual exports required.',
    cta_label='Explore the Shovels API',
    cta_href='/solutions/api') }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What is Shovels Online?',
            'a': 'Shovels Online is a web application for exploring nationwide U.S. building permits and contractor data without writing any code. Search, filter, and download records by location, permit type, contractor specialty, and more.',
        },
        {
            'q': 'Do I need technical skills to use it?',
            'a': 'No. Shovels Online is built for sales, operations, and marketing teams who need permit intelligence without SQL or engineering resources. If you can use a spreadsheet, you can use Shovels Online.',
        },
        {
            'q': 'How much of the U.S. is covered?',
            'a': 'Shovels covers approximately 85% of the U.S. population with permit and contractor data from ' ~ STATS.jurisdictions ~ ' jurisdictions, across every state and most major metro areas. See the full coverage map at shovels.ai/coverage.',
        },
        {
            'q': 'Does it include contractor contact information?',
            'a': 'Yes. Shovels includes phone numbers, emails, and website URLs for ' ~ STATS.contractors ~ ' contractors, plus contact information for 30M residential properties. All of it is exportable to CSV with one click.',
        },
        {
            'q': 'How do I export data?',
            'a': 'Download permit or contractor search results to CSV with a single click. You can export up to 1,000 records per export. For larger datasets, segment by geography or upgrade to the API, which has no result limits.',
        },
        {
            'q': 'What is Decisions data?',
            'a': 'Shovels Decisions provides intelligence from city council meetings and planning board discussions, including zoning changes, development approvals, and project timelines. It gives you visibility into projects months before permits are filed.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to explore construction activity?',
    description="Start your free trial and see what's being built in your market today.",
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup') }}
