#!/usr/bin/env python3
"""
Populate faq_data.json with FAQ content from research agent outputs.
This script contains the extracted FAQ data embedded directly.
"""

import json
from pathlib import Path


# FAQ data extracted from research agent outputs
FAQ_DATA = {
    # Data category posts - batch 1 (remaining from a8023be)
    "content/posts/spi-q2-2025.md": {
        "insert_after": "These aren't just statistics—they're signals of where the market is heading. As permitting processes become more efficient in places like North Carolina, and as contractors like DRB Group and Shea Homes show triple-digit quarterly growth, we're seeing the industry's remarkable ability to evolve. From ADUs in Wayne County to climate-adapted roofing in Florida, each permit represents concrete market intelligence you can use to make smarter business decisions.",
        "faqs": [
            {
                "q": "Which permit types are most common in Q2 2025?",
                "a": "Electrical permits led with 106,784 filings (21.21% of total permits), followed by plumbing at 72,957 (14.49%) and HVAC at 72,874 (14.48%). Together, these three essential building systems represent over 50% of all permit activity in Q2 2025."
            },
            {
                "q": "Which states dominate building permit activity in Q2 2025?",
                "a": "Florida leads with 138,742 permits (19.48%), followed by Texas with 120,127 (16.87%) and California with 91,897 (12.91%). These three states alone account for nearly half of all permits issued nationwide."
            },
            {
                "q": "What is the median permit processing time for different project types?",
                "a": "Processing times vary significantly by project complexity. Simple permits like plumbing, HVAC, and heat pumps take a median of 1 day. Roofing and gas permits take 2 days. More complex projects take longer: solar installations take 7 days, new construction takes 18 days, and ADUs require 19 days."
            },
            {
                "q": "Which states lead in new construction as a percentage of total permits?",
                "a": "West Virginia leads at 34.67% of its permits going to new construction, significantly above the national average of 9.39%. Delaware follows at 25.32%, Mississippi at 20.47%, and Idaho at 17.98%. These rankings reveal significant construction activity in previously overlooked states."
            },
            {
                "q": "Where are ADU permits being issued the most?",
                "a": "Los Angeles County dominates with 2,243 ADU permits in Q2 2025, nearly 10 times more than the second-ranking county (Harford County, MD with 259). Florida appears four times in the top 10 (Escambia, Lee, Santa Rosa, and Indian River counties), suggesting strong ADU growth in that state."
            }
        ]
    },
    "content/posts/spi-q3-2025.md": {
        "insert_after": "Q3 2025 permit data shows construction capital flowing toward infrastructure supporting technological and energy transitions: data centers powering AI, battery systems stabilizing grids, EV chargers supporting electrified transportation, and essential building systems keeping properties functional. The markets facilitating this construction most efficiently are pulling ahead.",
        "faqs": [
            {
                "q": "How many building permits did Shovels track in Q3 2025?",
                "a": "Shovels recorded 515,912 permits in Q3 2025 (July 1 - September 30). Of these, 83.94% were active (in-progress), 14.41% were final (fully processed), and the remainder were in review, inactive, or had no status assigned."
            },
            {
                "q": "Which states have the highest construction intensity per capita in Q3 2025?",
                "a": "North Carolina leads the nation at 452 permits per 100,000 residents, followed by Virginia (393), Nevada (352), Nebraska (345), and Florida (344). This per capita view reveals a different picture than raw permit counts, showing states like Nebraska and South Dakota punching well above their population weight."
            },
            {
                "q": "How significant is data center construction activity in Q3 2025?",
                "a": "Q3 2025 saw 234 data center related permits issued nationwide. Virginia alone accounted for 52.6% of all data center permits, with Loudoun County pulling 84 permits (35.9% of the national total). Global data center demand is expected to triple by 2030, driven primarily by AI workloads."
            },
            {
                "q": "What does the battery storage permit data reveal about renewable energy trends?",
                "a": "In Q3 2025, 9,098 battery storage permits were issued. California dominates with 6,764 permits (74% of all national battery storage permits). Hawaii leads in adoption intensity, with 37.7% of all permits involving battery storage, driven by high electricity costs and grid independence goals."
            },
            {
                "q": "How fast are EV charger permits being approved, and is permitting reform making a difference?",
                "a": "The median approval duration for EV charger permits nationwide is just 1 day, though the mean is higher due to outliers. California's permitting reforms, including AB 1236 (2015) and AB 970's shot clock mechanism (2021), appear to be working. Mean approval times have decreased significantly over the past five years, and California accounts for 46.8% of all EV permits in the database."
            }
        ]
    },
    "content/posts/ev-charger-contractors.md": {
        "insert_after": "We're excited by all of this data, and we want you to be excited too. Want to do your own epic analysis of the building trades? Get in touch: sales@shovels.ai.",
        "faqs": [
            {
                "q": "Which California jurisdictions have the most active EV charger contractors?",
                "a": "Sacramento County leads with 429 active EV charger contractors since 2022, followed by Berkeley (209), Encinitas (203), Oakland (140), and Anaheim (119)."
            },
            {
                "q": "Is the number of EV charger contractors in California growing?",
                "a": "Yes. In Sacramento, approximately one new EV charger contractor becomes active each quarter, and in Berkeley the rate is about 1.5 new contractors per quarter. Jurisdictions with fewer contractors are seeing even faster growth rates, with dramatic recent increases in Anaheim, Sacramento, and Oakland."
            },
            {
                "q": "What share of US EV chargers are installed in California?",
                "a": "Nearly 30% of all EV chargers in the US are installed in California. The next largest states by share are New York, Florida, Texas, Massachusetts, and Washington, which collectively account for about 25%."
            },
            {
                "q": "Are EV charger contractors expanding into multiple jurisdictions?",
                "a": "Yes. The percentage of EV contractors working across multiple jurisdictions has been trending upward, with a significant surge during COVID that sustained even after the pandemic subsided. This geographic expansion is another indicator of market growth."
            }
        ]
    },
    # Data category posts - batch 2 (from aaee810)
    "content/posts/ev-charger-growth.md": {
        "insert_after": "To learn more about how you can use the Shovels building permit API to access monthly energy transition activity data and build applications related to this area, check out our documentation at [https://docs.shovels.ai/api-reference](https://docs.shovels.ai/api-reference)!",
        "faqs": [
            {
                "q": "How fast is EV charger installation growing in California?",
                "a": "The compound annual growth rate (CAGR) for EV charger permits in California from 2012 to 2022 was approximately 38.76%. Based on monthly data, Shovels projected roughly 11,000 permits in 2023 (a 40% increase over 2022) and 13,000 in 2024 (another 20% jump)."
            },
            {
                "q": "Is there a seasonal pattern to EV charger permit filings in California?",
                "a": "Yes. The months of August, September, and October tend to have the highest average number of permits. Permit volumes are generally lower at the start of the year and increase as the year progresses."
            },
            {
                "q": "What types of energy transition data does the Shovels building permit API cover?",
                "a": "Beyond EV charger installations, the Shovels API covers wall battery permits, heat pump HVAC conversions, solar panel installations, and other energy transition activities. Users can query by the type of work involved."
            },
            {
                "q": "How can businesses use EV charger permit data?",
                "a": "Businesses can use residential EV charger permit data to identify optimal locations for commercial charging stations, perform stress tests on the electrical grid, generate targeted sales leads, and predict future demand for electric vehicles."
            }
        ]
    },
    "content/posts/ev-permit-approvals.md": {
        "insert_after": "Phew! That was a lot of information about EV charger approval times. It seems we're still just scratching the surface. If you want to do more analysis, [let us know](https://www.shovels.ai/contact). We have lots of data.",
        "faqs": [
            {
                "q": "Which California jurisdictions have the fastest EV charger permit approval times?",
                "a": "Oakland leads with a median approval time of just 3 days, followed by Dublin (4 days), El Dorado County (5 days), Sacramento (5 days), and San Diego County (5 days). Most of the fastest jurisdictions are in Northern California."
            },
            {
                "q": "Which California jurisdictions have the slowest EV charger permit approval times?",
                "a": "Los Angeles has the slowest median approval time at 93 days, followed by San Francisco (70 days), Santa Ana (64 days), Santa Monica (64 days), and Pasadena (60 days). Four of the five slowest jurisdictions are in Southern California."
            },
            {
                "q": "Is there a difference in EV charger permit approval times between Northern and Southern California?",
                "a": "Yes. The data shows a clear regional pattern: Northern California jurisdictions issue EV charger permits significantly faster than Southern California jurisdictions."
            },
            {
                "q": "Does processing more permits cause longer approval times?",
                "a": "No. The analysis found essentially no correlation between the volume of permits a jurisdiction processes and its approval speed. The Pearson correlation coefficient was -0.073, indicating a very weak relationship. Jurisdictions that handle more permits do not necessarily take longer to approve them."
            },
            {
                "q": "Did COVID-19 affect EV charger permit approval times in California?",
                "a": "Surprisingly, permit processing times actually improved after COVID across California jurisdictions. Some areas like Riverside County saw skyrocketing permit volumes during the pandemic but managed to keep processing times down, suggesting they implemented streamlining reforms."
            }
        ]
    },
    "content/posts/virginia-data-center-report.md": {
        "insert_after": "Start digging our data with a [free online Shovels account](https://app.shovels.ai/), or [contact us](https://www.shovels.ai/contact) today to get started.",
        "faqs": [
            {
                "q": "What share of U.S. data center permits does Virginia account for?",
                "a": "Between July 2024 and July 2025, Virginia issued 1,239 permits explicitly linked to data centers, representing approximately 80.4% of all such permits nationwide."
            },
            {
                "q": "Why is Loudoun County the center of data center development?",
                "a": "Loudoun County accounts for nearly 90% of Virginia's data center permits. Its dominance is driven by established infrastructure, proximity to major internet exchange points, robust power availability, and supportive local policies."
            },
            {
                "q": "What are proxy indicators for identifying hidden data center permits?",
                "a": "Many data center permits do not explicitly mention data center in their descriptions. Key proxy indicators include high-amperage electrical references (e.g., 4000A service), data hall terminology, critical power infrastructure like UPS systems, specialized cooling systems (CRAH units, chillers), and phased development patterns with sequential electrical buildouts."
            },
            {
                "q": "How much data center activity in Virginia is hidden from standard permit searches?",
                "a": "Analysis suggests the true scale of data center construction in Virginia may be 15-20% higher than official counts. At some locations, up to 90% of data center-related permits do not explicitly mention data center. Extrapolating statewide, an additional 185-250 permits may be data center-related but hidden."
            },
            {
                "q": "What types of permits dominate Virginia's data center construction?",
                "a": "Infrastructure upgrades account for nearly 50% of all permits, with electrical permits alone comprising over 27% (339 total). The most common permit types are electrical commercial alterations (132), new electrical infrastructure (116), and mechanical upgrades (76). New ground-up construction accounts for about 22.5% of permits."
            }
        ]
    },
    "content/posts/digging-in-1-solar-trends.md": {
        "insert_after": "Happy Digging, and let us know how you enjoyed RE+ in Anaheim this year!",
        "faqs": [
            {
                "q": "What is the average solar permit approval time in California?",
                "a": "California has an average solar permit approval time of 6.15 days statewide. Some hotspots perform even better, with San Diego County leading at a 1.79-day average."
            },
            {
                "q": "Where is most U.S. solar construction activity concentrated?",
                "a": "The vast majority of solar construction activity is in California, which has led the nation in solar adoption for decades. Key hubs include Los Angeles, San Diego, San Jose, and areas in the Central Valley."
            },
            {
                "q": "Is solar construction still growing in California?",
                "a": "Solar construction in California saw its biggest peak in March 2023 with over 33,000 solar-inclusive project permits filed in a single month. The trendline since then shows a slight slowdown compared to those highs, but activity remains substantial. Seasonal spikes occur before and after summer."
            },
            {
                "q": "What types of solar permit data does Shovels provide?",
                "a": "Shovels aggregates and normalizes solar construction data that can be queried by market, geographic region, address, permit type, contractor, and other fields. The data covers everything from small residential solar panel installations to large commercial solar arrays, and includes metrics like permit volume, approval times, and contractor profiles."
            }
        ]
    },
    "content/posts/analysis-texas-roofing-income.md": {
        "insert_after": "Happy Digging!",
        "faqs": [
            {
                "q": "What is the relationship between household income and roofing permit activity in Texas?",
                "a": "There is a clear positive correlation. Low-income areas (under $30k/year) average 0.21 roofing permits per household, while high-income areas (over $150k/year) average 0.51 permits per household. The wealthiest 28% of areas account for 74% of all roofing permits."
            },
            {
                "q": "Why do higher-income areas pull more roofing permits?",
                "a": "Several factors contribute: better access to financial resources and favorable loan terms, a tendency toward regular roof inspections and preventative maintenance, use of higher-quality materials, and viewing home improvements as strategic investments. Essentially, wealthier homeowners can afford to pay more upfront, which is cheaper in the long run."
            },
            {
                "q": "What does this data mean for lower-income homeowners?",
                "a": "The data highlights a significant disparity. Over 72% of Texas census tracts fall below the upper-middle income bracket, and these areas are underrepresented in roofing permits relative to their household count. This suggests lower-income homeowners may lack the resources for critical roof maintenance, which affects home value, structural integrity, and energy efficiency."
            },
            {
                "q": "How many census tracts were analyzed in this study?",
                "a": "The study examined more than 3,200 census tracts across Texas, combining roofing permit data with owner demographics and income bracket information."
            },
            {
                "q": "What policy recommendations emerge from this analysis?",
                "a": "The analysis recommends implementing policy measures to support roofing repairs in lower-income areas, developing contractor education about government-backed programs, providing more accessible financing options, and creating cross-industry partnerships among banks, non-profits, and businesses to help homeowners maintain their homes."
            }
        ]
    },
    "content/posts/bayren-affiliations.md": {
        "insert_after": "The shifts we see today, influenced by BayREN's strategic decisions, are creating a blueprint for other regions to follow. And as we continue to gather data and analyze trends, we look forward to contributing the conversation around proptech and sustainability.",
        "faqs": [
            {
                "q": "What is BayREN and what role does it play in Bay Area energy upgrades?",
                "a": "The Bay Area Regional Energy Network (BayREN) is a key player in building electrification in the San Francisco Bay Area. Over the past decade, it has fostered environmentally conscious decisions among communities and building contractors, strategically focusing on technologies where the market needs the most support."
            },
            {
                "q": "Do BayREN-affiliated contractors install more heat pumps than non-affiliated contractors?",
                "a": "Yes. The data shows that BayREN-affiliated contractors install significantly more heat pumps than non-affiliated contractors, reflecting BayREN's strategic priority to promote this dual-purpose heating and cooling technology that cuts overall energy use compared to traditional HVAC systems."
            },
            {
                "q": "Why do BayREN contractors install fewer solar panels than other contractors?",
                "a": "This likely reflects BayREN's strategy of filling gaps in the building electrification market. The solar market in the Bay Area may already be well-developed with optimized financial incentives, so BayREN focuses its resources on technologies like heat pumps that have yet to reach the same level of market maturity."
            },
            {
                "q": "How do EV charger installation rates compare between BayREN and non-BayREN contractors?",
                "a": "EV charger installation numbers are closely aligned between BayREN-affiliated contractors and non-affiliated contractors. This suggests the push for EV infrastructure is equally strong across the board, with BayREN's efforts complementing an already thriving market driven by statewide initiatives and private investment."
            }
        ]
    }
}


def main():
    """Write FAQ data to JSON file."""
    output_file = Path(__file__).parent / "faq_data.json"

    # Load existing data
    existing_data = {}
    if output_file.exists():
        with open(output_file) as f:
            existing_data = json.load(f)

    # Merge with new data (new data takes precedence)
    merged_data = {**existing_data, **FAQ_DATA}

    # Write back
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=2)

    print(f"✅ Updated {output_file}")
    print(f"📊 Total entries: {len(merged_data)}")
    new_count = len(FAQ_DATA)
    print(f"🆕 New entries added: {new_count}")


if __name__ == "__main__":
    main()
