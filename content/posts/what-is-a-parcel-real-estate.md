title: What Is a Parcel in Real Estate? A Basic Guide
subtitle: Understand what a parcel is, how Assessor's Parcel Numbers work, and why parcel data matters for permits, due diligence, and property records.
date: 2026-05-12
modified: 2026-05-12
category: Customer Success
tag1: Parcels
tag2: Real Estate
tags: parcel, APN, assessor parcel number, parcel map, building permits, property records, real estate data
authors: Ruoji Tang
author_image: /theme/images/team/Ruoji.svg
author_title: Senior Marketing Manager
slug: what-is-a-parcel-real-estate
summary: Learn what a parcel is in real estate, how APNs and parcel maps work, and how parcel data connects to building permits, ownership records, and property due diligence.
image: /images/blog_images/what-is-a-parcel-real-estate-hero.png

---

If you've spent any time working with property records, building permits, or site selection data, you've run into the concept of a "parcel." It shows up in county databases, GIS layers, permit applications, and title documents. But what a parcel actually is, and how it's structured as a record, is less obvious than it seems.

> **Key Takeaways**
>
> - A parcel is a legally defined unit of land with fixed boundaries, recorded ownership, and a unique identifier assigned by the county assessor
> - The Assessor's Parcel Number (APN) is the canonical key connecting a parcel across permits, title, tax, and utility records
> - Parcel data supports site selection, pre-acquisition due diligence, market analysis, and property data pipelines
> - Shovels includes the Regrid ID in its permit schema, allowing developers to join permit history and parcel ownership with a single shared key

## What Is a Parcel in Real Estate?

A **parcel** is a legally defined unit of land with fixed boundaries, recorded ownership, and a unique identifier assigned by the county. It is the fundamental unit of property in the public record system. Every property transaction, tax assessment, and building permit traces back to a parcel.

Parcels are not defined by what sits on the land. A parcel can contain a house, a warehouse, a parking lot, or nothing at all. What defines it is the legal boundary and the county's record of it.

## What Makes a Parcel Official?

A parcel becomes official when it is recorded by the county assessor. This typically happens when land is subdivided, merged, or adjusted through a legal process. Once the change is recorded, the assessor creates or updates a parcel record in the county's property database.

That record includes:

- A legal description of the property boundaries
- A recorded deed
- Ownership information
- A unique parcel identifier

The identifier is called the Assessor's Parcel Number (APN). The APN is the main key used to connect the parcel to permits, title documents, tax assessments, and other public records. While APN formats vary by county, the purpose is the same everywhere.

Each parcel also has a GIS boundary polygon stored in the county's mapping system. This polygon defines the parcel's legal footprint and is updated whenever parcels are split, merged, or otherwise changed.

## Parcel Boundaries and Parcel Maps

Parcel maps are visual representations of these GIS boundaries. They show exactly where one parcel ends and another begins. County assessors publish these maps through their GIS portals, but formats and update schedules differ widely.

![Example of a parcel map from San Diego Geographic Information Source]({static}/images/blog_images/what-is-a-parcel-real-estate-parcel-map.png)
*Example of a parcel map from <a href="https://www.sangis.org/" target="_blank">San Diego Geographic Information Source</a>.*

Because every county manages its own data, working with parcel information at a national scale can be difficult. Providers like <a href="https://regrid.com/" target="_blank">Regrid</a> solve this by collecting parcel data from thousands of jurisdictions, standardizing the fields, and assigning stable identifiers that remain consistent even when county-issued APNs change. This is especially useful when you need to track a property over time across multiple datasets.

One thing worth knowing: parcel boundaries in consumer mapping tools like Google Maps or Google Earth are often approximate or missing entirely. For legal or analytical work, the authoritative source is the county GIS portal or a specialized parcel data provider.

## How Parcels Connect to Building Permits

Every building permit is filed against a parcel. Whether the work involves a roof replacement, a new HVAC system, or a ground-up development, the permit is tied to the parcel where the work takes place.

This makes the parcel the natural join key for any serious property data workflow. If you want to:

- Review the construction history of a property,
- Identify open or expired permits,
- Investigate regulatory risk before an acquisition, or
- Track development activity over time,

you are almost always working at the parcel level.

<a href="https://www.shovels.ai/" target="_blank">Shovels</a> processes over 180 million building permits nationwide. Through our partnership with <a href="https://regrid.com/" target="_blank">Regrid</a>, we are able to include the Regrid ID in every permit record. This gives customers a direct way to connect permit activity with parcel ownership and boundary data using a single shared identifier, without manual address matching.

For data teams building property intelligence pipelines, this makes a difference. The `address_id` in Shovels maps to the `ll_uuid` in Regrid, giving you a clean bridge between construction activity and the underlying parcel record.

