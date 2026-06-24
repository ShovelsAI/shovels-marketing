Title: Activate Audiences with Permit Data
Description: Use building permit data to create unique home remodel and improvement audiences.
slug: audiences

{% import 'macros/faq.html' as ui_faq %}

{# Hero refreshed to the new style (grid-pattern background + font-medium
   H1 + updated illustration). The page stays live but is dropped from nav
   at launch — see REFRESH_PLAN. CTAs and lead copy kept as-is. #}
<section class="relative w-full overflow-hidden bg-white pt-20 pb-24 px-6 md:pt-28 md:pb-32 md:px-10">

  <div class="pointer-events-none absolute inset-0"
       style="background-image: linear-gradient(#ebf0ed 1px, transparent 1px), linear-gradient(90deg, #ebf0ed 1px, transparent 1px); background-size: 56px 56px; -webkit-mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%); mask-image: radial-gradient(ellipse at 50% 30%, black 40%, transparent 75%);"
       aria-hidden="true"></div>

  <div class="relative mx-auto max-w-6xl">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-10 md:gap-16 items-center">

      <div class="md:col-span-6">
        <h1 class="text-balance text-4xl font-medium tracking-tight text-gray-900 md:text-6xl">Target your ideal audience using building permit data</h1>
        <p class="mt-6 text-lg text-gray-500">Building permits provide deterministic data on home improvement activity. Create unique audiences for home remodelers, home improvement contractors, and more.</p>
        <div class="mt-8 flex flex-wrap items-center gap-x-6 gap-y-4">
          <a href="{filename}contact.md" class="inline-block rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Contact us</a>
          <a href="https://www.canva.com/design/DAGG1zhzCPg/XS_ATV42ProDgwNpuopvqA/view?utm_content=DAGG1zhzCPg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h48c3473fe5" class="text-sm font-semibold text-gray-900" target="_blank">One-pager <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>

      <div class="md:col-span-6">
        <img src="{static}/images/audiences/hero.svg" alt="Illustration of a contractor atop a wall of building-permit data blocks" class="block w-full h-auto" />
      </div>

    </div>
  </div>
</section>
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Reach in-market homeowners</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl lg:text-balance">Run your next ad campaign with building permit data</h2>
      <p class="mt-6 text-lg/8 text-gray-300">It's hard to reach people who are in the market <span class="italic">right now</span> for home improvement-related services. With building permit data, we can time this perfectly. We built a tool to help you reach them.</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            In-market for solar panel maintenance
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">We can use building permit data to see the age of each solar installation and target homeowners who are in the market for maintenance. This maintenance can be related to the battery, inverter, or other components.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            In-market for home warranty services
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">When homeowners do major remodels and additions, they often choose to get a home warranty for their major appliances. We can build specific segments for HVAC, water, and kitchen appliances.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Electric enthusiasts
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">We can use building permit data to identify homeowners who are most likely to adopt new electric appliances like solar panels, battery storage, electric vehicles, heat pump water heaters and HVAC systems, and induction ranges.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            In-market for furniture, windows and drapes
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">When homeowners add new rooms, redo kitchens and bathrooms, or push out walls, they will replace all the windows, not just the ones impacted by the construction. We can target these homeowners with ads for new couches, windows, and window treatments.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            In-market for mortgage refinancing
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">Construction is expensive, and homeowners don't always have the financing lined up when they start a project. We can target homeowners who are in the market for a mortgage refinance, home equity line of credit, or other financing options.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <svg class="flex-none size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            In-market for kitchen appliances
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">We can look at the age of each kitchen remodel and target homeowners who have not had a kitchen remodel in the last 10 years. These households are most likely to be in the market for new kitchen appliances.</p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>
<div class="overflow-hidden bg-white py-24 sm:py-32 hidden lg:block">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <p class="max-w-2xl text-pretty text-5xl font-semibold tracking-tight text-gray-900 sm:text-balance sm:text-6xl">Get the one-pager</p>
    <div class="mt-6 max-w-xl xl:col-end-1 xl:row-start-1">
      <p class="text-pretty text-lg font-medium text-gray-500 sm:text-xl/8">Let us help you build your most effective campaign ever.</p>
    </div>
    <a href="https://www.canva.com/design/DAGG1zhzCPg/XS_ATV42ProDgwNpuopvqA/view?utm_content=DAGG1zhzCPg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h48c3473fe5" target="_blank">
      <div class="relative overflow-hidden pt-16">
        <div class="mx-auto max-w-7xl">
          <img src="{static}/images/audiences-one-pager.png" alt="Audiences one-pager" class="mb-[-12%] rounded-xl shadow-2xl ring-1 ring-gray-900/10 cursor-pointer" width="2432" height="1442">
          <div class="relative" aria-hidden="true">
            <div class="absolute -inset-x-20 bottom-0 bg-gradient-to-t from-white pt-[7%]"></div>
          </div>
        </div>
      </div>
    </a>
  </div>
</div>
{{ ui_faq.faq_section(
    heading='Frequently Asked Questions',
    items=[
        {'q': 'What kind of data does Shovels use to build audiences?', 'a': 'Shovels uses building permit data, which provides deterministic information on home improvement activity. This data shows what work homeowners have done, when it was completed, and what type of project it was, allowing for precise audience targeting.'},
        {'q': 'What types of audiences can I create with Shovels?', 'a': 'You can create audiences for a wide range of segments, including homeowners in-market for solar panel maintenance, home warranty services, mortgage refinancing, kitchen appliances, furniture and windows, and electric appliance adoption (such as EVs, heat pumps, and battery storage).'},
        {'q': 'How does Shovels help me reach homeowners at the right time?', 'a': "Building permits include timing data that shows when projects were completed. Shovels uses this to identify homeowners who are likely in-market right now — for example, targeting solar panel owners whose installations are aging and may need maintenance, or homeowners who haven't remodeled their kitchen in over 10 years."},
        {'q': 'Can I use Shovels audiences for ad campaigns?', 'a': 'Yes. Shovels is designed to help you run ad campaigns by providing building permit-based audience segments. You can target homeowners with ads for products and services that match their recent or upcoming home improvement needs.'},
        {'q': 'How does Shovels identify homeowners who might need financing?', 'a': "Shovels identifies homeowners who have active construction projects, since construction is expensive and financing isn't always arranged upfront. These homeowners are strong prospects for mortgage refinancing, home equity lines of credit, and other financing products."},
    ]) }}

<div class="bg-white">
  <div class="mx-auto max-w-7xl px-6 pb-24 sm:pb-32 lg:px-8">
    <h2 class="max-w-2xl text-balance text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Explore our building permit and contractor data now</h2>
    <div class="mt-10 flex items-center gap-x-6">
      <a href="https://app.shovels.ai/" class="rounded-full bg-shovels-primary px-6 py-3 text-sm font-semibold text-white hover:bg-shovels-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get started</a>
      <a href="https://docs.shovels.ai/docs/shovels-online-quickstart-guide" class="text-sm/6 font-semibold text-gray-900">Quickstart guide <span aria-hidden="true">→</span></a>
    </div>
  </div>
</div>
