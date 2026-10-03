# POL — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-10-03 14:33:33  |  **ISO Code:** `POL`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 56 GW | 174 TWh | 131 Mt | 100% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 12/23 units | 0.96 GW | 1.3 GW | 28.5% |
| ⚫ **Coal** | 10 MW | 144/144 units | 29.2 GW | 29.2 GW | 33.9% |
| 🔥 **Gas** | 10 MW | 38/39 units | 8.95 GW | 8.96 GW | 58% |
| 💧 **Hydro Power** | 10 MW | 9/10 units | 0.532 GW | 0.535 GW | — |
| ☀️ **Solar** | 200 MW | 13/4894 units | 4.2 GW | 20.7 GW | — |
| 🌊 **Windoff** | 200 MW | 1/1 units | 1.2 GW | 1.2 GW | — |
| 💨 **Windon** | 200 MW | 0/365 units | 0 GW | 10.7 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 6/6 units | 1.88 GW | 1.88 GW | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/1 units | 0.05 GW | — | 33% |
| 🔥 **Gas** | 10 MW | 13/13 units | 5.8 GW | — | 46.8% |
| 💧 **Hydro Power** | 10 MW | 1/1 units | 0.08 GW | — | — |
| ⚛️ **Nuclear** | — | 49/49 units | 15.6 GW | — | — |
| ☀️ **Solar** | 200 MW | 2/20 units | 0.77 GW | 1.18 GW | — |
| 🌊 **Windoff** | 200 MW | 19/19 units | 18.2 GW | — | — |
| 💨 **Windon** | 200 MW | 1/8 units | 0.48 GW | 0.55 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 2/2 units | 1.45 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 13.2 GW | 9.54 GW after capacity penalty |
| 🔥 **Gas**  | 6.77 GW  | 5.72 GW after capacity penalty |

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
| **Individual Plant Coverage** | 80% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 119 GW from all sources |
| **Plants Above Threshold** | 284 individual plants tracked |
| **Total Plants Processed** | 823 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 3.8 GW
  - **hydro**: 0.31 GW
  - **bioenergy**: 0.26 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_POL.xlsx` — full dataset in a model-agnostic format
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
