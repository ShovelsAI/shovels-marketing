import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const COLORS = {
  primary: "#01654D",
  light: "#EAE2CF",
  dark: "#101727",
  secondary: "#E9BE51",
};

const TRANSITION_MS = 600;

const fmt = new Intl.NumberFormat("en-US");

// DOM references
const container = document.getElementById("treemap");
const tooltip = document.getElementById("treemap-tooltip");
const tooltipName = document.getElementById("tooltip-name");
const tooltipCount = document.getElementById("tooltip-count");
const tooltipPct = document.getElementById("tooltip-pct");
const breadcrumbRoot = document.getElementById("breadcrumb-root");
const breadcrumbSep = document.getElementById("breadcrumb-separator");
const breadcrumbState = document.getElementById("breadcrumb-state");
const loading = document.getElementById("treemap-loading");
const searchInput = document.getElementById("location-search-input");
const searchList = document.getElementById("location-search-list");
const dropdownBtn = document.getElementById("filter-dropdown-btn");
const dropdownLabel = document.getElementById("filter-dropdown-label");
const dropdownPanel = document.getElementById("filter-dropdown-panel");

let currentView = "states"; // "states" or "counties"
let currentState = null;
let rootData = null;

// --- Dropdown toggle ---
function openDropdown() {
  dropdownBtn.classList.add("open");
  dropdownPanel.classList.add("open");
  searchInput.value = "";
  populateSearchList("");
  // Focus search input after a frame so the panel is visible
  requestAnimationFrame(() => searchInput.focus());
}

function closeDropdown() {
  dropdownBtn.classList.remove("open");
  dropdownPanel.classList.remove("open");
  highlightTreemapItem(null);
}

function toggleDropdown() {
  if (dropdownPanel.classList.contains("open")) {
    closeDropdown();
  } else {
    openDropdown();
  }
}

dropdownBtn.addEventListener("click", toggleDropdown);

// Close dropdown when clicking outside
document.addEventListener("mousedown", (e) => {
  if (!dropdownBtn.contains(e.target) && !dropdownPanel.contains(e.target)) {
    closeDropdown();
  }
});

// Close dropdown on Escape
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeDropdown();
});

// Color scale: low → light, high → dark green
function buildColorScale(children) {
  const values = children.map((d) => d.value);
  return d3
    .scaleLog()
    .domain([Math.max(1, d3.min(values)), d3.max(values)])
    .range([COLORS.light, COLORS.primary])
    .interpolate(d3.interpolateHcl)
    .clamp(true);
}

// Decide label visibility based on rectangle size
function labelStrategy(d, totalArea) {
  const area = (d.x1 - d.x0) * (d.y1 - d.y0);
  const pct = area / totalArea;
  const w = d.x1 - d.x0;
  const h = d.y1 - d.y0;
  if (pct > 0.03 && w > 60 && h > 40) return "full"; // abbreviation + count
  if (pct > 0.008 && w > 35 && h > 20) return "abbr"; // abbreviation only
  return "none";
}

// Highlight a treemap rectangle by name (from the dropdown list)
function highlightTreemapItem(name) {
  d3.select(container)
    .selectAll(".treemap-rect")
    .classed("highlighted", false)
    .style("opacity", 1);

  if (!name) return;

  d3.select(container)
    .selectAll("g")
    .each(function (d) {
      if (d && d.data && d.data.name === name) {
        d3.select(this).select("rect").classed("highlighted", true).style("opacity", 0.85);
      }
    });
}

