title: Florida Wants to Make Building ADUs Easier. Here's Where Things Stand.
subtitle: Five years of Florida permit data reveal where ADUs are booming, and where approval backlogs persist
date: 2026-04-24
modified: 2026-04-24
category: Data
tag1: ADU Content
tag2: Real Estate
tags: ADU Content, SB 48, housing policy, Florida
authors: Ruoji Tang
author_image: /theme/images/team/Ruoji.svg
author_title: Senior Marketing Manager
slug: florida-adu-sb-48
summary: Florida lawmakers want to make ADUs easier to build. Shovels' permit data reveal which Florida markets are building the most ADUs, how wide the approval time gap is, and what statewide reform could mean.
image: /images/blog_images/florida-adu-sb-48-hero.png

---

Florida has been pushing to make ADUs easier to build. In early 2026, state lawmakers came close to passing legislation that would require every city and county to allow homeowners to build accessory dwelling units in single-family residential zones with no public hearing required. <a href="https://www.wptv.com/money/real-estate-news/granny-flats-get-a-boost-as-florida-lawmakers-pass-housing-bill" target="_blank">SB 48 passed the Florida Senate 38-0</a> but stalled in the House on the final day of session.

To understand what statewide reform might mean for neighborhoods across Florida, we compiled data to capture a snapshot of ADUs as they stand today. We pulled five years of Florida ADU permit data from Shovels to look at how many ADUs are being built, where they're concentrated, and which jurisdictions move quickly (and which don't). Here's what we found.

> **Key Findings**
>
> - Florida ADU addresses grew 68% from 2021 to 2025, with a 2023 spike to 2,078, a brief 2024 dip, and a 2025 recovery to a new high of 2,113. This is the baseline before a statewide by-right mandate takes effect.
> - Cape Coral accounts for roughly 40% of statewide volume. New Smyrna Beach, Largo, and Pinellas Park are the consistent performers that don't get enough attention.
> - Approval times range from 2 days (Escambia County) to 347 days (St. Petersburg), a 174x gap that statewide reform efforts like SB 48 aim to close.
> - <a href="https://www.flsenate.gov/Session/Bill/2026/48" target="_blank">SB 48</a> passed the Florida Senate 38-0 but stalled in the House in March 2026 over a short-term rental dispute. ADU reform remains a top legislative priority and is widely expected to return in 2027.

## What Is an ADU, or "Granny Flat"?

First things first. An accessory dwelling unit is a secondary residence on the same lot as a primary home. Florida law calls them ADUs, but you'll also hear "granny flats," "granny pods," "in-law suites," "carriage houses," and "backyard cottages." Same concept, different names.

They come in a few forms: 

- A detached ADU is a separate structure in the backyard, like a cottage or carriage house. An attached ADU is an addition to the main house with its own entrance.
- A garage conversion turns an existing structure into livable space and tends to be the most cost-effective path.
- A junior ADU (JADU) is carved out of the existing home itself, typically under 500 square feet, often from a bedroom or interior space.

> For more on ADUs, check out our piece on <a href="https://www.shovels.ai/blog/adu-boom-2.8M-permits/" target="_blank">America's ADU Boom: What 2.8 Million Permits Reveal About the Housing Solution</a>.

## What Is SB 48 and What Does It Mean for the Future of ADUs?

Right now, ADU rules in Florida are a local patchwork. Some cities are more permissive, but many are restrictive. Parking requirements, design review committees, owner-occupancy mandates, and minimum lot sizes often make projects difficult, even when homeowners want to move forward.

That's what <a href="https://www.flsenate.gov/Session/Bill/2026/48" target="_blank"><strong>Senate Bill 48</strong></a> aimed to change. Under the proposed SB 48 framework, every jurisdiction would be required to allow at least one ADU on any single-family lot. More importantly, it would remove the most common roadblocks.

Applications would no longer be subject to discretionary review or public hearings. If plans meet code, the application goes through standard review. There are no neighborhood meetings, and no board approval needed. (As we found, some jurisdictions can take over a year to approve ADU permits. Removing discretionary review is exactly the kind of structural change that would make a meaningful impact.)

![Example of an ADU. Jacksonville Daily Record.]({static}/images/blog_images/florida-adu-sb-48-jacksonville.jpeg)
*Example of an ADU. Jacksonville Daily Record.*

