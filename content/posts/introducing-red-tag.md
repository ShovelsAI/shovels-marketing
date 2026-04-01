title: Introducing Shovels Red Tag: Agentic Permit Enforcement
subtitle: Launch of our automated permit enforcement product.
date: 2026-04-01
modified: 2026-04-01
category: Company
tags: permit data, construction, transparency, product storytelling, April Fools
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
slug: introducing-red-tag
summary: What started as a simple product enhancement ended up red-tagging a 89,000-square-foot project in Washington, DC.
image: /images/blog_images/introducing-red-tag-hero.png

As you know, we've been doing a lot of mapping around here. We like maps, and we're getting better and better at maps.

At a mapping conference last year we met another startup that was collecting super high resolution satellite imagery.

Interesting, we thought. Could we use AI to determine how far along a project is once its permit is approved? Is the crane stood up? Has the lumber arrived? All that would be pretty cool.

And then another idea came into focus: What if we could do the opposite, use those same satellite images to detect construction *without* a permit? And if indeed the permit doesn't exist, we could file a report, and if it turns out we're right, the project would get red-tagged.

Red. What else is red? Lobsters. What cool new tool uses a lobster emoji? OpenClaw **🦞**. If you're an AI nerd like us, you know where this is going.

Agentic red tagging. Let the AI agents loose, red-tagging all sorts of things, all over the country!

It'll be like that super annoying neighbor who won't even let you hang Christmas lights without calling the building department. Everywhere, all at once. On autopilot!

We loved the idea, so we did what any self-respecting AI startup would do: **we vibe-coded it over the weekend**.

We're launching today!

## What We Built

Introducing **Red Tag**, the first agentic permit-enforcement tool built on top of real construction data.

![Red Tag product interface showing permit gap detection dashboard]({static}/images/blog_images/introducing-red-tag-product-screenshot.png)

Here's how it works:

Red Tag runs on RedClaw, our customized OpenClaw instance that scans satellite images for construction. If we detect construction activity and find no associated permit record, we generate a report and send it to the <a href="https://www.shovels.ai/blog/ahj-in-construction/" target="_blank">Authority Having Jurisdiction (AHJ)</a>.

The AHJ is the body empowered to enforce building codes and permit requirements for a given project, and when they receive a complaint of unpermitted construction, they're required to investigate. Just for added weight, we copy the President of the United States and the head of the IRS.

An investigation on an unpermitted project typically triggers a stop-work order.

A stop-work order means a red tag on the door.

The tool is simple. The data is public. The block parties can get awkward, but hey, we're just making public data useful!

## Red Tag Features

🔍 **Permit Gap Detection**: Search any of the 30 million addresses in our database. If it was permitted, we should have it.

📋 **One-Click AHJ Reporting**: Red Tag auto-identifies the correct <a href="https://www.shovels.ai/blog/ahj-in-construction/" target="_blank">Authority Having Jurisdiction</a> based on address, because figuring out *which* agency to call is half the battle. No hunting for the right form. No figuring out which of the three million contractors in our database did the work. Just click, confirm, and submit.

📎 **Evidence Attachment**: Attach supporting documentation to your report, satellite imagery, news articles, contractor announcements, nationally televised press conferences, Google StreetView images, and your own evidence, if you want. Our system accepts up to 500MB per submission.

📬 **Status Notifications**: Receive email updates when your Red Tag report is opened, assigned, and actioned by the relevant AHJ. If you prefer USPS, it will arrive in an unmarked envelope for discretion.

🛑 **Red Tag Database**: See all the Red Tags we've filed. When an address receives a red tag, we send a Shovels tote bag and a yard sign with the words "It Wasn't Me" to each of the neighbors.

## Our First Red Tag

This one got awkward. Real fast.

Our very first run scanned the web for large-scale construction projects and one address came back with a massive red tag.

- **Estimated construction footprint:** 89,000 square feet
- **Estimated job value: $**350 million
- **Construction detected via satellite imagery:** Umm.. yea
- **Permits on file:** ZERO

We assumed it was a data error. Our team triple-checked. They checked again. They combed through every permit in the jurisdiction. They refreshed the source and did it again, this time by hand. They went for a walk and came back and checked one more time. They even asked ChatGPT.

Zero permits. 89,000 square feet. $350 million price tag. Active construction.

Who on earth would do such a thing?

And who on earth could get away with it?

![Image: 89K square foot active construction zone - no permits. Source: msn.com]({static}/images/blog_images/introducing-red-tag-construction-site.png)
*Image: 89K square foot active construction zone - no permits. Source: msn.com*

For context: 89,000 square feet is roughly the size of a mid-sized regional airport terminal. You cannot build 89,000 square feet in the United States, in a jurisdiction with some of the most stringent historic preservation review requirements in the country, no less, without permits. Or rather, you *shouldn't* be able to.

Before we could stop it, the RedClaw agent filed the red tag report. It copied the White House, the IRS, even the New York Times tip line (AI can be so clever).

The address was **1600 Pennsylvania Ave NW, Washington, D.C. 20500**.

Yes, <a href="https://www.whitehouse.gov/about-the-white-house/the-white-house/#:~:text=East%20Wing%20Expansion%20Stages" target="_blank">that one</a>.

Oopsies.

![Image: Shovels first Red Tag filing. Source: theguardian.com]({static}/images/blog_images/introducing-red-tag-guardian.png)
*Image: Shovels first Red Tag filing. Source: theguardian.com*

It turns out that our first Red Tag was effective. Just days after submission, the news came out:

<div style="text-align: center;">
<img src="{static}/images/blog_images/introducing-red-tag-result.jpeg" alt='Image: News headline "Judge Halts White House Ballroom Construction"' style="max-width: 400px; width: 100%; display: block; margin: 0 auto;">
<em>Image: News headline "Judge Halts White House Ballroom Construction"</em>
</div>

> **Note:** *Red Tag is <a href="https://app.shovels.ai/signup/" target="_blank">available</a> to all Shovels users starting today. Free tier includes 3 Red Tag reports per month. Unlimited reporting available on our Pro plan.*

*If you made it this far:* 🍀 H*appy April Fools' Day from everyone at Shovels. Red Tag is not a real product.*

*What IS real: Shovels has a ton of data. If you want to know what's being built, where, by whom, and whether it's permitted, that part we can actually help with - <a href="https://www.shovels.ai/contact" target="_blank">reach out to us</a> or <a href="https://app.shovels.ai/signup/" target="_blank">start a free account</a>.*

*Sincerely,*

*The Shovels April Fools' Day Newsletter Committee*

P.S. Here's <a href="https://www.shovels.ai/blog/introducing-the-department-of-permit-efficiency-dope/" target="_blank">last year's April Fools' Day newsletter</a>. It was pretty good too!
