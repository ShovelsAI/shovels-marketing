title: July 2025 Newsletter
subtitle: Shovels is now a geospatial business
date: 2025-07-15
modified: 2025-07-15
category: Company
tags: company, geospatial, esri
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
summary: This month, Shovels is at the Esri User Conference, announcing a new geodatabase with 170 million building permits, and plans to become more map-first. We're also working on a geospatial API and enhanced enterprise data licenses with Overture Maps integration.
image: /images/mappy.png


Last month, in case you missed it, we [announced our fundraise](https://www.shovels.ai/blog/shovels-raises-5m-seed-round-to-scale-ai-powered-building-permit-platform/). 

Raising funds is great; earning funds is even better. This newsletter is going to be about the latter.

This week, Betty and I are at the Esri User Conference. It’s where the world’s geospatial data community gathers and pays homage to the company that seems to have started it all. We’re happy to be a part of it.

We’re also happy to share that we now have a geodatabase with 170 million building permits on it, ready to share with the millions of ArcGIS users in the county.

More on this and everything else we’re working on is below! 

# Shovels, the geospatial business

I talk to a lot of our customers. Sometimes it’s a humbling experience. You give us a lot of feedback about Shovels Online and what could be better about it. You tell us where we need to look for more jurisdictions. You remind us how much *more* data is still out there. 

I don’t mind it. This is what we’re here for, and for those of you who are entrepreneurs, this should all sound very familiar. It wouldn’t be entrepreneurship without some criticism.

I shared a lot of detail about where we’re going. It’s a big mission and gets us all fired up to keep going every day. 

Since it’s Esri week, I want to share more about what “geospatial data” means to us. 

## More maps

![Don't worry, be mappy]({static}/images/mappy.png)

Shovels Online is not yet very “mappy.” That’s going to change. 

We might even go “map-first” so you can visualize all the contractors, all the permits, and all the properties before you toggle over to lists that you can download or push to your CRM.

Permits are inherently geospatial, but we don’t present them this way. We’re going to fix that and I’m very excited about it. 

Getting a slick geodatabase spun up was just the first step! Everything else will follow. 

> 🗺️
>
> If ArcGIS is your jam, we should talk! We are now able to offer full or partial hosted feature layers as part of our Enterprise Data License service.

## A geospatial API

Many moons ago I posted on LinkedIn about how the world (or the US, at least) needs an API service to look up a permit and return its building permit jurisdiction. 

I even shared the algorithm:

- Determine if a given address is within city limits
    - If not, return the county
    - If so, determine if the given city is a permit jurisdiction
        - If not, return the county
        - If so, return the city

Easier said than done! But it can definitely be done (and we’ve already done it.) What we haven’t done yet is made this data available as an API and web app. That’s coming next.

Other geospatial offerings that can follow:

- Polygons of permit jurisdictions so you can display them on any map, not just Esri maps
- Pre-computed permit density levels (we call this NVI, or neighborhood vitality index) for pre-defined (or arbitrary) geospatial areas
- Boundary box searching (so you can power your own maps with Shovels data!)

I’m also very excited about this! 

## Enhanced enterprise data licenses

I’ve written about this before too, but now with the general availability release of Overture Maps, we can truly tie permit activity to points-of-interest (POI) data like retail businesses. 

We can return all the Starbucks, Walmart, and Amazon building permits, because with Overture we can reliably associate permit addresses with businesses. It’s a real gift to the data community. 

We’ll start collect a lot more data about jurisdictions and addresses outside of our permit coverage zones, and while this is very exciting, it also will pose some customer support challenges as we explain why we know some things about jurisdictions but don’t (yet) have their permits. 

I share all of this to bring you along for the ride. It’s a good time 😊

# Shovels, the data business

When we shared our funding announcement, we also shared that we’ve migrated permit infrastructure. This was a massive effort and a huge upgrade. 

We’re now up to nearly 1700 jurisdictions covered and continue to add more jurisdictions and permits per month than we’ve ever added before. This month is no exception.

- 2.9M permits so far in 2025
- 251K permits since June
- 22K permits in July
- 1690 jurisdictions to date

It’s the middle of the month and we just did another huge data release. Why? Because we can. 

Our full dataset processing time is now under 12 hours and you know what that means… even more frequent updates! 

💥 We’ll be updating twice a month going forward 💥

# Shovels, the AI business

I have to remind people that we got [shovels.ai](http://shovels.ai) before ChatGPT was a thing. True fact! We got the AI because it was the only shovels domain available (we didn’t raise enough money to buy shovels.com).

The AI in Shovels, though, is quite obvious. We use it everyday, and we will be the first to make conversational AI available to anyone interested in construction activity. 

We're close. It's not ready yet, but we have a prototype, a [YouTube video](https://www.youtube.com/watch?v=j3_JYppwcyo), and a [landing page](https://www.shovels.ai/charlie) to get early signups. 

https://www.youtube.com/watch?v=j3_JYppwcyo

If you want to be one of the first to try it out, sign up for [the waitlist here](https://www.shovels.ai/charlie)!

# Things to do with permits: make contractor dashboards with Esri

I see many more of these in our future. We’ll also make them public. 

And since I didn’t say much about our contractor data in this newsletter, let me be clear, there is much to be excited about here too! 

Among them, new construction is clearly a need among Esri users, and we need to roll that construction into nationwide builders rather than breaking them up by state.

This is a start at showing how active the top builders are in the US. We’ve already started to report on them in our [quarterly permit index](https://www.shovels.ai/blog/shovels-quarterly-permit-index-q1-2025/) (the next one is coming out soon!) and we’ll continue to expand our ability to analyze new construction builders at nationwide scale. 

![Esri Dashboard for Shovels Top Contractors]({static}/images/esri-dashboard.png) 