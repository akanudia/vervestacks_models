# IND — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-27 10:46:14  |  **ISO Code:** `IND`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 441 GW | 1805 TWh | 1288 Mt | 101% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 37/140 plants | 11.3 GW | 0.033 GW | 32.8% |
| ⚫ **Coal** | 500 MW | 324/710 plants | 275 GW | 0.782 GW | 37.1% |
| 🔥 **Gas** | 500 MW | 18/100 plants | 31.4 GW | — | 49.3% |
| 💧 **Hydro Power** | 110 MW | 137/267 plants | 61 GW | 0.764 GW | — |
| ⚛️ **Nuclear** | — | 31/31 plants | 13.4 GW | 0.64 GW | — |
| 🛢️ **Oil** | 500 MW | 0/6 plants | 0.656 GW | — | 38.8% |
| ☀️ **Solar** | 200 MW | 486/1190 plants | 216 GW | — | — |
| 💨 **Windon** | 200 MW | 158/395 plants | 76 GW | — | — |
| 🔋 **Pumped Storage** | 110 MW | 19/20 plants | 19.4 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 4/9 plants | 0.361 GW | 30.9% |
| ⚫ **Coal** | 500 MW | 135/141 plants | 107 GW | 41% |
| 🔥 **Gas** | 500 MW | 1/3 plants | 1.02 GW | 57% |
| 💧 **Hydro Power** | 110 MW | 122/153 plants | 78 GW | — |
| ⚛️ **Nuclear** | — | 24/24 plants | 26.3 GW | — |
| ☀️ **Solar** | 200 MW | 131/192 plants | 89 GW | — |
| 🌊 **Windoff** | 200 MW | 6/6 plants | 5 GW | — |
| 💨 **Windon** | 200 MW | 35/60 plants | 19.7 GW | — |
| 🔋 **Pumped Storage** | 110 MW | 82/82 plants | 104 GW | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 178 GW | 139 GW after capacity penalty |
| 🔥 **Gas**  | 8.62 GW  | 7.28 GW after capacity penalty |

---

## Data Sources & Coverage

### Base-Year Power Plant Specifications

- **Global Energy Monitor (GEM)** — Open-access database of individual power plants worldwide,
  including location, capacity, fuel type, commissioning year, and technical specifications.
- **International Renewable Energy Agency (IRENA)** — Global renewable energy capacity and generation
  statistics (2000–2022), disaggregated by country and technology.
- **EMBER Climate** — Global dataset tracking electricity generation, installed capacity, and emissions
  intensity (2000–2022).

### Enhanced Renewable Energy Characterization

- **GEM–REZoning–Atlite Integration** — Renewable energy units enriched with capacity factors from
  Atlite weather data and precise grid-cell locations from the REZoning database.
- Individual renewable plants receive location-specific capacity factors derived from 2013 hourly
  weather patterns.
- Plants mapped to 50×50 km REZoning grid cells for consistent spatial modelling.

### Data Processing Notes

| Metric | Value |
|--------|-------|
| **Individual Plant Coverage** | 86% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 1138 GW from all sources |
| **Plants Above Threshold** | 2319 individual plants tracked |
| **Total Plants Processed** | 3529 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **windon**: 8.18 GW
  - **bioenergy**: 7.88 GW
  - **hydro**: 2.66 GW
  - **solar**: 6.42 GW
- **EMBER data**:
  - **gas**: 1.06 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_IND.xlsx` — full dataset in a model-agnostic format
- **VEDA Model Files:** Complete model ready for Veda-TIMES execution
- **Scenario Files:** AR6 climate scenarios and policy assumptions

---

## Quality Assurance

- Cross-validation between IRENA, EMBER, and UNSD statistics
- Capacity-generation consistency checks
- Technology classification verification
- Historical data reconciliation for base year (2022)
- Renewable resource potential validated against REZoning database
- Temporal analysis verified through statistical scenario methods

*For questions about specific data sources or methodology, refer to the
[VerveStacks Methods documentation](https://vervestacks.readthedocs.io/en/latest/).*

---
*Generated by VerveStacks Energy Model Processor*
