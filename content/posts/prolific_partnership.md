Title: Unlocking Shovels's Potential with Prolific
Subtitle: Learn how the Shovels team built their LLM training sample. 
Date: 2024-09-26
Modified: 2024-09-29
Category: Company
Tags: AI, Machine Learning, Partnership
Authors: Alex Brown
Summary: The Shovels data engineering team partnered with Prolific to crowdsource data analysis experts. These experts helped to curate and categorize messy permit data into an organized sample. Shovels used this sample to train their LLM models to unlock their entire data pipeline.
Image: /images/shovels_prolific_hero.png

Earlier this year, we partnered with [Prolific](https://www.prolific.com/) to leverage their crowdsourced data analyst experts to help our engineers wrangle the messy and disjointed dataset that is US building permits. The Prolific team was an immense help, and in hindsight, we couldn’t have done it without them.

If you’re curious about the specifics, **check out their case study on Shovels [here](https://www.prolific.com/resources/how-shovels-found-high-skilled-annotators-for-data-labeling-with-prolific-s-specialist-participants)**.

## Scalability is Key

Our data engineers (shout out to Luka and Petra 🦾) are some of the best in the business, but even they couldn’t handle the curation of a classification model to accurately handle 200 million permits by themselves. It was possible, but wasn’t time- or cost-effective. Which was where Prolific came in.

Prolific’s vast network of data analysts meant that we could source multiple teams of construction experts to help us curate a golden sample of permit classification (tagging each by work type, address, location, and many more) to serve as the basis of our LLM training data. We’d known that the key to effective LLM and AI usage is all in the proprietary training data, so a human touch (many of them, in fact) was crucial.

## The Data Speaks for Itself

Comparing the results of the independent expert teams and their direct classification scores, we were able to create a highly accurate and effective training model. With that foundation in place, we brought it into our marquee data pipeline to handle the hundreds of millions of building permits we have (with more added every week).

With our classification and data cleaning in place, our business intelligence trifecta — on homeowners, on contractors, and on the wider construction market — is “shovel-ready”. In fact, our **Web App**, **API**, and **Data Feeds** are already in use across both small businesses and enterprises.

Check out our [Free Trial](https://beta.shovels.ai) if you’d like to get started with our Web App or API, or reach out to [Sales](mailto:sales@shovels.ai) for a sample file of your desired market and segment!
