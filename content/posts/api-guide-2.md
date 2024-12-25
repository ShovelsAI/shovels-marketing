Title: How to use the Shovels V2 API
Subtitle: The definitive guide to getting started with the Shovels V2 API
Date: 2024-12-26
Modified: 2024-12-26
Category: Customer Success
Tags: api
Authors: Ryan Buckley
Summary: The Shovels V2 REST API enables property, climate, and construction technology developers to access detailed building permit and contractor data. The API provides two primary resources: Permits (official construction documents from local authorities) and Contractors (skilled building trade professionals). Additional endpoints include Lists for predefined values, Addresses for US address validation, and Meta endpoints for API information.
Image: /images/api-blog.jpg


# Getting Started with the Shovels API: A How-To Guide

The [Shovels API](https://docs.shovels.ai) is your gateway to a wealth of construction industry data. Whether you're building property tech, climate solutions, or construction software, our API makes it easy to access detailed information about building permits and licensed contractors. Let's walk through how to get started and make the most of our powerful filtering capabilities.

## Overview of the API

The Shovels API revolves around two main resources:

- **Permits** - Official documents issued by cities or counties that track construction and building alterations
- **Contractors** - Skilled professionals who perform the permitted work

Plus some handy additional resources:

- **Lists** - Pre-defined values for filtering (like property types and work categories)
- **Addresses** - Search and validate US addresses
- **Meta** - Information about the API and data coverage
- **Geography** - Find locations by searching cities, counties, and zip codes

## Quick Start: Authentication

Getting started is easy! All API requests need an API key in the `X-API-Key` header. Here's how to get one:

1. Sign up for a free account at [https://app.shovels.ai/create-account/](https://app.shovels.ai/create-account/)
2. Find your API key in your account dashboard (click your email in the top right)

Here's a simple Python example to get you going:

```python
import requests

API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.shovels.ai/v2'

response = requests.get(
    f"{BASE_URL}/permits/search",
    params={
        "permit_from": "2022-01-01",
        "permit_to": "2023-12-31", 
        "geo_id": "TX",
        "property_type": "residential",  # Filter by property type
        "permit_tags": ["solar", "hvac"]  # Filter by work type
    },
    headers={'X-API-Key': API_KEY}
)
```

## Power Filtering with Property Types and Tags

One of the most powerful features of our API is the ability to filter by property types and work categories (tags). This helps you zero in on exactly the data you need.

### Property Type Filtering

The `property_type` parameter lets you focus on specific types of buildings:

- residential
- commercial 
- industrial
- agricultural
- vacant_land
- office
- recreational
- exempt
- miscellaneous

For example, to find all commercial permits in Texas:

```python
params = {
    "permit_from": "2022-01-01",
    "permit_to": "2023-12-31",
    "geo_id": "TX",
    "property_type": "commercial"
}
```

### Work Category (Tags) Filtering

The `permit_tags` parameter helps you find specific types of work. Some popular tags include:

- solar - Solar panel installations
- hvac - Heating and cooling work
- reroof - Roofing projects
- room_addition - Home additions
- kitchen_remodel - Kitchen renovations
- bath_remodel - Bathroom renovations
- new_dwelling - New home construction
- pool_spa - Pool and spa installations
- utilities - Utility work
- window_door - Window and door replacements

Find all residential solar projects:

```python
params = {
    "permit_from": "2022-01-01",
    "permit_to": "2023-12-31",
    "geo_id": "TX",
    "property_type": "residential",
    "permit_tags": ["solar"]
}
```

## Finding Permits

The `/permits/search` endpoint is your main tool for discovering permits. At minimum, you need:
- A date range (`permit_from` and `permit_to`)
- A location (`geo_id`)

> **Pro Tip:** The `geo_id` can be a state ("TX"), zip code ("78701"), city, or county. For cities and counties, you'll need to look up their specific geo_id first using our geography endpoints.

```python
response = requests.get(f"{BASE_URL}/permits/search", params=params, headers=headers)

print(response.json())
```

The response includes a wealth of information about each permit:

```json
{
  "items": [
    {
      "id": "caf3b9d5ce317d53",
      "description": "Solar panel installation with battery backup",
      "number": "RE2303928",
      "jurisdiction": "Austin",
      "property_type": "residential",
      "tags": ["solar", "utilities"],
      ...
    },
    ...
  ],
  "page": 1,
  "size": 50,
  "next_page": 2
}
```

## Finding Contractors

The contractor search works similarly to permits. Use `/contractors/search` with the same filtering capabilities:

```python
params = {
    "permit_from": "2022-01-01", 
    "permit_to": "2023-12-31",
    "geo_id": "TX",
    "property_type": "residential",
    "permit_tags": ["solar"]
}

response = requests.get(f"{BASE_URL}/contractors/search", params=params, headers=headers)
```

This will find contractors who have done residential solar work in Texas during your date range.

## Getting More Details

Once you have a permit or contractor ID, you can get full details:

```python
# Get permit details
permit_params = {"id": "caf3b9d5ce317d53"}
response = requests.get(f"{BASE_URL}/permits", params=permit_params, headers=headers)

# Get contractor details
contractor_params = {"id": "e79c3393ad"}
response = requests.get(f"{BASE_URL}/contractors", params=contractor_params, headers=headers)
```

## Beyond the Basics

The API offers many more capabilities:
- Get contractor performance metrics
- Look up employee information
- Search addresses
- Access geographic data
- Get market statistics

Check out the complete [API Reference](https://docs.shovels.ai) to explore all the possibilities. And remember to use the `/list/*` endpoints to get the latest valid values for tags and other filters.

## Need Help?

We're here to help you succeed! Reach out to `support@shovels.ai` with any questions. We love seeing what our customers build with the API.