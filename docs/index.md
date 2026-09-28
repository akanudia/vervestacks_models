# CHN — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-28 21:40:56  |  **ISO Code:** `CHN`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 2492 GW | 8779 TWh | 5259 Mt | 101% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Total Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|---------------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 89/1670 units | 5.84 GW | 38.3 GW | 0.045 GW | 29.6% |
| ⚫ **Coal** | 1000 MW | 356/3808 units | 359 GW | 1464 GW | 4.27 GW | 40.7% |
| 🔥 **Gas** | 1000 MW | 0/826 units | 0 GW | 211 GW | 0.25 GW | — |
| 🌋 **Geothermal** | 1000 MW | 0/2 units | 0 GW | 0.016 GW | 0.024 GW | — |
| 💧 **Hydro Power** | 1000 MW | 95/1032 units | 329 GW | 464 GW | 0.024 GW | — |
| ⚛️ **Nuclear** | — | 91/91 units | 99 GW | 99 GW | — | — |
| ☀️ **Solar** | 500 MW | 513/15068 units | 652 GW | 1263 GW | 0.1 GW | — |
| 🌊 **Windoff** | 200 MW | 179/254 units | 69 GW | 75 GW | — | — |
| 💨 **Windon** | 360 MW | 325/7151 units | 226 GW | 740 GW | 0.41 GW | — |
| 🔋 **Pumped Storage** | 1000 MW | 160/183 units | 227 GW | 237 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Units Above / Total** | **Capacity Above Threshold** | **Aggregated (below)** | **Wtd Avg Efficiency** |
|---------------|---------------|-------------------------|------------------------------|------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 11/104 units | 0.85 GW | 2.43 GW | 32.9% |
| ⚫ **Coal** | 1000 MW | 166/471 units | 167 GW | 128 GW | 43.7% |
| 🔥 **Gas** | 1000 MW | 1/313 units | 1.6 GW | 121 GW | 33% |
| 🌋 **Geothermal** | 1000 MW | 0/3 units | 0 GW | 0.056 GW | — |
| 💧 **Hydro Power** | 1000 MW | 18/50 units | 43.5 GW | 9.66 GW | — |
| ⚛️ **Nuclear** | — | 76/76 units | 86 GW | — | — |
| ☀️ **Solar** | 500 MW | 239/2615 units | 289 GW | 277 GW | — |
| 🌊 **Windoff** | 200 MW | 80/87 units | 50 GW | 0.748 GW | — |
| 💨 **Windon** | 360 MW | 226/2951 units | 221 GW | 259 GW | — |
| 🔋 **Pumped Storage** | 1000 MW | 193/224 units | 270 GW | 14.2 GW | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 1254 GW | 921 GW after capacity penalty |
| 🔥 **Gas**  | 105 GW  | 88 GW after capacity penalty |

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
| **Plants Above Threshold** | 7857 individual plants tracked |
| **Total Plants Processed** | 10362 plants in database |
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
