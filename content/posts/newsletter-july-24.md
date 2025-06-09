Title: July 2024 Newsletter
Subtitle: This month we started rebuilding a few things. The results are exciting!
Date: 2024-7-10
Modified: 2024-7-10
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: This month's Shovels newsletter focuses on community engagement and significant updates. We announced new partnerships with Autodesk, Esri, and Deep Sync, and launched a public Discord server for better interaction. We introduced a new Shovels Coverage Dashboard for transparency and made pipeline improvements, including AI-driven permit classifications. Join us at the Esri User Conference, suggest ideas for our SXSW panel, and check out our comprehensive data insights and upcoming features.
image: /images/coverage.png


## Shovels July 2024 Newsletter
<br>
This month's update is all about community!

We have new partnerships. We have a public Discord server. On the data side, we're announcing a new coverage dashboard and a bunch of pipeline improvements.

*   Partnerships galore the last few weeks: We announced our [Autodesk integration](https://construction.autodesk.com/workflows/construction-software-integrations/shovels/) and our participation in the [Esri startup program](https://www.esri.com/en-us/about/partners/our-partners/startups) -- we are moving geo-spatially into construction project management!
*   And another partnership: [Deep Sync](https://deepsync.com/) for targeting homeowners with ads based on their permit history. I couldn't fit this one into the previous bullet. 
*   We'll be at the [Esri User Conference](https://www.esri.com/en-us/about/events/uc/overview) in San Diego next week! Reply or join our Discord (see below) if you can meet up. 
*   How about Austin in March 2025? We need ideas for a SXSW panel. We'll be your data partner. [Submissions are due](https://panelpicker.sxsw.com/) on July 21.
*   Speaking of reaching out, you can now [chat us up on Discord](https://discord.gg/Nypja3cKDx). We launched a public server! [Hop into our Discord](https://discord.gg/Nypja3cKDx) to chat with us about permits, contractors, data science, or the blink-182 summer concert tour (I went and it was EPIC 🤘)
*   Our customers love our transparency. Here's a big heaping spoonful of it: We released a **very** detailed [Shovels Coverage Dashboard](https://shovels.metabaseapp.com/public/dashboard/0573503d-88ac-4ba4-a723-346b55de482b). Now you can see exactly where we have (and don't have) building permit and contractor data! 
*   Our nationwide AI-driven permit classifications are available to our database and report customers. These are REALLY GOOD. I know because our most skeptical customers said so. We'll roll them out to the API and web app shortly. 

Quick reminder
==============

You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we have over 1,500 subscribers! 

Shovels exists to make building permit and contractor data useful. We're hearing from our customers that to be _useful_ we need to make permit data _insightful_.

That's where we're headed. 

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company). 

Our thesis as a data insights company
=====================================

We are not the only company selling tons of building permit records.

The big guys like ATTOM and CoreLogic and smaller ones like BuildZoom and Construction Monitor have been doing this for 10+ years.

What sets us apart, and the whole reason we built Shovels in the shadow of these incumbents, is to **make it easy** to get insights from building permit data.  

That's it! We bring data coverage transparency, self-service options, an API with great documentation, a public data dictionary, seamless data lake transfers, and enthusiastic one-on-one support to a huge industry that (clearly) needs it.

I've learned from our customers that clean, reliable, ready-to-use data about what's getting built and who's doing it is very valuable. They want frequent updates, complete coverage, and lots of ways to filter. 

I've learned from my team that doing all the above is hard. Very hard. Which is why, despite the long head start, the other guys haven't done it.

So that is our thesis for being here, doing what we do!

Here are a few highlights of what's coming this year: 

*   **Jurisdiction profiles.** We're rolling permits and contractors up by jurisdiction to offer insights like permit approval and construction times by permit type. A clickable dashboard for (almost) every building permit office in the country.
*   **Address profiles.** See every permit and contractor who worked on an address. 
*   **Permit portfolios.** Organize groups of permits that you want to track in one place. This feature is particularly useful for brokers and contractors.
*   **Permit inspection details.** Get the inspection history on a given permit to see how work is progressing. 
*   **Permit review details.** Find out why permits get stuck in review and how long each review step usually takes. 
*   **Subcontractor relationships.** GCs usually work with the same subs. Many jurisdictions document it. We're bringing these valuable relationships to light. 

We are very excited about all of this! It still feels like we're just getting started.

From the Engineering desk
=========================

Here are a few of the engineering tasks we finished last month. 

*   **AI Permit tagging**: Our new AI-enhanced tagging process is now active in the data pipeline, processing 120 million permits so far. This upgrade allows us to classify new permits more swiftly and efficiently, utilizing the latest AI methods to deliver industry-leading results.
*   **Enhanced address search**: We introduced a new [address search API endpoint](https://docs.shovels.ai/api-reference/#operation/search_addresses_v1_addresses_search_get). It is designed to simplify free-form address search for our customers and provide normalized addresses that can be used in other API calls supporting address parameters. This update aims to improve the user experience when using our API.
*   **Advanced contractor data handling**: Our contractor's dataset constantly evolves with new data and advanced data engineering techniques. To enable seamless customer integration, we now provide a full changelog detailing all changes from one month to the next.

Things to do with permits: make a coverage heat map
===================================================

With mapping on my mind, and a new coverage dashboard, I want to specifically call out our [new permit coverage heat map](https://shovels.metabaseapp.com/public/dashboard/0573503d-88ac-4ba4-a723-346b55de482b). 

We now have geo-coordinates on most of our permit addresses. We can bin these coordinates in 1 degree blocks to visualize our permit coverage. 

Check it out!  

![Explore our permit data using our web app]({static}/images/coverage.png)

It may not look like much, but this represents a TON of hard work -- pulling data from thousands of jurisdictions into dozens of data pipelines and finally into a single database of 140M geotagged building permits.

That's what I'm looking forward to talking about next week at the Esri conference.

And if you want to nerd out about it online, now you can [find us on Discord](https://discord.gg/Nypja3cKDx) 🤓