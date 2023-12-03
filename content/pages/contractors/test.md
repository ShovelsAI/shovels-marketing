Title: Test Contractor
slug: contractors/test

<div class="mx-auto max-w-7xl text-base mt-10">
  <div class="md:flex no-wrap mx-2">
    <!-- Left Side -->
    <div class="w-full md:w-3/12 lg:pr-8">
      <!-- Profile Card -->
      <div class="bg-white">
        <h1 class="text-gray-900 font-bold text-3xl leading-8 my-1">Top 🐶 Construction</h1>
        <p class="text-gray-500 hover:text-gray-600 leading-6 mb-4">A top contractor active in Lafayette who specializes in 500+ sq ft remodels.</p>
        <div class="flex flex-wrap gap-2">
          <div class="inline-flex items-center rounded-full bg-gray-100 px-2.5 py-0.5 text-xs  text-gray-800">Home Addition</div>
          <div class="inline-flex items-center rounded-full bg-red-100 px-2.5 py-0.5 text-xs  text-red-800">Kitchen Renovation</div>
          <div class="inline-flex items-center rounded-full bg-yellow-100 px-2.5 py-0.5 text-xs  text-yellow-800">Major Remodel</div>
          <div class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs  text-green-800">Top 1% Pass rate</div>
          <div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs  text-blue-800">Top 1% Speed</div>
        </div>
        <dl class="divide-y divide-gray-200 border-gray-200 mt-5">
          <div class="flex justify-between py-3 text-sm ">
            <dt class="text-gray-500">Email</dt>
            <dd class="whitespace-nowrap text-gray-900">bryon@crowleycon.com</dd>
          </div>
          <div class="flex justify-between py-3 text-sm ">
            <dt class="text-gray-500">Phone</dt>
            <dd class="whitespace-nowrap text-gray-900">925-555-5555</dd>
          </div>
          <div class="flex justify-between py-3 text-sm ">
            <dt class="text-gray-500">Address</dt>
            <dd class="whitespace-nowrap text-gray-900">Lafayette, CA</dd>
          </div>
          <div class="flex justify-between py-3 text-sm ">
            <dt class="text-gray-500">License #</dt>
            <dd class="whitespace-nowrap text-gray-900 hover:font-underline">
              <a href="#" target="_blank">CA - 1234567</a>
            </dd>
          </div>
          <div class="flex justify-between py-3 text-sm ">
            <dt class="text-gray-500">License Status</dt>
            <dd><span class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs  text-green-800">Active</span></dd>
          </div>
        </dl>
      </div>
      <div class="bg-white mt-4 lg:mt-10">
        <h2 class="flex items-center space-x-3 font-bold text-gray-900 text-xl leading-8 mb-2">Similar Contractors</h2>
        <div class="grid grid-cols-3 gap-2">
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
          <span class="inline-flex h-14 w-14 items-center justify-center rounded-full bg-gray-500">
            <span class="text-xl  leading-none text-white">TW</span>
          </span>
        </div>
      </div>
    </div>
    <!-- Right Side -->
    <div class="w-full md:w-9/12 mx-2">
      <div class="mx-auto max-w-4xl">
        <dl class="my-5">
          <div id="jobChart" class="w-full h-50"></div>
        </dl>
        <dl class="mb-5 grid grid-cols-1 gap-5 sm:grid-cols-4">
          <div class="overflow-hidden rounded-lg bg-slate-50 px-4 py-5 shadow sm:p-6">
            <dt class="truncate text-sm  text-gray-500">Active Permits</dt>
            <dd class="mt-1 text-3xl font-semibold tracking-tight text-gray-900">5</dd>
          </div>
          <div class="overflow-hidden rounded-lg bg-slate-50 px-4 py-5 shadow sm:p-6">
            <dt class="truncate text-sm  text-gray-500">Typical Capacity</dt>
            <dd class="mt-1 text-3xl font-semibold tracking-tight text-gray-900">6</dd>
          </div>
          <div class="overflow-hidden rounded-lg bg-slate-50 px-4 py-5 shadow sm:p-6">
            <dt class="truncate text-sm  text-gray-500">Inspection Pass Rate</dt>
            <dd class="mt-1 text-3xl font-semibold tracking-tight text-gray-900">86%</dd>
          </div>
          <div class="overflow-hidden rounded-lg bg-slate-50 px-4 py-5 shadow sm:p-6">
            <dt class="truncate text-sm  text-gray-500">Typical Duration</dt>
            <dd class="mt-1 text-3xl font-semibold tracking-tight text-gray-900">250 days</dd>
          </div>
        </dl>
      </div>
      <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
        <dl class="mt-10 space-y-6 divide-y divide-gray-900/10 -mt-2">
          <!-- template -->
          <div x-data="{ open: false }" class="pt-6">
            <dt>
              <button type="button" x-description="Expand/collapse question button" class="flex w-full items-start justify-between text-left text-gray-900" aria-controls="faq-1" @click="open = !open" aria-expanded="false" x-bind:aria-expanded="open.toString()">
                <div>
                  <p class="text-base font-semibold leading-7">1500 sq ft addition in Lafayette</p>
                  <div class="sm:flex mt-2">
                    <p class="flex items-center text-sm text-gray-500">
                      <svg class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M5.75 2a.75.75 0 01.75.75V4h7V2.75a.75.75 0 011.5 0V4h.25A2.75 2.75 0 0118 6.75v8.5A2.75 2.75 0 0115.25 18H4.75A2.75 2.75 0 012 15.25v-8.5A2.75 2.75 0 014.75 4H5V2.75A.75.75 0 015.75 2zm-1 5.5c-.69 0-1.25.56-1.25 1.25v6.5c0 .69.56 1.25 1.25 1.25h10.5c.69 0 1.25-.56 1.25-1.25v-6.5c0-.69-.56-1.25-1.25-1.25H4.75z" clip-rule="evenodd"></path>
                      </svg>
                      265 days
                    </p>
                    <p class="mt-2 flex items-center text-sm text-gray-500 sm:ml-6 sm:mt-0">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 14.25l6-6m4.5-3.493V21.75l-3.75-1.5-3.75 1.5-3.75-1.5-3.75 1.5V4.757c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0c1.1.128 1.907 1.077 1.907 2.185zM9.75 9h.008v.008H9.75V9zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm4.125 4.5h.008v.008h-.008V13.5zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                      </svg>
                      85% pass 
                    </p>
                  </div>
                </div>
                <span class="ml-6 flex h-7 items-center">
                  <svg x-description="Icon when question is collapsed." x-state:on="Item expanded" x-state:off="Item collapsed" class="h-6 w-6" :class="{ 'hidden': open }" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6"></path>
                  </svg>
                  <svg x-description="Icon when question is expanded." x-state:on="Item expanded" x-state:off="Item collapsed" class="h-6 w-6 hidden" :class="{ 'hidden': !(open) }" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M18 12H6"></path>
                  </svg>
                </span>
              </button>
            </dt>
            <dd class="mt-4" id="faq-1" x-show="open" x-transition style="display: none;">
              <div class="flex flex-initial">
                <div id='myDiv'></div>
                <div class="pl-4">
                  <div class="flex flex-wrap gap-2 mb-4">
                    <div class="inline-flex items-center rounded-full bg-gray-100 px-2.5 py-0.5 text-xs  text-gray-800">Home Addition</div>
                    <div class="inline-flex items-center rounded-full bg-red-100 px-2.5 py-0.5 text-xs  text-red-800">Kitchen Renovation</div>
                    <div class="inline-flex items-center rounded-full bg-yellow-100 px-2.5 py-0.5 text-xs  text-yellow-800">Major Remodel</div>
                  </div>
                  <dl class="grid grid-cols-1 gap-x-2 gap-y-4 sm:grid-cols-2">
                    <div class="sm:col-span-1">
                      <dt class="text-sm  text-gray-500">Full address</dt>
                      <dd class="mt-1 text-sm text-gray-900">123 Main St, Lafayette, CA 94549</dd>
                    </div>
                    <div class="sm:col-span-1">
                      <dt class="text-sm  text-gray-500">Square footage</dt>
                      <dd class="mt-1 text-sm text-gray-900">1500</dd>
                    </div>
                    <div class="sm:col-span-1">
                      <dt class="text-sm  text-gray-500">Number of structures</dt>
                      <dd class="mt-1 text-sm text-gray-900">2</dd>
                    </div>
                    <div class="sm:col-span-1">
                      <dt class="text-sm  text-gray-500">Fees</dt>
                      <dd class="mt-1 text-sm text-gray-900">$120,000</dd>
                    </div>
                    <div class="sm:col-span-2">
                      <dt class="text-sm  text-gray-500">About</dt>
                      <dd class="mt-1 text-sm text-gray-900">Fugiat ipsum ipsum deserunt culpa aute sint do nostrud anim incididunt cillum culpa consequat. Excepteur qui ipsum aliquip consequat sint. Sit id mollit nulla mollit nostrud in ea officia proident. Irure nostrud pariatur mollit ad adipisicing reprehenderit deserunt qui eu.</dd>
                    </div>
                  </dl>
                </div>
              </div>
            </dd>
          </div>
          <!-- endtemplate -->
          <div x-data="{ open: false }" class="pt-6">
            <dt>
              <button type="button" x-description="Expand/collapse question button" class="flex w-full items-start justify-between text-left text-gray-900" aria-controls="faq-1" @click="open = !open" aria-expanded="false" x-bind:aria-expanded="open.toString()">
                <div>
                  <p class="text-base font-semibold leading-7">1500 sq ft addition in Lafayette</p>
                  <div class="sm:flex mt-2">
                    <p class="flex items-center text-sm text-gray-500">
                      <svg class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M5.75 2a.75.75 0 01.75.75V4h7V2.75a.75.75 0 011.5 0V4h.25A2.75 2.75 0 0118 6.75v8.5A2.75 2.75 0 0115.25 18H4.75A2.75 2.75 0 012 15.25v-8.5A2.75 2.75 0 014.75 4H5V2.75A.75.75 0 015.75 2zm-1 5.5c-.69 0-1.25.56-1.25 1.25v6.5c0 .69.56 1.25 1.25 1.25h10.5c.69 0 1.25-.56 1.25-1.25v-6.5c0-.69-.56-1.25-1.25-1.25H4.75z" clip-rule="evenodd"></path>
                      </svg>
                      265 days
                    </p>
                    <p class="mt-2 flex items-center text-sm text-gray-500 sm:ml-6 sm:mt-0">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 14.25l6-6m4.5-3.493V21.75l-3.75-1.5-3.75 1.5-3.75-1.5-3.75 1.5V4.757c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0c1.1.128 1.907 1.077 1.907 2.185zM9.75 9h.008v.008H9.75V9zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm4.125 4.5h.008v.008h-.008V13.5zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                      </svg>
                      85% pass 
                    </p>
                  </div>
                </div>
                <span class="ml-6 flex h-7 items-center">
                  <svg x-description="Icon when question is collapsed." x-state:on="Item expanded" x-state:off="Item collapsed" class="h-6 w-6" :class="{ 'hidden': open }" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6"></path>
                  </svg>
                  <svg x-description="Icon when question is expanded." x-state:on="Item expanded" x-state:off="Item collapsed" class="h-6 w-6 hidden" :class="{ 'hidden': !(open) }" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M18 12H6"></path>
                  </svg>
                </span>
              </button>
            </dt>
            <dd class="mt-4" id="faq-1" x-show="open" style="display: none;">
              <div class="flex flex-initial">
                <div id='myDiv2'></div>
                <div class="pl-4">
                  <p class="text-base leading-7 text-gray-600">Because they're so good at it. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas cupiditate laboriosam fugiat.</p>
                </div>
              </div>
            </dd>
          </div>
        </dl>      
      </div>
    </div>
  </div>
