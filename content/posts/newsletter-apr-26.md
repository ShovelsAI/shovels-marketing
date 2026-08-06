title: We Passed SOC 2® Type 2 — Here's Why It Matters (and What's Coming Next)
subtitle: SOC 2 is done — plus a product heads-up and a deep dive on Decisions
date: 2026-04-16
modified: 2026-04-16
category: Newsletter
tag1: 
tag2: 
tags: SOC 2, Shovels Online, API, rate limiting, Charlie, Properties, Decisions, ReZone
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
slug: april-2026-newsletter
summary: SOC 2 Type 2 is done — plus a heads up on upcoming Shovels Online, API rate limits, Charlie, Properties, and Decisions. Oh my!
image: /images/blog_images/april-2026-newsletter-hero.png

---

Before we get started, I have to share: there is no <a href="https://www.shovels.ai/blog/introducing-red-tag/" target="_blank">Shovels Red Tag product</a> 🫠. 

It was an April Fools' joke, guys. We got kudos, not for a good joke, but rather for creating a credible, useful product. We'll have to go a bit crazier next time!

I also admit that I skipped the March newsletter. By the time I realized this, we were a week away from publishing the Red Tag post and I decided you didn't need to hear from us twice. Anyway, most of you didn't notice. 

So this one will be just a little bit longer than usual. There's a lot to say! 

## SOC 2 in the AI Era

You might think SOC 2 Type 2 sounds like something your doctor might describe in a measured tone. It might make your face blush. You're not wrong. I am talking about viruses, but not that kind. 

After months and months of hard work, our SOC 2 Type 2 test came back positive. In other words, we passed! We are compliant. We have a new <a href="https://trust.shovels.ai/" target="_blank">Security Center</a> to prove it.

Our SOC 2 Type 2 report unlocks a number of opportunities for us in the Fortune 1000 due to the strict security requirements of publicly-traded companies. Most of you are not at public companies (👋 to those who are!) — yet our security compliance still matters. 

Here's why. Two (quite odd) words: Mythos and Spud. 

There has been much hand-wringing about the end of days with respect to artificial general intelligence (AGI) and the singularity (wherein robots completely outsmart us). It seems that every new OpenAI and Anthropic model release creates another wave of dooms and glooms and then nothing happens. 

Thus, I was struck by the tone of the All-In Podcast guys when they admitted some real concern about the warnings from both Anthropic (<a href="https://red.anthropic.com/2026/mythos-preview/" target="_blank">see article</a>) and OpenAI (<a href="https://x.com/btibor91/status/2036540895986602266?s=20" target="_blank">see tweet</a>) that their new models are finding zero-day security vulnerabilities all over the Internet. They call them zero-day because they're newly discovered, some hidden for decades.

So now the good guys are trying to shore up the Internet before the bad guys exploit this new AI capability, but they won't shore up everything. That's what brings me back to SOC 2. 

We started this process back in July. We just got our report a week ago. It takes that long. It was hours of meetings, hundreds of security tests, and new laptops (yes, with virus detection!) for everyone. 

I think of SOC 2 like an alarm system sign in our front yard. It won't prevent a robber from *trying* to sneak in, but it probably makes our neighbor's house a more attractive target. 

When the AI-powered hackers target startups, they'll target the ones without SOC 2 first. 

(How do you outrun a bear? Run faster than the other guy!) 

In this AI era we're all living in, SOC 2 will become a bigger deal. And we're a better, stronger, more secure company for doing this already.  

## Heads up: changes coming to Shovels Online and API

With all that AI and SOC 2 stuff being said, I suppose it should be no surprise that *we* would get scraped. We've become the target of bot swarms and clever other hackers who exploit the "unlimited" nature of our web application. 

At the same time, our legitimate usage has grown tremendously. Like, 3X the registrations just in the last 4 months! Our new self-serve subscription revenue each month is more than anything I've ever seen first-hand. 

Because of both the legitimate and illegitimate usage growth, we've decided to change things. Not right away, but it's coming. 

So here's the heads up. 

Sometime in the next… let's just say 6-8 weeks, we will no longer offer unlimited usage in Shovels Online. Instead, it will be rate-limited. We're still figuring out what that limit will be, but it will be a limit and we'll probably track it on a rolling 30 days basis, as we do currently with API customers. 

Free users will have a low rate limit. Paying users will have a much higher one. We'll set the limits so they fit this principal: generous but fair. I think those are words to live by.

We will also offer some very cool new Shovels Online features! Among them:

- Fully-integrated <a href="https://charlie.shovels.ai/login" target="_blank">Charlie</a>. Charlie and the app will no longer be separate; we are merging them together and Charlie will be able to control your search queries for you. I've tried our latest internal release. It's magic!
- Properties resolution. Instead of searching for solar permits in Florida and resolving only to contractors or the permits themselves, we're adding Properties as another way to resolve your query. The implication is this: "Show me all Properties in Florida that have NOT had a roofing permit in the last 10 years." Shovels Online will return that list of properties and let you download it.
- Decisions resolution. Oh boy. I'll have more to say about this below. But yes, <a href="https://docs.shovels.ai/docs/knowledge-base/data/decisions/overview#what-are-shovels-decisions" target="_blank">Decisions</a> are coming.
- Note: both Properties and Decisions will be available via our <a href="https://www.shovels.ai/api" target="_blank">API</a> and <a href="https://www.shovels.ai/cli" target="_blank">CLI</a> in addition to <a href="https://www.shovels.ai/permit-database" target="_blank">Shovels Online</a>.

## Everything I've learned about Decisions in the last 3 months

