Title: Shovels Enterprise: Permit Data Native to Snowflake, BigQuery & Databricks
Description: U.S. building permit and contractor data delivered natively to Snowflake, BigQuery, or Databricks. Custom refresh cadences, SOC 2 Type II, and dedicated support.
slug: solutions/data-feed-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/icons.html' as icons %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/industries_strip.html' as ui_ind %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    eyebrow='Shovels Enterprise',
    h1='Permit data, native to your stack',
    description='U.S. permit and contractor dataset, delivered live to Snowflake, BigQuery, or Databricks. Normalized to one schema, with no pipelines to build or maintain.',
    cta_label='Talk to sales',
    cta_href='/contact',
    illustration_src='/images/solutions/data-feed/hero.svg',
    illustration_alt='Shovels permit and contractor data delivered to your data warehouse') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='We meet the security and compliance requirements of enterprise data teams. Our SOC 2 Type II certification reflects controls independently audited over a sustained period—and we complete security questionnaires, sign DPAs, and share audit reports as part of your procurement process.',
    cta_label='View security documentation →',
    cta_href='https://trust.shovels.ai/') }}

{# ── Coded feature visuals (light cards + one dark chart). The schema
   fields and chart values are illustrative, not an exact data contract. #}

{% set f1_media %}
<div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
  <div class="flex items-stretch">
    {# Source node — boosted green outline box; stretches to the full
       height of the warehouse stack for balance. #}
    <div class="flex w-44 shrink-0 flex-col items-center justify-center gap-4 rounded-2xl border border-shovels-primary px-6">
      <img src="/images/shovels-navbar-logo.svg" alt="Shovels" class="h-9 w-auto">
      {{ icons.database(class='size-8 text-shovels-primary') }}
    </div>
    {# Connector — source stub to the vertical bus; per-box stubs + dots.
       Bus insets (top/bottom-12) = half a box height (h-24), so it spans
       the first to last box centers. #}
    <div class="relative w-12 shrink-0" aria-hidden="true">
      <span class="absolute left-1/2 top-12 bottom-12 w-px -translate-x-1/2 bg-gray-300"></span>
      <span class="absolute left-0 top-1/2 h-px w-1/2 -translate-y-1/2 bg-gray-300"></span>
    </div>
    {# Warehouse boxes — square-ish, centered enlarged glyph #}
    <div class="flex flex-1 flex-col gap-4">
      {% for logo, name in [
          ('snowflake.svg', 'Snowflake'),
          ('bigquery.svg', 'BigQuery'),
          ('databricks.png', 'Databricks'),
      ] %}
      <div class="relative flex h-24 items-center justify-center rounded-2xl bg-gray-50 ring-1 ring-gray-100">
        <span class="absolute right-full top-1/2 h-px w-6 -translate-y-1/2 bg-gray-300" aria-hidden="true"></span>
        <span class="absolute right-full top-1/2 size-2 -translate-y-1/2 translate-x-1/2 rounded-full bg-shovels-primary" aria-hidden="true"></span>
        <img src="/images/logos/{{ logo }}" alt="{{ name }}" class="size-14 object-contain">
      </div>
      {% endfor %}
    </div>
  </div>
</div>
{% endset %}

{% set f2_media %}
<div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
  <div class="flex items-center justify-between">
    <span class="font-medium text-gray-900">June 2026</span>
    <span class="rounded-full bg-shovels-primary/10 px-2.5 py-1 text-xs font-medium text-shovels-primary">Custom cadence available</span>
  </div>
  <div class="mt-4 grid grid-cols-7 gap-1 text-center text-xs">
    {% for d in ['S','M','T','W','T','F','S'] %}<span class="py-1 font-medium text-gray-400">{{ d }}</span>{% endfor %}
    <span></span>
    {% for day in range(1, 31) %}
    <span class="flex aspect-square items-center justify-center rounded-md {% if day in [1, 15] %}bg-shovels-primary font-semibold text-white{% else %}text-gray-600{% endif %}">{{ day }}</span>
    {% endfor %}
  </div>
  <div class="mt-5 grid grid-cols-3 gap-3 border-t border-gray-100 pt-4 text-center">
    <div><p class="text-sm font-semibold text-gray-900">1st &amp; 15th</p><p class="text-xs text-gray-500">standard delivery</p></div>
    <div><p class="text-sm font-semibold text-gray-900">+7.2M</p><p class="text-xs text-gray-500">records / cycle</p></div>
    <div><p class="text-sm font-semibold text-gray-900">SLA</p><p class="text-xs text-gray-500">enterprise terms</p></div>
  </div>
</div>
{% endset %}

{% set f3_media %}
<div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
  <div class="grid grid-cols-2 gap-3">
    {% for tbl, fields in [
        ('permits', ['permit_id', 'status', 'job_value', 'tags[]']),
        ('contractors', ['license_no', 'trade', 'pass_rate', 'permits[]']),
        ('property', ['parcel_id', 'use_type', 'year_built', 'sqft']),
        ('decisions', ['decision_id', 'jurisdiction', 'hearing_at', 'permit_id']),
    ] %}
    <div class="rounded-lg border border-gray-200 bg-gray-50 p-3">
      <p class="font-mono text-xs font-semibold text-shovels-primary">{{ tbl }}</p>
      <ul class="mt-2 space-y-1">
        {% for f in fields %}<li class="font-mono text-[11px] text-gray-500">{{ f }}</li>{% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
  <p class="mt-4 text-center font-mono text-xs text-gray-400">one unified schema &middot; analytics &amp; AI-ready</p>
</div>
{% endset %}

{% set f5_media %}
<div class="rounded-xl bg-gray-900 p-6 shadow-sm ring-1 ring-white/10">
  <div class="flex items-center justify-between">
    <span class="text-sm font-medium text-white">20+ years of permit history</span>
    <span class="font-mono text-xs text-gray-400">analytics-ready</span>
  </div>
  <div class="mt-6 flex h-32 items-end gap-1.5">
    {% for h in [12, 16, 14, 20, 22, 26, 24, 30, 33, 38, 35, 42, 46, 44, 50, 57, 54, 63, 70, 76, 84, 92] %}
    <div class="flex-1 rounded-t {% if loop.index > 19 %}bg-[#E9BE51]{% else %}bg-emerald-400/60{% endif %}" style="height: {{ h }}%"></div>
    {% endfor %}
  </div>
  <div class="mt-3 flex justify-between font-mono text-xs text-gray-500">
    <span>2003</span><span>2014</span><span>2026</span>
  </div>
</div>
{% endset %}

{% set features = [
    {
        'number': '01',
        'title': 'Warehouse-native delivery',
        'description': 'Live data delivered to your environment — <a href="https://app.snowflake.com/marketplace/providers/GZTSZDXJR9D/Shovels" target="_blank" rel="noopener noreferrer" class="font-semibold text-shovels-primary hover:text-shovels-primary/80 hover:underline">Snowflake</a>, <a href="https://console.cloud.google.com/marketplace/product/shovels-b7048/cloud-marketplace-a90e0dec-0ac2-4be6-bc13-15b7c2080b51.cloudpartnerservices.goog?project=shovels-b7048" target="_blank" rel="noopener noreferrer" class="font-semibold text-shovels-primary hover:text-shovels-primary/80 hover:underline">BigQuery</a>, Databricks, or parquet files to S3, GCS, or Azure. We ingest, normalize, and maintain the pipeline so your team can focus on analysis.',
        'media': f1_media,
    },
    {
        'number': '02',
        'title': 'Custom refresh cadences',
        'description': 'Choose standard twice-monthly updates or a custom delivery schedule aligned to your workflow, reporting needs, and SLA requirements. Receive data when your business needs it.',
        'media': f2_media,
    },
    {
        'number': '03',
        'title': 'Full schema access',
        'description': 'Access every permit, contractor, property, and decision field through a unified analytics and AI-ready schema. No jurisdiction-by-jurisdiction mapping or cleanup required. Put our interconnected tables to work for your specific needs.',
        'media': f3_media,
    },
    {
        'number': '04',
        'title': 'Dedicated support',
        'description': 'Work directly with a dedicated customer success and solutions architect who helps your team onboard, integrate, and operationalize the data. Get answers from experts, not a support queue.',
        'image_src': '/images/industries/building-materials/uc3-dealer-intel.svg',
        'image_alt': 'A Shovels solutions architect working alongside a customer data team',
        'framed': False,
    },
    {
        'number': '05',
        'title': '20+ years of history',
        'description': 'Access the complete permit backlog, not just recent records. Train models, analyze long-term trends, and backfill workflows with more than 20 years of construction activity — or use real-time city decisions and net-new permit, contractor, and property data.',
        'media': f5_media,
    },
] %}

{{ ui.use_case_section(
    eyebrow='ENTERPRISE',
    heading='Enterprise-ready from day one',
    cases=features) }}

{{ ui_ind.industries_strip(heading='TRUSTED BY DATA TEAMS IN') }}

{# Coverage — shared include as a placeholder; Enterprise-specific copy
   updates pending from the team (may need a parameterized variant). #}
{% include 'sections/coverage.html' %}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'How is data delivered to my warehouse?',
            'a': 'Shovels delivers data natively to Snowflake, BigQuery, and Databricks. We handle the transfer directly with no ETL pipelines or middleware required on your end. Custom delivery schedules are available for enterprise contracts.',
        },
        {
            'q': 'Can I trial the data before committing?',
            'a': 'Yes. We can deliver a sample dataset directly to your Snowflake, BigQuery, or Databricks environment so your team can evaluate coverage, schema, and data quality before signing. We also publish public marketplace listings on Snowflake and BigQuery.',
        },
        {
            'q': 'How complete is the coverage?',
            'a': 'Shovels covers approximately 85% of the U.S. population across ' ~ STATS.jurisdictions ~ " jurisdictions, all normalized to a single schema. You won't need to handle jurisdiction-by-jurisdiction variation. A full coverage dashboard is available at shovels.ai/coverage.",
        },
        {
            'q': 'How often is the data refreshed?',
            'a': 'Standard delivery includes updates on the 1st and 15th of each month, with 5-10 million new records per cycle. Custom refresh cadences are available for enterprise contracts with specific SLA requirements.',
        },
        {
            'q': 'What does the support model look like?',
            'a': 'Enterprise customers get a dedicated solutions architect for onboarding, integration, and ongoing support. We also respond to security questionnaires, sign DPAs, and provide SOC 2 Type II documentation as part of any procurement process.',
        },
        {
            'q': 'How do I make the case internally for a permit data subscription?',
            'a': 'The ROI framing depends on your use case — sales prospecting, market sizing, risk modeling, or network planning. Our team can help you build a business case with sample data in your environment and a coverage report for your target markets.',
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Construction intelligence, delivered your way',
    description='The most complete permit dataset available, delivered to your stack.',
    cta_label='Talk to sales',
    cta_href='/contact') }}
