title: What Is an Assessor Parcel Number, and How to Find It
subtitle: Everything you need to know about APNs: what they are, how they're formatted, and the fastest ways to look one up.
date: 2026-05-20
modified: 2026-05-20
category: Customer Success
tag1: Parcels
tag2: Real Estate
tags: assessor parcel number, APN, parcel number, property data, county assessor
authors: Ruoji Tang
author_image: /theme/images/team/Ruoji.svg
author_title: Senior Marketing Manager
slug: what-is-assessor-parcel-number
summary: Learn what an Assessor Parcel Number (APN) is, how it's structured, and the step-by-step ways to find a parcel number using county websites, tax records, deeds, and property data tools.
image: /images/blog_images/what-is-assessor-parcel-number-hero.png

---

You need to pull a permit history on a property. The county portal asks for a parcel number. You don't have one. Now what?

An Assessor Parcel Number (APN) is the unique ID your county assigns to every piece of land in its jurisdiction. It's what connects a property across tax records, building permits, title documents, and ownership history. Knowing how to find one quickly saves a lot of time, whether you're researching a single address or running lookups at scale.

This guide covers what an APN is, how it's structured, and all the ways to track one down.

> **Key Takeaways**
>
> - An Assessor Parcel Number (APN) is the unique identifier a county assessor assigns to each parcel of land. It's the primary key connecting a property across tax, permit, title, and ownership records.
> - APN formats vary by county (3K+ in the US). Most use a hyphenated numeric string that encodes geographic information like map book, page, and parcel position.
> - The fastest ways to find a parcel number are: the county assessor's website, a property tax bill, a recorded deed, or a county GIS map.
> - Shovels includes the Regrid parcel identifier alongside every permit record, giving customers a direct join between construction activity and parcel ownership data.

## What Is an Assessor Parcel Number?

An **Assessor Parcel Number (APN)** is a unique identifier assigned by the county assessor to each parcel of land in the public record. It's the primary key used to connect a property across tax assessments, building permits, title documents, and ownership records.

Every county in the United States assigns APNs to parcels within its jurisdiction. The APN stays with the parcel, not the owner. It remains the same even when a property changes hands. When a parcel is subdivided, merged, or otherwise altered through a legal process, the existing APN is retired and new ones are issued.

The APN goes by different names depending on where you are. Some counties call it a Parcel Identification Number (PIN), a Tax Parcel ID, a Tax ID Number, or just a Parcel Number. Different names, same concept.

> If you're new to parcel data more broadly, our guide on <a href="https://www.shovels.ai/blog/what-is-a-parcel-real-estate/" target="_blank">what a parcel is in real estate</a> covers the bigger picture: how parcels are defined, how they're officially recorded, and how they connect to building permits and ownership history.

## What Does an APN Look Like?

APN formats vary by county, but most follow a numeric pattern based on how the county has organized its assessor's maps. Some typical formats:

- **123-456-78** (three-group hyphenated, common in California counties)
- **12-34-567-890-1234** (longer hyphenated format used in some Midwest counties)
- **1234567890** (flat numeric string with no separators)

Many counties encode geographic information into the number itself. In Los Angeles County, for example, the APN reflects the map book, page, and parcel position within that page. In other counties, the format is purely sequential. There's no national standard, which is one reason working with parcel data across county lines gets complicated quickly.

What matters practically: the APN is unique within a county and stable over time (barring physical parcel changes), making it the most reliable identifier for a specific piece of land.

## Why Does the APN Matter?

The APN is the backbone of the public property record system. Every significant document tied to a piece of land connects back to it:

- **Property tax records**: Tax bills are issued by parcel. The APN is how the assessor tracks ownership, taxable value, and payment history.
- **Building permits**: Every permit application includes the parcel where the work is happening. The APN links the permit to the property's boundary, ownership, and construction history.
- **Title and deed records**: Recorded deeds reference the parcel's APN in the legal description. When title researchers trace ownership history, they follow the APN backward through time.
- **Zoning and utility records**: Many jurisdictions use the APN in zoning classifications, utility hookup records, and entitlement filings.

For data teams, the APN is the join key. Want to connect permit history with ownership data? Join on the APN. Want to link a tax roll to a GIS boundary file? APN. It's the thread that runs through every public property record.

## How to Find a Parcel Number

There are five reliable ways to find a parcel number. Which one makes sense depends on what you already have.

### 1. County Assessor's Website

This is the most direct route. Most county assessors run a public portal where you can search by property address and get the APN back. Search "[county name] assessor parcel search" in a browser and navigate to the official .gov website.

Enter the street address and the results will show the APN alongside ownership information and assessed value. Some county portals are clean and modern. Others look like they haven't been touched since 2003. Either way, this is the authoritative source.

### 2. Property Tax Bill

If you own the property or have access to tax documents, the APN is printed directly on the tax bill. It's usually labeled "Parcel Number," "APN," or "Tax Parcel ID." This is the fastest method if you have the paperwork on hand.

### 3. Recorded Deed or Title Report

Recorded deeds include the APN in the legal description of the property, usually near the top of the document. Title reports, closing packages, and abstracts of title all include it as well. If you're in the middle of a transaction or doing due diligence, this is a quick place to pull it from.

### 4. County GIS Map

Most counties publish a public GIS portal with parcel boundary layers. Click on a parcel on the map and the APN appears in the pop-up. Search for "[county name] GIS parcel map" to find it. This method is especially useful for properties without a clear address, such as vacant lots, rural parcels, or large undivided acreage.

### 5. Parcel Data Provider

For anyone working with multiple properties or building data pipelines, looking up parcels one by one through county portals isn't practical. National parcel data providers like <a href="https://regrid.com/" target="_blank">Regrid</a> aggregate parcel records from thousands of counties into a standardized, searchable dataset. You can query by address, coordinates, owner name, or existing identifiers.

