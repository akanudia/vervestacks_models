# DEU — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-07-09 13:26:31  |  **ISO Code:** `DEU`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 227 GW | 566 TWh | 238 Mt | 100% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 25/87 plants | 9.94 GW | — | 31.4% |
| ⚫ **Coal** | 110 MW | 78/108 plants | 37.3 GW | 3.12 GW | 35.2% |
| 🔥 **Gas** | 110 MW | 96/246 plants | 34 GW | 2.1 GW | 42.8% |
| 🌋 **Geothermal** | 10 MW | 2/7 plants | 0.06 GW | — | 100% |
| 💧 **Hydro Power** | 10 MW | 22/22 plants | 4.98 GW | — | 46% |
| ⚛️ **Nuclear** | — | 3/3 plants | 4.29 GW | — | 100% |
| 🛢️ **Oil** | 110 MW | 6/18 plants | 1.89 GW | — | 32.7% |
| ☀️ **Solar** | 200 MW | 43/403 plants | 73 GW | 0.002 GW | 61% |
| 🌊 **Windoff** | 200 MW | 29/38 plants | 10.1 GW | — | 99% |
| 💨 **Windon** | 200 MW | 61/349 plants | 62 GW | — | 76% |
| 🔋 **Pumped Storage** | 10 MW | 21/21 plants | 6.15 GW | — | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/2 plants | 0.088 GW | 33% |
| 🔥 **Gas** | 110 MW | 13/19 plants | 9.32 GW | 54% |
| 🌋 **Geothermal** | 10 MW | 1/1 plants | 0.012 GW | 100% |
| 💧 **Hydro Power** | 10 MW | 1/1 plants | 0.2 GW | 100% |
| ☀️ **Solar** | 200 MW | 17/61 plants | 9.46 GW | 100% |
| 🌊 **Windoff** | 200 MW | 10/11 plants | 7.74 GW | 100% |
| 💨 **Windon** | 200 MW | 8/55 plants | 5.07 GW | 100% |
| 🔋 **Pumped Storage** | 10 MW | 5/5 plants | 1.57 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 40.4 GW | 30 GW after capacity penalty |
| 🔥 **Gas**  | 36 GW  | 30.4 GW after capacity penalty |

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
| **Total Capacity Tracked** | 282 GW from all sources |
| **Plants Above Threshold** | 586 individual plants tracked |
| **Total Plants Processed** | 1457 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 41.99 GW
  - **windon**: 21.94 GW
  - **hydro**: 4.02 GW
  - **bioenergy**: 7.7 GW
  - **geothermal**: 0.03 GW
- **EMBER data**:
  - **coal**: 0.46 GW |

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