## How Developers and Investors Use Parcel Data

For anyone doing serious property work, parcel data is not just background infrastructure. It is an active part of the workflow. Here are a few common applications:

**Site selection**: Parcel data helps identify land based on size, ownership, zoning, and proximity to other parcels. It is especially important when assembling multiple parcels for a larger project.

**Pre-acquisition due diligence**: Permit history, joined with parcel data, can reveal unpermitted additions, open violations, expired permits, and incomplete work that may not be obvious during a site visit.

**Market analysis**: Linking permit activity with parcel-level ownership changes lets you track development pressure in a submarket before it becomes visible in price data. New ownership combined with a run of permits usually indicates that a site is being repositioned.

**Risk and compliance**: Parcels with mismatches between the assessed improvement value and the permit record usually highlight issues. Parcels where the current use differs from permitted use are also worth a second look.

**Data pipelines**: For proptech companies and data teams, parcel identifiers provide the link between permit data, ownership records, boundaries, and assessor attributes at scale.

> Shovels data is available via <a href="https://www.shovels.ai/api" target="_blank">API</a>, <a href="https://www.shovels.ai/data-feed" target="_blank">enterprise data feed</a>, and as <a href="https://www.shovels.ai/gis" target="_blank">ArcGIS hosted feature layers</a> for teams already working in the Esri ecosystem. <a href="https://www.shovels.ai/contact" target="_blank">Contact us</a> to discuss how the Shovels and Regrid datasets can work together for your use case.

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is a parcel in real estate?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel is a legally defined unit of land recorded by the county assessor, with fixed boundaries, a unique identification number, and recorded ownership. It is the base unit for property taxes, title records, and building permits.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is a parcel ID number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel ID, also called an Assessor's Parcel Number or APN, is a unique identifier assigned by the county assessor to each parcel in the public record. It is the key used to link a parcel across permit records, tax assessments, and title documents. APN formats vary by county and state.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How do parcel maps work?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel map shows the legal boundaries of individual parcels as a GIS layer, sourced from county assessor data. Providers like Regrid standardize these maps into a nationwide dataset with consistent formatting and persistent parcel identifiers. Parcel boundaries in consumer mapping tools are often approximate; dedicated parcel data providers give you the accurate legal footprint.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How are parcels used in building permits?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Every building permit is filed against a parcel. The parcel ID connects the permit to the property's ownership record, tax assessment, and physical boundary. Reviewing the permit history on a parcel is a standard part of real estate due diligence, letting buyers and developers understand what work has been done and whether it was properly permitted.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How do Shovels and Regrid work together?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Shovels has added Regrid's universal parcel identifier, the Regrid ID, to its nationwide permit dataset. This allows joint customers to join Shovels permit data with Regrid parcel ownership and boundary data using a single shared key. The integration is available through the Shovels API, enterprise data feed, and as ArcGIS hosted feature layers. <a href="https://www.shovels.ai/blog/integrating-parcel-and-permit-data-in-partnership-with-regrid/" target="_blank">Find out more here</a>.</p>
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
      "name": "What is a parcel in real estate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel is a legally defined unit of land recorded by the county assessor, with fixed boundaries, a unique identification number, and recorded ownership. It is the base unit for property taxes, title records, and building permits."
      }
    },
    {
      "@type": "Question",
      "name": "What is a parcel ID number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel ID, also called an Assessor's Parcel Number or APN, is a unique identifier assigned by the county assessor to each parcel in the public record. It is the key used to link a parcel across permit records, tax assessments, and title documents. APN formats vary by county and state."
      }
    },
    {
      "@type": "Question",
      "name": "How do parcel maps work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel map shows the legal boundaries of individual parcels as a GIS layer, sourced from county assessor data. Providers like Regrid standardize these maps into a nationwide dataset with consistent formatting and persistent parcel identifiers. Parcel boundaries in consumer mapping tools are often approximate; dedicated parcel data providers give you the accurate legal footprint."
      }
    },
    {
      "@type": "Question",
      "name": "How are parcels used in building permits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every building permit is filed against a parcel. The parcel ID connects the permit to the property's ownership record, tax assessment, and physical boundary. Reviewing the permit history on a parcel is a standard part of real estate due diligence, letting buyers and developers understand what work has been done and whether it was properly permitted."
      }
    },
    {
      "@type": "Question",
      "name": "How do Shovels and Regrid work together?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Shovels has added Regrid's universal parcel identifier, the Regrid ID, to its nationwide permit dataset. This allows joint customers to join Shovels permit data with Regrid parcel ownership and boundary data using a single shared key. The integration is available through the Shovels API, enterprise data feed, and as ArcGIS hosted feature layers."
      }
    }
  ]
}
</script>
