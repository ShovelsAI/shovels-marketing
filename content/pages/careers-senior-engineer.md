Title: Senior AI-Native Engineer: Data, Platform & Agents
Description: We're not looking for the traditional 10x engineer. We're looking for the next generation: an engineer who runs a team of AI agents and ships what used to take a team of humans.
slug: careers/senior-engineer

<!-- back link -->
<section class="py-6">
  <div class="mx-auto max-w-4xl px-6">
    <a href="{filename}careers.md" class="text-emerald-900 hover:underline">← Back to Careers</a>
  </div>
</section>

<!-- position title -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-6">Senior AI-Native Engineer: Data, Platform &amp; Agents 👷‍♂️👷‍♀️👷</h1>
  </div>
</section>

<!-- intro -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <p class="mb-4">
      <strong>We're not looking for the traditional 10x engineer.</strong> We're looking for the
      next generation: an engineer who runs a team of AI agents and ships what used to take a team
      of humans. Every project at Shovels already runs on a mix of humans and agents, and the agent
      share keeps growing. Where this is heading: one human lead running a mostly-agent team. This
      role is for someone who wants to build that, not read about it.
    </p>
    <p class="mb-4">
      Your mandate is everything behind the product: the data platform that turns millions of
      permits into intelligence, the infrastructure it runs on, and the AI harness that runs all
      of it.
    </p>
    <p class="mb-4"><strong>
      When a trillion-dollar economy leans on building permits as its leading signal, you realize
      just how powerful our data is - and why we're obsessed with structuring it.
    </strong></p>
  </div>
</section>

<!-- about shovels -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">About Shovels</h2>
    <p class="mb-4">Building permits are the leading signal for a trillion-dollar economy. Every renovation, solar install, and commercial build leaves a paper trail, and we turn that trail into intelligence: who builds what, where, and how well. Backed by multi-million-dollar VC funding and a growing customer base, we're building the intelligence layer for the built world.</p>
    <p class="mb-4">We're a small, fully remote team: engineering in Europe, business in the US. What started as two people with a big vision is still scrappy, still all-in.</p>
  </div>
</section>

<!-- how we actually build -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">How We Actually Build</h2>
    <p class="mb-4">Everyone says they use AI. Here's what that means at Shovels, concretely:</p>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>We built our own AI harness</strong> on top of Claude Code: 139 skills across 31 plugins at last count, with ~580 commits to that repo in the past 30 days. More than half of the people shipping to it aren't engineers; sales, finance, and marketing run their own agent workflows too.</li>
      <li><strong>Agents write production code end to end.</strong> New data adapters get implemented, tested, quality-checked, and PR'd by an agent pipeline. A human reviews and owns the merge.</li>
      <li><strong>Our morning on-call round is an agent harness.</strong> It scans the whole scraping fleet, investigates suspects with adversarial verification, files the tickets, and writes the report. A human reads it and makes the calls.</li>
      <li><strong>We plan with evidence.</strong> For a recent API over a 159-million-row dataset, agents generated four rival architectures, we killed two on evidence, built a disposable proof of concept at full production scale overnight, and ran eight rounds of blind multi-agent review before writing any product code. Every load-bearing claim gets verified against live data before a plan is allowed to rely on it.</li>
    </ul>
    <div class="mb-4">
      <iframe width="100%" height="315" src="https://www.youtube.com/embed/j3_JYppwcyo?si=gRLk9mIyDK_1DDDu&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <p class="mb-4">The principle behind all of it: <strong>generation is cheap, verification is the job.</strong> Humans set direction and own every decision; agents generate, measure, and attack. The bar for shipping is simple: you may only ship work, yours or an agent's, whose errors you could have caught.</p>
    <p class="mb-4">And don't take our word for any of this. We published the working notes from planning our newest API, rival architectures, refuted claims, prevented incidents and all: <a href="https://shovelsai.github.io/team-notes/2026-07-07-a9e2-how-we-plan-with-agents.html" class="text-emerald-900 underline hover:no-underline">Measure first, then plan (public edition)</a>.</p>
  </div>
</section>

<!-- how we work -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">How We Work</h2>
    <p class="mb-4">Written-first, and not as ideology: engineering is in Europe, business is on the US West Coast, so anything important has to survive a 24-hour round trip in writing.</p>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>Meetings are for decisions, not updates.</strong> Most engineers here have two or three meetings a week.</li>
      <li><strong>Two-week cycles, planned to about 80%</strong> so reality has room to interrupt.</li>
      <li><strong>AI Lab every Friday:</strong> 30 minutes of trading agent workflows, prompt patterns, and tool demos with each other.</li>
      <li><strong>Radical transparency:</strong> you'll see the financials, join strategic planning, and have a real voice in where the company goes.</li>
      <li><strong>Every engineer leads a real project within their first two quarters.</strong> Full authority, kickoff to ship. It's scheduled, not granted by tenure.</li>
    </ul>
  </div>
</section>

<!-- what you'll do -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">What You'll Do</h2>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>Build and scale the data platform:</strong> Python, Prefect, dbt, DuckDB, Polars, and Trino processing millions of permit records daily.</li>
      <li><strong>Develop the harness itself:</strong> new skills, multi-agent workflows, agent observability, and the tooling that lets one engineer direct many agents. Not just use it. Build it, then use it to ship.</li>
      <li><strong>Own the infrastructure:</strong> shape our AWS architecture, deployed with Terraform and Docker.</li>
      <li><strong>Power the API internals:</strong> FastAPI on PostgreSQL, tuned for a growing customer base.</li>
      <li><strong>Go where leverage is highest.</strong> This role is deliberately unscoped. If the biggest win this cycle is in the pipeline, you're in the pipeline; if it's in the harness, you're in the harness.</li>
    </ul>
  </div>
