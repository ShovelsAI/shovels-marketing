Title: Property Intelligence for Insurance Providers
Description: Permit-backed property risk data for insurance providers. Verify roofs, validate claims, and find new business — a modern BuildFax alternative.
slug: insurance-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/logo_grid.html' as ui_grid %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Property intelligence for insurance providers',
    description='Underwrite with verified property data, validate claims faster, and find new business based on real construction activity.',
    illustration_src='/images/industries/insurance/hero.svg',
    illustration_alt='Insurance hero illustration') }}

{# Static logo grid — 3 of 4 sourced; Trinh Insurance (trinhinsurance.com)
   pending. comeryx.png has a baked-in background — needs knockout. #}
{% set insurance_logos = [
    {'src': '/images/logos/scription.png', 'alt': 'Scription', 'height': 26},
    {'src': '/images/logos/drodat.png', 'alt': 'Drodat', 'height': 28},
    {'src': '/images/logos/comeryx.png', 'alt': 'Comeryx', 'height': 28},
] %}

{{ ui_grid.logo_grid(logos=insurance_logos, heading='TRUSTED BY INSURANCE TEAMS') }}

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
        'image_src': '/images/industries/insurance/uc1-underwrite.png',
        'image_alt': 'Underwriting view in Shovels — property detail with permit history',
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
        'image_src': '/images/industries/insurance/uc2-leads.png',
        'image_alt': 'Lead generation view — permit search filtered to recent residential permits',
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
        'image_src': '/images/industries/insurance/uc3-verify-claims.png',
        'image_alt': 'Claims verification view — permit record matched against claim',
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
        'image_src': '/images/industries/insurance/uc4-close-gap.png',
        'image_alt': 'Revenue-gap analysis — permit search filtered to additions and renovations',
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
        'image_src': '/images/industries/insurance/uc5-catastrophe.svg',
        'image_alt': 'Catastrophe reconstruction illustration',
        'framed': False,
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What insurance teams can do with Shovels',
    cases=insurance_cases) }}

{% include 'sections/enterprise_teams.html' %}

{% include 'sections/coverage.html' %}

{{ ui_res.resources_section(
    articles=get_industry_articles('Insurance')) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What data is included?',
            'a': 'Shovels data includes building permits, contractor profiles, contractor state license (CSL) files, and property metadata including permit type, project description, valuation, dates, contractor information, and parcel ownership records.',
        },
        {
            'q': 'How is it delivered?',
            'a': 'You can access Shovels via our online platform, REST API, SFTP, or direct cloud integration with Snowflake, BigQuery, or Databricks. Contact us to discuss customized delivery options.',
        },
        {
            'q': 'Is Shovels SOC 2 compliant?',
            'a': 'Yes, we are SOC 2 Type II certified. Documentation is available on request.',
        },
        {
            'q': 'Is Shovels a BuildFax alternative?',
            'a': "The core difference is what the data covers and how it's delivered. BuildFax tracks permits. Shovels tracks permits and the contractors who pulled them, including standardized state license (CSL) files across 37 states, so you can verify contractor credentials, not just construction activity. We deliver via modern API or direct cloud integration with no legacy batch formats and no long-term lock-in.",
        },
        {
            'q': 'Do you have roofing-specific data?',
            'a': 'Yes. We tag roofing permits using AI classification, which lets you query roof replacement activity by address, ZIP, or county. This is useful for risk banding, renewal triggers, and claims verification. Learn more about our roofing data by contacting us.',
        },
        {
            'q': 'Do you cover rural areas?',
            'a': 'Yes, and actively expanding. Our team targets rural and offline jurisdictions underserved by existing data providers. We also prioritize coverage based on customer demand. If you need specific jurisdictions, let us know.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to underwrite what was actually built?',
    description='See how permit and contractor data fits into your underwriting, claims, and growth workflows.') }}
