Title: How to supercharge lead generation with Shovels API and Clay
Date: 2025-06-07
Subtitle: Automate construction industry prospecting with Shovels API and Clay
Modified: 2025-06-07
Category: Company
Tags: lead-generation, automation, api-integration, clay, construction-industry, sales-automation, prospecting
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: This article provides a practical guide on integrating Shovels API with Clay to automate construction industry lead generation. It demonstrates how to combine Shovels' database of 170M+ building permits and 3M+ contractors with Clay's no-code platform to create efficient prospecting workflows. The guide includes three real-world examples: finding active HVAC contractors, enriching contractor profiles, and building solar company mailing lists, showing how to reduce manual research costs by 87% while significantly increasing prospect volume.
image: /images/shovels-clay.png


Using the Shovels API within Clay transforms construction industry prospecting from manual research into automated data pipelines. This powerful combination gives sales and marketing teams instant access to building permit data, contractor information, and property owner details - all enriched and organized within Clay's no-code platform.

To good to be true? Not really. Here's how the pros do it. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/IhUpiT_PTWU?si=4OIUY2MHKKS1pR-L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What makes this integration powerful

**Shovels** provides the most comprehensive building permit and contractor database in the United States, covering over 170 million building permits and 3 million contractors. Our API offers precise geographic filtering, permit tracking, and detailed contractor performance metrics. With the Shovels API, you can filter by everything from specific work types to job values and inspection pass rates.

**Clay** revolutionizes go-to-market workflows by combining 100+ data sources with AI-powered enrichment capabilities. Its HTTP API integration feature (available on Explorer plans and above) enables teams to connect any external API without writing code. Clay's write to table functionality then transforms complex API responses into structured, actionable lead lists ready for outreach campaigns.

Together, these tools eliminate hours of manual research while uncovering high-intent prospects that traditional methods miss. Sales teams can identify contractors winning new projects, marketing teams can target homeowners completing renovations, and business development teams can track competitor activity - all automated within Clay workflows.

## Authentication: Connecting Shovels to Clay

### Step 1: Get your Shovels API Key

Shovels uses key-based authentication, which makes it very easy to work with API services like Clay's HTTP API enrichment. If you've never set something like this up before, though, it can be a bit confusing so let's walk through it.

