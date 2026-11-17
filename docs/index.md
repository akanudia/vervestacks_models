# VNM — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-11-17 09:13:52  |  **ISO Code:** `VNM`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 78 GW | 265 TWh | 109 Mt | 99% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 4/21 units | 0.258 GW | 0.648 GW | 30.9% |
| ⚫ **Coal** | 10 MW | 80/81 units | 31.1 GW | 31.1 GW | 37.6% |
| 🔥 **Gas** | 10 MW | 24/25 units | 17.3 GW | 17.3 GW | 47.4% |
| 💧 **Hydro Power** | 10 MW | 143/143 units | 24 GW | 24 GW | — |
| 🛢️ **Oil** | 10 MW | 2/2 units | 0.66 GW | 0.66 GW | 33.8% |
| ☀️ **Solar** | 200 MW | 19/1236 units | 5.31 GW | 19.1 GW | — |
| 🌊 **Windoff** | 200 MW | 0/38 units | 0 GW | 2.09 GW | — |
| 💨 **Windon** | 200 MW | 6/128 units | 1.95 GW | 6.63 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 1/1 units | 1.2 GW | 1.2 GW | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 12/19 units | 0.869 GW | 0.195 GW | 31.3% |
| ⚫ **Coal** | 10 MW | 7/7 units | 3.83 GW | — | 40.3% |
| 🔥 **Gas** | 10 MW | 42/42 units | 46 GW | — | 46.3% |
| 🌋 **Geothermal** | 10 MW | 2/2 units | 0.045 GW | — | 100% |
| 💧 **Hydro Power** | 10 MW | 4/4 units | 0.45 GW | — | — |
| ⚛️ **Nuclear** | — | 4/4 units | 4.6 GW | — | — |
| ☀️ **Solar** | 200 MW | 70/347 units | 27.4 GW | 21.5 GW | — |
| 🌊 **Windoff** | 200 MW | 20/57 units | 24.6 GW | 2.75 GW | — |
| 💨 **Windon** | 200 MW | 4/181 units | 0.95 GW | 11.3 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 1/1 units | 1.5 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 28.5 GW | 21 GW after capacity penalty |
| 🔥 **Gas**  | 15.8 GW  | 13.3 GW after capacity penalty |

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
| **Individual Plant Coverage** | 94% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 249 GW from all sources |
| **Plants Above Threshold** | 461 individual plants tracked |
| **Total Plants Processed** | 819 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **hydro**: 5.8 GW
  - **solar**: 1.52 GW
  - **bioenergy**: 0.05 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_VNM.xlsx` — full dataset in a model-agnostic format
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
[VerveStacks Methods documentation](https://kanors-emr.github.io/VerveStacks-docs/).*

---
*Generated by VerveStacks Energy Model Processor*
