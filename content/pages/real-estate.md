Title: Find the best building sites using building permits
Description: Improve site selection with our Neighborhood Vitality Index (NVI) and permit approval speed metrics to identify the most actively improving areas.
slug: real-estate

{% block background_pattern %}
<svg class="absolute inset-0 -z-10 size-full stroke-gray-200 [mask-image:radial-gradient(100%_100%_at_top_right,white,transparent)]" aria-hidden="true">
  <defs>
    <pattern id="83fd4e5a-9d52-42fc-97b6-718e5d7ee527" width="200" height="200" x="50%" y="-1" patternUnits="userSpaceOnUse">
      <path d="M100 200V.5M.5 .5H200" fill="none" />
    </pattern>
  </defs>
  <svg x="50%" y="-1" class="overflow-visible fill-gray-50">
    <path d="M-100.5 0h201v201h-201Z M699.5 0h201v201h-201Z M499.5 400h201v201h-201Z M-300.5 600h201v201h-201Z" stroke-width="0" />
  </svg>
  <rect width="100%" height="100%" stroke-width="0" fill="url(#83fd4e5a-9d52-42fc-97b6-718e5d7ee527)" />
</svg>
{% endblock background_pattern %}

<div class="relative isolate overflow-hidden">
  <div class="mx-auto max-w-7xl px-6 py-32 sm:py-40 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0 lg:grid lg:max-w-none lg:grid-cols-2 lg:gap-x-16 lg:gap-y-8 xl:grid-cols-1 xl:grid-rows-1 xl:gap-x-8">
      <h1 class="max-w-2xl text-balance text-5xl font-semibold tracking-tight text-gray-900 sm:text-7xl lg:col-span-2 xl:col-auto">Pick smarter locations</h1>
      <div class="mt-6 max-w-xl lg:mt-0 xl:col-end-1 xl:row-start-1">
        <p class="text-pretty text-lg font-medium text-gray-500 sm:text-xl/8">Building permits tell you what’s changing nearby and how long it takes to put shovels in the ground. Shovels brings these insights to the surface so you can determine the best locations for your next development.</p>
        <div class="mt-10 flex items-center gap-x-6">
          <a href="https://app.shovels.ai/" class="rounded-md bg-emerald-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-emerald-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-600">Get started</a>
          <a href="{filename}/posts/newsletter-aug-24.md" class="text-sm/6 font-semibold text-gray-900" target="_blank">Read more <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <div class="mt-10 aspect-6/5 w-full max-w-lg rounded-2xl object-cover sm:mt-16 lg:mt-0 lg:max-w-none xl:row-span-2 xl:row-end-2 xl:mt-46">
        <img class="relative max-h-[500px]" src="theme/images/builders/hero.svg" alt="Illustration showing building materials and construction data analytics">
      </div>
    </div>
  </div>
  <div class="absolute inset-x-0 bottom-0 -z-10 h-24 bg-gradient-to-t from-white sm:h-32"></div>
</div>
<div class="bg-white pb-12 sm:pb-16">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="grid grid-cols-1 items-center gap-x-8 gap-y-16 lg:grid-cols-2">
      <div class="mx-auto w-full max-w-xl lg:mx-0">
        <h2 class="text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Partners</h2>
        <p class="mt-6 text-lg/8 text-gray-600">We partner with leading geospatial companies to bring you the best data and tools for your site selection process.</p>
        <!--
        <div class="mt-8 flex items-center gap-x-6">
          <a href="#" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Create account</a>
          <a href="#" class="text-sm font-semibold text-gray-900">Contact us <span aria-hidden="true">&rarr;</span></a>
        </div>
        -->
      </div>
      <div class="mx-auto grid w-full max-w-xl grid-cols-2 items-center gap-12 sm:gap-16 lg:mx-0 lg:max-w-none lg:pl-8">
        <img class="max-h-24 w-full object-contain object-left" src="{static}/images/esri.svg" alt="Esri">
        <img class="max-h-24 w-full object-contain object-left" src="{static}/images/regrid.svg" alt="Regrid">
      </div>
    </div>
  </div>
