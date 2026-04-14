Title: Shovels 101: Maximizing Shovels Online
Subtitle: In-depth tutorial on how to get the most of our your Shovels Online subscription.
Date: 2024-11-20
Modified: 2024-11-20
Category: Customer Success
Tag1: Shovels Online
Tag2:
Tags: web application, tutorial
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: Learn from the experts how to get the most out of Shovels Online. Unlock use cases, best practices, and insider tips. Subscribe today before prices increase.
image: /images/maximizing-shovels-online-hero.png

We just [announced](https://www.shovels.ai/blog/welcome-to-shovels-online/) the release of our new-and-improved web application, [Shovels Online](https://app.shovels.ai), and it’s time to dig deeper into some best practices, tips and tricks, and other insider guidance from the Shovels team to help you leverage our platform to it’s fullest.

> **Note**: We’re still technically in early-adopter territory, as far as pricing goes. If you’ve been considering our platform thus far, now’s the best time to get in on the action before prices go up! Black Friday is coming a little early this year 🎁

## Shovels Online Use Cases

Compared with our other products, like our [API](https://www.shovels.ai/api) and [Enterprise data](https://www.shovels.ai/data-feed) offering, Shovels Online has the lowest barrier to entry. But just because it’s web-based and codeless doesn’t mean it isn’t powerful in it’s own right. 

Like any tool, it’s important to know which one to use. Shovels are designed to dig, and Shovels Online is designed to explore opportunities. Let’s get in to a few of our most common use cases.

### Homeowner Leads

f you’re a New England regional heat pump retailer (or installer!), then you can use the Shovels Online permit database to find addresses with homeowner contact details in your market that show signals of buyer intent and interest. 

Those signals might be recently pulled permits for other green or climate-friendly appliances, like solar panels or other electrification projects. This shows that they’re already interested in upgrading. 

Cross-referencing those results against a list of addresses that recently pulled permits for fossil fuel-based heater installs lets you narrow down your search to those who may have aging heating systems, in need of replacement. Now you’re confident that you wont waste your time selling a heat pump to someone that just replaced their gas heater last year. 

You now have a lead list complete with contact details and permit contexts, and all that’s left is for your Sales team to start reaching out. 

It truly is that simple. Replace “heat pump” with “bathroom remodel”, “roof”, or whatever business you’re in, and the rest of the logic will stay the same.

### Contractor Leads

Using nearly identical logic to the homeowner section above, you - a completely different New England regional heat pump *supplier* - may instead want to search for contractors in your market area. 

Based on your model, you may want to go after the experienced and proven contractors and offer them a better deal than their existing supplier. Alternatively, you may want to look for brand new contractors, fresh-faced and newly entering the market, and build a relationship with them from the very beginning. The world is your oyster (stew). 

Using the `Building`, `Permit`, and `Contractor` filters, you can fine-tune your search to the exact specifications of your business model, and export all that data (including contact info) into a CSV and the waiting arms of your outbound Sales team.

### Derivative Lead

Homeowner and Contractor leads are by far the most common, but we’ve been routinely surprised by the breadth and width of opportunities that you can glean from public permit data. 

For example:

- Permit approval timing: Use Shovels Online to figure out how long it will take to get that heat pump permit in your target jurisdiction!
- Resident demographics: We just released a new API endpoint for identifying residents of addresses. Now you know who to make that postcard out to 😊

## How to Build a High-Quality Search

Now that we’ve got the general use cases covered, let’s dig deep into the logic of a Shovels Online search query, how to leverage the entire range of filters, and make sure that the results are actually what you’re looking for. 

### Specific Geographies

The first step is to determine what scale are you looking at, and in what region. If it’s a pretty niche project type, like New England `pool` installations, then you may want to zoom out and look at the `state` level. 

On the other end of the spectrum, if you’re looking at something very common like `New Construction` and `Residential`, then you may want to get as granular as `zip code`. 

At the end of the day, you have unlimited searches, so there’s no harm in going piecemeal and working through your market area and seeing what volume you’re getting back.

### Permits or Contractors?

Permits and Contractors are the two main axes by which all Shovels data is aligned, and Shovels Online is no different. While there is some overlap, like wanting to know the connected contractor on a given permit, most people will want to search for one or the other. 

To start, we suggest looking at which persona you’re trying to sell to (a homeowner or a contractor) and choose accordingly.

### Focusing on Key Filters

Some of the most important and powerful upgrades to our web application with the release of Shovels Online is the increased number of filters and parameters. You can now specify minimum project details for a given structure across multiple dimensions. Things like `minimum market value` , `minimum lot size`, or even keywords from the permit `description` make it easier than ever to get the exact kind of projects that fit your business model. 

On the Contractor side, you can filter by performance metrics too: `minimum total permits` or `maximum [project] duration` and others.

### Spot-Check the Results

Now that you’ve built out the perfect query, it’s time to put the results to the test. Once the filters are applied and the results are in, spot check a few by clicking “View Details” and make sure that it matches your expectation. 

To get the volume you need, you may need to expand or contract your geography or `date range`. Adjust those, or any other filters, as needed and re-apply. 

In any case, once you’re happy with what you’ve found, there’s two final steps: 

1. Save the filters, so you can repeat this search query later. 
2. Download the list, so you can run whatever final filters on the CSV file before dividing it up amongst your Sales team. 

Using all these steps, you’ll set yourself up for the greatest chance of success in curating and delivering a high quality lead list. If you run into any errors, or have other questions about the results you see, don’t hesitate to [reach out to us](mailto:support@shovels.ai).

## Tips and Tricks

The general tutorial above should get most people 95% of the way there. However, there are a few nifty tricks and optimizations that may be useful to you. As the Shovels Online platform grows and matures, and our engineers get to deliver on the functionality they’ve been dreaming up, expect this “Tips and Tricks” list to only grow from here!

### Smart Exporting

By default, the “Download List” button caps out at 1000 rows in CSV file. If you want to get more than 1000, then you can slightly adjust the filters (such as geography) to get a new set of 1000 rows. With some quick combination and deduplication, you can easily build a Frankenstein lead list of as many rows as you can find. 

We will note that this **is not** suggested at scale. If you’re finding yourself working at such volumes, we highly suggest checkout our our API, which is purpose-built for those kinds of loads. Plus, there are even more filters for even better search results.

### Saving Your Work

With Shovels Online we introduced the Saved Profiles feature, which allows you to favorite and save individual permits, contractors, or geographies for easy and convenient future access. Beyond that, you can also save the exact filters and search parameters you’ve been working on already. 

So once you’ve fine tuned your super query that fits the exact model and needs of your team, never fear of needing to recreate it later. It’ll be there, under `Saved Filters`, for next time.

## Get In Now!

As we mentioned at the top, this is an exciting time to be using [Shovels Online](https://app.shovels.ai). If you want to lock-in our old pricing then be sure to [reach out to our Sales team](mailto:sales@shovels.ai) for help getting your account set up and your discount confirmed.

On the other hand, if you’re new here (welcome!) and interested in our platform, then we’d love to chat more about your specific use case and learn what permit data means to you. 

We hope that this tutorial is helpful, and Happy Digging!

## Frequently Asked Questions

**Q: What are the main use cases for Shovels Online?**

A: The main use cases are generating homeowner leads (finding addresses with permit activity that signals buyer intent), generating contractor leads (finding contractors by experience level and market area), and derivative analysis like permit approval timing and resident demographics.

**Q: How do I build a high-quality search on Shovels Online?**

A: Start by choosing your geography scale (state level for niche project types, zip code for common ones). Decide whether you are searching for permits or contractors based on your target persona. Apply key filters like minimum market value, lot size, or permit description keywords. Then spot-check results by clicking View Details on a few entries to verify accuracy.

**Q: Is there a limit on how many records I can download from Shovels Online?**

A: The Download List button caps at 1,000 rows per CSV export. To get more, adjust your filters slightly (such as changing geography) to generate a new set of 1,000 rows, then combine and deduplicate. For larger-scale needs, the Shovels API is recommended.

**Q: Can I save my search filters in Shovels Online for later use?**

A: Yes. Shovels Online includes a Saved Filters feature that lets you save your exact search parameters so you can re-run the same query later without rebuilding it. You can also save individual permits, contractors, or geographies as Saved Profiles for quick future access.

<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are the main use cases for Shovels Online?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The main use cases are generating homeowner leads (finding addresses with permit activity that signals buyer intent), generating contractor leads (finding contractors by experience level and market area), and derivative analysis like permit approval timing and resident demographics."
      }
    },
    {
      "@type": "Question",
      "name": "How do I build a high-quality search on Shovels Online?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start by choosing your geography scale (state level for niche project types, zip code for common ones). Decide whether you are searching for permits or contractors based on your target persona. Apply key filters like minimum market value, lot size, or permit description keywords. Then spot-check results by clicking View Details on a few entries to verify accuracy."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a limit on how many records I can download from Shovels Online?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Download List button caps at 1,000 rows per CSV export. To get more, adjust your filters slightly (such as changing geography) to generate a new set of 1,000 rows, then combine and deduplicate. For larger-scale needs, the Shovels API is recommended."
      }
    },
    {
      "@type": "Question",
      "name": "Can I save my search filters in Shovels Online for later use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Shovels Online includes a Saved Filters feature that lets you save your exact search parameters so you can re-run the same query later without rebuilding it. You can also save individual permits, contractors, or geographies as Saved Profiles for quick future access."
      }
    }
  ]
}
</script>