The legislation also targeted quieter barriers that discourage homeowners. Cities would be prohibited from imposing additional parking requirements if existing space is sufficient. Adding an ADU wouldn't jeopardize a homeowner's homestead tax exemption. And while rentals would be allowed, local ordinances could prohibit leases shorter than 30 days. This was, ironically, the provision that ultimately helped sink the bill.

While the bill passed the Florida Senate 38-0 in early 2026, it <a href="https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82546" target="_blank">returned to the House</a> on the final day of session where it died in House messages. The sticking point: the Senate wanted to let cities ban ADUs from being listed as short-term rentals and the House refused. Rather than let that dispute hold up the broader housing bill, <a href="https://flhousingactionlab.substack.com/p/what-to-watch-in-the-last-week-of" target="_blank">lawmakers dropped the ADU provisions entirely</a>. 

All that said, affordable housing remains a top priority in Florida, and similar legislation is expected to return in the 2027 session.

## Methodology

To get an accurate pulse on ADUs in Florida now, we did things a little differently. We counted distinct ADU addresses in the Shovels permit database for Florida from 2021 through 2025. We used `COUNT(DISTINCT ADDRESS_ID)` to avoid counting sub-permits (electrical, plumbing, inspections) as separate ADU units. 

To identify genuine ADU projects rather than accessory structures broadly, we combined Shovels' ADU classifier flag with a keyword filter referencing an accessory dwelling unit, in-law suite, ADU, granny flat, second unit, or similar terms. This matters especially in Florida, where the classifier alone picks up screen enclosures, carports, and storage sheds that many jurisdictions permit under the same codes as ADUs.

We also excluded jurisdictions where we did not have consistent year-over-year data. All that said, we encourage treating the data as directional indicators rather than definitive permit counts for the state.

As many sources like the <a href="https://flhousingactionlab.substack.com/p/adus-in-florida-what-the-data-tells" target="_blank">Florida Housing Action Lab point out</a>, comprehensive tracking is incomplete, and many jurisdictions started tracking ADU counts only recently.

## How Has Florida ADU Activity Trended Over the Last 5 Years?

Looking at our limited dataset, Florida ADU activity grew roughly 65% from 2021 to the 2023 peak. Some of that 2023 spike reflects reconstruction activity in Cape Coral and Fort Myers following Hurricane Ian in September 2022.

![Graph: Florida ADU Permits by Year]({static}/images/blog_images/florida-adu-sb-48-permits-by-year.png)

| Year | ADU Addresses | YoY Change |
| --- | --- | --- |
| 2021 | 1,256 | — |
| 2022 | 1,386 | +10.3% |
| 2023 | 2,078 | +50.0% |
| 2024 | 1,769 | -14.9% |
| 2025 | 2,113 | +19.4% |

As a result, the numbers include more than just organic ADU demand (as the jurisdiction-by-jurisdiction breakdown in the next section indicates), but the trend does show real growth.

ADU activity is running at roughly 1,300 to 2,100 addresses per year statewide, and we're seeing modest but steady permit activity in markets that have formalized their ADU programs.

The 2024 dip is real but short-lived. It mirrors the broader Florida construction cooling: higher insurance costs, slower in-migration, and a market absorbing a surge of new supply from 2022 and 2023. 

The especially active 2024 hurricane season completes the picture. Hurricane Milton made landfall near Siesta Key in October, hitting the same Southwest Florida markets that were still recovering from Ian. Cape Coral and Sanibel, which together account for a large share of statewide volume, would have felt that most acutely. The 2025 recovery to 2,113, a new high, suggests underlying demand held through it all.

As more jurisdictions begin systematically tracking ADUs, we anticipate a fuller picture of the trend.

> For a broader breakdown of Florida's housing market trends over the past five years, check out our <a href="https://www.shovels.ai/blog/florida-housing-market-building-permit-data/" target="_blank">Florida Housing Market Outlook</a>.

## Where Are Florida ADUs Actually Being Built?

Statewide totals make up only part of the story. ADU activity in Florida is highly concentrated, and a few markets are doing most of the work. 

In our dataset, Cape Coral stands apart. Its surge in 2023 and renewed strength in 2025 reflect the long tail of Hurricane Ian rebuilding. That's a localized dynamic, but it's large enough to shape statewide numbers.

![Graph: Florida Jurisdictions With High ADU Activity]({static}/images/blog_images/florida-adu-sb-48-jurisdictions.png)

