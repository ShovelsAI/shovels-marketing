Title: Building Contractor and Permit API
Description: Access our V2 API with enhanced geo-search capabilities, expanded filtering, and lightning-fast response times for building permit and contractor data.
slug: api

<!-- hero -->
<section class="hero_container">
  <div class="hero_text-container">
    <h1 class="hero_title text-amber-300">The next generation of building permit & contractor data</h1>
    <p class="hero_description text-lime-50">Access our completely rebuilt V2 API with enhanced geo-search capabilities, expanded filtering, and lightning-fast response times.</p>
    <div class="mt-10 mb-20 flex items-center gap-x-6">
      <a href="https://app.shovels.ai"
        class="shovels-button" target="_blank">Free trial <img class="inline" src="theme/images/caret-right.svg"></a>
      <a href="https://shovels-v2.redoc.ly"
        class="shovels-button bg-stone-200" target="_blank">API Documentation <img class="inline" src="theme/images/caret-right.svg"></span></a>
    </div>
  </div>
  <div class="hero_image-container">
    <img class="max-h-[500px]" src="theme/images/api/hero.svg">
  </div>
</section>

<!-- elaboration -->
<section class="mx-auto my-24 max-w-7xl px-6">
  <!-- 'table' -->
  <dl class="elaboration_container 3xl:grid-cols-4 mb-20">
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/ping.png">
        </div>
        <span class="elaboration-card_title">Enhanced Geographic Search</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">Our new geo_id system enables precise searching by address, zip code, jurisdiction, city, and county - making location-based queries more powerful than ever.</p>
      </dd>
    </div>
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/json.png">
        </div>
        <span class="elaboration-card_title">Advanced Filtering</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">10x more search parameters including property specs, contractor history, and permit details - all delivered in clean JSON format.</p>
      </dd>
    </div>
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/accurate.png">
        </div>
        <span class="elaboration-card_title">Regular Updates</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">Continuous data refresh from multiple source partners, enhanced with our proprietary processing systems for maximum accuracy.</p>
      </dd>
    </div>
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/metrics.png">
        </div>
        <span class="elaboration-card_title">Quality metrics</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">We include our derivative metrics (inspection pass rates and green permit types, for example) wherever it's available.</p>
      </dd>
    </div>
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/schema.png">
        </div>
        <span class="elaboration-card_title">Custom schema</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">We can customize schema delivery for an additional monthly fee.</p>
      </dd>
    </div>
    <div class="elaboration-card">
      <dt class="">
        <div class="mb-6">
          <img src="theme/images/api/terms.png">
        </div>
        <span class="elaboration-card_title">Flexible terms</span>
      </dt>
      <dd class="elaboration-card_text-container">
        <p class="flex-auto">We won't make your legal team nitpick every line of our terms and conditions. Terms are designed to give you flexibility to reuse and even resell Shovels output.</p>
      </dd>
    </div>
  </dl>
  <div class="mx-auto max-w-7xl px-6 lg:px-0">
    <div x-data="{
                selectedId: null,
                init() {
                    // Set the first available tab on the page on page load.
                    this.$nextTick(() => this.select(this.$id('tab', 1)))
                },
                select(id) {
                    this.selectedId = id
                },
                isSelected(id) {
                    return this.selectedId === id
                },
                whichChild(el, parent) {
                    return Array.from(parent.children).indexOf(el) + 1
                }
            }" x-id="['tab']" class="mx-auto flex flex-col md:flex-row">
          
          <ul x-ref="tablist" @keydown.right.prevent.stop="$focus.wrap().next()" @keydown.home.prevent.stop="$focus.first()" @keydown.page-up.prevent.stop="$focus.first()" @keydown.left.prevent.stop="$focus.wrap().prev()" @keydown.end.prevent.stop="$focus.last()" @keydown.page-down.prevent.stop="$focus.last()" role="tablist" class="max-w-lg m-0 p-0">
            <li>
              <button :id="$id('tab', whichChild($el.parentElement, $refs.tablist))" @click="select($el.id)" @mousedown.prevent="" @focus="select($el.id)" type="button" :tabindex="isSelected($el.id) ? 0 : -1" :aria-selected="isSelected($el.id)" :class="isSelected($el.id) ? 'bg-[#BC9842]' : 'bg-[#E8BD51]'" class="px-5 py-2.5 no-border text-left rounded-tl text-[#101727] hover:bg-[#D1AA49] bg-[#BC9842]" role="tab" id="tab-1-1" tabindex="0" aria-selected="true">
                <h2 class="text-xl uppercase">Property Permits API</h2>
                <p class="my-2">Retrieve all current and past permits pulled on a given US address. Lookup by address or parcel number.</p>
              </button>
            </li>
            <li>
              <button :id="$id('tab', whichChild($el.parentElement, $refs.tablist))" @click="select($el.id)" @mousedown.prevent="" @focus="select($el.id)" type="button" :tabindex="isSelected($el.id) ? 0 : -1" :aria-selected="isSelected($el.id)" :class="isSelected($el.id) ? 'bg-[#BC9842]' : 'bg-[#E8BD51]'" class="px-5 py-2.5 text-left text-[#101727] hover:bg-[#D1AA49] border-gray-900 bg-[#E8BD51]" role="tab" id="tab-1-2" tabindex="-1" aria-selected="false">
                  <h2 class="text-xl  uppercase">Contractor Permits API</h2>
                  <p class="my-2">Retrieve all current and past permits worked on by a contractor. Lookup by contractor name.</p>
              </button>
            </li>
            <li>
              <button :id="$id('tab', whichChild($el.parentElement, $refs.tablist))" @click="select($el.id)" @mousedown.prevent="" @focus="select($el.id)" type="button" :tabindex="isSelected($el.id) ? 0 : -1" :aria-selected="isSelected($el.id)" :class="isSelected($el.id) ? 'bg-[#BC9842]' : 'bg-[#E8BD51]'" class="px-5 py-2.5 no-border text-left rounded-bl text-[#101727] hover:bg-[#D1AA49] bg-[#E8BD51]" role="tab" id="tab-1-3" tabindex="-1" aria-selected="false">
                  <h2 class="text-xl  uppercase">Contractor Details API</h2>
                  <p class="my-2">Retrieve all derived metrics, including breakdowns of activity by permit type. Filter by region or activity metrics.</p>
              </button>
            </li>
          </ul>
          <div role="tabpanels" class="max-w-2xl rounded-r-md m-0 p-0">
            <section x-show="isSelected($id('tab', whichChild($el, $el.parentElement)))" :aria-labelledby="$id('tab', whichChild($el, $el.parentElement))" role="tabpanel" class="" aria-labelledby="tab-1-1" style="">
              <pre style="white-space: pre-wrap;"><code class="rounded-r-md language-json hljs"><span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"property_address"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"18491 Davis Ave"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"property_city"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Los Gatos"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"property_zip_code"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"95030"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"property_county"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Santa Clara"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"property_state"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"CA"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"permits"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
        <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">"project_id"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"DEV20-0118"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"status"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Finaled"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"start_date"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"2020-01-21"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"end_date"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"2021-04-12"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"duration_days"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">447</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"inspection_pass_rate"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0.67</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Battery Storage System"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"details"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Install (1) 13.5kwh energy storage system and (n) 200amp main breaker and load center"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"address"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"18491 Davis Ave"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"city"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Los Gatos"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"county"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Santa Clara"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"state"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"CA"</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-punctuation">{</span>...<span class="hljs-punctuation">}</span>
      <span class="hljs-punctuation">]</span>
      <span class="hljs-punctuation">}</span></code></pre>
            </section>
            <section x-show="isSelected($id('tab', whichChild($el, $el.parentElement)))" :aria-labelledby="$id('tab', whichChild($el, $el.parentElement))" role="tabpanel" aria-labelledby="tab-1-2" style="display: none;">
              <pre style="white-space: pre-wrap;"><code class="rounded-r-md language-json hljs"><span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"contractor_name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"TESLA ENERGY OPERATIONS INC"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_address"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"901 Page Ave"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_city"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Fremont"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_zip_code"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"94538"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_county"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Alameda"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_state"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"CA"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_phone"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"(844) 837 5201"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_license_no"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"888104"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"permits"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
        <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">"project_id"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"DEV20-0118"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"status"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Finaled"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"start_date"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"2020-01-21"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"end_date"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"2021-04-12"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"duration_days"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">447</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"inspection_pass_rate"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0.67</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Battery Storage System"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"details"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Install (1) 13.5kwh energy storage system and (n) 200amp main breaker and load center"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"address"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"18491 Davis Ave"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"city"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Los Gatos"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"county"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Santa Clara"</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">"state"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"CA"</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-punctuation">{</span>...<span class="hljs-punctuation">}</span>
      <span class="hljs-punctuation">]</span>
      <span class="hljs-punctuation">}</span></code></pre>
            </section>
            <section x-show="isSelected($id('tab', whichChild($el, $el.parentElement)))" :aria-labelledby="$id('tab', whichChild($el, $el.parentElement))" role="tabpanel" aria-labelledby="tab-1-3" style="display: none;">
              <pre style="white-space: pre-wrap;"><code class="rounded-r-md language-json hljs"><span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"contractor_name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"TESLA ENERGY OPERATIONS INC"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_address"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"901 Page Ave"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_city"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Fremont"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_zip_code"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"94538"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_county"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Alameda"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_state"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"CA"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_phone"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"(844) 837 5201"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"contractor_license_no"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"888104"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"all_permits"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">700</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"active_permits"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">162</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"expired_permits"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">55</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"avg_project_duration_days"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">198.98</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"avg_inspection_pass_rate"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0.76</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"permit_types"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
        <span class="hljs-string">"Battery Storage System"</span><span class="hljs-punctuation">,</span>
        <span class="hljs-string">"Solar Photovoltaic System"</span><span class="hljs-punctuation">,</span>
        <span class="hljs-string">"Electrical"</span>
      <span class="hljs-punctuation">]</span>
      <span class="hljs-punctuation">}</span></code></pre>
            </section>
          </div>
    </div>
    <!-- end of tabbed example API responses -->
  </div>
</section>

