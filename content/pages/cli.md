Title: Shovels CLI — Construction data from your terminal
Description: Agent-first CLI for the Shovels building permit and contractor API. One binary. JSON output. Zero interactivity. Built for AI agents, scripts, and developers who live in the terminal.
slug: cli

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- HERO                                                                   -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<svg class="absolute inset-0 -z-10 size-full stroke-gray-200 [mask-image:radial-gradient(100%_100%_at_top_right,white,transparent)]" aria-hidden="true">
  <defs>
    <pattern id="cli-grid" width="200" height="200" x="50%" y="-1" patternUnits="userSpaceOnUse">
      <path d="M100 200V.5M.5 .5H200" fill="none" />
    </pattern>
  </defs>
  <rect width="100%" height="100%" stroke-width="0" fill="url(#cli-grid)" />
</svg>

<div class="relative isolate overflow-hidden">
  <div class="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none lg:grid lg:grid-cols-2 lg:gap-x-16 lg:gap-y-6">
      <div>
        <h1 class="max-w-xl text-balance text-5xl font-semibold tracking-tight text-gray-900 sm:text-7xl">Construction data from your terminal</h1>
        <p class="mt-6 max-w-xl text-pretty text-lg font-medium text-gray-500 sm:text-xl/8">Your AI agent's gateway to U.S. construction data.</p>
        <div class="mt-10 flex items-center gap-x-6">
          <a href="https://app.shovels.ai/" class="rounded-md bg-shovels-primary px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-shovels-primary/80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get your API key</a>
          <a href="https://github.com/ShovelsAI/shovels-cli" class="text-sm/6 font-semibold text-gray-900">View on GitHub <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <!-- Terminal mockup -->
      <div class="mt-10 lg:mt-0">
        <div class="rounded-xl bg-gray-900 shadow-2xl ring-1 ring-white/10 overflow-hidden">
          <div class="flex items-center gap-2 px-4 py-3 border-b border-white/10">
            <span class="size-3 rounded-full bg-red-500"></span>
            <span class="size-3 rounded-full bg-yellow-500"></span>
            <span class="size-3 rounded-full bg-green-500"></span>
            <span class="ml-2 text-sm text-gray-400 font-mono">terminal</span>
          </div>
          <div class="p-5 font-mono text-sm leading-relaxed">
            <p class="text-gray-400">$ <span class="text-white">curl -LsSf https://shovels.ai/install.sh | sh</span></p>
            <p class="text-green-400 mt-1">Installed shovels to ~/.shovels/bin/shovels</p>
            <p class="text-gray-500 mt-4"># How many solar permits in 92024 (Encinitas, CA) last year?</p>
            <p class="text-gray-400 mt-1">$ <span class="text-white">shovels permits search --geo-id 92024 \</span></p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-from 2024-01-01 --permit-to 2024-12-31 \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--tags solar --include-count --limit 1 \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;| jq '.meta.total_count.value'</p>
            <p class="text-shovels-secondary mt-1">581</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="absolute inset-x-0 bottom-0 -z-10 h-24 bg-gradient-to-t from-white sm:h-32"></div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- WHAT CAN YOU DO — Command showcase                                     -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Permits, contractors, addresses</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-white sm:text-balance sm:text-5xl">Everything in one binary</h2>
      <p class="mt-6 text-lg/8 text-gray-300">No SDKs, no dependencies, no configuration files. Download a single binary and start querying construction data in seconds.</p>
    </div>
  </div>

  <!-- Command examples grid -->
  <div class="mx-auto mt-16 max-w-7xl px-6 lg:px-8">
    <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">

      <!-- Example 1: Search permits -->
      <div class="rounded-xl bg-gray-800/50 ring-1 ring-white/10 overflow-hidden">
        <div class="px-5 py-3 border-b border-white/10">
          <p class="text-sm font-semibold text-shovels-secondary">Roofing permits in Miami Beach</p>
        </div>
        <div class="p-5 font-mono text-sm leading-relaxed">
          <p class="text-gray-400">$ <span class="text-white">shovels permits search \</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--geo-id 33139 \ <span class="text-gray-500"># Miami Beach, FL</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-from 2024-01-01 \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-to 2024-12-31 \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--tags roofing --include-count \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--limit 1 | jq '.meta.total_count.value'</p>
          <p class="text-shovels-secondary mt-1">490</p>
        </div>
      </div>

      <!-- Example 2: Get contractor details -->
      <div class="rounded-xl bg-gray-800/50 ring-1 ring-white/10 overflow-hidden">
        <div class="px-5 py-3 border-b border-white/10">
          <p class="text-sm font-semibold text-shovels-secondary">How many permits has this contractor filed?</p>
        </div>
        <div class="p-5 font-mono text-sm leading-relaxed">
          <p class="text-gray-400">$ <span class="text-white">shovels contractors permits 03xTGkafsf</span> <span class="text-gray-500"># Cosmic Solar Inc.</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--limit all \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;| jq '.data | length'</p>
          <p class="text-shovels-secondary mt-1">2056</p>
        </div>
      </div>

      <!-- Example 3: Pipeline -->
      <div class="rounded-xl bg-gray-800/50 ring-1 ring-white/10 overflow-hidden">
        <div class="px-5 py-3 border-b border-white/10">
          <p class="text-sm font-semibold text-shovels-secondary">Export electrical contractors to CSV</p>
        </div>
        <div class="p-5 font-mono text-sm leading-relaxed">
          <p class="text-gray-400">$ <span class="text-white">shovels contractors search \</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--geo-id 78701 \ <span class="text-gray-500"># Austin, TX</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-from 2024-01-01 \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-to 2024-12-31 \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--tags electrical --limit 100 \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;| jq -r '.data[] | [.name, .permit_count] | @csv'</p>
          <p class="text-gray-300 mt-1">"KENNETH TUMLINSON",554</p>
          <p class="text-gray-300">"JOSEPH H MARTINEZ",85</p>
          <p class="text-gray-300">"CDX ELECTRICAL SERVICES",19</p>
          <p class="text-gray-500">...</p>
        </div>
      </div>

      <!-- Example 4: Address lookup -->
      <div class="rounded-xl bg-gray-800/50 ring-1 ring-white/10 overflow-hidden">
        <div class="px-5 py-3 border-b border-white/10">
          <p class="text-sm font-semibold text-shovels-secondary">Resolve an address to a geo_id</p>
        </div>
        <div class="p-5 font-mono text-sm leading-relaxed">
          <p class="text-gray-400">$ <span class="text-white">shovels addresses search \</span></p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;-q "1600 Pennsylvania Ave" \</p>
          <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;| jq '.data[0] | {name, geo_id}'</p>
          <p class="text-gray-300 mt-1">{</p>
          <p class="text-gray-300">&nbsp;&nbsp;"name": "<span class="text-green-400">1600 Pennsylvania Ave Nw, Washington, DC</span>",</p>
          <p class="text-gray-300">&nbsp;&nbsp;"geo_id": "<span class="text-shovels-secondary">Kw5MGExoU6Y</span>"</p>
          <p class="text-gray-300">}</p>
        </div>
      </div>

    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- BUILT FOR AI AGENTS                                                    -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none lg:grid lg:grid-cols-2 lg:gap-x-16 lg:items-start">
      <div>
        <p class="text-base/7 font-semibold text-shovels-secondary">Agent-first design</p>
        <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Your AI agent's interface to construction data</h2>
        <p class="mt-6 text-lg/8 text-gray-600">No MCP headaches — no context bloat, no credential juggling, no host lock-in. Claude Code, OpenAI Codex, Cursor, or your own agents shell out to <code class="text-sm bg-gray-100 px-1.5 py-0.5 rounded">shovels</code> and get structured data back instantly.</p>
        <dl class="mt-10 max-w-xl space-y-6 text-base/7 text-gray-600">
          <div class="relative pl-9">
            <dt class="font-semibold text-gray-900">
              <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" /></svg>
              JSON to stdout. Always.
            </dt>
            <dd class="mt-1">No tables, no colors, no spinners. stdout is always valid JSON. Errors go to stderr. Your parser never breaks.</dd>
          </div>
          <div class="relative pl-9">
            <dt class="font-semibold text-gray-900">
              <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" /></svg>
              Help text written for LLMs
            </dt>
            <dd class="mt-1">Every <code class="text-sm bg-gray-100 px-1.5 py-0.5 rounded">--help</code> is specific, example-rich, and jargon-free. An AI agent can read the help and construct the right command on the first try.</dd>
          </div>
          <div class="relative pl-9">
            <dt class="font-semibold text-gray-900">
              <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" /></svg>
              Meaningful exit codes
            </dt>
            <dd class="mt-1">Exit 0 = success. Exit 2 = auth error. Exit 3 = rate limited. Your agent can branch on the exit code without parsing anything.</dd>
          </div>
          <div class="relative pl-9">
            <dt class="font-semibold text-gray-900">
              <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" /></svg>
              Zero interactivity
            </dt>
            <dd class="mt-1">No prompts, no confirmations, no progress bars. It succeeds and prints JSON, or it fails and prints a JSON error. Nothing in between.</dd>
          </div>
        </dl>
      </div>
      <!-- AI agent terminal mockup -->
      <div class="mt-10 lg:mt-0">
        <div class="rounded-xl bg-gray-900 shadow-2xl ring-1 ring-white/10 overflow-hidden">
          <div class="flex items-center gap-2 px-4 py-3 border-b border-white/10">
            <span class="size-3 rounded-full bg-red-500"></span>
            <span class="size-3 rounded-full bg-yellow-500"></span>
            <span class="size-3 rounded-full bg-green-500"></span>
            <span class="ml-2 text-sm text-gray-400 font-mono">claude code</span>
          </div>
          <div class="p-5 font-mono text-sm leading-relaxed">
            <p class="text-gray-500 italic"># Your AI agent runs this:</p>
            <p class="text-gray-400 mt-2">$ <span class="text-white">shovels permits search --help</span></p>
            <p class="text-gray-400 mt-1">...</p>
            <p class="text-gray-500 mt-3 italic"># Reads the help, builds the query:</p>
            <p class="text-gray-400 mt-2">$ <span class="text-white">shovels permits search \</span></p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--geo-id 94110 \ <span class="text-gray-500"># San Francisco, CA</span></p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-from 2024-06-01 \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--permit-to 2024-12-31 \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--tags roofing \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--property-type residential \</p>
            <p class="text-white">&nbsp;&nbsp;&nbsp;&nbsp;--limit 20</p>
            <p class="text-gray-500 mt-3 italic"># Parses the JSON, reasons about the results,</p>
            <p class="text-gray-500 italic"># then asks for contractor details...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- COMPOSABILITY — Pipe it, chain it, script it                           -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-gray-50 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Unix philosophy</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-balance sm:text-5xl">Pipe it. Chain it. Script it.</h2>
      <p class="mt-6 text-lg/8 text-gray-600">JSON output means you can compose the CLI with any tool in your stack. Build workflows that would take weeks with a GUI.</p>
    </div>

    <div class="mx-auto mt-16 max-w-4xl">
      <div class="space-y-6">

        <!-- Composability example 1 -->
        <div class="rounded-xl bg-white shadow-sm ring-1 ring-gray-200 overflow-hidden">
          <div class="px-5 py-3 border-b border-gray-100">
            <p class="text-sm font-semibold text-gray-900">Build a solar contractor CSV in one line</p>
          </div>
          <div class="p-5 font-mono text-sm leading-relaxed bg-gray-900 text-white">
            <p>shovels contractors search --geo-id CA \</p>
            <p>&nbsp;&nbsp;--permit-from 2024-01-01 --permit-to 2024-12-31 \</p>
            <p>&nbsp;&nbsp;--tags solar --limit all \</p>
            <p>&nbsp;&nbsp;| jq -r '.data[] | [.name, .phone, .permit_count] | @csv' \</p>
            <p>&nbsp;&nbsp;> solar_contractors_ca.csv</p>
          </div>
        </div>

        <!-- Composability example 2 -->
        <div class="rounded-xl bg-white shadow-sm ring-1 ring-gray-200 overflow-hidden">
          <div class="px-5 py-3 border-b border-gray-100">
            <p class="text-sm font-semibold text-gray-900">Monitor new permits in your market (cron job)</p>
          </div>
          <div class="p-5 font-mono text-sm leading-relaxed bg-gray-900 text-white">
            <p><span class="text-gray-500"># crontab: 0 8 * * MON</span></p>
            <p>shovels permits search --geo-id 94110 \ <span class="text-gray-500"># San Francisco, CA</span></p>
            <p>&nbsp;&nbsp;--permit-from $(date -v-7d +%Y-%m-%d) \</p>
            <p>&nbsp;&nbsp;--permit-to $(date +%Y-%m-%d) \</p>
            <p>&nbsp;&nbsp;| jq '.meta.count' \</p>
            <p>&nbsp;&nbsp;| xargs -I{} echo "{} new permits this week in 94110"</p>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- WHY NOT JUST CURL — The comparison                                     -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Why not just curl?</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-balance sm:text-5xl">Because pagination shouldn't be your problem</h2>
    </div>

    <div class="mx-auto mt-16 max-w-5xl grid grid-cols-1 gap-8 lg:grid-cols-2">

      <!-- curl way -->
      <div class="rounded-xl overflow-hidden ring-1 ring-red-200">
        <div class="px-5 py-3 bg-red-50 border-b border-red-200">
          <p class="text-sm font-semibold text-red-800">With curl: 15+ lines, manual pagination</p>
        </div>
        <div class="p-5 font-mono text-xs leading-relaxed bg-gray-900 text-gray-300">
          <p>cursor=""</p>
          <p>while true; do</p>
          <p>&nbsp;&nbsp;resp=$(curl -s -H "X-API-Key: $KEY" \</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;"https://api.shovels.ai/v2/permits/search\</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;?geo_id=92024&permit_from=2024-01-01\</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;&permit_to=2024-12-31&cursor=$cursor")</p>
          <p>&nbsp;&nbsp;echo "$resp" | jq '.items[]'</p>
          <p>&nbsp;&nbsp;cursor=$(echo "$resp" | jq -r '.next_cursor')</p>
          <p>&nbsp;&nbsp;[ "$cursor" = "null" ] && break</p>
          <p>done</p>
        </div>
      </div>

      <!-- CLI way -->
      <div class="rounded-xl overflow-hidden ring-1 ring-green-200">
        <div class="px-5 py-3 bg-green-50 border-b border-green-200">
          <p class="text-sm font-semibold text-green-800">With shovels: one command, all records</p>
        </div>
        <div class="p-5 font-mono text-sm leading-relaxed bg-gray-900 text-white">
          <p>shovels permits search \</p>
          <p>&nbsp;&nbsp;--geo-id 92024 \</p>
          <p>&nbsp;&nbsp;--permit-from 2024-01-01 \</p>
          <p>&nbsp;&nbsp;--permit-to 2024-12-31 \</p>
          <p>&nbsp;&nbsp;--limit all</p>
        </div>
      </div>

    </div>
    <p class="mx-auto mt-8 max-w-xl text-center text-base text-gray-500">The CLI handles auth headers, cursor pagination, rate-limit retries, and credit tracking. You just say how many records you want.</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- FEATURE GRID                                                           -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <dl class="mx-auto grid max-w-2xl grid-cols-1 gap-x-6 gap-y-10 text-base/7 text-gray-300 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8 lg:gap-y-16">
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" /></svg>
          Single binary.
        </dt>
        <dd class="inline">No runtime, no dependencies. Download one file, put it on your PATH, done. macOS, Linux, and Windows.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" /></svg>
          Pagination handled.
        </dt>
        <dd class="inline"><code class="text-xs bg-white/10 px-1 rounded">--limit all</code> fetches every record. The CLI manages cursors, page sizes, and the 100K ceiling internally.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182" /></svg>
          Auto-retry.
        </dt>
        <dd class="inline">Rate-limited? The CLI backs off with jitter and retries automatically. Respects Retry-After headers.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          Credit tracking.
        </dt>
        <dd class="inline">Every response includes <code class="text-xs bg-white/10 px-1 rounded">credits_used</code> and <code class="text-xs bg-white/10 px-1 rounded">credits_remaining</code>. Your agent always knows the cost.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" /></svg>
          Checksum-verified installs.
        </dt>
        <dd class="inline">The install script downloads from GitHub Releases and verifies SHA256 checksums before touching your system.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M17.25 6.75L22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3l-4.5 16.5" /></svg>
          Open source.
        </dt>
        <dd class="inline">MIT licensed. Read the code, fork it, contribute. Built with Go and Cobra.</dd>
      </div>
    </dl>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- INSTALL CTA                                                            -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div class="bg-gray-100">
  <div class="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <h2 class="text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Get started in 10 seconds</h2>
      <div class="mt-8 rounded-xl bg-gray-900 p-5 shadow-2xl ring-1 ring-white/10">
        <p class="font-mono text-sm text-white text-center">curl -LsSf https://shovels.ai/install.sh | sh</p>
      </div>
      <p class="mt-6 text-base text-gray-600">Then set your API key and start querying:</p>
      <div class="mt-4 rounded-xl bg-gray-900 p-5 shadow-2xl ring-1 ring-white/10">
        <div class="font-mono text-sm text-left">
          <p class="text-gray-400">$ <span class="text-white">export SHOVELS_API_KEY=your-key</span></p>
          <p class="text-gray-400 mt-1">$ <span class="text-white">shovels permits search --geo-id 92024 --permit-from 2024-01-01 --permit-to 2024-12-31</span></p>
        </div>
      </div>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a href="https://app.shovels.ai/" class="rounded-md bg-shovels-primary px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-shovels-primary/80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get your API key</a>
        <a href="https://github.com/ShovelsAI/shovels-cli" class="text-sm/6 font-semibold text-gray-900">GitHub <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </div>
</div>

<!-- JSON-LD structured data for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Shovels CLI",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "macOS, Linux, Windows",
  "description": "Agent-first command-line interface for the Shovels building permit and contractor API. JSON-only output, automatic pagination, and structured error codes designed for AI agents and scripts.",
  "url": "https://www.shovels.ai/cli",
  "downloadUrl": "https://github.com/ShovelsAI/shovels-cli/releases/latest",
  "softwareVersion": "0.1.0",
  "license": "https://opensource.org/licenses/MIT",
  "offers": {
    "@type": "Offer",
    "url": "https://app.shovels.ai/"
  },
  "author": {
    "@type": "Organization",
    "name": "Shovels",
    "url": "https://www.shovels.ai"
  }
}
</script>
