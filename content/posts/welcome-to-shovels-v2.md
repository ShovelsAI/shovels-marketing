Title: Welcome to Shovels V2
Subtitle: An introduction to our upgraded API and Shovels Online platforms
Date: 2024-10-22
Modified: 2024-10-22
Category: Company
Tags: new release, api, web app
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: Shovels is launching their upgraded API and web app product. It has increased functionality, improved UX, and brand new features. It releases October 24th for general availability. 
Image: /images/welcome-to-shovels-v2-hero.jpg

# Welcome to Shovels V2

Launch week continues today with an introduction to the functionality of our V2, including both the Shovels **API V2.0** and **Shovels Online** (our new-and-improved web app). We've been hard at work for the past 6 months upgrading our infrastructure, increasing data fidelity and accuracy, and designing new endpoints and exploration opportunities via Shovels Online. Let's dig in.

## Introduction

First, a bit of backstory. There are three levels to the Shovels platform - raw data feed, API, and web application - and each one has it's own strengths and weaknesses. To start, the raw data was the highest priority, as it was the foundation of all the layers on top of it. As engineering resources freed up and joined the team, we were able to dedicate more time to higher layers of the API and web app. The web app, as the shallowest layer, was both easier and more difficult to develop. Exploration was the key functionality, with integrated GIS functionality to search for permits via map view, as well as other filters and profiling which makes the permit data search a little more user-friendly for non-developer types. 

But the time for (near) parity has arrived, so we're breaking out all the new bells and whistles we've been cooking up to bring the API and Shovels Online versions up to speed with the data from the raw feed. We're not done though, not by a long shot. We have lofty aspirations for the Shovels platform, and 2.0 is just the next step. 

## Upgrades from V1.0

Let's talk specifically about the API now. V1.0 had a few key objects, namely `address`, `contractor`, and `permit`. These all had interconnected metadata and parameters, some of which are obvious like `zip_code`, where others are more nuanced like `contractors/name` which required some cleaning on our end prior to delivery. 

In V2.0, we've done a huge overhaul to the former `address` part, turning into the bright and shiny `geo_id`. Instead of complicated concatenations of `street` + `house_number` + `city`, etc that made up an individual `address` objects, now we have distinct ids assigned to every parcel, every zip code, every jurisdiction, every city, and every county. This makes our infrastructure way cleaner, faster, and simpler to connect our data to the literal earth underfoot.

Beyond the `geo_id` refactoring, we've more than quintupled the search and filtering parameters for our endpoints. Now, you can specify things like `min_lot_size` or `c_min_total_permits_count`, which can help you (or your sales teams) narrow your results to properties of a minimum size, or contractors with a minimum number of permits under their belt. This is just two such parameters, there are many more.

Also, with our brand new `geo_id` schema, we can expand our search capabilities to a broader capacity, now including `counties` and `jurisdictions`. While this change is helpful (and many of you specifically asked for it), the real kicker with these is how it further unlocks the capabilities of our web application, **Shovels Online**.

## Shovels Online

![Marketing image of the new Shovels Online web application](/images/shovels-online.png)

Our web application is built on top of our API, so most of the new features and upgrades have been inherited up a layer to enhance our live exploration and codeless offering. Here are a few of the highlights:

* **Actual Onboarding**: First-time users will now be greeted with an actual onboarding wizard to help you establish your preferences and the type(s) of data you're looking for. 

* **Enhanced Filtering**: New API endpoints (as described above) means better filtering options in the web app. Now available, you can search and refine by geographies, financial filters, building specs, permit details, and contractor profiles. And once you're there, you'll see a normal header of your selected filters, to make it easy to adjust as you need. And best of all, you can save your configured filters for repeat usage! 

* **Improved Results Downloads**: Now that we've implemented proper pagination, it's easier for us to configure a key feature that's been requested from the very beginning: downloading the results of a filter or search. For this initial release, we're maxing out downloads for a given search at 1000, but you can multi-select or unselect the ones you don't want prior to download. 

* **Detailed Drill-Downs**: The drill-down data has been one of the unique features specific to our web app, and so it's deserved special attention too. Now, when looking into a permit's details, we've put all the data we have at your fingertips. Sometimes they'll be rendered graphically, like permit status progress bars and historical timelines, sometimes they'll be hyperlinks to further details at all the geographical levels described in the `geo_id` section above. We've interconnected the data as never before, and now you're free to explore that to your heart's content. 

* **Saved Profiles**: This one is my personal favorite addition - being able to save the filters and results from a previous session for repeated use. If there are a few specific properties or contractors you're paying attention to, you can essentially bookmark them. If there's a detailed search query that you spent hours perfecting the parameters and filters on that you'll need to re-use every month, then you can just save it and it'll be there, waiting for you. 

* **Elegant UI**: Technical improvements aside, we've come along way to bring our UX/UI up to spec. We're users of our own platform every day, so we gave it the care and attention necessary to make it as smooth of an experience as possible. It's intuitive, interactive, and hopefully quicker to learn. The **Shovels Online** platform is always improving, so please do not hesitate to let us know if we miss the mark or omitted something obvious and glaring. 

The team is extremely proud of the new web app, and we are hoping to unlock your exploratory potential to see US permit data in a brand new way.

## What's Next?

We can promise that the moment V2.0 launches, we'll already be thinking towards to V2.1 and even V3.0. In fact, the entire Shovels team is meeting in person for our semi-annual summit this week for the launch to brainstorm, among other things, what we do next. 

However, in the shorter term, we're completely open for feedback. We did our best, but it's impossible to plan for every use case, and we're constantly surprised at how clever your search queries and leverage strategies are. They go way beyond anything we thought of.

Please check out the new **Shovels Online** when it launches *this* Thursday, Oct 24th. Walk through the system, double check the use cases you had in mind, and [report back to us](mailto:support@shovels.ai) how it goes. We've got a big roadmap, but we're happy to add more items to make it that much smoother for you and your team. 

## That's all (for today)!

Launch week continues, and we'll be releasing more info - sneak peaks at the UI, what will happen to existing web app customers, and more - very soon. Thank you for your continued support and hype, it means the world to us. 

Happy Digging!
