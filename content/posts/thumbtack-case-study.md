title: How Thumbtack Uses Shovels to Streamline Contractor License Verification
subtitle: Inside Thumbtack's partnership with Shovels to verify contractor licenses at marketplace scale
date: 2026-07-28
modified: 2026-07-28
category: Case Study
tag1: EDL
tag2: Home Services
tags: thumbtack, contractor license verification, CSL, contractor data, home services marketplace
authors: Morgan Friberg
author_image: /theme/images/team/morgan.svg
author_title: VP of Marketing
slug: thumbtack-case-study
summary: Thumbtack, one of America's largest home services marketplaces, uses Shovels' Contractor State License file and Enterprise Data License to streamline contractor license verification. Learn how standardized license data across 37 states helps Thumbtack verify pros faster and reduce onboarding friction.
image: /images/blog_images/case-study-thumbtack.png

Thumbtack is one of America's largest home services marketplaces. It connects millions of homeowners with more than 300,000 local professionals across over 500 project categories. At scale, *trust is the product*. Homeowners want confidence in the professionals they hire, and for certain trades and jurisdictions, licensing information can serve as an important trust signal.

That's the challenge Thumbtack's Trust and Safety team set out to solve when they partnered with us: improving the efficiency and consistency of license verification workflows while reducing friction for professionals. Within a year, Shovels' license and permit data became an important data source supporting those workflows, helping Thumbtack navigate a licensing landscape that is constantly changing.

## The Challenge

License verification is one of the most complex data problems in home services. Requirements vary by state and by trade, involve thousands of classification subsets, and change constantly. For years, confirming licensing information relied heavily on manual searches across state licensing databases. This created three compounding problems:

- **Structural complexity:** Every state database has its own structure, requirements, and update cadence. There is no single standard for how licensing information is organized or maintained.
- **Onboarding friction:** Contractors manually submit license details before they're verified. The extra steps slow down activation times on a marketplace that depends on getting qualified pros online quickly.
- **A taxonomy nightmare:** With roughly 3,000 state-specific license classifications nationwide, scaling license verification across states is no easy task. A "plumber" in one state's licensing system may be classified very differently in another.

Scaling license verification workflows was only part of the challenge. Thumbtack also wanted to create a more seamless experience for professionals by reducing the amount of information that needed to be manually collected and reviewed. Better data could help make verification faster, more consistent, and less burdensome for everyone involved.

## The Solution

This is where Shovels comes in. Thumbtack licenses our Contractor State License (CSL) file alongside our contractor and building permit data through an [Enterprise Data License](https://www.shovels.ai/data-feed) (bulk data share), delivered into their [BigQuery](https://console.cloud.google.com/marketplace/product/shovels-b7048/cloud-marketplace-a90e0dec-0ac2-4be6-bc13-15b7c2080b51.cloudpartnerservices.goog?project=shovels-b7048) data warehouse and refreshed on the 1st and 15th of each month.

The CSL aggregates licensing records from 37 states covering over 1.8 million contractors. Importantly, it retains every state's original license types in full. What Shovels adds is a CLASSIFICATION_DERIVED field that identifies which trade each license falls under, one of 13 [standardized categories derived from official classifications](https://www.shovels.ai/data-dictionary#contractors), such as plumbing, electrical, roofing, and HVAC.

That added layer is what makes working across states practical. Thumbtack can pull all plumbing-related license types across states, for example, without losing any state-level detail, instead of keyword-matching against thousands of state-specific licensing types and codes.

This data supports Thumbtack's streamlined badging workflow. Thumbtack cross-references professionals against Shovels license data as part of its verification process, and when a pro meets Thumbtack's verification criteria, Thumbtack awards them a "license verified" badge. In some cases, this happens without the pro needing to manually enter license details, removing a step that would otherwise slow down onboarding.

<figure class="my-10 rounded-2xl bg-shovels-light px-8 py-8 sm:px-12 sm:py-10">
  <div aria-hidden="true" class="font-serif text-7xl leading-none text-shovels-secondary-text">&ldquo;</div>
  <p class="text-xl sm:text-2xl font-medium leading-relaxed text-shovels-dark" style="margin-top:-1.75rem">Trust is everything for our marketplace. Shovels gives our team reliable, consistently structured licensing data to work from, which makes it easier to support pros as they get up and running.</p>
  <figcaption class="mt-6">
    <div class="font-semibold text-shovels-primary">Carmen Rombough</div>
    <div class="text-sm text-gray-600">Senior Manager, Risk Analytics, Thumbtack</div>
  </figcaption>
</figure>

In short, Shovels data serves as an early layer of checking. Thumbtack's team reviews, quality-assures, and continuously refines how the data is applied, and Thumbtack's own verification standards determine the outcome.

## The Results

Shovels continues to be an important part of Thumbtack's license verification operations, helping streamline license reviews and reduce manual effort. The initial deployment supported license verification workflows for hundreds of plumbers across six states, and Thumbtack has since expanded the program to electricians and HVAC contractors. License checks that once required navigating state databases one at a time can now start from a single standardized source.

Here's what's on the horizon for the partnership:

- **Expanded automation.** As the partnership evolves, Thumbtack is exploring additional ways to leverage Shovels' data to automate portions of its license verification operations, further improving efficiency and scalability.
- **Growth beyond licensing.** With data refreshes delivered twice monthly (and weekly updates on the roadmap), Thumbtack is exploring new ways to use permit data. Contractors appearing repeatedly across jurisdictions are often indicators of larger, more established businesses. Permit activity helps identify these active, established contractors and can serve as an additional trust signal.
- **A long-term investment.** Thumbtack extended the partnership into a multi-year agreement, signaling that Shovels had become foundational infrastructure.

For Thumbtack, working with Shovels delivers more than operational efficiency. It supports homeowner confidence and removes friction for legitimate contractors joining the marketplace. This is what trust at marketplace scale looks like.

> Shovels combines building permit and contractor data with local government decisions to help you verify licenses and identify growth opportunities. <a href="https://www.shovels.ai/contact" target="_blank">Talk to us directly about a custom solution</a>.
