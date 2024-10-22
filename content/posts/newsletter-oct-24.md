Title: October 2024 Newsletter
Subtitle: 150M permits at your fingertips 
Date: 2024-10-9
Modified: 2024-10-9
Category: Company
Tags: company
Authors: Ryan Buckley
Summary: We're gearing up to launch Shovels Online at the end of the month, offering an easier way to access and download building permit data. A launch party is scheduled for October 24 in San Francisco!
Image: /images/domains.png


# 🚀 It's launch month here at Shovels! 🚀

Shovels Online is under *heavy* development now. The hammers are swinging. The chainsaws are revving. Data dust is flying everywhere.

We're slated to launch at the end of the month! We want to celebrate and you're invited to the party.

More below! 

* Come to [our launch party](https://lu.ma/bsst1m5f) in downtown SF at 5pm on Oct 24! We can only really let 50 people into the penthouse suite at The Avery, so please check your calendars [and RSVP](https://lu.ma/bsst1m5f)!
* Here's another big thing: **contractor website domains**. Inspired by [Jordan's crazy hackathon](https://www.youtube.com/watch?v=VF2t9qbBUDo) last month, we went and got this done. Now it's 10X easier to add more contact info for each contractor you find in Shovels.
* The ad stuff is pretty cool too. We're about to go online with another data partner, putting more building permit-based homeowner segments out there for targeting. Holler if you want info on that!
* We had our fastest monthly batch process ever. Massive kudos to the Shovels Engineering squad (still just a team of 2) for processing 150 million permits in just 24 hours. 

# Quick reminder

You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 3,000 subscribers! 

Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends. 

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company). 

# One last thing about Shovels Online before it actually launches

I just want to say... this new software release is a big deal for us. I say this for a few reasons.

We didn't start Shovels to be a small company. Been there, done that. Shovels is meant to be a big company, and to be a big company, we need to have multiple interfaces. I firmly believe this. We're a data company at the core, but data isn't useful if you can't *get* to it, and not everybody wants an API key or a Snowflake table share.

Some of you (many, I hear) just want something to *click*. That's it. Click, click, download. 

We're nice people and we want to help. So we're giving you that. (But not for free, silly. You still have to pay for it.)

Our current software product leaves much to be desired but it gave us conviction that we should hire some professionals to make a truly great software product. That's what you can expect from the new Shovels Online.

You'll see in a couple of weeks! You won't believe you ever logged into the old one. 

And here's where it gets interesting: I also believe that in the next year or so, a majority of our revenue will come from Shovels Online.

We're making decent money now, but most of it comes from the big data deals. We'll still do plenty of those, but I believe there's a huge demand for *click, click, download* type of access to not only get the permit data but also the *insights* we're packing into it.

This does not exist in the market today. 

We get feedback from API and table share customers that we can percolate up to the software layer. That's the other benefit of having multiple interfaces: lots of customer feedback, coming from different perspectives. When we merge them together, magic happens.

By building software on our own data, we see our data and our API in a different way. It's easy to ignore the rough edges when we're not building anything on top of it. This "dogfooding" helps both of us and will continue to keep Shovels the best product for fast and easy permit intelligence. 

So that's why this is a big deal. New software gets released all the time (hello, [Product Hunt](https://www.producthunt.com/)!) but these new products don't always define a market category.

That's what we're trying to do here.

We'll send another email out when the new and improved Shovels Online is LIVE! 

# From the Engineering desk: backend fixes and contractor website domains!

The first V2 API endpoints are live. Many of you have been asking for early access and we've been telling you we'll offer it -- we'll honor that, but not yet ([not yet](https://www.youtube.com/watch?v=FRgp2v9Km9M).)

But if you *really* want it *now*, [fill out this form](https://forms.gle/NkEq3WBjWwHfaeHh8) and tell us what you're working on!

# 🤓 Tech Stuff

* **Infrastructure & Bug Fixes**
  * New scripts, new data libraries, a bunch of little things add up to our best, smoothest, most amazing data run in the 14 months since we started doing this. 
  * We also added some new monitoring features to the API so we debug any issues with greater speed and accuracy.
* **Address Consolidation & Static IDs**
  * We designed a new format for static address IDs that map across various geo scopes, such as individual addresses, cities, and counties, making it easier to reference and manage permits.
  * This goes live at the end of the month! 

# 🔎 Contractor Website Domains

I've been talking about this for months. SORRY. 

Starting already, we're able to export custom reports with contractor domains appended!

I've delivered a few reports to roaring applause, and I've used them myself to gather up more contractor contacts using Clay, but you can use any B2B database for this.

They key is to have the domain, which now you do. We'll push this out to the API once we get the other stuff shored up. 

Can't wait to see what you all build with this! 

# Things to do with permits: prospect into contractors

Like all things in modern go-to-market, it starts in [Clay](https://www.clay.com/).

Here I've uploaded the Shovels output of a bunch of non-residential contractors. According to our permit data, these guys have worked on at least one commercial property.

![1M domains on contractors]({static}/images/domains.png)

See that CONTRACTORS\_WEBSITE field? That's new.

Since we have the domains (huzzah!) we can easily use Prospeo's integration with Clay to look up emails from these domains. They'll return up to 50 emails at a time! All for about a nickel.

To do this, you just add the find email addresses enrichment and choose the CONTRACTORS\_WEBSITE column. Clay makes this pretty intuititive.

![Use Shovels with Clay]({static}/images/clay.png)

You can now use Clay to further enhance with the name, title, and LinkedIn profile, or append other Shovels data for additional segmentation.

If you watched our hackathon with Blueprint GTM, you saw how they used Clay, Shovels API, and Claude or ChatGPT to craft credible, unique messages to each contact. It was super fun to watch and it shows how creative sales and marketing folks can turn our data into prospecting gold.

We're grateful and excited to be on this journey with you. We're only getting started!