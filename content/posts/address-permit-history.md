Title: Why Don't All Addresses Have Permit History?
Subtitle: Understand the nuance of why a given address would have a permit on record.
Date: 2024-10-02
Modified: 2024-10-02
Category: Customer Success
Tags: permits, tutorial, resource, address
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: Not all addresses will have permits, for a variety of reasons. Variance between local requirements and enforcement means that not all projects require permits. Available digitization of permits makes it even more complicated, but Shovels has a plan keep improving data completeness.  
image: /images/address-history-hero.jpg


If you want an accurate picture of what’s been done to a property, it makes sense to look at the permit history. Theoretically, any project of reasonable size — a kitchen remodel, a new roof, a plug-in EV Charger install — would have some level of sign-off from the city or local jurisdiction, right? It’s up to the government to ensure that construction is done in a safe and legal manner, with inspections and approvals before work even begins as well as prior to completion. There should be a paper trail.

However, it’s that bureaucratic red tape that can bog down a project in it’s infancy, especially for understaffed permit departments. It’s not that your paperwork is out of order, there’s just too long of a queue. In some areas, you’d be free to do the work yourself; in others, work done without a permit can mean a hefty fine and teardown. 

At the end of the day, it all comes down to the local building code. And if we know anything about local regulations, the variance from town to town can be extreme. This is the core of our problem. **There are no standardized rules nationwide that mandate which work does or does not require a permit**. And even if there were, enforcement is another issue entirely. 

## Building Codes and Regulations

Consider a homeowner in Agawam, MA that is interested in upgrading their heating solution. Their old furnace finally gave out last winter, and they want to install a new heat pump to handle this winter’s cold and next summer’s heat, all from the same unit. The homeowner considers themselves a handyman, so could he do the installation alone, without a permit? 

