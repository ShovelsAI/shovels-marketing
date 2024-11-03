Title: June 2024 Newsletter
Subtitle: This month we started rebuilding a few things. The results are exciting!
Date: 2024-6-18
Modified: 2024-6-18
Category: Company
Tags: company
Authors: Ryan Buckley
Summary: Shovels has launched a rebuilt web application and updated API documentation, adding city search to both the permit and contractor search APIs, along with license classification filtering. They re-classified every building permit in Texas, added 2 million permits, 1.3 million geo-tagged addresses, and expanded to 19 new jurisdictions. The nationwide contractor license data project is integrating state license files and building electrification rebate program affiliations. A website rewrite is underway, enhancing user experience. The new software build includes enhanced CSV downloads and city-based search functionalities.
Image: /images/heat-pumps-in-ny.png


## Shovels June 2024 Newsletter
<br>
This month we started rebuilding a few things. The results are exciting!

*   We rebuilt and re-released our web application. You can check it out now at [https://app.shovels.ai](https://app.shovels.ai). It just kinda needed to happen.
*   We rebuilt our [API docs](https://shovels.redoc.ly/) too. 
*   Speaking of API, we added city to the [permit search API](https://shovels.redoc.ly/#operation/search_permits_description_v1_permits_search_get) and the [contractor search API](https://shovels.redoc.ly/#operation/get_contractors_by_activity_city_v1_contractors_activity_city_get) (and the [new app](https://app.shovels.ai) and our [ShovelsGPT](https://chatgpt.com/g/g-zXFhOF8SP-shovels-ai)). 
*   You can now also search contractors by their license classification  ⚡️
*   We re-classified every building permit in Texas and the results are amazing. More details and the math behind this is below. The rest of the country is next.
*   2 million more permits and 1.3 million new geo-tagged addresses. We also added 19 new jurisdictions. 
*   Our big nationwide contractor license data project has begun. We're integrating all of the state contractor license files we can get our hands on. **We're also including building electrification rebate program affiliations!** 
*   We've begun a big website rewrite project which you'll start to notice in the coming weeks and months. This just kinda needed to happen too. 

Quick reminder
==============

We are here to make building permit data useful. We're hearing from our customers that to be _useful_ we need to make permit data _insightful_.

That's where we're headed. 

We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company). 

Another new software build
==========================

It's a good thing we like learning new software platforms. Cuz if we didn't... Man, I'd be in the wrong profession.  

A few newsletters back ([this one]({filename}newsletter-feb-24.md), to be exact) we launched the Shovels app. It was built in Flutter using FlutterFlow. That detail doesn't matter to 99% of you, but it mattered to me, because I picked it. The main benefit of Flutter is it's cross-platform; the same code lets us deploy to web, Android, and iOS. 

I didn't know it at the time, but this compatibility leads to a lot of limitations. It was hard getting the web app to do what we wanted it to do. 

Also, and this is where you come in, it became clear awfully fast that you don't care about mobile apps. And that meant my Flutter choice was the wrong one.

There were a lot of benefits to this exercise, though. Building our app, "dogfooding" our API, led to the changes you'll see in V2 (more about that [in this newsletter]({filename}newsletter-apr-24.md)). It also made us very comfortable decoupling the web framework from our data backend. We're leaning into that even more with our [brand new beta](https://app.shovels.ai/). 

We're using a fancy new front-end platform to build it. You'll feel the difference right away. 

It's still very much a beta, though. It's a step along the way to our V2 release with all of the new bells and whistles we've been talking about for months. 

For example, check out all these heat pumps in New York!

![Explore our permit data using our web app]({static}/images/heat-pumps-in-ny.png)

Here's a quick summary of the cool new stuff this release does:

*   **Contractor contact info is now included in the CSV download.** On a Permit search, toggle on the Has Contractor? option under Contractor Filters. On a Contractor search, it's always included. 
*   **All permit details are included in the CSV download.** This used to be limited to just a few fields. Now it's not, so you get everything!
*   **Search permits by city.** Now you don't need to remember every zip code in every city! 
*   **Search contractors by city.** Ditto.
*   **An overall cleaner, faster experience.** You'll see. It just feels a lot better.

From the Engineering desk
=========================

We know that software is only as good as the underlying data. That fact is not lost on us. Here's how we improved Shovels permit data last month.  
  
**Permit database growth**  
  
Our total number of permits increased by 2 million, and we expanded our coverage to include 18 additional jurisdictions, along with 30,000 more contractors. In June, more than 400,000 new permits were filed that we are now tracking.

**Better classifications using large language models (LLMs)**

I wish I could share exactly how we did this, but it's a bit of a trade secret at this point. In short, we tested a whole bunch of LLMs against an expert data annotation platform which served as ground truth.

By testing against human annotators, we could see how LLMs "think" about permit descriptions. We then optimized this process to bring down both the production time and its associated cost. We've landed in a really nice place. 

We classified every building permit Texas and have moved on to the rest.

**More geo-tagging**

We're using Esri (where we just joined [their startup program](https://www.esri.com/en-us/about/partners/our-partners/startups)!) to add 1.3 million geo-coordinates to our addresses, which helps reduce the gap of 3 million un-geocoded addresses. The remainder should be geocoded before next month's release. 

**Contractor state license files**

Also next month -- more contractor contact information and building electrification rebate program affiliations. The data collection has been underway for some time and we're finally ready to merge it into production. 

Things to do with permits: sell stuff to contractors
====================================================

We've been taking a LOT of calls recently from companies that sell to building contractors (they also call them "vendors" or "companies" -- basically, orgs that build things) and they all say the same thing: **finding info about contractors is hard**.

Sure, there's ZoomInfo but their firmographic info is static. Employee and revenue numbers don't tell you who does C&I or multifamily or SFH builds. It doesn't tell you where they build or their trades specialization. 

That's where permits come in (with some help from state contractor license files!) Permits fill the void and make contractor databases come to life. We've been working on this for a year (from the start of Shovels, really) and are going to push HARD in the coming months to release a truly exceptional sales intelligence product. 

Here's the big idea:

*   **A website for every contractor (or darn close).** A contractor website domain is the key to joining all sorts of other databases into Shovels. We're going to give them to you.
*   **Contacts at contractors.** The phone and email address on the permit might not be the person you want to reach. We get it. We're building out our own B2B contractor contact database so you can reach deeper into the org. This will be available in both the web app and the API.
*   **Clay integration.** To know [Clay](https://www.clay.com/) is to love Clay. We're working with them on a native Shovels integration. This will be 🔥
*   **Classifications and certifications.** If you want to filter by general contractor, electrician, or other special license, you'll be able to do that too. And we're even adding electrification rebate program affiliations for those of you working to save us from global warming. 

We're thrilled to be working with all of you. 