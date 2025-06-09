Title: May 2025 Newsletter
Subtitle: Discover new API features and company milestones!
Date: 2025-5-16
Modified: 2025-5-16
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels is entering a new phase with more resources and a focus on rapid growth. This one recaps our journey so far, announces major API and data updates, and introduces the first Shovels Permit Index, offering new insights into national permit trends. Exciting partnerships and more innovations are on the horizon!
image: /images/spi-county-map-q1-2025.png


Next week the whole team is in Nashville 🤠🪕 for our twice annual big Shovels Summit. It’s when our engineers and account execs get to break bread, brainstorm, and go on whiskey tours together. 

It’s going to be a blast. 

Also, please forgive us for slower ticket response times. We’ve carved out blocks for work, but it’ll be tricky to keep up with all of that *and* set our course for the next six months. 

We’ll figure it out, though. We always do.

# How far we’ve come

Next month I’ll write about the future of Shovels. We’re going to talk a lot about it next week. I mean, that’s really the *only* topic, but we’re breaking it down into its core units so we can build the picture back up.

I look forward to reporting back on all that to all of you.

For now, maybe a quick look-back? I can do it in Summit-sized chunks. 

## The first one: September 2023

Oh, I still remember picking up Luka and Petra at SFO. It was only my second time meeting Luka; hadn’t seen him since 2020. I’d never met Petra in person. We probably had $500 in monthly revenue then, just a couple of very small, early customers.

This one was really about getting to know each other and the business opportunity. We’d raised some money at this point, around $750,000, and the opportunity felt enormous.

We hosted a local happy hour, attended [Blueprint](https://blueprintvegas.com/) together in Las Vegas, and then scattered. 

## The API rebuild: March 2024

This was a lot of planning and meetings. We had more investors; our total raise came out to $1.5M. We had more customers, too. Monthly revenue grew to around $8K. 

We took a short trip to Hollywood for some customer and investor meetings. Luka and I went out one night to see Fred Armisen do live standup. That was great. 

We mapped out all of our customers at a WeWork in Santa Monica and took an SpaceX engineer out to a vegan lunch. He was playing with our API and had some helpful feedback. 

The API turned out to be “the thing” we would focus on for the next 6 months. Each Summit going forward would have “the thing” it focused on too.  It was at this Hollywood summit that we committed to trashing V1 and starting V2, with the goal to launch it and a new software experience later in the fall. 

At this point, the team was still just me, Luka, and Petra. 

## The V2 launch and skunkworks: October 2024

Trying to launch a product on a deadline is a special form of torture. I don’t like it. Everyone tells you that the project is on track, on time, going swimmingly, until it’s not, and then it’s a huge scramble and everyone’s blaming each other. 

That was my experience with a particular software agency that shall remain nameless. Next time we’re doing it in-house. 

We held our launch event in San Francisco. Betty had joined us in May, bringing all sorts of skills and resources, including event planning (a huge bonus!). So our event was lovely, everything about it, and our new product release limped over the finish line. 

More importantly, we made a major strategic decision that I get to announce next month. Tease! 

At this point we had two more on the revenue team and around $40K of subscription revenue. 

## Which brings me to Nashville: May 2025

We have resources: customers and cash. A lot of both, actually, and the agenda for Nashville is what to do now. 

The question is no longer about how to do a lot with a little, it’s about how to do a lot more, a lot faster, with a lot. 

This is the next phase of Shovels and you get to be part of it! 

# What’s happening now

We had quite a few updates in our May release! 

**Cursor-based API pagination**

Why you care: Shovels Online is going to move a lot faster. We haven’t made this upgrade yet ourselves, but we will. Anyone doing API integrations today will benefit as you splunk deeper into the results! 

**Expanded contractor state license coverage**

This one matters a lot! We now have all license data on every state licensed contractor - that’s a big deal! We use this data to enhance address, classifications, license numbers, and statuses. 

I truly believe we’re the best in the industry at this. 

**New address field: apn**

We have much more parcel number coverage and will eventually add this as a permit and contractor filter in our API and Shovels Online. 

**Online results ordering logic**

Whenever we return permit results, they’re always ordered descending by date, so the most recent ones are first. Many of you asked for this!

---

# Things to do with permits: make an Index

We’ve been talking about a Shovels Permit Index forever. A few weeks ago, I finally started building it. I needed a few things to fall into place first: a good public mapping experience, some better charting, and our Claude + Snowflake MCP server. 

With those in place, I can finally present to you this: Our first quarterly [Shovels Permit Index](https://www.shovels.ai/blog/shovels-quarterly-permit-index-q1-2025/). Here are a few interesting takeaways:

- We saw about 2 million new permits in Q1 2025, 6% fewer than the 2.1 million issued in Q4 2024.
- When you drill down to the county level, it’s a mixed bag across the US. California has a lot of permit shrinkage, with a few growth spots in rural areas. Florida and Texas are also mixed.
- D.R. Horton and Lennar top our list of most active builders in Q1 2025.

Here’s my favorite image from the report. I’m proud of this map! 

![Shovels Quarterly Permit Starts Q1 2025]({static}/images/spi-county-map-q1-2025.png)

One more thing: we’re also really happy to be closer now with the founders of [UrbanForm](https://www.urbanform.us/) (get deep zoning data) and [ReZone](https://re-zone.ai/) (track zoning changes). Permit data is a logical counterpart to zoning data, and we keep trying to find partners who can work on this with us. We’re moving faster now. 

More to come next month!