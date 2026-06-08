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
| [ x]   | Hero | Hero         | Figma  | `hero.svg`                  | Energy & Climate hero illustration                                                                                         |
| [ x]   | UC1  | Screenshot   | Notion | `uc1-electrification.png`   | Contractor search filtered to solar, EV charger, and heat pump trade types, showing permit count                           |
| [ x]   | UC2  | Screenshot   | Notion | `uc2-solar-permits.png`     | Permit search filtered to solar permits in a target ZIP, showing address, filed date, contractor                          |
| [ x]   | UC3  | Illustration | Notion | `uc3-policy.svg`            | City council chamber with a reach-code vote underway; analyst capturing the policy signal early                            |
| [ x]   | UC4  | Screenshot   | Notion | `uc4-solar-map.png`         | Map filtered to solar permits in a target metro, showing recent filings by location                                       |
| [ x]   | UC5  | Illustration | Notion | `uc5-oregon-map.svg`        | Region-wide Oregon county map with solar, EV charger, and heat pump installs lighting up by color                          |


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

---

# Industry Logo Grids (`logo_grid`)

Per-industry static logo strips (the "companies like you" row). Source
each logo into `content/images/logos/`, then Claude wires the page's
`logo_grid` once the set is complete. Telecommunications is **skipped**
for now — no logo wall identified.

Companies are taken from the **Social Proof** column of the Industry
Pages Copy Notion DB. Logos are **not fetchable from a domain** — source
an official SVG (Wikimedia, the company's brand/press page, or a cleaned
inline SVG from their site), tight-crop it, knock out any background,
and drop it in. Color doesn't matter; the grey CSS filter flattens it.
See COMPONENTS.md → `logo_grid` / `logo_strip` for the full process and
the legal gate (Notion `Logo Use`).

**Naming**: `content/images/logos/{company-slug}.{svg|png}` — lowercase,
hyphens, SVG preferred.

### Energy & Climate — `/climate` (grid wired with 4 of 6)

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [x] | Schneider Electric | se.com | `schneider-electric.svg` | ✅ |
| [x] | EnergySage | energysage.com | `energysage.svg` | ✅ |
| [x] | Rewiring America | rewiringamerica.org | `rewiring-america.png` | ✅ |
| [x] | Frontline Wildfire | frontlinewildfire.com | `frontline-wildfire.svg` | ✅ |
| [ ] | Base Power | basepowercompany.com | `base-power.svg` | ➖ |
| [ ] | PermitPower | permitpower.org | `permitpower.svg` | ➖ |

### Real Estate — `/real-estate`

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [x] | AWS — confirmed: use existing AWS mark for amazon.com | amazon.com | `aws.svg` | ✅ |
| [x] | Redfin | redfin.com | `redfin.svg` | ✅ |
| [x] | D.R. Horton | drhorton.com | `dr-horton.svg` | ✅ |
| [x] | JLL | jll.com | `jll.png` | ✅ |
| [ ] | TRC Companies | trccompanies.com | `trc-companies.svg` | ➖ |
| [ ] | Ownwell | ownwell.com | `ownwell.svg` | ➖ |

### Home Services — `/home-services`

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [x] | Angi — confirmed (split from Houzz in Notion) | angi.com | `angi.svg` | ✅ |
| [x] | Houzz — confirmed (split from Angi in Notion) | houzz.com | `houzz.svg` | ✅ |
| [ ] | Pearl Certification | pearlcertification.com | `pearl-certification.svg` | ➖ |
| [ ] | Hawkins Service Co | hawkinsserviceco.com | `hawkins-service.svg` | ➖ |
| [ ] | Jukebox Health | jukeboxhealth.com | `jukebox-health.svg` | ➖ |
| [ ] | Peakzi | peakzi.me | `peakzi.svg` | ➖ |

### Building Materials — `/building-materials`

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [x] | QXO | qxo.com | `qxo.svg` | ✅ |
| [~] | Heidelberg Materials ⚠ sourced legacy "HeidelbergCement" mark — verify current branding | heidelbergmaterials.com | `heidelberg-materials.svg` | ✅ (Wikimedia, verify) |
| [x] | Owens Corning | owenscorning.com | `owens-corning.svg` | ✅ (Wikimedia) |
| [ ] | Avenue Roofing | avenueroofing.com | `avenue-roofing.svg` | ➖ |
| [ ] | Automate | automate-works.com | `automate.svg` | ➖ |

### Insurance — `/insurance` (only 4 listed; ⚠ confirm target count)

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [ ] | Scription | scription.com | `scription.svg` | ➖ |
| [ ] | Trinh Insurance | trinhinsurance.com | `trinh-insurance.svg` | ➖ |
| [ ] | Drodat | drodat.com | `drodat.svg` | ➖ |
| [ ] | Comeryx | comeryx.com | `comeryx.svg` | ➖ |

### Construction Technology — `/software`

| Status | Company | Domain | Target file | In repo |
|---|---|---|---|---|
| [ ] | PlanHub | planhub.com | `planhub.svg` | ➖ |
| [ ] | Fuse Service | fuseservice.com | `fuse-service.svg` | ➖ |
| [ ] | Handle | handle.com | `handle.svg` | ➖ |
| [ ] | ToolBelt | toolbelt.work | `toolbelt.svg` | ➖ |
| [ ] | Algoma | algoma.co | `algoma.svg` | ➖ |
| [ ] | Crown Roofing | crownroofing.com | `crown-roofing.svg` | ➖ |

### Telecommunications — skipped

No logo wall identified. No `logo_grid` on this page for now.

### Logo grid wiring status

| Page | Logos ready | Grid wired? |
|---|---|---|
| Energy & Climate | 4 / 6 | ✅ (4 shown; add Base Power + PermitPower when sourced) |
| Real Estate | 4 / 6 | ⬜ pending (need TRC, Ownwell) |
| Home Services | 2 / 6 | ⬜ pending (need Pearl, Hawkins, Jukebox Health, Peakzi) |
| Building Materials | 3 / 5 | ⬜ pending (need Avenue Roofing, Automate; verify Heidelberg) |
| Insurance | 0 / 4 | ⬜ pending (need all 4) |
| Construction Tech | 0 / 6 | ⬜ pending (need all 6) |
| Telecommunications | — | n/a (skipped) |

### Sourcing legend

`[x]` in repo & confirmed · `[~]` in repo, needs verification · `[ ]`
still to source. Statics that aren't on Wikimedia (most small/private
companies) need a manual scrape — source an official SVG from the
company's brand/press page, clean it, and drop it in
`content/images/logos/` under the Target file name above.