| Jurisdiction | 2021 | 2022 | 2023 | 2024 | 2025 | 5-Yr Total |
| --- | --- | --- | --- | --- | --- | --- |
| Cape Coral | 401 | 502 | 1,037 | 615 | 956 | 3,433 |
| Pinellas Park | 104 | 175 | 153 | 135 | 111 | 619 |
| New Smyrna Beach | 113 | 130 | 92 | 89 | 94 | 498 |
| Largo | 77 | 54 | 38 | 135 | 146 | 406 |
| Hillsborough County | 75 | 51 | 75 | 89 | 81 | 363 |
| Walton County | 81 | 70 | 40 | 44 | 35 | 266 |
| Sanibel | 50 | 21 | 95 | 46 | 25 | 218 |
| Melbourne | 52 | 64 | 42 | 44 | 13 | 211 |

Beyond that, we see a cluster of mid-sized markets consistently producing ADUs year after year.

New Smyrna Beach is a quieter story worth watching. It posted 90 to 130 addresses per year, consistently, in a market that rarely makes housing headlines. Largo shows a different pattern: modest early years followed by a jump in 2024 and 2025, suggesting the market is starting to move. 

Pinellas Park holds its position as the Tampa Bay area's most consistent ADU market. Hillsborough County, the county surrounding Tampa, is also worth watching. The jurisdiction added 363 addresses over five years, and Tampa itself contributes another 104. Together, that's nearly 470 in the Tampa metro, making it one of the more active regions in our statewide dataset.

> For a deep dive at what's driving construction activity across the Tampa Bay region, see our <a href="https://www.shovels.ai/blog/tampa-housing-market-permit-data/" target="_blank">Tampa housing market breakdown</a>.

## How Long Does ADU Approval Take Now?

If there's one place where ADU reform could have immediate, meaningful impact, it's approval timelines. We found that in the past 5 years, the gap between jurisdictions has been extreme. Some areas moved permits through in under two weeks. Others took nearly a year.

Here are the median approval days over five years across multiple jurisdictions. 

**Fastest jurisdictions:**

![Graph: Median Approval Days for the Fastest Jurisdictions]({static}/images/blog_images/florida-adu-sb-48-fastest-approvals.png)

| Jurisdiction | Median Days to Approval | ADU Volume (5-yr) |
| --- | --- | --- |
| Escambia County | 2 | 10 |
| DeSoto County | 8 | 171 |
| Winter Park | 10 | 14 |
| Longwood | 13 | 47 |
| Pinellas Park | 14 | 611 |
| Rockledge | 15 | 56 |
| Walton County | 16 | 194 |
| Newberry | 17 | 57 |
| Melbourne | 19 | 211 |

**Slowest jurisdictions:**

![Graph: Median Approval Days for the Slowest Jurisdictions]({static}/images/blog_images/florida-adu-sb-48-slowest-approvals.png)

| Jurisdiction | Median Days to Approval | ADU Volume (5-yr) |
| --- | --- | --- |
| St. Petersburg | 347 | 74 |
| Seminole County | 250 | 149 |
| Surfside | 93 | 20 |
| Maitland | 70 | 73 |
| Pembroke Pines | 57 | 169 |

On the faster side, Pinellas Park and Walton County are useful benchmarks. They report solid volumes and fast approvals. That combination is what a functioning ADU pipeline looks like.

On the other end, St. Petersburg stands out for the opposite reason. It's not just slow. It's slow at scale. A 347-day median approval time in a relatively active market signals a structural bottleneck, not a one-off issue.

For builders and contractors, the approval time gap has direct implications for project economics. A 14-day approval in Pinellas Park versus a 347-day approval in St. Petersburg isn't just inconvenient. It changes the carrying cost calculation on every ADU project you bid.

## What Would By-Right ADU Reform Mean for Florida Homeowners and Renters?

SB 48 stalled, but what it proposed for homeowners was anything but abstract. Right now, the ability to build an ADU in Florida depends almost entirely on what local jurisdictions decide.

Under the proposed framework, homeowners would be able to build an ADU without going through a public hearing. Neighbors could still weigh in, but they would not have veto power. If your plans meet code, the application goes through standard review. Owner-occupancy mandates, one of the most common blockers for homeowners who don't live full-time on the property, would be removed.

For Florida homeowners who want to build a backyard cottage or convert a garage but hit a wall during the approval process, these changes would be decisive. If you're waiting to start a project, it's worth watching closely to see if the bill is reintroduced.

