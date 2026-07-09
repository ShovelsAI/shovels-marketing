Title: Careers at Shovels
Description: We're building the intelligence platform for the built world. We're hiring senior AI-native engineers who run teams of agents.
slug: careers

<!-- hero -->
<section class="bg-emerald-900 py-24">
  <div class="mx-auto max-w-4xl px-6">
    <div class="flex items-center justify-center">
      <div class="flex-1 text-center">
        <h1 class="hero_title text-white">Join Our Team</h1>
        <p class="hero_description !text-white">Come build the intelligence layer for the built world.</p>
      </div>
      <div class="flex-1 flex justify-center">
        <image src="/images/careers/shovels-guy-pose5.png" class="max-w-[25%]">
      </div>
    </div>
  </div>
</section>

<!-- live signal feed: demonstrate the thesis instead of describing it -->
<section class="sig-band">
  <div class="sig-wrap">
    <div class="sig-copy">
      <p class="sig-kicker">// live signal</p>
      <h2 class="sig-h2">The built world, streaming.</h2>
      <p class="sig-lede">Every building permit is a signal that someone is about to spend money on the built world. We index them across ~2,000 US jurisdictions, roughly 85% of the population, and turn the raw stream into intelligence.</p>
      <div class="sig-counter">
        <span class="sig-count" id="sig-count">0</span>
        <span class="sig-count-label">signals observed while you've been reading</span>
      </div>
      <p class="sig-foot">Now multiply by a country. That's the job.</p>
    </div>
    <div class="sig-feedwrap">
      <div class="sig-feedhead"><span class="sig-dot"></span> sample feed · illustrative</div>
      <div class="sig-feed" id="sig-feed" aria-label="Illustrative stream of building permit records"></div>
    </div>
  </div>
</section>