I want to say, first off, that it's a privilege to have time to do research and development at a company like Shovels at a time like this. I have R&D time now because we've made some critical hires in the last few months. I'll share more about this in future newsletters. 

To wit: as Luka has told me over and over, there's never been a more exciting time to be a builder. Luka and I are both builders, but I get to be the tip of the spear and he gets to figure out how to scale everything. 

Hence, Shovels Decisions! 

In case you missed it, we <a href="https://www.shovels.ai/blog/shovels-acquires-rezone/" target="_blank">acquired ReZone</a> from Daniel Heller and Brad Hargreaves in January this year. Both are experts in government data. Now we get to "Shovelize" ReZone and this process has been going for months now. We're calling it Shovels Decisions.

Our thesis with Decisions is this: don't stop at transcripts. Get everything and then convert the bundle of docs into useful Decisions objects that fit nicely into a database row or onto a map. This is what our customers want. 

Also, don't stop at city council and planning commissions! Track every body that posts meeting documents online (the smaller ones don't record or have transcripts). This is also what our customers want. 

When we dug deeper into Decisions, here's what we found: there are A LOT of different kinds of meetings in our local governments:

**🌳 Shade Tree Commission (Hoboken, NJ)** — Decides which trees get planted, removed, or protected. Hoboken has had one since the 1970s.

**🌿 Cannabis Review Board (Hoboken, NJ)** — Reviews cannabis business license applications. A body that didn't exist 5 years ago and is now a regular municipal fixture.

**🏛️ Historical Architectural Review Board (Allentown, PA)** — Decides whether you can change the color of your front door in a historic district.

**🚶 Riverwalk Commission (Naperville, IL)** — Governs a specific 1.75-mile riverwalk along the DuPage River — an entire commission for a walking path.

**🏗️ Value Adjustment Board** **(Orange County, FL)** — Where property owners go to contest their tax assessments. The board can literally lower your tax bill.

**👮 Providence External Review Authority (Providence, RI)** — Civilian oversight of police — reviews complaints against officers.

**💧 Oklahoma City Water Utilities Trust** **(Oklahoma City, OK)** — A separate government trust that owns and operates the city's entire water system.

We've collected agendas, minutes, and related attachments from each of these bodies going back to January 2020 wherever possible. 

We're now processing thousands of Decisions every single day. 

## Things to do with Decisions: track the local housing project

I recently read about this <a href="https://www.eastbaytimes.com/2026/04/09/walnut-creek-townhome-project-shadelands/?share=mmshuascttipbatawwre" target="_blank">new housing project</a> in my hometown of Walnut Creek, CA. It was in the paper just a few days ago. California needs more housing, lots more housing, so it piqued my interest.

Then I looked it up in our new Decisions system. Here's what I found! 

#### **Planning Commission Meeting — Feb 12, 2026**

We have the full document packet, including approval of:

- Final EIR + Mitigation Monitoring & Reporting Program
- Vesting Tentative Map No. 9683
- Final Design Review
- Density Bonus, Tree Removal, and Tree Dripline Encroachment Permits

Notable: The project was submitted under the State Housing Accountability Act (Builder's Remedy) + State Density Bonus Law.

Related attachments: Draft/Final EIR, Arborist Reports, Architectural/Civil/Landscape Plans, SB330 checklist, Applicant's Requested Waivers, public comments.

#### **City Council Meeting — April 7, 2026**

We have the full document bundle for the appeals hearing. Two appeals were filed:

1. **"Friends of Walnut Creek"** — filed Feb 20, 2026 (from Concord, CA)
2. **Individual neighbor** — filed Feb 23, 2026 (from 2701 Shadelands Drive, adjacent to project)

Related attachments: Draft resolutions for both appeals, original Notices of Appeal, First Carbon Solutions' response defending the EIR, Signature Development Group's response, EIR appendices, and a large batch of new public comments.

When the clerk posts the minutes that verify what happened, we'll generate the decisions! In the meantime, <a href="https://docs.google.com/spreadsheets/d/1g7QAbmrprhi1_-SxgvBJevl3OCqpI6pU8ppphltXcuA/edit?usp=sharing" target="_blank">here's a download</a> of every decision we have from that Planning Commission meeting.

### What this all means

We're Shovels. We focus on the data. We don't think big blobs of text are all that useful. A transcript alone can provide sentiment and show the presence of keywords, but you have to do work to figure out what *actually happened*. 

Same thing with agendas and transcripts and resolutions. They're just blobs of text until you break them down and make them useful. 

A Decision is a useful object. We distill Decisions from blobs of text. 

Decisions customers are already covering the local markets they care about, and we have a few other early adopters for our expanded nationwide product. If you're interested in subscribing to Decisions, please <a href="https://www.shovels.ai/contact" target="_blank">contact us</a>!

P.S. Check out these recent blog posts! 

- <a href="https://www.shovels.ai/blog/california-housing-market-building-permit-data/" target="_blank">https://www.shovels.ai/blog/california-housing-market-building-permit-data/</a>
- <a href="https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/" target="_blank">https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/</a>
- <a href="https://www.shovels.ai/blog/5g-beyond-urban-centers-permit-data/" target="_blank">https://www.shovels.ai/blog/5g-beyond-urban-centers-permit-data/</a>
- <a href="https://www.shovels.ai/blog/tampa-housing-market-permit-data/" target="_blank">https://www.shovels.ai/blog/tampa-housing-market-permit-data/</a>
- <a href="https://www.shovels.ai/blog/introducing-red-tag/" target="_blank">https://www.shovels.ai/blog/introducing-red-tag/</a>
