#!/usr/bin/env python3
"""
Populate faq_data.json with Landing Page FAQ content.
"""

import json
from pathlib import Path


# Landing Page FAQ data from research agent a68a7de
LANDING_PAGE_FAQS = {
    "content/pages/audiences.md": {
        "insert_after": "</div>",
        "faqs": [
            {
                "q": "What kind of data does Shovels use to build audiences?",
                "a": "Shovels uses building permit data, which provides deterministic information on home improvement activity. This data shows what work homeowners have done, when it was completed, and what type of project it was, allowing for precise audience targeting."
            },
            {
                "q": "What types of audiences can I create with Shovels?",
                "a": "You can create audiences for a wide range of segments, including homeowners in-market for solar panel maintenance, home warranty services, mortgage refinancing, kitchen appliances, furniture and windows, and electric appliance adoption (such as EVs, heat pumps, and battery storage)."
            },
            {
                "q": "How does Shovels help me reach homeowners at the right time?",
                "a": "Building permits include timing data that shows when projects were completed. Shovels uses this to identify homeowners who are likely in-market right now -- for example, targeting solar panel owners whose installations are aging and may need maintenance, or homeowners who haven't remodeled their kitchen in over 10 years."
            },
            {
                "q": "Can I use Shovels audiences for ad campaigns?",
                "a": "Yes. Shovels is designed to help you run ad campaigns by providing building permit-based audience segments. You can target homeowners with ads for products and services that match their recent or upcoming home improvement needs."
            },
            {
                "q": "How does Shovels identify homeowners who might need financing?",
                "a": "Shovels identifies homeowners who have active construction projects, since construction is expensive and financing isn't always arranged upfront. These homeowners are strong prospects for mortgage refinancing, home equity lines of credit, and other financing products."
            }
        ]
    },
    "content/pages/building-materials.md": {
        "insert_after": "</div>",
        "faqs": [
            {
                "q": "How does Shovels help building material suppliers find contractors?",
                "a": "Shovels provides nationwide building permit data that lets you segment contractors by revenue, service area, and specialty. This enriches your lead program with unique insights on both commercial and residential builders, and the data integrates directly with Salesforce and HubSpot."
            },
            {
                "q": "Can Shovels help prevent fraudulent purchases?",
                "a": "Yes. Shovels can verify that a prospective customer is a licensed contractor by checking their registration information against a database of nearly 3 million contractors. This helps prevent unauthorized or fraudulent purchases of building materials."
            },
            {
                "q": "How can building material distributors use Shovels for credit decisions?",
                "a": "Shovels provides trailing revenue, permit history, and service area detail for contractors. This data helps you assess credit risk when deciding whether to open a line of credit for a contractor account."
            },
            {
                "q": "What contractor information does Shovels provide?",
                "a": "Shovels offers detailed contractor profiles including revenue estimates, permit history, service area coverage, employee contact information, and license verification data. This helps your sales team qualify leads and close more accounts."
            },
            {
                "q": "Which companies use Shovels for building materials sales?",
                "a": "Shovels is trusted by companies including Schneider Electric, Beacon, Harvest Thermal, Boldr, and Generator Supercenter."
            }
        ]
    },
    "content/pages/home-services.md": {
        "insert_after": "</div>",
        "faqs": [
            {
                "q": "What makes Shovels the most complete contractor database in America?",
                "a": "Shovels combines two authoritative data sources -- building permits and state contractor license directories -- to create the most comprehensive view of the construction labor market. The data covers 37 states and includes license classifications, permit details, and contact information."
            },
            {
                "q": "Who uses Shovels for contractor data?",
                "a": "Leading home services companies including Angi, Thumbtack, Houzz, and Housecall Pro trust Shovels to find, verify, and enrich contractor data at scale."
            },
            {
                "q": "How does Shovels standardize contractor license data?",
                "a": "Shovels normalizes over 3,000 messy contractor classifications from 37 different states down to approximately a dozen clean, standardized classifications. The original classifications are also provided alongside the standardized versions."
            },
            {
                "q": "How is the data delivered?",
                "a": "Shovels supports all major cloud storage providers (AWS, Azure, GCP) and can push data to Snowflake, BigQuery, and Databricks. Data transfers are done securely via SFTP and HTTPS. Custom reports can be generated in whatever schema and file format your data team prefers."
            },
            {
                "q": "How often is the contractor data updated?",
                "a": "The contractor state license files are refreshed monthly, pulled directly from the source, ensuring the data stays current and accurate."
            }
        ]
    }
}


def main():
    """Merge Landing Page FAQ data into faq_data.json."""
    data_file = Path(__file__).parent / "faq_data.json"

    # Load existing data
    existing_data = {}
    if data_file.exists():
        with open(data_file) as f:
            existing_data = json.load(f)

    # Merge
    merged_data = {**existing_data, **LANDING_PAGE_FAQS}

    # Write back
    with open(data_file, 'w') as f:
        json.dump(merged_data, f, indent=2)

    print(f"✅ Updated {data_file}")
    print(f"📊 Total entries: {len(merged_data)}")
    print(f"🆕 Landing page entries added: {len(LANDING_PAGE_FAQS)}")


if __name__ == "__main__":
    main()
