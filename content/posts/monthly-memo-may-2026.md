title: Monthly Memo - May 2026
subtitle: Future-Shovels: Decisions, Properties, V3, and Shovels Online
date: 2026-05-14
modified: 2026-05-14
category: Company
tag1:
tag2:
tags: Memo, Newsletter, Decisions, Properties, ReZone, Data ingestion, V3 API, Shovels Online, Charlie
authors: Ryan Buckley
author_image: /theme/images/team/ryan.svg
author_title: CEO
slug: monthly-memo-may-2026
summary: April was a record month, and May is a reminder of business ebb and flow—but the work continues. Updates include expanding "Decisions" coverage, an exploration of nationwide property/tax assessor data, the shift to a property-based architecture and breaking V3 API, plus a near-ready overhaul of Shovels Online with a new frontend/backend, Charlie integration, and an improved map.
image: /images/blog_images/monthly-memo-may-2026-hero.jpg

---

There's something about the struggle. 

April was our best month by every KPI we measure. May is definitely *not April*. (Loud and clear, *May*, we got it!) 

This is the ebb and flow of business. We all deal with it. From the local cafés to the venture-backed AI startups, there are good months and not-so-good months. The only thing to do about it is to keep working. 

Fortunately, I know no other way. 

I spent every night in April and May on a mission to extract every meeting packet and property detail from every major jurisdiction in the country. It's me and a fleet of AI agents probing, prodding, poking at every database and website that might have any morsel of info that we can ingest into future-Shovels. 

Future-Shovels isn't here yet. It's in the works. For now, it's my job to figure out what future-Shovels looks and feels like, and since I'm actually not a great planner, I think ahead by building. I don't know what the form can be until I start trying to actually put it together.

My future-Shovels projects involve Decisions and Properties. I don't know how many Decisions are available. Nobody does! It's never been done. There are north of 180M properties in the US. 

#### Decisions, decisions

Decisions, the things that come from government meetings. I've been thinking about Decisions long before we had the opportunity to <a href="https://www.shovels.ai/blog/shovels-acquires-rezone/" target="_blank">acquire ReZone</a>. 

Since then, we 7X'd our Decisions coverage. We're going back in time to 2020, a richer history than anyone else. It's complicated work. The pipeline keeps breaking. We're trying to feed 300-page minutes to Gemini and it doesn't like that. Cities post their agendas and minutes on old WordPress sites instead of using PrimeGov and Legistar. Some even put up a records request process just to get their minutes (what's up with that??).

The point is — it breaks. It's been a constant battle for weeks and months. It's getting better, but we're in the muck now, the long tail of trial and error that is both exhausting and exhilarating. 

Who am I kidding? I live for this. 

#### **Properties**

This one just sorta happened. I was having a good run at Decisions. It was working. I felt like a boss.

After chatting with Luka about how interesting it would be to develop our own tax assessor data feed, and how there are only a few companies that are doing it on their own (the rest resell), I decided to see what Claude Opus 4.7 could do. 

This wasn't a sophisticated prompt. I told it the same thing any of you would. "See if you can download the tax assessor property data from Contra Costa County. I don't know exactly where it is. You'll have to look for it. Gather as much information as possible."

Something like that. 

To my surprise and delight, it worked. Mostly. It's raw, it's messy, but it's there and we're now over 100M records deep, nearly a third of the 3,000 counties in the US. Every day we knock down a dozen more. And then I'll pass it to Petra to make the data beautiful. 

It's also been fun to trade notes with <a href="https://regrid.com/" target="_blank">Regrid</a>, our parcel partner.

#### V3

These next two projects are not my domain but I might be their loudest cheerleader. 

We're calling this one V3 and we committed ourselves to get it done this year. 

We're migrating from a data architecture based around permits to one that's based around properties. Our line of sight extends far beyond permits, and we shouldn't be restricted to only displaying addresses and contractors that have permits. 

It's a big change. We have to do it. 

This will create breaking changes to our V2 API, so we'll have to bump the version. To V3. 

#### Shovels Online

Our self-service product, <a href="https://app.shovels.ai/" target="_blank">Shovels Online</a>, is getting a massive overhaul. It's rewritten. New frontend, new backend. It's snappy, it's fresh, it's built for the future. It incorporates <a href="https://charlie.shovels.ai/" target="_blank">Charlie</a>, our AI agent, and it will have a suuuper awesome map. 

This will be legit. It's almost ready. The team is on it now, clicking around and filing bug tickets. You'll hear much more about this as we get closer to launch! 

#### In conclusion

The good months would be boring if we didn't have a not-good one every once in a while. It's motivation to keep going, to keep finding the top. 

It's all just part of the game, and we're playing to win!
