Title: August 2023 Newsletter
Subtitle: Lots of API updates and new states are launching this week
Date: 2023-8-17
Modified: 2023-8-17
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels, the leading provider of building permit and contractor API services, is expanding to Florida and Texas, with plans to cover all 47 remaining states by end of summer. We recently added date filters to our API, allowing users to easily access the most relevant data. Our team has also resolved any issues related to displaying dates in the API response. We are developing a new website that will offer registration and API key services, as well as a data explorer portal. Looking ahead, we are working on new market endpoints for building permits, providing valuable insights into current and historical trends by zip code. 
Image: /images/bottom5.png


Hello!

I like California. I've lived here my whole life, and so have both of my parents and most of my grandparents. That's why when we launched Shovels, we started in California. Why wouldn't we? California is the best 😎.

But we keep hearing that the home of the Grateful Dead and Clint Eastwood is just not enough. You want more, so by golly, you'll get more. We are launching Florida and Texas in just a few days. And soon after that... the remaining 47 🇺🇸!

Here's what else is going on:

*   **We added date filters to the API and fixed some issues displaying dates in the API response 🎉**
*   We're building out a brand new website on some brand new technology. It will allow us to quickly add registration and API key services, as well as a data explorer portal for you folks that prefer not to deal with API endpoints. 
*   That $249/mo price is live. On this plan you get 1,000 lookups per month in any  one state (so long as it's California... for now :) A self-serve pricing page will go up soon.

API update: Date filters!
=========================

Dates are important! You might not care about the roofing permit from 10 years ago, but you definitely care about the one filed last week. Our new date filters allow you to hone in on precisely the data you care most about.

We also now default sort permits by date descending, so in all responses, when you see a list of permits, the most recent ones are first.

This is live already (as of about 12 hours ago!)

To celebrate, we added two new demos: [Permit Directory](https://shovels.retool.com/embedded/public/9ab4b347-6227-4ee3-8648-b1e0dc632e1b) and [Contractor Directory](https://shovels.retool.com/embedded/public/e440a465-a280-44be-aa81-5388b8ac20ff). You have to add a zip code and both the start and end dates for the demos to work.

If you really want to test it out, you'll need an API key. Just reply and I'll get one for you. 

_Sneak preview: **markets**. We're starting to plan for a new set of markets endpoints that will tell you all sorts of interesting current and historical trends for building permits by zip code. This data will be fantastic for those who are trying to prioritize sales territories by identifying where certain types of building activity is happening._ 

Things to do with permits: Calculate approval times
===================================================

On most of our permits we are able to see the file date and the issue date, which bookend the jurisdiction's permit processing period. In other words, we can see which jurisdictions are slow and which ones are quick to approve permits.

For building developers, this is really important information. 

Since we keep hearing from EV charger companies, we decided to continue on our investigation of this industry with a post on EV charger permit approval times in California. We looked at every EV charger permit over the last few years and tallied them up by jurisdiction. 

Here's one insight: **We learned that Oakland approves EV charger permits 30X faster than LA**. Crazy, eh?

You can [read more about it here]({filename}ev-permit-approvals.md). 

[![Chart showing the 5 jurisdictions with slowest EV charger permit approval times]({static}/images/bottom5.png)]({filename}ev-permit-approvals.md)

Thanks for sticking with us. We're working hard to deliver the best building permit and contractor API in the country. And we're really close to covering the whole thing. 

We'll keep you updated!