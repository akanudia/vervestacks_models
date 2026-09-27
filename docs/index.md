# CHN — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-27 11:02:32  |  **ISO Code:** `CHN`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 2492 GW | 8779 TWh | 5258 Mt | 101% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 289/892 plants | 38.3 GW | 0.045 GW | 28.8% |
| ⚫ **Coal** | 1000 MW | 721/2061 plants | 1464 GW | 4.27 GW | 37.3% |
| 🔥 **Gas** | 1000 MW | 55/407 plants | 211 GW | 0.25 GW | 52% |
| 🌋 **Geothermal** | 1000 MW | 0/2 plants | 0.016 GW | 0.024 GW | 100% |
| 💧 **Hydro Power** | 1000 MW | 106/721 plants | 464 GW | 0.024 GW | — |
| ⚛️ **Nuclear** | — | 91/91 plants | 99 GW | — | — |
| ☀️ **Solar** | 500 MW | 859/2035 plants | 1263 GW | 0.1 GW | — |
| 🌊 **Windoff** | 200 MW | 185/246 plants | 75 GW | — | — |
| 💨 **Windon** | 360 MW | 755/2008 plants | 740 GW | 0.41 GW | — |
| 🔋 **Pumped Storage** | 1000 MW | 160/183 plants | 237 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 27/68 plants | 3.28 GW | 32.2% |
| ⚫ **Coal** | 1000 MW | 219/301 plants | 294 GW | 43.3% |
| 🔥 **Gas** | 1000 MW | 43/90 plants | 123 GW | 55% |
| 🌋 **Geothermal** | 1000 MW | 0/2 plants | 0.056 GW | 100% |
| 💧 **Hydro Power** | 1000 MW | 20/36 plants | 53 GW | — |
| ⚛️ **Nuclear** | — | 76/76 plants | 86 GW | — |
| ☀️ **Solar** | 500 MW | 350/480 plants | 565 GW | — |
| 🌊 **Windoff** | 200 MW | 80/87 plants | 51 GW | — |
| 💨 **Windon** | 360 MW | 357/452 plants | 480 GW | — |
| 🔋 **Pumped Storage** | 1000 MW | 196/215 plants | 284 GW | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 359 GW | 296 GW after capacity penalty |
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
| **Individual Plant Coverage** | 81% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 6537 GW from all sources |
| **Plants Above Threshold** | 7830 individual plants tracked |
| **Total Plants Processed** | 10453 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 384.08 GW
  - **windon**: 27.98 GW
  - **hydro**: 66.78 GW
  - **windoff**: 1.49 GW |

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
