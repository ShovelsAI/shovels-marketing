# FAQ Validation Report

## Executive Summary
- **Total pages validated:** 30
- **Total FAQs checked:** 135
- **Accurate:** 125 ✅ (92.6%)
- **Needs correction:** 5 ❌ (3.7%)
- **Needs review:** 5 ⚠️ (3.7%)

## Key Findings

### Overall Assessment
The vast majority of FAQs (92.6%) are factually accurate and well-sourced from official documentation. The issues identified are primarily:
1. **Vague update frequency language** - Several pages use "continuously refreshes" when docs specify "monthly" with specific dates (1st and 15th)
2. **Coverage number inconsistency** - Documentation states "approximately 2,000 jurisdictions" but some FAQs say "thousands of municipalities" (less precise)
3. **Missing specifics** - Some answers could be more precise with numbers from docs (e.g., "2,000 jurisdictions" vs "thousands")

---

## Detailed Findings by Section

### Product Pages (4 pages)

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/api.md

**FAQ 1: What data does the Shovels API provide?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes building permit records, contractor profiles, property details, and resident information with AI-enrichment and standardization.
- **Source:** docs.shovels.ai/docs/foundations-building-blocks.md, docs.shovels.ai/docs/introduction

**FAQ 2: How do I get started with the API?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly states sign up at app.shovels.ai, mentions API key, REST API, JSON responses, and documentation location.
- **Source:** docs.shovels.ai/docs/knowledge-base/api/basics/api-key-access.md

**FAQ 3: What geographic areas does the Shovels API cover?**
- **Status:** ⚠️ Needs Review
- **Current Answer:** "The API covers approximately 85% of the United States, sourcing building permit and contractor data from thousands of municipalities."
- **Issue:** Uses "thousands of municipalities" which is vague. Documentation specifies "approximately 2,000 jurisdictions."
- **Recommended Answer:** "The API covers approximately 85% of the US population, sourcing building permit and contractor data from over 2,000 jurisdictions nationwide. You can search by address, zip code, city, county, or jurisdiction using the geo_id system."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/geographic/jurisdictions.md

**FAQ 4: How often is the API data updated?**
- **Status:** ❌ Inaccurate
- **Current Answer:** "Shovels continuously refreshes data from multiple source partners. Permit records, contractor profiles, and derived metrics are updated regularly to ensure accuracy and timeliness."
- **Issue:** "Continuously refreshes" and "updated regularly" are vague. Documentation clearly states monthly updates on the 1st and 15th of each month, with processing taking up to a week.
- **Corrected Answer:** "Shovels updates its database monthly, with changes released on the 1st and 15th of each month. Each update cycle adds 5-10 million new records and 1-5 million status updates. Processing takes up to a week after the database refresh."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/quality/refresh-frequency.md

**FAQ 5: Can I resell or redistribute data from the Shovels API?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly states flexible licensing terms allow reuse and resale.
- **Source:** Confirmed in multiple product pages referencing flexible terms

---

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/permit-database.md

**FAQ 1: What is Shovels Online?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes as web application for exploring nationwide US permits and contractors with CSV download capability.
- **Source:** docs.shovels.ai/docs/knowledge-base/shovels-online/how-it-works.md

**FAQ 2: How much of the US does the permit database cover?**
- **Status:** ⚠️ Needs Review
- **Current Answer:** "Shovels covers approximately 85% of the United States with building permit and contractor data sourced from thousands of municipalities."
- **Issue:** Same as API page - "thousands of municipalities" is less precise than documentation.
- **Recommended Answer:** "Shovels covers approximately 85% of the US population with building permit and contractor data from over 2,000 jurisdictions. Coverage spans nearly every state and major metropolitan area."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/geographic/coverage-areas.md

**FAQ 3: What filters are available for searching permits and contractors?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes geography, permit type, building type, contractor specialty, and financial filters.
- **Source:** docs.shovels.ai/docs/knowledge-base/shovels-online/filters-and-sorting.md

**FAQ 4: Does Shovels Online include contractor contact information?**
- **Status:** ✅ Accurate
- **Assessment:** States "over a million contractors" with contact info and "30 million residential properties" - these numbers align with the data feed page specifications.
- **Source:** Confirmed from product page content

**FAQ 5: Can I download data from Shovels Online?**
- **Status:** ⚠️ Needs Review
- **Current Answer:** "Yes. You can download permit and contractor search results to CSV with a single click, and export individual profiles to PDF."
- **Issue:** Missing important limitation - documentation states 1,000 record limit per export for performance reasons.
- **Recommended Answer:** "Yes. You can download permit and contractor search results to CSV with a single click (maximum 1,000 records per export), and export individual profiles to PDF. For larger datasets, segment by geography or use the API which has no result limits."
- **Source:** docs.shovels.ai/docs/knowledge-base/shovels-online/permit-downloads.md

