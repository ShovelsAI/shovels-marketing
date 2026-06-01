title: What Is a Parcel Map?
subtitle: How county parcel maps work, what they show, and where to find them
date: 2026-06-01
modified: 2026-06-01
category: Customer Success
tag1: Parcels
tag2: Real Estate
tags: parcel map, parcel boundaries, lot dimensions, parcels data, parcel map vs plat map
authors: Ruoji Tang
author_image: /theme/images/team/Ruoji.svg
author_title: Senior Marketing Manager
slug: what-is-a-parcel-map
summary: A parcel map is an official county record showing land parcel boundaries and APNs. Learn what parcel maps include, how to read one, and where to find it.
image: /images/blog_images/what-is-a-parcel-map-hero.png

---

Every piece of land in the US has a legal boundary on record, and a parcel map is where you find it.

County parcel maps are the official geographic index of how land is divided within a jurisdiction. Whether you're researching a single address or building a property data pipeline, the parcel map is the layer that turns tax records and legal descriptions into something you can actually see and navigate.

> **Key Takeaways**
>
> - **What it is**: A parcel map is an official county document showing parcel boundaries, dimensions, and Assessor Parcel Numbers (APNs) for every piece of land in a jurisdiction.
> - **What it shows**: Parcel boundaries, lot dimensions, APNs, street rights-of-way, and neighboring parcels. Some jurisdictions add zoning and easement overlays.
> - **It's not the same as a plat map**: A plat map is a one-time subdivision document; a parcel map is the county's ongoing, jurisdiction-wide record of all land divisions.
> - **Where to find one**: County GIS portal, county assessor's office, or national parcel data providers.
> - **Why it matters for data work**: The APN on a parcel map is the join key connecting permit history, ownership records, and zoning decisions across data sources.
> - **Join Shovels permit data with parcel data**: Shovels includes the Regrid parcel identifier alongside every permit record, so you can connect construction activity to parcel boundaries without manual county lookups.

## What Is a Parcel Map?

A **parcel map** is an official county document that defines and displays the boundaries of individual <a href="https://www.shovels.ai/blog/what-is-a-parcel-real-estate/" target="_blank">parcels of land</a> within a jurisdiction. Each parcel on the map corresponds to a distinct legal unit of land, identified by its <a href="https://www.shovels.ai/blog/what-is-assessor-parcel-number/" target="_blank">Assessor Parcel Number (APN)</a>, and shown with its boundary lines, dimensions, and relationship to adjacent parcels and streets.

Parcel maps are maintained by the county assessor or recorder's office and serve as the authoritative record of how land is divided in that jurisdiction. They're used in property transactions, permit applications, title research, zoning analysis, and infrastructure planning. Some counties call them tax maps, so-called because the document is maintained primarily for property tax purposes, but the underlying boundaries and APNs are the same.

Unlike a satellite image or street map, a parcel map shows the legal land record. Two adjacent properties with identical houses appear as two distinct units, each with its own APN, boundaries, and history.

## What Does a Parcel Map Show?

A standard parcel map includes several core elements.

**Parcel boundaries** are the foundation of the map. Each parcel is outlined according to the legal description recorded with the county. Boundary lines may follow streets, natural features, or surveyed bearings and distances from the original subdivision.

![Parcel boundaries on a parcel map of San Bernardino County]({static}/images/blog_images/what-is-a-parcel-map-san-bernardino-boundaries.png)
*Parcel boundaries on a parcel map of San Bernardino County. Source: <a href="https://open.sbcounty.gov/" target="_blank">San Bernardino County Open Portal</a>*

**Assessor Parcel Numbers (APNs)** are labeled on or adjacent to each parcel. The APN is the unique identifier that connects the parcel to tax records, building permits, title documents, and ownership history. It's the key field for joining parcel data to any other property dataset.

**Dimensions and area** are typically shown for each parcel, either directly on the map or in an accompanying data table. These reflect legal dimensions, not necessarily what you'd measure on the ground.

**Street names and rights-of-way** provide geographic context. Public roads, alleys, and easements appear as distinct features separate from privately held parcels.

