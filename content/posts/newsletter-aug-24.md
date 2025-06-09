Title: August 2024 Newsletter
Subtitle: Lots of API updates and new states are launching this week
Date: 2024-8-17
Modified: 2024-8-17
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: We introduce Neighborhood Vitality Index and our partnership with Esri.
image: /images/esri-nvi-map.jpg


In this newsletter we'll recap the summer (because according to my local school district, it's  *over*) and look ahead to fall.

But before I get into the bullet points, I want to offer a brief sentimental reflection. It was a year ago, August 2023, in this very newsletter, that we announced our first API pricing plans. We've come a long way since then.

On Friday I met with a HVAC software startup. They said how much they appreciate our fast API with self-serve keys, clean data, and great documentation. That's basically the nicest thing you could say to a guy like me.

They'll be a customer, alongside dozens of others paying us real money for permit and contractor data. One year in, Shovels is a real company.

August is our anniversary month, so I share this to say thanks.

----------------------------------------------------------------

Okay, enough looking backward -- here's what's coming up next!

- We will have a booth at [Blueprint](https://blueprintvegas.com/) in Las Vegas from Sept 17-19. Find us and say hi!
- We won't have a booth at [RE+](https://www.re-plus.com/) in Anaheim on Sept 9-12, but we will be walking around and meeting a lot of people (and a few of our customers) who do have booths. Reach out if you'll be there!
- We'll also be in NYC for some of [Climate Week](https://www.climateweeknyc.org/) from Sept 22-29. Lots of climate capital and tech will converge there and we are ready for it.
- For those of you new to this newsletter, don't forget to [find us on Discord](https://discord.gg/Nypja3cKDx). We're just getting started with our new online Shovels community.
- On the tech front, we added *start_date* and *end_date* to our database table shares and they'll launch in the API this week. It's a much better way to filter and query.
- We added *primary_email* and *primary_phone* to the contractors table. Many of you asked for this. We delivered!
- We also made more progress on contractor de-duplication. This will continue to be a work in progress -- and we will continue to be the very best at it.
- The wireframes on our new and improved web application are **DONE**. Let the building begin! Our new app is going to be awesome. I know this because of all the feedback you've given us on [the beta](https://app.shovels.ai/). We're still on track to release in **mid-October**.
- We can now merge permit data into geospatial files like parcels and census tracts. More on this site selection use case below!
- Finally, shout out to [Alex Katzman](https://www.linkedin.com/in/alexkatzman/) from [Growth Inflection](https://growthinflection.com/) for coming up with a phrase that you're going to see a lot more of: "shovel-ready data." Indeed, the difference between us and the others is just that: **Our data is shovel-ready**.

# Quick reminder

You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we have over 1,700 subscribers!

Shovels finds the value in local government data. We're focusing first on making building permit and contractor useful and accessible, but there's a ton of other data on the roadmap too.

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can  [read them all here](https://www.shovels.ai/blog/?category=Company).

# The hard thing about hard data

Last month I mentioned a bunch of features that we'll release in the next quarter or two. You can  [read the full list here](https://www.shovels.ai/blog/july-2024-newsletter/)  but I'll call out three of the ones that don't exist  *anywhere* today:  **permit review details**,  **permit inspection details**, and  **subcontractor relationships**.

Many jurisdictions provide this data, but it's buried deep in the "blob" of HTML that you get when you scrape the permit off the website. It's not included every time and the way that it's structured is prone to change.

Most of the other guys don't even grab it. We have this data but we haven't gotten around to processing and parsing it yet. We know there will be a gazillion edge cases to resolve once we get started.

This is what makes hard data hard. It's also what makes the work we do valuable. I want Shovels to keep getting better at it, to be the  *very best*, and to share what we find with the companies and organizations that need it.

I've been thinking about this a lot recently because Shovels, believe it or not, isn't just a building permit data company. It's where we're starting, and there is a LOT further to go down this rabbit hole, but at our core we are curious about all sorts of local government data.

This is the expertise we're developing and the place we'll ultimately take among the pantheon of great data companies. I'm tremendously excited about this vision and look forward to writing many more newsletters about all of it 😬

That aside, let's get down to brass tacks!

# From the Engineering desk

We're thrilled to share with you some exciting updates to our product! We've had our sleeves rolled up digging into your feedback and creating enhancements to provide you with an even better user experience.

- **API /v1/addresses/search zip code ext bug:** We’ve fixed a pesky bug tied to zip codes. If you have used the ext in the free-form search you didn’t get the expected results. Glitch fixed ✅
- **Date-Related Additions:** We've got you covered when tracking timelines. We've defined `start_date` and `end_date` based on permit dates, additionally, you now have the `total_duration` as the difference between these dates.
- **Primary Contact Info:** Keeping you connected! We have added primary phone and primary email fields to the contractors' dataset ensuring you have the best contact information on hand. No more long arrays!
- **Improved Identification Features:** We've made some adjustments in business and individual names for clearer identification - no more puzzling over who's who!
- **Deduplication Fixes:** To ensure the integrity of your data, we've implemented a fix to avoid duplicate entries.

We are committed to creating a catering platform that serves your construction data needs in the most efficient way possible.

# Things to do with permits: choose a retail location

Let me just say this first, because I had another idea for this part of the newsletter.

I have a heat pump water heater. For months I've been getting error alerts via its app on my phone. Compressor shutdown blah blah; I've been ignoring it because the hot water still works.

*How will I find a good contractor?*  Ugh, I don't want to deal with this right now.

... 🙄 ...

Finally, last night I used Shovels to look up contractors who recently worked on heat pump water heaters in my zip code. I emailed three using the contact info we provide. One of them replied immediately. Michael is coming to my house tomorrow afternoon to fix it.

I just thought that was cool.

----------------------------------------------------------------

Now let's talk site selection!

We're still stoked about our partnership with Esri. They opened up a bunch of doors into new business relationships and use cases for permit data. The one that keeps coming up is site selection.

Picture this: you're responsible for choosing the next ten locations for Chic-fil-A in Texas. How do you decide? You can use demographic data, plot competitors' locations, and map new home developments. All of that is helpful, but it's also pretty obvious.

What's not obvious? Looking where valued-add home renovations are trending. This signal shows which neighborhoods are investing locally, have disposable income, and likely to venture into downtown and try a new store or restaurant.

We're coining a new term for this:  **Neighborhood Vitality Index**, or NVI ("envy"). By rolling value-add renovation permits into points of interest, parcels, and census tracts, we can help companies map their next site locations.

Want to see for yourself?  [Here's our Esri map](https://shovels.maps.arcgis.com/home/item.html?id=bcaed6407a4c47449ccc0769d9543c17)  of Dallas County!

![Map of Dallas County showing the Neighborhood Vitality Index visualization in ESRI's mapping software]({static}/images/esri-nvi-map.jpg)