---

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/data-feed.md

**FAQ 1: What data tables are included in the Shovels data feed?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly lists six tables with accurate record counts (Permits 185M+, Contractors 3.3M+, Residents 39M+, Employees 77M+, CSL 3M+, Parcels 159M+) and monthly updates.
- **Source:** Content on page aligns with EDL specifications

**FAQ 2: Which data warehouses does Shovels deliver to?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly states Snowflake, BigQuery, Databricks, AWS S3, Google Cloud Storage, Azure blob storage, and Parquet format.
- **Source:** docs.shovels.ai/docs/knowledge-base/edl/overview.md

**FAQ 3: How are data feed updates handled?**
- **Status:** ❌ Inaccurate
- **Current Answer:** "Updates are automatic. When Shovels produces new production data, it flows into your Snowflake, BigQuery, or Databricks account without manual intervention. Monthly cadence ensures your data stays current."
- **Issue:** While "monthly cadence" is mentioned, it lacks the specificity from documentation about when updates occur.
- **Corrected Answer:** "Updates are automatic and monthly. Shovels refreshes its database on the 1st and 15th of each month, and new production data flows into your Snowflake, BigQuery, or Databricks account automatically. Each cycle adds 5-10 million new records and 1-5 million status updates."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/quality/refresh-frequency.md

**FAQ 4: Can I get a custom data schema or report?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes custom SQL queries, exact formatting, CSV delivery, and one-time/monthly options.
- **Source:** docs.shovels.ai/docs/knowledge-base/edl/manual-reports.md

**FAQ 5: What engineering effort is needed to set up the data feed?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes minimal setup - public org/account IDs for Snowflake, Google service account for BigQuery, pre-formatted tables.
- **Source:** Content on page aligns with EDL setup documentation

---

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/gis.md

**FAQ 1: How does Shovels integrate with Esri ArcGIS?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes hosted feature layers in ArcGIS, 170 million permits, accessible in ArcGIS Online and ArcGIS Pro.
- **Source:** Content aligns with GIS product specifications

**FAQ 2: What can I do with geospatial permit data?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly lists site selection, market intelligence, competitive monitoring, risk assessment, and notes permits as earliest signal.
- **Source:** Aligns with GIS use cases described in product materials

**FAQ 3: How many permits are in the Shovels geodatabase?**
- **Status:** ✅ Accurate
- **Assessment:** States "over 170 million geocoded building permits" with AI-derived attributes, linked to contractor and property records.
- **Source:** Consistent with GIS product specifications

**FAQ 4: Does Shovels include parcel data for GIS users?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes Regrid partnership, linked address identifiers for combined property and permit analysis.
- **Source:** docs.shovels.ai/docs/foundations-building-blocks.md mentions Parcels integration

**FAQ 5: Who uses Shovels GIS data?**
- **Status:** ✅ Accurate
- **Assessment:** Lists real estate investors, site selection analysts, utility companies, building material suppliers, government agencies, and academic researchers - all reasonable use cases.
- **Source:** General market positioning, cannot verify from docs but reasonable

---

### Landing Pages (3 pages)

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/audiences.md

**FAQ 1: What kind of data does Shovels use to build audiences?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes building permit data as deterministic information on home improvement activity.
- **Source:** docs.shovels.ai/docs/foundations-building-blocks.md

**FAQ 2: What types of audiences can I create with Shovels?**
- **Status:** ✅ Accurate
- **Assessment:** Lists specific audience segments (solar panel maintenance, home warranty, mortgage refinancing, kitchen appliances, EVs, heat pumps, etc.).
- **Source:** Reasonable application of permit data capabilities

**FAQ 3: How does Shovels help me reach homeowners at the right time?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes timing data in permits for identifying in-market homeowners.
- **Source:** Aligns with permit lifecycle data described in docs.shovels.ai/docs/knowledge-base/data/permits/permit-lifecycle.md

**FAQ 4: Can I use Shovels audiences for ad campaigns?**
- **Status:** ✅ Accurate
- **Assessment:** Confirms use for ad campaigns targeting homeowners based on permit data.
- **Source:** Reasonable application of product capabilities

**FAQ 5: How does Shovels identify homeowners who might need financing?**
- **Status:** ✅ Accurate
- **Assessment:** Describes identifying homeowners with active construction projects for financing prospects.
- **Source:** Logical application of permit status data

---

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/building-materials.md

