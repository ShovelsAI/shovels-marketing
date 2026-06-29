Title: Infrastructure Intelligence for Telecommunications Companies
Description: Telecom infrastructure data for fiber network planning. Track competitor builds, monitor city councils, and target markets where permits move fastest.
slug: telecommunications-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Infrastructure intelligence for telecommunications companies',
    description='Access telecom infrastructure data across the US, monitor competitor filings, and identify favorable markets for smarter fiber network planning.',
    illustration_src='/images/industries/telecommunications/hero.svg',
    illustration_alt='Telecommunications hero illustration') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise telecommunications carriers and infrastructure operators. Our controls are independently audited over time, clearing the bar for vendor security reviews at large carriers and ISPs.') }}

{% set telecommunications_cases = [
    {
        'number': '01',
        'title': 'Identify new commercial, residential, and industrial developments for network planning',
        'description': 'Get ahead of subscriber demand with the latest residential construction data.',
        'bullets': [
            'Identify new commercial, residential, and industrial construction by subdivision, ZIP, and metro',
            'Detect new build zones months before occupancy and service requests',
            'Prioritize network buildout based on construction density',
            'Align network deployment timelines with construction schedules',
        ],
        'image_src': '/images/industries/telecommunications/uc1-new-developments.svg',
        'image_alt': 'Shovels app — new-construction permit results filtered by location and date, beside a map showing permit clusters across the state',
    },
    {
        'number': '02',
        'title': 'Monitor competitor network permit filings in your service areas',
        'description': 'Compare competitor filings against your network design to identify gaps, protect territory, and prioritize capital.',
        'bullets': [
            'Track competitor network permit filings by geography and carrier',
            'Detect competitive activity in existing service territories early',
            'Identify markets where Tier 1 and Tier 3 ISPs are expanding',
            'Prioritize defensive deployments in high-risk areas',
        ],
        'image_src': '/images/industries/telecommunications/uc2-competitor-filings.svg',
        'image_alt': "Shovels app — a competitor's fiber-optic network permit detail, with location map, timeline, and project description",
    },
    {
        'number': '03',
        'title': 'Target markets where permits move fastest',
        'description': 'Consider approval durations and focus deployments in the right markets.',
        'bullets': [
            'Identify jurisdictions with fast, predictable approval timelines',
            'Compare jurisdictions by approval rate before committing resources',
            'Map contacts and approval patterns for right-of-way planning',
            'Prioritize markets where permits close fastest',
        ],
        'image_src': '/images/industries/telecommunications/uc3-fastest-permits.svg',
        'image_alt': 'A network planner comparing two regions — one flagged fast approvals, one slow — deciding where to deploy fiber first',
        'framed': False,
    },
    {
        'number': '04',
        'title': 'Access city council intelligence before permits are filed',
        'description': 'Get visibility into broadband expansion, franchise agreements, and right-of-way permissions with Shovels Decisions.',
        'bullets': [
            'Track franchise agreement reviews and broadband expansion initiatives',
            'Monitor BEAD funding allocations and council support for infrastructure projects',
            'Identify municipalities prioritizing internet infrastructure investment',
            'Know which markets have council backing before committing capital',
        ],
        'image_src': '/images/industries/telecommunications/uc4-council-intelligence.png',
        'image_alt': 'Shovels Decisions — feed filtered by broadband, infrastructure, or right-of-way keywords',
    },
    {
        'number': '05',
        'title': 'Protect existing infrastructure from construction damage',
        'description': 'Monitor construction activity around critical infrastructure before incidents occur.',
        'bullets': [
            'Set alerts for permit activity near existing network infrastructure',
            'Identify construction projects that could impact underground cable routes',
            'Enable joint trenching by spotting infrastructure work in the same corridors',
            'Coordinate with utilities and contractors before damage occurs',
        ],
        'image_src': '/images/industries/telecommunications/uc5-protect-infrastructure.svg',
        'image_alt': 'An excavator near an urban street with underground cable routes highlighted as a warning — a field engineer coordinating before damage occurs',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What telecom teams can do with Shovels',
    cases=telecommunications_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Telecommunications')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'How does Shovels classify fiber and telecom permits?',
            'a': 'Shovels uses proprietary AI models to tag and classify hundreds of millions of permits for fiber, utility, and infrastructure activity, including ISP-specific permit classification that reveals which carriers are actively building in any market.',
        },
        {
            'q': 'What city council data does Shovels provide for telecom companies?',
            'a': 'Shovels Decisions tracks franchise agreement discussions, broadband expansion initiatives, right-of-way permit debates, and BEAD funding allocation priorities from city councils nationwide, giving you visibility months before permits are filed.',
        },
        {
            'q': 'How does Shovels identify permit-friendly jurisdictions?',
            'a': 'Shovels analyzes historical approval timelines and approval rates across thousands of jurisdictions, helping you route fiber deployment around difficult authorities and focus on markets with faster, more predictable permit processes.',
        },
        {
            'q': 'Can Shovels help track competitive fiber deployments?',
            'a': 'Yes. Our AI-enhanced fiber permit classification reveals where ISPs from Tier 1 carriers like AT&T and Verizon to regional Tier 3 providers are actively building, enabling strategic market entry decisions and investment prioritization.',
        },
        {
            'q': 'How does permit data improve fiber network planning for ISPs?',
            'a': 'Shovels gives ISPs and telecom companies advance notice of where new residential and commercial construction is happening, including the exact permit type, contractor, location, and filing date. Teams use this to prioritize fiber network planning and fiber planning and design decisions: where to extend infrastructure, when to file permits, and which markets have the densest near-term subscriber demand. Data is also available for teams building fiber optic network design workflows.',
        },
        {
            'q': 'What telecom infrastructure data does Shovels provide?',
            'a': 'Shovels aggregates permit and construction data from thousands of US jurisdictions, including fiber-related permits (conduit, aerial, underground, right-of-way) as well as multi-family, commercial, and single-family construction signals. Telecom teams use this data to monitor competitive fiber deployment, identify underserved markets, and inform capital planning for new infrastructure.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to improve planning with permit intelligence?',
    description="See how Shovels helps telecom teams plan faster, compete smarter, and protect what's already in the ground.",
    cta_label='Get Started') }}