// Populate the dropdown list based on current view
function populateSearchList(filter) {
  searchList.innerHTML = "";
  const query = (filter || "").toLowerCase();

  let items;
  if (currentView === "states") {
    items = rootData.children
      .map((d) => ({ name: d.name, abbreviation: d.abbreviation, value: d.value }))
      .sort((a, b) => a.name.localeCompare(b.name));
  } else {
    items = currentState.children
      .map((d) => ({ name: d.name, value: d.value }))
      .sort((a, b) => a.name.localeCompare(b.name));
  }

  if (query) {
    items = items.filter(
      (d) =>
        d.name.toLowerCase().includes(query) ||
        (d.abbreviation && d.abbreviation.toLowerCase().includes(query))
    );
  }

  items.forEach((item) => {
    const div = document.createElement("div");
    div.className = "filter-dropdown-item";
    const label = item.abbreviation ? `${item.name} (${item.abbreviation})` : item.name;
    div.innerHTML =
      `<span class="name">${label}</span>` +
      `<span class="count">${fmt.format(item.value)}</span>`;

    div.addEventListener("mouseenter", () => {
      highlightTreemapItem(item.name);
      div.classList.add("active");
    });
    div.addEventListener("mouseleave", () => {
      highlightTreemapItem(null);
      div.classList.remove("active");
    });

    // Click to drill down (states view)
    if (currentView === "states") {
      div.addEventListener("click", () => {
        const original = rootData.children.find((s) => s.name === item.name);
        if (original && original.children && original.children.length > 0) {
          closeDropdown();
          drillDown(original);
        }
      });
    }

    searchList.appendChild(div);
  });
}

function updateDropdownLabel() {
  if (currentView === "states") {
    dropdownLabel.textContent = "State";
    searchInput.placeholder = "Search states...";
  } else {
    dropdownLabel.textContent = "County";
    searchInput.placeholder = "Search counties...";
  }
}

// Filter list as user types
searchInput.addEventListener("input", () => {
  populateSearchList(searchInput.value);
});

function renderTreemap(data, parentValue) {
  const rect = container.getBoundingClientRect();
  const width = rect.width;
  const height = Math.max(450, rect.height);

  // Clear existing SVG
  d3.select(container).select("svg").remove();

  const svg = d3
    .select(container)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("font-family", "'Scandia', system-ui, sans-serif");

  // Build flat leaf nodes for treemap (strip children so D3 treats items as leaves)
  const leaves_data = data.map((d) => ({
    name: d.name,
    abbreviation: d.abbreviation,
    value: d.value,
    children: d.children, // preserve for drill-down lookup, but not passed to hierarchy
  }));

  // Build hierarchy — use eachBefore to assign value directly so D3 doesn't recurse into children
  const hierarchy = d3
    .hierarchy({
      name: "root",
      children: leaves_data.map((d) => ({ name: d.name, abbreviation: d.abbreviation, value: d.value })),
    })
    .sum((d) => d.value)
    .sort((a, b) => b.value - a.value);

  d3.treemap().tile(d3.treemapSquarify).size([width, height]).padding(2).round(true)(hierarchy);

  const leaves = hierarchy.leaves();
  const totalArea = width * height;
  const colorScale = buildColorScale(data);

  // Draw rectangles
  const cells = svg
    .selectAll("g")
    .data(leaves)
    .join("g")
    .attr("transform", (d) => `translate(${d.x0},${d.y0})`);

  cells
    .append("rect")
    .attr("class", "treemap-rect")
    .attr("width", (d) => d.x1 - d.x0)
    .attr("height", (d) => d.y1 - d.y0)
    .attr("fill", (d) => colorScale(d.data.value))
    .attr("rx", 2)
    .style("opacity", 0)
    .transition()
    .duration(TRANSITION_MS)
    .style("opacity", 1);

  // Labels
  cells.each(function (d) {
    const g = d3.select(this);
    const w = d.x1 - d.x0;
    const h = d.y1 - d.y0;
    const strategy = labelStrategy(d, totalArea);
    const label = d.data.abbreviation || d.data.name;

    // Determine text color based on background brightness
    const bg = d3.color(colorScale(d.data.value));
    const lum = 0.299 * bg.r + 0.587 * bg.g + 0.114 * bg.b;
    const textColor = lum < 140 ? "#fff" : COLORS.dark;

    if (strategy === "full") {
      g.append("text")
        .attr("class", "treemap-label")
        .attr("x", w / 2)
        .attr("y", h / 2 - 8)
        .attr("fill", textColor)
        .attr("font-size", Math.min(16, w / 5) + "px")
        .attr("font-weight", "600")
        .text(label);
      g.append("text")
        .attr("class", "treemap-label")
        .attr("x", w / 2)
        .attr("y", h / 2 + 12)
        .attr("fill", textColor)
        .attr("font-size", Math.min(12, w / 7) + "px")
        .style("opacity", 0.85)
        .text(fmt.format(d.data.value));
    } else if (strategy === "abbr") {
      g.append("text")
        .attr("class", "treemap-label")
        .attr("x", w / 2)
        .attr("y", h / 2 + 4)
        .attr("fill", textColor)
        .attr("font-size", Math.min(13, w / 4) + "px")
        .attr("font-weight", "500")
        .text(label);
    }
  });

  // Interactivity
  cells
    .style("cursor", currentView === "states" ? "pointer" : "default")
    .on("mouseenter", function (_, d) {
      const pctOfTotal = ((d.data.value / parentValue) * 100).toFixed(1);
      tooltipName.textContent = d.data.name;
      tooltipCount.textContent = fmt.format(d.data.value) + " permits";
      tooltipPct.textContent = pctOfTotal + "% of " + (currentView === "states" ? "national" : "state") + " total";
      tooltip.classList.add("visible");
      d3.select(this).select("rect").style("opacity", 0.85);
    })
    .on("mousemove", function (event) {
      const x = event.clientX + 12;
      const y = event.clientY - 10;
      tooltip.style.left = x + "px";
      tooltip.style.top = y + "px";
    })
    .on("mouseleave", function () {
      tooltip.classList.remove("visible");
      d3.select(this).select("rect").classed("highlighted", false).style("opacity", 1);
    });

  // Click to drill into state
  if (currentView === "states") {
    cells.on("click", function (_, d) {
      // Look up the original data entry (with children) by name
      const original = data.find((s) => s.name === d.data.name);
      if (!original || !original.children || original.children.length === 0) return;
      drillDown(original);
    });
  }

  // Update dropdown label and list for current view
  updateDropdownLabel();
  populateSearchList("");
}

