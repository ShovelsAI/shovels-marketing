title: What Parcels Data Is, and What It Includes
subtitle: The fields, sources, and uses of parcel data. Learn how it connects to permits, ownership, and zoning
date: 2026-06-11
modified: 2026-06-11
category: Customer Success
tag1: Parcels
tag2: Real Estate
tags: zoning, property data, GIS, APN, tax parcel id
authors: Ruoji Tang
author_image: /theme/images/team/Ruoji.svg
author_title: Senior Marketing Manager
slug: what-is-parcel-data
summary: Parcel data is structured property information tied to a specific land parcel. Learn what parcel data includes, where it comes from, and how it's used.
image: /images/blog_images/what-is-parcel-data-hero.png

---

If you're pulling together property data from multiple sources, parcel data provides the connective tissue. It's the layer that ties a physical piece of land to its owner, its assessed value, its legal description, and its history.

Most property workflows, from real estate due diligence to permit research to insurance underwriting, depend on parcel data. Understanding what it includes and where it comes from is the first step to using it effectively.

> **Key Takeaways**
>
> - **What it is**: Parcel data is structured property information compiled from county assessor and recorder records, tied to a specific legal unit of land.
> - **What it includes**: Parcel identifier (APN), owner name, legal description, assessed value, lot dimensions, land use classification, and sale history. Field availability varies by county.
> - **Where it comes from**: County assessors and recorders are the primary source. National providers like Regrid aggregate it into standardized, queryable datasets covering the entire US.
> - **Who uses it**: Real estate, insurance, construction, telecom, and government teams all rely on parcel data for property research and data workflows.
> - **How it connects to permits**: Every building permit is tied to a parcel. Joining permit data with parcel data gives a complete view of construction activity, ownership, and property history.
> - **Shovels**: Shovels includes the Regrid parcel identifier alongside every permit record, linking construction activity directly to parcel ownership and boundary data across 159M+ parcels.

## What Is Parcel Data?

**Parcel data** is structured information about individual <a href="https://www.shovels.ai/blog/what-is-a-parcel-real-estate/" target="_blank">parcels of land</a>, compiled from public county records. Each parcel in a jurisdiction is assigned an <a href="https://www.shovels.ai/blog/what-is-assessor-parcel-number/" target="_blank">Assessor Parcel Number (APN)</a> that serves as the unique identifier connecting the parcel across assessor, recorder, permit, and GIS records. Parcel data organizes those records into a queryable, standardized dataset.

The primary source is the county assessor's office, which maintains property records for tax administration. The assessor tracks ownership, assessed value, and physical characteristics for every parcel in the jurisdiction. County recorders complement this with deed and title records, capturing transaction history.

At the county level, this data exists in different formats across 3,000+ jurisdictions. National parcel data providers aggregate records from counties, standardize the fields, and make them available through APIs and bulk datasets. That aggregation is what makes parcel data practical to use at scale.

## What Does Parcel Data Include?

The specific fields vary by county and provider, but most parcel datasets include some combination of the following:

**Parcel identification:** The APN or parcel ID is the unique identifier for the parcel within the county. The legal description is the formal textual description of the property boundaries derived from the original survey. Parcel geometry contains the GIS boundary coordinates that define where the parcel sits on a map.

**Location and address:** The property address, county and municipality, and sometimes census tract and block. Address standardization varies across counties, which is one reason national providers add significant value.

**Ownership:** Owner name, owner mailing address, and ownership type (individual, LLC, trust, corporation, government). Some states restrict public disclosure of owner names, although availability varies.

**Physical characteristics:** Lot area in square feet or acres, lot dimensions, land use or zoning classification, and (where improvements exist) year built, building square footage, and bedroom and bathroom counts for residential properties.

**Assessed value:** Land value, improvement value, and total assessed value as determined by the county assessor. These figures drive property tax bills and are updated on the county's assessment cycle, which is typically annual.

