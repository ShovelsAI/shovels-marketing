Title: The Intelligence Layer for the Built World
Description: Shovels turns fragmented permit data into construction intelligence. Access nationwide permit and contractor data via API, web app, or data warehouse.
slug: homepage-preview
status: hidden

{% import 'macros/logo_strip.html' as ui_logos %}

{# Customer logos in Domain Authority order — see the Shovels_Logo_Ranking
   sheet for the ranking and COMPONENTS.md → logo_strip for the swap process.
   Legal gate: cross-check the Notion "Logo Use" column before launch. #}
{% set customer_logos = [
    {'src': '/images/logos/aws.svg', 'alt': 'AWS', 'height': 34},
    {'src': '/images/logos/google.svg', 'alt': 'Google'},
    {'src': '/images/logos/oracle.svg', 'alt': 'Oracle', 'height': 22},
    {'src': '/images/logos/redfin.svg', 'alt': 'Redfin', 'height': 26},
    {'src': '/images/logos/university-of-michigan.svg', 'alt': 'University of Michigan', 'height': 34},
    {'src': '/images/logos/houzz.svg', 'alt': 'Houzz'},
    {'src': '/images/logos/angi.svg', 'alt': 'Angi'},
    {'src': '/images/logos/schneider-electric.svg', 'alt': 'Schneider Electric', 'height': 36},
    {'src': '/images/logos/thumbtack.png', 'alt': 'Thumbtack', 'height': 28},
    {'src': '/images/logos/energysage.svg', 'alt': 'EnergySage', 'height': 26},
    {'src': '/images/logos/jll.png', 'alt': 'JLL'},
    {'src': '/images/logos/frontline-wildfire.svg', 'alt': 'Frontline Wildfire Defense'},
    {'src': '/images/logos/dr-horton.svg', 'alt': 'D.R. Horton', 'height': 36},
    {'src': '/images/logos/urbanize.svg', 'alt': 'Urbanize', 'height': 26},
    {'src': '/images/logos/rewiring-america.png', 'alt': 'Rewiring America'},
    {'src': '/images/logos/qxo.svg', 'alt': 'QXO', 'height': 26},
] %}

{{ ui_logos.logo_strip(logos=customer_logos) }}
