Title: May 2024 Newsletter
Subtitle: We added a new team member and are actively building our next major software release
Date: 2024-5-13
Modified: 2024-5-13
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: Shovels has grown by adding Betty Wan to the team, aiming to enhance their revenue efforts and overall growth. They are currently seeking feedback on their clickable prototype for version 2, which integrates comprehensive building permit and contractor data into one app. Additionally, they are advancing their data capabilities with AI-enhanced tagging and climate tech initiatives, emphasizing the importance of building permit data in reducing fossil fuel consumption and promoting sustainable building practices.
image: /images/cfh-case-header.png


## Shovels May 2024 Newsletter
<br>
Since we last wrote, our team of 3 grew 33%. We're now a team of 4. We're stoked to welcome [Betty Wan](https://www.linkedin.com/in/bettywan7/) to Shovels!

Luka and I have known Betty for years and we knew she'd be perfect to lead our revenue efforts. The timing worked, so here we are.  

That's top of mind as we move to make Shovels 33% better and grow 33% faster. Here's what's up!  

*  We have a clickable prototype of V2. I need to schedule some [short 15 minute calls](https://www.shovels.ai/contact) to watch _you_ click through it. Trade 15 minutes for some permit data? [Let's chat!](https://www.shovels.ai/contact)
*  Our new tagging system is almost ready for launch. Our first AI-enhanced tags will be live before the next newsletter! More on this process below.
*  More jurisdictions, more duration calculations, and more contractor de-duplication was in our latest batch release, which was processed using way more automation.
*  Because every day is Earth Day 🌱 we have a new [climate tech case study]({filename}case-carbon-free-homes.md), a new [climate tech one-pager]({static}/pdfs/Shovels_Climate.pdf), and identified over 14,000 contractors with green rebate program affiliations (more on this next month!)

## First, a primer

A new subscriber told me that she loves this newsletter (I mean, who wouldn't?) but that it's hard to pick up the story mid-stream. Since we're adding > 100 new subscribers every month, I figured she's not alone. 

So, here's the plot so far:

- Shovels set out in Oct 2022 to make building permit data useful  
- Luka and Ryan raised some angel and pre-seed money in March 2023  
- Petra joined us to boost our data engineering in May 2023  
- We released our nationwide building permit API in August 2023  
- We followed that with a nationwide building contractor API in Nov 2023  
- (Lost? Here's [what an API is]({filename}api-guide-1.md))  
- Then we launched [a custom GPT]({filename}gpt-guide-1.md) and [a web app]({filename}app-guide-1.md)  
- Now we're making all ☝️ a lot better  
- And Betty just joined to help me sell this stuff

## Thus, we need V2 feedback

In [last month's newsletter]({filename}newsletter-apr-24.md) I described what V2 is all about.

Basically, it's the killer building permit and building contractor app that doesn't exist in the market yet probably because it seems too obvious.

We're going to give you the ability to look at the permit queue in any jurisdiction, and the active permits on any contractor, and the permit history on any address. All in one killer app. 

We have a clickable prototype and before we really start building it, we'd love to watch you to try to use it.

Can I get [15 mins of your time](https://www.shovels.ai/contact)? What you'll get in return is influence, our gratitude, and some free Shovels data.

Here's the same sneak peak I shared last month.

![Explore our permit data using our web app]({static}/images/explore.png)

## From the Engineering desk

At Shovels, we're on a mission to make our data dazzle by harnessing the coolest tech out there! We're excited to introduce our latest initiative: using Large Language Models (LLMs) to improve the tagging accuracy of permit records.

**Efficient Testing and Validation**

Our approach included a comprehensive evaluation of various LLMs, selecting the best fit for understanding and categorizing permit data. We are establishing a rigorous validation process, incorporating expert feedback to refine the model's accuracy through continuous iterations.

**Scalable Architecture for Future Growth**

Based on our findings, we've been designing a scalable architecture that integrates with our systems and is equipped to handle future expansions. This ensures our capacity to manage and tag data efficiently as our operations grow.

**Re-tagging and Expanding Tags**

We will soon re-tag all existing permit records with this new system, doubling our tag categories! This expansion will enrich our dataset, offering more detailed insights and enhancing the value we deliver to our clients. 

**Miscellanea**

- We have implemented stricter validation rules for permit dates to address previously observed inaccuracies, such as implausible dates like "1900-01-01".   
- We added construction\_duration which captures the time span between the issue and final date. The previous duration field is now called approval\_duration.  
- We fixed issues where some permits did not have a status field set despite having a final\_date value.   
- We resolved a bug affecting the grouping of contractors. Now contractors sharing the same phone number are accurately grouped together.

# Things to do with permits: save humanity

I subscribe to the notion that "Save the Planet" doesn't make much sense. The planet was fine before it was dominated by homo sapiens and it would be fine without us, too.

We don't need to Save the Planet. We need to save ourselves. 

Last month was Earth Month, punctuated by Earth Day on April 22. Much of the discussion was about the ocean currents that impact air temperature and weather events everywhere. 

What contributes to warmer oceans? Greenhouse gases. And what contributes to greenhouse gases? Fossil fuels. And what accounts for a third of all fossil fuel consumption? Buildings.

Specifically, heating air and water inside of buildings. This is why building permit data is [useful for climate tech]({static}/pdfs/Shovels_Climate.pdf).

It's why we're working with [so many climate and construction companies](https://www.shovels.ai/blog/?category=Case%20Study) who want to identify home and building owners who can level up to hyper efficient heat pumps to do the heating currently done by gas, oil, and propane appliances.

Building permit data isn't perfect, but it's the best tool we've got. 

We're here to help.