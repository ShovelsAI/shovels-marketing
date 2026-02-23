Title: Shovels 101: Finding Address Permit History
Subtitle: The definitive guide to using the Shovels API to find address permit history
Date: 2024-08-29
Modified: 2024-11-04
Category: Customer Success
Tags: api
Authors: Alex Brown
Author_image: /theme/images/team/alex.svg
Author_title: Technical Support & Writer
Summary: The Shovels API gives you insight into permit history by per address. Users can follow these three steps to retrieve this information. This data can help with contractor and jurisdiction analysis.
image: /images/shovels-101-address-permit-history.png

Understanding a property’s permit history is critical to any project. Whether you’re researching a new property to acquire, or double-checking what previous owners have done to one you already own, it’s important info to have. 

With the [Shovels API](https://docs.shovels.ai/api-reference/) in your toolbox, finding permits specific to a given address is a breeze. 

## Authentication and Setup

If you don’t already have a **Shovels Web App** account (welcome!), then head over and setup a [Free Trial](https://app.shovels.ai). Go to the **Settings** page to get your API Key, read over our API Docs, and open your preferred terminal, shell, or editor. 

For a more in-depth introduction to using our API, please refer to our [API documentation](https://docs.shovels.ai/docs/shovels-api-introduction). 

This guide will assume a basic familiarity with cURL, JSON parsing, and our API schema. Example query snippets will use cURL, but our API docs have examples in a variety of other languages too.

## Using the Shovels API

To set the scene, imagine that you’re a prospective buyer wanting to do your due diligence on an intriguing property. The building was constructed in the last 15 years, and it’s important to you that the previous owners have kept everything above board with the required permits and inspections handled. 

With the Shovels API, you can get from address to detailed permit history based on the jurisdiction’s own books with three API calls.

## Step 1: Finding the Address

Using the [GET Search Addresses](https://docs.shovels.ai/api-reference/#operation/search_addresses_v1_addresses_search_get)  endpoint, search for the address to confirm that there are any permits on record (our system goes back ~20 years). 

A sample query, for a “123 Main St”, should look something like this:

```
curl -i -X GET 'https://api.shovels.ai/v1/addresses/search?q=123%20MAIN%ST' 
	-H 'X-API-Key: YOUR_API_KEY_HERE'
```

> **Important**: Remember to use `%20` to denote any spaces in the address string, and that the correct endpoint here is */addresses/*, NOT ~~/address/~~.

Assuming your other syntax and API key is input correctly, this request should return the following:

```
[
	{
		"street_no":"123",
		"street":"MAIN ST",
		"city":"ST. FRANCISVILLE",
		"zip_code":"12345",
		"zip_code_ext":null,
		"state":"LA"
	},
	{
		"street_no":"123",
		"street":"SO MAIN ST",
		"city":"ST. ALBANS",
		"zip_code":null,
		"zip_code_ext":null,
		"state":"VT"
	},
	{
		"street_no":"123",
		"street":"MAIN ST",
		"city":"NACOGDOCHES",
		"zip_code":"75961",
		"zip_code_ext":null,
		"state":"TX"
	},
	{
		"street_no":"123",
		"street":"MAIN ST",
		"city":"AGAWAM",
		"zip_code":"01001",
		"zip_code_ext":null,
		"state":"MA"
	},
	{
		"street_no":"123",
		"street":"MAIN ST",
		"city":"HOPKINTON",
		"zip_code":"02804",
		"zip_code_ext":null,
		"state":"RI"
	}
]
```

The returned list of addresses is ordered by relevance and formatted according to USPS standard. In this case, of all the matching addresses in the US, **five of them have relevant permit histories**. 

Pick which address you want to dig deeper into, and **proceed to step 2**.

> **Note**: Permit availability rates can vary drastically for a number of reasons (offline or infrequently uploaded records, isn’t yet in our jurisdiction [Coverage Map](https://shovels.metabaseapp.com/public/dashboard/0573503d-88ac-4ba4-a723-346b55de482b?city=&county_or_jurisdiction=&state=&tab=133-permit-types&zip_code=), or many others). If your desired address isn’t included, then please reach out to us at [support@shovels.ai](mailto:support@shovels.ai) and we’ll take a look. 

## Step 2: Retrieve Permits for the Address

Using the data returned in Step 1, we will now retrieve the exact permits themselves for the desired address. 

Using the [GET Permits by Address](https://docs.shovels.ai/api-reference/#operation/get_permits_by_address_v1_permits_address_get) endpoint, enter the relevant address data to the next query. The list of required parameters are noted in the schema on the API doc linked just above. 

Again, a sample query, for “123 Main St, Agawam, MA 01001”, would look something like this:

```
curl -i -X GET 'https://api.shovels.ai/v1/permits/address?street_no=123&street=MAIN%20ST&state=MA&city=AGAWAM&zip_code=01001'
	-H 'X-API-Key: YOUR_API_KEY_HERE'
```

> **Important**: The multiple parameters required for this endpoint are noted with the AND `&` operator.

This second request should return the following:

```
{
	"items":
	[
		"5c4015a630e941b6",
		"0eb49a17aa7e8791",
		"77d2073b694190dd",
		"cd66d9dda0662b59",
		"5575716497ab9bd6"
	],
	"page":1,
	"size":5,
	"next_page":null
}
```

which shows that there are 5 permits on record for this address. These Permit IDs are unique to the Shovels platform, but can be used to retrieve the detailed permit details.

To do so, **proceed to Step 3**.

## Step 3: Return Detailed Permit History

Using the [GET Permits by ID](https://docs.shovels.ai/api-reference/#operation/get_permits_by_id_v1_permits_get) endpoint, you can search for a single (or string array) of permit IDs. 

In this sample, to request the first permit payload would look something like this:

```
curl -i -X GET 'https://api.shovels.ai/v1/permits?id=5c4015a630e941b6' 
	-H 'X-API-Key: YOUR_API_KEY_HERE'
```

> **Important**: Searching for multiple permits at once requires a string **array**, which is denoted in the cURL request by the `&id=string` clause for each additional permit ID. 

The third request for the single permit should return the following:

```
[
	{"id":"5c4015a630e941b6",
		"description":"Replace existing 12' x 14' deck with a 20' x 20' deck (estimated cost $8,000), zone res a2, receipt  No.58233",
		"number":"17961",
		"jurisdiction":"Agawam Town",
		"job_value":null,
		"type":"Building",
		"subtype":"Building permit - new",
		"fees":null,
		"status":"active",
		"file_date":"2014-04-14",
		"issue_date":null,
		"final_date":null,
		"construction_duration":null,
		"approval_duration":null,
		"inspections_pass_rate":null,
		"contractor_id":null,
		"address":
			{
				"street_no":"123",
				"street":"MAIN ST",
				"city":"AGAWAM",
				"zip_code":"01001",
				"zip_code_ext":null,
				"state":"MA",
				"latlng":[42.087486267089844,-72.6227035522461]
			},
		"tags":
			["accessory_structure","residential"]
	}
]
```

And there you have it! This information can be exported for whatever outside needs you have, and this process can be easily repeated for any addresses and permits needed. 

The same information is searchable via our Web App at https://app.shovels.ai/.

For enterprise-level usage, get our full dataset with deeper insights, dashboards, and flat files. However you need to retrieve this data, we’ll make it happen.

## Troubleshooting Tips

- A full list of our error codes are described in our API docs [here](https://docs.shovels.ai/api-reference/#section/API-Details). Most errors are 404s, which frequently mean either the address is input incorrectly, or there isn’t a permit record on file to match the search terms.
    - If you are able to find the correct address in our **Web App**, then double check the syntax of the request. 
- If you run into any other questions, please email us at [support@shovels.ai](mailto:support@shovels.ai) and we’ll help you!

## Conclusion

We hope this guide is helpful (and we’ve got more on the way). Our API is meant to be intuitive and easy to use, so we definitely want to know any and all hiccups you encounter. If there’s an endpoint that we don’t support yet, or any other feedback for our platform, we’d love to hear it. 

We’re building out Shovels API v2 right now, and your requests might make the next release. 

Happy Building!

## Frequently Asked Questions

**Q: How do I look up the permit history for a specific address using the Shovels API?**

A: It is a three-step process. First, use the Search Addresses endpoint to find and confirm the address. Second, use the Permits by Address endpoint with the address details to get a list of permit IDs. Third, use the Permits by ID endpoint to retrieve the full details of each permit.

**Q: What format should the address be in when querying the API?**

A: Use %20 to denote spaces in the address string. The address components (street number, street name, city, state, zip code) are passed as separate parameters joined with the & operator. The addresses returned by Shovels are formatted according to USPS standards.

**Q: What should I do if my address does not appear in the Shovels search results?**

A: There are several possible reasons: the address may not have any permits on record, the jurisdiction may not have digitized its permits yet, or the address may not be in Shovels' coverage area. You can check the Shovels Coverage Map to see available jurisdictions, or email support@shovels.ai for help.

**Q: Can I retrieve multiple permits at once from the API?**

A: Yes. The Permits by ID endpoint accepts a string array of permit IDs, allowing you to request multiple permits in a single API call by adding an &id=string clause for each additional permit ID.

<!-- JSON-LD FAQ schema for AI answer engines -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I look up the permit history for a specific address using the Shovels API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is a three-step process. First, use the Search Addresses endpoint to find and confirm the address. Second, use the Permits by Address endpoint with the address details to get a list of permit IDs. Third, use the Permits by ID endpoint to retrieve the full details of each permit."
      }
    },
    {
      "@type": "Question",
      "name": "What format should the address be in when querying the API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use %20 to denote spaces in the address string. The address components (street number, street name, city, state, zip code) are passed as separate parameters joined with the & operator. The addresses returned by Shovels are formatted according to USPS standards."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do if my address does not appear in the Shovels search results?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There are several possible reasons: the address may not have any permits on record, the jurisdiction may not have digitized its permits yet, or the address may not be in Shovels' coverage area. You can check the Shovels Coverage Map to see available jurisdictions, or email support@shovels.ai for help."
      }
    },
    {
      "@type": "Question",
      "name": "Can I retrieve multiple permits at once from the API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Permits by ID endpoint accepts a string array of permit IDs, allowing you to request multiple permits in a single API call by adding an &id=string clause for each additional permit ID."
      }
    }
  ]
}
</script>
