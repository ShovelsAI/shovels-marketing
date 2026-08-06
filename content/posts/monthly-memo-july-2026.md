title: Monthly Memo - July 2026
subtitle: The four proprietary datasets we call our own—and how they came to be
date: 2026-07-13
modified: 2026-07-13
category: Company
tag1:
tag2:
tags: Memo, Newsletter, Permits, Contractors, Decisions, Properties, Data ingestion, Acquisition, ReZone
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
slug: monthly-memo-july-2026
summary: This month's memo is the epilogue to Ryan's data journey—the four proprietary building blocks Shovels now owns outright. It traces how the company started with permits (buyer intent, invisible to Google), expanded to contractors and their license data, acquired ReZone to add government Decisions, and is now building nationwide Properties from tax assessor rolls across about 2,800 counties. The payoff is a circular, self-enriching system where Permits, Decisions, and Properties each enrich the others in near real-time.
image: /images/blog_images/monthly-memo-july-2026-hero.jpg

---

Last month, I sailed on Pinecrest Lake. This month, my family sails the Adriatic. I'll get to see the places where many at Shovels call home. It definitely feels like summer.

In this memo I will share more about our data strategy, the four unique, proprietary building blocks that we call our own, how they came to be, and what you should expect, by the end of summer, to see for yourself.

#### We started with permits

My <a href="https://www.shovels.ai/blog/monthly-memo-june-2026/" target="_blank">last memo</a> was about our journey from licensing data to building it all ourselves. This memo will be the epilogue to that story.

We started with permits. Permits are buyer intent. Permits are points in a timeline, or a heatmap, or an input into a data model. For this reason, permits are actually fascinating. I stumbled upon this in 2022 and wanted to be Stripe, or Google, for local, public government data. Once that was in the air, things moved pretty quickly.

Looking back, though, our first pitch deck barely mentioned permits at all. The market problem I chose to focus on was contractors. Contractors have very low signal on the internet. There's just not that much to build a profile around. Unlike most white collar jobs, especially software engineers, contractors kind of float through the interwebs undetected.

Enter… permits! Permits tell the story that the rest of the internet misses. Permits are largely outside the reach of Google, so we have to get the permits in order to tell the story about the contractors. Once you have the permits, you can say a whole lot about them.

Saying a lot about the contractors should be interesting to businesses, and I like B2B business models, so…

#### We expanded to contractors

We launched our permit API in August 2023. The contractor API launched in November 2023. The two were connected, of course. About half of permits had a contractor ID you could look up to get detail about the company that built whatever the permit described.

Permits lacked a lot of contact info for contractors, so we had to enrich using the state contractor license databases. These are also public but are hard to assemble. For two years we've been enriching our contractor data with these sources.

For a while, that was it. Permits, contractors, and contractor licenses. Then came ReZone.

#### We acquired a decisions company

It always seemed logical that we would go here. I even <a href="https://www.shovels.ai/blog/april-2023-newsletter/" target="_blank">wrote about it in April 2023</a>. It would be another 19 months before the opportunity came to quickly add this IP and customer base via an <a href="https://www.shovels.ai/blog/shovels-acquires-rezone/" target="_blank">acquisition</a>. So you could say we were already "there" when the deal presented itself. We went for it.

We loved that government minutes, agendas, and transcripts presented buyer intent and market activity *prior to* the building permit being filed. It made so much sense that we should have this.

The following six months, from January 2026 through June 2026, were a scramble. Acquiring and integrating another technology is never easy. We had to do that while dealing with a bunch of other stuff you do as a startup. A couple of months ago we completed a major milestone, setting up the decisions pipeline to run autonomously, and <a href="https://www.shovels.ai/blog/decisions-api-launch/" target="_blank">launching the API</a> so everyone can access the data.

So that made three proprietary datasets: Permits, Contractors, and Decisions.

And now, a fourth.

#### Now we're adding properties

Properties come from tax assessor rolls. Unlike our other three datasets, they're exclusively county-level. That makes it easier, but it's still hard!

For several months we've been exploring the space, connecting with other geospatial data enthusiasts on LinkedIn, and creating our own vocabulary about properties based on the many conversations that we've had with our largest customers.

The result: property and parcel data from about 2,800 counties in the US. We will use this information to enrich our Permit tables, and we'll use our Permit tables to enrich our Properties too. We'll also use Decisions to enrich Properties.

This circular, self-enriching motion feels like a new product. Tax assessors typically update property records once per year. It's usually just a markup on the assessed value. Most don't even bother to look at the permit records before they re-assess (we know because we've spoken to them!)

Our product will be different, unique, special. Nobody else in the market will be able to enrich Properties, in near real-time, from Permits and government Decisions.

I'm not sure when we'll have this one live, but we're moving as fast as we can!