**Adjoining parcel references** let you navigate between parcels. Most county parcel map systems organize parcels into map books or tiles, each assigned a book and page number (this is sometimes called a parcel map number.) In older paper-based systems, this number was the physical filing reference for the subdivision document that established those boundaries. In modern GIS systems, it's embedded in parcel history records.

Some jurisdictions layer in zoning designations, flood zone boundaries, or utility easements on top of the base parcel map, though these are usually maintained as separate GIS overlays.

## Parcel Map vs. Plat Map

A parcel map and a plat map are related but not the same thing.

A plat map (also called a subdivision plat) is created when a larger piece of land is formally divided into multiple parcels. It documents the new lot layout, street dedications, easements, and dimensions for that specific subdivision. A plat map is recorded once, at the moment of subdivision, and becomes part of the permanent land record.

A parcel map is ongoing. It reflects the current state of all land divisions in the jurisdiction, incorporating new plats as they're recorded and updating when parcels are split, merged, or otherwise altered. The plat is one input into the parcel map; the parcel map is the living record built from all of them.

In some states, particularly California, "parcel map" also has a specific legal meaning: the subdivision method used for smaller splits of four or fewer parcels, as distinct from a tract map used for larger developments. In that context, a parcel map is itself a recorded document. For most everyday purposes, though, "parcel map" means the county's GIS-based layer showing all current land divisions across the jurisdiction.

## How to Read a Parcel Map

Reading a parcel map is straightforward once you know what to look for.

**Start with the APN.** Every parcel is labeled with its APN. This number is the key to the parcel's full public record: ownership, assessed value, permit history, and zoning classification. Note it before anything else.

**Trace the boundaries.** The lines around each parcel define its legal extent. On a digital GIS parcel map, click a parcel to see dimensions and data in the sidebar panel. On a paper or PDF map, boundaries are drawn with bearings and distances from the original survey.

**Note the context.** Streets, adjacent parcels, and open space give you geographic orientation. Check neighboring parcels if you're researching easements, access rights, or shared boundaries.

**Cross-reference with other records.** A parcel map is most useful paired with other data. The APN connects to the assessor's database for ownership and valuation. The parcel boundary maps to permit history. A separate zoning layer shows what uses are allowed on the site.

**Check parcel history for complex properties.** When a parcel has been subdivided, merged, or had boundary adjustments, earlier APNs are retired and new ones issued. Most county GIS systems include a parcel history layer showing how current parcels relate to prior ones.

> **Did you know?** Through our partnership with <a href="https://regrid.com/" target="_blank">Regrid</a>, Shovels includes the Regrid parcel identifier alongside every permit record in our nationwide dataset. The `address_id` field in Shovels maps directly to the `ll_uuid` in Regrid, giving data teams a direct join between construction activity and parcel boundaries, ownership, and assessor attributes.

## How to Find a Parcel Map

There are three reliable ways to access parcel map data.

**County GIS portal.** Most counties publish a free interactive parcel map viewer online. Search "[county name] GIS parcel map" or "[county name] parcel viewer" in your browser. These portals let you search by address or APN and display parcel boundaries over an aerial or street map base. This is the best starting point for single-property research. Update cadence varies: some counties refresh their parcel layer daily, others weekly or monthly, so check when the portal data was last updated for time-sensitive work.

**County assessor's office.** The assessor maintains the official parcel record. Many offices have moved their maps online, but for older records or historical research, the office itself can provide physical map books or archived documents.

**National parcel data providers.** For anyone working across counties or building data pipelines, manual lookups don't scale. National parcel data providers like <a href="https://regrid.com/" target="_blank">Regrid</a> aggregate parcel records from thousands of counties into a standardized, queryable dataset. You can search by address, coordinates, owner name, or APN across the entire country, and receive data through an API or bulk download.

> Shovels connects permit history, contractor records, and parcel identifiers across 1,800+ jurisdictions and 159M+ parcels nationwide. <a href="https://www.shovels.ai/contact" target="_blank">Contact us</a> to discuss how parcel and permit data can support your workflow.

