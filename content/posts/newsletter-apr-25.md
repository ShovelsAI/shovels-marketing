Title: April 2025 Newsletter
Subtitle: It's Climate Week in San Francisco and we are here for it.
Date: 2025-04-21
Modified: 2025-04-21
Category: Company
Tags: company
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: This month's update covers our energy data initiatives, major improvements to contractor license data with 12 new categories, and insights from our solar permit density analysis in San Diego. We're also previewing upcoming enhancements to contractor domains and permit job value modeling.
Image: /images/pw.png

It being Climate Week in San Francisco, and the climate this past week being nothing short of *lovely* (sunny and 72**°**), I give to you a relatively shorter newsletter that's a bit of a recap on where Shovels came from and what energy companies can do with our building permit and contractor data.

*You're getting this email because you reached out to us. We send one big newsletter each month. People seem to like it -- we now have over 5,200 subscribers!*

*Shovels transforms building permit data into actionable insights about contractors, homeowners, and market trends.*

*We post all of our newsletters on our blog. If you want the full recap on what's been going on at Shovels, you can [read them all here](https://www.shovels.ai/blog/?category=Company).*

# ⚡️ Energy and permits

I am VERY curious to see what 300 energy data hackers plan to do with us and our friends [Bayou Energy](https://www.bayou.energy/), [Palmetto](https://palmetto.com/), and [Texture](https://www.texturehq.com/) in this week's [energy hackathon](https://lu.ma/pwh9o2e8?tk=jYxRHS). 

To me, having looked up to climate tech entrepreneurs my whole career, it's rewarding to stand alongside a few of the best, and maybe even call myself one. Going all the way back, it was a curiosity about how to find a good heat pump installer that set me off on this journey. (We found one, and we love our Fujitsu Halcyon mini-splits.)

From that beginning, we've gone on to sign deals with massive companies like Oracle ([Opower](https://www.oracle.com/utilities/opower-energy-efficiency/)) and awesome climate startups like [WattBot](https://wattbot.com/). I love working in the climate and energy markets.

To take it down to brass tacks, here's the energy work that can be done with our data:

- Track regional electrification trends by monitoring heat pump, EV charger, and solar panel  permits (see [blog post](https://www.shovels.ai/blog/solar-permit-density-san-diego/), below)
- Identify and validate contractors with specific electrical/HVAC licenses for utility incentive programs
- Forecast grid capacity needs based on electrical infrastructure upgrades in specific neighborhoods
- Analyze seasonal construction patterns to optimize workforce deployment and supply chain management
- Help manufacturers of electrical equipment track distribution and market penetration across regions

There's so much that can be done with this data. It feels like we're still just getting started.

# 📢 What's happening now

Finally, here's what we're thrilled to announce has gone live this month.

## New and improved contractor license data!

Long-time coming on this one.

We added dozens of new state license files to fill missing license and classification details. This update brings two key changes:

1. Added classification categories for contractors with **existing** licenses
2. Added license data for over 80,000 previously unlicensed contractors

We distilled over 3,000 state contractor classifications into 12 contractor license categories and brought them into our EDL product.

- Concrete & Paving
- Demolition & Excavation
- Electrical
- Fencing & Glazing
- Framing & Carpentry
- General Building Contractor
- General Engineering Contractor
- HVAC
- Landscaping & Outdoor Work
- Plumbing
- Roofing
- Specialty Trades

Since contractors can have multiple licenses, we'll present them separated by vertical bars (e.g., HVAC | Electrical).

This is available now to our enterprise customers and we'll roll it out to **Shovels API** and **Shovels Online** later this month.

## More contractor domains and permit job values

Next on the docket is improved contractor domain coverage. The new domain data is ready to be merged into our contractor tables and released in a couple of weeks.

We've also completed the R&D on our permit job value modeling, which will not only increase the job_value fill rate on permits, it will also dramatically improve the accuracy of our contractor revenue data.

I've written here about these projects before. It turned out to be a heavier lift than we thought. Doing it right took a lot of creativity and required us to tack on some new data science projects before we could even get started.

For example, to model job values, we actually needed to create more permit attributes, which meant doing entity extraction on the permit description field. With that done (on 170 million permits — not a small feat) we could get back to the modeling math.

Bringing multiple regression to permit data — that's why we're here, folks!  

I expect both projects to go live next month. 

# Things to do with permits: cumulative solar permit density charts 🤓

![Solar permit density graph]({static}/images/pw.png)

I was invited to give a short talk for the Center for Built Environment at UC Berkeley (Go Bears!)  which I gladly accepted.

Here are [the slides](https://docs.google.com/presentation/d/1i50LcSxkA5Voq2FpCxLrRerP1uGGDwqe5rzNfQpK-Qo/edit?usp=sharing) and here's [the blog post](https://www.shovels.ai/blog/solar-permit-density-san-diego/) about the slides.  

The TL/DR here is we helped a policy group in San Diego apply for a grant and used our permit data in San Diego to demonstrate how it can show home improvement adoption rates. Specifically, we wanted to understand which neighborhoods are leading the charge in building electrification, so we analyzed solar adoption curves across census tracts in Poway and Chula Vista.

The big surprise? Two very different cities - Poway (older homes, more affluent) and Chula Vista (newer construction, more diverse) - showed nearly identical solar adoption rates. They emerged organically by looking at the census tract level for highest current adoption. Even more interesting, Chula Vista's significantly lower permit fees ($458 vs San Diego's $6,420) and "Solar Ready" ordinance seem to be driving adoption more than traditional factors like home age or wealth. 

It's a great example of how smart local policy can accelerate sustainability efforts and how permit data can shine a light on homeowner behavior.