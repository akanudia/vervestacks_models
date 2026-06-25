# GBR — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-06-25 19:52:39  |  **ISO Code:** `GBR`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 108 GW | 322 TWh | 72 Mt | 89% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 25/147 plants | 8.43 GW | 0.025 GW | 24.9% |
| ⚫ **Coal** | 50 MW | 12/12 plants | 6.33 GW | — | 27% |
| 🔥 **Gas** | 50 MW | 104/144 plants | 36.7 GW | 1.99 GW | 42.5% |
| 🌋 **Geothermal** | 10 MW | 0/1 plants | 0.002 GW | — | 100% |
| 💧 **Hydro Power** | 10 MW | 21/21 plants | 3.97 GW | — | 84% |
| ⚛️ **Nuclear** | — | 14/14 plants | 11.9 GW | — | 100% |
| 🛢️ **Oil** | 50 MW | 8/9 plants | 0.599 GW | — | 20.9% |
| ☀️ **Solar** | 200 MW | 21/133 plants | 17.6 GW | — | 79% |
| 🌊 **Windoff** | 200 MW | 35/56 plants | 22.7 GW | — | 97% |
| 💨 **Windon** | 200 MW | 25/283 plants | 17 GW | — | 96% |
| 🔋 **Pumped Storage** | 10 MW | 2/2 plants | 0.824 GW | — | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 4/12 plants | 0.517 GW | 33.1% |
| 🔥 **Gas** | 50 MW | 31/38 plants | 19 GW | 55% |
| 🌋 **Geothermal** | 10 MW | 0/1 plants | 0.005 GW | 100% |
| ⚛️ **Nuclear** | — | 12/12 plants | 5.42 GW | 100% |
| ☀️ **Solar** | 200 MW | 26/39 plants | 25 GW | 100% |
| 🌊 **Windoff** | 200 MW | 60/69 plants | 76 GW | 100% |
| 💨 **Windon** | 200 MW | 26/35 plants | 18.8 GW | 100% |
| 🔋 **Pumped Storage** | 10 MW | 12/12 plants | 10.8 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 6.33 GW | 4.6 GW after capacity penalty |
| 🔥 **Gas**  | 38.7 GW  | 32.7 GW after capacity penalty |

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
| **Total Capacity Tracked** | 284 GW from all sources |
| **Plants Above Threshold** | 422 individual plants tracked |
| **Total Plants Processed** | 1040 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **windon**: 0.99 GW
  - **windoff**: 1.02 GW
  - **hydro**: 0.93 GW
  - **solar**: 5.53 GW
  - **bioenergy**: 1.45 GW |

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
[VerveStacks Methods documentation](https://vervestacks.readthedocs.io/en/latest/).*

---
*Generated by VerveStacks Energy Model Processor*
