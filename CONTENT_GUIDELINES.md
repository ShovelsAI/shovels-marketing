# Content Guidelines for Shovels Marketing Site

This document outlines best practices for creating content on the Shovels marketing site, with a focus on Answer Engine Optimization (AEO) and FAQ implementation.

## Table of Contents
1. [When to Add FAQs](#when-to-add-faqs)
2. [FAQ Writing Guidelines](#faq-writing-guidelines)
3. [Technical Implementation](#technical-implementation)
4. [Validation Checklist](#validation-checklist)
5. [Examples](#examples)

---

## When to Add FAQs

### ✅ Always Include FAQs

**Product & Feature Pages**
- Main product pages (API, Permit Database, Data Feed, GIS, etc.)
- New feature announcement pages with substantial detail
- Product comparison pages

**Landing Pages**
- Customer segment pages (audiences, building-materials, home-services)
- Industry-specific landing pages
- Solution pages for specific use cases

**Educational Content**
- How-to guides and tutorials (Shovels 101 series, API guides)
- Technical documentation overviews
- Best practices articles

**Data Analysis & Research**
- Market analysis reports (SPI, industry trends)
- Geographic analysis (solar density, EV charger growth)
- Original research with insights

### ❌ Skip FAQs For

**Time-Sensitive Content**
- Monthly newsletters
- Partnership announcements
- Company news updates
- Event announcements

**Non-Text Content**
- Podcast episode announcements
- Video content pages
- Image galleries

**Brief Content**
- Blog posts under 500 words
- Quick tips or list posts
- Social media roundups

**Story-Driven Content**
- Case studies (narrative format works better)
- Customer testimonials
- Behind-the-scenes posts

---

## FAQ Writing Guidelines

### Number of Questions
- **Minimum**: 3 questions
- **Optimal**: 5 questions
- **Maximum**: 8 questions (avoid overwhelming readers)

### Question Quality
**Good questions:**
- Start with what, how, why, when, can, does
- Address common user concerns
- Reflect actual customer questions
- Use natural language people would search for

**Examples:**
- ✅ "How often is the API data updated?"
- ✅ "What geographic areas does Shovels cover?"
- ✅ "Can I resell data from the Shovels API?"
- ❌ "What is data?" (too vague)
- ❌ "Tell me about updates" (not a question)

### Answer Quality
**Guidelines:**
- **Length**: 2-4 sentences (50-100 words)
- **Tone**: Professional but conversational
- **Specificity**: Include numbers, dates, concrete details
- **Accuracy**: Always verify against docs.shovels.ai
- **Consistency**: Use official stats from homepage (185M+ permits, 3.3M+ contractors, 33M+ addresses, 5M+ monthly updates)

**Answer structure:**
1. Direct answer to the question (first sentence)
2. Additional context or benefits (optional second sentence)
3. Related detail or next step (optional third sentence)

**Example:**
```
Q: How often is the API data updated?

A: Shovels updates its database monthly, with changes released on
the 1st and 15th of each month. Each update cycle adds 5-10 million
new records and 1-5 million status updates. Processing takes up to a
week after the database refresh.
```

### Source of Truth

**Always verify answers against:**
1. **Primary**: https://docs.shovels.ai/docs/introduction
2. **Secondary**: Homepage stats (themes/shovels/templates/index.html)
3. **Tertiary**: Product pages (api.md, permit-database.md, etc.)

**Official numbers (as of Feb 2026):**
- Building permits: 185M+
- Contractors: 3.3M+
- US addresses covered: 33M+
- New permits monthly: 5M+
- Geographic coverage: 85% of US population, over 2,000 jurisdictions
- Update frequency: Monthly on 1st and 15th
- Database refresh: 5-10M new records, 1-5M status updates per cycle

---

## Technical Implementation

### HTML Format (Visible FAQs)

Place FAQ section at the bottom of the page, before final CTA:

```html
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
      <h2 class="text-3xl font-semibold tracking-tight text-gray-900 sm:text-4xl">Frequently Asked Questions</h2>
      <dl class="mt-10 space-y-8 divide-y divide-gray-900/10">
        <div class="pt-8 lg:grid lg:grid-cols-12 lg:gap-8">
          <dt class="text-base/7 font-semibold text-gray-900 lg:col-span-5">Question here?</dt>
          <dd class="mt-4 lg:col-span-7 lg:mt-0">
            <p class="text-base/7 text-gray-600">Answer here.</p>
          </dd>
        </div>
        <!-- Repeat for each Q&A pair -->
      </dl>
    </div>
  </div>
</div>
```

### JSON-LD Schema (for AI Answer Engines)

Add immediately after the HTML FAQ section:

```html
<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question text here?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Answer text here."
      }
    },
    {
      "@type": "Question",
      "name": "Second question?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Second answer."
      }
    }
  ]
}
</script>
```

**Important:**
- Keep HTML and JSON-LD in sync (same questions and answers)
- Escape quotes in JSON-LD (use `\"` for quotes within text)
- Validate JSON-LD syntax before committing

---

## Validation Checklist

Before publishing content with FAQs:

### Content Validation
- [ ] 3-5 questions included
- [ ] Questions start with what/how/why/when/can/does
- [ ] Answers are 2-4 sentences each
- [ ] All answers verified against docs.shovels.ai
- [ ] Numbers match official homepage stats
- [ ] No temporal language ("recently", "currently", "soon")
- [ ] No vague terms ("regularly updated", "many", "thousands")

### Technical Validation
- [ ] HTML FAQ section present with proper structure
- [ ] JSON-LD schema included immediately after HTML
- [ ] HTML and JSON-LD have identical Q&A pairs
- [ ] JSON-LD syntax is valid (no trailing commas, quotes escaped)
- [ ] FAQ section placed before final CTA
- [ ] Page renders correctly on localhost

### SEO Validation
- [ ] FAQ section appears on the page (not hidden/broken)
- [ ] Questions are visible and readable
- [ ] Schema validates in Google Rich Results Test
- [ ] No duplicate questions across the site

---

## Examples

### Example 1: Product Page FAQs (API)

**Good:**
```
Q: What data does the Shovels API provide?

A: The Shovels API provides building permit records, contractor
profiles, property details, and resident information from over 2,000
jurisdictions across the United States. Data is AI-enriched and
standardized into a clean JSON format with geographic search,
advanced filtering, and derived quality metrics like inspection
pass rates.
```

**Why it works:**
- Directly answers "what data"
- Includes specific details (2,000 jurisdictions)
- Mentions key features (AI-enriched, standardized, filters)
- Uses official terminology from docs

### Example 2: Landing Page FAQs (Building Materials)

**Good:**
```
Q: How does Shovels help building material suppliers find contractors?

A: Shovels provides nationwide building permit data that lets you
segment contractors by revenue, service area, and specialty. This
enriches your lead program with unique insights on both commercial
and residential builders, and the data integrates directly with
Salesforce and HubSpot.
```

**Why it works:**
- Addresses specific audience pain point
- Explains the "how" with concrete details
- Mentions integration capabilities
- Focuses on business value

### Example 3: Data Analysis Post FAQs

**Good:**
```
Q: What does the Shovels Permit Index (SPI) measure?

A: The SPI tracks quarterly construction activity by measuring permit
counts, valuation, and status changes across over 2,000 US
jurisdictions. The index provides leading indicators for the
construction industry, showing trends before they appear in
housing starts or economic reports.
```

**Why it works:**
- Defines the metric clearly
- Provides context on methodology
- Explains value proposition
- Uses specific, verifiable numbers

---

## Common Mistakes to Avoid

### ❌ Vague or Inconsistent Numbers
**Bad:** "thousands of municipalities"
**Good:** "over 2,000 jurisdictions"

### ❌ Unclear Update Frequency
**Bad:** "updated regularly" or "continuously refreshes"
**Good:** "monthly updates on the 1st and 15th"

### ❌ Temporal Language
**Bad:** "We recently added this feature"
**Good:** "This feature includes..."

### ❌ Questions Without Question Marks
**Bad:** "Tell me about API authentication"
**Good:** "How do I authenticate with the Shovels API?"

### ❌ Overly Long Answers
**Bad:** Paragraph with 8+ sentences covering multiple topics
**Good:** 2-4 focused sentences directly answering the question

### ❌ Missing JSON-LD Schema
- Always include both visible HTML and structured data
- Pages with FAQs are 3.2x more likely to appear in AI Overviews

---

## Resources

- **Official Documentation**: https://docs.shovels.ai/docs/introduction
- **Homepage Stats**: themes/shovels/templates/index.html (lines 59-76)
- **Example Product Page**: content/pages/api.md
- **Example Landing Page**: content/pages/home-services.md
- **Example Blog Post**: content/posts/shovels-101-permit-statuses.md
- **Schema Validator**: https://validator.schema.org/
- **Google Rich Results Test**: https://search.google.com/test/rich-results

---

## FAQ Validation Report

A comprehensive validation of all site FAQs was completed on 2026-02-17. See `faq-validation-report.md` for:
- Accuracy assessment (92.6% accurate)
- Identified corrections
- Recommended improvements
- Validation methodology

---

**Last Updated**: February 17, 2026
**Maintained By**: Marketing Team
**Questions?** Contact betty@shovels.ai
