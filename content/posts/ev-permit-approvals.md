Title: EV charger permit processing times in California
Subtitle: There's a wide disparity in the time it takes for EV charger permits to get approved in California. 
Date: 2023-8-10
Modified: 2023-8-10
Category: Data
Tags: gtm, building permits, ev chargers, permit timeline
Authors: Ryan Buckley
Summary: There's a wide disparity in the time it takes for EV charger permits to get approved in California. Some jurisdictions are 10X slower than others, and we'll share which are fastest and slowest to approve EV charger permits in California.


## Background on EV charging in California

In keeping with our thinking about EV chargers, which you can [read more about here]({filename}ev-charger-growth.md), we're turning our attention now to how long it takes for jurisdictions to approve EV charger permits.

First, let's take a step back. This analysis is important because California has committed to deploying five million zero-emission vehicles (ZEVs) and building out 250,000 charging stations by 2025. This includes building a network of nearly 20,000 Level 2 and DC fast EV charging stations across the state. Additionally, the state plans to invest $2.5 billion over the next five years to expand the EV charging infrastructure and provide incentives for drivers to purchase electric vehicles.

Having more residential EV chargers would make it easier for California residents to own and use electric vehicles. This would also relieve the burden on public EV chargers. The more EV chargers we have in homes, the less strain on the public chargers required for people who live in multifamily housing and don't have a dedicated charger.

More residential EV chargers also creates more jobs and boost the economy. Installation and maintenance of these chargers increases demand for electricians, supporting many local businesses. 

## Potential for building permit reform

One way to get more EV chargers installed is to streamline the permitting process. EV chargers, because they are high-voltage, require a licensed electrician and a building permit to begin the installation, and an inspector must approve it.

While this process can be cumbersome, building permits exist to ensure that construction projects adhere to local safety and building codes. This is important for protecting the public and ensuring that buildings are safe and structurally sound. Building permits also provide a way for local governments to track construction projects and collect fees to help fund public services.

Some people advocate permitting reform because the current permitting process is overly burdensome, time consuming, and costly, leading to delays and inefficiencies. Permitting reform may reduce the time and cost of obtaining permits, and make it easier for businesses and homeowners to quickly obtain the necessary approvals to install appliances like EV chargers. 

Okay, with that background, let's look at the data in California. 

## Shovels analysis of EV charger permit approval times

Shovels collects and analyzes building permit data. Two data points that we consistently see are the file date, or when the permit was submitted to the jurisdiction, and the issue date, or when the jurisdiction approved the permit. At this point, work can begin, and we'll eventually see the final date, or when the work was completed. 

The file date and the issue date show how long it takes for a jurisdiction to process a permit. As anyone who has had work done knows, this can be an agonizing process. The longer the delay, the more likely your contractor will get busy or supply costs will increase. Homeowners and contractors both want faster permit approval times. 

With that in mind, we set out to ask a few questions:

### Differences between jurisdictions

_Jurisdiction comparison: Which jurisdictions have the fastest and slowest average EV permit approval times? How do they compare to each other?_

_Are there differences in permit approval times between Northern and Southern California?_

Here are the jurisdictions with the SLOWEST EV median charger permit approval times. We go with the median because there are outliers in the data that will skew the mean. You can see this in the table below, which shows that the mean is greater than the median in each case. The standard deviation and IQR (interquartile range) also demonstrate the skew. Therefore, the median is our best way to compare jurisdictions.

It's interesting that four of the five slowest permitting jurisdictions are in Southern California. The median approval times are at least two months. That's too long! 

| Jurisdiction   | Count | Mean   | Standard Deviation | Median | Q1   | Q3   | IQR  |
| -------------- | ----- | ------ | ------------------ | ------ | ---- | ---- | ---- |
| Los Angeles    | 402.0 | 151.36 | 152.31            | 93.0  | 37.25 | 227.0 | 189.75 |
| San Francisco  | 68.0  | 194.26 | 460.07            | 70.0  | 11.0  | 203.25 | 192.25 |
| Santa Ana      | 72.0  | 99.71  | 117.26            | 64.0  | 31.0  | 103.0  | 72.0 |
| Santa Monica   | 235.0 | 96.28  | 88.62             | 64.0  | 41.0  | 121.0  | 80.0 |
| Pasadena       | 80.0  | 100.08 | 111.54            | 60.0  | 35.5  | 125.25 | 89.75 |

