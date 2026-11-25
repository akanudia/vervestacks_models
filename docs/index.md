# GBR — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-11-25 23:30:52  |  **ISO Code:** `GBR`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 108 GW | 325 TWh | 73 Mt | 88% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 30/125 units | 6.3 GW | 8.71 GW | 0.025 GW | 25.2% |
| ⚫ **Coal** | 50 MW | 12/12 units | 6.33 GW | 6.33 GW | — | 27% |
| 🔥 **Gas** | 50 MW | 106/158 units | 36.8 GW | 38.1 GW | 1.99 GW | 42.6% |
| 🌋 **Geothermal** | 10 MW | 0/1 units | 0 GW | 0.002 GW | — | — |
| 💧 **Hydro Power** | 10 MW | 23/23 units | 1.63 GW | 1.63 GW | — | — |
| ⚛️ **Nuclear** | — | 14/14 units | 11.9 GW | 11.9 GW | — | — |
| 🛢️ **Oil** | 50 MW | 7/12 units | 0.467 GW | 0.599 GW | — | 22% |
| ☀️ **Solar** | 200 MW | 11/1482 units | 5.52 GW | 21.1 GW | — | — |
| 🌊 **Windoff** | 200 MW | 30/97 units | 20.6 GW | 25 GW | — | — |
| 💨 **Windon** | 200 MW | 9/857 units | 2.58 GW | 18.1 GW | — | — |
| 🔋 **Pumped Storage** | 10 MW | 4/4 units | 3.16 GW | 3.16 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 4/12 units | 0.245 GW | 0.272 GW | 33.4% |
| 🔥 **Gas** | 50 MW | 19/27 units | 13.7 GW | 0.242 GW | 56% |
| 🌋 **Geothermal** | 10 MW | 0/1 units | 0 GW | 0.005 GW | — |
| ⚛️ **Nuclear** | — | 12/12 units | 5.42 GW | — | — |
| 🛢️ **Oil** | 50 MW | 11/11 units | 1.65 GW | — | 36.6% |
| ☀️ **Solar** | 200 MW | 17/1158 units | 8.93 GW | 22.9 GW | — |
| 🌊 **Windoff** | 200 MW | 45/59 units | 62 GW | 1.03 GW | — |
| 💨 **Windon** | 200 MW | 10/382 units | 3.03 GW | 14 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 12/12 units | 11.6 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 5.76 GW | 4.29 GW after capacity penalty |
| 🔥 **Gas**  | 28.9 GW  | 24.4 GW after capacity penalty |

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
| **Individual Plant Coverage** | 90% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 282 GW from all sources |
| **Plants Above Threshold** | 446 individual plants tracked |
| **Total Plants Processed** | 1180 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 5.14 GW
  - **bioenergy**: 2.27 GW
  - **hydro**: 0.61 GW
  - **windon**: 0.33 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_GBR.xlsx` — full dataset in a model-agnostic format
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
