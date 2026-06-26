# CHN — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-06-26 13:56:40  |  **ISO Code:** `CHN`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 2492 GW | 8777 TWh | 5268 Mt | 101% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 279/489 plants | 38.3 GW | 0.045 GW | 28.8% |
| ⚫ **Coal** | 1000 MW | 741/1485 plants | 1428 GW | 4.77 GW | 37.2% |
| 🔥 **Gas** | 1000 MW | 57/291 plants | 206 GW | 0.2 GW | 52% |
| 🌋 **Geothermal** | 1000 MW | 0/1 plants | 0.026 GW | — | 100% |
| 💧 **Hydro Power** | 1000 MW | 99/374 plants | 404 GW | — | 85% |
| ⚛️ **Nuclear** | — | 91/91 plants | 99 GW | — | 100% |
| ☀️ **Solar** | 500 MW | 543/1408 plants | 847 GW | 0.05 GW | 91% |
| 🌊 **Windoff** | 200 MW | 160/183 plants | 65 GW | — | 100% |
| 💨 **Windon** | 360 MW | 560/1315 plants | 572 GW | 2.64 GW | 99% |
| 🔋 **Pumped Storage** | 1000 MW | 155/170 plants | 223 GW | — | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 24/31 plants | 3.28 GW | 32.2% |
| ⚫ **Coal** | 1000 MW | 178/245 plants | 257 GW | 43.6% |
| 🔥 **Gas** | 1000 MW | 30/59 plants | 113 GW | 53% |
| 💧 **Hydro Power** | 1000 MW | 20/35 plants | 109 GW | 100% |
| ⚛️ **Nuclear** | — | 76/76 plants | 86 GW | 100% |
| ☀️ **Solar** | 500 MW | 279/365 plants | 474 GW | 100% |
| 🌊 **Windoff** | 200 MW | 62/66 plants | 41.5 GW | 100% |
| 💨 **Windon** | 360 MW | 253/296 plants | 322 GW | 100% |
| 🔋 **Pumped Storage** | 1000 MW | 201/211 plants | 292 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 1432 GW | 893 GW after capacity penalty |
| 🔥 **Gas**  | 206 GW  | 174 GW after capacity penalty |

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
| **Individual Plant Coverage** | 99% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 5588 GW from all sources |
| **Plants Above Threshold** | 5804 individual plants tracked |
| **Total Plants Processed** | 7191 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **windon**: 11.71 GW
  - **solar**: 109.96 GW
  - **hydro**: 87.82 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_CHN.xlsx` — full dataset in a model-agnostic format
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
