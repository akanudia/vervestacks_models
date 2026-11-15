# ZAF — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-11-15 19:28:06  |  **ISO Code:** `ZAF`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 66 GW | 239 TWh | 211 Mt | 121% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/31 units | 0.117 GW | 0.361 GW | — | 27.9% |
| ⚫ **Coal** | 10 MW | 125/125 units | 46.2 GW | 46.2 GW | 2.47 GW | 34% |
| 🔥 **Gas** | 10 MW | 6/7 units | 1.28 GW | 1.29 GW | — | 33% |
| 💧 **Hydro Power** | 10 MW | 3/3 units | 0.642 GW | 0.642 GW | — | — |
| ⚛️ **Nuclear** | — | 2/2 units | 1.94 GW | 1.94 GW | — | — |
| 🛢️ **Oil** | 10 MW | 20/20 units | 2.42 GW | 2.42 GW | — | 32.4% |
| ☀️ **Solar** | 200 MW | 8/349 units | 3.59 GW | 12.2 GW | — | — |
| 💨 **Windon** | 200 MW | 1/75 units | 0.23 GW | 6.54 GW | — | — |
| 🔋 **Pumped Storage** | 10 MW | 4/4 units | 2.89 GW | 2.89 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 0/2 units | 0 GW | 0.062 GW | — |
| ⚫ **Coal** | 10 MW | 2/2 units | 1.46 GW | — | 32.2% |
| 🔥 **Gas** | 10 MW | 7/7 units | 9.6 GW | — | 52% |
| 🛢️ **Oil** | 10 MW | 1/1 units | 0.45 GW | — | 28.8% |
| ☀️ **Solar** | 200 MW | 41/99 units | 26 GW | 5.99 GW | — |
| 🌊 **Windoff** | 200 MW | 1/1 units | 0.81 GW | — | — |
| 💨 **Windon** | 200 MW | 4/21 units | 1.72 GW | 2.06 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 1/1 units | 1.5 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 41.7 GW | 32.2 GW after capacity penalty |
| 🔥 **Gas**  | 0 GW  | 0 GW after capacity penalty |

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
| **Individual Plant Coverage** | 88% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 127 GW from all sources |
| **Plants Above Threshold** | 280 individual plants tracked |
| **Total Plants Processed** | 580 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 2.76 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_ZAF.xlsx` — full dataset in a model-agnostic format
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