<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is a parcel map?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel map is an official county document showing the boundaries, dimensions, and Assessor Parcel Numbers (APNs) of individual land parcels within a jurisdiction. It's the geographic layer of the public land record, updated as parcels are created, split, or merged.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What does a parcel map show?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel map shows parcel boundaries, lot dimensions, APNs, street names and rights-of-way, and the relationship between adjacent parcels. Some jurisdictions layer in zoning designations, easements, or flood zone boundaries as additional overlays.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is the difference between a parcel map and a plat map?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A plat map is a one-time document recorded when land is formally subdivided. A parcel map is the county's ongoing, jurisdiction-wide record incorporating all subdivisions over time. In California and some other states, "parcel map" also has a specific legal meaning for small-lot splits of four or fewer parcels.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How do I find a parcel map for a specific property?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">The fastest route is the county GIS parcel viewer. Search for the county's GIS portal, enter the property address or APN, and parcel boundaries and details will appear. The county assessor's office and national providers like Regrid are also reliable sources, especially for bulk or multi-county research.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Is a parcel map the same as a tax map?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Largely yes. Tax map is another term some counties use for their parcel maps, emphasizing that the document is maintained for property tax purposes. The boundaries and APNs are the same. Some jurisdictions maintain a separate GIS layer that updates more frequently than the official tax map, but they draw from the same underlying data.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Can I use a parcel map to find permit history?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel map gives you the APN, which is the key to permit history. Once you have the APN, you can look up all permits filed for that parcel through the county building department portal or through a nationwide permit data source like Shovels.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">What is a parcel map number?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">A parcel map number typically refers to the book and page number of the recorded subdivision document that established the parcel's current boundaries. In modern GIS systems, this is embedded in parcel history records. In older paper-based systems, it was the physical filing reference for the original map.</p>
          </dd>
        </div>
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">How often are parcel maps updated?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">County GIS parcel layers update when changes are officially recorded: new subdivisions, lot line adjustments, or mergers. Some counties update daily; others do weekly or monthly batches. For time-sensitive work, verify data currency directly with the county or use a national parcel provider that publishes its update cadence.</p>
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
      "name": "What is a parcel map?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel map is an official county document showing the boundaries, dimensions, and Assessor Parcel Numbers (APNs) of individual land parcels within a jurisdiction. It's the geographic layer of the public land record, updated as parcels are created, split, or merged."
      }
    },
    {
      "@type": "Question",
      "name": "What does a parcel map show?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel map shows parcel boundaries, lot dimensions, APNs, street names and rights-of-way, and the relationship between adjacent parcels. Some jurisdictions layer in zoning designations, easements, or flood zone boundaries as additional overlays."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between a parcel map and a plat map?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A plat map is a one-time document recorded when land is formally subdivided. A parcel map is the county's ongoing, jurisdiction-wide record incorporating all subdivisions over time. In California and some other states, \"parcel map\" also has a specific legal meaning for small-lot splits of four or fewer parcels."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find a parcel map for a specific property?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The fastest route is the county GIS parcel viewer. Search for the county's GIS portal, enter the property address or APN, and parcel boundaries and details will appear. The county assessor's office and national providers like Regrid are also reliable sources, especially for bulk or multi-county research."
      }
    },
    {
      "@type": "Question",
      "name": "Is a parcel map the same as a tax map?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Largely yes. Tax map is another term some counties use for their parcel maps, emphasizing that the document is maintained for property tax purposes. The boundaries and APNs are the same. Some jurisdictions maintain a separate GIS layer that updates more frequently than the official tax map, but they draw from the same underlying data."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use a parcel map to find permit history?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel map gives you the APN, which is the key to permit history. Once you have the APN, you can look up all permits filed for that parcel through the county building department portal or through a nationwide permit data source like Shovels."
      }
    },
    {
      "@type": "Question",
      "name": "What is a parcel map number?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A parcel map number typically refers to the book and page number of the recorded subdivision document that established the parcel's current boundaries. In modern GIS systems, this is embedded in parcel history records. In older paper-based systems, it was the physical filing reference for the original map."
      }
    },
    {
      "@type": "Question",
      "name": "How often are parcel maps updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "County GIS parcel layers update when changes are officially recorded: new subdivisions, lot line adjustments, or mergers. Some counties update daily; others do weekly or monthly batches. For time-sensitive work, verify data currency directly with the county or use a national parcel provider that publishes its update cadence."
      }
    }
  ]
}
</script>
