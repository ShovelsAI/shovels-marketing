Title: How to use the Shovels app
Subtitle: The definitive guide to getting started with the Shovels app
Date: 2024-02-12
Modified: 2023-02-12
Category: Customer Success
Tags: app, launch
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels app, a web application that provides access to building permit and contractor data, has been launched. The app, built using Google's Flutter technology, allows users to find and profile addresses, permits, and contractors. The application was developed in response to a market need for a user-friendly platform that doesn't require API knowledge. Future updates will include Android and iOS versions of the app, improved geocoding, and additional search and filter options. The app is priced at $499/month per account.
Image: /images/boulder-commercial.png


We are very excited to announce the launch of V1 of [the Shovels app](https://app.shovels.ai). This is a web application you can access on any desktop or mobile browser. Now you can access our building permit and contractor data without an API standing in the way. 

I’m going to share the history of how we got here and why building software is a pretty big deal for us. Then I’ll share what we’re releasing today and, importantly, what’s in store for the future. 

## How the Shovels API became an app

We like data. It’s in our DNA. The founders, me and Luka, met over mobile data. We were both building separate companies, attacking the mobile data market from different angles. We combined the companies so we could offer a more complete picture of the mobile data environment.

Our first hire, Petra, is a data engineer. She brought some big company experience with her, largely from the firmographic (company) data market. She also liked the challenge of making real-world data more accessible and useful. 

Ultimately, that’s what we’re doing here. We’re making government data more accessible and useful. It’s a big challenge. 

When we started really putting the building blocks for Shovels in place, digging and framing the foundation (to use an apropos building analogy), we understood that there would three core objects in the data structure: addresses, permits, and contractors.

It made sense that they would be related. Permits have addresses. Contractors have permits. Therefore, contractors would also have addresses. We knew we could tie them all together in a relational database and help software developers build some really compelling applications.

And they did, and they are. We’re really excited to be helping a new crop of property, real estate, climate, and construction entrepreneurs build cool new applications.

Still, we kept hearing from our own sales and marketing outreach that there was a product missing. They wanted to be able to browse the permits and contractors in our system. They wanted to be able to download this data without needing to contact us, wait for a reply, and then negotiate a price on a custom report.

The answer became clear. We needed to build our own software product. 

## The need for a building data application

We are not the first to aggregate and sell building permit data. If you look for it, you can find a half dozen other companies that have been doing this long before we started thinking about doing it in October 2022. 

However, those incumbents are mostly stodgy old data services. They barely have an API and prefer to sell annual licenses to heavy datasets that only data engineers can parse and access. It’s not a startup-friendly approach, and when we looked these guys up, we weren’t impressed. 

We knew that the first step for Shovels would be to launch an API. We did that for permits in August 2023, and we followed up a couple of months later with our contractor API. 

But like I said, it wasn’t enough. An API is not user-friendly. Most people in the building trades don’t know what it is. A lot of you reading this may not be familiar with the concept either. We were limited in who we could sell to, and the market continued to be underserved. 

By late 2023, we had the bandwidth to build our own software application using our own public API. We started building using a relatively new technology called Flutter. I’ll explain why this is important.

Flutter is an open-source software development kit released by Google in 2015. Originally intended to be cross-platform, allowing developers to release both Android and iOS applications from a single codebase, it expanded in 2019 to also support web applications. Flutter 3 was released in March 2022. This is what we’re on today, and it will allow us to also release MacOS and Linux applications, in addition to web, Android, and iOS apps.

I think Flutter and technologies like it are awesome and I’m glad to be among the first companies to fully embrace it. We know that many people in the building trades live on their smartphones. They’re always on the move, so a mobile application makes sense. Flutter allows us to support our web application and mobile applications from a single codebase so we can develop and release faster than anyone else. 

We’re launching our web application today, but you can expect us to follow up with Android and iOS apps very soon! 

## Features of the Shovels app

We are launching with the ability to find and profile each of our three core objects: addresses, permits, and contractors. Let’s go through each one! 

### Address Permit Profiles

This is straight forward. Look up an address, get the permits! 

![Address profile page]({static}/images/5757-permits.png)

Here we see all the permits on 5757 Central Ave, Boulder CO, an office building outside of downtown Boulder. Yes, we cover commercial properties, too! 

*Quick note: The address lookup process still needs some TLC. You may find that we don’t return addresses on properties you know have permits. That’s likely a geocoding issue, and we’re working on it.*

We are developing profiles on properties and these will become even more useful and robust in the coming months. Soon, you’ll find the standard property details (lot size, stories, square feet, etc) as well as contact info for the occupants. Use this for marketing, analytics, and your own product enhancements! 

### Permit Database

One way to dig up this 5757 Central Ave property is by finding all commercial permits in the Boulder area. I searched for a downtown Boulder ZIP code and set our tag filter to “commercial” to see it in this list.

![Commercial permits in Boulder]({static}/images/boulder-commercial.png)

You can click on any of these addresses to see the same level of detail shown in the previous snapshot. 

![Permits zoomed in]({static}/images/boulder-commercial-1.png)

A few other notes on our Permit Database:

- **Search by keyword**: You can put any text you want in here and we’ll scan the descriptions of over 120M permits to find the ones that match.
- **Search by state or zip**: Right now you can only limit the geography by ZIP code and state. Soon, you’ll also be able to search by city, county, or the permit jurisdiction.
- **Filter on permit fees and job value**: If you want to further refine your search, you can set minimum thresholds of permit fees and job values. The permit fees are collected by the county and the job values are self-reported, usually by the contractor. Note that not every jurisdiction collects these values, but if they do, we’ll have them.
- **Download to a CSV file**: Each of our tables includes a download feature so you can take this data into your other software products and make magic happen.

### Contractor Directory

Our third feature is also suitable for personal use. Have you ever needed to find a contractor and wished you could just see who all of your neighbors used for that remodel, or cottage, or solar installation? The benefits of hiring someone who’s been in your neighborhood before are several:

- Most houses in a neighborhood were built around the same time, often by the same developer. Therefore, they have similar attics, crawl spaces, and wiring. It helps when a contractor knows what your house feels like before he shows up.
- Permitting can be challenging, so it’s best to hire a contractor who knows what to expect of your local building department. If they know him, they may treat his permit requests differently. These little things matter!
- Contractors who know your neighborhood are invested. They want to do a good job, because they want you to recommend them. It’s best to hire someone who wants to expand their business in your neighborhood.

Do you know what *won’t* tell you who works in your neighborhood? Yelp. Or Google. Or Nextdoor (unless you put up a post and ask.) The only reliable, consistent, accurate way to find which contractors work in your neighborhood is to use building permits. 

So that’s what we do. 

![Find building contractors by permit type]({static}/images/find-by-job.png)

Here I’m looking for every commercial contractor in the same Boulder ZIP code. How do we know a contractor is “commercial”? We know by their permits. This feature searches for commercial permits and then returns all of the contractors on those permits.

Makes sense, right? Seems like something like this should have been out there long ago, right? We agree.

## What’s coming out next?

It’s important to note that everything we’re doing here is available on [our public API](https://docs.shovels.ai/api-reference). We are building this app using the *same* endpoints that our customers can access. This software app is kind of like an API demo, too.

We’re already working on V2 of our API. The V2 will have a bunch of cool new stuff like:

- Searching for permits using lat / long coordinates. That way you can drag the map and we’ll automatically update the permit results!
- Searching by cities, counties, and jurisdictions. We know it’s frustrating to search by ZIP code. There are reasons why we did it that way to start, and the V2 will fix that!
- Seeing a jurisdiction dashboard. Wouldn’t it be great to see a dashboard of every permit under review, recently approved, or finalized in any jurisdiction in the country? We’re on it!
- Get property details with the permit history. We’re going to include tax assessor data in future address profiles.

That’s just a sneak preview! Before we can update our app, we have to update the API. It’s already under development.

## Does this cost anything, by the way?

Yes! We are going to charge $499/mo per account for access to all of this amazing data. You’ll get a generous trial period, though, and all of our constant updates. 

When we release the V2, price will probably go up, but we’ll won’t raise prices on our early customers. 

Check it out! [https://app.shovels.ai](https://app.shovels.ai)