#!/usr/bin/env python3
"""
Script to batch-add FAQ sections and schema to blog posts and landing pages.
Uses the FAQ content drafted by research agents.
"""

import json
import re
from pathlib import Path

# FAQ data structured by file
FAQ_DATA = {
    "content/posts/permit-jurisdiction-file.md": {
        "insert_after": 'Grab it [on Kaggle](https://www.kaggle.com/datasets/rbucks/building-permit-jurisdictions-in-the-united-states){:target="_blank"} or [download the CSV]({static}/images/jurisdiction_mappings.csv).',
        "faqs": [
            {
                "q": "What is a building permit jurisdiction (AHJ)?",
                "a": "An AHJ, or authority-having jurisdiction, is the government entity responsible for issuing building permits in a given area. Some cities issue their own permits, while others delegate permitting to the county. Shovels identified over 10,000 such jurisdictions across the United States."
            },
            {
                "q": "How do I know if my city issues its own building permits or if the county handles them?",
                "a": "If a city appears on the Shovels jurisdiction list, it issues its own building permits. If a city is not on the list, the county is likely the authority-having jurisdiction for building permits in that area."
            },
            {
                "q": "Where can I download the list of building permit jurisdictions?",
                "a": "The dataset is available for free on Kaggle at the Building Permit Jurisdictions in the United States dataset page, or you can download the CSV file directly from the Shovels website."
            },
            {
                "q": "Why does Pennsylvania have so many building permit jurisdictions compared to other states?",
                "a": "Pennsylvania has 1,575 permit jurisdictions, far more than any other state, and roughly 3 times as many as Ohio despite having a similar population. The exact reason for this is unclear, but it stands out as a significant outlier, with 12.15 jurisdictions per 100,000 residents compared to the national average of about 10 jurisdictions per county."
            }
        ]
    },
    "content/posts/spi-q1-2025.md": {
        "insert_after": "This is exactly why having detailed permit data is so valuable. Whether you're spotting local growth opportunities, keeping tabs on what other builders are up to, or figuring out how big-picture changes affect your neighborhood — we're here to help you make smart choices in this exciting 2025 construction landscape!",
        "faqs": [
            {
                "q": "How many building permits were issued in the US in Q1 2025?",
                "a": "The US saw approximately 2.02 million building permits in Q1 2025, which is a 6.1% decline from Q4 2024's 2.16 million. While this represents the third consecutive quarter of decreases since the peak in Q2 2024, the rate of decline is slowing compared to the 12.5% drop between Q3 and Q4 2024."
            },
            {
                "q": "Which counties saw the biggest growth in building permits during Q1 2025?",
                "a": "Among counties with a significant base of permits, Pulaski County (AR) grew by 769%, Mahoning County (OH) by 373%, Salt Lake County (UT) by 346%, and Richmond County (GA) by 232%. Philadelphia County (PA) had the largest absolute increase with 6,797 additional permits."
            },
            {
                "q": "How are tariffs and interest rates affecting new construction permits?",
                "a": "New tariffs introduced in early 2025, including a 25% charge on steel and aluminum imports, are increasing building costs. Combined with persistently high interest rates that raise borrowing costs and reduce home affordability, builders are being more cautious. New construction permits fell 7.2% from Q4 2024 to Q1 2025, dropping to 134,000."
            },
            {
                "q": "Who are the top home builders by permit volume in Q1 2025?",
                "a": "D.R. Horton led with 4,237 permits and Lennar Homes followed closely with 4,020 permits. Among the most improved builders, Highland Homes saw 108% growth, Perry Homes jumped 84%, and Mattamy Homes grew 80% compared to Q4 2024."
            }
        ]
    },
    # Additional entries will be added in batches
}


def generate_faq_markdown(faqs):
    """Generate the visible FAQ markdown section."""
    lines = ["## Frequently Asked Questions", ""]
    for faq in faqs:
        lines.append(f"**Q: {faq['q']}**")
        lines.append("")
        lines.append(f"A: {faq['a']}")
        lines.append("")
    return "\n".join(lines)


def generate_faq_schema(faqs):
    """Generate the FAQPage JSON-LD schema."""
    main_entity = []
    for faq in faqs:
        main_entity.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity
    }

    schema_json = json.dumps(schema, indent=2)
    return f"""
<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{schema_json}
</script>"""


def add_faq_to_file(file_path, insert_after, faqs):
    """Add FAQ section and schema to a markdown file."""
    path = Path(file_path)
    if not path.exists():
        print(f"ERROR: File not found: {file_path}")
        return False

    content = path.read_text()

    # Check if FAQ already exists
    if "## Frequently Asked Questions" in content or "FAQPage" in content:
        print(f"SKIP: FAQ already exists in {file_path}")
        return False

    # Find insertion point
    if insert_after not in content:
        print(f"ERROR: Insert marker not found in {file_path}")
        print(f"  Looking for: {insert_after[:80]}...")
        return False

    # Generate FAQ content
    faq_markdown = generate_faq_markdown(faqs)
    faq_schema = generate_faq_schema(faqs)
    faq_content = f"\n\n{faq_markdown}{faq_schema}"

    # Insert FAQ
    new_content = content.replace(insert_after, insert_after + faq_content)

    # Write back
    path.write_text(new_content)
    print(f"SUCCESS: Added FAQ to {file_path}")
    return True


def main():
    """Process all files with FAQ data."""
    repo_root = Path(__file__).parent.parent
    success_count = 0
    skip_count = 0
    error_count = 0

    for file_rel_path, data in FAQ_DATA.items():
        file_path = repo_root / file_rel_path
        result = add_faq_to_file(
            str(file_path),
            data["insert_after"],
            data["faqs"]
        )
        if result:
            success_count += 1
        elif "SKIP" in str(result):
            skip_count += 1
        else:
            error_count += 1

    print(f"\nSummary: {success_count} added, {skip_count} skipped, {error_count} errors")
    return error_count == 0


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
