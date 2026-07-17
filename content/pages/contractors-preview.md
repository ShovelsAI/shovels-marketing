Title: Contractors Data
Description: Search contractor profiles built from permit history: licenses, verified contacts, specialties, work history, and performance metrics for US contractors.
slug: data/contractors-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/use_case.html' as ui_uc %}
{% import 'macros/record_fields.html' as ui_rec %}
{% import 'macros/data_delivery.html' as ui_dd %}
{% import 'macros/data_types.html' as ui_dt %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{# ── §1 HERO ─────────────────────────────────────────────────────────── #}
{{ ui_hero.hero(
    eyebrow='Data · Contractors',
    h1='Contractor data, built from the work they actually do',
    description='Shovels builds a profile for every contractor in our permit dataset: licenses, contacts, specialties, and a verifiable track record of permits pulled.',
    illustration_src='/images/data/contractors/hero.svg',
    illustration_alt='Illustration of a contractor profile built from permit history',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/',
    secondary_cta_label='See our data dictionary',
    secondary_cta_href='/data-dictionary#contractors') }}

{# ── §2 SOC 2 TRUST BANNER (generic body) ───────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.') }}

{# ── §3 PROCESS ─────────────────────────────────────────────────────── #}
{{ ui_hiw.how_it_works(
    eyebrow='Our process',
    heading='From permit records to contractor intelligence',
    anchor='process',
    steps=[
        {'number': '1', 'title': 'Collected at the source',
         'description': 'Contractor details come from permit applications, state licensing boards, and business registrations.'},
        {'number': '2', 'title': 'Deduplicated and grouped',
         'description': 'Related records merge into one profile, with group IDs linking branches of the same company.'},
        {'number': '3', 'title': 'Enriched',
         'description': 'Licenses, employee counts, websites, and social profiles are layered onto every record.'},
        {'number': '4', 'title': 'Scored by real work',
         'description': 'Permit history powers every metric: volume, job values, durations, and inspection pass rates.'},
    ]) }}

{# ── §4 WHAT'S IN EVERY CONTRACTOR RECORD ────────────────────────────── #}
{{ ui_rec.record_fields(
    heading="What's in every contractor record",
    cta_label='See more in our data dictionary',
    cta_href='/data-dictionary#contractors',
    fields=[
        {'name': 'Specialty', 'description': 'Standardized classification from licenses and permit history: roofing, electrical, HVAC, plumbing, general building, and more.'},
        {'name': 'Contacts', 'description': 'Primary email and phone from recent permits, ranked by frequency, plus website and LinkedIn.'},
        {'name': 'License', 'description': 'Number, issuing state, and status (active, expired, suspended, revoked), from official state license files.'},
        {'name': 'Work history', 'description': "Every permit they've pulled, tallied by work type and status."},
        {'name': 'Performance', 'description': 'Average job value, construction duration, and inspection pass rate.'},
        {'name': 'Company profile', 'description': 'Employee range, revenue range, business type, and Google rating.'},
    ]) }}

{# ── §5 USE CASES ───────────────────────────────────────────────────── #}
{{ ui_uc.use_case_section(
    eyebrow='The data',
    heading="Know who's behind the work",
    cases=[
        {
            'number': '01',
            'title': 'Find the right contractors, not just a list',
            'description': 'See the real difference between contractors. Filter by project history.',
            'bullets': [
                'Filter by standardized specialty and territory',
                'Separate pure-play specialists from generalists using their permit mix',
                'Size companies by permit volume and employee count',
            ],
            'image_src': '/images/industries/building-materials/uc1-trade-metro.png',
            'image_alt': 'Most-active contractors ranked in a table',
        },
        {
            'number': '02',
            'title': 'Reach contractors with verified contacts',
            'description': 'Get contact data, ranked by recent activity, directly from permit applications.',
            'bullets': [
                'Primary email and phone from recent permits',
                'Export to CSV or straight to your CRM',
                'Employee-level contacts with titles and seniority',
            ],
            'image_src': '/images/industries/insurance/uc2-leads.png',
            'image_alt': 'Contractor contact panel with verified emails and phones',
        },
        {
            'number': '03',
            'title': 'Vet and monitor contractors',
            'description': 'Review license status from official state files, backed by work history.',
            'bullets': [
                'Verify license status before you onboard or underwrite',
                'Review real work history, not self-reported claims',
                'Track metrics like inspection pass rate and construction duration',
            ],
            'image_src': '/images/industries/home-services/uc1-contractor-marketplace.png',
            'image_alt': 'Contractor profile with job value, pass rate, and duration metrics',
        },
        {
            'number': '04',
            'title': 'Source and enrich deals',
            'description': 'Use contractor profiles to find targets, enrich lists, and read local markets.',
            'bullets': [
                'Enrich your existing lists by business name or license number',
                'Map service areas from where contractors actually pull permits',
                'Benchmark market share by trade and geography',
            ],
            'image_src': '/images/industries/building-materials/uc2-target-metro.png',
            'image_alt': 'Territory density map with a permit panel',
        },
    ]) }}

{# ── §6 DATA DELIVERY (dark) ─────────────────────────────────────────── #}
{{ ui_dd.data_delivery(
    eyebrow='Delivery',
    heading='One unified dataset, three ways to access it',
    dark=True,
    cards=[
        ('Shovels Online', 'Explore, filter, and export permit, contractor, and decision data in our self-serve web app.', '/permit-database', 'shovels-globe'),
        ('Shovels API', 'Build construction intelligence into your product, CRM, or internal tools with our REST API.', '/api', 'data-api'),
        ('Enterprise', 'Get the full dataset as parquet files or table shares in Snowflake, Databricks, or BigQuery.', '/data-feed', 'enterprise-box'),
    ]) }}

{# ── §7 INDUSTRIES STRIP ────────────────────────────────────────────── #}
{{ ui_ind.industries_strip() }}

{# ── §8 COVERAGE ────────────────────────────────────────────────────── #}
{% include 'sections/coverage.html' %}

{# ── §9 EXPLORE THE CONNECTED DATASETS (minus Contractors) ───────────── #}
{{ ui_dt.data_types(
    eyebrow='Data types',
    heading='Explore the connected datasets',
    description='Every contractor is linked across datasets, so you see the full picture — the projects, the properties, and the people behind the work.',
    exclude='Contractors') }}

{# ── §10 FAQ ────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {'q': 'What is contractor data?', 'a': "Contractor data is a profile of a licensed construction business: who they are, what they're licensed to do, and what work they've actually performed. Shovels builds these profiles from permit applications, state licensing boards, and business registrations, then keeps them current with every data release."},
        {'q': 'Where do contractor contacts come from?', 'a': 'Primarily from permit applications. Contractors have every incentive to list working phone numbers and emails on permits, so the contact data is unusually reliable. We rank each contact by how often and how recently it appears, and enrich profiles with websites and LinkedIn URLs.'},
        {'q': 'How does Shovels handle duplicate contractors?', 'a': 'Every contractor gets a persistent Shovels ID, and related records (branches, subsidiaries, name variations) are linked with a group ID. You see one clean profile per business instead of a dozen fragments.'},
        {'q': 'What fields are included in a contractor record?', 'a': 'Business name and DBA, standardized specialty classification, license number and status, contact details, employee and revenue ranges, Google rating, and permit-derived metrics like total permits, average job value, construction duration, and inspection pass rate. Full list in the data dictionary.'},
        {'q': 'Can I get contacts for individual employees?', 'a': 'Yes. Contractor records link to employee data with names, job titles, seniority, and business and personal emails, so you can reach the right person, not just the front office.'},
        {'q': 'How do I access contractor data?', 'a': 'Three ways: search and export in Shovels Online, integrate the Shovels API, or license the full dataset via Snowflake, Databricks, or BigQuery. The free trial includes contractor search, no credit card required.'},
    ]) }}

{# ── §11 FINAL CTA ──────────────────────────────────────────────────── #}
{{ ui_cta.final_cta(
    heading='Find the contractors behind the work',
    description='Search for free, or talk to us about API and enterprise delivery.',
    cta_label='Get started',
    cta_href='https://app.shovels.ai/signup/') }}
