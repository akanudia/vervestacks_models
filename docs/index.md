# ITA — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-07-09 13:43:10  |  **ISO Code:** `ITA`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 129 GW | 280 TWh | 91 Mt | 86% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 16/29 plants | 3.39 GW | — | 37.3% |
| ⚫ **Coal** | 150 MW | 16/20 plants | 6.81 GW | — | 42.7% |
| 🔥 **Gas** | 150 MW | 114/180 plants | 59 GW | 0.782 GW | 54% |
| 🌋 **Geothermal** | 40 MW | 11/25 plants | 0.834 GW | — | 100% |
| 💧 **Hydro Power** | 40 MW | 89/89 plants | 15.4 GW | — | 68% |
| 🛢️ **Oil** | 150 MW | 7/15 plants | 2.13 GW | 0.08 GW | 33.9% |
| ☀️ **Solar** | 200 MW | 12/78 plants | 25.7 GW | — | 48.3% |
| 🌊 **Windoff** | 200 MW | 0/1 plants | 0.03 GW | — | 100% |
| 💨 **Windon** | 200 MW | 17/134 plants | 12.3 GW | — | 89% |
| 🔋 **Pumped Storage** | 40 MW | 19/19 plants | 7.56 GW | — | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/2 plants | 0.083 GW | 33.8% |
| 🔥 **Gas** | 150 MW | 10/16 plants | 6.2 GW | 47.9% |
| ☀️ **Solar** | 200 MW | 8/20 plants | 4.08 GW | 100% |
| 🌊 **Windoff** | 200 MW | 49/49 plants | 45.4 GW | 100% |
| 💨 **Windon** | 200 MW | 0/7 plants | 0.738 GW | 100% |
| 🔋 **Pumped Storage** | 40 MW | 1/1 plants | 0.27 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 6.81 GW | 4.78 GW after capacity penalty |
| 🔥 **Gas**  | 60 GW  | 51 GW after capacity penalty |

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
| **Individual Plant Coverage** | 93% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 191 GW from all sources |
| **Plants Above Threshold** | 364 individual plants tracked |
| **Total Plants Processed** | 685 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **windon**: 2.03 GW
  - **bioenergy**: 2.58 GW
  - **hydro**: 7.28 GW
  - **solar**: 19.88 GW
- **EMBER data**:
  - **gas**: 11.48 GW
  - **coal**: 0.41 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_ITA.xlsx` — full dataset in a model-agnostic format
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
