Title: March 2025 Newsletter
Subtitle: Join our energy hackathon, explore new features, and discover the power of parcel-based permit analysis
Date: 2025-03-10
Modified: 2025-03-10
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Our March newsletter highlights exciting opportunities: join our SF Climate Week Energy API Hackathon, connect with sales hackers on our growing Discord, and explore recent Shovels Online and API updates including website search filters, improved sorting, and expanded contractor data fields. Plus, learn how mapping permits to parcels can provide deeper property insights.
image: /images/vegas.jpeg 


You know what we all need right now? A shorter newsletter. Quick and to the point. Punchy! That’s what we’re doing this month. 

- Check out our [SF Climate Week Energy API Hackathon](https://lu.ma/pwh9o2e8?tk=jYxRHS)!
- [Our Discord](https://discord.com/invite/Nypja3cKDx) has a new channel for all you Clay sales hackers
- A few cool Shovels Online and API updates and a preview of what’s coming
- We’re pushing parcels in our monthly “Things to do with permits” feature

*You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 4,700 subscribers!*

*Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends.*

*We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company).*

# ⚡️ Calling all energy geeks!

A zebra can’t change his stripes, and I’ve been picking up trash my whole life. 

It’s a habit I learned from my Republican grandpa. We’d hike, pick up trash, and listen to Rush Limbaugh while playing gin rummy for hours and hours. 

He’d support the notion of reliable and abundant energy. If that energy happens to be clean/green/renewable, all the better! So long as it’s reliable and abundant.

We’ve partnered up with the best energy API companies in the industry to co-host what’s becoming THE hackathon for SF Climate Week. Here’s who’s involved:

- [Bayou Energy](https://www.bayou.energy/): Easy access to energy utility data
- [Texture](https://www.texturehq.com/): API wrapper for building energy data
- [Palmetto](https://palmetto.com/business/energy-intelligence-api): Building energy modeling
- And us, [Shovels](https://docs.shovels.ai/docs/introduction): Permitted construction activity

Plus, we have two whip-smart VC co-hosts judging: [Stepchange](https://www.stepchange.vc/) and [Virta Ventures](https://www.virtaventures.co/). 

The presentations and awards will be in San Francisco on Tuesday morning, April 22 and the AWS GenAI Loft will be available for in-person hackathon-ing but you can also participate virtually!

It’s [free to sign up](https://lu.ma/pwh9o2e8?tk=jYxRHS)! 

# 🤑 Calling all sales hackers!

I’m seeing more clever marketing and sales people diving into sales hacking. The AI toolkit makes it easy, and we’re here for it. 

We want to build a community specifically for property, construction, and building trades sales hackers. Since we already have [a Shovels Discord server](https://discord.com/invite/Nypja3cKDx) (which has also been sorta blowing up recently) we created a new channel, #sales-hackers, on it.

I will be nudging our Clay and Shovels API friends over there. The purpose is to share clever ways to use Clay, OpenAI, Shovels, Apollo, and other data providers to automate outreach in the property and construction industries. 

I hope you’ll [join us](https://discord.com/invite/Nypja3cKDx)! 

# 👩🏻‍💻 Recent tech updates

We moved the ball forward on some big projects. That was the story of the last 30 days. Here are a few smaller things that we also released:

## Shovels Online

### Search by contractor website

This was already available in the API but we just added it to Shovels Online. Now you can filter for contractors and permits by their website domain. One of our big projects this month was to improve the fill rate. You’ll see those results in just a couple more weeks! 

### Persisting your last search

Now when you start a new session, Shovels Online will automatically bring you back to the last geography you searched. It’s the little things, right?

### And more

The Shovels Revenue Team met in Las Vegas (that’s us, below) to hammer out the rest of our  product roadmap. The main theme was to make it easier for you to get *immediate value* out of Shovels data. 

For example, we’ll bring all this new contractor data(see below) into the app in the next couple of weeks! 

![Revenue Team]({static}/images/vegas.jpeg)

## Shovels API

### 🎉 Default sorting by start_date

Yes, it’s about time. We fixed a bug that was preventing us from doing this right. Now all permits are sorted by start_date as default, so the most recent permits and contractors will *always* be on top. 

This change will automatically flow into Shovels Online too. In fact, the API is deploying as I write this! 

### A bunch of new contractor fields

These weren’t included in the contractor API response before. Now they are! 

- license_inact_date: When the license went inactive
- license_act_date: When the license became active
- review_count: The number of Google business account reviews
- rating: The 1-5 star rating on their Google business account
- dba: Their “doing business as,” if available
- sic: The company SIC code
- naics: The company NAICS code
- linkedin_url: Their LinkedIn company URL
- revenue: Revenue range as provided on social media
- employee_count: Employee count as provided on social media
- primary_industry: Their self-reported industry as provided on social media
- first_seen_date: When Shovels first saw them

### Filter employees by department

Only care about HR, finance, or sales? Now you can filter those employees by their departments so you only get the contractor roles that you care about most. It’ll be just a few days until we get this into Shovels Online. 

# 🗺️ Things to do with permits: resolve to parcels

Two days ago I was in Palm Springs for the Esri Partner Conference. A week before that, Las Vegas with the team. A few days before that, Las Vegas for the International Builders’ Show. 

The common thing: parcels. 

It’s much easier to present 170M building permits on a map when they’re rolled up by parcel rather than as individual points. The parcel count drops to the 30M range. And then on parcels we can find out things like:

- Total number of permits
- Total value of permits
- Average time between permits
- Has had a roofing permit or not
- Has had a solar permit or not

The list goes on… and this, of course, can say a lot about the residential home or commercial property and the residents or owner of that property. 

Since we’re keeping this newsletter short, I’ll stop here. If you think this data can provide valuable insights for your business (you should all be raising your hands) please reach out! We (and [Regrid](https://www.regrid.com)) are waiting to help. 

Cheers!