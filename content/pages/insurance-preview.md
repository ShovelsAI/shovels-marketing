Title: Insurance preview — Industry-page template progress
Description: Sandbox preview of the Insurance Industry page as components come online. Not linked from anywhere; replace with the real insurance.md when shipped.
slug: insurance-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}

{{ ui_hero.hero(
    eyebrow='STRATEGIC INSIGHTS',
    h1='Property intelligence for insurance providers',
    description='Underwrite with verified property data, validate claims faster, and find new business based on real construction activity.',
    illustration_src='/images/industries/insurance/hero.svg',
    illustration_alt='Insurance hero illustration') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise insurance carriers. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{% set insurance_cases = [
    {
        'number': '01',
        'title': 'Underwrite what was actually built',
        'description': 'Permit records show exactly what was built, when, and by whom, giving underwriters a verified baseline for property risk.',
        'bullets': [
            'Flag aging roofs and high-risk properties before a claim happens',
            'Verify contractor licenses across the nation with standardized CSL data',
            'Enrich COPE data with permit records and surface recent improvements that affect pricing',
            'Refine portfolio pricing with permit activity layered by ZIP or county',
        ],
        'image_src': '/images/industries/insurance/use-case-placeholder.png',
        'image_alt': 'UC1 placeholder — final tight crop pending from design',
    },
    {
        'number': '02',
        'title': 'Generate insurance leads from permit activity',
        'description': 'Reach contractors and homeowners the moment coverage decisions are made, so you can time your messages for maximum impact.',
        'bullets': [
            'Create and segment lead lists by location, trade, permit type, or property profile',
            "Target builders and contractors for general liability and workers' comp coverage",
            'Reach homeowners and residents after renovations as high-intent prospects for home insurance and warranties',
        ],
        'image_src': '/images/industries/insurance/use-case-placeholder.png',
        'image_alt': 'UC2 placeholder — final tight crop pending from design',
    },
    {
        'number': '03',
        'title': 'Verify claims against the permit of record',
        'description': 'Claims data can be incomplete or inconsistent. Permit records provide an independent source of truth.',
        'bullets': [
            'Flag unpermitted improvements before binding',
            'Match claims to permit records by address and date',
            'Identify discrepancies between reported work and actual permit activity',
            'Run bulk permit validation after catastrophes to prioritize high-risk claims',
        ],
        'image_src': '/images/industries/insurance/use-case-placeholder.png',
        'image_alt': 'UC3 placeholder — final tight crop pending from design',
    },
    {
        'number': '04',
        'title': 'Close the revenue gap in your existing book',
        'description': "What's insured doesn't always match the actual property. Compare your records against real construction activity and find what's missing.",
        'bullets': [
            'Match your book against permit activity to identify unenrolled properties',
            'Surface builder customers whose activity exceeds current coverage',
            'Expand revenue within your existing customer base',
        ],
        'image_src': '/images/industries/insurance/use-case-placeholder.png',
        'image_alt': 'UC4 placeholder — final tight crop pending from design',
    },
    {
        'number': '05',
        'title': 'Sharpen catastrophe models with reconstruction data',
        'description': 'After a major event, reconstruction activity determines how losses develop. Permit data provides a live view so reserves, contractor networks, and cash flow projections stay accurate.',
        'bullets': [
            'Compare post-disaster permit volume to claims reserves to pressure-test your CAT models',
            'Track rebuild timelines by ZIP to forecast cash flow',
            'Monitor contractor activity to activate repair networks',
            'Identify areas where rebuilding lags behind a CAT event',
        ],
        'image_src': '/images/industries/insurance/uc5-catastrophe.png',
        'image_alt': 'Catastrophe reconstruction illustration',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What insurance teams can do with Shovels',
    cases=insurance_cases) }}