</section>

<!-- stack -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">Our Stack</h2>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>Languages &amp; frameworks:</strong> Python, FastAPI, Polars, dbt, scikit-learn, Scrapy</li>
      <li><strong>AI engineering:</strong> Claude Code, Codex, Gemini CLI, and our own harness (skills, hooks, multi-agent workflows)</li>
      <li><strong>Gen AI:</strong> Anthropic, AWS Bedrock, OpenAI, Gemini</li>
      <li><strong>Orchestration:</strong> Prefect</li>
      <li><strong>Storage &amp; warehouses:</strong> Amazon S3, PostgreSQL, DuckDB, AWS Athena (Trino), Snowflake</li>
      <li><strong>Infrastructure:</strong> Docker, Terraform, AWS (Fargate, RDS, EC2)</li>
    </ul>
  </div>
</section>

<!-- who you are -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">Who You Are</h2>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>You've been living AI engineering, not watching it.</strong> Agents are how you work every day. You have opinions about harnesses, context, and verification, and you earned them by shipping.</li>
      <li><strong>Staff-level taste in system design.</strong> You know what to build, what to kill, and which decisions are two-way doors. You'd rather delete a design than defend it.</li>
      <li><strong>You can sketch the solution without AI.</strong> That fluency is exactly what qualifies you to review AI's version of it. Strong fundamentals in distributed systems, data wrangling, and cloud environments are the foundation this role stands on.</li>
      <li><strong>You love to experiment.</strong> New tool, new pattern, new model: you try it, measure it, and share what you learned.</li>
      <li><strong>Entrepreneurial.</strong> You see a gap, build the tool, ship it, and tell the team. Nobody hands you a spec here; you write them.</li>
    </ul>
  </div>
</section>

<!-- why shovels -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">Why Shovels?</h2>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>Impact from day one:</strong> your work directly shapes the product and the company.</li>
      <li><strong>Room to grow:</strong> early engineers lead projects and shape how a mostly-agent engineering org gets built.</li>
      <li><strong>Flexibility:</strong> fully remote, async-friendly, no strict 9-to-5.</li>
      <li><strong>Transparency:</strong> you'll see the inner workings of the business and help steer it.</li>
      <li><strong>Great pay + stock options:</strong> competitive salary and meaningful equity in a company on the rise.</li>
    </ul>
    <p class="mb-4">Twice a year we bring everyone together in person to connect, strategize, and celebrate.</p>
  </div>
</section>

<!-- how to apply -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">How to Apply</h2>
    <div class="flex flex-col md:flex-row items-center gap-6 md:gap-x-8">
      <div class="flex-1">
        <p class="mb-4">No lengthy forms, no take-home assignments. Send your resume and a quick note about why this role to <a href="mailto:luka@shovels.ai" class="text-emerald-900 underline hover:no-underline">luka@shovels.ai</a>. We'll set up a friendly chat about your past work, then a live working session on a real problem: you bring your own agent setup and you drive. We're interested in how you operate (direction, spec, verification), not just what comes out.</p>
        <p class="mb-4">The whole process is those two conversations. It costs you an afternoon, not a month, and you hear back from us either way.</p>
        <p class="font-bold">Let's build something amazing!</p>
      </div>
      <div class="flex-none w-full md:w-72">
        <img src="/images/careers/shovels-guy-pose9.png" class="w-full">
      </div>
    </div>
  </div>
</section>

<!-- using AI when you apply -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">Using AI When You Apply</h2>
    <p class="mb-4">Yes, obviously. Most companies pretend candidates don't have agents. You do, and we'd worry if you didn't, so here are the actual rules:</p>
    <ul class="list-disc pl-6 space-y-2 mb-4">
      <li><strong>The application: use your agents freely,</strong> including on this page.</li>
      <li><strong>The chat: just you.</strong> It's a conversation between people, not a test.</li>
      <li><strong>The live session: you and your agents together.</strong> Your setup, your workflow, a real problem. We're watching direction, spec, and verification, not typing speed.</li>
      <li><strong>The one thing we test raw:</strong> whether you could have caught your agents' errors. That's our shipping bar, so it's the hiring bar too.</li>
    </ul>
  </div>
</section>

<!-- optional challenge -->
<section class="my-12">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-6">Optional: Skip the Cover Letter</h2>
    <p class="mb-4">Show us something true instead. Grab a free trial API key at <a href="https://app.shovels.ai" class="text-emerald-900 underline hover:no-underline">app.shovels.ai</a>, point your agents at <a href="https://docs.shovels.ai" class="text-emerald-900 underline hover:no-underline">our API</a>, and send us one true, non-obvious thing about the built world, with the receipts: what you found, the queries that found it, and how you verified it wasn't an artifact of the data.</p>
    <p class="mb-4">Impress us with the finding or with how you directed your agents to it; the best submissions do both. This replaces the "why this role" note entirely, we read every one, and <strong>"we couldn't verify this" is the only wrong answer.</strong></p>
  </div>
</section>