**Transaction history:** Last sale date, last sale price (not recorded in all states), and prior owner name. This data comes from deed records at the county recorder.

![Tax parcels map of Manhattan. Source: NYS GIS Clearinghouse]({static}/images/blog_images/what-is-parcel-data-manhattan-map.png)
*Tax parcels map of Manhattan. Source: NYS GIS Clearinghouse*

It's useful to note that not every county captures all of these fields. Sale price confidentiality laws in some states, legacy systems in others, and varying update schedules mean no national parcel dataset is fully complete. This is a known limitation of working with parcel data across jurisdictions.

## Where Does Parcel Data Come From?

The authoritative source for parcel data is local government. County assessors maintain assessment records for tax purposes. County recorders capture deed and title transactions. In the US, this data is generally public record and must be made available under state public records laws.

In practice, accessing it directly from counties means navigating thousands of separate portals, formats, and access methods. Some counties offer bulk downloads or data feeds. Others only expose data through search interfaces that don't support programmatic access. Update schedules range from daily to quarterly.

National parcel data providers solve this aggregation problem by pulling from county sources and normalizing field names, data types, and geometries into a single consistent schema. The result is a dataset that works the same way whether you're looking at a parcel in Los Angeles County or a rural county in Vermont.

> Looking for parcels data? Through our partnership with <a href="https://regrid.com/" target="_blank">Regrid</a>, Shovels includes the Regrid parcel identifier alongside every permit record in our nationwide dataset. The `address_id` field in Shovels maps directly to the `ll_uuid` in Regrid, giving data teams a direct join between construction activity and parcel ownership, boundaries, and assessor attributes, no address matching required.
>
> And if you need earlier development signals on a parcel, <a href="https://www.shovels.ai/blog/decisions-api-launch/" target="_blank">Shovels Decisions</a> tracks zoning and land use actions from city councils and planning boards, surfacing how parcel classifications are changing before any permit is ever filed.

## How Is Parcel Data Used?

Parcel data is foundational to a wide range of workflows across industries.

Real estate teams use it for site selection, comparable analysis, ownership research, and acquisition due diligence. Knowing who owns a parcel, what's on it, how it's assessed, and when it last sold informs underwriting and deal strategy at every stage.

Insurance underwriters use parcel data to assess property risk. Physical characteristics, flood zone classifications, land use designations, and ownership structures are all inputs into risk models for homeowners, commercial, and specialty lines.

Construction and permitting workflows depend on parcel data to connect permit records to the properties they describe. Every building permit references a parcel. Joining permit data to ownership and boundary data gives a complete picture of construction activity at any address.

Telecommunications companies use parcel data for fiber deployment planning, serviceable address identification, and ownership research for right-of-way negotiations.

Government and municipal teams use parcel data for tax assessment, zoning enforcement, infrastructure planning, and comprehensive plan analysis.

## How to Access Parcel Data

There are three main routes to parcel data, depending on your scale and use case.

**County assessor and GIS portals** are the direct source. Most counties publish a public parcel viewer and many offer bulk data downloads or exports. Quality and format vary significantly. Search "[county name] assessor parcel data" to find what a specific county makes available. This works well for single-county research or one-time lookups.

**National parcel data providers** aggregate county data into standardized, nationwide datasets. Shovels's data partner Regrid, for example, covers U.S. parcels with consistent field naming and regular updates from county sources. National data providers are the right choice for multi-county or national workflows that can't absorb county-by-county integration work.

**Integrated datasets** combine parcel data with other property records in a single product. Shovels integrates the Regrid parcel identifier into its nationwide permit and contractor dataset, so teams working with construction data also get parcel context without additional data engineering. For teams already working in GIS environments, Shovels data is also available as ArcGIS hosted feature layers.

