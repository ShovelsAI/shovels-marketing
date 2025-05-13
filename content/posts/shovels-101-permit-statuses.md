Title: Shovels 101: Permit Statuses
Subtitle: The definitive guide to understanding Shovels Permit Statuses
Date: 2024-09-03
Modified: 2025-05-13
Category: Customer Success
Tags: permit status, web app
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: The Shovels ecosystem breaks down construction permit status based on jurisdiction regulation and construction cycles. Permits can be In Review, Active, Final, or Inactive. Users can investigate permit status via Shovels to analyze wider trends in contractor performance and jurisdiction activity. 
Image: /images/shovels-101-permit-status.png


Permits are hard enough to acquire on their own, so we want to take the confusion out of understanding a permit's status. 

In our mission to make permit data as clean and straightforward as possible, let's quickly review Permit Statuses and how they map from our ecosystem to the actual construction process.

## Permit Status Definitions

![Flowchart describing Shovels permit status lifecycle, going from "In Review" to a cycle of "Active" and "Inactive", ending with "Final"](/images/permit-status-flowchart.png)

In the Shovels ecosystem, there are **four** statuses that Permits can be in:

* `in_review`: From the moment the permit is filed with the local jurisdiction, until it is approved. This is defined by the `file_date`  object.
* `active`: From the moment the permit is approved, until project completion or some other intermediate restriction. This is defined by the `issue_date`  object.
* `final`: When the permit is completed, and submitted back to the jurisdiction upon job completion. This is defined by the `final_date` object.
* `inactive`: If any part of the process stalls or gets restricted from progression, then the permit status moves to `inactive`. Disqualifying reasons and reporting time will vary by jurisdiction and local regulation, but can include failing to meet project inspections, the permit may expire before completion or [inactivity for more than 6 months (180 days)](https://ecode360.com/6567722#6567722), and many others.

For more system definitions (beyond permit statuses), check out our [Data Dictionary](https://docs.google.com/spreadsheets/d/1qiIxx37_-6vGfGp2i5pXv4w2FdsLsShjCqSVO5v6OMQ/edit?gid=249471341#gid=249471341)!

## Timeline

Now that we've got the definitions out of the way, let's put them into practice with a sample project timeline. We'll add in the relevant variables and objects that our system uses to track the permit progress where relevant.

"John and Jane Doe remodeled their house in Agawam, MA and contracted out the work to a local contractor, Acme Construction, LLC."

1. Acme Construction, LLC have gathered all the paperwork and due diligence for the project, and are submitting the permit to the local jurisdiction, the Hampden County Building Department. They receive their permit number and file date, and in the next few days, this permit will show up in the Shovels database as `in_review`. 
    * `file_date` would be **2022-05-02** (May 4th, 2023), for those keeping track at home.
2. A few weeks later, Acme Construction, LLC's permit for single-family residence remodel is approved, and they're cleared to begin construction. Great news, and now, their corresponding permit will show as `active`.
    * `issue_date` would be **2022-05-26**, and `approval_time` would be 24 days.
3. 8 months in to the project, and Acme Construction, LLC has made huge progress. However, they didn't pass one of their inspections, and aren't able to resume work until that underlying issue has been fixed. When this data is submitted to the jurisdiction alongside their permit files, the Shovels database will now classify this permit as `inactive`. 
    * Provisional `construction_duration` would be calculated from `issue_date` to the date of the failed inspection (**2023-01-29**), as 250 days.
4. 6 months later, and Acme Construction, LLC has fixed the issue and passed their inspection. Once updated with the HC Building Dept, this permit will return to active.
    * Construction resumes on **2023-07-29** and `construction_duration` count will now continue, until project completion. 
5. 7 months later, and everything is completed! All inspections have been passed, and John and Jane have their new remodeled house all ready to move back in. Once that paperwork is completed, then the Shovels database will show the permit as `final`. 
    * `final_date` would be **2024-02-29**, with a `total_duration` of 664 days, and `construction_duration` of 465 days.

> **Note about derived dates:** The `start_date` and `end_date` fields are derived dates created by Shovels to provide consistent date tracking across jurisdictions. `start_date` is derived by coalescing `file_date`, `issue_date`, and `final_date` in that order. `end_date` uses the same fields but in reverse order. This means that `start_date` and `end_date` can be the same value, and `end_date` may be populated even when a permit is still active. We recommend using these fields in conjunction with the permit status field for accurate permit lifecycle analysis.

## Analysis

These data points can be extremely helpful for further analysis of jurisdiction and contractor efficiency. For instance, Acme Construction, LLC's work for Mr. and Mrs. Doe's remodel could be compared against other remodel jobs they've done in the past, or even against other contractors with the same licensing and job types. 

At the same time, jurisdiction's approval times can be compared based on job type or seasonal application windows, which may give further insight into developmental opportunities in that region. 

The possibilities are endless.

## Conclusion

Permit Status is an important data point to everyone involved in the construction and proptech industries, and we want to make sure that our system is as easy to understand as possible. 

**Shovels 101** will be our tutorial series, and we've got a bunch of topics lined up for future publication. If there's anything you want us to cover, further questions about permit statuses, or any other fields in our dataset, let us know at [support@shovels.ai](mailto:support@shovels.ai)!

Happy Building!
