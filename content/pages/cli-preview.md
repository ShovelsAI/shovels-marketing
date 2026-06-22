Title: Shovels CLI: Construction Data Straight From Your Terminal
Description: Agent-first CLI for the Shovels building permit and contractor API. One binary, JSON output, zero interactivity—built for AI agents, scripts, and pipelines.
slug: features/cli-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/code_window.html' as ui_code %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/soc2_trust.html' as ui_soc2 %}
{% import 'macros/callout.html' as ui_callout %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{# ── Hero terminal (reused from the live /cli page; validated commands) #}
{% set hero_terminal %}{% call ui_code.code_window(title='terminal', copyable=True, copy_text="curl -LsSf https://shovels.ai/install.sh | sh") %}
<span class="text-gray-500">$</span> <span class="text-white">curl -LsSf https://shovels.ai/install.sh | sh</span>
<span class="text-green-400">Installed shovels to ~/.shovels/bin/shovels</span>

<span class="text-gray-500"># How many solar permits in 92024 (Encinitas, CA) last year?</span>
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search --geo-id 92024 \</span>
<span class="text-white">    --permit-from 2024-01-01 --permit-to 2024-12-31 \</span>
<span class="text-white">    --tags solar --include-count --limit 1 \</span>
<span class="text-white">    | jq '.meta.total_count.value'</span>
<span class="text-shovels-secondary">581</span>
{% endcall %}{% endset %}

{{ ui_hero.hero(
    eyebrow='Shovels CLI',
    h1='Construction data straight from your terminal',
    description='An agent-first CLI for the Shovels API. One binary, JSON output, zero interactivity. Built for AI agents, scripts, and pipelines.',
    cta_label='Get your API key',
    cta_href='https://app.shovels.ai/',
    secondary_cta_label='View on GitHub →',
    secondary_cta_href='https://github.com/ShovelsAI/shovels-cli',
    media=hero_terminal,
    bg_src='/images/features/cli/gear.svg') }}

{{ ui_soc2.soc2_trust(
    heading='Shovels is SOC 2® Type II certified',
    body='Shovels meets enterprise security and compliance requirements. Our SOC 2 Type II certification reflects controls independently audited over a sustained period, not just a point-in-time snapshot.',
    cta_label='Read more about our security practices →',
    cta_href='https://trust.shovels.ai/') }}

{# ── Feature terminals (reused validated commands, re-rendered via code_window) #}
{% set f1_media %}{% call ui_code.code_window(title='permits search') %}
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search \</span>
<span class="text-white">    --geo-id 33139 \</span>          <span class="text-gray-500"># Miami Beach, FL</span>
<span class="text-white">    --permit-from 2024-01-01 \</span>
<span class="text-white">    --permit-to 2024-12-31 \</span>
<span class="text-white">    --tags roofing --include-count \</span>
<span class="text-white">    --limit 1 | jq '.meta.total_count.value'</span>
<span class="text-shovels-secondary">490</span>
{% endcall %}{% endset %}

{% set f2_media %}{% call ui_code.code_window(title='claude code') %}
<span class="text-gray-500"># Your AI agent runs this:</span>
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search --help</span>
<span class="text-gray-400">...</span>
<span class="text-gray-500"># Reads the help, builds the query:</span>
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search \</span>
<span class="text-white">    --geo-id 94110 \</span>          <span class="text-gray-500"># San Francisco, CA</span>
<span class="text-white">    --permit-from 2024-06-01 \</span>
<span class="text-white">    --tags roofing \</span>
<span class="text-white">    --property-type residential \</span>
<span class="text-white">    --limit 20</span>
<span class="text-gray-500"># Parses the JSON, reasons about the results...</span>
{% endcall %}{% endset %}

{% set f3_media %}{% call ui_code.code_window(title='build CSV') %}
<span class="text-gray-500">$</span> <span class="text-white">shovels contractors search --geo-id CA \</span>
<span class="text-white">    --permit-from 2024-01-01 --permit-to 2024-12-31 \</span>
<span class="text-white">    --tags solar --limit all \</span>
<span class="text-white">    | jq -r '.data[] | [.name, .phone, .permit_count] | @csv' \</span>
<span class="text-white">    > solar_contractors_ca.csv</span>
{% endcall %}{% endset %}

{# F4 visual — reliability cards (not a terminal). #}
{% set f4_media %}
<div class="space-y-3">
  {% for title, body in [
      ('Pagination handled', '--limit all manages cursors, page sizes, and the 100K-record ceiling'),
      ('Auto-retry on rate limits', 'Backoff + jitter; respects Retry-After'),
      ('Credit tracking', 'Every response reports credits_used and credits_remaining'),
  ] %}
  <div class="rounded-xl border border-gray-200 bg-white p-5 shadow-sm">
    <p class="text-sm font-semibold text-gray-900">{{ title }}</p>
    <p class="mt-1 font-mono text-xs text-gray-500">{{ body }}</p>
  </div>
  {% endfor %}
</div>
{% endset %}

{% set features = [
    {
        'number': '01',
        'title': 'Query everything with one open-source binary',
        'description': 'No SDKs, no dependencies, no config files. Download one file and query permits, contractors, and addresses in seconds.',
        'bullets': [
            'macOS, Linux, and Windows',
            'Open source (MIT, Go) with checksum-verified installs',
            '<code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">--limit all</code> handles cursors, page sizes, and rate-limit retries',
        ],
        'media': f1_media,
    },
    {
        'number': '02',
        'title': 'Plug directly into your AI agents',
        'description': 'Claude Code, Codex, Cursor, or your own agents shell out to <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">shovels</code> and get structured data back. No MCP headaches, no context bloat, no credential juggling.',
        'bullets': [
            'JSON to <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">stdout</code>, always; errors to <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">stderr</code>',
            '<code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">--help</code> text written for LLMs: specific, example-rich, jargon-free',
            'Meaningful exit codes: 0 = success, 2 = auth error, 3 = rate limited',
        ],
        'media': f2_media,
    },
    {
        'number': '03',
        'title': 'Pipe it, chain it, script it',
        'description': 'JSON output composes with jq, cron, and everything else in your stack. Build workflows that would take weeks in a GUI.',
        'bullets': [
            'Build a solar contractor CSV in one line',
            'Monitor new permits in your market on a cron job',
            'Resolve addresses to <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">geo_id</code>s mid-pipeline',
        ],
        'media': f3_media,
    },
    {
        'number': '04',
        'title': 'Move faster with reliability built in',
        'description': 'The CLI handles the operational plumbing, so jobs run unattended and your agent always knows the cost.',
        'bullets': [
            '<code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">--limit all</code> manages cursors, page sizes, and the 100K-record ceiling',
            'Auto-retry on rate limits with backoff + jitter; respects <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">Retry-After</code>',
            'Every response reports <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">credits_used</code> and <code class="rounded bg-gray-100 px-1.5 py-0.5 text-sm">credits_remaining</code>',
        ],
        'media': f4_media,
    },
] %}

{{ ui.use_case_section(
    eyebrow='AGENT-FIRST BY DESIGN',
    heading='Permits, contractors, and addresses. No integration required.',
    cases=features) }}

{# ── Gallery — four validated command examples across the dataset. #}
{% set g1 %}{% call ui_code.code_window(title='count permits', fill=True, copyable=True, copy_text="shovels permits search --geo-id 33139 --permit-from 2024-01-01 --permit-to 2024-12-31 --tags roofing --include-count --limit 1 | jq '.meta.total_count.value'") %}
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search --geo-id 33139 \</span>
<span class="text-white">    --permit-from 2024-01-01 --permit-to 2024-12-31 \</span>
<span class="text-white">    --tags roofing --include-count --limit 1 \</span>
<span class="text-white">    | jq '.meta.total_count.value'</span>
<span class="text-shovels-secondary">490</span>
{% endcall %}{% endset %}
{% set g2 %}{% call ui_code.code_window(title='contractor permits', fill=True, copyable=True, copy_text="shovels contractors permits 03xTGkafsf --limit all | jq '.data | length'") %}
<span class="text-gray-500">$</span> <span class="text-white">shovels contractors permits 03xTGkafsf \</span>  <span class="text-gray-500"># Cosmic Solar Inc.</span>
<span class="text-white">    --limit all | jq '.data | length'</span>
<span class="text-shovels-secondary">2056</span>
{% endcall %}{% endset %}
{% set g3 %}{% call ui_code.code_window(title='export CSV', fill=True, copyable=True, copy_text="shovels contractors search --geo-id 78701 --tags electrical --limit 100 | jq -r '.data[] | [.name, .permit_count] | @csv'") %}
<span class="text-gray-500">$</span> <span class="text-white">shovels contractors search --geo-id 78701 \</span>  <span class="text-gray-500"># Austin, TX</span>
<span class="text-white">    --tags electrical --limit 100 \</span>
<span class="text-white">    | jq -r '.data[] | [.name, .permit_count] | @csv'</span>
<span class="text-gray-300">"KENNETH TUMLINSON",554</span>
<span class="text-gray-300">"JOSEPH H MARTINEZ",85</span>
<span class="text-gray-500">...</span>
{% endcall %}{% endset %}
{% set g4 %}{% call ui_code.code_window(title='resolve address', fill=True, copyable=True, copy_text="shovels addresses search -q \"1600 Pennsylvania Ave\" | jq '.data[0] | {name, geo_id}'") %}
<span class="text-gray-500">$</span> <span class="text-white">shovels addresses search \</span>
<span class="text-white">    -q "1600 Pennsylvania Ave" \</span>
<span class="text-white">    | jq '.data[0] | {name, geo_id}'</span>
<span class="text-gray-300">{</span>
<span class="text-gray-300">  "name": "<span class="text-green-400">1600 Pennsylvania Ave Nw, Washington, DC</span>",</span>
<span class="text-gray-300">  "geo_id": "<span class="text-shovels-secondary">Kw5MGExoU6Y</span>"</span>
<span class="text-gray-300">}</span>
{% endcall %}{% endset %}

<section class="w-full bg-white px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <h2 class="text-center text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">See it across the whole dataset</h2>
    <div class="mt-12 grid grid-cols-1 gap-6 lg:grid-cols-2">
      <div>{{ g1 }}</div>
      <div>{{ g2 }}</div>
      <div>{{ g3 }}</div>
      <div>{{ g4 }}</div>
    </div>
  </div>
</section>

{# ── Why not just curl — comparison (reused from live /cli). #}
<section class="w-full bg-gray-50 px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">WHY NOT JUST CURL?</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Because pagination shouldn't be your problem</h2>
    </div>
    <div class="mx-auto mt-12 grid max-w-5xl grid-cols-1 gap-8 lg:grid-cols-2">
      <div class="flex h-full flex-col overflow-hidden rounded-xl ring-1 ring-red-200">
        <div class="border-b border-red-200 bg-red-50 px-5 py-3">
          <p class="text-sm font-semibold text-red-800">✕ With curl — 15+ lines, manual pagination</p>
        </div>
        <pre class="flex-auto overflow-x-auto bg-gray-900 p-5 font-mono text-xs leading-relaxed text-gray-300"><code>cursor=""
while true; do
  resp=$(curl -s -H "X-API-Key: $KEY" \
    "https://api.shovels.ai/v2/permits/search\
?geo_id=92024&permit_from=2024-01-01\
&permit_to=2024-12-31&cursor=$cursor")
  echo "$resp" | jq '.items[]'
  cursor=$(echo "$resp" | jq -r '.next_cursor')
  [ "$cursor" = "null" ] && break
done</code></pre>
      </div>
      <div class="flex h-full flex-col overflow-hidden rounded-xl ring-1 ring-green-200">
        <div class="border-b border-green-200 bg-green-50 px-5 py-3">
          <p class="text-sm font-semibold text-green-800">✓ With shovels — one command, all records</p>
        </div>
        <pre class="flex-auto overflow-x-auto bg-gray-900 p-5 font-mono text-sm leading-relaxed text-white"><code>shovels permits search \
  --geo-id 92024 \
  --permit-from 2024-01-01 \
  --permit-to 2024-12-31 \
  --limit all</code></pre>
      </div>
    </div>
    <p class="mx-auto mt-8 max-w-xl text-center text-base text-gray-500">The CLI handles auth headers, cursor pagination, rate-limit retries, and credit tracking. Just say how many records you want.</p>
  </div>
</section>

{# Links to /api (Shovels API) — moves to /solutions/api at launch. #}
{{ ui_callout.callout(
    variant='green',
    heading='Building an application?',
    body='The CLI is built on the Shovels API. For full REST access and integration into your product, use our API directly.',
    cta_label='Learn more about our API',
    cta_href='/api') }}

{# ── How it works — terminal per step (vertical). #}
{% set hiw1 %}{% call ui_code.code_window(title='install', copyable=True, copy_text="curl -LsSf https://shovels.ai/install.sh | sh") %}
<span class="text-gray-500">$</span> <span class="text-white">curl -LsSf https://shovels.ai/install.sh | sh</span>
<span class="text-green-400">Installed shovels (sha256 verified)</span>
{% endcall %}{% endset %}
{% set hiw2 %}{% call ui_code.code_window(title='auth', copyable=True, copy_text="export SHOVELS_API_KEY=your-key") %}
<span class="text-gray-500">$</span> <span class="text-white">export SHOVELS_API_KEY=your-key</span>
{% endcall %}{% endset %}
{% set hiw3 %}{% call ui_code.code_window(title='query', copyable=True, copy_text="shovels permits search --geo-id 92024 --permit-from 2025-01-01") %}
<span class="text-gray-500">$</span> <span class="text-white">shovels permits search --geo-id 92024 \</span>
<span class="text-white">    --permit-from 2025-01-01</span>
<span class="text-gray-300">{ "meta": { "count": <span class="text-shovels-secondary">138</span> }, ... }</span>
{% endcall %}{% endset %}

<section id="how-it-works" class="w-full bg-white px-6 md:px-10 py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="inline-block rounded-full border border-shovels-primary/20 bg-shovels-primary/5 px-3 py-1 text-xs font-medium uppercase tracking-wider text-shovels-primary">HOW IT WORKS</span>
      <h2 class="mt-4 text-pretty text-3xl font-medium tracking-tight text-gray-900 md:text-4xl">Up and running in seconds</h2>
    </div>
    {# Stepper: numbered circles on a left rail, connected by a vertical line
       (segment runs from below each circle, across the gap, to the next),
       with a card per step holding the text (left) + terminal (right). #}
    <div class="mx-auto mt-12 max-w-5xl space-y-6">
      {% for num, title, tagline, term in [
          ('1', 'Install', 'One line, checksum-verified, no runtime to install.', hiw1),
          ('2', 'Set your API key', 'Grab a key from your Shovels account dashboard.', hiw2),
          ('3', 'Run your first query', 'JSON results, instantly.', hiw3),
      ] %}
      <div class="flex items-stretch gap-5 md:gap-6">
        <div class="relative flex w-10 shrink-0 flex-col items-center pt-1">
          {# Runs from this circle's center down to the next circle's center
             (space-y-6 gap + pt-1 + half-circle = 48px); both circles sit on
             top (z-10), so it reads flush into each number. #}
          {% if not loop.last %}
          <span class="absolute left-1/2 top-6 -bottom-12 w-0.5 -translate-x-1/2 bg-gray-200" aria-hidden="true"></span>
          {% endif %}
          <span class="relative z-10 flex size-10 items-center justify-center rounded-full bg-shovels-primary text-sm font-semibold text-white">{{ num }}</span>
        </div>
        <div class="flex-1 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
          <div class="grid grid-cols-1 items-center gap-6 md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-xl font-medium text-gray-900">{{ title }}</h3>
              <p class="mt-2 text-base text-gray-500">{{ tagline }}</p>
            </div>
            <div>{{ term }}</div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What is the Shovels CLI?',
            'a': "The Shovels CLI is a command-line interface for the Shovels construction data API. It's a single open-source binary that lets you query building permits, contractors, and addresses directly from your terminal, returning clean JSON every time. It was designed from the ground up for AI agents, scripts, and data pipelines.",
        },
        {
            'q': 'What platforms does the CLI support?',
            'a': "The CLI runs on macOS, Linux, and Windows. The install script downloads the binary from GitHub Releases and verifies its SHA256 checksum before anything touches your system, so you always know exactly what you're installing.",
        },
        {
            'q': 'How do AI agents use the CLI?',
            'a': "AI agents like Claude Code, Codex, and Cursor simply shell out to the shovels command. They read the LLM-friendly --help text to construct the right command, parse the JSON that comes back on stdout, and branch on meaningful exit codes. There's no MCP server to configure and no credential juggling involved.",
        },
        {
            'q': 'How does pricing work?',
            'a': 'The CLI authenticates with your Shovels API key and draws from the same credit balance as the API. Every response includes credits_used and credits_remaining fields, so you—or your agent—always know exactly what a query cost and how much you have left.',
        },
        {
            'q': 'Is the CLI open source?',
            'a': "Yes, the CLI is fully open source under the MIT license. It's written in Go using the Cobra framework, and the complete source code is available on GitHub—we welcome issues, feedback, and contributions.",
        },
        {
            'q': 'How is the CLI different from the API?',
            'a': "They share the same data and the same credits, so the difference comes down to ergonomics. The CLI handles auth headers, cursor pagination, rate-limit retries, and credit tracking for you, which makes it ideal for terminal work and AI agents. If you're building Shovels data into an application, the API gives you direct REST access.",
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Get started in 10 seconds',
    description='Install the CLI, set your API key, and run your first query.',
    cta_label='Get your API key',
    cta_href='https://app.shovels.ai/') }}
