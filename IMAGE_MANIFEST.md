# Industry Page Image Manifest

Tracking system for every image on the redesigned Industry pages. Use it
as a download checklist: export/download each asset, drop it into the
listed folder under the listed filename, and tick its box. Claude then
renames (where needed), wires references into the page, and verifies on
dev in one pass.

---

## How to use this

1. **Heroes** export from **Figma** → save as **SVG** → `hero.svg`.
2. **Use-case assets** download from the **Notion comment thread** on the
  matching `UC#: Image` property (Industry Pages Copy DB) → save under
   the **Target filename** below.
3. **Match the format to the Type**:
  - **Screenshot** → PNG, tight-cropped (no baked-in padding — the
   `browser_frame` chrome adds its own). Rendered framed.
  - **Illustration** → SVG preferred (PNG ok if raster-only). Rendered
  unframed (`framed: False`), so it needs no browser chrome.
4. **Tick the box** when the new file is in place.
5. Tell Claude when a page (or batch) is dropped; Claude reconciles
  filenames, updates the page's `framed` flags if a slot's Type changed,
   and confirms the page renders with no `TBD` placeholders.

### Legend

- **Status** — `[x]` new asset delivered & in place · `[ ]` still needed
- **In repo** — `✅` a file already exists at this path (baseline; may
still be replaced) · `➖` empty slot, page currently shows a red `TBD`
placeholder or a framed blank
- **Type** — `Hero` · `Screenshot` (framed PNG) · `Illustration`
(unframed SVG)

### Naming convention

- Hero: `hero.svg`
- Use case: `uc{N}-{short-slug}.{ext}` — lowercase, hyphens, descriptive
slug, `.png` for screenshots / `.svg` for illustrations. No spaces, no
underscores, no folder-name repetition.

> Heroes and use-case assets are tracked here. **Homepage customer
> logos** are tracked separately via the Notion `Logo Use` column + the
> `Shovels_Logo_Ranking` sheet — see COMPONENTS.md → `logo_strip`.

---

## Insurance — `content/images/industries/insurance/`


| Status | Slot | Type         | Source | Target filename         | Depicts                                                                                             |
| ------ | ---- | ------------ | ------ | ----------------------- | --------------------------------------------------------------------------------------------------- |
| [ x]   | Hero | Hero         | Figma  | `hero.svg`              | Insurance hero illustration                                                                         |
| [ x]   | UC1  | Screenshot   | Notion | `uc1-underwrite.png`    | Property detail showing permit history with additions, renovations, contractor names, and dates     |
| [ x]   | UC2  | Screenshot   | Notion | `uc2-leads.png`         | Permit search filtered to recent residential permits in a ZIP, showing type, job value, and address |
| [ x]   | UC3  | Screenshot   | Notion | `uc3-verify-claims.png` | Claim vs. permit-of-record comparison flagging a discrepancy                                        |
| [ x]   | UC4  | Screenshot   | Notion | `uc4-close-gap.png`     | Permit search filtered to additions and renovations in a target ZIP by date range                   |
| [ x]   | UC5  | Illustration | Notion | `uc5-catastrophe.svg`   | Cat-modeling team watching reconstruction permits spread across a storm-affected region             |


**Cleanup**: delete leftover `use-case-placeholder.png` from this folder.

---

## Energy & Climate — `content/images/industries/climate/`


| Status | Slot | Type         | Source | Target filename             | Depicts                                                                                                                    |
| ------ | ---- | ------------ | ------ | --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                  | Energy & Climate hero illustration                                                                                         |
| [ ]    | UC1  | Screenshot   | Notion | `uc1-electrification.png`   | Contractor search filtered to solar, EV charger, and heat pump trade types, showing permit count                           |
| [ ]    | UC2  | Screenshot   | Notion | `uc2-homeowner-permits.png` | Permit search filtered to solar permits in a target ZIP, showing address, filed date, contractor *(rename from `uc2.png`)* |
| [ ]    | UC3  | Illustration | Notion | `uc3-policy.svg`            | City council chamber with a reach-code vote underway; analyst capturing the policy signal early                            |
| [ ]    | UC4  | Screenshot   | Notion | `uc4-green-mortgage.png`    | Map filtered to solar permits in a target metro, showing recent filings by location *(rename from `uc4.png`)*              |
| [ ]    | UC5  | Illustration | Notion | `uc5-oregon-map.svg`        | Region-wide Oregon county map with solar, EV charger, and heat pump installs lighting up by color                          |


---

## Building Materials — `content/images/industries/building-materials/`


| Status | Slot | Type         | Source | Target filename              | Depicts                                                                                        |
| ------ | ---- | ------------ | ------ | ---------------------------- | ---------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                   | Building materials hero illustration                                                           |
| [ ]    | UC1  | Screenshot   | Notion | `uc1-trade-metro.png`        | Contractor search filtered by trade type and metro, sorted by permit count                     |
| [ ]    | UC2  | Screenshot   | Notion | `uc2-target-metro.png`       | Map showing permit density in a target metro                                                   |
| [ ]    | UC3  | Illustration | Notion | `uc3-dealer-intel.svg`       | Materials rep and dealer at a showroom counter reviewing local contractor activity on a tablet |
| [ ]    | UC4  | Illustration | Notion | `uc4-forecast-demand.svg`    | Supply-chain planner seeing permit activity appear ahead on a production calendar              |
| [ ]    | UC5  | Screenshot   | Notion | `uc5-market-comparative.png` | Bar chart of permit volume by work type across two target metros (Hex/Sheets)                  |


---

## Home Services — `content/images/industries/home-services/`


