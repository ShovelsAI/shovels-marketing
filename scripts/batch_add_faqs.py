#!/usr/bin/env python3
"""
Batch add FAQ sections to blog posts using manually defined FAQ data.
Run from repo root: uv run python scripts/batch_add_faqs.py
"""

import json
from pathlib import Path
import sys


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


def add_faq_to_file(file_path, insert_marker, faqs, dry_run=False):
    """Add FAQ section and schema to a markdown file."""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return False

    content = path.read_text()

    # Check if FAQ already exists
    if "## Frequently Asked Questions" in content or "FAQPage" in content:
        print(f"⏭️  FAQ already exists: {path.name}")
        return True

    # Find insertion point
    if insert_marker not in content:
        print(f"❌ Insert marker not found in {path.name}")
        print(f"   Looking for: {insert_marker[:80]}...")
        return False

    # Generate FAQ content
    faq_markdown = generate_faq_markdown(faqs)
    faq_schema = generate_faq_schema(faqs)
    faq_content = f"\n\n{faq_markdown}{faq_schema}"

    if dry_run:
        print(f"🔍 Would add FAQ to: {path.name}")
        return True

    # Insert FAQ
    new_content = content.replace(insert_marker, insert_marker + faq_content, 1)

    # Write back
    path.write_text(new_content)
    print(f"✅ Added FAQ to: {path.name}")
    return True


def main():
    """Load FAQ data and process files."""
    # For now, load from JSON file
    repo_root = Path.cwd()
    data_file = repo_root / "scripts" / "faq_data.json"

    if not data_file.exists():
        print(f"❌ FAQ data file not found: {data_file}")
        print("   Please ensure faq_data.json exists in the scripts directory")
        return False

    with open(data_file) as f:
        faq_data = json.load(f)

    print(f"📋 Processing {len(faq_data)} files...\n")

    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("🔍 DRY RUN MODE - no files will be modified\n")

    success_count = 0
    skip_count = 0
    error_count = 0

    for file_rel_path, data in faq_data.items():
        file_path = repo_root / file_rel_path
        result = add_faq_to_file(
            str(file_path),
            data["insert_after"],
            data["faqs"],
            dry_run=dry_run
        )
        if result:
            if "already exists" in str(result) or "⏭️" in str(result):
                skip_count += 1
            else:
                success_count += 1
        else:
            error_count += 1

    print(f"\n📊 Summary: {success_count} added, {skip_count} skipped, {error_count} errors")
    return error_count == 0


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