The financial case for ADUs depends on the market, but it's a real opportunity in many parts of Florida. In the Tampa Bay area, a well-finished one-bedroom ADU rents for about <a href="https://craftlineremodeling.com/adu-construction-tampa-2025/" target="_blank">$1,200 to $1,800 per month</a>. Build cost for a detached ADU typically runs <a href="https://www.angi.com/articles/how-much-do-adu-costs.htm" target="_blank">$150 to $300 per square foot</a>. A garage conversion can come in at <a href="https://www.angi.com/articles/cost-to-convert-garage-to-adu.htm" target="_blank">$60,000 to $150,000</a>. Over time, a steady rental income can offset construction costs, especially for lower-cost builds.

![Many homeowners turn ADUs into short-term rentals for extra income.]({static}/images/blog_images/florida-adu-sb-48-short-term-rental.png)
*Many homeowners turn ADUs into short-term rentals for extra income.*

For renters, ADUs are in demand as affordable housing. <a href="https://www.huduser.gov/portal/pdredge/pdr-edge-trending-072425.html" target="_blank">HUD-funded research on ADU rental pricing</a> suggests ADUs tend to come in below local market rents, making them one of the more accessible options in constrained rental markets. For a state with nearly a million cost-burdened renter households, that matters beyond the individual homeowner's bottom line.

But at the end of the day, not every ADU is about savings or extra income. A large share are built for family use: aging parents, adult children, or multigenerational living arrangements. <a href="https://states.aarp.org/florida/addressing-housing-affordability-in-florida-the-role-of-accessory-dwelling-units-adus" target="_blank">AARP</a> was one of the loudest supporters of SB 48 precisely because multigenerational housing presents an attractive option in Florida. This demand doesn't always show up in rental data, but it's a major driver of interest.

## What Would By-Right ADU Reform Mean for ADU Builders and Contractors?

From a builder's perspective, the opportunity is less about statewide totals and more about where projects actually move. The underlying demand is durable: Florida's rental market is under real pressure, and ADUs are one of the few ways to add supply in established single-family neighborhoods without large development infrastructure.

Cape Coral and the surrounding Lee County area offer volume. New Smyrna Beach and Largo offer the kind of consistent, steady pipeline that works well for smaller operators. In the Tampa Bay corridor, Pinellas Park and the broader Hillsborough County market combine steady demand with fast approvals, the combination that matters most when you're trying to keep projects moving. 

Approval timelines, in particular, will shape how you set expectations with clients. A project in Escambia County might clear permitting in a week. The same project in a slower jurisdiction could sit for months. That difference needs to be priced in from the start.

If and when reform does pass, it should start to shift the map. Markets that haven't yet shown strong ADU volume stand to benefit most from by-right approvals. As those rules take hold across every Florida jurisdiction, the geographic distribution of ADU activity is likely to broaden.

## What Comes Next for Florida ADUs

Florida already has more ADU activity than most people realize: roughly 1,300 to 2,100 addresses per year in recent data. The trend is upward: strong growth through 2023, a brief 2024 dip, and a 2025 recovery to a new high. A handful of markets are doing most of the work, while tracking remains inconsistent. Statewide reform, if and when it passes, would accelerate all of it. 

The policy momentum behind ADUs in Florida is real, and notably bipartisan. <a href="https://www.flsenate.gov/Session/Bill/2026/48" target="_blank">SB 48</a>'s 38-0 Senate vote makes clear that this isn't a partisan fight. The question isn't whether Florida will eventually require by-right ADUs statewide, but when. Similar legislation is widely expected in the 2027 session.

At the same time, it's worth keeping expectations grounded. Removing zoning barriers doesn't reduce construction costs. Building an ADU still requires meaningful capital, and the economics don't work everywhere.

Where the policy matters most is in high-demand markets: places where housing is already constrained and additional supply can be absorbed. The approval time gaps and geographic concentration in our data are exactly the argument for why reform matters.

That's what makes this permit data valuable right now. Shovels tracks all of this in the permit record, at the address level, across every Florida jurisdiction we cover. When reform does pass, this baseline is what we'll measure against. 