function drillDown(stateData) {
  currentView = "counties";
  currentState = stateData;

  // Update breadcrumb
  breadcrumbRoot.classList.remove("hidden");
  breadcrumbSep.classList.remove("hidden");
  breadcrumbState.classList.remove("hidden");
  breadcrumbState.textContent = stateData.name;

  // Hide tooltip
  tooltip.classList.remove("visible");

  renderTreemap(stateData.children, stateData.value);
}

function drillUp() {
  if (currentView !== "counties") return;
  currentView = "states";
  currentState = null;

  // Update breadcrumb
  breadcrumbRoot.classList.add("hidden");
  breadcrumbSep.classList.add("hidden");
  breadcrumbState.classList.add("hidden");

  // Hide tooltip
  tooltip.classList.remove("visible");

  renderTreemap(rootData.children, rootData.meta.total_permits);
}

function updateStats(data) {
  const totalCounties = data.children.reduce(
    (sum, s) => sum + (s.children ? s.children.length : 0),
    0
  );
  document.getElementById("stat-total").textContent = fmt.format(data.meta.total_permits);
  document.getElementById("stat-states").textContent = data.meta.states_covered;
  document.getElementById("stat-counties").textContent = fmt.format(totalCounties);
  document.getElementById("stat-period").textContent = data.meta.period;
  document.getElementById("stat-generated").textContent = data.meta.generated;
}

// Responsive: re-render on resize
let resizeTimer;
const observer = new ResizeObserver(() => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    if (currentView === "states") {
      renderTreemap(rootData.children, rootData.meta.total_permits);
    } else if (currentState) {
      renderTreemap(currentState.children, currentState.value);
    }
  }, 200);
});

// Breadcrumb click handler
breadcrumbRoot.addEventListener("click", drillUp);

// Initialize
async function init() {
  try {
    const response = await fetch("https://d3kha1895daa88.cloudfront.net/permit-coverage.json");
    rootData = await response.json();

    loading.remove();
    updateStats(rootData);
    renderTreemap(rootData.children, rootData.meta.total_permits);
    observer.observe(container);
  } catch (err) {
    loading.textContent = "Failed to load coverage data.";
    console.error("Coverage treemap error:", err);
  }
}

init();
