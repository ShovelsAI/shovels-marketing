Title: US Solar Construction Trends (2024)
Subtitle: Insights into US Solar Construction Trends using the Shovels platform and data models.
Date: 2024-09-11
Modified: 2024-09-11
Category: Data
Tags: RE Plus, Solar, Insights
Authors: Alex Brown
Summary: The Shovels dataset and model can highlight key construction trends and patterns. In this blog, we discuss solar construction specifically due to the RE+ clean energy convention. Use Shovels to inform your construction company's business models and strategy.
Image: /images/digging-in-us-solar-construction-heatmap-watermarked.png

[RE+](https://www.re-plus.com/) is the largest and most comprehensive clean energy conference in the United States. In honor of it’s 20th Anniversary, we’re publishing some insights we’ve gleaned from our datasets and models here at Shovels. 

(By the way, if you’re reading at the time of publication, we’re at RE+ in Anaheim right now! Come find us on the floor, or reach out directly to coordinate — we want to meet you!)

Solar tech, and clean energy tech generally, is something we’re really passionate about. We’ve recently [partnered with WattCarbon](https://www.shovels.ai/blog/shovels-partners-with-wattcarbon/) to support their decarbonization efforts via their new Energy Attribute Certificate (EAC) Marketplace, and also worked with [Carbon Free Homes](https://www.shovels.ai/blog/case-study-empowering-carbon-free-homes/) to improve their climate-friendly contractor matching platform. 

But today, we’re shining a light on solar construction trends thus far in 2024.

## The Shovels Model

For anyone new here (welcome!), we’ll give a quick refresher on what we do. Shovels is a building insights company, and we aggregate, normalize, and make construction data useful. It started at building permits, but we’re expanding into more robust models by incorporating contractor profiles, tax assessor files, and other publicly accessible data. 

From there, we can query, filter, and summarize the data any which way you like: by market, geo-region, or address; by permit type or fields, by contractors, etc. 

For today’s analysis, we’re going to be querying our model based on two key filters:

1. Permits filed this year; or `file_date = 2024%`. 
2. Solar-inclusive projects (anything that includes solar technology); or `solar = true`.

> [!NOTE]
> Fields like these, along with other variables used in our model, can be reviewed in our [Data Dictionary](https://docs.google.com/spreadsheets/d/1qiIxx37_-6vGfGp2i5pXv4w2FdsLsShjCqSVO5v6OMQ/edit?gid=1818227349#gid=1818227349). 

We can dig deeper than those to get into specifics of things like **Contractor Availability** or **Average Approval Time** later on, but for now these two filters will serve as the foundation of this dataset. 

While there are solar projects all over the country, it’s clear that the vast majority of activity is here in California, so let’s take a closer look.

## Spotlight on California

California has led the nation in solar adoption and technology for decades now, and part of that adoption is the widespread governmental support in the forms of [incentives, tax credits, and rebates](https://www.forbes.com/home-improvement/solar/california-solar-incentives/). So it makes sense that The Golden State continues to outpace everyone else in the push towards net-zero emissions and clean energy production. 

Filtering the dataset above once again — by `state = CA` — and sorting by geo-coordinates `lat` and `long`, we can see a heat map of this year’s construction volume.

![Map of California with heatmap showing volume of solar project permits, by geographical coordinates.](/images/digging-in-ca-solar-construction-heatmap-watermarked.png) 

Hubs like Los Angeles, San Diego, San Jose, and others in the Central Valley show the most activity. 

However, tax incentives aren’t the entire picture. The state-wide building permit pipeline is a well-oiled machine. Experienced contractors and administrative support makes filing your permit easy, which results in an astounding 6.15 day average approval time. 

Sidenote: to be fair to the other states, some are performaing just as well if not better than California (eg, NY with an average of 2.8 days), yet none come even close to the permit volume. 

More impressively, the hotspots above have even better approval times, with San Diego County leading the way with a blistering 1.79 day average.

As a reminder, this is across all projects which include solar installation of any kind, so small panels on your personal home are counted in line with massive commercial construction that cover their roofs with solar arrays. 

If your local jurisdiction wants to up their pace and adoption rates for solar- or other green-energy technologies, California is a good place to emulate.

## Insights, In Season

Metrics like **Permit Volume** and **Average Approval Time** can be nice pats-on-the-back, but the real power of the Shovels model is trend and market gap analysis. 

Taking the model we’ve refined already, let’s tweak it slightly to get a historical view of the past 4 years. If we adjust the original filter to `file_date = 202%` (to cover everything built since January 2020), we can see the construction trends and seasonalities. 

Below is one such query, visualized and sorted by `month`.

![Area line graph showing California permit volume for solar projects since January 2020, by month.](/images/digging-in-ca-solar-construction-trend-2020s-watermarked.png)

There are seasonal spikes before and after Summer, with the biggest peak to date in March 2023 with a staggering 33k+ solar-inclusive project permits filed that month alone. This graph illustrates the duality of man, or at least those who installed their solar panels in advance versus those who regret not getting them up earlier that Spring. 

The trendline here shows that things are slowing down, but only in comparison to the previous years’ highs. Using other construction data to determine solar saturation and wider construction trends in your specific market, Shovels could provide actionable insights into timing and lead-gen opportunities. 

Maybe other green technologies like [heat pumps](https://techcleanca.com/) are relatively underrated, and ripe for a strong market push?

> [!Tip]
> Free Shovels Advice: if you’re a solar supplier or in a solar-adjacent market, now would be **a very good time** to confirm those outbound pipelines are fired up to prepare for the early Fall installation push. 
> 
> Shovels has in-depth contractor profiles and data that you could use for that very purpose — [reach out today](mailto:sales@shovels.ai)!

Derivative metrics that can inform projections and trends are the name of the game, and a core tenet of the Shovels model and datasets. While solar construction is close-to-heart, we cover all range of project types — if it requires a building permit (and the jurisdiction digitizes their records), then we’ll have it for consumption. If we don't, let us know and we'll get it for you.

## Get Your Own Shovel Today

Building permit data is the foundation of the Shovels platform, and wrangling it at scale can provide actionable business insights, legislative or administrative effectiveness reports, or anything in between. 

If that kind of scale is what you’re looking for, then our [Enterprise](https://www.shovels.ai/data-feed) product will be the best fit. We’ll send you the files and raw data for consumption into, or in tandem with, existing models. 

On the other hand, we have a [robust API](https://www.shovels.ai/api) for direct integration of our data to your own platform(s). 

Check out our [Free Trial](https://beta.shovels.ai) today to see how our platform works, or get in contact with us for a demo and sample dataset of your preferred market at [sales@shovels.ai](mailto:sales@shovels.ai). 

Happy Digging, and let us know how you enjoyed RE+ in Anaheim this year!
