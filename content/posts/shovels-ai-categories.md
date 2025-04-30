Title: Putting the AI in Shovels.AI
Subtitle: The overview of using AI to power the Shovels platform.
Date: 2025-04-29
Modified: 2025-04-29
Category: Company
Tags: AI, permits, data
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: The Shovels platform is powered by AI, but it isn't a gimmick. We use LLMs to turn messy permit data into a structured dataset. This transformation unlocks the key permit insights and intelligence that you can't get anywhere else. 
Image: /images/shovels-ai-categories-hero.png

What does the ".ai" in [shovels.ai](https://www.shovels.ai){:target="_blank"} even mean? 

These days, it's hard to differentiate between the trendy buzzwords and GenAI wrappers from the tools that rely on actual machine learning and large-language models (LLMs) to deliver value. 

Today, we'll give a sneak peak behind the curtain on what it means for Shovels to be "powered by AI". 

## The Shovels Platform

At our core, we leverage modern AI and LLM tools to bring structure to one of the messiest datasets in the US: building permits. 

With over **170M+ permits nationwide**, spread across **20k+ independent permit jurisdictions**, standardization is no joke. Every city or county has its own permitting terminology, standards, and requirements. This means that there are hundreds (or sometimes even thousands) of variations on describing and categorizing similar projects. 

We address this challenge by using self-trained and specialized LLMs to tag and classify every permit we have, using a consistent schema and structure to make this data actually useful. Permit data analysis is only possible when you can have a clearly defined and normalized dataset. 

If you'd like to read more about how we did this, check out our [blog post on our partnership with Prolific](https://www.shovels.ai/blog/unlocking-shovelss-potential-with-prolific/){:target="_blank"}.

Now let's dig in to the details (as much as we can) of how we do it.

## AI-Powered Tagging

Actual permits can range from highly-structured documents (looking at you California and Florida) to nearly free-form (sorry New Hampshire 🤷) data. This makes analysis at a regional or national scale nearly impossible. 

We solved this by building a data cleaning pipeline that uses LLMs to:

- Read each permit's description, type, subptye, and any other associated context.
- Extract that contextual meaning.
- Assign that permit to one or more Shovels-defined categories (or tags). 

Permits may span multiple project types, so the nuance of a large scale electrification project may be represented with a combination of  `solar`, `electrical`, `ev_charger`, `battery`, and `roofing` tags at the same time. 

## The Shovels-defined Categories

Here's the full list of our categories that we can assign to a given permit:

- `ADDITION`
- `ADU`
- `BATHROOM`
- `BATTERY`
- `DEMOLITION`
- `ELECTRIC_METER`
- `ELECTRICAL`
- `EV_CHARGER`
- `FIRE_SPRINKLER`
- `GAS`
- `GENERATOR`
- `GRADING`
- `HEAT_PUMP`
- `HVAC`
- `KITCHEN`
- `NEW_CONSTRUCTION`
- `PLUMBING`
- `POOL_AND_HOT_TUB`
- `REMODEL`
- `ROOFING`
- `SOLAR`
- `WATER_HEATER`

As we expand and enhance our platform and classification pipeline, we may introduce more categories (we've already got `WINDOW_AND_DOOR` on the docket). If you have any suggestions, please [let us know](mailto:support@shovels.ai)!

## Why Categorization Matters

Structuring data is the first step to scalable analysis, so it was crucial that we figured out a way to squeeze the entire breadth of permit data (including the spelling errors) into a consistent schema. With this in place, we can turn this raw data into actionable insights.

This isn't something that you can just plug into your preferred GenAI application and call it a day -- it took an unbelievable amount of work to dial it in. 

But the benefit is absolutely worth it. With this newly-structured data, businesses of all sizes are *already* using Shovels to:

- **Improve Searchability**: Find the addresses and projects they need quickly and at scale.
- **Enable cross-jurisdiction intelligence**: Compare apples-to-apples, even when the permit terminology or requirements differ.
- **Automate workflows**: Power marketing, sales, and analytics with the cleanest data inputs in the market.

## "Neat ... what can I actually do with this data?"

Here are some of the most common examples we see today:

**Real Estate Development**: 

Developers can identify trends in zoning approvals, new construction activity, or infrastructure upgrades across specific geographies.

**Climate Tech**: 

Tags like `SOLAR`, `EV_CHARGER`, and `HEAT_PUMP` allow climate-focused companies to track clean energy adoption and locate target markets.

**Home Services**: 

Companies offering HVAC, roofing, or plumbing can identify homes with recent installs—or aging infrastructure—and focus outreach accordingly.

### Example: HVAC Lead Targeting

Want to reach homeowners who've recently installed HVAC systems in the past year?

1. Use Shovels to filter all permits tagged with `HVAC`, by zip code.
2. Exclude permits tagged with `NEW_CONSTRUCTION` to target retrofits **only**.
3. Export this curated list for direct mail or email outreach campaigns directly to the homeowners. 

For more on this workflow, check out [our recent blog on GTM strategies here](https://www.shovels.ai/blog/top-5-gtm-strategies-using-shovels-online/){:target="_blank"}. 

## Conclusion

Categorization isn't just nice to have; it's essential infrastructure for working with fragmented and unstructured permit and construction data. 

Shovels uses a combination of purpose-built LLMs to clean, classify, and standardize millions of records, making it easier to extract insights and take action. 

If you work with permit data - whether for marketing, research, or planning - Shovels offers a scalable and intelligent approach to organizing it. 

Want to learn more or discuss your specific data needs? [Get in touch today!](https://www.shovels.ai){:target="_blank"}