| Status | Slot | Type         | Source | Target filename                  | Depicts                                                                                             |
| ------ | ---- | ------------ | ------ | -------------------------------- | --------------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                       | Home services hero illustration                                                                     |
| [ ]    | UC1  | Screenshot   | Notion | `uc1-contractor-marketplace.png` | Contractor detail showing license status, permit history, trade type, and active permit count       |
| [ ]    | UC2  | Illustration | Notion | `uc2-homeowner-intent.svg`       | Homeowner in a half-demo'd kitchen receiving a perfectly timed message — peak intent, first contact |
| [ ]    | UC3  | Screenshot   | Notion | `uc3-demand-by-trade.png`        | Map filtered to HVAC permits in a metro, showing ZIP-level density                                  |
| [ ]    | UC4  | Screenshot   | Notion | `uc4-verify-licenses.png`        | Contractor search showing license status, trade class, state, and permit count                      |
| [ ]    | UC5  | Screenshot   | Notion | `uc5-high-intent-homeowners.png` | Permit filter with remodel + status in review                                                       |


---

## Real Estate — `content/images/industries/real-estate/`


| Status | Slot | Type         | Source | Target filename                 | Depicts                                                                                                    |
| ------ | ---- | ------------ | ------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                      | Real estate hero illustration                                                                              |
| [ ]    | UC1  | Screenshot   | Notion | `uc1-property-history.png`      | Property detail showing full permit history with work type, contractor, and status                         |
| [ ]    | UC2  | Screenshot   | Notion | `uc2-development-pipeline.png`  | Map filtered to demolition and grading permits in a target area                                            |
| [ ]    | UC3  | Illustration | Notion | `uc3-neighborhood-momentum.svg` | Street with active renovations and rising NVI score badges — investor spotting momentum before prices move |
| [ ]    | UC4  | Screenshot   | Notion | `uc4-upzoning-decisions.png`    | Shovels Decisions feed filtered for upzoning and development-approval decisions                            |
| [ ]    | UC5  | Illustration | Notion | `uc5-market-trends.svg`         | Two analysts — one on a printed report, one on a live permit dashboard — one clearly ahead of the market   |


---

## Construction Technology — `content/images/industries/software/`


| Status | Slot | Type         | Source | Target filename                   | Depicts                                                                                           |
| ------ | ---- | ------------ | ------ | --------------------------------- | ------------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                        | Construction technology hero illustration                                                         |
| [ ]    | UC1  | Illustration | Notion | `uc1-integration-ready.svg`       | Developer receiving clean, structured permit data flowing into their platform — no raw parsing    |
| [ ]    | UC2  | Screenshot   | Notion | `uc2-contractor-verification.png` | Contractor detail showing permit history, license status, and active permits by date              |
| [ ]    | UC3  | Illustration | Notion | `uc3-upcoming-projects.svg`       | Contractor seeing upcoming projects on a map, reaching out before competitors know the jobs exist |
| [ ]    | UC4  | Screenshot   | Notion | `uc4-permit-tracking.png`         | Permit detail showing status, filing date, approval date, and inspection milestones               |
| [ ]    | UC5  | Screenshot   | Notion | `uc5-property-history.png`        | Property detail showing all historical permits by date with work type, contractor, and value      |


> Folder is `software/` (matches the live `/software/` URL). The page's
> editorial framing is "Construction Technology."

---

## Telecommunications — `content/images/industries/telecommunications/`


| Status | Slot | Type         | Source | Target filename                  | Depicts                                                                                                              |
| ------ | ---- | ------------ | ------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [ ]    | Hero | Hero         | Figma  | `hero.svg`                       | Telecommunications hero illustration                                                                                 |
| [ ]    | UC1  | Screenshot   | Notion | `uc1-new-developments.png`       | Map filtered to new construction permits in a metro, showing cluster density                                         |
| [ ]    | UC2  | Screenshot   | Notion | `uc2-competitor-filings.png`     | Map of permit filings in a defined service area, filtered by date and permit type                                    |
| [ ]    | UC3  | Illustration | Notion | `uc3-fastest-permits.svg`        | Network planner comparing two regions (fast vs. slow approvals), deciding where to deploy fiber first                |
| [ ]    | UC4  | Screenshot   | Notion | `uc4-council-intelligence.png`   | Shovels Decisions feed filtered by broadband, infrastructure, or right-of-way keywords                               |
| [ ]    | UC5  | Illustration | Notion | `uc5-protect-infrastructure.svg` | Excavator near an urban street with underground cable routes highlighted — field engineer coordinating before damage |


---

## Status summary (baseline at manifest creation)


| Page               | Hero | UC1 | UC2      | UC3 | UC4      | UC5 |
| ------------------ | ---- | --- | -------- | --- | -------- | --- |
| Insurance          | ✅    | ✅   | ✅        | ✅   | ✅        | ✅   |
| Energy & Climate   | ✅    | ✅   | ✅ rename | ✅   | ✅ rename | ✅   |
| Building Materials | ✅    | ✅   | ✅        | ➖   | ✅        | ✅   |
| Home Services      | ✅    | ➖   | ➖        | ➖   | ➖        | ➖   |
| Real Estate        | ✅    | ➖   | ➖        | ➖   | ➖        | ➖   |
| Construction Tech  | ✅    | ➖   | ➖        | ➖   | ➖        | ➖   |
| Telecommunications | ✅    | ➖   | ➖        | ➖   | ➖        | ➖   |


`✅` = file present at manifest creation · `➖` = empty slot (page shows
placeholder) · `rename` = present but filename will change on replacement.

The designer's redesign touches **most** existing assets, so `✅` marks a
baseline file, not a "done" — tick the Status box above once the **new**
version is in place.