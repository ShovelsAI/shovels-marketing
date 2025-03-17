Title: Top 5 Most Useful Derived Metrics
Subtitle: Learn about the most insightful construction metrics that are unique to the Shovels platform.
Date: 2025-03-13
Modified: 2025-03-13
Category: Customer Success
Tags: Metrics
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: Shovels provides a wide variety of construction data, including uniquely derived metrics that aren't available elsewhere. These five metrics are very useful for deeper insights into construction activity. Best practice is to combine these metrics with detailed filters for maximum impact.
Image: /images/top-5-derived-metrics-hero.png

Construction data is all about translating how different regulatory bodies define the same data, and then making the analysis from there. Sometimes it’s easy with things like `address` or `assessed market value` or even `homeowner name`. These data points are straightforward and intuitive, which makes the analysis that much easier. 

On the other hand are what we call *derived metrics*: data that’s there in the public record if you put the puzzle pieces together. Extrapolation is a core tenet of data science, and today we’re going to highlight the five most useful derived metrics in the Shovels platform. 

Technically speaking anyone with the same breadth of nationwide data could do the same. However, we’ve *already* done so, and made it accessible too. It’s not ground-breaking, but it is convenient.

## Average Approval Duration

**Average Approval Duration** measures the time (in `days`) between when a permit is filed and when it is approved (`issue_date` minus `file_date`), averaged across the given subset. 

In a **Contractor search**, this could indicate how well the specified contractor prepares their paperwork. For best comparison, make sure you’re looking at similar project types in the same permit jurisdiction. 

In a **Geography search**, this could indicate jurisdiction (or whichever scale of governing body selected) efficiency in managing their incoming permits. Administrators within (or without) can use this metric as a stepping stone for further analysis of competency, staffing, or procedural issues that might be inhibiting the general construction process.

`avg_approval_duration` is a convenient shortcut to running all these queries and averages on your own, or a shorthand for how efficiently work is getting done.

## Average Construction Duration

**Average Construction Duration** measure the time (in `days`) between when a permit is filed and when it is marked as “finaled” (`final_date` minus `file_date`), averaged across the given subset.

This derived metric focuses on the entire construction process more broadly, and is a more results-based metric for analyzing contractor or homeowner (or in extreme cases, permit jurisdiction) efficiency.

One the other hand, we have seen this used in interesting market analysis for construction trends in high-value areas. Abnormally long construction durations could indicate loophole usage to maintain the development rights to a property without the full cost and labor of *actually completing the project**.*** 

`avg_construction_duration` is the older sibling to `avg_approval_duration` above, where it’s main differentiation is an increase in scope. It’s best used in combination with other factors or in highly defined queries to filter out the noise and variability of an entire construction project.

## Average Inspection Pass Rate

**Average Inspection Pass Rate** is the percentage (multiplied by 100, so 75% would return as `75`) of inspections passed compared with inspections made. 

This is a very simple derived metric, but can even more insightful for contractor efficiency. The higher the number (especially as `permit_count` increases) the smoother the construction process, which is a good thing for everyone involved.

## First Seen Date

**First Seen Date** is used for both `Permits` and `Contractors`, to similar effects. 

For `Contractors`, it refers to the first time a given contractor appears in our system as recorded on a permit. If you’re looking to target *new* contractors, this is a key metric. 

For `Permits`, it refers to the date the permit was added into the wider Shovels platform. This is primarily helpful for understanding any digitization delays on the side of the permit jurisdiction office, or just to understand when historical permit data is added after the fact. 

If the `first_seen_date` and `file_date` are roughly a month apart (our current refresh rate), then you know the data is as fresh as can be and the underlying permitting office is maintaining good digitization practices.

## Permit Count

**Permit Count** is the simplest of the derived metrics we cover in this blog, but it’s by far the most widely usable. It is a summary and count of permits filed for a certain person or place, plain and simple. 

However, for all it’s simplicity it’s one that’s difficult to find through the raw public record. With Shovels, `permit_count` is a record of construction activity (and by extension, all the other extrapolated market indicators that construction activity can signal) for a given area or contractor.

## Explore today!

We like to think of ourselves as an insights company more than a raw data company. We make the easy and useful connections internally and deliver them to anyone that wants them. If we can save you the time and effort, then we’re doing our part. 

These derived metrics are available throughout our entire platform.

In it’s simplest form, our [Shovels Online](https://app.shovels.ai) dashboard and web application allows you to search for Permits or Contractors and then see all the nested details beneath. 

For a more detailed (and programmatic) view, explore our [API](https://docs.shovels.ai/docs/shovels-api-introduction). 

If you have any questions, or want a sample dataset for your team to explore, [get in touch today](mailto:sales@shovels.ai)!