</div>
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Shovels data science</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-white sm:text-balance sm:text-5xl">Neighborhood Vitality Index (NVI)</h2>
      <p class="mt-6 text-lg/8 text-gray-300">Through our partnerships with Esri and Regrid, Shovels calculates NVI by comparing the relative permit density of home improvement projects by census tract in every major metropolitan area in the country. Use NVI to find the most actively improving neighborhoods.</p>
    </div>
  </div>
  <div class="relative overflow-hidden pt-16">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <img src="{static}/images/esri-nvi-map.jpg" alt="App screenshot" class="mb-[-12%] rounded-xl shadow-2xl ring-1 ring-white/10" width="2432" height="1442">
      <div class="relative" aria-hidden="true">
        <div class="absolute -inset-x-20 bottom-0 bg-gradient-to-t from-gray-900 pt-[7%]"></div>
      </div>
    </div>
  </div>
  <div class="mx-auto mt-16 max-w-7xl px-6 sm:mt-20 md:mt-24 lg:px-8">
    <dl class="mx-auto grid max-w-2xl grid-cols-1 gap-x-6 gap-y-10 text-base/7 text-gray-300 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8 lg:gap-y-16">
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="m9 13.5 3 3m0 0 3-3m-3 3v-6m1.06-4.19-2.12-2.12a1.5 1.5 0 0 0-1.061-.44H4.5A2.25 2.25 0 0 0 2.25 6v12a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9a2.25 2.25 0 0 0-2.25-2.25h-5.379a1.5 1.5 0 0 1-1.06-.44Z" />
          </svg>
          Custom reports.
        </dt>
        <dd class="inline">Create custom reports in the schema and file format your data team prefers.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>
          Filter by property type.
        </dt>
        <dd class="inline">We use tax assessor data to filter by property type, including commercial, residential, and industrial buildings.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path fill-rule="evenodd" d="M15.312 11.424a5.5 5.5 0 0 1-9.201 2.466l-.312-.311h2.433a.75.75 0 0 0 0-1.5H3.989a.75.75 0 0 0-.75.75v4.242a.75.75 0 0 0 1.5 0v-2.43l.31.31a7 7 0 0 0 11.712-3.138.75.75 0 0 0-1.449-.39Zm1.23-3.723a.75.75 0 0 0 .219-.53V2.929a.75.75 0 0 0-1.5 0V5.36l-.31-.31A7 7 0 0 0 3.239 8.188a.75.75 0 1 0 1.448.389A5.5 5.5 0 0 1 13.89 6.11l.311.31h-2.432a.75.75 0 0 0 0 1.5h4.243a.75.75 0 0 0 .53-.219Z" clip-rule="evenodd" />
          </svg>
          Refreshed monthly.
        </dt>
        <dd class="inline">We add millions of new building permits and dozens of new jurisdictions to our database every month.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 6.75V15m6-6v8.25m.503 3.498 4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 0 0-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0Z" />
          </svg>
          Nationwide coverage.
        </dt>
        <dd class="inline">We cover all 48 states and 85% of the US population. Coverage is highest in the populated areas with the most active construction activity.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z" />
          </svg>
          Commercial and residential.
        </dt>
        <dd class="inline">We cover both commercial and residential building permits. Use NVI to find the most actively improving neighborhoods for retail, office, and industrial development.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
          </svg>
          By parcel, census tract, or ZIP.
        </dt>
        <dd class="inline">We roll up NVI by parcel, census tract, and ZIP code, giving you the most granular data possible.</dd>
      </div>
    </dl>
  </div>
</div>
<div class="overflow-hidden bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
          <p class="text-base/7 font-semibold text-shovels-primary">Modern workflow</p>
          <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">The latest tech</h2>
          <p class="mt-6 text-lg/8 text-gray-600">We use modern geospatial and data science techniques to bring you the most accurate and useful data possible.</p>
          <dl class="mt-10 max-w-xl space-y-8 text-base/7 text-gray-600 lg:max-w-none">
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 size-5 text-shovels-primary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
                  <path fill-rule="evenodd" d="M5.5 17a4.5 4.5 0 0 1-1.44-8.765 4.5 4.5 0 0 1 8.302-3.046 3.5 3.5 0 0 1 4.504 4.272A4 4 0 0 1 15 17H5.5Zm3.75-2.75a.75.75 0 0 0 1.5 0V9.66l1.95 2.1a.75.75 0 1 0 1.1-1.02l-3.25-3.5a.75.75 0 0 0-1.1 0l-3.25 3.5a.75.75 0 1 0 1.1 1.02l1.95-2.1v4.59Z" clip-rule="evenodd" />
                </svg>
                Push anywhere.
              </dt>
              <dd class="inline">We support all major cloud storage providers, including AWS, Azure, and GCP. We also push to Snowflake, BigQuery, and Databricks.</dd>
            </div>
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 size-5 text-shovels-primary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
                  <path fill-rule="evenodd" d="M10 1a4.5 4.5 0 0 0-4.5 4.5V9H5a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2h-.5V5.5A4.5 4.5 0 0 0 10 1Zm3 8V5.5a3 3 0 1 0-6 0V9h6Z" clip-rule="evenodd" />
                </svg>
                Transfer securely.
              </dt>
              <dd class="inline">We use SFTP and HTTPS to transfer your data securely. Let us do the data appending so your team can focus on what matters most.</dd>
            </div>
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 size-5 text-shovels-primary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
                  <path d="M4.632 3.533A2 2 0 0 1 6.577 2h6.846a2 2 0 0 1 1.945 1.533l1.976 8.234A3.489 3.489 0 0 0 16 11.5H4c-.476 0-.93.095-1.344.267l1.976-8.234Z" />
                  <path fill-rule="evenodd" d="M4 13a2 2 0 1 0 0 4h12a2 2 0 1 0 0-4H4Zm11.24 2a.75.75 0 0 1 .75-.75H16a.75.75 0 0 1 .75.75v.01a.75.75 0 0 1-.75.75h-.01a.75.75 0 0 1-.75-.75V15Zm-2.25-.75a.75.75 0 0 0-.75.75v.01c0 .414.336.75.75.75H13a.75.75 0 0 0 .75-.75V15a.75.75 0 0 0-.75-.75h-.01Z" clip-rule="evenodd" />
                </svg>
                New models.
              </dt>
              <dd class="inline">We use AI and modern data science to derive new insights from permit, parcel, and census tract data.</dd>
            </div>
          </dl>
        </div>
      </div>
      <img src="{static}/images/nvi.png" alt="Product screenshot" class="w-[48rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem] md:-ml-4 lg:-ml-0" width="2432" height="1442">
    </div>
  </div>
</div>