> Need to work with parcel data at scale? Shovels connects permit history, contractor records, and Regrid parcel identifiers across 1,800+ jurisdictions and 159M+ parcels nationwide. Explore <a href="https://www.shovels.ai/permit-database" target="_blank">Shovels Online</a> or <a href="https://www.shovels.ai/contact" target="_blank">contact us</a> to discuss how parcel and permit data can support your workflow.

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is parcel data?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Parcel data is structured information about individual land parcels, compiled from county assessor, recorder, and GIS records. It includes the parcel's unique identifier (APN), owner name, legal description, assessed value, land use classification, and physical characteristics. It's the foundational layer for most property data workflows.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What does parcel data include?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Most parcel datasets include the APN, property address, owner name and mailing address, legal description, parcel geometry, lot dimensions, land use or zoning classification, assessed value, and sale history. The specific fields available vary by county and data provider.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Where does parcel data come from?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Parcel data originates from county assessors, who maintain records for property tax purposes, and county recorders, who track deed and title transactions. National providers like Regrid aggregate records from thousands of counties into standardized, queryable datasets.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is parcel data used for?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Parcel data is used across real estate, insurance, construction, telecom, and government. Common uses include site selection, ownership research, due diligence, permit-to-parcel data joins, insurance underwriting, and fiber deployment planning.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is the difference between parcel data and property data?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Parcel data refers specifically to structured records maintained by county assessors and recorders for each legal unit of land. Property data is a broader term that may include listing information, MLS data, automated valuation models, and other sources beyond the public record. Parcel data is the most standardized and authoritative layer within that broader category.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Is parcel data public record?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Yes. In the US, parcel data maintained by county assessors and recorders is generally public record. Most states require assessors to make this data available. Some states have privacy protections that limit owner name disclosure, so availability of that specific field varies.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is a tax parcel ID number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A tax parcel ID number is another name for the APN (Assessor Parcel Number). Counties use different terminology: APN, parcel ID, PIN (Parcel Identification Number), tax parcel ID, or tax map number. All refer to the same thing: the unique identifier the county assessor assigns to a specific parcel for tracking ownership, assessed value, and tax obligations.</p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is parcel data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Parcel data is structured information about individual land parcels, compiled from county assessor, recorder, and GIS records. It includes the parcel's unique identifier (APN), owner name, legal description, assessed value, land use classification, and physical characteristics. It's the foundational layer for most property data workflows."
      }
    },
    {
      "@type": "Question",
      "name": "What does parcel data include?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most parcel datasets include the APN, property address, owner name and mailing address, legal description, parcel geometry, lot dimensions, land use or zoning classification, assessed value, and sale history. The specific fields available vary by county and data provider."
      }
    },
    {
      "@type": "Question",
      "name": "Where does parcel data come from?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Parcel data originates from county assessors, who maintain records for property tax purposes, and county recorders, who track deed and title transactions. National providers like Regrid aggregate records from thousands of counties into standardized, queryable datasets."
      }
    },
    {
      "@type": "Question",
      "name": "What is parcel data used for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Parcel data is used across real estate, insurance, construction, telecom, and government. Common uses include site selection, ownership research, due diligence, permit-to-parcel data joins, insurance underwriting, and fiber deployment planning."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between parcel data and property data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Parcel data refers specifically to structured records maintained by county assessors and recorders for each legal unit of land. Property data is a broader term that may include listing information, MLS data, automated valuation models, and other sources beyond the public record. Parcel data is the most standardized and authoritative layer within that broader category."
      }
    },
    {
      "@type": "Question",
      "name": "Is parcel data public record?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. In the US, parcel data maintained by county assessors and recorders is generally public record. Most states require assessors to make this data available. Some states have privacy protections that limit owner name disclosure, so availability of that specific field varies."
      }
    },
    {
      "@type": "Question",
      "name": "What is a tax parcel ID number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A tax parcel ID number is another name for the APN (Assessor Parcel Number). Counties use different terminology: APN, parcel ID, PIN (Parcel Identification Number), tax parcel ID, or tax map number. All refer to the same thing: the unique identifier the county assessor assigns to a specific parcel for tracking ownership, assessed value, and tax obligations."
      }
    }
  ]
}
</script>