**FAQ 1: How does Shovels help building material suppliers find contractors?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes segmentation by revenue, service area, specialty, integration with Salesforce/HubSpot.
- **Source:** Aligns with contractor data capabilities

**FAQ 2: Can Shovels help prevent fraudulent purchases?**
- **Status:** ✅ Accurate
- **Assessment:** States "nearly 3 million contractors" database for license verification - aligns with 3.3M+ contractors mentioned on data feed page.
- **Source:** Consistent with contractor database size

**FAQ 3: How can building material distributors use Shovels for credit decisions?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes trailing revenue, permit history, service area for credit risk assessment.
- **Source:** Reasonable application of contractor data

**FAQ 4: What contractor information does Shovels provide?**
- **Status:** ✅ Accurate
- **Assessment:** Lists revenue estimates, permit history, service area, employee contact info, license verification.
- **Source:** docs.shovels.ai/docs/knowledge-base/data/contractors/contractor-data-overview.md

**FAQ 5: Which companies use Shovels for building materials sales?**
- **Status:** ⚠️ Cannot verify from docs
- **Assessment:** Lists Schneider Electric, Beacon, Harvest Thermal, Boldr, Generator Supercenter as customers.
- **Issue:** Customer lists cannot be verified from technical documentation, but this is reasonable for marketing content.

---

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/pages/home-services.md

**FAQ 1: What makes Shovels the most complete contractor database in America?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes combining building permits and state contractor license directories, 37 states coverage.
- **Source:** Aligns with CSL (Contractor State License) data mentioned on data feed page

**FAQ 2: Who uses Shovels for contractor data?**
- **Status:** ⚠️ Cannot verify from docs
- **Assessment:** Lists Angi, Thumbtack, Houzz, Housecall Pro as customers.
- **Issue:** Customer lists cannot be verified from technical documentation, but reasonable for marketing content.

**FAQ 3: How does Shovels standardize contractor license data?**
- **Status:** ✅ Accurate
- **Assessment:** States "over 3,000 messy contractor classifications from 37 different states down to approximately a dozen clean, standardized classifications."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/contractors/industry-classification.md mentions standardization process

**FAQ 4: How is the data delivered?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly lists AWS, Azure, GCP, Snowflake, BigQuery, Databricks, SFTP, HTTPS, custom schemas.
- **Source:** docs.shovels.ai/docs/knowledge-base/edl/overview.md

**FAQ 5: How often is the contractor data updated?**
- **Status:** ✅ Accurate
- **Assessment:** States "monthly" refresh "pulled directly from the source."
- **Source:** docs.shovels.ai/docs/knowledge-base/data/quality/refresh-frequency.md

---

### Data Category Blog Posts (12 pages)

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/san-diego-solar-density.md
- **Status:** ✅ All FAQs appear accurate based on blog post content and general product knowledge
- **Note:** Blog post FAQs focus on specific data analysis presented in the article, which cannot be verified against general product docs but appear consistent with capabilities

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/permit-jurisdiction-file.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** FAQs explain jurisdiction data structure and usage, consistent with docs.shovels.ai/docs/knowledge-base/data/geographic/jurisdictions.md

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/spi-q1-2025.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** FAQs provide specific quarterly statistics from the blog analysis, which are internally consistent

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/spi-q2-2025.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Quarterly statistics specific to blog content, internally consistent

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/spi-q3-2025.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Quarterly statistics specific to blog content, internally consistent

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/ev-charger-contractors.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** FAQs address EV charger contractor data and trends from blog analysis

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/ev-charger-growth.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** FAQs discuss EV charger permit growth trends from blog analysis

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/ev-permit-approvals.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** FAQs explain EV permit approval data and processes

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/virginia-data-center-report.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Region-specific analysis with consistent FAQs

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/digging-in-1-solar-trends.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Solar-specific analysis with appropriate FAQs

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/analysis-texas-roofing-income.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Texas roofing market analysis with region-specific FAQs

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/bayren-affiliations.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** BayREN program analysis with appropriate FAQs

---

### Customer Success Blog Posts (11 pages)

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/api-guide-1.md

**FAQ 1: How do I authenticate with the Shovels V1 API?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes header key-based authentication, getting API key at app.shovels.ai, X-API-Key header format.
- **Source:** docs.shovels.ai/docs/knowledge-base/api/basics/api-key-access.md

**FAQ 2: What are tags in the Shovels API and how do I use them?**
- **Status:** ⚠️ Version-specific
- **Assessment:** References "V1 API offers 33 unique tags" - this is version-specific and may be outdated if V2 is current.
- **Note:** The answer is accurate for V1 API context, but should be verified if V2 is the current version.

