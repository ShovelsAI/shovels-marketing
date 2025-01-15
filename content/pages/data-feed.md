Title: Building Contractor and Permit Data Feed
Description: Get nationwide building permit and contractor data directly in your Snowflake, Big Query, or Databricks environment with automatic updates and flexible delivery options.
slug: data-feed

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
      <h1 class="max-w-2xl text-balance text-5xl font-semibold tracking-tight text-gray-900 sm:text-7xl lg:col-span-2 xl:col-auto">Custom reports and data feeds</h1>
      <div class="mt-6 max-w-xl lg:mt-0 xl:col-end-1 xl:row-start-1">
        <p class="text-pretty text-lg font-medium text-gray-500 sm:text-xl/8">We'll push the full nationwide history of building permit and contractor records directly into your Snowflake, BigQuery, or Databricks accounts. We can also provide parquet files.</p>
        <div class="mt-10 flex items-center gap-x-6">
          <a href="https://app.shovels.ai/" class="rounded-md bg-emerald-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-emerald-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-600">Get started</a>
          <a href="https://docs.shovels.ai" class="text-sm/6 font-semibold text-gray-900" target="_blank">Documentation Hub<span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <div class="mt-10 aspect-6/5 w-full max-w-lg rounded-2xl object-cover sm:mt-16 lg:mt-0 lg:max-w-none xl:row-span-2 xl:row-end-2 xl:mt-46">
        <img class="relative max-h-[500px]" src="theme/images/data-feed/hero.svg" alt="Illustration showing building materials and construction data analytics">
      </div>
    </div>
  </div>
  <div class="absolute inset-x-0 bottom-0 -z-10 h-24 bg-gradient-to-t from-white sm:h-32"></div>
</div>
<div class="bg-white pb-12 sm:pb-24">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-lg grid-cols-4 items-center gap-x-8 gap-y-12 sm:max-w-xl sm:grid-cols-6 sm:gap-x-10 sm:gap-y-14 lg:mx-0 lg:max-w-none lg:grid-cols-5">
      <img class="col-span-2 max-h-12 w-full object-contain lg:col-span-1" src="theme/images/home/oracle.svg" alt="Oracle and Shovels" width="158" height="48">
      <img class="col-span-2 max-h-12 w-full object-contain sm:col-start-2 lg:col-span-1" src="{static}/images/kohler.svg" alt="Kohler" width="158">
      <img class="col-span-2 max-h-12 w-full object-contain lg:col-span-1" src="theme/images/home/topbuild.svg" alt="TopBuild" width="158" height="48">
      <img class="col-span-2 max-h-12 w-full object-contain sm:col-start-2 lg:col-span-1" src="{static}/images/beacon.svg" alt="Beacon" width="158">
      <img class="col-span-2 max-h-12 w-full object-contain sm:col-start-2 lg:col-span-1" src="theme/images/home/houzz.svg" alt="Houzz" width="158" height="48">
    </div>
  </div>
</div>
<div class="bg-gray-900 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:text-center">
      <p class="text-base/7 font-semibold text-shovels-secondary">Enterprise-grade building permit data</p>
      <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl lg:text-balance">Large scale data delivery for modern data teams</h2>
      <p class="mt-6 text-lg/8 text-gray-300">We use the latest geospatial and data science techniques to bring you the most accurate and useful data possible. We deliver to Snowflake, BigQuery, and Databricks or directly to your S3, GCS, or Azure buckets.</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/ping.png" alt="Snowflake integration icon" class="size-5 flex-none">
            Add building permit data to Snowflake
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">To get our permit data in Snowflake, we just need your public org and account identifiers. No extra engineering or security support required.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/json.png" alt="Big Query integration icon" class="size-5 flex-none">
            Add building permit data to BigQuery
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">To get permit data into your BigQuery account, we just need a Google service account. The tables will arrive pre-formatted and ready to query.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/accurate.png" alt="Parquet format icon" class="size-5 flex-none">
            Building permit parquet files
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">We know that dealing with CSV files is a massive headache, especially with complex data and confusing serializations. That's why we like parquet and prefer to send building contractor and permit data in this format.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/metrics.png" alt="Automatic updates icon" class="size-5 flex-none">
            Automatic updates
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">With our private table sharing service, updates are done automatically. When we have new production data, it flows into your Snowflake, Big Query, or Databricks account automatically.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/schema.png" alt="Custom schema icon" class="size-5 flex-none">
            Custom schema
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">For super custom reporting, we can run SQL locally and format your report exactly the way you want it. For these requests, we'll deliver as CSV and offer both one-time and monthly options.</p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base/7 font-semibold text-white">
            <img src="theme/images/data-feed/terms.png" alt="Terms and conditions icon" class="size-5 flex-none">
            Flexible terms
          </dt>
          <dd class="mt-4 flex flex-auto flex-col text-base/7 text-gray-300">
            <p class="flex-auto">We won't make your legal team nitpick every line of our terms and conditions. Terms are designed to give you flexibility to reuse and even resell Shovels data.</p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>
<div class="overflow-hidden bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
          <p class="text-base/7 font-semibold text-shovels-primary">Enterprise-grade workflows</p>
          <h2 class="mt-2 text-pretty text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">We ❤️ data warehouses</h2>
          <p class="mt-6 text-lg/8 text-gray-600">We're used to working with data science teams and integration consultants. Contact us to discuss your use case and get a data sample.</p>
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

