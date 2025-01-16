Title: December 2024 Newsletter
Subtitle: Cool new permit lookup features in the Shovels app and why we're going long on climate
Date: 2024-12-19
Modified: 2024-12-19
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: We added some new tools to the Shovels web app. We also now have a nationwide contractor directory, so anybody can look up contractors based on their service area, not just their work address. And we're doing a lot of data enrichment! 
Image: /images/summerhill.png


Doesn’t it feel like I haven’t written one of these in a while? Maybe it’s just me.

Either way, boy oh boy… do WE have some THINGS to REPORT this month. More below. 

- We launched! That thing we flooded your inbox about last month? It’s live and it works and we have the subscription invoices to prove it. This newsletter will probably mostly be about Shovels Online.
- We now have millions of home residents, contractor employees, and website domains. They’re all in the API and database files. Soon they’ll be in Shovels Online too. Who cares? YOU DO! I’ll tell you why.
- Coming up next month: modeled job values for more accurate contractor revenue segmentation. Super excited about this one!
- 10M new permits. A dozen new jurisdictions. A half-dozen new API endpoints. Overhaul of our [Coverage Dashboard](https://dashboard.stripe.com/subscriptions/sub_1QWfsBF4y5bBweC6N8xBg1c7). New jurisdiction profile pages in the web app...
- Yeesh, we’re ready for winter break!

# Quick reminder

You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 3,800 subscribers!

Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends.

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company).

# A better Shovels Online

![Summerhill contractor profile]({static}/images/summerhill.png)

I have been writing about this for a while. Now we have something to *actually* show you!

There’s plenty to improve but we can see what this little toddler will grow up to be and we’re awfully proud. The bones are good. We’re on our way to building a truly remarkable data exploration tool for the construction industry. 

Here are a few features that I personally love.

- **Download 1,000 records exceptionally fast**. This is not like the old app. You get 1,000 custom-filtered contractor or permit records in CSV format at lightning speed.
- **Combine building and permit attributes in your searches**. Find *solar* contractors who work on *commercial* buildings. Find *roofing* guys that specialize in the *residential* market. In any zip, any county, any city. Then download!
- **See contractor permit volume over time**. This is new! We now have helpful charts on contractor profiles that show how permit volumes change over time. Group by month, quarter, or year.
- **Jurisdiction profiles**. This was one of the major reasons for V2. We needed to refactor our API structure and how we filter by geographies and that led to this idea: profiles for every geography. Every city, every county, every address, every permit jurisdiction. You can see the very start of this now by clicking the **Search** menu in the top navigation.

Note: We’re restricting free trials to one week. If you want to extend or talk about pricing options, please reach out! We’re friendly and want to help. Best email for that is [sales@shovels.ai](mailto:sales@shovels.ai). 

# An even better API

The [V2 API](https://docs.shovels.ai/api-reference/permits/search-permits) has been out for a minute. People like it. It’s way better than V1, which we put together before we really knew how people like to query building permits. 

I predict that the V2 will stand the test of time. It’s modular, it’s elegant, and it works the way prop, climate, and construction tech developers expect it to work. It’s already pretty great and it will continue to get better. 

That better-ment has already begun. 

- **Contractor employees**. THIS IS A BIG ONE. Many, many, many of you have been asking to go deeper into the org. You don’t necessarily want the email or phone of the person who filed the permit. You want their procurement, finance, or marketing leader. Now you can get them in Shovels. This just launched [in the API](https://docs.shovels.ai/api-reference/contractors/list-contractor-employees) today. We’ll get this into the web app ASAP.
- **Contractor metrics.** We give you everything you need to count permits and sum revenue by month, quarter, or year for any contractor. Many of you asked for this! What’s the 2023 revenue for Joe’s Plumbing? We had to run SQL queries for you. Now you can do this self-serve with the API.
- **Geography metrics**. Since we roll permits into contractors and compute metrics, we figured this should happen to geographies too. Now we offer the equivalent metrics endpoints for county, city, and jurisdiction. We figure this will be GREAT for market intelligence as you decide where to expand.
- **Residents of addresses**. This is a cool one. When you get the geo_id of an address, you can look up who is associated with that address and get their email and phone. These emails and phone numbers are ad campaign-ready; they’re already associated with online identities that you can advertise against. There’s so much you can do with this!
- **Contractor domains**. Finally, contractor domains. I’ve been spending a lot of time working in Clay and am already seeing the benefits of having contractor domains to associate with other datasets. This is a work-in-progress and we’ll continue to add more domains (coverage is ~50% today). It’s clear to me, though, how much productivity this can unlock. We’re excited to be in the GTM trenches with you.

# Things to do with permits: run ads

I’m coming back to this use case because we just signed our first major online audience deal. 

This new customer is using permits to identify remodeling prospects in specific local geographies nationwide. They could maybe back into this audience using website visits, but it’s messy. Just because you googled how long a roof lasts doesn’t mean you’re looking to replace your roof tomorrow. 

So how do you know if someone’s actually in the market *now*? You look at their permits. We ran a few tests for these guys and it worked really well. We could provide them with a bunch of relevant home improvement segments that they can go and sell to their customers. We have a few other major deals like this in the works. 

Some examples of homeowners that we can identify:

- Likely to need a new roof
- Likely to make a major home purchase (refrigerators, stoves, couches) soon
- Likely to want a new home appliance warranty
- Likely in the market for a home maintenance subscription
- Likely in the market for pool supplies and maintenance

Each of these audiences can have hundreds of thousands of people, easily targeted online. Let us know if you want more details! 

Happy holidays! 