> **Did you know?**
>
> Through our partnership with Regrid, Shovels includes the Regrid parcel identifier alongside every permit in our nationwide dataset.
>
> The `address_id` in Shovels maps directly to the `ll_uuid` in Regrid, giving data teams a clean join between construction activity and parcel ownership, boundaries, and assessor attributes. No manual address matching. No county-by-county lookups.
>
> You can receive a direct, single-join path from construction activity to parcel ownership and boundary data. Read more about how to <a href="https://www.shovels.ai/blog/integrating-parcel-and-permit-data-in-partnership-with-regrid/" target="_blank">join building permit data with parcel data using the Regrid ID here</a>.

## How to Find an Assessor Parcel Number by Address

Here's the most common scenario: you have an address and you need the APN. Here's the step-by-step process:

1. Identify which county the address falls in
2. Search "[county name] assessor parcel search" in your browser
3. Find the official county assessor's website (look for a .gov domain)
4. Enter the street address in the search field
5. The results page will show the APN along with ownership details and assessment information

If the county portal isn't returning results (which happens more often than it should), try the county GIS map as a fallback. If you're looking up parcel or real estate data at scale, national data providers offer support for a variety of use cases. It's worth exploring your options.

> <a href="https://www.shovels.ai/contact" target="_blank">Contact us</a> to learn how the Shovels and Regrid datasets can work together for your use case. Shovels data is available via <a href="https://www.shovels.ai/api" target="_blank">API</a>, <a href="https://www.shovels.ai/data-feed" target="_blank">enterprise data feed</a>, and as <a href="https://www.shovels.ai/gis" target="_blank">ArcGIS hosted feature layers</a> for teams already working in the Esri ecosystem.

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is an Assessor Parcel Number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">An Assessor Parcel Number (APN) is a unique identifier assigned by the county assessor to each parcel of land in the public record. It connects the parcel to tax assessments, building permits, title documents, and ownership history. Depending on the jurisdiction, it may also be called a Parcel ID, PIN, Tax Parcel Number, or Parcel Identification Number.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How do I find my parcel number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">The fastest way to find a parcel number is to search the county assessor's website by property address. The APN also appears on property tax bills, recorded deeds, and title reports. For multiple properties or bulk lookups, a national parcel data provider like Regrid is more practical than going county by county.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How do I find an assessor parcel number by address?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Go to the assessor's website for the county where the property is located. Use the public parcel search tool to enter the street address. The results will include the APN along with ownership and assessed value information. If the county portal isn't working, try the county GIS map viewer as an alternative.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Is an APN the same as a parcel number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Yes. APN, Parcel Number, Parcel ID, and PIN all refer to the same thing: the unique identifier assigned to a parcel by the county assessor. The terminology varies by state and county, but the concept is identical everywhere.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Does an APN change when a property is sold?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">No. The APN stays with the parcel, not the owner. When a property sells, the APN remains the same. APNs only change when the physical parcel itself changes, such as when land is subdivided, merged, or boundary-adjusted through a legal process.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Where do I find the APN on a deed?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">The APN appears in the legal description section of a recorded deed, usually near the top of the document. It may be labeled "Assessor's Parcel Number," "APN," or "Tax Parcel ID." Title reports and closing packages will also include it.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Can I look up a parcel number using GPS coordinates?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Yes, using a county GIS map portal or a national parcel data provider. Most GIS portals allow you to click a location on the map and retrieve parcel details including the APN. Parcel data APIs from providers like Regrid also support coordinate-based lookups.</p>
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
      "name": "What is an Assessor Parcel Number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An Assessor Parcel Number (APN) is a unique identifier assigned by the county assessor to each parcel of land in the public record. It connects the parcel to tax assessments, building permits, title documents, and ownership history. Depending on the jurisdiction, it may also be called a Parcel ID, PIN, Tax Parcel Number, or Parcel Identification Number."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find my parcel number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The fastest way to find a parcel number is to search the county assessor's website by property address. The APN also appears on property tax bills, recorded deeds, and title reports. For multiple properties or bulk lookups, a national parcel data provider like Regrid is more practical than going county by county."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find an assessor parcel number by address?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Go to the assessor's website for the county where the property is located. Use the public parcel search tool to enter the street address. The results will include the APN along with ownership and assessed value information. If the county portal isn't working, try the county GIS map viewer as an alternative."
      }
    },
    {
      "@type": "Question",
      "name": "Is an APN the same as a parcel number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. APN, Parcel Number, Parcel ID, and PIN all refer to the same thing: the unique identifier assigned to a parcel by the county assessor. The terminology varies by state and county, but the concept is identical everywhere."
      }
    },
    {
      "@type": "Question",
      "name": "Does an APN change when a property is sold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The APN stays with the parcel, not the owner. When a property sells, the APN remains the same. APNs only change when the physical parcel itself changes, such as when land is subdivided, merged, or boundary-adjusted through a legal process."
      }
    },
    {
      "@type": "Question",
      "name": "Where do I find the APN on a deed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The APN appears in the legal description section of a recorded deed, usually near the top of the document. It may be labeled \"Assessor's Parcel Number,\" \"APN,\" or \"Tax Parcel ID.\" Title reports and closing packages will also include it."
      }
    },
    {
      "@type": "Question",
      "name": "Can I look up a parcel number using GPS coordinates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, using a county GIS map portal or a national parcel data provider. Most GIS portals allow you to click a location on the map and retrieve parcel details including the APN. Parcel data APIs from providers like Regrid also support coordinate-based lookups."
      }
    }
  ]
}
</script>
