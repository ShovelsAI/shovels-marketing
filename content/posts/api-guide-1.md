Title: How to use the Shovels API
Subtitle: The definitive guide to getting started with the Shovels API
Date: 2023-10-13
Modified: 2023-10-13
Category: Customer Success
Tags: api
Authors: Ryan Buckley
Summary: The Shovels API provides an intuitive platform for proptech enthusiasts looking to leverage building permit data. Users can access and filter building activities via types or specific date ranges. The API employs 'tags' to categorize 33 distinct types of building activities.
Image: /images/api-blog.jpg


So... you want to build something cool in proptech, and you figured out (wisely, I might add) that building permits will make your product *shine*.

That is excellent news, and we are here to help. 

## Authentication

We use header key-based authentication. There are two steps to authenticate:

1. Get your API key at [https://app.shovels.ai](https://app.shovels.ai){:target="_blank"} . You will see it on your dashboard when you register and log in. 
2. Add your key to this HTTP header when you make a request: `X-API-Key: YOUR_API_KEY_HERE`. [Click here](https://realpython.com/python-requests/#request-headers){:target="_blank"}  for more information about making HTTP requests with headers using Python. *(Note: you can use any programming language; we like Python 🐍)*

## Filters

We learned early on that our customers wanted two types of filters:

1. **By activity**: Filter building activity by the *type* of activity
2. **By date**: Show the activity in between two dates, and always display the most recent activity first

### Tags

Let's look at the building activity filter first. We call types of activity *tags*.

We offer 33 unique tags as of this publication date in October 2023. That number will increase over time! 

To use tags, you need to know what they are. We named them to (hopefully) be self-explanatory. If you need clarification, you can check the Tags tab in the [Data Dictionary](https://docs.google.com/spreadsheets/d/1qiIxx37_-6vGfGp2i5pXv4w2FdsLsShjCqSVO5v6OMQ/edit#gid=1842205445){:target="_blank"} . We'll try to keep this updated. 

To see a list programmatically, perhaps for your own internal dashboard or BI tool, you can always list our tags using the [Get All Available Tags](https://shovels-v2.redoc.ly/#operation/List/operation/get_all_available_tags_v1_list_tags_get){:target="_blank"}  endpoint.

To make this extra super clear, let's go through some examples. I'm going to show the code snippets using Curl, a command-line tool available natively in every operating system. Just open a new command-line prompt (e.g. Terminal on MacOS) to use it. 

#### Get details on every heat pump installation in a zip code 

Let's use 94123, my old neighborhood in San Francisco. Start by finding the right tag (using the methodology above) for heat pumps: `heat_pump` should do the trick!

Next, find the endpoint. [Get Permits By Zip Code](https://shovels-v2.redoc.ly/#operation/Permits/operation/get_permits_by_zip_code_v1_permits_zip_get){:target="_blank"}  sounds about right! 

Make the request. Here's the Curl command.

```bash
curl -X 'GET' \
  'https://api.shovels.ai/v1/permits/zip?zip_code=94123&tags=heat_pump&page=1&size=50' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOUR_API_KEY_HERE'
```

And it worked! 

```
{
  "items": [
    {
      "id": "07ec97288669e01793a9dbb47c352400",
      "address": {
        "street_no": "3550",
        "street": "BAKER ST",
        "city": "SAN FRANCISCO",
        "zip_code": "94123",
        "state": "CA",
        "lat": 37.804016,
        "long": -122.44678
      }
    },
    {
      "id": "179c87dcfa6f499edff389c2272f819b",
      "address": {
        "street_no": "12",
        "street": "RICO WAY",
        "city": "SAN FRANCISCO",
        "zip_code": "94123",
        "state": "CA",
        "lat": 37.805016,
        "long": -122.438484
      }
    }
  ]
}
```

So what do we do with all those `id` values? Each one is an internal ID for a Shovels permit. To get the details we want (since we probably want more than just the address) let's take the `id` and pass it into our [Get Permit by ID](https://shovels-v2.redoc.ly/#operation/Permits/operation/get_permit_by_id_v1_permits__id__get){:target="_blank"}  endpoint.

```bash
curl -X 'GET' \
  'https://api.shovels.ai/v1/permits/179c87dcfa6f499edff389c2272f819b' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOUR_API_KEY_HERE'
```

And we get this in response:

```
{
  "jurisdiction": "San Francisco",
  "issue_date": "2017-09-07",
  "final_date": null,
  "type": "Plumbing",
  "inspections_pass_rate": null,
  "fees": null,
  "address_id": "1973404EE7003B21",
  "description": "Work category: 1m; new rooftop heatpump with ductwork on rooftop, 24,000 btu",
  "contractor_id": null,
  "number": "PMW20170907784",
  "status": "Active",
  "id": "179c87dcfa6f499edff389c2272f819b",
  "address": {
    "street_no": "12",
    "street": "RICO WAY",
    "city": "SAN FRANCISCO",
    "zip_code": "94123",
    "state": "CA",
    "lat": 37.805016,
    "long": -122.438484
  },
  "tags": [
    "air_source_heat_pump",
    "heat_pump",
    "utilities"
  ]
}
```

Neato! If we wanted to store all these heat pump installs in a database or spreadsheet, we could write more code for that. I recommend asking ChatGPT to do it for you.

#### Get all the heat pump HVAC installers in a zip code

What if you don't care about the permits or the homes, and you just want to know who did the install? We can help with that, too! 

Our handy [Get Permits By Activity Zip Code](https://shovels-v2.redoc.ly/#operation/Contractors/operation/get_contractors_by_activity_zipcode_v1_contractors_activity_zip_get){:target="_blank"}  endpoint should be perfect. We can use the same example, and we'll introduce dates this time. 

For this API call, let's find all the heat pump HVAC installers who did work in the first two quarters of 2023. 

```
curl -X 'GET' \
  'https://api.shovels.ai/v1/contractors/activity/zip?zip_code=94103&tags=heat_pump&start_date=2023-01-01&end_date=2023-07-01&page=1&size=50' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOUR_API_KEY_HERE'
```

**Note that our dates take the form `YYYY-MM-DD`. This is important!**

The response now is:

```
{
  "id": "adfbb85fa395444c9516dcfe97ffcfb5",
  "name": "DENIZ SALON",
  "business_name": "KA - BI CONSTRUCTION INC."
}
```

Same deal. The `id` shown is our internal Shovels contractor ID. Let's hit our [Get Contractor by Id](https://shovels-v2.redoc.ly/#operation/Contractors/operation/get_contractor_by_id_v1_contractors__id__get){:target="_blank"}  endpoint with it to get those contractor details! 

```
curl -X 'GET' \
  'https://api.shovels.ai/v1/contractors/adfbb85fa395444c9516dcfe97ffcfb5' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOUR_API_KEY_HERE'
```

And the details are:

```
{
  "license": "944398",
  "name": "DENIZ SALON",
  "email": "denizsalon@yahoo.com,salon642002@yahoo.com",
  "street": "BAYSHORE HY",
  "business_name": "KA - BI CONSTRUCTION INC.",
  "id": "adfbb85fa395444c9516dcfe97ffcfb5",
  "phone": "6502914299",
  "street_no": "1290",
  "city": "BURLINGAME",
  "state": "CA"
}
```

### Dates

Building permits have dates galore. We show file dates, issue dates, and final dates. File dates are when the permit was sent to the jurisdiction. Issue dates are when the permits are approved for construction, and the final dates is when the jurisdiction finally signs off on the finished work. 

Our date filters, called `start_date` and `end_date`, are based solely on the file date.

To show how this works, let's look at permits filed in New York in August 2023. We can use our [Get Permits by State](https://shovels-v2.redoc.ly/#operation/Permits/operation/get_permits_by_state_v1_permits_state_get){:target="_blank"}  endpoint! 

```
curl -X 'GET' \
  'https://api.shovels.ai/v1/permits/state?state=NY&start_date=2023-08-01&end_date=2023-08-31&page=1&size=50' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOUR_API_KEY_HERE'
```

We could use tags here too, but I chose not to. Here's what the first two permits look like:

```
{
  "id": "e101ca8b62f825a1199fb370365b85d7",
  "address": {
    "street_no": "3",
    "street": "NEW HAMPSHIRE AVE",
    "city": "EAST GREENBUSH",
    "zip_code": "12144",
    "state": "NY",
    "lat": 42.625023,
    "long": -73.725845
  }
},
{
  "id": "d0c345961c8c446f3e56655c0ddfca8a",
  "address": {
    "street_no": "410",
    "street": "ROCKAWAY AVE",
    "city": "HEMPSTEAD",
    "zip_code": "11581",
    "state": "NY",
    "lat": 40.658535,
    "long": -73.70126
  }
}
```

I could look up the details on these the same way I described above. No need to repeat! 

## Conclusion

This API is meant to be fast to learn and easy to work with. If you have any questions (really!) we want to know and provide support so we can make it easier to use.

And if you find that you're looking for an endpoint that we're not offering yet, let us know. We just might build it. 

Cheers! 