For the State of Massachusetts, that answer is unfortunately **no**. According to the state’s [building code](https://www.mass.gov/doc/780-cmr-ninth-edition-base-code-chapter-1-scope-and-administration-amendments/download) (Section 105.2 of the 780 CMR (Code of Massachusetts Regulations)), which the Town of Agawam has adopted wholesale, a permit is required for this new install. The list of exempted projects is small, especially compared to some jurisdictions in some rural Texas counties, that might not have any permitting required at all!

The second issue, briefly mentioned above, regards enforcement. In all likelihood, this homeowner could install their own heat pump in secrecy, and no one would even know until the property was sold and the new buyer arranges a house inspection. Even where permits are required, the jurisdiction record office will never have a complete accounting of projects done. 

(To be clear, Shovels **does not** endorse such rogue construction. Always consult your local permit department for guidance on which projects you can DIY and which ones you need paperwork for.)

The variety of permit regulations across jurisdictions means that some areas will have more permits on file than others, even if equal numbers of equivalent projects were completed. From us at Shovels, we can only provide data on filed permits. And even then, only if those permits have been digitized. 

## Permit Digitization

The permits themselves are usually kept by either the local permit department or the County Clerk office. The forms are usually paper, but sometimes they’re submitted online. In many cases, the paper forms are later digitized and uploaded for public online access. 

Ideally, the jurisdictions will also upload their historical records. This can vary even more widely, but for the most part, we generally have ~20 years of permits, where available. 

These digitized permit records (and the insights gleaned from them) are what Shovels delivers.

However, digitization efforts and timelines vary dramatically (sensing a pattern yet?) from one jurisdiction to another. 

In summary, there are multiple hurdles we have to overcome to access digitized permit data:

1. Permit Requirements — does the jurisdiction require a permit for this type of project?
2. Regulation Adherence — how capable is the jurisdiction in enforcing that projects have the required permits?
3. Permit Digitization — how quick is the jurisdiction about uploading their filed permits for online access? How many years of permit history have they uploaded?

There’s a reason that few providers are able to effectively deliver these records and insights. Permit data is a mess, and it takes a ton of effort to parse, clean, and categorize it all. 

But we love a challenge, so we remain undaunted. 

## What Is Shovels Doing About It?

We knew that permit data was messy when we got into this business, so we have spent the vast majority of our codebase, engineering resources, and brainstorming power on how to solve this problem. 

Without getting into either the weeds or our secret sauce, we have three ongoing projects to improve the quantity and quality of our available permit data. 

1. Improve the training and quality of our proprietary LLMs (read more about how we built these [here](https://www.shovels.ai/blog/unlocking-shovelss-potential-with-prolific/)) — this will help us improve the timeliness of our delivery. The faster we can get the permits cleaned and our datasets updated, the fresher the insights. 
2. Enhance our relationships with local jurisdiction permitting offices to increase digitization with direct records requests — this will help us target specific jurisdictions with lower-than-usual digitization rates. 
3. Improve our personal transparency with what data we have and what we don't — check out our [Coverage Dashboard]({filename}../pages/coverage.md) to see a high-level view of what we have today. 

With every data refresh (which will increase to weekly soon!), we strive to get closer and closer to the truly available permit data ceiling. More permits are filed every day, and more jurisdictions increase their digitization efforts, so that end is in sight. 

## Get Started Today

We pride ourselves, here at Shovels, on being the best of the bunch when it comes to refining permit data into business intelligence. If there are particular markets or segments that you want to prioritize, [reach out to us](/contact) and we can either affirm that we have coverage there, or increase our timeline on getting them for you. 

In the meantime, poke around in our [Web App](https://app.shovels.ai) with a Free Trial to see the “shovel-ready” data we have for you now. 

Happy Digging!

## Frequently Asked Questions

**Q: Why doesn't every address have a permit history in Shovels?**

A: There are three main reasons: (1) the local jurisdiction may not require a permit for the type of work done, (2) even where permits are required, enforcement varies and some work is done without permits, and (3) the jurisdiction may not have digitized its permit records or made them available online yet.

**Q: Do all jurisdictions require permits for the same types of projects?**

A: No. There are no standardized nationwide rules mandating which work requires a permit. Requirements vary dramatically from one jurisdiction to another. Some states like Massachusetts have detailed requirements, while some rural counties may have minimal or no permitting requirements at all.

**Q: How far back does Shovels permit data go?**

A: Shovels generally has approximately 20 years of permit history where available, depending on how far back each jurisdiction has digitized and uploaded its records.

**Q: What is Shovels doing to improve data completeness?**

A: Shovels is pursuing three strategies: improving proprietary LLMs to speed up permit data processing and delivery, building relationships with local jurisdiction offices to increase digitization through direct records requests, and improving transparency about data coverage through a public Coverage Dashboard.

<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why doesn't every address have a permit history in Shovels?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There are three main reasons: (1) the local jurisdiction may not require a permit for the type of work done, (2) even where permits are required, enforcement varies and some work is done without permits, and (3) the jurisdiction may not have digitized its permit records or made them available online yet."
      }
    },
    {
      "@type": "Question",
      "name": "Do all jurisdictions require permits for the same types of projects?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. There are no standardized nationwide rules mandating which work requires a permit. Requirements vary dramatically from one jurisdiction to another. Some states like Massachusetts have detailed requirements, while some rural counties may have minimal or no permitting requirements at all."
      }
    },
    {
      "@type": "Question",
      "name": "How far back does Shovels permit data go?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Shovels generally has approximately 20 years of permit history where available, depending on how far back each jurisdiction has digitized and uploaded its records."
      }
    },
    {
      "@type": "Question",
      "name": "What is Shovels doing to improve data completeness?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Shovels is pursuing three strategies: improving proprietary LLMs to speed up permit data processing and delivery, building relationships with local jurisdiction offices to increase digitization through direct records requests, and improving transparency about data coverage through a public Coverage Dashboard."
      }
    }
  ]
}
</script>