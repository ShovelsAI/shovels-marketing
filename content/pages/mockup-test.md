Title: Mock-up frame test
Description: Sandbox for the reusable browser-frame component used across the redesign. Not linked from anywhere; safe to delete once shipped.
slug: mockup-test
status: hidden

{% import 'macros/mockup.html' as ui %}

<div class="bg-white py-16">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <h1 class="text-3xl font-semibold tracking-tight text-gray-900">Browser-frame mock-up sandbox</h1>
    <p class="mt-3 text-gray-600">Same macro at various widths and aspect ratios. 30px internal padding is now the default.</p>

    <h2 class="mt-16 text-xl font-semibold text-gray-900">1. <code>mock1</code> — default <code>max-w-5xl</code></h2>
    <p class="mt-2 text-sm text-gray-500">Contractor card. Largest preset width.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/mock1.png', 'Contractor card mock-up') }}
    </div>

    <h2 class="mt-16 text-xl font-semibold text-gray-900">2. <code>mock2</code> — narrower <code>max-w-2xl</code></h2>
    <p class="mt-2 text-sm text-gray-500">Permit list with filters. Constrained so the frame can sit beside copy.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/mock2.png', 'Permits list mock-up', max_width='max-w-2xl') }}
    </div>

    <h2 class="mt-16 text-xl font-semibold text-gray-900">3. <code>mock3</code> — small <code>max-w-md</code></h2>
    <p class="mt-2 text-sm text-gray-500">Permit timeline. Tests how the chrome reads at a small frame size.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/mock3.png', 'Permit timeline mock-up', max_width='max-w-md') }}
    </div>

    <h2 class="mt-16 text-xl font-semibold text-gray-900">4. <code>mock4</code> — in a two-column hero layout</h2>
    <p class="mt-2 text-sm text-gray-500">Frame sized by the parent grid column (<code>max_width=''</code>) — the way it would appear in a real feature section.</p>
    <div class="mt-6 grid grid-cols-1 lg:grid-cols-2 gap-x-12 gap-y-8 items-center">
      <div>
        <h3 class="text-2xl font-semibold tracking-tight text-gray-900">Every permit, every parcel</h3>
        <p class="mt-4 text-gray-600">See every permit on a property — file dates, issue dates, finals, scope of work, the contractor who pulled it.</p>
      </div>
      <div>
        {{ ui.browser_frame('/images/mock4.png', 'Permit detail mock-up', max_width='') }}
      </div>
    </div>

    <hr class="mt-24 border-gray-200" />

    <h2 class="mt-16 text-3xl font-semibold tracking-tight text-gray-900">Stress test: varying image dimensions</h2>
    <p class="mt-3 text-gray-600">Real screenshots from the repo at very different aspect ratios — to confirm the frame holds up for any future asset, not just the Figma mock-ups.</p>

    <h3 class="mt-12 text-xl font-semibold text-gray-900">5. Wide screenshot — <code>addresses.png</code> (700 × 511)</h3>
    <div class="mt-6">
      {{ ui.browser_frame('/images/addresses.png', 'Address lookup screen') }}
    </div>

    <h3 class="mt-16 text-xl font-semibold text-gray-900">6. Very tall screenshot — <code>5757-permits.png</code> (800 × 1175) in <code>max-w-2xl</code></h3>
    <p class="mt-2 text-sm text-gray-500">Tests how the frame handles a portrait-orientation screenshot.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/5757-permits.png', 'Permit list view', max_width='max-w-2xl') }}
    </div>

    <h3 class="mt-16 text-xl font-semibold text-gray-900">7. Small screenshot — <code>ai-classifications.png</code> (384 × 256) in <code>max-w-md</code></h3>
    <p class="mt-2 text-sm text-gray-500">Tests whether chrome stays proportional at a small size.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/ai-classifications.png', 'AI-driven permit classification', max_width='max-w-md') }}
    </div>

    <h3 class="mt-16 text-xl font-semibold text-gray-900">8. Very large native screenshot — <code>approval-times-scatter.png</code> (2379 × 1579)</h3>
    <p class="mt-2 text-sm text-gray-500">Native size much bigger than the frame; downscaled by the browser. Confirms no overflow issues.</p>
    <div class="mt-6">
      {{ ui.browser_frame('/images/approval-times-scatter.png', 'Approval times scatterplot') }}
    </div>

  </div>
</div>
