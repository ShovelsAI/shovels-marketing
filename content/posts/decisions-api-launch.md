title: By the Time a Permit Is Filed, It's Too Late. The Shovels Decisions API Beta Is Live.
subtitle: Phase two of the ReZone acquisition brings local government meeting intelligence into the same API you already use for permits and contractors.
date: 2026-06-02
modified: 2026-06-02
category: Product
tag1: Decisions
tag2: Real Estate
tags: decisions API, zoning, rezone, ReZone, planning commission, government data, product launch, intelligence layer, product
authors: Morgan Friberg
author_image: /theme/images/team/morgan.svg
author_title: VP of Marketing
slug: decisions-api-launch
summary: Shovels Decisions API Beta is live. Track zoning approvals, rezonings, and planning commission decisions across 600+ cities and nearly 200,000 records, months before permits are filed. Phase two of the ReZone acquisition.
image: /images/blog_images/decisions-api-launch-hero.png

---

If your product or service needs to be included in a major project, building permit data alone is not enough. By the time a permit gets filed, the decisions you care about have already been made. The rezoning. The planning commission sign-off. The demolition approval. The environmental review. The architects are chosen. The lenders are committed. The plan is locked.

That's the gap the Shovels Decisions API Beta closes. As of today, every Shovels user (free, paid, and enterprise) can query the same zoning and land use decisions that precede every major permit. This is phase two of <a href="https://www.shovels.ai/blog/shovels-acquires-rezone/" target="_blank">our acquisition of ReZone</a> in January, and it brings government meeting intelligence into the same API you already use for permits and contractors.

## Why decisions come before permits

Nearly every major permit (a new hospital, a new power plant, a new data center, a new shopping center) is preceded by a decision. Either vacant land has to be rezoned so it can become a wind farm, a data center, or housing, or an existing structure has to be demolished to make way for what comes next. At some point, a governing body has to weigh in.

Demolitions, environmental impact, and rezonings all require oversight and review. Elected officials, not just building department staff, participate in the discussion. These conversations happen every day across thousands of jurisdictions, from small rural communities to major metropolitan areas.

For companies that sell products or services that need to be included in the original project plans, permit notifications often arrive too late. By that point, many of the key decisions have already been made. The real advantage comes from knowing when the conversation starts, so you can reach the property owner, lender, architect, or builder early enough to shape what ultimately gets built.

## From 20,000 records to nearly 200,000 (and growing)

When Shovels acquired ReZone in January, the dataset covered about 100 cities and 20,000 decisions. Five months later, we're at 600+ cities and nearly 200,000 decisions. That's a tenfold increase in decisions and a sixfold increase in jurisdictions.

We always wanted to include this data in our API. We held off because searching for decisions in only 10% of jurisdictions was simply not enough. At today's launch, decisions coverage spans half the jurisdictions where we already have permit coverage. We expect to hit 100% parity in the coming months. After that, decisions coverage will likely surpass permits. The earlier signal will become the broader one. That's exactly the point.

## What you can do with Shovels Decisions

Decisions are built for teams whose work depends on knowing about projects before they break ground:

- **Data center and energy developers** following rezonings and zoning code modifications tied to power infrastructure, industrial uses, transmission lines, solar, and wind
- **Fiber and telecommunications teams** monitoring infrastructure decisions across target geographies
- **Building product and equipment suppliers** finding projects early enough to get specified into the original plans
- **Home builders and real estate investors** tracking rezonings and density changes that can shift land values before construction begins
- **Lenders and financial services** seeing which projects are moving from early discussion toward approval and permitting

When applicable, decision records will be linked to a property (address, coordinates, geographic IDs), to applicants, owners, developers, architects, engineers, contractors, and representatives. Decisions also connect to permits and jurisdictions, so a single project can be tracked from first city council mention to final certificate of occupancy.

## How to access Shovels Decisions Beta data

Shovels Decisions are currently available via our API and Enterprise Data License (bulk data shares). 

- **Shovels API (free and paid tiers).** Decisions endpoints are included in the free trial. If you have an API key, you can query decisions today.
- **Enterprise Data License.** Bulk Decisions can be added to your existing data license, and Decisions-only licenses are available. Existing customers, ping your account rep. New customers, <a href="https://www.shovels.ai/contact" target="_blank">contact sales</a>.
- **Shovels Online.** Decisions data will be added to the next version of Shovels Online for people who don't speak API. Decisions will be searchable, tied to permits and jurisdictions, and exportable for reports and AI agent workflows. Coming soon to a web browser near you!

You can find endpoints, parameters, and more information in our <a href="https://docs.shovels.ai/api-reference/decisions/search-decisions" target="_blank">API reference</a> and <a href="https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview" target="_blank">knowledge base</a>. The full field definitions for Shovels Decisions are available in our <a href="https://www.shovels.ai/data-dictionary#decisions" target="_blank">data dictionary</a>.

## Pricing

> During beta, Shovels Decisions costs one credit per decision. As Shovels Decisions comes out of beta—once we scale and refine the product offering—we will update the pricing. At that time, we will reach out to all customers.

