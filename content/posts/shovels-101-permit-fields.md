Title: Understanding Permit Data Fields
Subtitle: Learn how to understand the Shovels permit data fields
Date: 2024-10-09
Modified: 2024-10-09
Category: Customer Success
Tags: permits, tutorial, resource
Authors: Alex Brown
Summary: The Shovels permit database has many fields, which are sometimes blank. Use the Data Dictionary to understand what these fields mean, and why some might be null. Review the most important fields for a permit, and filter out what isn't needed. 
Image: /images/shovels-101-permit-fields.png


Permits are incredibly data-dense objects, assuming that they’re filled out correctly and completely. It’s no simple task to keep all the fields straight, and if you have, contact us because we probably want to hire you. 

In this tutorial, I’ll walk through the vast world of Shovels permit (and other object) data fields, what they mean, why some fields are blank or `NULL`, and some tips and tricks for cutting right to the critical fields. 

## Using the Shovels Data Dictionary

With as many fields available across so many different data types (**Permits**, **Contractors**, **Properties**, and more…), it’s a monumental task to keep track of which ones are where, and what they even mean. 

That’s where the [Data Dictionary](https://docs.google.com/spreadsheets/d/1qiIxx37_-6vGfGp2i5pXv4w2FdsLsShjCqSVO5v6OMQ/edit?gid=1818227349#gid=1818227349) comes in. This publicly-available spreadsheet (check the multiple tabs across the bottom for more info) gives an exhaustive breakdown of all the fields, variables, and parameters that our dataset contains. 

For the purposes of this tutorial, I’ll include a sample permit payload for a single permit from Agawam, MA. This includes all available fields for permits, beyond just the ones included in the Shovels **Web App** or **API**. For definitions of any of these, check out the Data Dictionary.

Bear with me please, there are a lot of fields…

```json
[
 {
   "ID": "8ee111a1199934d5",
   "PERMIT_NUMBER": "E-21-99",
   "CBSA": "Springfield, MA",
   "CBSA_FIPS": 44140,
   "COUNTY_FIPS": 13,
   "STATE_FIPS": 25,
   "STATUS_ORIGINAL": "complete",
   "APN": "",
   "FILE_DATE": "2021-02-24",
   "FINAL_DATE": "",
   "OWNER_NAME": "Agawam Rentals Llc",
   "OWNER_STREET": "Po Box 246",
   "OWNER_CITY": "Hadley",
   "OWNER_STATE": "MA",
   "OWNER_ZIPCODE": 1035,
   "OWNER_PHONE": "",
   "OWNER_EMAIL": "",
   "APPLICANT_NAME": "",
   "APPLICANT_STREET": "",
   "APPLICANT_CITY": "",
   "APPLICANT_STATE": "",
   "APPLICANT_ZIPCODE": "",
   "APPLICANT_PHONE": "",
   "APPLICANT_EMAIL": "",
   "ARCHITECT_NAME": "",
   "ARCHITECT_STREET": "",
   "ARCHITECT_CITY": "",
   "ARCHITECT_STATE": "",
   "ARCHITECT_ZIPCODE": "",
   "ARCHITECT_PHONE": "",
   "ARCHITECT_EMAIL": "",
   "ARCHITECT_LICENSE": "",
   "ENGINEER_NAME": "",
   "ENGINEER_STREET": "",
   "ENGINEER_CITY": "",
   "ENGINEER_STATE": "",
   "ENGINEER_ZIPCODE": "",
   "ENGINEER_PHONE": "",
   "ENGINEER_EMAIL": "",
   "ENGINEER_LICENSE": "",
   "DESIGNER_NAME": "",
   "DESIGNER_STREET": "",
   "DESIGNER_CITY": "",
   "DESIGNER_STATE": "",
   "DESIGNER_ZIPCODE": "",
   "DESIGNER_PHONE": "",
   "DESIGNER_EMAIL": "",
   "DESIGNER_LICENSE": "",
   "NEW_DWELLING": false,
   "NEW_ADU": false,
   "ACCESSORY_STRUCTURE": false,
   "POOL_SPA": false,
   "ROOM_ADDITION": false,
   "KITCHEN_REMODEL": false,
   "BATH_REMODEL": false,
   "SOLAR": false,
   "REROOF": false,
   "UTILITIES": true,
   "WINDOW_DOOR": false,
   "FOUNDATION": false,
   "SITEWORK": false,
   "DEMOLITION": false,
   "EXTERIOR_REMODEL": false,
   "TENANT_IMPROVEMENT": false,
   "RESIDENTIAL": true,
   "AIR_SOURCE_HEAT_PUMP": true,
   "GROUND_SOURCE_HEAT_PUMP": "",
   "EV_CHARGER": false,
   "SOLAR_BATTERY_STORAGE": false,
   "ELECTRICAL_PANEL_UPGRADE": "",
   "ELECTRICAL_SERVICE_UPGRADE": "",
   "EFFICIENCY": "",
   "HEAT_PUMP_WATER_HEATER": "",
   "INDUCTION_STOVE": "",
   "WIND": "",
   "COMMERCIAL": false,
   "MULTIFAMILY": false,
   "PUBLIC_WORK": "",
   "NUM_SOLAR_PANELS": "",
   "SOLAR_PANEL_POWER": "",
   "SOLAR_SYSTEM_CAPACITY": "",
   "UTILITY_CAPACITY": "",
   "ACCESSORY_STRUCTURE_TYPE": "",
   "ATTACHED_DETACHED": "",
   "CONDITION": "",
   "BATH_ITEMS_INSTALLED": "",
   "REMODEL_MATERIALS_USED": "",
   "DEMO_FULL_PARTIAL": "",
   "EXTERIOR_REMODEL_TYPE": "",
   "FOUNDATION_TYPE": "basement",
   "FOUNDATION_WORK_TYPE": "",
   "KITCHEN_ITEMS_INSTALLED": "",
   "ADU_TYPE": "basement",
   "CONSTRUCTION_TYPE": "",
   "ADU_LEGALIZATION": "",
   "DWELLING_TYPE": "",
   "POOL_TYPE": "",
   "REROOF_TYPE": "",
   "REROOF_MATERIAL": "",
   "ROOM_ADDITION_TYPE": "",
   "SITEWORK_TYPE": "",
   "SOLAR_INSTALL_TYPE": "",
   "SOLAR_BRAND": "",
   "SOLAR_BATTERY_INCLUDED": "",
   "UTILITY_TYPE": "mini split, water heaters",
   "WINDOW_DOOR_TYPE": "",
   "SIZE_SQUARE_FEET": "",
   "NUM_BEDS": "",
   "NUM_BATHS": "",
   "NUM_UNITS": "",
   "NUM_BUILDINGS": "",
   "NUM_FLOORS": "",
   "SIZE_SQUARES": "",
   "NUM_ROOMS": "",
   "NUM_WINDOWS": "",
   "NUM_DOORS": "",
   "COUNTY": "Hampden County",
   "JURISDICTION": "Agawam Town",
   "TYPE": "Electrical",
   "SUBTYPE": "Additions/alterations - residential",
   "STATUS": "final",
   "ISSUE_DATE": "",
   "DESCRIPTION": "Wire mini split system, install bath fan in 2nd floor bath, wire 2 electric water heaters and install 2 receptacles for washing machines in basement",
   "JOB_VALUE": "",
   "FEES": "",
   "APT_NUMBER": "",
   "HEAT_PUMP": true,
   "WATER_HEATER": true,
   "HVAC": false,
   "STREET": "HIGH ST",
   "STREET_NO": 33,
   "ZIPCODE": 1001,
   "ZIPCODE_EXT": "",
   "CITY": "AGAWAM",
   "STATE": "MA",
   "DISTRICT": "HAMPDEN",
   "LONG": -72.632972717,
   "LAT": 42.097988129,
   "ADDRESS_ID": "Jy207ojc0Jk",
   "INTL_ADDRESS_NORMALIZED": true,
   "CONSTRUCTION_DURATION": "",
   "APPROVAL_DURATION": "",
   "INSPECTION_PASS_RATE": "",
   "INSPECTION_PASSED": "",
   "INTL_CONTRACTOR_LINKED": "",
   "_META_LOADED_AT": "2024-09-16 01:38:53.371 -0700",
   "_META_SOURCE_FILE_NAME": "nationwide/permits/20240912_224317_00015_ph49q_2c6b1418-b9d6-482e-82aa-570deb28ab0b",
   "START_DATE": "2021-02-24",
   "END_DATE": "2021-02-24",
   "TOTAL_DURATION": 0,
   "RNO": 1
 }
]
```

As you can see, there’s a lot of detail here. Many of these are the key details that most of our insights are based on, yet still there are a ton of blank fields.

Let’s dig in to these unfilled fields. 

## Why Are These Fields Blank?

For some context, the permit fields we maintain in our database are unlikely to map 1:1 to any given permit if you actually looked at the source permit filing. However, as part of our aggregation methods, we have to combine and cover for all the possible fields that different jurisdictions may offer on their permits. This leads to a lot of empty fields. 

At first glance the number of empty fields in the sample above might be worrying. But if we take a look at the actual fields themselves, we’ll see that they’re pretty niche details to begin with. 

These are generally separated into four groups of field “classes”:

1. Optional professional contact details, like `applicant_name`, `architect_phone`, `engineer_zipcode`, or `designer_license` — these are rarely used in general, but are exceedingly rare within the same permit. 
2. Project-specific fields like `remodel_materials_used` , `reroof_type`, or `num_windows` — these may be used in a large scale project like an house-wide remodel, but for smaller projects they’ll usually be unrelated and left blank. 
3. Commonly unfilled fields like `job_value` or `fees`, which are infrequently required and even less often accurate. This is especially true for non-contractor permits.
4. Derivative metrics when we’ve calculated and added to the payload, like `construction_duration`, `approval_duration` , or `inspection_pass_rate`  — these are based on other metrics, which are either left off historical records or are incomplete in the permit itself. 

Given the variation in jurisdiction requirements for which fields are required, or even included, on their permits, it can be difficult for a single database schema to show only the relevant fields for a given permit. It’s definitely something we’re keeping in mind, but for the moment we trust that you’ll understand that not all fields are equally important. 

## Top 10 Most Useful Permit Fields

There are 100 (!) different fields on a given permit flat file, but let’s highlight the most important ones. If any of these fields are empty, then [let us know](mailto:support@shovels.ai) and we’ll investigate.

1. `File_date` : The date when the permit is filed with the permit department or jurisdiction.
2. `Permit_number`: The local jurisdiction’s record identifier. 
3. `Owner_name`: The name of the property owner for the permit work.
4. `Residential`: Whether the permit is done to a commercial or residential property.
5. `Jurisdiction`: The local governmental body which oversees the permit work. 
6. `Type`: The type of permit work being done. These types are not standardized at the jurisdiction level, but at Shovels we’ve used LLMs to condense 600k+ variations into 22 project classifications.
7. `Subtype`: The subtype of permit work being done, imported as a string directly from the permit source. 
8. `Status`: The status of the permit, one of either `in_review`, `active`, `final`, or `inactive`. See our [blog post on permit statuses](https://www.shovels.ai/blog/shovels-101-permit-statuses/) for more info. 
9. `Description`: The description on the permit
10. `Street` (plus `street_no`, `zipcode`, `city`, `state` ): These fields collectively represent the permit’s address. 

This list above is generalized as a rule, so it’s very likely that the most important fields to your business are slightly different. But that’s ok, because our data is easy to filter to get exacly what you need. 

## Customize the Data to Your Needs

We have three different delivery methods, which are suited for different business needs. If you want simple data that can be accessed codelessly, then the [Web App](https://www.shovels.ai/permit-database) will be perfect for you. If you want a bit more, which can be programmatically integrated with your platform or product offering, then our [API](https://www.shovels.ai/api) would be better. 

But if you really want to get granular, then our enterprise-ready [Data Feed](https://www.shovels.ai/data-feed) will be best. You can either access the entire Shovels dataset in your warehouse of choice, or you can get the raw data in flat file and query it yourself. 

No matter the use case, Shovels can get you what you need. Check out our [Free Trial](https://beta.shovels.ai), or get in touch with [Sales](mailto:sales@shovels.ai) for data sample and demo call. 

Happy Digging!