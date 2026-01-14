Title: January 2026 Newsletter
Subtitle: Shovels is growing up: ReZone acquisition, Charlie launch, and critical Shovels Online improvements
Date: 2026-1-14
Modified: 2026-1-14
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels kicks off 2026 with major moves: acquiring ReZone for government decisions data, launching Charlie (our AI research agent), and delivering critical Shovels Online improvements including contractor-merged exports, negative queries, and upcoming Addresses and Decisions tabs. Plus, a preview of entity extraction from permit descriptions.
Image: /images/blog_images/2026-01-Newsletter.png


Yea, happy new year, yadda yadda yadda. I'm just glad we're all back to work 🧑‍💻

In case you missed it, Shovels made a couple of big moves recently:

1. We [acquired ReZone](https://www.shovels.ai/blog/shovels-acquires-rezone/), a world-class government decisions database, and improved the technology to scale it out nationwide! 
2. We hired an industry veteran to run sales. [Matt Drobick](https://www.linkedin.com/in/matthew-drobick-25a8b06/) comes with twenty years of experience selling property data and most recently lead sales at ATTOM.

So today, let's add a third.

1. We launched [Charlie](https://charlie.shovels.ai/), our sweet new AI research agent. 

In this newsletter I get to tell you what this all means for the rest of 2026! 

# Shovels is growing up

For the first time since we started, I'm feeling like I have all-star players in every position. I'm not used to this. Sometimes I don't know what to do! My old daily playbook no longer works, so I get to be… well… strategic! 

You know, look at next month instead of what's right in front of me.

This is what a mature CEO does, or so I hear. As Bezos says, "There are no accidents," (or some variation thereof) because every bit of success Amazon ever announced was preordained three quarters earlier. 

That's how I want 2026 to feel. We're making big moves now so the rest of the year's success is obvious, preordained, baked in. 

And you get the benefits! Here's how this works. 

## Our first acquisition: ReZone

I met [Daniel](https://www.linkedin.com/in/daniel-helller/), CEO of [ReZone](https://www.re-zone.ai/), through LinkedIn. Nice guy, scrappy, reminded me a bit of myself 😊

Shovels has always been curious about meetings, transcripts, and decisions. It's the most obviously valuable city government data after permits. In fact, many of our customers find that building permits are "too late." By the time the permit gets filed, its usefulness for them has evaporated. 

Getting into city transcripts has always felt attainable. "Like a hot knife cutting through butter," is what I told anyone who'll listen, when describing the difference between getting permits and getting transcripts. Every government publishes their agendas, minutes, and even transcripts (which usually wind up on YouTube, transcribed by Google). No crazy scraping technology required. 

None of this is secret. Unlike permits, spend a few minutes googling for city council transcripts and you'll figure this one out. 

If access is so easy, what's so hard about this? As we learned from talking to Daniel, teasing out the value of the decisions from the agendas and the transcripts is the real science. Battle-testing your prompts, getting feedback from your customers, all of that has great strategic value. 

We could learn it, sure, but that would take us into the back half of this year. Why do that when the opportunity presents itself to get it now, in January? That's what ReZone offers, and we eagerly accepted. 

Now we just have to connect the dots: the common key between everything is our set of geo_ids. We're appending them to all of the existing and new ReZone decisions. We have about 20,000 to start, and will expand to 60,000 decisions shortly.

Expect to see decisions offered via Charlie, API, and Shovels Online very soon! 

## Our AI research agent, Charlie

Charlie is available to all! Free plan users get a sneak peak, and paid plan users get a whole lot more tokens. 

And you already have an account! Just log in or sign up at [https://charlie.shovels.ai](https://charlie.shovels.ai) using your Shovels Online credentials. Exact same logins for Shovels Online and Charlie!  

Think of Charlie as your data analyst. Charlie will be great for doing top-to-bottom drill-downs. Start at the national level, and dig dig dig for geographies of interest. Once you're honed in, you might want to switch back over to Shovels Online to get your detail lists and exports. 

Charlie can point you to specific permits and contractors in Shovels Online, but she's really there to have a conversation about our data and tell you what's going on, to pique your interest and help you get the most of Shovels Online. 

Perhaps we should build an even tighter product coupling between Charlie and Shovels Online someday? 

[You May Be Right](https://www.youtube.com/watch?v=Jo9t5XK0FhA), as Billy Joel says. 

I'll just leave it at that. 

## Critical Shovels Online improvements

Speaking of Shovels Online, this product has been in dire need of some upgrades, and we've already started to deliver them. No long wind-up narrative here, folks. Let's just get to the product goodies. 

### The permits export now includes contractors!

No more VLOOKUP lessons! The permits download now comes pre-merged with contractors so you don't have to join them anymore. 

It's amazing how much better this report looks now. Previously, we left you with a less-than-useful `contractor_id` field at the end of the file. "What's this?" you would ask. "How do I use it?" Well… I'd mutter, you sorta need to… and nobody was happy.  

Now everybody is happy!

### We now support negative queries

Want to find contractors that did NOT do an ELECTRICAL permit in the last 5 years? Now you can! 

And when we release our address listings, you'll be able to find homes that have had NO ROOFING PERMITS in the last 15 years entirely through Shovels Online. No need to hit us up on the support channels for a custom count.  

We're very excited about this. Although we don't mind doing custom reports, we understand it doesn't scale well and it's just more friction for everybody. We'd much rather empower you to do it yourself. 

### Two more tabs: Addresses and Decisions (coming soon!)

Coming soon: resolve to addresses, and search for decisions. 

The address resolution is obvious and I wish we already had it. Address resolution means setting your filters (e.g. residential homes, last 2 years, NO solar permits) and instead of getting a list of contractors or permits, you'll get a list of addresses. These addresses will be residential homes with NO SOLAR permits in the last 2 years. 

It's close to a permit object, but it'll act differently because a permit inherently is a snapshot in time. An address can have many permits (just like a contractor can have many permits) so our filters can look at the set of permits and filter accordingly. 

You'll see. It's gonna be rad. 

And the Decisions database will be basic but allow all paying Shovels Online users to access the FULL ReZone database. Because we like you. 

# Things to do with permits: mine the descriptions

Next time we'll be able to do something with permits and decisions. This time, I'll show you something Petra has been working on. It's super cool. 

Many of you have asked, and many times I have answered, that our entity extraction project is "moving along." We have some progress to show now. We're doing two things to the description field: 

1. Extracting entities
2. Making them human-readable

Here's a real permit description:

```json
Sfd: 3000 sf w/483 gar
```

And what we're able to do with it:

```json
description_derived = Build a single-family home with a garage.  
tag = new_construction 
building_type = single_family 
square footage = 3000.0  
```

Imagine what this means for solar and roofing permits! And siding, electrical panel and meter permits too! There's so much rich data ripe for the picking, and finally we have the technology to make this a relatively straightforward pipeline task. 

Extractions will likely be a related table (many per permit), and derived description will be a new field available on the permits table.

As always, our goal each month is to show that nobody is thinking harder and working harder on public construction data. 

And the good news is we keep enjoying it. 

See you next month!