</div>


<script type="text/javascript">
  var jobChart = {
    x: ["2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06", "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12"],
    y: [5, 0, 2, 1, 0, 3, 1, 0, 5, 0, 1, 0],
    type: 'scatter',
    mode: 'markers',
    marker: {
      size: 12
    }
  };
  var layout = {
    showlegend: false,
    height: 150,
    margin: {
      b: 20,
      l: 30,
      r: 0,
      t: 0
    },
    yaxis: {
      title: 'Permits',
      tickmode: 'linear',
      tick0: 0,
      dtick: 1,
    }
  };
  Plotly.newPlot('jobChart', [jobChart], layout, {displayModeBar: false, responsive: true});
</script>


<script type="text/javascript">

var data = [{
  type:'scattermapbox',
  lat:['45.5017'],
  lon:['-73.5673'],
  mode:'markers',
  marker: {
    size:14
  },
  text:['Montreal'],
  showlegend: false,
}]

var layout = {
  autosize: true,
  hovermode:'closest',
  margin: {
    b: 0,
    l: 0,
    r: 0,
    t: 0
  },
  width: 350,
  height: 350,
  mapbox: {
    bearing:0,
    center: {
      lat:45,
      lon:-73
    },
    pitch:0,
    zoom:5,
    height: 350,
    logoPosition: 'top-left',
    attributionControl: false
  },
}

Plotly.setPlotConfig({
  mapboxAccessToken: "pk.eyJ1Ijoic2hvdmVscyIsImEiOiJjbGZ2azd3eG0wMWZ4M3JvYW5oMDRid3VmIn0.DOWDV3_aXoBc0NzDRs-nPQ"
})

Plotly.newPlot('myDiv', data, layout, {displayModeBar: false, responsive: true})
Plotly.newPlot('myDiv2', data, layout, {displayModeBar: false, responsive: true})

</script>