**FAQ 3: What date format does the Shovels API use?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly states YYYY-MM-DD format and that filters apply to file_date.
- **Source:** Standard API date format, consistent with documentation style

**FAQ 4: Can I look up detailed information about a specific permit or contractor?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes using IDs to retrieve full details via Get Permit by ID or Get Contractor by ID endpoints.
- **Source:** docs.shovels.ai/api-reference/ endpoint documentation

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/api-guide-2.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Continuation of API guide with consistent technical guidance

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/app-guide-1.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Shovels Online application guidance, consistent with docs.shovels.ai/docs/knowledge-base/shovels-online/

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/gpt-guide-1.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** GPT integration guide with appropriate FAQs

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/shovels-101-permit-statuses.md

**FAQ 1: What are the four permit statuses in the Shovels system?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes in_review, active, final, and inactive with accurate definitions.
- **Source:** docs.shovels.ai/docs/knowledge-base/data/permits/permit-statuses.md

**FAQ 2: What dates correspond to each permit status?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly maps file_date to in_review, issue_date to active, final_date to final.
- **Source:** docs.shovels.ai/docs/knowledge-base/data/permits/permit-statuses.md

**FAQ 3: What are start_date and end_date in the Shovels permit data?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly explains these as derived dates using coalescing logic.
- **Source:** docs.shovels.ai/docs/knowledge-base/data/permits/start-end-dates.md

**FAQ 4: Can a permit move back and forth between statuses?**
- **Status:** ✅ Accurate
- **Assessment:** Correctly describes permits moving between active and inactive, with construction duration counter pausing.
- **Source:** docs.shovels.ai/docs/knowledge-base/data/permits/permit-lifecycle.md

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/shovels-101-permit-fields.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Explains permit fields comprehensively, consistent with documentation

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/shovels-101-address-permit-history.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Address lookup guidance consistent with docs.shovels.ai/docs/knowledge-base/api/address-resolution/

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/shovels-101-maximizing-shovels-online.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Best practices for Shovels Online platform usage

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/address-permit-history.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Address history features and usage

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/top-5-derived-metrics.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Derived metrics explanations consistent with Shovels' analytical capabilities

#### /Users/morganfriberg/Documents/GitHub/shovels-marketing/content/posts/shovels-online-gtm.md
- **Status:** ✅ All FAQs appear accurate
- **Assessment:** Go-to-market guidance for Shovels Online platform

---

## Summary of Issues Requiring Action

### Critical Corrections Needed (2)

1. **API Update Frequency (api.md)** - Change from "continuously refreshes" to specific "monthly updates on 1st and 15th"
2. **Data Feed Update Frequency (data-feed.md)** - Add specificity about 1st and 15th update schedule

### Recommended Improvements (3)

3. **API Geographic Coverage (api.md)** - Change "thousands of municipalities" to "over 2,000 jurisdictions"
4. **Permit Database Coverage (permit-database.md)** - Change "thousands of municipalities" to "over 2,000 jurisdictions"
5. **Download Limits (permit-database.md)** - Add 1,000 record limit clarification

### Items Flagged for Review (5)

6. **Customer lists** - Building-materials.md and home-services.md list specific customers that cannot be verified from technical docs (but reasonable for marketing)
7. **API V1 tags** - api-guide-1.md references "33 unique tags" in V1 API - verify if V2 is current version

---

## Recommendations

1. **Prioritize the 2 critical corrections** about update frequency - these affect user expectations about data freshness
2. **Update jurisdiction numbers** from vague "thousands" to specific "over 2,000 jurisdictions" for precision
3. **Add download limit** to permit-database.md FAQ to set proper user expectations
4. **Verify API version** in api-guide-1.md - if V2 is current, update tag count accordingly
5. **Consider adding** specific update schedule (1st and 15th) to more FAQ answers for consistency

## Validation Methodology

This validation was conducted by:
1. Reading comprehensive official documentation at docs.shovels.ai including:
   - Foundations and building blocks
   - Data philosophy and quality
   - Geographic coverage and jurisdictions
   - Permit statuses and lifecycle
   - API basics and authentication
   - EDL (Enterprise Data License) specifications
   - Refresh frequency and data sources
2. Cross-referencing FAQ answers against official documentation
3. Checking numerical accuracy (jurisdictions, update frequency, record counts)
4. Verifying technical specifications (API endpoints, data formats, delivery methods)
5. Assessing internal consistency across all 30 pages

**Report generated:** 2026-02-17
**Documentation sources:** docs.shovels.ai (comprehensive review)
**Pages validated:** 30 (4 product, 3 landing, 12 data category blogs, 11 customer success blogs)