<style>
.sig-band { background: #0a0a0a; color: #fff; padding: 80px 0; }
.sig-wrap { max-width: 1120px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 56px; align-items: center; }
.sig-kicker { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; letter-spacing: .18em; text-transform: uppercase; color: #e8bd51; margin-bottom: 16px; }
.sig-h2 { color: #ffffff; font-size: clamp(30px, 4vw, 44px); font-weight: 700; line-height: 1.05; letter-spacing: -.02em; margin-bottom: 16px; }
.sig-lede { font-size: 16px; line-height: 1.6; color: #b9b9b6; max-width: 520px; margin-bottom: 28px; }
.sig-counter { display: flex; flex-direction: column; gap: 2px; margin-bottom: 14px; }
.sig-count { font-size: 52px; font-weight: 700; color: #e8bd51; line-height: 1; font-variant-numeric: tabular-nums; font-family: ui-monospace, Menlo, monospace; }
.sig-count-label { font-family: ui-monospace, Menlo, monospace; font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: #8a8a86; }
.sig-foot { font-size: 14px; color: #8a8a86; }
.sig-feedwrap { border: 1px solid #262626; border-radius: 3px; background: #0f0f0f; overflow: hidden; }
.sig-feedhead { font-family: ui-monospace, Menlo, monospace; font-size: 11px; letter-spacing: .08em; color: #8a8a86; padding: 10px 14px; border-bottom: 1px solid #1e1e1e; display: flex; align-items: center; gap: 8px; }
.sig-dot { width: 7px; height: 7px; border-radius: 50%; background: #e8bd51; display: inline-block; animation: sig-pulse 1.6s infinite; }
@keyframes sig-pulse { 0% { box-shadow: 0 0 0 0 rgba(232,189,81,.5); } 70% { box-shadow: 0 0 0 6px rgba(232,189,81,0); } 100% { box-shadow: 0 0 0 0 rgba(232,189,81,0); } }
.sig-feed { height: 360px; overflow: hidden; position: relative; display: flex; flex-direction: column; justify-content: flex-end; -webkit-mask-image: linear-gradient(180deg, transparent, #000 14%, #000 86%, transparent); mask-image: linear-gradient(180deg, transparent, #000 14%, #000 86%, transparent); }
.sig-row { display: flex; align-items: baseline; gap: 10px; padding: 9px 14px; border-top: 1px solid #171717; font-family: ui-monospace, Menlo, monospace; font-size: 12.5px; white-space: nowrap; animation: sig-in .5s ease; }
@keyframes sig-in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
.sig-ts { color: #6a6a66; font-size: 11px; }
.sig-city { color: #efefec; flex: 1; overflow: hidden; text-overflow: ellipsis; }
.sig-type { color: #b9b9b6; border: 1px solid #2c2c2c; border-radius: 2px; padding: 1px 6px; font-size: 11px; }
.sig-val { color: #e8bd51; font-weight: 600; }
@media (max-width: 820px) { .sig-wrap { grid-template-columns: 1fr; gap: 32px; } .sig-feed { height: 280px; } }
@media (prefers-reduced-motion: reduce) { .sig-dot { animation: none; } .sig-row { animation: none; } }
</style>

<script>
(function () {
  var feed = document.getElementById('sig-feed');
  var countEl = document.getElementById('sig-count');
  if (!feed || !countEl) return;
  var types = [['Solar PV',15000,42000],['Reroof',8000,31000],['ADU',120000,310000],['Kitchen remodel',24000,92000],['New SFR',255000,620000],['Commercial TI',80000,1900000],['Pool',44000,112000],['HVAC replace',6000,18000],['Water heater',1500,5200],['Addition',40000,185000],['Solar + battery',28000,66000],['EV charger',1200,4200],['Deck',8000,26000],['Foundation repair',12000,48000]];
  var cities = ['Austin, TX','Phoenix, AZ','Denver, CO','Tampa, FL','Columbus, OH','Raleigh, NC','Boise, ID','Nashville, TN','Sacramento, CA','Portland, OR','Charlotte, NC','Mesa, AZ','San Antonio, TX','Fort Worth, TX','Atlanta, GA','Salt Lake City, UT','Reno, NV','Kansas City, MO','Omaha, NE','Tucson, AZ'];
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function money(lo, hi) { var v = Math.round((lo + Math.random() * (hi - lo)) / 100) * 100; return '$' + v.toLocaleString('en-US'); }
  function ts() { var d = new Date(); function p(n) { return (n < 10 ? '0' : '') + n; } return p(d.getHours()) + ':' + p(d.getMinutes()) + ':' + p(d.getSeconds()); }
  var CADENCE = 1150, SEED = 10, start = Date.now();
  function addRow() {
    var t = pick(types);
    var row = document.createElement('div');
    row.className = 'sig-row';
    row.innerHTML = '<span class="sig-ts">' + ts() + '</span><span class="sig-city">' + pick(cities) + '</span><span class="sig-type">' + t[0] + '</span><span class="sig-val">' + money(t[1], t[2]) + '</span>';
    feed.appendChild(row);
    while (feed.children.length > 14) { feed.removeChild(feed.firstChild); }
  }
  // Counter is derived from real elapsed time, not tick count: throttle-proof and honest.
  function updateCount() { countEl.textContent = (SEED + Math.floor((Date.now() - start) / CADENCE)).toLocaleString('en-US'); }
  for (var i = 0; i < SEED; i++) addRow();
  updateCount();
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) { setInterval(function () { addRow(); updateCount(); }, CADENCE); }
})();
</script>

<!-- about shovels -->
<section class="my-24">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-3xl font-bold tracking-tight mb-6">About Shovels</h2>
    <p class="mb-4">Every building permit is a signal that someone is about to spend money on the built world. Millions a year, buried across thousands of government systems, in formats nobody ever agreed on. We turn that raw paper trail into intelligence: who is building what, where, and how well, in front of the people who need to see it first.</p>
    <p class="mb-4">We're not a data broker. Data brokers sell you rows. We're building the intelligence platform for the built world (the shorthand we use internally is "Palantir for the built world"), where the moat isn't the data itself, it's the signal quality and the products we build on top of it. Backed by multi-million-dollar VC funding and a growing customer base, we're taking on one of the largest, least-structured, and most valuable data sectors on earth.</p>
    <p class="mb-4">What started as two people with a big vision is now a small team of engineers and data obsessives spread across the globe. Still scrappy, still all-in.</p>
  </div>
</section>

<!-- open positions -->
<section class="my-24">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-3xl font-bold tracking-tight mb-8">Open Positions</h2>
    <!-- job cards grid -->
    <div class="grid md:grid-cols-2 gap-6">
      <!-- senior engineer card -->
      <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow flex flex-col">
        <h3 class="text-2xl font-bold mb-3">Senior AI-Native Engineer: Data, Platform &amp; Agents</h3>
        <p class="text-xs uppercase tracking-widest text-gray-400 font-mono mb-6">Remote · Read access: agents only</p>
        <a href="{filename}careers-senior-engineer.md" class="inline-block bg-emerald-900 text-white px-6 py-2 rounded hover:bg-emerald-800 transition-colors self-start mt-auto">
          View Details →
        </a>
      </div>
      <!-- fullstack engineer card -->
      <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow flex flex-col">
        <h3 class="text-2xl font-bold mb-3">Senior AI-Native Full-Stack Engineer: Product &amp; Growth</h3>
        <p class="text-xs uppercase tracking-widest text-gray-400 font-mono mb-6">Remote · Read access: agents only</p>
        <a href="{filename}careers-senior-fullstack-engineer.md" class="inline-block bg-emerald-900 text-white px-6 py-2 rounded hover:bg-emerald-800 transition-colors self-start mt-auto">
          View Details →
        </a>
      </div>
    </div>
  </div>
</section>

<!-- why shovels -->
<section class="my-24">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-3xl font-bold tracking-tight mb-6">Why Shovels?</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>AI-native, not AI hype:</strong> everyone here commands a team of agents. We built our own harness and ship with it every day, and the trajectory is one human lead running a mostly-agent team. If you'd rather live the frontier than read about it, this is where it's happening.</li>
      <li><strong>Impact from day one:</strong> your work directly shapes the product and the company.</li>
      <li><strong>Room to grow:</strong> early engineers lead real projects and shape how a mostly-agent org gets built.</li>
      <li><strong>Flexibility:</strong> fully remote, async-friendly, no strict 9-to-5.</li>
      <li><strong>Transparency:</strong> you'll see the financials and the inner workings of the business, and help steer it.</li>
      <li><strong>Great pay + stock options:</strong> competitive salary and meaningful equity in a company on the rise.</li>
    </ul>
  </div>
</section>

<!-- how we work -->
<section class="my-24">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-3xl font-bold tracking-tight mb-6">How We Work</h2>
    <p class="mb-4">We run on a written-first operating system, and not as ideology: engineering sits in Europe and the business in the US, so anything that matters has to survive a 24-hour round trip in writing. Meetings are for decisions, not updates, and most engineers have two or three a week.</p>
    <p class="mb-4">Work moves in two-week cycles, planned to about 80% so reality has room to interrupt. Every Friday the team trades agent workflows, prompt patterns, and new tools in our AI Lab. Every engineer leads a real project, kickoff to ship, within their first two quarters: scheduled, not granted by tenure. Twice a year we bring everyone together in person to connect, strategize, and celebrate.</p>
  </div>
</section>
