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

<!-- national signal map: the whole country, lighting up -->
<section class="nm-band">
  <div class="nm-wrap">
    <p class="nm-kicker">// national signal</p>
    <h2 class="nm-h2">The whole country, lighting up.</h2>
    <p class="nm-lede">Millions of permits a year, across ~2,000 jurisdictions. Every dot is a metro we index; the brighter it flares, the more the built world is moving there. Zoom into any one of them and we can trace it from the first vote to the last inspection.</p>
    <div class="nm-mapwrap" id="nm-map" aria-label="Illustrative map of US metros Shovels indexes"></div>
    <div class="nm-foot">Illustrative animation. Dot position and size reflect real permit volume by metro; the flaring is decorative.</div>
  </div>
</section>

<style>
.nm-band { background: #0a0a0a; color: #fff; padding: 84px 0 44px; }
.nm-wrap { max-width: 1000px; margin: 0 auto; padding: 0 24px; }
.nm-kicker { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; letter-spacing: .18em; text-transform: uppercase; color: #e8bd51; margin-bottom: 14px; }
.nm-h2 { color: #ffffff; font-size: clamp(28px, 4vw, 44px); font-weight: 700; line-height: 1.05; letter-spacing: -.02em; margin-bottom: 14px; }
.nm-lede { font-size: 16px; line-height: 1.6; color: #b9b9b6; max-width: 660px; margin-bottom: 32px; }
.nm-mapwrap { position: relative; width: 100%; max-width: 900px; margin: 0 auto; aspect-ratio: 1.82 / 1; border: 1px solid #1c1c1c; border-radius: 4px; background: radial-gradient(ellipse at 50% 42%, #12110a 0%, #0b0b0b 72%); overflow: hidden; }
.nm-dot { position: absolute; border-radius: 50%; background: #977c2c; box-shadow: 0 0 5px rgba(151,124,44,.35); transform: translate(-50%, -50%); }
.nm-dot.nm-flare { animation: nm-flare 1.1s ease-out; }
@keyframes nm-flare { 0% { background: #f3d791; box-shadow: 0 0 6px 2px rgba(232,189,81,.9); } 45% { background: #e8bd51; } 100% { background: #977c2c; box-shadow: 0 0 0 12px rgba(232,189,81,0); } }
.nm-card { position: absolute; background: #141414; border: 1px solid #343434; border-radius: 3px; padding: 9px 12px; min-width: 158px; font-family: ui-monospace, Menlo, monospace; opacity: 0; transition: opacity .35s; pointer-events: none; z-index: 5; }
.nm-card.show { opacity: 1; }
.nm-c-city { font-size: 12px; color: #fff; font-weight: 600; }
.nm-c-stat { font-size: 11px; color: #e8bd51; margin-top: 3px; }
.nm-c-arc { display: flex; gap: 5px; margin-top: 8px; align-items: center; }
.nm-c-arc i { width: 6px; height: 6px; border-radius: 50%; background: #e8bd51; }
.nm-c-arc span { flex: 1; height: 1px; background: #3a3a3a; }
.nm-c-lbl { font-size: 9px; color: #7a7a76; margin-top: 6px; letter-spacing: .04em; text-transform: uppercase; }
.nm-foot { max-width: 900px; margin: 14px auto 0; font-family: ui-monospace, Menlo, monospace; font-size: 10.5px; color: #575753; text-align: center; }
</style>

<script>
(function () {
  var map = document.getElementById('nm-map');
  if (!map) return;
  // [city, state, permit_count, lat, lon] — real metros and volumes from Shovels data.
  var METROS = [
    ['Houston','TX',5170993,29.762,-95.414],['Los Angeles','CA',3293771,34.092,-118.383],['Denver','CO',2485955,39.733,-104.951],
    ['Austin','TX',2191076,30.297,-97.759],['Indianapolis','IN',2131523,39.785,-86.136],['Las Vegas','NV',1994117,36.092,-115.197],
    ['Jacksonville','FL',1827966,30.296,-81.626],['Portland','OR',1486948,45.524,-122.642],['New York','NY',1108140,40.753,-73.982],
    ['Colorado Springs','CO',1100818,38.874,-104.766],['Nashville','TN',1067413,36.14,-86.791],['Cleveland','OH',1008749,41.482,-81.662],
    ['Brooklyn','NY',974167,40.667,-73.954],['Orlando','FL',938287,28.509,-81.357],['Virginia Beach','VA',934555,36.823,-76.084],
    ['El Paso','TX',875808,31.806,-106.397],['Fort Wayne','IN',853574,41.1,-85.146],['Philadelphia','PA',774606,39.985,-75.156],
    ['St. Petersburg','FL',709917,27.787,-82.668],['Sacramento','CA',675213,38.561,-121.471],['Tampa','FL',664169,27.987,-82.472],
    ['Bakersfield','CA',653379,35.355,-119.051],['Oakland','CA',592197,37.802,-122.22],['San Diego','CA',537992,32.797,-117.138],
    ['Plano','TX',537893,33.051,-96.751],['Seattle','WA',528913,47.626,-122.333],['Durham','NC',454102,35.972,-78.894],
    ['Omaha','NE',445234,41.256,-96.069],['San Jose','CA',442543,37.31,-121.876],['Frisco','TX',439492,33.148,-96.824],
    ['Pensacola','FL',433630,30.454,-87.281],['Cary','NC',403390,35.781,-78.82],['Louisville','KY',396150,38.205,-85.673],
    ['Dallas','TX',388841,32.826,-96.8],['Bronx','NY',385311,40.848,-73.879],['Phoenix','AZ',382313,33.525,-112.079],
    ['Fort Worth','TX',365316,32.777,-97.349],['Modesto','CA',355519,37.662,-120.993],['Boston','MA',351594,42.33,-71.088],
    ['Atlanta','GA',341788,33.775,-84.382],['Raleigh','NC',336879,35.828,-78.637],['Columbus','OH',298284,40.002,-82.995],
    ['Staten Island','NY',278141,40.581,-74.143],['Brownsville','TX',277468,25.94,-97.484],['Killeen','TX',267093,31.089,-97.738],
    ['Gainesville','FL',255225,29.657,-82.379],['Santa Rosa','CA',249120,38.452,-122.71],['Salt Lake City','UT',245336,40.754,-111.886],
    ['Oxnard','CA',240022,34.197,-119.184],['Bellingham','WA',224581,48.757,-122.473],['Lubbock','TX',220399,33.534,-101.916],
    ['Corona','CA',220028,33.856,-117.56],['Miami Beach','FL',217122,25.807,-80.134],['Fort Collins','CO',216360,40.551,-105.069],
    ['Baltimore','MD',213313,39.31,-76.612],['Torrance','CA',207303,33.834,-118.34],['Clearwater','FL',206564,27.961,-82.747],
    ['Fontana','CA',206112,34.109,-117.458],['Salinas','CA',204313,36.686,-121.643],['Memphis','TN',203788,35.115,-89.946],
    ['Rochester','MN',201492,44.031,-92.481],['St. Louis','MO',199241,38.619,-90.358],['Bismarck','ND',197518,46.823,-100.774],
    ['Silver Spring','MD',196183,39.047,-77.022],['McKinney','TX',195110,33.194,-96.683],['Punta Gorda','FL',192787,26.913,-81.984],
    ['Vallejo','CA',191737,38.112,-122.233],['Denton','TX',190473,33.198,-97.131],['Tallahassee','FL',187995,30.49,-84.25],
    ['Ocala','FL',187036,29.179,-82.132],['Greenville','SC',185446,34.844,-82.378]
  ];
  var LON0 = -125, LONW = 59, LAT0 = 49.5, LATH = 25;
  var counts = METROS.map(function (m) { return m[2]; });
  var lmin = Math.log(Math.min.apply(null, counts)), lmax = Math.log(Math.max.apply(null, counts));
  function sizeOf(c) { return 3 + (Math.log(c) - lmin) / (lmax - lmin) * 6.5; }
  function stat(c) { return c >= 1e6 ? (c / 1e6).toFixed(1) + 'M permits indexed' : Math.round(c / 1000) + 'K permits indexed'; }

  var dots = [];
  var cumw = [], total = 0;
  METROS.forEach(function (m, i) {
    var x = (m[4] - LON0) / LONW * 100, y = (LAT0 - m[3]) / LATH * 100, sz = sizeOf(m[2]);
    var el = document.createElement('div');
    el.className = 'nm-dot';
    el.style.left = x + '%'; el.style.top = y + '%'; el.style.width = sz + 'px'; el.style.height = sz + 'px';
    map.appendChild(el);
    dots.push({ el: el, x: x, y: y });
    total += Math.sqrt(m[2]); cumw.push(total);
  });
  function weightedIdx() { var r = Math.random() * total; for (var i = 0; i < cumw.length; i++) { if (r <= cumw[i]) return i; } return cumw.length - 1; }

  var card = document.createElement('div');
  card.className = 'nm-card';
  card.innerHTML = '<div class="nm-c-city"></div><div class="nm-c-stat"></div><div class="nm-c-arc"><i></i><span></span><i></i><span></span><i></i><span></span><i></i><span></span><i></i></div><div class="nm-c-lbl">decision → permit → complete</div>';
  map.appendChild(card);

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function showCard(i) {
    var m = METROS[i], dn = dots[i];
    card.querySelector('.nm-c-city').textContent = m[0] + ', ' + m[1];
    card.querySelector('.nm-c-stat').textContent = stat(m[2]);
    var cx = Math.min(84, Math.max(16, dn.x));
    card.style.left = cx + '%';
    if (dn.y < 34) { card.style.top = (dn.y + 3) + '%'; card.style.transform = 'translate(-50%, 8%)'; }
    else { card.style.top = (dn.y - 3) + '%'; card.style.transform = 'translate(-50%, -108%)'; }
    card.classList.add('show');
  }

  if (reduce) { dots.forEach(function (dn) { dn.el.style.background = '#8a742e'; }); showCard(3); return; }

  setInterval(function () { var i = weightedIdx(); var el = dots[i].el; el.classList.remove('nm-flare'); void el.offsetWidth; el.classList.add('nm-flare'); }, 320);
  var cardOn = false;
  setInterval(function () {
    if (cardOn) { card.classList.remove('show'); cardOn = false; }
    else { showCard(weightedIdx()); cardOn = true; }
  }, 2400);
})();
</script>

<!-- signal lifecycle: from a government decision to a finished building -->
<section class="lc-band">
  <div class="lc-wrap">
    <p class="lc-kicker">// signal lifecycle</p>
    <h2 class="lc-h2">We see it before it's built.</h2>
    <p class="lc-lede">The built world starts as a line item in a government meeting. We capture that decision, then follow it into the ground: the rezoning, the plat, the permits, the build. Watch one go from a vote to the keys.</p>

    <div class="lc-stage">
      <div class="lc-topbar">
        <div><span class="lc-proj" id="lc-proj">—</span><span class="lc-city" id="lc-city"></span></div>
        <div class="lc-clock" id="lc-clock">—</div>
      </div>
      <div class="lc-detail" id="lc-detail">&nbsp;</div>
      <div class="lc-track" id="lc-track">
        <div class="lc-line"></div>
        <div class="lc-fill" id="lc-fill"></div>
        <div class="lc-playhead" id="lc-playhead"></div>
      </div>
      <div class="lc-arc">decision · plat · permit · construction · complete</div>
      <div class="lc-punch" id="lc-punch">&nbsp;</div>
      <div class="lc-foot">Illustrative. Built from real Shovels signal types: planning decisions, plats, permits, and inspections.</div>
    </div>
  </div>
</section>

<style>
.lc-band { background: #0a0a0a; color: #fff; padding: 84px 0; }
.lc-wrap { max-width: 1000px; margin: 0 auto; padding: 0 24px; }
.lc-kicker { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; letter-spacing: .18em; text-transform: uppercase; color: #e8bd51; margin-bottom: 14px; }
.lc-h2 { color: #ffffff; font-size: clamp(28px, 4vw, 44px); font-weight: 700; line-height: 1.05; letter-spacing: -.02em; margin-bottom: 14px; }
.lc-lede { font-size: 16px; line-height: 1.6; color: #b9b9b6; max-width: 640px; margin-bottom: 36px; }
.lc-stage { border: 1px solid #262626; border-radius: 4px; background: #0f0f0f; padding: 22px 26px 20px; }
.lc-topbar { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; flex-wrap: wrap; }
.lc-proj { font-weight: 700; font-size: 17px; color: #fff; }
.lc-city { font-family: ui-monospace, Menlo, monospace; font-size: 12px; color: #8a8a86; margin-left: 10px; }
.lc-clock { font-family: ui-monospace, Menlo, monospace; font-size: 20px; color: #e8bd51; font-variant-numeric: tabular-nums; letter-spacing: .02em; }
.lc-detail { min-height: 46px; margin: 20px 0 24px; font-size: 15px; color: #e8e8e5; line-height: 1.5; display: flex; align-items: center; gap: 11px; flex-wrap: wrap; }
.lc-chip { font-family: ui-monospace, Menlo, monospace; font-size: 10px; letter-spacing: .1em; text-transform: uppercase; color: #0a0a0a; background: #e8bd51; border-radius: 2px; padding: 3px 8px; white-space: nowrap; }
.lc-track { position: relative; height: 24px; margin: 6px 0; }
.lc-line { position: absolute; left: 0; right: 0; top: 11px; height: 2px; background: #232323; }
.lc-fill { position: absolute; left: 0; top: 11px; height: 2px; width: 0; background: #e8bd51; }
.lc-playhead { position: absolute; top: 2px; left: 0; width: 2px; height: 20px; background: #fff; box-shadow: 0 0 8px rgba(255,255,255,.55); }
.lc-node { position: absolute; top: 4px; width: 15px; height: 15px; margin-left: -7px; border-radius: 50%; background: #0f0f0f; border: 2px solid #333; transition: background .2s, border-color .2s, transform .2s; }
.lc-node.on { background: #e8bd51; border-color: #e8bd51; transform: scale(1.13); }
.lc-arc { font-family: ui-monospace, Menlo, monospace; font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; color: #5f5f5b; margin-top: 12px; }
.lc-punch { min-height: 24px; margin-top: 22px; font-size: 15px; font-weight: 600; color: #e8bd51; }
.lc-foot { margin-top: 16px; font-family: ui-monospace, Menlo, monospace; font-size: 10.5px; color: #575753; }
@media (max-width: 600px) { .lc-clock { font-size: 16px; } }
</style>

<script>
(function () {
  var track = document.getElementById('lc-track');
  var fill = document.getElementById('lc-fill');
  var playhead = document.getElementById('lc-playhead');
  var clockEl = document.getElementById('lc-clock');
  var detailEl = document.getElementById('lc-detail');
  var punchEl = document.getElementById('lc-punch');
  var projEl = document.getElementById('lc-proj');
  var cityEl = document.getElementById('lc-city');
  if (!track) return;

  var MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  function d(s) { var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function fmt(ms) { var x = new Date(ms); return MON[x.getMonth()] + ' ' + x.getFullYear(); }

  var projects = [
    { name: 'Cedar & 8th', city: 'Austin, TX', stages: [
      { t: '2022-03-14', stage: 'Council decision', text: 'Rezoned R-1 → CAC-1(EX). 240-unit mixed-use approved.' },
      { t: '2023-01-19', stage: 'Final plat', text: 'Subdivision and site plan approved.' },
      { t: '2023-08-02', stage: 'Building permit', text: 'New commercial building filed. $38.4M.' },
      { t: '2024-02-11', stage: 'Construction', text: 'Permit issued. Three structures, 22k sqft retail.' },
      { t: '2025-11-06', stage: 'Complete', text: 'Certificate of occupancy. 240 homes.' } ] },
    { name: 'Harbor Logistics Park', city: 'Mesa, AZ', stages: [
      { t: '2021-09-08', stage: 'Council decision', text: 'Rezoned A-1 → I-1. 1.1M sqft distribution center approved.' },
      { t: '2022-06-15', stage: 'Plan amendment', text: 'Site plan and traffic study approved.' },
      { t: '2023-03-30', stage: 'Building permit', text: 'New light-industrial warehouse filed. $61M.' },
      { t: '2023-11-19', stage: 'Construction', text: 'Permit issued. Two rail spurs.' },
      { t: '2024-12-02', stage: 'Complete', text: 'Final inspection passed. 1.1M sqft online.' } ] },
    { name: 'Grove Town Center', city: 'Raleigh, NC', stages: [
      { t: '2022-05-02', stage: 'Council decision', text: 'Special Use Permit approved. Retail + drive-through, B-2.' },
      { t: '2023-02-10', stage: 'Final plat', text: 'Lot consolidation approved.' },
      { t: '2023-09-25', stage: 'Building permit', text: 'New commercial building filed. $9.7M.' },
      { t: '2024-03-30', stage: 'Construction', text: 'Permit issued. Restaurant + retail shell.' },
      { t: '2025-04-14', stage: 'Complete', text: 'Certificate of occupancy.' } ] }
  ];

  var PLAY = 9000, HOLD = 2800;
  var nodes = [];
  var cur = -1, t0 = 0, span = 1, months = 0, startTs = 0, holding = false, holdUntil = 0;

  function months_between(a, b) { return Math.round((b - a) / (1000 * 60 * 60 * 24 * 30.44)); }

  function loadProject(i) {
    cur = i;
    var pr = projects[i];
    projEl.textContent = pr.name;
    cityEl.textContent = pr.city;
    t0 = d(pr.stages[0].t).getTime();
    var t1 = d(pr.stages[pr.stages.length - 1].t).getTime();
    span = t1 - t0;
    months = months_between(t0, t1);
    // rebuild nodes
    for (var k = 0; k < nodes.length; k++) track.removeChild(nodes[k].el);
    nodes = [];
    for (var s = 0; s < pr.stages.length; s++) {
      var pos = (d(pr.stages[s].t).getTime() - t0) / span * 100;
      var el = document.createElement('div');
      el.className = 'lc-node';
      el.style.left = pos + '%';
      track.appendChild(el);
      nodes.push({ el: el, pos: pos, stage: pr.stages[s].stage, text: pr.stages[s].text });
    }
    setProgress(0);
    punchEl.innerHTML = '&nbsp;';
  }

  function setProgress(p) {
    fill.style.width = (p * 100) + '%';
    playhead.style.left = (p * 100) + '%';
    clockEl.textContent = fmt(t0 + p * span);
    var active = 0;
    for (var k = 0; k < nodes.length; k++) {
      var on = (p * 100) >= nodes[k].pos - 0.01;
      nodes[k].el.classList.toggle('on', on);
      if (on) active = k;
    }
    detailEl.innerHTML = '<span class="lc-chip">' + nodes[active].stage + '</span><span>' + nodes[active].text + '</span>';
  }

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  loadProject(0);

  if (reduce) {
    setProgress(1);
    punchEl.textContent = 'Shovels logged this ' + months + ' months before it opened.';
    return;
  }

  startTs = performance.now();
  function frame(now) {
    if (holding) {
      if (now >= holdUntil) { holding = false; loadProject((cur + 1) % projects.length); startTs = now; }
    } else {
      var p = Math.min(1, (now - startTs) / PLAY);
      setProgress(p);
      if (p >= 1) { punchEl.textContent = 'Shovels logged this ' + months + ' months before it opened.'; holding = true; holdUntil = now + HOLD; }
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
</script>

<!-- about shovels -->
<section class="my-24">
  <div class="mx-auto max-w-4xl px-6">
    <h2 class="text-3xl font-bold tracking-tight mb-6">About Shovels</h2>
    <p class="mb-4">Every building permit is a signal that someone is about to spend money on the built world. Millions a year, scattered across thousands of government systems, in formats nobody ever agreed on. We turn that raw paper trail into intelligence: who is building what, where, and how well.</p>
    <p class="mb-4">A trillion-dollar economy runs on construction, and almost none of it is legible in real time. We make it legible, and we get it to the people who move first on it: the analysts, operators, and companies whose entire business depends on seeing where the built world is heading next. That's the intelligence layer for the built world, and we're the ones building it. Backed by multi-million-dollar VC funding and a growing customer base, going after one of the largest and least-structured data problems left.</p>
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