Start by grabbing your API key from Shovels Online. Log in here: [https://app.shovels.ai](https://app.shovels.ai)

> 😊  Note: Even **free** accounts on Shovels Online have API keys enabled! 

Now go here: [https://app.shovels.ai/profile-settings/](https://app.shovels.ai/profile-settings/)

Click the API Key tab and to see your API Key. It looks like this. Click **Copy** and move on to the next step! 

![Shovels API Key]({static}/images/shovels-api-key.png)

### Step 2: Save your Shovels API Key as a Clay Headers account

Log into your Clay account and click Settings in the navigation pane on the bottom left.

Then go to Connections and click the **+ Add Connection** button.

In the search bar, search for Headers. You should now be here. 

![Clay headers]({static}/images/headers.png)

Click HTTP API (Headers) and you'll see this pop up. Name your connection (I call it "Shovels") and click the **+ Add a new key and value pair** button.

- In the Key field, enter `X-API-Key`
- In the Value field, paste your Shovels API Key, which you copied in the previous step

![Name your Clay connection]({static}/images/name-connections.png)

![Store your key]({static}/images/store-key.png)

That's it! Now for any HTTP API enrichment in Clay, you can conveniently choose Shovels from your HTTP API (Headers) account and you won't need to look up your Shovels API again.

![Clay headers]({static}/images/headers2.png)

Now we can begin Shoveling inside of Clay. Let's hop to it. 

## Example 1: Building active HVAC contractor lists by geography

Finding HVAC contractors actively pulling permits in your target market traditionally requires searching multiple government websites and cross-referencing business databases like Yelp and Google Maps, which often provide stale data. 

> 📖 **Permit Tags Reference:** You can use any of our `permit_tag` values. For convenience, here they are: `addition`, `adu`, `bathroom`, `battery`, `demolition`, `electric_meter`, `electrical`, `ev_charger`, `fire_sprinkler`, `gas`, `generator`, `grading`, `heat_pump`, `hvac`, `kitchen`, `new_construction`, `plumbing`, `pool_and_hot_tub`, `remodel`, `roofing`, `solar`, `water_heater`

With Shovels and Clay, this becomes a three-step automated process.

First, set up your Clay table and add a text field called Cities. Write a few city names, one per row. 

Now add an HTTP API column. Set the method to GET and use the endpoint `https://api.shovels.ai/v2/cities/search`. In the query parameters, add one called `q` and in the value choose the City column (press "/" to see a list of columns). This API call returns the unique geo_id for each city - Shovels' geographic identifier system that enables precise location-based searching.

To isolate this geo_id, make a new column. Go **+ Add Column** and click the Formula option. 

![Clay formulas]({static}/images/formula.png)

Here's the formula I used: `Shovels City Lookup?.items?.[0]?.geo_id.trim()` but Clay also has a nice "Use AI" option where you can describe what you're trying to get. Remember to type the "/" character to be able to reference other columns in the table. 

Call this column geo_id.

> 📚 **Understanding Clay Formula fields and being able to use the AI helper is critical to moving fast inside of Clay!**

![Clay formulas AI]({static}/images/formulas-ai.png)

Now we have a column with our Shovels geo_id, so we can use it to find contractors! 

> 💡 **Important note:** if you don't care about cities and are fine searching states or zip codes, the two-character state abbreviation (CA, FL) and the zip code (94123, 33178) are their own geo_id's. You don't need to look them up! 

Create a second HTTP API column for contractor discovery. Configure it to make a GET request to the `https://api.shovels.ai/v2/contractors/search` endpoint with these required parameters: `permit_from` set to 90 days ago, `permit_to` as today's date, `geo_id` pulled from the formula field we just made, and `permit_tags` set to **hvac**. This returns all HVAC contractors with recent residential permit activity. 

This is how your setup should look.

![Clay http api setup]({static}/images/clay-setup.png)

Finally, use Clay's write to table feature to transform the nested contractor data into individual rows. 

In your HTTP API column results, click "Send to table," select the items array containing contractor items, and the original city name, just to have it. Here's my setup.

![Clay send to table]({static}/images/clay-setup2.png)

Your new table automatically populates with qualified, active HVAC contractors and all the Shovels data we have on them. From this other table, you'll be able to parse out the Shovels fields into separate columns and run some AI summaries on them.

This is explained in the next step! 

## Example 2: Enriching contractors for personalized cold outreach

Starting with just contractor names, you can build complete profiles with permit history and performance metrics that enable highly personalized outreach icebreakers. This approach works perfectly for targeting specific high-value contractors or building account-based marketing campaigns.

> 💡 **If you already have contractor_id's you can start with those too!** You'll have these at the end of Example 1. It's much easier to work with contractor_id's than contractor names.

Begin by configuring an HTTP API call to search contractors by name. Use the endpoint `https://api.shovels.ai/v2/contractors/search` with the contractor_name parameter linked to your Clay column. Set a wide date range using the `permit_from` and `permit_to` parameters like we've done before to capture comprehensive permit history, and use a state `geo_id` like CA or FL so you cast a wider net. This search returns matching contractors with their unique contractor_id.

Create a second API column to fetch detailed contractor metrics using the contractor_id. Call `https://api.shovels.ai/v2/contractors/<contractor_id>` (but `contractor_id` should be a reference to your Clay table field with the contractor_id value) to retrieve the complete contractor profile. Key fields include tag_tally (showing permit counts by work type like `{roofing: 45, solar: 12, hvac: 28}`), status_tally (permit statuses showing completion rates), inspection pass rates, average project durations, and monthly activity trends. These metrics reveal contractor specializations, reliability, and growth patterns.

Now leverage Clay's AI enrichment capabilities to generate personalized icebreakers. Create a Clay AI column with a prompt like: "Based on this contractor's permit data showing `tag_tally` and `recent projects`, write a personalized cold email opening that references their specific work and recent success." The AI analyzes permit patterns to create relevant hooks: "I noticed ABC Roofing completed 12 residential re-roofing projects in Austin last quarter - impressive growth from your 2024 average of 6 per quarter."

## Example 3: Creating homeowner mailing lists for solar companies

Solar installation companies need homeowners who recently invested in roof improvements - a perfect use case for Shovels' permit data combined with Clay's multi-table workflows. This approach identifies pre-qualified prospects based on actual home improvement behavior.

Start by searching for recent roofing permits in your target geography. Configure an HTTP API call to `https://api.shovels.ai/v2/permits/search` with parameters: `permit_from` 60 days ago, `permit_to` today, `geo_id` for your target area (see Example 1 for resolving cities to geo_id's), `property_type` as residential, and `permit_tags` set to roofing. Add `min_job_value` of 5000 to filter for substantial roof projects. This returns permits including the critical address information with each property's unique geo_id.

Use the Send to table enrichment to create a new "Roofing Properties" table from the permit results. Map these fields to columns: permit description, job value, file date, property address components (street, city, state, zip), and most importantly, the `address_id` which is in the `geo_ids` key on each permit. This creates individual rows for each property with recent roofing work - your base prospect list.

For each property, make an API call to retrieve homeowner information using `https://api.shovels.ai/v2/addresses/<address_id>/residents`. This endpoint returns resident names and available contact information. Configure conditional logic to only run this enrichment for properties with completed permits (using the status field). Map the resident data to new columns for first name, last name, and any available contact details. Combine this with Clay's additional data providers to append phone numbers or email addresses where Shovels data has gaps.

The final table contains homeowners who invested $5,000+ in roof work within 60 days - prime candidates for solar installation outreach. Export to your CRM or marketing automation platform for targeted direct mail campaigns highlighting solar incentives for new roofs.

🌟 Magic! ✨

## Massive time and cost savings with automated prospecting

Traditional construction industry prospecting involves manually searching government permit databases, cross-referencing contractor licenses, and building lists one record at a time. A single sales rep might spend **20 hours per week** on research, yielding 50-100 qualified prospects. With Shovels and Clay integration, the same research happens in minutes, generating thousands of verified, enriched prospects.

Consider the cost impact: manual research at $25/hour costs $500 weekly per rep, or $26,000 annually. The Shovels API and Clay Explorer plan combined cost under $500 monthly - an **87% cost reduction** while increasing prospect volume by 10-50x. More importantly, your team focuses on selling instead of searching.

The accuracy improvement is equally dramatic. Manual research relies on outdated directories and incomplete databases. Shovels provides real-time permit data directly from government sources, ensuring you're targeting contractors and homeowners based on actual, recent activity. Clay's enrichment layer adds contact information, company details, and AI-powered personalization - creating ready-to-contact prospect lists that convert at significantly higher rates.

For construction industry sales teams, real estate professionals, and B2B companies targeting contractors or property owners, this integration transforms prospecting from a bottleneck into a competitive advantage. The combination of Shovels' comprehensive permit intelligence and Clay's automation capabilities creates a lead generation system that scales with your business while dramatically reducing cost per lead.

> 🎁  I made some Clay table templates! [Get them here](https://app.clay.com/shared-workbook/share_0sxht86CPrde37QtkZB).