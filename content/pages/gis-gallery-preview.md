Title: Shovels Map Gallery
Description: A gallery of live Esri ArcGIS web maps built on Shovels building-permit data — explore permit activity, density, and market signals across the United States.
slug: features/gis/gallery-preview
status: hidden

{% import 'macros/final_cta.html' as ui_cta %}

{# Loads Esri's embeddable-components web component, which defines the
   <arcgis-embedded-map> custom element used for each map below. #}
<script type="module" src="https://js.arcgis.com/5.0/embeddable-components/"></script>

{# Centered page header — reuses the hero's crossing-gradient grid
   pattern with a radial fade, but single-column and centered (no
   illustration). #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-16 px-6 md:pt-28 md:pb-20 md:px-10">
  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>
  <div class="relative mx-auto max-w-3xl text-center">
    <h1 class="text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">Shovels Map Gallery</h1>
  </div>
</section>

{# Map embeds — six live Esri ArcGIS web maps, single column. Each is
   an <arcgis-embedded-map> sized to fill the column (width:100%). Map 1
   carries an explicit center/scale (nationwide view); the rest open at
   their saved default extent. To add or reorder maps, edit the `maps`
   list — item-id and portal-url come from the ArcGIS item URL. Map 5
   lives on the public arcgis.com portal, the rest on shovels.maps. #}
{% set maps = [
    {'item_id': '0d19f3b462234657b4174b01535762bc', 'portal': 'https://shovels.maps.arcgis.com', 'center': '-97.41287064817928,38.974082964549225', 'scale': '18489297.737236'},
    {'item_id': '2ede666ff98d49e8807435cd0432a94a', 'portal': 'https://shovels.maps.arcgis.com'},
    {'item_id': '019ea7d351d44149a8e338d27329ab43', 'portal': 'https://shovels.maps.arcgis.com'},
    {'item_id': 'a5af2ce8a9f04023acff04874a7c6bd7', 'portal': 'https://shovels.maps.arcgis.com'},
    {'item_id': '463693277e9a496889945e45652ebc14', 'portal': 'https://www.arcgis.com'},
    {'item_id': '77279e96fa59489e995b3df6bf03d335', 'portal': 'https://shovels.maps.arcgis.com'},
] %}
<section class="w-full bg-white px-6 md:px-10 pb-24">
  <div class="mx-auto grid max-w-5xl grid-cols-1 gap-10">
    {% for m in maps %}
    <div class="overflow-hidden rounded-xl ring-1 ring-gray-200 shadow-sm">
      <arcgis-embedded-map
        style="height:600px;width:100%;"
        item-id="{{ m.item_id }}"
        theme="light"
        heading-enabled legend-enabled information-enabled share-enabled time-zone-label-enabled
        {% if m.center %}center="{{ m.center }}" scale="{{ m.scale }}"{% endif %}
        portal-url="{{ m.portal }}"></arcgis-embedded-map>
    </div>
    {% endfor %}
  </div>
</section>

{{ ui_cta.final_cta(
    heading='Ready to map our Shovel-ready data?',
    description='Explore our geospatial building permit intelligence now.',
    cta_label='Contact Us',
    cta_href='https://www.shovels.ai/contact') }}
