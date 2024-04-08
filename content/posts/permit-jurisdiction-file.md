Title: The list of every building permit jurisdiction in the US
Subtitle: We are open-sourcing our database of every building permit jurisdiction in the United States
Date: 2024-4-6
Modified: 2024-4-6
Category: Data
Tags: building permits, AHJ, permit jurisdiction
Authors: Ryan Buckley
Summary: Shovels is open-sourcing of a comprehensive list of building permit jurisdictions that we discovered only recently. Our new database includes over ten thousand building permit jurisdictions and associates each jurisdiction with a county and state.
Slug: list-of-all-building-permit-jurisdictions
Image: /images/building-permit-list.png


We are thrilled to announce another open-source dataset from the Shovels vault. Our latest file is a comprehensive mapping of state, county, and building permit jurisdictions.

## What is this list of building permit jurisdictions?

Our dataset includes over 10,000 building permit jurisdictions (AHJ's -- authority-having jurisdictions), and relates each jurisdiction to its respective state and county. 

We found this mapping buried in an obscure government website. We noticed that when we clicked on a state, a select box appeared with all of the counties in that state. This mapping is widely available from the US Census and many other open data sources. 

But when we clicked on the county, another select box appeared with every building permit jurisdiction in the county. *That* got our attention. Before this discovery, we didn't know of a single source of truth for how many AHJ's are out there for building permits. Now we can count at least 10,000 of them.

## Who needs a list of every building permit jurisdiction? 

When architects, developers, and homeowners start a new project, the first question they might ask is, "Where do I file my building permits?" The answer is far from obvious; many cities don't have building departments; they delegate building permitting to the county.

The list we are open-sourcing today includes every building permit jurisdiction. If a city or town is on this list, then they issue their own building permits. If a city or town is not on this list, then it's safe to conclude that their AHJ is the county. 

We figure many folks who work in cities and counties don't know every AHJ within their boundaries. Now they do.

## How many building permit jurisdictions are in each state? 

We got curious and decided to ask this data a few questions. How many AHJ's are in each state? Does that jurisdiction correlate with population? We had to merge in some public census data to figure this out. 

On average, there are about ten permit jurisdictions per county. If a county has a million residents, that means each permit jurisdiction serves about 100,000 people. 

Pennsylvania stands out with the highest number of permit jurisdictions, totaling 1575. No other state comes close! It's unclear why Pennsylvania needs so many of them. For example, although Pennsylvania has the same population as Ohio, it has almost 3X the number of building permit jurisdictions. 

This chart makes the outliers easy to see.

![Population vs Jurisdiction Count]({static}/images/jurisdictions-vs-population.png)

Here's a table of every state, its population, number of jurisdictions, and the ratio of jurisdictions per 100,000 residents.

| State                |   Population |   Permit Jurisdictions |   Jurisdictions per 100,000 Residents |
|:---------------------|-------------:|-----------------------:|--------------------------------------:|
| Alaska               |       733406 |                      7 |                              0.954451 |
| Alabama              |      5108468 |                    200 |                              3.91507  |
| Arkansas             |      3067732 |                    110 |                              3.58571  |
| Arizona              |      7431344 |                     76 |                              1.0227   |
| California           |     38965193 |                    471 |                              1.20877  |
| Colorado             |      5877610 |                    113 |                              1.92255  |
| Connecticut          |      3617176 |                    137 |                              3.78749  |
| District of Columbia |       678972 |                      1 |                              0.147281 |
| Delaware             |      1031890 |                     20 |                              1.93819  |
| Florida              |     22610726 |                    389 |                              1.72042  |
| Georgia              |     11029227 |                    307 |                              2.78351  |
| Hawaii               |      1435138 |                      2 |                              0.139359 |
| Iowa                 |      3207004 |                    235 |                              7.32771  |
| Idaho                |      1964726 |                     75 |                              3.81733  |
| Illinois             |     12549689 |                    696 |                              5.54595  |
| Indiana              |      6862199 |                    227 |                              3.30798  |
| Kansas               |      2940546 |                    172 |                              5.84925  |
| Kentucky             |      4526154 |                    135 |                              2.98266  |
| Louisiana            |      4573749 |                    164 |                              3.58568  |
| Massachusetts        |      7001399 |                    317 |                              4.52767  |
| Maryland             |      6180253 |                     74 |                              1.19736  |
| Maine                |      1395722 |                    131 |                              9.38582  |
| Michigan             |     10037261 |                    659 |                              6.56554  |
| Minnesota            |      5737915 |                    474 |                              8.26084  |
| Missouri             |      6196156 |                    340 |                              5.48727  |
| Mississippi          |      2939690 |                     75 |                              2.55129  |
| Montana              |      1132812 |                     21 |                              1.85379  |
| North Carolina       |     10835491 |                    226 |                              2.08574  |
| North Dakota         |       783926 |                     72 |                              9.18454  |
| Nebraska             |      1978379 |                     95 |                              4.80191  |
| New Hampshire        |      1402054 |                     81 |                              5.77724  |
| New Jersey           |      9290841 |                    572 |                              6.1566   |
| New Mexico           |      2114371 |                     20 |                              0.945908 |
| Nevada               |      3194176 |                     11 |                              0.344377 |
| New York             |     19571216 |                    906 |                              4.62925  |
| Ohio                 |     11785935 |                    586 |                              4.97203  |
| Oklahoma             |      4053824 |                    129 |                              3.18218  |
| Oregon               |      4233358 |                    130 |                              3.07085  |
| Pennsylvania         |     12961683 |                   1575 |                             12.1512   |
| Rhode Island         |      1095962 |                     39 |                              3.55852  |
| South Carolina       |      5373555 |                    152 |                              2.82867  |
| South Dakota         |       919318 |                     58 |                              6.30902  |
| Tennessee            |      7126489 |                    194 |                              2.72224  |
| Texas                |     30503301 |                    651 |                              2.1342   |
| Utah                 |      3417734 |                    141 |                              4.12554  |
| Virginia             |      8715698 |                    115 |                              1.31946  |
| Vermont              |       647464 |                     40 |                              6.17795  |
| Washington           |      7812880 |                    201 |                              2.57267  |
| Wisconsin            |      5910955 |                    530 |                              8.9664   |
| West Virginia        |      1770071 |                    115 |                              6.49691  |
| Wyoming              |       584057 |                     12 |                              2.05459  |

## Conclusion

Our mission is to make government data meaningful and actionable. Our tools and datasets, like the one we're open-sourcing today, are designed to make government data useful. We hope this helps. 

Stay tuned for updates and join us in shaping the future of building permit data! Explore the dataset, unleash its potential, and let's do great things together.

--

Oh, you probably wanted the data. 

See it [on Kaggle](https://www.kaggle.com/datasets/rbucks/building-permit-jurisdictions-in-the-united-states) or [download the CSV]({static}/images/jurisdiction_mappings.csv).


