Title: October 2023 Newsletter
Subtitle: The Shovels API is live and self-serve! 
Date: 2023-10-17
Modified: 2023-10-17
Category: Company
Tags: company
Authors: Ryan Buckley
Summary: You can now sign up for your very own Shovels API key and start building awesome stuff with building permits. Our new web application is going to have more features to find contractors, look up permits, and get all the permits on any address in the country. 
Image: /images/app-auth-screenshot.png


This will be a newsletter about using the Shovels building permit API.

However, a new war began since our last newsletter, and I think first of the children. I don't know how to help other than to put this little mention in this little newsletter and try to stay positive. 

With that... back to permits. 

*   Last month, I said we'd work on loading every state into the API. This month, I get to tell you it's done! Yay! 
*   To celebrate this launch, we're making it easier to get API keys. You don't need to ask us first. Just register an account with [our sweet new app](https://beta.shovels.ai) and get your API key 💪
*   Don't know how to use an API? That's cool, for most of my life, I didn't either. I have a solution for you, too. Read below. 
*   If you do like APIs, don't forget about our [pretty API docs](https://shovels.redoc.ly) 😍 and check out our [API starter guide](https://www.shovels.ai/blog/how-to-use-the-shovels-api/).[](https://www.shovels.ai/blog/how-to-use-the-shovels-api/)

🇺🇸 The API is national 🇺🇸
=============================

These 100 million permits span:

*   24,593,329 addresses
*   14,688 zip codes
*   973 jurisdictions
*   656 counties
*   48 states

And across all of these permits we applied 33 unique "tags" in order to make it easy to cluster and slice these 100 million permits to your liking... **all by using the Shovels API**. 

**API wuh? 🤔**
===============

Here's my attempt at writing the shortest-ever tutorial on how to use an API. We have a more detailed [tutorial on the blog](https://www.shovels.ai/blog/how-to-use-the-shovels-api/). 

An API is like a set of defined questions you can ask a database using your favorite programming language. Each of these questions is called an "endpoint." 

For example, you can ask [this endpoint](https://shovels.redoc.ly/#operation/Permits/operation/get_permits_by_address_v1_permits_address_get) the question, "What are all the permits on 15 Cherry Lane, Anytown, MD?"

You can ask [this endpoint](https://shovels.redoc.ly/#operation/Permits/operation/get_permits_by_zip_code_v1_permits_zip_get) the question, "Which homes in the zip code 94123 pulled ADU permits in the last 6 months?"

And so on... each endpoint is purpose-built for you to ask a certain type of question. The questions our endpoints can answer are described in our [lovely API documentation](https://shovels.redoc.ly). 

If anything's unclear, please holler at me! I'll be happy to share my screen as we do some programming together.

API keys galore
===============

I've always thought that to be truly developer-friendly, a company should not stand in between developers and the API. The docs should be great, the API should be fast, and when inspiration strikes, software developers shouldn't have to wait for an API key.

So we've built an app to give you an API key whenever you want one. Just make an account at [https://beta.shovels.ai](https://beta.shovels.ai). You'll see your shiny new API key on the dashboard.

_Note: We built this thing for the web using a new mobile app technology called Flutter. That means we're going to release native mobile apps, too!_

100 million building permits in your pocket, coming soon to an app store near you.

![App screenshot]({static}/images/app-auth-screenshot.png)

Spreadsheets for the rest of us
===============================

Not everyone knows what JSON is. Even those in tech might think I omitted a vowel from the name of a popular YouTuber / investor. 

Regardless, I have a solution. We will run CSV files you as you need them, one-off or monthly, for roughly the same price as our API. We won't give you the entire database, but we'll accommodate you if you'll accommodate a monthly subscription. 

CSV files are super convenient and until we have a self-serve solution for you to query and download your own CSVs, we'll be happy to do it for you! 

Pricing page is live
====================

Why do I always save this section for last? I dunno! 

We can't give this data away for free. If you start using your API key, we will start asking you to pay for it. Pricing is going to be reasonable, though. The shared goal here is for you to use Shovels data and be absolutely thrilled with it.

Check out our pricing (with some minor updates from last time) here: [https://www.shovels.ai/pricing](https://www.shovels.ai/pricing).[](https://www.shovels.ai/pricing)

✌️ Peace