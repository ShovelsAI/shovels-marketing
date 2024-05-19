Title: September 2023 Newsletter
Subtitle: 100M permits at your disposal 
Date: 2023-9-17
Modified: 2023-9-17
Category: Company
Tags: company
Authors: Ryan Buckley
Summary: I'm happy to share that we have processed all 100 million building permits nationwide. With the release of our markets endpoint, you can now see current and historical building permit counts for specific zip codes. We also revamped our API documentation to make it more user-friendly. We also updated our monthly API pricing.
Image: /images/sql.jpg


Greetings from Las Vegas. I'm on Day 5 and very happy to be heading home now. 😮‍💨

I feel proud today. The Shovels team, all three of us, had a very productive two weeks working together in-person. I'm going to share some highlights below.

*   **🚀 We processed 100M building permits! We can run custom SQL queries and export CSV files for residential and commercial buildings nationwide. 🚀**
*   States currently available in the API: California, Texas, Florida, and New York. Now that the rest are processed, we'll begin loading them into the API too. 
*   Speaking of API, we released our [markets endpoint](https://shovels.redoc.ly/#operation/Markets/operation/get_market_activity_by_zip_code_v1_markets_permits_zip_get). We count current and historical building permit counts on all of our zip codes sliced by any of our tags. I'll describe an interesting application for this data below! 
*   We also released [new prettier API docs](https://shovels.redoc.ly). Why does this matter? I'll tell you.
*   Our pricing matrix is good to go. You'll know what cost to expect when you're ready to get on this building permit data bandwagon. 

100 million building permits
============================

I know most people reading this newsletter aren't data nerds. I'm glad for that. I'm also glad that I'm surrounded by people who love thinking about and wrangling with data. Building permit data is particularly challenging because it uses data types that are prone to be inconsistent. 

For example, look at these addresses: 

*   4203 Pearl Gate Drive, Las Vegas
*   4203 Pearl Gate, Las Vegas, NV 89133
*   4203 Pearl Gate DR, 89133

You know these are all the same address. But you're human and you're an expert at deduction. How do you get machines, which aren't built for ambiguity, to know these addresses are the same? And then how do you get machines to fill in the missing address components? 

This is just one of many, many fascinating (dare I say fun?) problems we solved on the road to 100 million permits. I'm so proud of this team for getting through it so quickly. 

Because now we can do stuff like this. 

![SQL Screenshot]({static}/images/sql.jpg)

Yes, that's a screenshot of SQL. Yes, this is a marketing newsletter.

I just want to make a point about what it means to "process" 100 million permits. It means we have them all in a standard taxonomy that allows us to look up the same info across states, counties, and cities and run complex filters. 

What I'm showing here is a way to identify leads for solar installers. This query scans all 100 million building permits in about 3 seconds using inexpensive AWS technology. It's amazing what our team built. 

And now it can be yours!

Things to do with permits: Learn about neighborhoods
====================================================

Pretend you're in the market for a new home (or if you really are in this market, don't pretend, and I'm sorry). 

You are interested in two homes in the same city. They're comparable in size, age, amenities, school district, and price. You'd be happy with either one.

But there's a critical difference lurking below surface. They're in different neighborhoods, and different neighborhoods act... differently. We can measure this. 

Let's say one home is in a neighborhood with very little permit activity. The neighbors aren't maintaining, improving, or expanding their homes. They're not invested. 

The other home is in a neighborhood bustling with solar installs, new ADUs, and kitchen remodels. The homeowners are doubling down on their purchases, in it for the long haul. 

Which house would you prefer now? I know my answer.

This is a new way of looking at neighborhoods. I don't believe this data exists anywhere else. We want to help you get it out there! 

![Neighborhood improvement index]({static}/images/neighborhood-index.jpg)

Here's a heat map at the zip code level in my neck of the woods (we could also do this block-by-block) showing relative investment in ADUs, kitchens, and other additions. The SQL query that drives it is pretty cool too, but I'll just leave you with the map.

Beautiful API documentation
===========================

The first company I co-founded was [Scripted](https://www.scripted.com/). I'm a business guy, but I've always been fascinated by programming. I guess that's why I landed in tech. 

Early on at Scripted, I found reasons to get my hands dirty in Ruby and Python. I committed code, reviewed pull requests, and sprinkled bits of "Ryansoft" like fairy dust throughout our repository. I also worked with a lot of APIs, and I got to see the impact first-hand of thoughtful design and helpful documentation.

I admire companies like Stripe and Clearbit who make it easy for developers to use their products. I want Shovels to be the same. Fortunately, the competition in our market is pretty weak.

That's why we are going to make Shovels the most developer-friendly construction data API in the country.

Our [new API docs](https://shovels.redoc.ly) are searchable, have input and output samples, and a new page structure. Enjoy! 

Money talk
==========

Finally, yes, we are going to charge money for all this awesomeness. Here's how it looks. 

⛺️ $249/mo: 1,000 lookups, residential only, in one state

🏠 $749/mo: 5,000 lookups, residential only, nationwide

🏢 $2,499/mo: 50,000 lookups, residential and commercial, nationwide