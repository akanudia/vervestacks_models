# JPN — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-30 11:06:12  |  **ISO Code:** `JPN`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 332 GW | 1041 TWh | 568 Mt | 105% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 69/120 units | 5.4 GW | 7.01 GW | 0.159 GW | 28.8% |
| ⚫ **Coal** | 490 MW | 58/159 units | 42.2 GW | 54 GW | 1.58 GW | 36.9% |
| 🔥 **Gas** | 490 MW | 65/251 units | 43.8 GW | 91 GW | — | 44.6% |
| 🌋 **Geothermal** | 60 MW | 1/35 units | 0.065 GW | 0.699 GW | — | 100% |
| 💧 **Hydro Power** | 60 MW | 86/203 units | 20.5 GW | 25.2 GW | — | — |
| ⚛️ **Nuclear** | — | 36/36 units | 19.8 GW | 19.8 GW | 17.4 GW | — |
| 🛢️ **Oil** | 490 MW | 23/47 units | 14.5 GW | 20.1 GW | 1.15 GW | 29.3% |
| ☀️ **Solar** | 200 MW | 34/10769 units | 53 GW | 91 GW | 0.035 GW | — |
| 🌊 **Windoff** | 200 MW | 2/19 units | 1.22 GW | 1.72 GW | — | — |
| 💨 **Windon** | 200 MW | 1/231 units | 0.221 GW | 6.2 GW | — | — |
| 🔋 **Pumped Storage** | 60 MW | 35/36 units | 25 GW | 25 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 13/16 units | 0.995 GW | 0.127 GW | 33.4% |
| ⚫ **Coal** | 490 MW | 1/1 units | 0.5 GW | — | 44.4% |
| 🔥 **Gas** | 490 MW | 24/28 units | 15.3 GW | 0.789 GW | 57% |
| 🌋 **Geothermal** | 60 MW | 0/1 units | 0 GW | 0.015 GW | — |
| ☀️ **Solar** | 200 MW | 0/9 units | 0 GW | 0.668 GW | — |
| 🌊 **Windoff** | 200 MW | 41/49 units | 35.3 GW | 0.549 GW | — |
| 💨 **Windon** | 200 MW | 4/39 units | 1.94 GW | 2.69 GW | — |
| 🔋 **Pumped Storage** | 60 MW | 2/2 units | 2.28 GW | — | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 44.3 GW | 35.1 GW after capacity penalty |
| 🔥 **Gas**  | 55 GW  | 46.8 GW after capacity penalty |

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
| **Individual Plant Coverage** | 83% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 424 GW from all sources |
| **Plants Above Threshold** | 723 individual plants tracked |
| **Total Plants Processed** | 1532 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 52.49 GW
  - **hydro**: 9.43 GW
  - **windon**: 0.22 GW
  - **bioenergy**: 1.7 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_JPN.xlsx` — full dataset in a model-agnostic format
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
