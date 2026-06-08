Title: Contractor Intelligence for Home Services Platforms
Description: Home improvement leads for home services platforms. Generate roofing, HVAC, and renovation leads from real permit activity, and verify contractors at scale.
slug: home-services-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Contractor intelligence for home services platforms',
    description='Generate home improvement leads from active renovation permits and verify contractors at scale.',
    illustration_src='/images/industries/home-services/hero.svg',
    illustration_alt='Home services hero illustration') }}

{# Static 6-logo industry strip — full set, pending legal sign-off. #}
{% set home_services_logos = [
    {'src': '/images/logos/angi.svg', 'alt': 'Angi'},
    {'src': '/images/logos/houzz.svg', 'alt': 'Houzz'},
    {'src': '/images/logos/pearl-certification.svg', 'alt': 'Pearl Certification', 'height': 28},
    {'src': '/images/logos/hawkins-service.png', 'alt': 'Hawkins Service Co', 'height': 28},
    {'src': '/images/logos/jukebox-health.png', 'alt': 'Jukebox Health', 'height': 24},
    {'src': '/images/logos/peakzi.png', 'alt': 'Peakzi', 'height': 28},
] %}

{{ ui_grid.logo_grid(logos=home_services_logos, heading='TRUSTED BY HOME SERVICES PLATFORMS') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of home services platforms and enterprise operators. Contractor records, permit data, and lead intelligence are protected by controls independently verified over a sustained period.') }}

{% set home_services_cases = [
    {
        'number': '01',
        'title': 'Build a contractor marketplace on verified permit data',
        'description': 'Don’t rely on self-reported profiles or stale directories. See which contractors are actively pulling permits, what trades they work in, and where they operate.',
        'bullets': [
            'Find active contractors by trade, geography, and permit volume',
            'Enrich contractor profiles with verified work history and job counts',
            'Filter by license status, trade type, and active jurisdiction',
            'Onboard contractors with data-backed verification at signup',
        ],
        'image_src': '/images/industries/home-services/uc1-contractor-marketplace.png',
        'image_alt': 'Shovels app — contractor detail showing license status, permit history, trade type, and active permit count',
    },
    {
        'number': '02',
        'title': 'Reach homeowners the moment a project starts',
        'description': 'Home renovation permits are filed before the first contractor arrives. Turn permit filings into home renovation leads so you can reach homeowners at peak intent.',
        'bullets': [
            'Identify homeowners with active permits by trade type and geography',
            'Target renovation projects by job value and permit type',
            'Reach homeowners before competitors know a project has started',
            'Layer permit data over resident records for direct homeowner outreach',
            'Look up property ownership by address to reach owners directly, not just occupants',
        ],
        'image_src': '/images/industries/home-services/uc2-homeowner-intent.svg',
        'image_alt': "A homeowner in a half-demo'd kitchen, phone in hand, receiving a perfectly timed message from a home services platform — peak intent, first contact",
        'framed': False,
    },
    {
        'number': '03',
        'title': 'Analyze demand by trade and geography',
        'description': 'Get a real-time view of where HVAC, roofing, electrical, and plumbing demand is growing. See which ZIP codes have high remodel activity to determine where to expand.',
        'bullets': [
            'Track permit volume by trade type across any market or ZIP',
            'Identify trades with rising activity for supply-side recruitment',
            'Benchmark demand across markets to prioritize expansion',
            'Monitor seasonal permit patterns to optimize marketing spend',
        ],
        'image_src': '/images/industries/home-services/uc3-demand-by-trade.png',
        'image_alt': 'Shovels app — map filtered to HVAC permits in a metro, showing ZIP-level density',
    },
    {
        'number': '04',
        'title': 'Verify contractor licenses at scale',
        'description': 'Know who is licensed, for what, and where. Shovels standardizes contractor state license throughout the US, normalizing raw classifications into clean, queryable records.',
        'bullets': [
            'Access state license files nationwide in a single dataset',
            'Verify license status, trade classification, and geographic coverage',
            'Match permit records to license data for multi-signal verification',
            'Standardized trade categories to make filtering and querying easy',
        ],
        'image_src': '/images/industries/home-services/uc4-verify-licenses.jpg',
        'image_alt': 'Shovels app — contractor search showing license status, trade class, state, and permit count',
    },
    {
        'number': '05',
        'title': 'Surface high-intent homeowners from renovation permits',
        'description': 'Identify homeowners pulling permits for roofing, HVAC, additions, and remodels who are actively buying right now.',
        'bullets': [
            'Filter permits by renovation type to find high-intent homeowners',
            'Identify homeowners with completed permits for warranty outreach',
            'Layer resident contact data for direct homeowner marketing',
            'Build lookalike audiences from renovation permit activity',
        ],
        'image_src': '/images/industries/home-services/uc5-high-intent-homeowners.png',
        'image_alt': 'Permit filter with remodel and status in review',
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What home services teams can do with Shovels',
    cases=home_services_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Home Services')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What contractor data does Shovels provide?',
            'a': 'Shovels combines permit records with state contractor license files to provide permit history, trade classifications, license status, contact information, and employee data for contractors across 37 states.',
        },
        {
            'q': 'Which home services companies use Shovels?',
            'a': 'Thumbtack, Angi, Houzz, and Housecall Pro use Shovels to find, verify, and enrich contractor data at scale for their contractor marketplace and homeowner products.',
        },
        {
            'q': 'How does Shovels standardize license classifications?',
            'a': 'Shovels normalizes over 3,000 license classifications from 37 states into approximately a dozen clean, standardized trade categories. Original classifications are also provided alongside the standardized versions.',
        },
        {
            'q': 'How often is the data updated?',
            'a': 'Permit data is updated bi-weekly. State contractor license files are refreshed monthly, pulled directly from state licensing boards to ensure accuracy.',
        },
        {
            'q': 'How can home services platforms generate home improvement leads from permit data?',
            'a': 'When a homeowner pulls a permit for a renovation, addition, or replacement — it’s the clearest signal they’re in-market. Shovels makes that signal accessible at scale, so home services platforms can generate home improvement leads based on real project activity rather than intent surveys or ad clicks. Filter by trade type, project value, geography, and permit status to build targeted lead lists updated weekly.',
        },
        {
            'q': 'Can permit data generate roofing leads, HVAC leads, and other trade-specific lists?',
            'a': 'Yes. Shovels tracks permits at the trade level, including roofing, HVAC, electrical, plumbing, and more. Platforms use this to generate roofing leads, HVAC leads, and trade-specific contractor lists from permit data filtered by geography, license type, and permit volume. This supports roofing lead generation at scale and is especially useful for platforms that need to grow contractor supply and homeowner demand in the same markets simultaneously.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to build on the most complete contractor dataset in the US?',
    description='See how Shovels helps home services platforms find, verify, and enrich contractor data at scale.',
    cta_label='Get Started') }}
