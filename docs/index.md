# TUR — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-28 21:23:44  |  **ISO Code:** `TUR`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 107 GW | 321 TWh | 129 Mt | 82% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 10/80 units | 0.721 GW | 2.01 GW | — | 33.6% |
| ⚫ **Coal** | 60 MW | 77/83 units | 20.2 GW | 20.5 GW | 0.545 GW | 38.4% |
| 🔥 **Gas** | 60 MW | 74/98 units | 25.6 GW | 26.3 GW | 1.44 GW | 56% |
| 🌋 **Geothermal** | 60 MW | 4/77 units | 0.369 GW | 1.92 GW | — | 100% |
| 💧 **Hydro Power** | 60 MW | 116/201 units | 30 GW | 33.1 GW | — | — |
| ⚛️ **Nuclear** | — | 4/4 units | 4.8 GW | 4.8 GW | — | — |
| 🛢️ **Oil** | 60 MW | 4/5 units | 0.536 GW | 0.566 GW | — | 37.9% |
| ☀️ **Solar** | 200 MW | 14/2719 units | 6.69 GW | 23.8 GW | — | — |
| 💨 **Windon** | 200 MW | 2/429 units | 0.411 GW | 15.2 GW | — | — |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/2 units | 0.053 GW | 0.024 GW | 34% |
| ⚫ **Coal** | 60 MW | 2/2 units | 0.688 GW | — | 37.1% |
| 🌋 **Geothermal** | 60 MW | 1/12 units | 0.076 GW | 0.268 GW | 100% |
| 💧 **Hydro Power** | 60 MW | 18/28 units | 3.28 GW | 0.391 GW | — |
| ⚛️ **Nuclear** | — | 8/8 units | 9.9 GW | — | — |
| ☀️ **Solar** | 200 MW | 0/242 units | 0 GW | 4.24 GW | — |
| 💨 **Windon** | 200 MW | 2/34 units | 0.67 GW | 1.4 GW | — |
| 🔋 **Pumped Storage** | 60 MW | 2/2 units | 2.4 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 12.4 GW | 9.1 GW after capacity penalty |
| 🔥 **Gas**  | 20.6 GW  | 17.4 GW after capacity penalty |

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
| **Individual Plant Coverage** | 79% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 154 GW from all sources |
| **Plants Above Threshold** | 409 individual plants tracked |
| **Total Plants Processed** | 1111 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 4.95 GW
  - **hydro**: 5.58 GW
  - **bioenergy**: 0.58 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_TUR.xlsx` — full dataset in a model-agnostic format
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
