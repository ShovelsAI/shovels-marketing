Title: March 2024 Newsletter
Subtitle: We launched an Android app and now offer private table sharing
Date: 2024-3-11
Modified: 2024-3-11
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Author_image: /theme/images/team/ryan.svg
Author_title: CEO
Summary: We launched our Android app in Google Play and made a bunch of data pipeline improvements. We can also now share tables to Snowflake, Big Query, and Databricks.
Image: /images/screenshots.png


Last month we launched [our web app](https:/app.shovels.ai). This month we're offering even more ways to get your hands on our building permit and contractor data!

And we want to meet you IRL.

*   A few days ago we launched an [Android app](https://play.google.com/store/apps/details?id=com.shovels.shovels1). You can find it now on Google Play. Next month we'll launch on the Apple App Store, too. 
*   Let's meet! The Shovels team will be in SF from March 18-19 and LA on March 21. We'll come to your office. 
*   Lots more data and API enhancements. Details below.
*   We can now push permit and contractor tables into Big Query, Snowflake, Databricks, S3, GCS, and Azure! 

We're so mobile
===============

We built the Shovels app using a relatively new technology called Flutter. This software development kit gives our small team a ton of leverage to build cross-platform and make rapid improvements to the app.

It's because of Flutter that we can build a web app and a mobile app at the same time, with the same code, and without a ton of cost.

You could say it gives us mobility. We're moving fast! 

Here's a few screenshots of our Android app. Get it on [Google Play now](https://play.google.com/store/apps/details?id=com.shovels.shovels1).

(We could have launched iOS too, but I gotta save _something_ for April.)

![Mobile app screenshots]({static}/images/screenshots.png)

**Hang out with us**
====================

The Shovels team is international. I'm in California. Luka and Petra are in Europe. We only meet in person a couple of times a year.

Lucky for you, the next convening is happening the week of March 18 and we want to meet. We'd love to come to your office and chat face-to-face about how you think about building permit and contractor data. 

The nice thing about a small team is we can fit in a single Uber. We'll come to you. 

*   San Francisco: March 18-19   
*   LA area: March 21

Just reply to me and we'll figure out a time.

Shovels in your data lake
=========================

We know that for many of you, API access doesn't fully scratch the itch.

You have bigger plans that will be realized only if you can merge our permits with your own data. We can send you our db files, but to pull them into Snowflake (or wherever) you'll need help from your engineering team and oh boy, that'll take forever. 

We have a solution for you.

We're now offering private shares of our production database tables into Big Query, Snowflake, Databricks, S3, GCS, and Azure.

It's super fast and easy and gives you unlimited access to query and join our permit and contractor tables with your data lake.

We've already done the engineering -- so you don't have to! 

The Shovels March release
=========================

It's a new month, and with that, a bunch of new fixes. Here's our March release notes. We pushed all this to production about a week ago. 

*   **Better address validation**: We've improved our ability to validate and enhance cities and ZIP codes on permit addresses. 
*   **Improvements in contractor grouping**: We're using more comprehensive details, including addresses and phone numbers, to cluster contractor branches into groups.
*   **A new address dataset**: We added over three million exact geo locations to our permits table. We are closing down the gap of unlinked permits (permits without geo coordinates).
*   **Improvements in our internal docs**: We move fast but we also recognize that investing in good documentation now will save us headaches later. We created a new internal knowledge base.
*   **API enhancements**: We introduced a [new API call](https://shovels-v2.redoc.ly/#operation/Permits/operation/get_permits_by_id_v1_permits_get) that allows for the specification of multiple permits in a single request.
*   **Database optimization**: In response to API usage patterns, we've restructured our database architecture. No more timeouts!
*   **API monitoring**: We have integrated with an awesome tool to help us track API usage, errors, and patterns.

Things to do with permits: make permit predictions
==================================================

Have you ever noticed that when one of your neighbors gets an ADU, or installs solar panels, or does the huge remodel and room addition, it seems to trigger everyone else in the neighborhood to do the same? 

There's FOMO in the home improvement market. I think we can measure this "Keeping up with the Jones's" phenomenon with building permit data and start to see where this wave of home improvements might be swelling in a particular neighborhood.

I'm not enough of a data scientist to give this justice (and apparently ChatGPT isn't either -- it wasn't very helpful this time) but with our table sharing (see above), perhaps _you_ can crack this riddle?

Here's a chart showing the distribution of the percentage of homes with permits since 2023 by ZIP code. What I mean by that is how much variance is there in "permits per capita" nationwide? Most ZIPs have low permit density, but a few are very active ones.

What's causing the difference? We don't know yet!

![Distribution of permit density by ZIP code]({static}/images/permits-distribution.png)

This is long enough
===================

Next month I plan to announce our iOS app and give a teaser for our V2 API and describe how it will improve the Shovels web and mobile apps.