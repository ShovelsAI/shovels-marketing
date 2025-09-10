Title: Building Contractor and Permit API
Description: Access our V2 API with enhanced geo-search capabilities, expanded filtering, and lightning-fast response times for building permit and contractor data.
slug: api

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
      <h1 class="max-w-2xl text-balance text-5xl font-semibold tracking-tight text-gray-900 sm:text-7xl lg:col-span-2 xl:col-auto">The API for building permits and building contractors</h1>
      <div class="mt-6 max-w-xl lg:mt-0 xl:col-end-1 xl:row-start-1">
        <p class="text-pretty text-lg font-medium text-gray-500 sm:text-xl/8">Access our completely rebuilt V2 API with enhanced geo-search capabilities, expanded filtering by property and contractor attributes, and lightning-fast responses.</p>
        <div class="mt-10 flex items-center gap-x-6">
          <a href="https://app.shovels.ai/" class="rounded-md bg-shovels-primary px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-shovels-primary/80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get your API key</a>
          <a href="https://docs.shovels.ai/api-reference/" class="text-sm/6 font-semibold text-gray-900" target="_blank">API documentation <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <div class="mt-10 aspect-6/5 w-full max-w-lg rounded-2xl object-cover sm:mt-16 lg:mt-0 lg:max-w-none xl:row-span-2 xl:row-end-2 xl:mt-46">
        <img class="relative max-h-[500px]" src="theme/images/api/hero.svg" alt="Illustration showing building materials and construction data analytics">
      </div>
    </div>
  </div>
  <div class="absolute inset-x-0 bottom-0 -z-10 h-24 bg-gradient-to-t from-white sm:h-32"></div>
</div>
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl sm:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">API for the building trades</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-white sm:text-balance sm:text-5xl">Nationwide building permit and contractor data in an intuitive API</h2>
      <p class="mt-6 text-lg/8 text-gray-300">We built this API to be the most developer-friendly way to access building permit and contractor data. It is powerful, fast, and easy to understand. It works the way you expect.</p>
    </div>
  </div>
  <div class="relative overflow-hidden pt-16">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <img src="{static}/images/api-docs.png" alt="API docs screenshot" class="mb-[-12%] rounded-xl shadow-2xl ring-1 ring-white/10" width="2432" height="1442">
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
          Enhanced geographic search.
        </dt>
        <dd class="inline">Our new geo_id system enables precise searching by address, zip code, jurisdiction, city, and county - making location-based queries more powerful than ever.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>
          Advanced filtering.
        </dt>
        <dd class="inline">10x more search parameters including property specs, contractor history, and permit details - all delivered in clean JSON format.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path fill-rule="evenodd" d="M15.312 11.424a5.5 5.5 0 0 1-9.201 2.466l-.312-.311h2.433a.75.75 0 0 0 0-1.5H3.989a.75.75 0 0 0-.75.75v4.242a.75.75 0 0 0 1.5 0v-2.43l.31.31a7 7 0 0 0 11.712-3.138.75.75 0 0 0-1.449-.39Zm1.23-3.723a.75.75 0 0 0 .219-.53V2.929a.75.75 0 0 0-1.5 0V5.36l-.31-.31A7 7 0 0 0 3.239 8.188a.75.75 0 1 0 1.448.389A5.5 5.5 0 0 1 13.89 6.11l.311.31h-2.432a.75.75 0 0 0 0 1.5h4.243a.75.75 0 0 0 .53-.219Z" clip-rule="evenodd" />
          </svg>
          Regular updates.
        </dt>
        <dd class="inline">Continuous data refresh from multiple source partners, enhanced with our proprietary processing systems for maximum accuracy.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 6.75V15m6-6v8.25m.503 3.498 4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 0 0-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0Z" />
          </svg>
          Quality metrics.
        </dt>
        <dd class="inline">We include our derivative metrics (inspection pass rates and green permit types, for example) wherever it's available.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z" />
          </svg>
          Residential and commercial.
        </dt>
        <dd class="inline">We include both residential and commercial building filters in the API. Search by property type to identify commercial or residential permits and contractors.</dd>
      </div>
      <div class="relative pl-9">
        <dt class="inline font-semibold text-white">
          <svg class="absolute left-1 top-1 size-5 text-shovels-secondary" viewBox="0 0 24 24" aria-hidden="true" data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
          </svg>
          Flexible terms.
        </dt>
        <dd class="inline">We won't make your legal team nitpick every line of our terms and conditions. Terms are designed to give you flexibility to reuse and even resell Shovels output.</dd>
      </div>
    </dl>
  </div>
</div>
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-5">
      <div class="col-span-2">
        <p class="text-base/7 font-semibold text-shovels-secondary">Building permit and contractor data</p>
        <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">The construction activity API</h2>
        <p class="mt-6 text-base/7 text-gray-600">We built, simply put, the best API in the market to identify what's getting built and who's doing it.</p>
      </div>
      <dl class="col-span-3 grid grid-cols-1 gap-x-8 gap-y-10 text-base/7 text-gray-600 sm:grid-cols-2 lg:gap-y-16">
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Geographic search
          </dt>
          <dd class="mt-2">Search by zip code, city, county or custom area using our geo_id system. Each geography includes detailed construction metrics.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Advanced permit filters
          </dt>
          <dd class="mt-2">Filter permits by value, type, status, and property characteristics. Search for specific work types like roofing, HVAC, or solar installations.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Contractor intelligence
          </dt>
          <dd class="mt-2">Search contractors by specialties, license types, and work history. Track their active permits and historical performance.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Resident & employee data
          </dt>
          <dd class="mt-2">Access detailed information about contractor employees and resident property owners associated with permits.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
              Market analytics
          </dt>
          <dd class="mt-2">Get construction activity metrics by geography, including permit volumes, values, and contractor activity levels.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Address resolution
          </dt>
          <dd class="mt-2">Validate and standardize US addresses with our address search endpoint for accurate permit and contractor lookups on specific addresses.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Property details
          </dt>
          <dd class="mt-2">Access property characteristics like square footage, year built, and property type to understand the full context of permits.</dd>
        </div>
        <div class="relative pl-9">
          <dt class="font-semibold text-gray-900">
            <svg class="absolute left-0 top-1 size-5 text-shovels-secondary" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon">
              <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />
            </svg>
            Customer support
          </dt>
          <dd class="mt-2">We're here to help you with any questions or issues you might have. We're a small team, but API users are our favorite and we're dedicated to making sure you have a great experience!</dd>
        </div>
      </dl>
    </div>
  </div>
</div>
<div class="bg-gray-100">
  <div class="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:px-8">
    <h2 class="max-w-2xl text-balance text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Explore our building permit and contractor data now</h2>
    <div class="mt-10 flex items-center gap-x-6">
      <a href="https://app.shovels.ai/" class="rounded-md bg-shovels-primary px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-shovels-primary/80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-shovels-primary">Get started</a>
      <a href="https://docs.shovels.ai/docs/shovels-online-quickstart-guide" class="text-sm/6 font-semibold text-gray-900">Quickstart guide <span aria-hidden="true">→</span></a>
    </div>
  </div>
</div>