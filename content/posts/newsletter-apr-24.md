Title: April 2024 Newsletter
Subtitle: We raised over $600,000 and have a robust roadmap
Date: 2024-4-10
Modified: 2024-4-10
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: We are very excited about the launch of Shovels V2. We know you are too. This is the start of the killer building permit application. The one that should have existed all along. We also can push 100 million building permits and contractors straight into Snowflake, Big Query, and Databricks.
image: /images/explore.png

## Shovels April 2024 Newsletter
<br>

Last month was a planning month for us. Luka and Petra joined me in California and we spent a lot of time together. We met a few of you in person, too.

All of this mingling and meeting helped us set the stage for the next phase of Shovels. We're growing up a bit. I'll explain what I mean. 

*   Shovels V2 is in the works! I'll share more about what exactly this means. In short: a whole bunch of stuff you've told us you need.
*   Because the V2 is our focus, I've neglected our iOS app development. It's just so V1. We'll get it launched in prep for V2, but it'll take us another month.  
*   PSA: We can now share 130M permits and 2.5M contractors directly into your Snowflake, Big Query, or Databricks account. This makes some data scientists VERY happy. 
*   Ever wanted a list of every building permit jurisdiction? [We released one](https://www.shovels.ai/blog/list-of-all-building-permit-jurisdictions/). We're working on a V2 of that, too. It will have at least 5,000 more jurisdictions!
*   Check out how [Beam](https://www.trybeam.com/), one of our happy customers, is using Shovels to [reach out to contractors](https://www.shovels.ai/blog/case-study-revolutionizing-lead-generation-for-beam/). 
*   Join us at our [Zero Carbon Building Happy Hour](https://lu.ma/z40116as) in Lafayette, CA on Earth Day, Monday April 22!

2 is better than 1
==================

There comes a time when you just need to cut bait and start over. After watching you use and build on Shovels, and building our own web and mobile apps, it became clear that our API design needed an overhaul. 

And not just a 1.1. We needed to sorta break everything. (But don't worry, V1 will be out for a while, and we'll help you through the transition!)

Here's what's so awesome about our V2. 

**Filters galore**

We're combining tax assessor data with permit data! The possibilities are endless. 

Filter building permits by lot and building area size, and number of units and stories. Want every solar permit on a $2 million house? Every ADU permit on a 20,000 sq ft lot? You'll have it.

You'll also be able to filter permits by city, county, and jurisdiction. I know, long time coming on this one.

Plus, there will be parity between permit and contractor filters. Want every solar _contractor_ who worked on a $2 million house? Every ADU _contractor_ who worked on a 20,000 sq ft lot? You get the idea.

This wasn't possible in V1 😉

**All new tagging**

Every Shovels user filters by permit tags. Now we're going to make them wayyyy better. Thanks to some AWS incubator credits, we can use AI to tag all 130M permits for us.

We're adding new tags and making them two-level. Check out the [working draft here](https://docs.google.com/spreadsheets/d/15rq0VbzD1FKcBzWAhGaAwbqlqm-BZa6nhM8F_qyNcMQ/edit#gid=0) and reply with your feedback. Let us know what's missing! 

The early tagging results are as amazing as you'd expect. What a time to be a data company. 

**More contact info**

We have A LOT more contact info on homeowners and contractors than we currently expose through the V1 API. This is going to change in V2.

In V2, you'll get the homeowners of a given address, all the people who work at a contractor company, and all the contact info.

As one customer recently told me, the industry needs a ZoomInfo for the building trades.

Because we know which contractors are actually active, Shovels is in the perfect position to deliver it. 

**All the profiles**

One of the interesting things we hear from customers is that Shovels is useful for investment and market selection decisions. However, we don't make it easy for them to count and roll up all of the permits by geo.

That's fixed in V2. I mentioned that cities, counties, and jurisdictions will be filters. Well, they'll also have profiles. 

Want to see every building permit in flight in Palo Alto? How long it's taking to get approval? We'll calculate permit approval times by tag or tag group. We'll also help you navigate between counties, cities, ZIP codes, and the elusive jurisdiction. Each one will have a profile.

Addresses will have profiles too! See all the permits, contractors, and roll up metrics on any address in our database. This is also coming in V2. 

We're a data company, but the software play is just so obvious. Somebody needed to build it. Why not us? 

Here's a little preview!

![Explore our permit data using our web app]({static}/images/explore.png)

Things to do with permits: get customers
========================================

One of the companies we spent time with in San Francisco is [Beam](https://www.trybeam.com/).

Beam helps contractors run invoices, collect payments, send estimates, and streamline other time-consuming parts of the job.

They're a smart, passionate team that loves to use data and technology to be more efficient, especially in their marketing. We're pleased to provide them with contractor and permit data that increases the conversion on their outreach and drives more revenue to their bottom line.

You can read the full case study [on our blog]({filename}case-beam.md) or [download the PDF]({static}/pdfs/Shovels_Beam.pdf).

So tell us what you want, what you really really want
=====================================================

Now is the time to influence what gets included in V2!