Title: Charlie: AI Research Assistant for Building Permit & Contractor Data
Description: Meet Charlie, the AI research assistant for the Shovels data network. Search permits, contractors, and city decisions in plain English. No SQL, no false positives, instant charts.
slug: features/charlie-preview
status: hidden

{% import 'macros/hero.html' as ui_hero %}
{% import 'macros/use_case.html' as ui %}
{% import 'macros/callout.html' as ui_callout %}
{% import 'macros/how_it_works.html' as ui_hiw %}
{% import 'macros/faq.html' as ui_faq %}
{% import 'macros/final_cta.html' as ui_cta %}

{{ ui_hero.hero(
    h1='Meet Charlie',
    description='Your AI research assistant for the Shovels data network. Ask about permits, contractors, city decisions—whatever you need.',
    cta_label='Start digging',
    cta_href='https://app.shovels.ai/signup/',
    illustration_src='/images/features/charlie/hero.svg',
    illustration_alt='Charlie, the Shovels AI research assistant') }}

{# All feature visuals are TBD placeholders — screenshots to be sourced.
   image_alt carries the intended-shot note from the copy doc. #}
{% set features = [
    {
        'number': '01',
        'title': 'Ask in plain English',
        'description': 'Charlie understands context and synonyms. She knows what you mean, not just what you type.',
        'bullets': [
            'Natural language, no SQL or API knowledge',
            'Knows database nuances and trade terminology',
            'Clickable example prompts to get started fast',
        ],
        'image_src': '/images/features/charlie/uc1-plain-english.png',
        'image_alt': 'Charlie answering a plain-English query in the chat',
    },
    {
        'number': '02',
        'title': 'Get clean results, not raw matches',
        'description': 'Charlie filters false positives automatically. She knows a "parking stacker" might be filed as an "automated parking system," and searches for both.',
        'bullets': [
            'False positives removed automatically',
            'Shows the SQL behind every answer',
            'Searches permits, contractors, and city decisions in one place',
        ],
        'image_src': '/images/features/charlie/uc2-sql.png',
        'image_alt': "Charlie's results with the SQL behind the answer shown",
    },
    {
        'number': '03',
        'title': 'Refine, visualize, and pick up where you left off',
        'description': 'Not quite right? Narrow, expand, or pivot until it is. Charlie builds charts from your questions and saves every chat.',
        'bullets': [
            "Iterative refinement until it's right",
            'Dynamic charts generated from your data',
            'Saved chats, available 24/7',
        ],
        'image_src': '/images/features/charlie/uc3-graph.png',
        'image_alt': 'A chart Charlie generated from a query inside the chat',
    },
] %}

{{ ui.use_case_section(
    eyebrow='AI-POWERED DATA INTELLIGENCE',
    heading='See what Charlie can do',
    cases=features) }}

{# Links to /permit-database (Shovels Online) — moves to
   /solutions/permit-database at launch; tracked in REFRESH_PLAN. #}
{{ ui_callout.callout(
    variant='warm',
    heading='Prefer to browse the data yourself?',
    body='Shovels Online offers construction data with hands-on filters, contractor and geography profiles, and one-click CSV downloads.',
    cta_label='Explore Shovels Online',
    cta_href='/permit-database') }}

{{ ui_hiw.how_it_works(
    eyebrow='How Charlie works',
    heading='Three steps to data intelligence',
    steps=[
        {
            'number': '1',
            'title': 'Tell Charlie what to find',
            'description': 'Just ask. "Find the top solar contractors in Texas" or "Which cities approved the most ADU permits last quarter?" No filters to configure.',
            'image': '/images/illustrations/icon-star.svg',
        },
        {
            'number': '2',
            'title': 'Watch her find it',
            'description': 'Charlie searches the entire Shovels data network—permits, contractors, city decisions—filtering out noise and false positives along the way.',
            'image': '/images/illustrations/icon-charlie-search.svg',
        },
        {
            'number': '3',
            'title': 'Get exactly what you need',
            'description': "Clean data, ready to use. Tell Charlie to narrow down, expand, or pivot. She sticks with your search until you're satisfied.",
            'image': '/images/illustrations/icon-bell.svg',
        },
    ]) }}

{{ ui_faq.faq_section(
    heading='Frequently asked questions',
    items=[
        {
            'q': 'What is Charlie?',
            'a': 'Charlie is an AI research assistant built on the Shovels data network. She turns plain-English questions into precise queries across building permits, contractors, and city decisions, then returns clean results that are ready to use—no query language required.',
        },
        {
            'q': 'What data can Charlie search?',
            'a': 'Charlie can search everything in the Shovels data network. That includes building permits from jurisdictions covering roughly 85% of the US population, contractor and license records, city and county decisions, and the property data linked to all of them.',
        },
        {
            'q': 'Do I need to know SQL or how to use an API?',
            'a': "No, you don't need any technical background. You ask questions in plain English and Charlie handles the querying. If you ever want to verify her work, she shows the SQL behind every answer so you can see exactly how she found your results.",
        },
        {
            'q': 'How is Charlie different from a regular database search?',
            'a': 'Traditional database search requires exact keywords and returns everything that happens to match. Charlie understands natural language and what you actually mean, removes false positives automatically, and keeps refining with you until the results are exactly right.',
        },
        {
            'q': 'Can Charlie create charts?',
            'a': "Yes. Charlie generates charts automatically based on your questions and the data she returns, and you can ask her to visualize any result. It's an easy way to turn a query into something you can drop straight into a report or presentation.",
        },
        {
            'q': 'How do I get access to Charlie?',
            'a': "Charlie lives within Shovels Online. Sign in with your existing Shovels account, or create a new one at app.shovels.ai/signup, and you can start asking questions right away—there's no training required and no software to install.",
        },
    ]) }}

{{ ui_cta.final_cta(
    heading='Ready to see what Charlie digs up?',
    description='Ask your first question and get answers instantly.',
    cta_label='Try it out',
    cta_href='https://app.shovels.ai/signup/') }}