> The full Shovels dataset is accessible via <a href="https://www.shovels.ai/permit-database" target="_blank">Shovels Online</a>, <a href="https://www.shovels.ai/api" target="_blank">API</a>, or <a href="https://www.shovels.ai/data-feed" target="_blank">Enterprise Data License</a>, whatever fits your workflow. Or, if you need a customized solution, <a href="https://www.shovels.ai/contact" target="_blank">just let us know</a>.

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is Florida Senate Bill 48 and did it pass?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Senate Bill 48 would have required every Florida city and county to allow at least one ADU on any single-family residential lot, removing the most common local barriers including public hearings and discretionary review. The bill passed the Florida Senate 38-0 in early 2026 but stalled in the House on the final day of session over a dispute about short-term rental restrictions. ADU provisions were dropped entirely rather than hold up the broader housing bill. Similar legislation is widely expected to return in the 2027 session.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Which Florida jurisdictions have the most ADU permit activity?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Cape Coral leads Florida ADU activity by a wide margin, accounting for roughly 40% of statewide volume with 3,433 addresses permitted over five years (2021–2025). Other consistent performers include Pinellas Park (619), New Smyrna Beach (498), and Largo (406). The Tampa metro — combining Pinellas Park and Hillsborough County — adds nearly 470 more, making it one of the most active ADU regions in the state.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How long does it take to get an ADU permit approved in Florida?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">ADU approval times vary dramatically across Florida jurisdictions, from as few as 2 days in Escambia County to a median of 347 days in St. Petersburg — a 174x gap. Fast-approving markets like Pinellas Park (14 days) and Walton County (16 days) also post strong permit volumes, showing that speed and demand can coexist. Removing discretionary review, as SB 48 proposed, is specifically aimed at closing this gap statewide.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How has Florida ADU permit activity trended over the past five years?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Florida ADU addresses grew roughly 68% from 1,256 in 2021 to 2,113 in 2025, reaching a five-year high. Activity peaked in 2023 at 2,078 — partly driven by Hurricane Ian rebuilding in Cape Coral and Fort Myers — before a brief 2024 dip. The 2025 recovery to a new high suggests underlying demand held through broader Florida construction cooling and two active hurricane seasons.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What types of ADUs can be built in Florida?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Florida allows several ADU types depending on local zoning: detached backyard cottages or carriage houses, attached additions with separate entrances, garage conversions, and junior ADUs (JADUs) carved out of existing interior space. Garage conversions tend to be the most cost-effective path, often running $60,000 to $150,000. Under the proposed SB 48 framework, all Florida jurisdictions would have been required to allow at least one ADU type on any single-family lot.</p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Florida Senate Bill 48 and did it pass?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Senate Bill 48 would have required every Florida city and county to allow at least one ADU on any single-family residential lot, removing the most common local barriers including public hearings and discretionary review. The bill passed the Florida Senate 38-0 in early 2026 but stalled in the House on the final day of session over a dispute about short-term rental restrictions. ADU provisions were dropped entirely rather than hold up the broader housing bill. Similar legislation is widely expected to return in the 2027 session."
      }
    },
    {
      "@type": "Question",
      "name": "Which Florida jurisdictions have the most ADU permit activity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cape Coral leads Florida ADU activity by a wide margin, accounting for roughly 40% of statewide volume with 3,433 addresses permitted over five years (2021–2025). Other consistent performers include Pinellas Park (619), New Smyrna Beach (498), and Largo (406). The Tampa metro — combining Pinellas Park and Hillsborough County — adds nearly 470 more, making it one of the most active ADU regions in the state."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it take to get an ADU permit approved in Florida?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ADU approval times vary dramatically across Florida jurisdictions, from as few as 2 days in Escambia County to a median of 347 days in St. Petersburg — a 174x gap. Fast-approving markets like Pinellas Park (14 days) and Walton County (16 days) also post strong permit volumes, showing that speed and demand can coexist. Removing discretionary review, as SB 48 proposed, is specifically aimed at closing this gap statewide."
      }
    },
    {
      "@type": "Question",
      "name": "How has Florida ADU permit activity trended over the past five years?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Florida ADU addresses grew roughly 68% from 1,256 in 2021 to 2,113 in 2025, reaching a five-year high. Activity peaked in 2023 at 2,078 — partly driven by Hurricane Ian rebuilding in Cape Coral and Fort Myers — before a brief 2024 dip. The 2025 recovery to a new high suggests underlying demand held through broader Florida construction cooling and two active hurricane seasons."
      }
    },
    {
      "@type": "Question",
      "name": "What types of ADUs can be built in Florida?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Florida allows several ADU types depending on local zoning: detached backyard cottages or carriage houses, attached additions with separate entrances, garage conversions, and junior ADUs (JADUs) carved out of existing interior space. Garage conversions tend to be the most cost-effective path, often running $60,000 to $150,000. Under the proposed SB 48 framework, all Florida jurisdictions would have been required to allow at least one ADU type on any single-family lot."
      }
    }
  ]
}
</script>
