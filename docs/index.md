# DEU — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-10-01 17:43:28  |  **ISO Code:** `DEU`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 226 GW | 567 TWh | 228 Mt | 96% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 33/106 units | 8.36 GW | 10.1 GW | — | 32.2% |
| ⚫ **Coal** | 110 MW | 74/98 units | 34.6 GW | 36.1 GW | 3.65 GW | 35.5% |
| 🔥 **Gas** | 110 MW | 83/291 units | 24 GW | 34.3 GW | 2.1 GW | 45.1% |
| 🌋 **Geothermal** | 10 MW | 0/12 units | 0 GW | 0.06 GW | — | — |
| 💧 **Hydro Power** | 10 MW | 45/45 units | 5.14 GW | 5.14 GW | — | — |
| ⚛️ **Nuclear** | — | 3/3 units | 4.29 GW | 4.29 GW | — | — |
| 🛢️ **Oil** | 110 MW | 7/23 units | 1.45 GW | 2.19 GW | — | 33.4% |
| ☀️ **Solar** | 200 MW | 61/7956 units | 54 GW | 98 GW | 0.005 GW | — |
| 🌊 **Windoff** | 200 MW | 30/42 units | 10.4 GW | 11.1 GW | — | — |
| 💨 **Windon** | 200 MW | 24/2278 units | 21.2 GW | 66 GW | — | — |
| 🔋 **Pumped Storage** | 10 MW | 22/22 units | 6.19 GW | 6.19 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/2 units | 0.05 GW | 0.038 GW | 33% |
| 🔥 **Gas** | 110 MW | 21/27 units | 13.2 GW | 0.263 GW | 57% |
| 🌋 **Geothermal** | 10 MW | 1/1 units | 0.012 GW | — | 100% |
| 💧 **Hydro Power** | 10 MW | 1/1 units | 0.2 GW | — | — |
| ☀️ **Solar** | 200 MW | 2/743 units | 1.3 GW | 8.01 GW | — |
| 🌊 **Windoff** | 200 MW | 9/9 units | 5 GW | — | — |
| 💨 **Windon** | 200 MW | 0/388 units | 0 GW | 11.1 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 5/5 units | 1.56 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 35.4 GW | 27.2 GW after capacity penalty |
| 🔥 **Gas**  | 14.9 GW  | 12.6 GW after capacity penalty |

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
| **Individual Plant Coverage** | 72% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 319 GW from all sources |
| **Plants Above Threshold** | 740 individual plants tracked |
| **Total Plants Processed** | 2356 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 53.57 GW
  - **windon**: 21.23 GW
  - **hydro**: 3.9 GW
  - **bioenergy**: 7.78 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_DEU.xlsx` — full dataset in a model-agnostic format
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
