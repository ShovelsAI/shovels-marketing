#!/usr/bin/env python3
"""
Populate faq_data.json with Customer Success blog post FAQ content.
"""

import json
from pathlib import Path


# Customer Success FAQ data from research agent a5f2640
CUSTOMER_SUCCESS_FAQS = {
    "content/posts/api-guide-1.md": {
        "insert_after": "Cheers!",
        "faqs": [
            {
                "q": "How do I authenticate with the Shovels V1 API?",
                "a": "You authenticate using header key-based authentication. First, get your API key by registering and logging in at app.shovels.ai. Then include your key in the HTTP header of each request using the format X-API-Key: YOUR_API_KEY_HERE."
            },
            {
                "q": "What are tags in the Shovels API and how do I use them?",
                "a": "Tags are how Shovels categorizes types of building activity (e.g., heat_pump, solar, reroof). You can use tags to filter permits or contractors by the type of work performed. The V1 API offers 33 unique tags, and you can list them all programmatically using the Get All Available Tags endpoint."
            },
            {
                "q": "What date format does the Shovels API use, and which date do the filters apply to?",
                "a": "The Shovels API uses the YYYY-MM-DD date format (e.g., 2023-08-01). The start_date and end_date filters are based on the permit's file date, which is when the permit was submitted to the jurisdiction."
            },
            {
                "q": "Can I look up detailed information about a specific permit or contractor?",
                "a": "Yes. Search results return internal Shovels IDs for permits and contractors. You can pass those IDs into the Get Permit by ID or Get Contractor by ID endpoints to retrieve full details including descriptions, dates, addresses, license numbers, and contact information."
            }
        ]
    },
    "content/posts/api-guide-2.md": {
        "insert_after": "We're here to help you succeed! Reach out to `support@shovels.ai` with any questions. We love seeing what our customers build with the API.",
        "faqs": [
            {
                "q": "What are the two main resources available through the Shovels V2 API?",
                "a": "The two main resources are Permits (official documents issued by cities or counties tracking construction and building alterations) and Contractors (skilled professionals who perform the permitted work). The API also provides Lists, Addresses, Meta, and Geography resources."
            },
            {
                "q": "What is a geo_id and what values can it take?",
                "a": "A geo_id is the location parameter used when searching for permits or contractors. It can be a state abbreviation (e.g., TX), a zip code (e.g., 78701), or a city or county identifier. For cities and counties, you need to look up their specific geo_id using the geography endpoints first."
            },
            {
                "q": "How do I filter permits by property type and work category?",
                "a": "Use the property_type parameter to filter by building type (e.g., residential, commercial, industrial) and the permit_tags parameter to filter by type of work (e.g., solar, hvac, reroof, kitchen_remodel). Both can be combined in a single search request."
            },
            {
                "q": "What is the minimum information required to search for permits?",
                "a": "At minimum, you need a date range (using the permit_from and permit_to parameters) and a location (using the geo_id parameter). You can optionally add property type and tag filters to narrow your results."
            }
        ]
    },
    "content/posts/app-guide-1.md": {
        "insert_after": "Check it out! [https://app.shovels.ai](https://app.shovels.ai)",
        "faqs": [
            {
                "q": "What is the Shovels app and how is it different from the API?",
                "a": "The Shovels app is a web application accessible on any desktop or mobile browser that lets you browse building permit and contractor data without needing any coding or API knowledge. It provides the same data as the API but through a visual, user-friendly interface."
            },
            {
                "q": "What are the three core data objects in the Shovels app?",
                "a": "The three core objects are addresses, permits, and contractors. They are all related: permits have addresses, contractors have permits, and therefore contractors also have addresses. You can search and profile each one in the app."
            },
            {
                "q": "How can I find contractors who work in my neighborhood using the Shovels app?",
                "a": "Use the Contractor Directory feature to search by zip code and permit type. The app finds contractors based on their actual permit history in your area, which is more reliable than review sites since it shows who has actually done permitted work in your neighborhood."
            },
            {
                "q": "Can I download data from the Shovels app?",
                "a": "Yes. Each table in the Shovels app includes a download feature that lets you export the data to a CSV file, which you can then use in other software products."
            }
        ]
    },
    "content/posts/gpt-guide-1.md": {
        "insert_after": "The Shovels AI Custom GPT is an easy way for anyone looking to access detailed, localized information on permits and contractors quickly. By following the steps outlined in this blog, you can quickly get the data you want.",
        "faqs": [
            {
                "q": "What is the Shovels AI Custom GPT and how does it work?",
                "a": "The Shovels AI Custom GPT is a tool built on ChatGPT that interacts with the Shovels API using natural language. Instead of writing code or API calls, you can type plain-English requests like Show me all roofing permits in zip 90210 and get detailed results on building permits and contractors."
            },
            {
                "q": "Do I need to know how to code to use the Shovels GPT?",
                "a": "No. The Shovels Custom GPT accepts natural language queries. You simply describe what you are looking for (permits, contractors, locations, dates) and the GPT handles the API interaction for you."
            },
            {
                "q": "What types of searches can I do with the Shovels Custom GPT?",
                "a": "You can search for building permits by type of work (e.g., roofing, pools, EV chargers), filter by state or zip code, set date ranges, and find contractors who specialize in specific types of work. The GPT covers data on over 113 million building permits and 3 million contractors across 48 states."
            },
            {
                "q": "What should I do if the GPT does not include contractor information in the results?",
                "a": "If the GPT returns permit data but does not list the associated contractors, simply ask it in a follow-up message. For example, type List the contractors too and the GPT will retrieve and display the contractor details."
            }
        ]
    },
    "content/posts/shovels-101-permit-statuses.md": {
        "insert_after": "Happy Building!",
        "faqs": [
            {
                "q": "What are the four permit statuses in the Shovels system?",
                "a": "The four statuses are: in_review (permit has been filed but not yet approved), active (permit is approved and work can proceed), final (work is completed and signed off by the jurisdiction), and inactive (the permit process has stalled due to failed inspections, expiration, or extended inactivity)."
            },
            {
                "q": "What dates correspond to each permit status in Shovels?",
                "a": "The in_review status is defined by the file_date (when the permit is filed). The active status is defined by the issue_date (when the permit is approved). The final status is defined by the final_date (when the jurisdiction signs off on completed work). The inactive status can occur at any point if the process stalls."
            },
            {
                "q": "What are start_date and end_date in the Shovels permit data?",
                "a": "These are derived dates created by Shovels for consistent date tracking. start_date is derived by coalescing file_date, issue_date, and final_date in that order. end_date uses the same fields in reverse order. Because of this, start_date and end_date can be the same value, and end_date may be populated even when a permit is still active. Use these fields together with the permit status for accurate analysis."
            },
            {
                "q": "Can a permit move back and forth between statuses?",
                "a": "Yes. A permit can move from active to inactive if the process stalls (for example, due to a failed inspection), and then return to active once the issue is resolved. The construction duration counter pauses during the inactive period and resumes when the permit becomes active again."
            }
        ]
    },
    "content/posts/shovels-101-permit-fields.md": {
        "insert_after": "Happy Digging!",
        "faqs": [
            {
                "q": "Why are so many fields blank or NULL on a Shovels permit record?",
                "a": "Shovels aggregates permit data from thousands of jurisdictions, each with different reporting requirements. To cover all possible fields from all jurisdictions, the schema includes many fields that will be irrelevant to any individual permit. Blank fields typically fall into categories like optional professional contacts, project-specific details unrelated to the permit type, commonly unfilled fields like job value, or derived metrics that require data not present on older records."
            },
            {
                "q": "What are the most important fields to look at on a Shovels permit?",
                "a": "The top fields are: file_date, permit_number, owner_name, residential (whether it is a commercial or residential property), jurisdiction, type, subtype, status, description, and the address fields (street, street_no, zipcode, city, state). If any of these are empty, you can contact Shovels support to investigate."
            },
            {
                "q": "Where can I find definitions for all the Shovels permit data fields?",
                "a": "The Shovels Data Dictionary is a publicly available spreadsheet with exhaustive breakdowns of all fields, variables, and parameters. It has multiple tabs covering permits, contractors, properties, and more."
            },
            {
                "q": "What are the different ways to access Shovels permit data?",
                "a": "There are three delivery methods: the Web App (codeless, browser-based access), the API (programmatic integration for your platform or product), and the enterprise Data Feed (full dataset access via your data warehouse or raw flat files)."
            }
        ]
    },
    "content/posts/shovels-101-address-permit-history.md": {
        "insert_after": "Happy Building!",
        "faqs": [
            {
                "q": "How do I look up the permit history for a specific address using the Shovels API?",
                "a": "It is a three-step process. First, use the Search Addresses endpoint to find and confirm the address. Second, use the Permits by Address endpoint with the address details to get a list of permit IDs. Third, use the Permits by ID endpoint to retrieve the full details of each permit."
            },
            {
                "q": "What format should the address be in when querying the API?",
                "a": "Use %20 to denote spaces in the address string. The address components (street number, street name, city, state, zip code) are passed as separate parameters joined with the & operator. The addresses returned by Shovels are formatted according to USPS standards."
            },
            {
                "q": "What should I do if my address does not appear in the Shovels search results?",
                "a": "There are several possible reasons: the address may not have any permits on record, the jurisdiction may not have digitized its permits yet, or the address may not be in Shovels' coverage area. You can check the Shovels Coverage Map to see available jurisdictions, or email support@shovels.ai for help."
            },
            {
                "q": "Can I retrieve multiple permits at once from the API?",
                "a": "Yes. The Permits by ID endpoint accepts a string array of permit IDs, allowing you to request multiple permits in a single API call by adding an &id=string clause for each additional permit ID."
            }
        ]
    },
    "content/posts/shovels-101-maximizing-shovels-online.md": {
        "insert_after": "We hope that this tutorial is helpful, and Happy Digging!",
        "faqs": [
            {
                "q": "What are the main use cases for Shovels Online?",
                "a": "The main use cases are generating homeowner leads (finding addresses with permit activity that signals buyer intent), generating contractor leads (finding contractors by experience level and market area), and derivative analysis like permit approval timing and resident demographics."
            },
            {
                "q": "How do I build a high-quality search on Shovels Online?",
                "a": "Start by choosing your geography scale (state level for niche project types, zip code for common ones). Decide whether you are searching for permits or contractors based on your target persona. Apply key filters like minimum market value, lot size, or permit description keywords. Then spot-check results by clicking View Details on a few entries to verify accuracy."
            },
            {
                "q": "Is there a limit on how many records I can download from Shovels Online?",
                "a": "The Download List button caps at 1,000 rows per CSV export. To get more, adjust your filters slightly (such as changing geography) to generate a new set of 1,000 rows, then combine and deduplicate. For larger-scale needs, the Shovels API is recommended."
            },
            {
                "q": "Can I save my search filters in Shovels Online for later use?",
                "a": "Yes. Shovels Online includes a Saved Filters feature that lets you save your exact search parameters so you can re-run the same query later without rebuilding it. You can also save individual permits, contractors, or geographies as Saved Profiles for quick future access."
            }
        ]
    },
    "content/posts/address-permit-history.md": {
        "insert_after": "Happy Digging!",
        "faqs": [
            {
                "q": "Why doesn't every address have a permit history in Shovels?",
                "a": "There are three main reasons: (1) the local jurisdiction may not require a permit for the type of work done, (2) even where permits are required, enforcement varies and some work is done without permits, and (3) the jurisdiction may not have digitized its permit records or made them available online yet."
            },
            {
                "q": "Do all jurisdictions require permits for the same types of projects?",
                "a": "No. There are no standardized nationwide rules mandating which work requires a permit. Requirements vary dramatically from one jurisdiction to another. Some states like Massachusetts have detailed requirements, while some rural counties may have minimal or no permitting requirements at all."
            },
            {
                "q": "How far back does Shovels permit data go?",
                "a": "Shovels generally has approximately 20 years of permit history where available, depending on how far back each jurisdiction has digitized and uploaded its records."
            },
            {
                "q": "What is Shovels doing to improve data completeness?",
                "a": "Shovels is pursuing three strategies: improving proprietary LLMs to speed up permit data processing and delivery, building relationships with local jurisdiction offices to increase digitization through direct records requests, and improving transparency about data coverage through a public Coverage Dashboard."
            }
        ]
    },
    "content/posts/top-5-derived-metrics.md": {
        "insert_after": "If you have any questions, or want a sample dataset for your team to explore, [get in touch today](mailto:sales@shovels.ai)!",
        "faqs": [
            {
                "q": "What are derived metrics in Shovels?",
                "a": "Derived metrics are data points that Shovels calculates by combining information from the public record. They are not directly reported on individual permits but are extrapolated from underlying data, such as dates, inspection results, and permit counts."
            },
            {
                "q": "What is the difference between Average Approval Duration and Average Construction Duration?",
                "a": "Average Approval Duration measures the time between when a permit is filed and when it is approved (issue_date minus file_date). Average Construction Duration measures the broader time between when a permit is filed and when it is marked as finaled (final_date minus file_date), encompassing the entire construction process."
            },
            {
                "q": "How is Average Inspection Pass Rate calculated?",
                "a": "It is the percentage of inspections passed compared to total inspections made, multiplied by 100 (so 75% is returned as 75). A higher rate, especially as a contractor's permit count increases, indicates a smoother construction process."
            },
            {
                "q": "What does the First Seen Date metric tell me?",
                "a": "For contractors, it shows the first time they appear in the Shovels system on a permit, which is useful for identifying new contractors entering the market. For permits, it shows when the permit was added to the Shovels platform, which helps you understand digitization delays or when historical data was backfilled."
            },
            {
                "q": "Where can I access these derived metrics?",
                "a": "These metrics are available across the entire Shovels platform: through Shovels Online (the web application and dashboard), the API (for programmatic access), and the enterprise data feed."
            }
        ]
    },
    "content/posts/shovels-online-gtm.md": {
        "insert_after": "**Want to explore how Shovels can power your GTM motion? [Let's talk.](http://www.shovels.ai/)**",
        "faqs": [
            {
                "q": "What go-to-market strategies can I execute using Shovels Online?",
                "a": "The top five strategies are: (1) direct mail campaigns to homeowners based on permit activity, (2) post-installation maintenance outreach to homeowners with existing systems, (3) competitor intelligence by analyzing competitor contractor activity, (4) email outreach and lead nurturing using homeowner contact data from permits, and (5) enterprise-grade custom reporting for larger teams."
            },
            {
                "q": "How can I use Shovels Online for direct mail campaigns?",
                "a": "Search for homeowners by permit type and date range in your market area. For example, find addresses where HVAC systems were installed 10-15 years ago (likely due for replacement), or find addresses with no HVAC permit history. Download the results with contact details and use them for targeted mailers."
            },
            {
                "q": "Does Shovels Online provide homeowner email addresses?",
                "a": "Yes, where available. Shovels Online provides verified personal and business emails for homeowners, which you can use for email campaigns and CRM enrichment. You can also contact Shovels support for help merging homeowner emails with your existing lead lists."
            },
            {
                "q": "How do I use Shovels Online for competitor analysis?",
                "a": "Search for contractors in your area and analyze their project activity, volume, busy seasons, and the types of work described in their permits. Use these insights to differentiate your service offerings and pricing from the competition."
            },
            {
                "q": "Can I save and re-run searches in Shovels Online on a regular basis?",
                "a": "Yes. Once you have built a search with your desired filters, you can save it and re-run it on a monthly basis when the Shovels platform data refreshes, ensuring you are always working with the freshest available data."
            }
        ]
    }
}


def main():
    """Merge Customer Success FAQ data into faq_data.json."""
    data_file = Path(__file__).parent / "faq_data.json"

    # Load existing data
    existing_data = {}
    if data_file.exists():
        with open(data_file) as f:
            existing_data = json.load(f)

    # Merge
    merged_data = {**existing_data, **CUSTOMER_SUCCESS_FAQS}

    # Write back
    with open(data_file, 'w') as f:
        json.dump(merged_data, f, indent=2)

    print(f"✅ Updated {data_file}")
    print(f"📊 Total entries: {len(merged_data)}")
    print(f"🆕 Customer Success entries added: {len(CUSTOMER_SUCCESS_FAQS)}")


if __name__ == "__main__":
    main()
