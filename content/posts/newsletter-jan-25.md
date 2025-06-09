Title: January 2025 Newsletter
Subtitle: A new year, a new website, and a new way to use Shovels.ai
Date: 2025-1-15
Modified: 2025-1-15
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels.ai kicks off 2025 with a smooth January release adding 9 new jurisdictions, improved documentation, new profile pages, and employee data. Looking ahead, the company plans major enhancements to permit data coverage and contractor insights, including job value modeling, retail associations, and revenue metrics.
image: /images/contractor-profile.png


I’m told that it’s mid-January and time for a greeting transition. So — I hope your year is off to a great start! 

Here’s what’s making our new year happy:

- January release was super smooth. 9 new jurisdictions. 162M total permits!
- I ❤️ me some good tech docs. Fortunately for us, our support extraordinaire Alex Brown has delivered. Check out his winter project: https://docs.shovels.ai
- The web app now has city, county, and jurisdiction profile pages (more on these below)
- Reminder: we show employees on contractor profiles now, and you can download them!
- My own winter project was a website rebuild. Happy new website: https://www.shovels.ai
- In the API we have a new `first_seen_date` contractor attribute so you can tell those freshman electricians about all the goods and services you offer. You’ll be able to filter for them soon!
- Also coming soon: address profiles! They’ll be like Carfax, but for addresses, and included in your web app and API subscriptions.
- All the above was staged by a stellar 2024. [Read our 2024 recap in the blog](https://www.shovels.ai/blog/2024-shovels-year-end-recap/)

---

You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 4,500 subscribers!

Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends.

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-_ahRe7B39PsnJ6dmdnVj6D6zmvBklI3407wxLC1yUPCPJRuRZuQlXhwFlDyP9nNZbXbu9D).

---

## A look ahead at 2025

I’ll sum up 2025 in two words: **permits** and **contractors**. Come to think of it, that’d sum up 2024, too. Hooray for consistency! 

Here’s what we’re look forward to:

### Permits

- **More job values**: we’re pretty far along on our permit job value model. The jurisdictions give us job value in only 25% of permits, so we’re modeling the other 75% with fancy statistics. By the end of this month we’ll have the nation’s most complete picture of construction costs.
- **More coverage**: we know there are gaps. We’re working with our partners to plug the holes, especially in the populated metro areas.
- **Less latency**: we also want to give you new permits and status changes as soon as they happen. We can’t do that with monthly updates. It’s a tricky problem but we’ll find a way to solve it!
- **Retail associations**: We’re associating commercial permits with the names of the retail businesses that operate there. You’ll be able to look up all the Starbucks permits in San Francisco and who worked those jobs, for example.
- **Jurisdiction lookup**: We now have a prototype that identifies the permit jurisdiction of ANY address in the US. Next, we’ll pre-compute the permit jurisdictions of all 155M addresses in our database.
- **Parcel associations**: We’ve been talking a lot with our friends at [Regrid](https://regrid.com/) and are excited to finally start working on permit-parcel associations. We’ll roll permit summaries onto tens of millions of their parcels and make it very easy to run additional geospatial analyses in ArcGIS and other Esri products.

### Contractors

- **Revenue metrics**: All those new job values roll up nicely onto our contractor profiles. When the job values are live, we’ll give you the most accurate estimates of contractor revenue by month, quarter, and year.
- **More domains and employees**: When it comes to B2B GTM AI (that’s “business-to-business go-to-market artificial intelligence”), website domains are the elixir of life. All the B2B companies use website domains to connect their databases. We’ve associated about 500,000 contractors with domains and employees and we’ll keep working on the rest.
- **Metrics and badges**: Break down contractors by property type, property category, or revenue tiers. We’ll make badges for contractors to signify which contractors do building electrification, are very active, appear dormant, or are willing to travel far from their HQ.

Our goal is to be the absolute very best at all of this. 

## Tech Updates

### New Documentation Hub

This one is a long time coming, but we've now released our centralized documentation hub. Check it out here at [docs.shovels.ai](http://docs.shovels.ai/).

We'll use this to host our **API Reference**, **Tutorials**, **Troubleshooting Guides**,  **Release Notes**, and much more to come!

### Updated Shovels Online

[Shovels Online](http://app.shovels.ai/) will always be a work in progress, but we've made significant strides over the holidays to bring it closer to our end vision.

Specifically, we've connected the various profiles across the entire platform, so you'll be able to navigate between cities, counties, and jurisdictions from either **Contractor Profiles** or **Permit Records**.

Beyond that, we've also included a new downloadable Employee table on **Contractor Profiles**, so you can now dig deeper into the personnel at the individual companies you're researching. This is *already* helping our customers target their outreach more effectively!

### New `/employees` and `/metrics` API endpoints

Adding to our prior month's platform improvement of including detailed employee data into our contractors table, we're now bringing that to our API.

The [`/v2/contractors/{id}/employees`](https://docs.shovels.ai/api-reference/contractors/list-contractor-employees) endpoint will allow you to retrieve an array of listed employees, including a wide range of demographic information.

The [`/v2/addresses/{id}/metrics`](https://docs.shovels.ai/api-reference/addresses/get-address-metrics) endpoint will return a detailed monthly digest of construction data for a given address, which will include breakdowns of permit counts across various states, as well as associated contractors, plus extra derived metrics like `avg_construction_duration` or `avg_inspection_pass_rate` to name a few. 

## Things to do with permits: drop pins onto shapefiles

A shapefile is a GIS data format that stores geographic features like points, lines, and polygons along with their attributes. It’s used in popular softwares like Esri ArcGIS for cool geospatial analyses.

We care about shapefiles because they define the boundaries of cities, counties and parcels. If we wanted to associate permits with cities or incorporated territories, we have to know whether the permit address actually sits inside the city boundary. 

This is easier said than done! The process goes a bit like this:

- Get tens of millions of addresses from building permit databases
- Run them through an API like Google Maps (good-bye money 💸) or find a better way (like we did) to get the latitude and longitude of each address
- Now find a shapefile for every city, county, and parcel in the country (or ask a friend)
- And THEN write a cool Python script to see if your permit coordinates land inside any of those shapefiles

Phew 😮‍💨 

But if you can pull that off… nice! You can now associate your permits with a TON of other geo-databases from public and private sources. 

Or just sit tight and let us do it for you.

I feel like we’re still in the first inning here and have a long game ahead of us, but we’re at the plate and swinging hard. 

Happy new year! 🫢