## What's next: minutes are accurate. Transcripts are fast. We're bringing both.

A quick note on how we build decisions today. We extract them from official agendas and minutes, and we don't create a decision record until the minutes are posted. That gives us accuracy: the same words, figures, and votes the governing body actually approved. The tradeoff is timeliness. In many jurisdictions, minutes don't get posted until weeks after a meeting happens.

The other approach is to skip the minutes and work straight from meeting transcripts. Transcripts are available faster. They're also long, messy, and unverified. That gets you speed at the cost of accuracy.

We're not picking one. Phase one of Decisions, which is live today, is built on agendas and minutes. Phase two layers transcripts on top. We'll process a meeting transcript as soon as it's available so you get the earliest possible signal, then come back and enhance or correct that record once the official minutes are published. The fast version reaches you first. The authoritative version catches up behind it.

We're also working on **decision statuses.** Right now, every record in the API is a final decision. But the most valuable signal isn't always the final vote. It's the first time a project hits an agenda. It's the discussion at the planning commission. It's the postponement, the conditional approval, the item tabled for next month. Coming soon, decisions will carry statuses like *proposed*, *discussed*, *approved*, *disapproved*, and *postponed*, so you can act on a project well before the gavel comes down.

This fits the bigger picture of what we're building at Shovels: the intelligence layer for the built world. Local government data is public by law but inaccessible by design. We turn information buried in PDFs, agendas, minutes, and city portals into structured data objects like permits, contractor profiles, and decisions, built for APIs, spreadsheets, AI agents, and data warehouses.  As a first-party data provider, we acquire, enrich, and own the data outright. We focus on local government, and we make it useful.

Decisions are the earliest signal in that lifecycle. Now, they're available in your API.

## Frequently Asked Questions

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <dl class="space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What's the difference between Decisions and Permits?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Permits document construction that is actually happening. Decisions precede them — they're the zoning approval, planning commission sign-off, or demolition authorization that makes a project possible. If you need to reach projects before shovels break ground, Decisions get you there months earlier.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How many jurisdictions have Decisions data?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">600+ cities and nearly 200,000 decision records as of today. Coverage spans half of Shovels' permit jurisdiction footprint, and we're adding more every month. We expect to reach 100% parity with permit coverage within months.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How much does the Decisions API cost?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">During beta, each decision query costs one credit. Pricing may change when Decisions exits beta after we scale and refine the offering. All customers will receive advance notice before any price updates.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Are Decisions available on Shovels Online?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Not yet. Decisions will be added to the next version of Shovels Online with search, filtering, connections to permits, and export capabilities. This is coming soon for users who prefer web-based discovery over API access.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">When will meeting transcripts be available?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Phase two of our Decisions roadmap includes meeting transcripts, which will be processed and added to decision records as soon as they're available — faster than official minutes. Once minutes are published, transcripts will be enhanced with official verification and decision status flags like proposed, discussed, approved, disapproved, and postponed.</p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>

<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's the difference between Decisions and Permits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Permits document construction that is actually happening. Decisions precede them — they're the zoning approval, planning commission sign-off, or demolition authorization that makes a project possible. If you need to reach projects before shovels break ground, Decisions get you there months earlier."
      }
    },
    {
      "@type": "Question",
      "name": "How many jurisdictions have Decisions data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "600+ cities and nearly 200,000 decision records as of today. Coverage spans half of Shovels' permit jurisdiction footprint, and we're adding more every month. We expect to reach 100% parity with permit coverage within months."
      }
    },
    {
      "@type": "Question",
      "name": "How much does the Decisions API cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "During beta, each decision query costs one credit. Pricing may change when Decisions exits beta after we scale and refine the offering. All customers will receive advance notice before any price updates."
      }
    },
    {
      "@type": "Question",
      "name": "Are Decisions available on Shovels Online?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not yet. Decisions will be added to the next version of Shovels Online with search, filtering, connections to permits, and export capabilities. This is coming soon for users who prefer web-based discovery over API access."
      }
    },
    {
      "@type": "Question",
      "name": "When will meeting transcripts be available?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Phase two of our Decisions roadmap includes meeting transcripts, which will be processed and added to decision records as soon as they're available — faster than official minutes. Once minutes are published, transcripts will be enhanced with official verification and decision status flags like proposed, discussed, approved, disapproved, and postponed."
      }
    }
  ]
}
</script>

> **Ready to try the Beta?** <a href="https://app.shovels.ai/signup/" target="_blank">Sign up for a free Shovels account</a> and start querying the Decisions endpoints, or <a href="https://www.shovels.ai/contact" target="_blank">contact sales</a> about bulk and enterprise access.
>
> **Want to learn more?** Read <a href="https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview" target="_blank">What are Shovels Decisions?</a>, <a href="https://docs.shovels.ai/docs/knowledge-base/data/decisions/decision-to-permit" target="_blank">From Decision to Permit</a>, or browse the full <a href="https://www.shovels.ai/data-dictionary#decisions" target="_blank">Decisions data dictionary</a>.
