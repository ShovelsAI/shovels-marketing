Title: Insurance preview — Industry-page template progress
Description: Sandbox preview of the Insurance Industry page as components come online. Not linked from anywhere; replace with the real insurance.md when shipped.
slug: insurance-preview
status: hidden

{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/resources.html' as ui_res %}
{% import 'macros/final_cta.html' as ui_cta %}

{# ========================================
   HERO SECTION — THREE WIDTH VARIATIONS
   ======================================== #}

{# V1: CURRENT LAYOUT (7/12 text, 5/12 illustration at ~640px) #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-24 px-6 md:pt-28 md:pb-32 md:px-10">
  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>

  <div class="relative mx-auto max-w-6xl">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-10 md:gap-16 items-center">
      <div class="md:col-span-7">
        <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">INSURANCE</span>
        <h1 class="mt-4 text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">Property intelligence for insurance providers</h1>
        <p class="mt-6 text-lg text-gray-500">Underwrite with verified property data, validate claims faster, and find new business based on real construction activity.</p>
        <div class="mt-8">
          <a href="https://app.shovels.ai/signup/" class="inline-block rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get started</a>
        </div>
      </div>
      <div class="md:col-span-5">
        <img src="/images/industries/insurance/hero.svg" alt="Insurance hero illustration" class="block w-full h-auto" />
      </div>
    </div>
  </div>
</section>

{# V3: EQUAL SPLIT 6/12 + 6/12 (50/50 layout, image at ~768px) #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-24 px-6 md:pt-28 md:pb-32 md:px-10">
  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>

  <div class="relative mx-auto max-w-6xl">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-10 md:gap-16 items-center">
      <div class="md:col-span-6">
        <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">INSURANCE</span>
        <h1 class="mt-4 text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">Property intelligence for insurance providers</h1>
        <p class="mt-6 text-lg text-gray-500">Underwrite with verified property data, validate claims faster, and find new business based on real construction activity.</p>
        <div class="mt-8">
          <a href="https://app.shovels.ai/signup/" class="inline-block rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get started</a>
        </div>
      </div>
      <div class="md:col-span-6">
        <img src="/images/industries/insurance/hero.svg" alt="Insurance hero illustration" class="block w-full h-auto" />
      </div>
    </div>
  </div>
</section>

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
        'image_src': '/images/industries/insurance/uc5-catastrophe.png',
        'image_alt': 'Catastrophe reconstruction illustration',
        'framed': False,
        'image_max_width': '420px',
    },
] %}

{{ ui.use_case_section(
    eyebrow='USE CASES',
    heading='What insurance teams can do with Shovels',
    cases=insurance_cases) }}

{# ========================================
   ENTERPRISE TEAMS SECTION — THREE LAYOUT VARIATIONS
   ======================================== #}

{# V1: CURRENT LAYOUT (left-aligned eyebrow, heading, and columns) #}
<section class="w-full bg-shovels-dark px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div>
      <span class="inline-block rounded-full border border-shovels-secondary/30 bg-shovels-secondary/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-secondary">Data Delivery</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-white md:text-4xl">Built for enterprise teams</h2>
    </div>
    <div class="mt-16 grid grid-cols-1 gap-10 md:grid-cols-3 md:gap-8">
      <div>
        <img src="/images/illustrations/enterprise-icon-api-feed.svg" alt="API and data feed delivery" class="size-16" />
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Access our data via our API or data feed</h3>
        <p class="mt-2 text-sm text-gray-300">Query directly, or receive structured feeds via SFTP, Snowflake, BigQuery, or Databricks. Customized solutions are also available.</p>
      </div>
      <div>
        <img src="/images/illustrations/enterprise-icon-ai-classified.svg" alt="AI-classified permits" class="size-16" />
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">AI-classified permits</h3>
        <p class="mt-2 text-sm text-gray-300">Clean, structured inputs out of the box. No raw text parsing required.</p>
      </div>
      <div>
        <img src="/images/illustrations/enterprise-icon-updates.svg" alt="Twice-monthly data updates" class="size-16" />
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Updated twice a month</h3>
        <p class="mt-2 text-sm text-gray-300">Millions of new records are added each cycle.</p>
      </div>
    </div>
  </div>
</section>

{# V2: CENTERED LAYOUT (centered eyebrow, centered heading, centered columns) #}
<section class="w-full bg-shovels-dark px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-secondary/30 bg-shovels-secondary/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-secondary">Data Delivery</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-white md:text-4xl">Built for enterprise teams</h2>
    </div>
    <div class="mt-16 grid grid-cols-1 gap-10 md:grid-cols-3 md:gap-8">
      <div class="text-center">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-api-feed.svg" alt="API and data feed delivery" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Access our data via our API or data feed</h3>
        <p class="mt-2 text-sm text-gray-300">Query directly, or receive structured feeds via SFTP, Snowflake, BigQuery, or Databricks. Customized solutions are also available.</p>
      </div>
      <div class="text-center">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-ai-classified.svg" alt="AI-classified permits" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">AI-classified permits</h3>
        <p class="mt-2 text-sm text-gray-300">Clean, structured inputs out of the box. No raw text parsing required.</p>
      </div>
      <div class="text-center">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-updates.svg" alt="Twice-monthly data updates" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Updated twice a month</h3>
        <p class="mt-2 text-sm text-gray-300">Millions of new records are added each cycle.</p>
      </div>
    </div>
  </div>
</section>

{# V3: CARD-BASED LAYOUT (centered header, cards with subtle background, more visual separation) #}
<section class="w-full bg-shovels-dark px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-secondary/30 bg-shovels-secondary/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-secondary">Data Delivery</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-white md:text-4xl">Built for enterprise teams</h2>
    </div>
    <div class="mt-16 grid grid-cols-1 gap-10 md:grid-cols-3 md:gap-8">
      <div class="rounded-lg border border-white/10 bg-white/5 p-8 text-center backdrop-blur-sm">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-api-feed.svg" alt="API and data feed delivery" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Access our data via our API or data feed</h3>
        <p class="mt-2 text-sm text-gray-300">Query directly, or receive structured feeds via SFTP, Snowflake, BigQuery, or Databricks. Customized solutions are also available.</p>
      </div>
      <div class="rounded-lg border border-white/10 bg-white/5 p-8 text-center backdrop-blur-sm">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-ai-classified.svg" alt="AI-classified permits" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">AI-classified permits</h3>
        <p class="mt-2 text-sm text-gray-300">Clean, structured inputs out of the box. No raw text parsing required.</p>
      </div>
      <div class="rounded-lg border border-white/10 bg-white/5 p-8 text-center backdrop-blur-sm">
        <div class="flex justify-center">
          <img src="/images/illustrations/enterprise-icon-updates.svg" alt="Twice-monthly data updates" class="size-16" />
        </div>
        <h3 class="mt-6 text-lg font-medium text-shovels-secondary">Updated twice a month</h3>
        <p class="mt-2 text-sm text-gray-300">Millions of new records are added each cycle.</p>
      </div>
    </div>
  </div>
</section>

{% include 'sections/coverage.html' %}

{# Resources — currently hardcoded with 3 insurance-relevant posts.
   Dynamic filtering by tag2/tags is a planned follow-up; see COMPONENTS.md "Open questions". #}
{{ ui_res.resources_section(
    articles=[
        {
            'url': '/blog/roofing-permit-data-insurance-roof-age/',
            'title': "The Roof Age Problem: What Permit Data Reveals About America's Rooftops",
            'image_src': '/images/blog_images/roofing-permit-data-insurance-roof-age-hero.png',
            'image_alt': 'Aerial view of a residential neighborhood',
        },
        {
            'url': '/blog/la-wildfire-rebuild-permit-data/',
            'title': 'LA Wildfires Recovery: What the Permit Record Shows',
            'image_src': '/images/blog_images/la-wildfire-rebuild-permit-data-hero.png',
            'image_alt': 'Aftermath of the LA wildfires',
        },
        {
            'url': '/blog/unpermitted-work/',
            'title': 'What Is Unpermitted Work? Risks, Disclosure, and What to Do About It',
            'image_src': '/images/blog_images/unpermitted-work-hero.png',
            'image_alt': 'Unpermitted construction work',
        },
    ]) }}

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