![Worst EV charger permit times]({static}/images/top5.png)

Looking now at the FASTEST EV charger timing jurisdictions, we see median times of less than a week. Interstingly, all but one of the jurisdictions is in Northern California. Even the averages here are reasonable, coming in at less than a month in the top four, but jumping to nearly three months average in San Diego. 

| Jurisdiction | Count | Mean | Standard Deviation | Median | Q1 | Q3 | IQR |
|---|---|---|---|---|---|---|---|
| Oakland | 817.0 | 17.20 | 40.06 | 3.0 | 1.0 | 10.0 | 9.0 |
| Dublin | 94.0 | 36.00 | 108.14 | 4.0 | 1.0 | 17.75 | 16.75 |
| El Dorado County | 266.0 | 13.96 | 34.67 | 5.0 | 2.0 | 11.0 | 9.0 |
| Sacramento | 846.0 | 21.29 | 48.47 | 5.0 | 2.0 | 16.0 | 14.0 |
| San Diego County | 89.0 | 89.07 | 151.01 | 5.0 | 1.0 | 119.0 | 118.0 |

![Best EV charger permit times]({static}/images/bottom5.png)

Here again, we see the apparent impact of outliers. San Diego has a media approval time of five days, but an average of three months. A few crazy long wait times down there are pulling the average away from the median.

![Histogram of San Diego EV charger permit approval times]({static}/images/sd-histogram.png)

Just because it was interesting, to further investigate this distinction between Northern California and Southern California, we made one more chart. It tells the story that emerged just by looking at the top 5 and bottom 5 jurisdictions: Northern California issues EV charger permits faster than Southern California. 

![Northern CA vs Southern CA]({static}/images/norcal-v-socal.png)

The fatness of the bottom of the candlestick shows the bottom and top quartile wait times. A smaller candle is better. 

### Trends over time

_How has the average EV permit approval time changed over the years for each jurisdiction? Are there any jurisdictions where the approval time is consistently getting faster or slower?_

_Are there certain times of the year when EV permit approval times are generally faster or slower? This could indicate seasonal workload fluctuations in permit offices._

To answer these questions, we looked for jurisdictions where permit approval times are getting worse and others where they are getting better. Bucking the NorCal/SoCal trend described above, we found that permit times are getting better in Riverside County and worse in Milpitas.

![Riverside County approval times by year]({static}/images/riverside-county.png)
![Milpitas approval times by year]({static}/images/milpitas.png)

The permit counts by year for each county might give some clues as to what's going on. 

![Riverside County and Milpitas EV charger permit counts by year]({static}/images/riverside-milpitas-count.png)

By the looks of these three charts, we find that the number of EV charger permits in Riverside County skyrocketed during the pandemic, and the jurisdiction must have put some permit streamlining reforms in place because despite the higher volume, they kept the processing times down. This combination led to a precipitous drop in permit approval times.

In fact, the COVID question was interesting, so we looked across the board and came up with this chart. The processing times actually improved after COVID. 

![Impact of COVID on permit approval times in California]({static}/images/covid.png)

### The relationship between permit volume and approval times

_Is there a correlation between the number of permits a jurisdiction processes and the speed of approval? In other words, do jurisdictions that process more EV permits tend to approve them faster or slower?_

This result surprised. We assume that bureaucratic government departments are easily overwhelmed. As the number of permit applications increases, we expect that approval times would get slower. In fact, there's no relationship between the volume of permits and the processing times across the jurisdictions in California.

![Scatter of approval times and volumes]({static}/images/approval-times-scatter.png)

The Pearson correlation coefficient here is −0.0730. This value indicates a very weak negative relationship. In other words, there's actually a slight tendency for jurisdictions that process more EV permits to approve them a bit faster, but the relationship is weak.

Phew! That was a lot of information about EV charger approval times. It seems we're still just scratching the surface. If you want to do more analysis, [let us know](https://www.shovels.ai/contact). We have lots of data. 






