Title: Data Delivery Options — Layout Options (Preview)
Description: Internal comparison of three layout directions for the homepage "Data delivery options" section. For designer review.
slug: data-delivery-options-preview
status: hidden

{% import 'macros/icons.html' as icons %}

{# ────────────────────────────────────────────────────────────────────
   Designer comparison page. Three real implementations of the homepage
   "Data delivery options" section, each under an amber scaffolding
   banner. Not part of the homepage flow — shared standalone so the
   designer can pick a direction and we fine-tune. The amber banners and
   this page itself are removed once a direction is chosen.

   Shared content drives all three so copy/links stay in sync:
   (icon, illustration, name, best_for, body, href). `best_for` is new
   draft copy introduced with options 2 and 3. #}
{% set delivery = [
    ('app_window', '/images/home/shovels-online.svg', 'Shovels Online', 'Explore &amp; export', 'Purchase single or multiple seats to explore and download our building permit, contractor, and local government decision data.', '/permit-database'),
    ('code', '/images/home/shovels-api.svg', 'Shovels API', 'Build into your product', 'Automate access and integrate with other applications like CRMs, custom web apps, and more.', '/api'),
    ('database', '/images/home/shovels-enterprise.svg', 'Enterprise Data License', 'Pipe into your warehouse', 'Get parquet files or private table shares into Snowflake, Databricks, or Big Query.', '/data-feed'),
] %}

{% macro option_banner(label, note) %}
<div class="border-y border-amber-200 bg-amber-50 px-6 py-3 text-center">
  <span class="text-sm font-semibold text-amber-900">{{ label }}</span>
  <span class="text-sm text-amber-700"> — {{ note }}</span>
</div>
{% endmacro %}


{# ══ OPTION 1 — Current (dark, illustration-led) ═══════════════════════ #}
{{ option_banner('Option 1 — Current', 'dark, illustration-led') }}
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2 class="text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl">Data delivery options</h2>
      <p class="mt-6 text-lg/8 text-gray-300">Three ways to access our building permit, contractor, and government decision data—self-serve online, via API, or as a licensed enterprise feed.</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
        {% for icon, illo, name, best, body, href in delivery %}
        <div class="flex flex-col">
          <dt class="text-base/7 font-semibold text-white">
            <div class="mb-6 flex size-20 items-center justify-center rounded-lg">
              <img src="{{ illo }}" alt="{{ name }}" class="size-20">
            </div>
            {{ name }}
          </dt>
          <dd class="mt-1 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">{{ body }}</p>
            <p class="mt-6">
              <a href="{{ href }}" class="text-sm/6 font-semibold text-shovels-secondary">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
        {% endfor %}
      </dl>
    </div>
  </div>
</div>


{# ══ OPTION 2 — Bordered cards + "best for" tag (dark) ═════════════════ #}
{{ option_banner('Option 2 — Bordered cards + “best for” tag', 'dark, icon tiles, decision-oriented') }}
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2 class="text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl">Data delivery options</h2>
      <p class="mt-6 text-lg/8 text-gray-300">Three ways to access our building permit, contractor, and government decision data—pick the one that fits how your team works.</p>
    </div>
    <dl class="mx-auto mt-16 grid max-w-xl grid-cols-1 gap-8 sm:mt-20 lg:mt-24 lg:max-w-none lg:grid-cols-3">
      {% for icon, illo, name, best, body, href in delivery %}
      <div class="flex flex-col rounded-2xl border border-white/10 bg-white/5 p-8">
        <dt>
          <span class="flex size-11 items-center justify-center rounded-xl bg-shovels-primary">
            {{ icons[icon](class='size-6 text-white') }}
          </span>
          <span class="mt-5 block text-xs font-medium uppercase tracking-wider text-shovels-secondary">{{ best }}</span>
          <span class="mt-1 block text-lg font-semibold text-white">{{ name }}</span>
        </dt>
        <dd class="mt-3 flex flex-auto flex-col text-base/7 text-gray-300">
          <p class="flex-auto">{{ body }}</p>
          <p class="mt-6">
            <a href="{{ href }}" class="text-sm/6 font-semibold text-shovels-secondary">Learn more <span aria-hidden="true">→</span></a>
          </p>
        </dd>
      </div>
      {% endfor %}
    </dl>
  </div>
</div>


{# ══ OPTION 3 — Numbered tiers (light) ════════════════════════════════ #}
{{ option_banner('Option 3 — Numbered tiers', 'light, framed as an ascending progression') }}
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2 class="text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Data delivery options</h2>
      <p class="mt-6 text-lg/8 text-gray-600">From self-serve to full enterprise delivery—three tiers that scale with how much data you need and how you want it.</p>
    </div>
    <dl class="mx-auto mt-16 grid max-w-xl grid-cols-1 gap-8 sm:mt-20 lg:mt-24 lg:max-w-none lg:grid-cols-3">
      {% for icon, illo, name, best, body, href in delivery %}
      <div class="flex flex-col border-t-2 border-shovels-primary pt-6">
        <dt>
          <span class="block text-3xl font-semibold text-shovels-primary">0{{ loop.index }}</span>
          <span class="mt-3 block text-xs font-medium uppercase tracking-wider text-shovels-primary">{{ best }}</span>
          <span class="mt-1 block text-lg font-semibold text-gray-900">{{ name }}</span>
        </dt>
        <dd class="mt-3 flex flex-auto flex-col text-base/7 text-gray-600">
          <p class="flex-auto">{{ body }}</p>
          <p class="mt-6">
            <a href="{{ href }}" class="text-sm/6 font-semibold text-gray-900 hover:text-shovels-primary">Learn more <span aria-hidden="true">→</span></a>
          </p>
        </dd>
      </div>
      {% endfor %}
    </dl>
  </div>
</div>
