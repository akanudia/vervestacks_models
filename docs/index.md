# AUS — VerveStacks Model

!!! info "Model Info"
    **Generated:** 2026-09-07 22:50:59  |  **ISO Code:** `AUS`

---

## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 101 GW | 273 TWh | 159 Mt | 101% |

> **Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA.
> UNSD has incomplete data for fuel consumption, so calibration is demonstrated against total CO₂ emissions
> reported by EMBER — confirming that efficiency assumptions are sound.

---

## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 6/34 plants | 1.03 GW | — | 30.6% |
| ⚫ **Coal** | 100 MW | 56/58 plants | 25.1 GW | — | 35.3% |
| 🔥 **Gas** | 100 MW | 117/145 plants | 26.9 GW | — | 36.6% |
| 💧 **Hydro Power** | 10 MW | 61/61 plants | 6.23 GW | 0.034 GW | — |
| 🛢️ **Oil** | 100 MW | 4/9 plants | 0.776 GW | — | 28.4% |
| ☀️ **Solar** | 200 MW | 35/229 plants | 40.8 GW | — | — |
| 💨 **Windon** | 200 MW | 36/122 plants | 17.6 GW | 1.01 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 6/6 plants | 4.86 GW | — | 80% (assumed round-trip) |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 2/5 plants | 0.28 GW | 32.8% |
| ⚫ **Coal** | 100 MW | 3/3 plants | 0.945 GW | 35.5% |
| 🔥 **Gas** | 100 MW | 19/22 plants | 5.74 GW | 35.1% |
| 💧 **Hydro Power** | 10 MW | 1/1 plants | 0.19 GW | — |
| ☀️ **Solar** | 200 MW | 118/179 plants | 120 GW | — |
| 🌊 **Windoff** | 200 MW | 31/31 plants | 63 GW | — |
| 💨 **Windon** | 200 MW | 159/189 plants | 185 GW | — |
| 🔋 **Pumped Storage** | 10 MW | 19/19 plants | 18 GW | 80% (assumed round-trip) |


Announced and pre-construction projects are offered as options to the model for endogenous investment.
This is particularly useful for hydro and pumped storage where country-wise potential is not readily
available. Grid locations of all these units are preserved.

### CCS Retrofit Potential

| Fuel | Retrofit Host Capacity | Retrofit Potential |
|------|------------------------|-------------------|
| ⚫ **Coal** | 25.1 GW | 18.1 GW after capacity penalty |
| 🔥 **Gas**  | 26.9 GW  | 22.8 GW after capacity penalty |

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
| **Individual Plant Coverage** | 95% of total capacity from plant-level GEM data |
| **Total Capacity Tracked** | 518 GW from all sources |
| **Plants Above Threshold** | 741 individual plants tracked |
| **Total Plants Processed** | 1113 plants in database |
| **Missing Capacity Added** | - **IRENA data**:
  - **solar**: 23.29 GW
  - **windon**: 1.62 GW
  - **hydro**: 0.64 GW
  - **bioenergy**: 0.23 GW
- **EMBER data**:
  - **gas**: 5.98 GW |

---

## Model Files

- **Source Data:** `source_data/VerveStacks_AUS.xlsx` — full dataset in a model-agnostic format
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
