title: Monthly Memo - June 2026
subtitle: Why we stopped licensing permit data—and the four proprietary datasets coming this year
date: 2026-06-15
modified: 2026-06-15
category: Company
tag1:
tag2:
tags: Memo, Newsletter, First-party data, Permits, Contractors, Decisions, Properties, Data ingestion, Scraping
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
slug: monthly-memo-june-2026
summary: On June 2, Shovels launched its Decisions API—the first expansion beyond permits, connecting decisions, permits, and contractors through shared geo_ids. Ryan ties the launch to a bigger shift: Shovels now gathers its permits, contractors, decisions, and property data 100% on its own, with no licensed records. By the end of the year, the company will have four interconnected proprietary datasets, all "Shovel-ready" for your data teams.
image: /images/blog_images/monthly-memo-june-2026-hero.jpg

---

Before I dive into this month's memo, I want to tell you about the <a href="https://docs.shovels.ai/api-reference/decisions/search-decisions" target="_blank">Decisions API</a> which launched on June 2. This is actually a pretty big deal, and it relates to my memo below about our transition away from data licensing. 

Decisions is our first expansion beyond permit data. Contractors and permits are closely tied. Contractor data lives on the permits, and we supplement with a separate collection of state contractor license databases. Permits are a whole other beast: different portals, different cadence, and a different technology to capture and process this data. 

As we've shouted from the rooftops many times, decisions and permits are related, but only in time and space; the public data don't actually connect. They're completely different gears of the public machinery. To connect them together, we have to do some work. 

With the release of our Decisions API, that work is done! We now have decisions and permits and contractors "talking" to each other via our common geo_id's. We'll find other ways to connect them too. 

Decisions is our first expansion beyond permits. It's entirely our own and it will rapidly improve in quality, coverage, and recency. For example, we're about to release our transcript-derived decisions, too. With transcripts, we can release *provisional* decisions while we wait for the minutes to post. 

Decisions are available now through our <a href="https://docs.shovels.ai/docs/shovels-api-introduction" target="_blank">API</a> and <a href="https://docs.shovels.ai/docs/shovels-cli-quickstart" target="_blank">CLI</a>. If you want a more hands-on tutorial, I'm happy to help! Just ping me at ryan@shovels.ai.   

#### A brief history of Shovels and scraping permits

A year ago, Shovels stopped licensing new permit data and relied entirely on our own technology to gather it. Two months ago, we removed our remaining historical licensed permits too.

Today our permits, contractors, decisions, and property data are gathered 100% ourselves. I don't think we'll ever license a core data product again.

Here's why: We don't like dependencies. We don't like them in our tech stack, and we also don't like them commercially. 

When you buy public records from Shovels, you're buying first-party data—not licensed. That matters because it means:

- We control quality, coverage, and continuity.
- We can bundle and process however we like, without vendor constraints.
- We'll never be forced to delete core historical data again.

That's all very important. 

#### How we got here

Luka and I met when we were each running businesses that scraped data about the mobile industry. My company looked inside mobile apps and discovered which software those apps used (e.g., Stripe or Google Maps). Luka's company captured the rankings, ratings, and reviews of mobile apps across hundreds of app stores worldwide.

Both were hard businesses to operate. Scraping in the late 2010s and early 2020s was constant whack-a-mole. I spent my days putting out fires while watching the mobile data aggregators (many were our customers) grow and grow.

"Next time, I want to be one of them," I told anyone who would listen (which was not many).

We merged our companies and Luka and I happily worked together until we sold the combined entity to a mobile data aggregator in the UK. Then we needed something else to do.

When it came time to start Shovels, I was very open to aggregating rather than scraping. We dabbled in permit scraping and confirmed it was hard and that we'd rather not do it. When we identified a permit data vendor who offered agreeable terms, we jumped in. For two years, they scraped and we supplemented with state contractor licenses, address datasets, and some offline jurisdiction permit gathering. Our APIs and data feeds were dependent on their data.

That was how Shovels worked until May 2025. After that, we were on our own—the cord was cut.

To our delight, the modern AI scraping toolkit made collecting online data *much* faster than the 2010s. We've been iterating on this nonstop ever since. The experience has improved dramatically but doing it reliably at scale is still hard. We built extensive monitoring infrastructure so we know immediately when a source stops delivering. We have all kinds of quality controls built into the pipeline as well, so if a source changes the way they display a field, we'll fix it before it pollutes production. 

We can build the source extraction AND the quality control AND the serving and display infrastructure simultaneously because of AI. 

This wasn't possible just a year ago! 

#### What happens next

The gist is this: we are a strong company and only getting stronger. We're innovating at the frontier on several fronts, taking leads in some areas and extending leads in others.

By starting in building permits, we cut our teeth on a very tricky data problem. We had to solve a wide range of tech challenges to get this far, and scraping was only part of it. Fortunately, the tech I've described here can be deployed across a wide range of public datasets.

It would only make sense, then, that we go after as much public data as possible. As I described at the very top, we're already doing it. By the end of this year we'll have four large proprietary datasets, all interconnected, all "Shovel-ready" for your data teams to use for critical business decisions. 

Permits, contractors, decisions, and properties… Oh my! 

Ryan
