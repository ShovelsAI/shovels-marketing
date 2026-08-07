Title: Pricing
Description: Shovels pricing — a free plan, self-serve Basic and Team plans, and custom Enterprise pricing. Every plan includes the web app, API, CLI, and Charlie AI on one shared credit balance.
slug: pricing-preview
status: hidden

{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/faq.html' as ui_faq %}

{# ── §1 PLANS ─────────────────────────────────────────────────────────
   Four pricing tiers on the refresh card system, then the warm EDL band.
   Grids are responsive (design mock was fixed 1280); price/credit copy is
   authoritative from the pricing design. #}
{% set plans = [
    {'name': 'Free', 'blurb': 'Explore the data before you commit.',
     'price': '$0', 'per': '/mo',
     'rows': [('off', 'No downloadable records'), ('on', '1 year of record history'),
              ('on', '100 results per query'), ('on', '1 seat')],
     'credits': '500 API credits / mo', 'credits_muted': true,
     'support': 'Knowledge Base + email support',
     'cta_label': 'Start free', 'cta_href': 'https://app.shovels.ai/signup/', 'cta_variant': 'outline'},
    {'name': 'Basic', 'featured': true, 'blurb': 'For individuals and independent research.',
     'price': '$599', 'per': '/mo',
     'rows': [('on', '25K downloadable records / mo'), ('on', 'Full historical records'),
              ('on', '1,000 results per query'), ('on', '1 seat')],
     'credits': '25,000 API credits / mo', 'credits_muted': false,
     'support': 'Knowledge Base + email support',
     'cta_label': 'Choose Basic', 'cta_href': 'https://app.shovels.ai/signup/', 'cta_variant': 'solid'},
    {'name': 'Team', 'blurb': 'For small team collaboration.',
     'price': '$999', 'per': '/mo',
     'rows': [('on', '50K downloadable records / mo'), ('on', 'Full historical records'),
              ('on', '1,000 results per query'), ('on', '2 seats')],
     'credits': '50,000 API credits / mo', 'credits_muted': false,
     'support': 'Dedicated customer support',
     'cta_label': 'Choose Team', 'cta_href': 'https://app.shovels.ai/signup/', 'cta_variant': 'solid'},
    {'name': 'Enterprise', 'blurb': 'Enterprise pricing tailored to your needs.',
     'price': 'Custom', 'per': '',
     'rows': [('on', 'Custom downloadable records'), ('on', 'Full historical records'),
              ('on', 'Custom results per query'), ('on', 'Custom seats')],
     'credits': 'Credits sized with you', 'credits_muted': false,
     'support': 'Dedicated customer support',
     'cta_label': 'Talk to sales', 'cta_href': '/contact', 'cta_variant': 'solid'},
] %}
<section class="w-full bg-white px-6 md:px-10 pt-20 pb-24 md:pt-28">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <h1 class="text-balance text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">We&rsquo;re making public data publicly available</h1>
    </div>

    <div class="mt-16 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {% for p in plans %}
      <div class="relative flex flex-col rounded-2xl {{ 'border-2 border-shovels-primary' if p.featured else 'border border-gray-200' }} p-8">
        {% if p.featured %}<span class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-shovels-primary px-3 py-1 text-xs font-semibold uppercase tracking-wider text-white">Most popular</span>{% endif %}
        <h3 class="text-xl font-medium text-gray-900">{{ p.name }}</h3>
        <p class="mt-2 min-h-[40px] text-sm text-gray-500">{{ p.blurb }}</p>
        <p class="mt-6 flex items-baseline gap-1">
          <span class="{{ 'text-3xl' if p.price == 'Custom' else 'text-4xl' }} font-bold tracking-tight text-gray-900">{{ p.price }}</span>
          {% if p.per %}<span class="text-sm text-gray-500">{{ p.per }}</span>{% endif %}
        </p>
        <ul role="list" class="mt-6 flex-auto space-y-2 text-sm text-gray-600">
          {% for state, label in p.rows %}
          <li class="flex min-h-[34px] items-start gap-2">
            {% if state == 'on' %}<span class="text-shovels-primary">&check;</span><span>{{ label }}</span>
            {% else %}<span class="text-gray-300">&ndash;</span><span class="text-gray-400">{{ label }}</span>{% endif %}
          </li>
          {% endfor %}
        </ul>
        <p class="mt-6 rounded-lg {{ 'bg-gray-50' if p.credits_muted else 'bg-shovels-primary/5' }} px-3 py-2 text-sm font-semibold text-shovels-primary">{{ p.credits }}</p>
        <p class="mt-6 min-h-[32px] text-xs text-gray-500">{{ p.support }}</p>
        {% if p.cta_variant == 'solid' %}
        <a href="{{ p.cta_href }}" class="mt-4 block rounded-full bg-shovels-primary px-4 py-2.5 text-center text-sm font-semibold text-white hover:bg-shovels-primary/90">{{ p.cta_label }}</a>
        {% else %}
        <a href="{{ p.cta_href }}" class="mt-4 block rounded-full border border-gray-300 px-4 py-2.5 text-center text-sm font-semibold text-gray-900 hover:border-gray-400 hover:bg-gray-50">{{ p.cta_label }}</a>
        {% endif %}
      </div>
      {% endfor %}
    </div>

    {# Enterprise Data License band — warm callout treatment. #}
    <div class="mt-6 flex flex-col gap-6 rounded-2xl bg-[#E9E1CE] p-8 md:flex-row md:items-center md:gap-8 md:p-10">
      <img src="/images/illustrations/enterprise-box.svg" alt="" class="size-16 shrink-0 md:size-20" />
      <div class="flex-auto">
        <p class="text-lg font-medium text-gray-900 md:text-xl">Looking for bulk data instead of API usage?</p>
        <p class="mt-2 text-sm text-gray-700">Our Enterprise Data License (EDL) delivers every permit, contractor, property, and resident record as parquet files or table shares in <a href="https://app.snowflake.com/marketplace/providers/GZTSZDXJR9D/Shovels" class="font-medium text-shovels-primary hover:text-shovels-primary/80 underline decoration-shovels-primary/30 underline-offset-2">Snowflake</a>, Databricks, or <a href="https://console.cloud.google.com/marketplace/product/shovels-b7048/cloud-marketplace-a90e0dec-0ac2-4be6-bc13-15b7c2080b51.cloudpartnerservices.goog?project=shovels-b7048" class="font-medium text-shovels-primary hover:text-shovels-primary/80 underline decoration-shovels-primary/30 underline-offset-2">BigQuery</a> &mdash; including fields the API doesn&rsquo;t expose. <a href="/solutions/data-feed" class="font-semibold text-shovels-primary hover:text-shovels-primary/80">Learn more <span aria-hidden="true">&rarr;</span></a></p>
      </div>
      <div class="shrink-0"><a href="/contact" class="inline-block whitespace-nowrap rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90">Talk to us <span aria-hidden="true">&rarr;</span></a></div>
    </div>
  </div>
</section>

{# ── §2 COMPARE ───────────────────────────────────────────────────────
   Feature matrix with collapsible groups. Enterprise column is one merged
   "Contact sales" cell (rowspan) that re-syncs as groups open/close. The
   toggle logic is a small self-contained script at the foot of the page.
   Wrapped in overflow-x-auto so the table scrolls on narrow screens. #}
{% set compare = [
    {'key': 'product', 'label': 'Product', 'open': true, 'rows': [
        {'label': 'Shovels Online access', 'vals': ['check', 'check', 'check']},
        {'label': 'API credits per month', 'tip': 'A credit is one record retrieved. Credit limits refresh monthly on your subscription date.',
         'vals': ['500', '25,000', '50,000']},
    ]},
    {'key': 'features', 'label': 'Features', 'open': false, 'rows': [
        {'label': 'Downloadable records per month', 'vals': ['dash', '25K / month', '50K / month']},
        {'label': 'Record history', 'vals': ['1 year', 'Full historical', 'Full historical']},
        {'label': 'Max search results per query', 'vals': ['100 records', '1,000 records', '1,000 records']},
        {'label': 'Seats', 'vals': ['1', '1', '2']},
        {'label': 'Map', 'vals': ['check', 'check', 'check']},
        {'label': 'Charlie AI agent', 'href': '/features/charlie', 'tip': 'Ask permit questions in plain English.', 'vals': ['check', 'check', 'check']},
        {'label': 'CLI', 'href': '/features/cli', 'tip': 'One binary, JSON output, built for terminals and agents.', 'vals': ['check', 'check', 'check']},
    ]},
    {'key': 'data-sets', 'label': 'Data sets', 'open': false, 'rows': [
        {'label': 'Permits', 'href': '/data/permits', 'tip': 'Every building permit we cover, AI-classified into structured records.', 'vals': ['check', 'check', 'check']},
        {'label': 'Contractors', 'href': '/data/contractors', 'tip': 'Contractor profiles with licenses, work history, and contact details.', 'vals': ['check', 'check', 'check']},
        {'label': 'Employees', 'href': 'https://www.shovels.ai/data-dictionary#employees', 'tip': 'Employee counts and roles tied to contractor profiles.', 'vals': ['dash', 'check', 'check']},
        {'label': 'Decisions', 'href': '/data/decisions', 'tip': 'Zoning and development decisions, before a permit is filed.', 'vals': ['check', 'check', 'check']},
        {'label': 'Properties', 'href': '/data/properties', 'tip': 'Parcels and addresses with full permit and ownership history.', 'vals': ['check', 'check', 'check']},
        {'label': 'Residents', 'href': '/data/residents', 'tip': 'Residents and homeowners tied to properties, with contacts.', 'vals': ['check', 'check', 'check']},
    ]},
    {'key': 'support', 'label': 'Support', 'open': false, 'rows': [
        {'label': 'Support', 'vals': ['Knowledge Base + email', 'Knowledge Base + email', 'Dedicated customer support']},
    ]},
] %}
{% macro cmp_cell(v) %}
  {%- if v == 'check' -%}<td class="px-4 py-4 text-center text-shovels-primary">&check;</td>
  {%- elif v == 'dash' -%}<td class="px-4 py-4 text-center text-gray-300">&ndash;</td>
  {%- else -%}<td class="px-4 py-4 text-center font-medium text-gray-900">{{ v }}</td>{%- endif -%}
{% endmacro %}
{% set ns = namespace(total=0) %}
{% for g in compare %}{% for r in g.rows %}{% set ns.total = ns.total + 1 %}{% endfor %}{% endfor %}
<section id="compare" class="w-full bg-white px-6 pb-24 md:px-10">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <h2 class="text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Compare every plan</h2>
      <p class="mt-4 text-lg text-gray-500">All of our datasets are included on every paid plan.</p>
    </div>
    <div class="mt-16 overflow-x-auto rounded-2xl border border-gray-200">
      <table id="compare-table" class="w-full min-w-[720px] border-collapse text-left">
        <thead>
          <tr>
            <th class="bg-gray-50 px-6 py-5 text-sm font-semibold text-gray-900 shadow-[inset_0_-1px_0_rgb(229,231,235)]"><span class="inline-flex items-center gap-3">Shovels plans<button type="button" id="expand-all" class="text-xs font-medium text-shovels-primary underline decoration-shovels-primary/30 underline-offset-2 transition hover:decoration-shovels-primary">Expand all</button></span></th>
            <th class="bg-gray-50 px-4 py-5 text-center text-sm font-semibold text-gray-900 shadow-[inset_0_-1px_0_rgb(229,231,235)]">Free<span class="mt-1 block text-xs font-normal text-gray-500">Free</span></th>
            <th class="bg-gray-50 px-4 py-5 text-center text-sm font-semibold text-gray-900 shadow-[inset_0_-1px_0_rgb(229,231,235)]">Basic<span class="mt-1 block text-xs font-normal text-gray-500">$599 / month</span></th>
            <th class="bg-gray-50 px-4 py-5 text-center text-sm font-semibold text-gray-900 shadow-[inset_0_-1px_0_rgb(229,231,235)]">Team<span class="mt-1 block text-xs font-normal text-gray-500">$999 / month</span></th>
            <th class="bg-gray-50 px-4 py-5 text-center text-sm font-semibold text-gray-900 shadow-[inset_0_-1px_0_rgb(229,231,235)]">Enterprise<span class="mt-1 block text-xs font-normal text-gray-500">Custom</span></th>
          </tr>
        </thead>
        <tbody class="text-sm">
          {% for g in compare %}
          <tr class="bg-gray-50/60" data-group-header="{{ g.key }}">
            <td colspan="4" class="{% if not loop.first %}border-t border-gray-200 {% endif %}px-6 py-3 text-xs font-semibold uppercase tracking-wider text-gray-500">
              <button type="button" data-group-toggle="{{ g.key }}" aria-expanded="{{ 'true' if g.open else 'false' }}" class="flex w-full items-center gap-2 text-left text-xs font-semibold uppercase tracking-wider text-gray-500 hover:text-gray-900">
                <svg class="size-3.5 shrink-0 transition-transform{{ '' if g.open else ' -rotate-90' }}" data-chev viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6l4 4 4-4"></path></svg>
                <span>{{ g.label }}</span>
              </button>
            </td>
            {% if loop.first %}
            <td data-span-cell rowspan="{{ ns.total + 1 }}" class="border-l border-gray-200 bg-white px-4 text-center align-middle text-sm font-medium text-gray-900"><a href="/contact" class="text-shovels-primary hover:text-shovels-primary/80">Contact sales</a></td>
            {% endif %}
          </tr>
          {% for r in g.rows %}
          <tr class="border-t border-gray-100{{ '' if g.open else ' hidden' }}" data-group-row="{{ g.key }}">
            <td class="px-6 py-4 text-gray-700">
              {% if r.tip %}<span class="inline-flex items-center gap-1.5">{{ r.label }}<a href="{{ r.href | default('#credits') }}" class="group relative inline-flex size-4 shrink-0 items-center justify-center rounded-full border border-gray-300 text-[10px] font-semibold leading-none text-gray-500 hover:border-shovels-primary hover:text-shovels-primary"><span aria-hidden="true">i</span><span class="sr-only">More about {{ r.label }}</span><span role="tooltip" class="pointer-events-none absolute bottom-full left-0 z-20 mb-2 hidden w-56 rounded-lg bg-gray-900 px-3 py-2 text-xs font-normal leading-snug text-white shadow-lg group-hover:block group-focus-visible:block">{{ r.tip }}</span></a></span>
              {% else %}{{ r.label }}{% endif %}
            </td>
            {{ cmp_cell(r.vals[0]) }}{{ cmp_cell(r.vals[1]) }}{{ cmp_cell(r.vals[2]) }}
          </tr>
          {% endfor %}
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</section>

{# ── §3 CREDITS (dark) ───────────────────────────────────────────────── #}
<section id="credits" class="w-full scroll-mt-24 bg-shovels-dark px-6 py-24 md:px-10">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-secondary/30 bg-shovels-secondary/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-secondary">How credits work</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-white md:text-4xl">You pay for records, not requests</h2>
      <p class="mt-6 text-base/7 text-gray-300">1 credit = 1 record, requested via API or an export in Shovels Online. Everything else is free. Credits reset monthly.</p>
    </div>
    <p class="mt-10 text-center"><a href="https://docs.shovels.ai/docs/knowledge-base/api/basics/request-counts#how-do-api-credits-work" class="text-sm font-semibold text-shovels-secondary hover:text-shovels-secondary/80">Learn more <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>

{# ── §4 ACCESS ───────────────────────────────────────────────────────── #}
{% set access = [
    {'img': 'shovels-globe', 'name': 'Shovels Online', 'body': 'Search, filter, and export permit and contractor data in the web app. No code needed.'},
    {'img': 'data-api', 'name': 'Shovels API', 'body': 'A REST API for product integrations, automated workflows, and large pulls.'},
    {'img': 'cli', 'name': 'Shovels CLI', 'body': 'One binary, JSON output, no dependencies. Built for terminals and AI agents.'},
    {'img': 'charlie-avatar', 'name': 'Charlie AI', 'body': 'Ask permit questions in plain English and get answers, no filters required.'},
] %}
<section class="w-full bg-white px-6 py-24 md:px-10">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <img src="/images/illustrations/map-hat.svg" alt="" class="mx-auto h-12 w-auto" />
      <h2 class="mt-6 text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Access your data however you work</h2>
      <p class="mt-4 text-lg text-gray-500">Every interface is included with every plan. The web app, API, CLI, and AI assistant all share one credit balance.</p>
    </div>
    <div class="mx-auto mt-16 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {% for a in access %}
      <div class="flex flex-col rounded-2xl border border-gray-200 p-8">
        <span class="flex h-[54px] items-center">
          {% if a.img == 'cli' %}
          <svg class="size-10 text-shovels-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>
          {% else %}
          <img src="/images/illustrations/{{ a.img }}.svg" alt="" class="w-10" />
          {% endif %}
        </span>
        <h3 class="mt-5 text-base font-medium text-gray-900">{{ a.name }}</h3>
        <p class="mt-2 flex-auto text-sm/6 text-gray-600">{{ a.body }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

{# ── §5 SOC 2 ─────────────────────────────────────────────────────────── #}
{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Every plan runs on the same audited infrastructure — the security and compliance controls enterprise buyers ask for, on the free tier too.') }}

{# ── §6 FAQ ───────────────────────────────────────────────────────────── #}
{{ ui_faq.faq_section(
    wrapper_class='!py-24',
    heading='Pricing questions',
    items=[
        {'q': 'What exactly is a credit?',
         'a': 'A credit is one cleaned, normalized record. Credits are spent just two ways — API requests and exports from Shovels Online — each metered by the number of records. Everything else in Shovels Online is free, and credits reset monthly based on your subscription or upgrade date.'},
        {'q': 'Do I need separate plans for the web app and the API?',
         'a': 'No. Every plan includes Shovels Online, the API, the CLI, and Charlie AI. They all share the same monthly credit balance, so you can switch between interfaces without changing plans.'},
        {'q': 'Is the free plan really free?',
         'a': 'Yes. No credit card is required. You get 500 credits per month, one year of record history, and up to 100 results per query across all six datasets. Downloads and full historical records are included with Basic.'},
        {'q': 'How do I upgrade?',
         'a': 'Free and Basic plans can be upgraded anytime at app.shovels.ai. For Team and Custom plans, get in touch with us and we will help you choose the right plan. Self-serve upgrades for higher tiers are coming soon.'},
        {'q': 'How is the Enterprise Data License different from the API?',
         'a': 'The API lets you retrieve records on demand. The Enterprise Data License gives your team the full dataset, delivered as parquet files or table shares in Snowflake, Databricks, or BigQuery, including fields not available through the API. Use the API to build applications and choose EDL when you want the data in your own warehouse.'},
        {'q': 'Is there an annual contract?',
         'a': 'Basic and Team plans are billed monthly. Custom plans and Enterprise Data Licenses are tailored to your needs and priced by agreement. Get in touch to learn more.'},
    ]) }}

{# ── §7 FINAL CTA (two buttons — bespoke; final_cta macro is single-CTA) ─ #}
<section class="w-full bg-white px-6 pb-24 md:px-10">
  <div class="mx-auto max-w-6xl">
    <div class="rounded-2xl border border-shovels-primary/20 bg-gradient-to-b from-[#F6FBF7] from-[25%] to-white to-[45%] p-10 text-center md:p-16">
      <h2 class="text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Not sure which plan fits?</h2>
      <p class="mx-auto mt-6 max-w-2xl text-base text-gray-500 md:text-lg">Tell us what you&rsquo;re building and how much data you need. We&rsquo;ll size a plan that fits your needs.</p>
      <div class="mt-8 flex flex-wrap items-center justify-center gap-4">
        <a href="https://app.shovels.ai/signup/" class="inline-block rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90">Search for free</a>
        <a href="/contact" class="inline-flex items-center gap-2 rounded-full border border-gray-300 px-6 py-3 text-sm font-semibold text-gray-900 transition-colors hover:border-gray-400 hover:bg-gray-50">Talk to us</a>
      </div>
    </div>
  </div>
</section>

{# Comparison-table group toggles + Enterprise rowspan resync. Vanilla,
   self-contained; runs after the table renders. #}
<script>
(function(){
  var table = document.getElementById('compare-table'); if (!table) return;
  var spanCell = table.querySelector('[data-span-cell]');
  function resync(){ if (spanCell) spanCell.rowSpan = table.querySelectorAll('tbody tr:not(.hidden)').length; }
  table.querySelectorAll('[data-group-toggle]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var key = btn.getAttribute('data-group-toggle');
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      btn.querySelector('[data-chev]').classList.toggle('-rotate-90', open);
      table.querySelectorAll('[data-group-row="' + key + '"]').forEach(function(r){ r.classList.toggle('hidden', open); });
      resync();
    });
  });
  var expandBtn = document.getElementById('expand-all');
  if (expandBtn) expandBtn.addEventListener('click', function(){
    var collapse = expandBtn.textContent === 'Collapse all';
    table.querySelectorAll('[data-group-toggle]').forEach(function(btn){
      btn.setAttribute('aria-expanded', String(!collapse));
      btn.querySelector('[data-chev]').classList.toggle('-rotate-90', collapse);
      table.querySelectorAll('[data-group-row="' + btn.getAttribute('data-group-toggle') + '"]').forEach(function(r){ r.classList.toggle('hidden', collapse); });
    });
    expandBtn.textContent = collapse ? 'Expand all' : 'Collapse all';
    resync();
  });
  resync();
})();
</script>
