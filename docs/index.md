# IND — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-29 16:35:32  |  **ISO Code:** `IND`

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

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 24/181 units | 8.14 GW | 11.3 GW | 0.033 GW | 34.1% |
| ⚫ **Coal** | 500 MW | 287/914 units | 178 GW | 275 GW | 0.782 GW | 39.1% |
| 🔥 **Gas** | 500 MW | 13/113 units | 8.62 GW | 31.4 GW | — | 51% |
| 💧 **Hydro Power** | 110 MW | 130/282 units | 52 GW | 61 GW | 0.764 GW | — |
| ⚛️ **Nuclear** | — | 31/31 units | 13.4 GW | 13.4 GW | 0.64 GW | — |
| 🛢️ **Oil** | 500 MW | 0/6 units | 0 GW | 0.656 GW | — | — |
| ☀️ **Solar** | 200 MW | 378/4300 units | 139 GW | 216 GW | — | — |
| 💨 **Windon** | 200 MW | 102/925 units | 34.6 GW | 76 GW | — | — |
| 🔋 **Pumped Storage** | 110 MW | 19/20 units | 19.3 GW | 19.4 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 2/11 units | 0.112 GW | 0.249 GW | 31.3% |
| ⚫ **Coal** | 500 MW | 132/150 units | 103 GW | 4.33 GW | 41.2% |
| 🔥 **Gas** | 500 MW | 1/3 units | 0.75 GW | 0.27 GW | 58% |
| 💧 **Hydro Power** | 110 MW | 111/183 units | 73 GW | 4.74 GW | — |
| ⚛️ **Nuclear** | — | 24/24 units | 26.3 GW | — | — |
| ☀️ **Solar** | 200 MW | 114/273 units | 78 GW | 11.5 GW | — |
| 🌊 **Windoff** | 200 MW | 6/6 units | 5 GW | — | — |
| 💨 **Windon** | 200 MW | 27/94 units | 13.8 GW | 5.88 GW | — |
| 🔋 **Pumped Storage** | 110 MW | 82/82 units | 104 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 194 GW | 149 GW after capacity penalty |
| 🔥 **Gas**  | 12 GW  | 10.2 GW after capacity penalty |

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
| **Plants Above Threshold** | 2316 individual plants tracked |
| **Total Plants Processed** | 3510 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 6.42 GW
  - **windon**: 8.18 GW
  - **hydro**: 2.66 GW
  - **bioenergy**: 7.88 GW
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
