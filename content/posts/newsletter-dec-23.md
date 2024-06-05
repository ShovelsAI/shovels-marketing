Title: December 2023 Newsletter
Subtitle: Cool new permit lookup features in the Shovels app and why we're going long on climate
Date: 2023-12-5
Modified: 2023-12-5
Category: Company
Tags: company
Authors: Ryan Buckley
Summary: We added some new tools to the Shovels web app. We also now have a nationwide contractor directory, so anybody can look up contractors based on their service area, not just their work address. And we're doing a lot of data enrichment! 
Image: /images/permits-screenshot.jpg


You can now look up permits by type and ZIP code or by postal address using [the Shovels app](https://beta.shovels.ai).

Our goal here is not to build the killer building permit SaaS app (that may come later). It's just to help you understand what's sitting in our database and give you some ideas about what to do with this data.

Since permits are tied to contractors, contractor profiles will start to appear here as well 😉

![Shovels permit directory]({static}/images/permits-screenshot.jpg)

Things to do with permits: see where contractors work
=====================================================

When you go to Yelp, or Thumbtack, or Porch, or Angi, or any of those guys to find an electrician "near me," you'll get a list of electricians whose business address is near you.

But that's not really how electricians and other trades work. They travel! They don't stick to the same ZIP code as their business address. 

Yelp et al, therefore, won't recommend the best electrician working in your neighborhood. Those guys have no clue who _actually_ _works_ in your neighborhood.

**But we do!**

Here's the [API endpoint](https://shovels.redoc.ly/#operation/Contractors/operation/get_contractors_by_activity_zipcode_v1_contractors_activity_zip_get) to find the most active heat pump (etc, etc) contractor that works in your ZIP code. We'll add a basic interface to the Shovels app to show you this too. Or if you want a sample CSV report, just reply. 

Heat pumps galore ☀️
====================

It's undeniable that the world is getting hotter. We can debate how much humanity is at fault, but the increase in worldwide average temperature and all the trouble that causes is irrefutable.

Regardless of whodunnit, there's a new crop of well-funded "climate tech" startups trying to prevent the impacts from getting worse. Shovels is here to help. 

The winds are shifting towards electric home appliances, and with that comes a tremendous business opportunity. Our timing here is perfect: the Inflation Reduction Act that passed in 2022 is going to hit the markets in 2024. That means a TON of building electrification permits (heat pumps, EV chargers, batteries, and solar) and installations. 

And it also means a lot of innovation and technology which will be visible in data that Shovels is uniquely capable of collecting. We intend to be the de facto leader in building electrification data going into next year. 

So that's why I'm excited. Here's a worthwhile [New York Times article](https://www.nytimes.com/2023/11/09/business/energy-environment/heat-pumps-biden-tax-credits-rebates.html?unlocked_article_code=1.90w.qsq1.QP6pmedG0WQU&smid=url-share) all about it. 

Now what?
=========

So many things! I'll mention a few highlights.

**Better contact info**

We're partnering with a B2B and B2C data company to fill in homeowner and contractor contact details where they're missing on permits. We're also appending homeowner data fields like job title and seniority level, marital status, and much more. On the contractor side, we're improving phone and email coverage, as well as business websites.

The result: some crazy awesome filtering for lead generation.

**Online advertising**

What if you could run online ads to everyone with a solar panel installation? Or an ADU? Or any kind of remodel in the last 5 years? We're partnering with two platforms that can take our permit data online and build lookalike audiences to expand your reach. Let me know if you're interested!  

**Tax assessor data**

We think it'd be pretty great to have all the tax assessor data (home value, lot size, number of stories, etc) alongside the building permit and building contractor data.  

Combined with the better contact info, I believe this will put Shovels second to none in the proptech lead gen category 💯

I'm very curious what you think of the above. What should we tackle first?