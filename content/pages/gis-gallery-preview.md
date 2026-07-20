Title: Building Permit Map Gallery
Description: Interactive building-permit maps from Shovels — live ArcGIS web maps of U.S. new construction, HVAC, electrical, roofing, data center, and wildfire-recovery activity.
Summary: A collection of live, interactive Esri ArcGIS web maps built on Shovels building-permit data, covering new construction, HVAC, electrical, roofing, data center, and wildfire-recovery permit activity across the United States.
slug: features/gis/gallery-preview
status: hidden

{% import 'macros/final_cta.html' as ui_cta %}

{# Loads Esri's embeddable-components web component, which defines the
   <arcgis-embedded-map> custom element used for each map below. #}
<script type="module" src="https://js.arcgis.com/5.0/embeddable-components/"></script>

{% set gallery_intro = "Explore building permit activity across the United States through live, interactive maps built on Shovels data and powered by Esri ArcGIS. Each map visualizes a slice of our nationwide permit record — from new construction and trade permits to disaster recovery — sourced directly from permit jurisdictions." %}

{# Map embeds — live Esri ArcGIS web maps, single column. Each is an
   <arcgis-embedded-map> sized to fill the column (width:100%). Map 1
   carries an explicit center/scale (nationwide view); the rest open at
   their saved default extent. `title` and `desc` give each map crawlable
   text (also feeds the ItemList JSON-LD below), since the embeds render
   via JS and are invisible to search/AI crawlers. To add or reorder
   maps, edit the `maps` list — item-id and portal-url come from the
   ArcGIS item URL; use the Web Map item id (not a Feature Layer/Service).
   Map 5 lives on the public arcgis.com portal, the rest on shovels.maps. #}
{% set maps = [
    {
        'item_id': '0d19f3b462234657b4174b01535762bc',
        'portal': 'https://shovels.maps.arcgis.com',
        'center': '-97.41287064817928,38.974082964549225',
        'scale': '18489297.737236',
        'title': 'Nationwide New Construction Permits (Q1 2026)',
        'desc': '28,525 new residential and commercial construction permits pulled across the United States in Q1 2026, mapped with contractor and location detail.',
    },
    {
        'item_id': '2ede666ff98d49e8807435cd0432a94a',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'Top 25 Homebuilder Permits (Q1 2026)',
        'desc': "16,774 new-construction permits from the nation's 25 largest homebuilders in Q1 2026 — built for competitive research and pipeline tracking.",
    },
    {
        'item_id': '019ea7d351d44149a8e338d27329ab43',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'Data Center Permits Started Since 2020',
        'desc': '227 data center construction permits across the U.S. from 2020 through mid-2026, including colocation and hyperscale projects.',
    },
    {
        'item_id': 'a5af2ce8a9f04023acff04874a7c6bd7',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'Nationwide HVAC Permits (Q1 2026)',
        'desc': '166,433 HVAC permits pulled nationwide in Q1 2026, with contractor and property detail for residential and commercial work.',
    },
    {
        'item_id': '463693277e9a496889945e45652ebc14',
        'portal': 'https://www.arcgis.com',
        'title': 'Nationwide Electrical Permits (Q1 2026)',
        'desc': '278,844 electrical permits from Q1 2026, spanning solar, EV chargers, battery storage, and electric-meter work.',
    },
    {
        'item_id': '77279e96fa59489e995b3df6bf03d335',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'Nationwide Roofing Permits (Q1 2026)',
        'desc': '83,444 roofing permits pulled across the United States in Q1 2026, with contractor and property detail.',
    },
    {
        'item_id': 'b0dd9aaf273c4d7aa1c5f54de30368d5',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'Nationwide Telecom Permits (Q1 2026)',
        'desc': '15,366 telecom permits pulled across the United States in Q1 2026, covering fiber, broadband, and other telecommunications infrastructure with contractor and location detail.',
    },
    {
        'item_id': 'f5827b37eda247498204f98f898f7bed',
        'portal': 'https://shovels.maps.arcgis.com',
        'title': 'LA County Wildfire Recovery',
        'desc': '5,699 addresses with demolition and new-construction permits across Altadena, Pacific Palisades, and Malibu after the January 2025 wildfires, classified by recovery stage and refreshed live.',
    },
] %}

{# Centered page header — reuses the hero's crossing-gradient grid
   pattern with a radial fade, but single-column and centered (no
   illustration). #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-16 px-6 md:pt-28 md:pb-20 md:px-10">
  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>
  <div class="relative mx-auto max-w-3xl text-center">
    <h1 class="text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">Shovels Map Gallery</h1>
    <p class="mt-6 text-lg text-gray-500">{{ gallery_intro }}</p>
  </div>
</section>

<section class="w-full bg-white px-6 md:px-10 pb-24">
  <div class="mx-auto max-w-5xl space-y-16">
    {% for m in maps %}
    <div id="map-{{ loop.index }}" class="scroll-mt-24">
      <h2 class="text-2xl font-medium tracking-tight text-gray-900 md:text-3xl">{{ m.title }}</h2>
      <p class="mt-2 max-w-3xl text-base text-gray-500">{{ m.desc }}</p>
      <div class="mt-6 overflow-hidden rounded-xl ring-1 ring-gray-200 shadow-sm">
        <arcgis-embedded-map
          style="height:600px;width:100%;"
          item-id="{{ m.item_id }}"
          theme="light"
          legend-enabled information-enabled share-enabled time-zone-label-enabled
          {% if m.center %}center="{{ m.center }}" scale="{{ m.scale }}"{% endif %}
          portal-url="{{ m.portal }}"></arcgis-embedded-map>
      </div>
    </div>
    {% endfor %}
  </div>
</section>

{# Machine-readable list of the maps for search + AI answer engines. The
   embeds are JS-rendered and opaque to crawlers, so this ItemList (built
   from the same `maps` data) is how a bot learns what the gallery holds.
   Each map is a Dataset (Shovels permit data, CC BY 4.0). #}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Shovels Building Permit Map Gallery",
  "description": {{ gallery_intro | tojson }},
  "url": "https://www.shovels.ai/features/gis/gallery",
  "numberOfItems": {{ maps | length }},
  "itemListElement": [
    {% for m in maps %}
    {
      "@type": "ListItem",
      "position": {{ loop.index }},
      "item": {
        "@type": "Dataset",
        "name": {{ m.title | tojson }},
        "description": {{ m.desc | tojson }},
        "url": "https://www.shovels.ai/features/gis/gallery#map-{{ loop.index }}",
        "creator": { "@type": "Organization", "name": "Shovels", "url": "https://www.shovels.ai" },
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isAccessibleForFree": true
      }
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  ]
}
</script>

{{ ui_cta.final_cta(
    heading='Ready to map our Shovel-ready data?',
    description='Explore our geospatial building permit intelligence now.',
    cta_label='Contact Us',
    cta_href='https://www.shovels.ai/contact') }}
