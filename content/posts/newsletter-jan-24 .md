Title: January 2024 Newsletter
Subtitle: With the help of ChatGPT, we are officially putting the AI in Shovels.ai
Date: 2024-1-4
Modified: 2024-1-4
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Summary: A custom GPT, millions of new permits and hundreds of thousands of new contractors. This is a major update to our database and the way you can access it!  
Image: /images/dashboard.png


Nice, I get to be the 32nd person to wish you a happy new year in a marketing newsletter 🤗

With that out of the way, let's get down to business!

*   With the help of ChatGPT, we are officially putting the AI in Shovels.ai. Preview [our custom GPT](https://chat.openai.com/g/g-apAxK8WGu-shovels-ai) before it goes behind a paywall later this month. Tell it to look up some permits! 
*   We added a bunch of new contractors and then de-duplicated them so searching by name is less confusing. We also improved the way permits are queried by zip code!
*   And more things to do with permit data: calculate permit approval times (soon with even more granularity). [](https://www.shovels.ai/blog/how-to-use-the-shovels-api/)

✨ Have you heard of ChatGPT? ✨
==============================

It might be true that we are shovels.ai because the .com was taken, but we've always known artificial intelligence would play a major role here.

OpenAI went and made doing that a whole lot easier by releasing custom GPTs late last year. These used to be called plugins, and they enable ChatGPT to interact with APIs like ours. So, we configured a custom GPT to use all of our API endpoints and [released it to the public](https://chat.openai.com/g/g-apAxK8WGu-shovels-ai)!

We hear that OpenAI is going to release a GPT Store later this month. When that happens, we'll put the ShovelsAI GPT in there. But for now, anyone with a ChatGPT Plus account ($20/mo) can use our GPT.

And, uhh... yea, it's pretty crazy. Here's what you can do:

*   Give it an address in plain text and ask for the permits.
*   Ask for a certain type of permit (heat pump? roof? foundation?) in a zip code.
*   Give it your address (or one nearby) and ask for a contractor recommendation.
*   Tell it to make a CSV from any result and give you a link to download it 😎 

We're going to release some more endpoints so you can filter by permit status, fees, and such. We'll also make it easier to filter by city (we only do zips and states right now).

We're super excited about this new way to use Shovels! [Check it out](https://chat.openai.com/g/g-apAxK8WGu-shovels-ai)! 

**🥳 A new product release worthy of 2024 🥳**
==============================================

We are also thrilled to announce our latest data update. Here are the highlights:

**Data Enhancements**

*   **Expanded Coverage:** Our jurisdiction, ZIP code, and city counts have increased, offering wider and more comprehensive data coverage:
    *   Jurisdictions: from 1,041 to 1,106
    *   ZIP+4 codes: from 113,255 to 121,926
    *   Cities: from 41,582 to 46,813
*   **Better Permit Geolocations:** Three million additional permits are now precisely geo-located, enhancing the accuracy of location data.
*   **More Contractors:** We increased the number of Shovels contractors by 17% to a total of 2.2M, covering 79K ZIP codes.
*   **Fewer Contractor Duplicates:** we’ve grouped contractors that belong to the same entity within a state. Different branches should now be represented as one contractor company.

**API Improvements**

*   **More intuitive ZIP code queries:** Querying our API is now more straightforward and includes all +4 extension results even if you only provide 5-digit ZIP code.
*   **Optimized Queries:** The introduction of materialized views has significantly boosted the efficiency and speed of API queries.

**Data Pipeline Updates**

*   **Metabase Integration:** Automation in QA and validation processes is enhanced through Metabase integration, offering immediate access to data insights.
*   **City Cleaning:** We've tightened our city cleaning process to ensure data accuracy.
*   **Address Updating:** Our permit address verification is more robust than ever, thanks to the automation of external address source processing.
*   **Data Extraction Advancements:** Progress in extracting more accurate data from raw fields continues, improving the overall data quality.
*   **Parallelism in Flows:** Processing efficiency has been boosted with further optimization of our data flows.

![Shovels permit directory]({static}/images/dashboard.png)

Things to do with permits: track approval times
===============================================

I like to listen to [these podcast interviews](https://www.capstonegov.com/podcast) of city council members, mayors, and economic development staff in Contra Costa County, where I live. Maybe not everyone's cup of tea, but I dig it. 

Frequently, and I mean wayyy more than you'd think, these civic professionals talk about **permit approval times**. The first mention was from the CEO of a local chamber of commerce. Then a very well connected commercial real estate broker said it. Then, once again, a local mayor mentioned how important this is. 

I had coffee a few days ago with the CEO of a regional economic development agency out here and she too said permit approval times are critical data for city and county managers to track. 

Shovels sees the permit file date and the issue date and can calculate the approval time. We did a [really thorough analysis](https://www.shovels.ai/blog/ev-charger-permit-processing-times-in-california/) of California EV charger permit processing times back in August. I plan to write another one on nationwide permit approval times next.

Here's some data from the midwest. What's going on, Louisville??

![Shovels permit directory]({static}/images/midwest.png)

Looking ahead
=============

Next month I'll announce some major progress on a new and improved web app. It's already looking awesome. 

Cheers to 2024!