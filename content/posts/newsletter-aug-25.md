title: August 2025 Newsletter
subtitle: Expansion, contraction, and government inbounds
date: 2025-08-19
modified: 2025-08-19
category: Company
tags: company, expansion, government
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
summary: This month we focus on jurisdiction expansion, processing time improvements, and new government partnerships. We're also working on enhanced property types and new tags for better permit identification.
image: /images/louiville.png


OH MAN. 

We've been BUSY. 

I look at the top right corner of my MacBook and it's August 19th and I haven't even started writing the dang newsletter yet. 

WHAT. THE. HECK. 

August has been a scramble. I suppose that's what this newsletter will be about. We have had four killer months of revenue growth in a row and the further along we get, the more we want to do.

Luka, my co-founder, is actually getting stressed, which is unusual for him. I think that means we're onto something. 

This month we also got the most government inbounds we've ever had, from Washington, D.C. to Silicon Valley. Why now? Why all of a sudden? I'll ponder it below.

It feels like an exciting time to be aggregating and analyzing local government data. As always, we're glad to be along for the ride. 

*You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 4,700 subscribers!*

*Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends.*

*We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company).*

# Expansion and contraction

Our top 3 priorities right now are jurisdiction expansion, jurisdiction expansion, and jurisdiction expansion. 

Today we're at 1,767 jurisdictions covered. By next month that number should be over 2,000. That'll put us pretty much at the top of the heap. 

There's so much to do. We completed new architecture that enables us to build collection and parsing systems faster than ever. We have new teammates who bring new expertise and ideas about how to structure our system better. It takes some coordination but when it works, it's magic. 

This quarter we will complete our coverage of the major gov techs (the platforms that cities and counties use to manage their building permits, among other things). After this, we travel the backroads of jurisdictions that use custom software, or none at all. We're taking feedback from you on where to focus this effort. If you have opinions, [write to us](https://www.shovels.ai/contact).

That's expansion. The contraction component is our release frequency. We used to refresh monthly; now we are regularly updating every two weeks! Importantly, the time it takes to process a new release is down to just 4 hours. 

4 HOURS to re-process 170M+ permits?! This used to take three weeks, with servers crashing all over like a monster truck rally. 

The goal is to release weekly and then every day or two. This contraction in processing time enables all sorts of new product possibilities:

- A permit and contractor feed. Check it every morning to see what's new.
- Email or text alerts. Get notified when a permit status changes or a contractor starts a new job.
- Email, postcard, or SMS marketing. Pipe Shovels into one of these marketing platforms and run fresh campaigns as soon as new data comes in.

We talk about this all the time here in Shovels-land. This will continue to be the focus through the rest of this year.

# And more…

When we're not expanding our coverage, we're going to prioritize these two other projects:

## Enhanced `property_type` values

We've learned that you *really* care about what type of property the permits and contractors are associated with. You mostly care about residential and commercial, but there are use cases for the others too (industrial, agricultural, vacant land, exempt, miscellaneous, office, and recreational).

The problem is we also have a lot of NULL property_type values. Too many, if you ask us. We're able  to use other datasources to accurately fill these fields in. We expect to cut the empty value count in half. 

## New tags

We have a bunch of new tags coming up: `window_door`, `telecom`, `internet`, and `data_center` . These have all been requested by you to make it easier to identify these types of permits. We'll trickle them out through our enterprise tables through to the web app and API. We're aiming for a Q3 release here. 

# Things to do with permits: help the government

Like I said up top, we got some eye-opening inbounds from federal and city-level governments recently. Everybody seems to be thinking about permit reform, and specifically about the time it takes to get permits approved.

If you've ever pulled a permit yourself, you know what I mean. The waiting sucks.

We don't solve that problem (but [we considered](https://www.shovels.ai/blog/introducing-the-department-of-permit-efficiency-dope/) it 😉). Instead, we measure it. And as the Peter Drucker saying goes, "you can't manage what you don't measure." 

The irony is that even though governments issue the permits, they can't report on them. Certainly not at the regional level. Therefore, they're not *useful* from a measurement standpoint. I want Shovels to play a role in permit reform by helping to identify what's working and what's not working, where the top performers are and which jurisdictions need some help. 

We'll all benefit from some transparency here. Our next Shovels Quarterly Index report publishes soon and will feature some jurisdiction-level rankings. 

In the meantime, here's a little dashboard we did for our friends in Louisville, KY. They're doing well!

![Residential Building Permit Timeline Analysis for Louisville, Nashville, and Cincinnati]({static}/images/louiville.png)
