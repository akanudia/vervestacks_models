# VerveStacks Model Generation Notes - USA
**Generated:** 2025-12-12 16:07:32


## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 1264 GW | 4287 TWh | 1730 Mt | 105% |

**Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA. UNSD has incomplete data for fuel consumption, so the calibration is demonstrated against the total CO2 emission reported by EMBER. This shows that the efficiency assumptions are good.


## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Mothballed Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|--------------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 80/100 plants | 11.1 GW | — | 29.4% |
| ⚫ **Coal** | 860 MW | 98/132 plants | 224 GW | — | 34.4% |
| 🔥 **Gas** | 860 MW | 189/305 plants | 558 GW | 7.92 GW | 44.7% |
| 🌋 **Geothermal** | 190 MW | 7/39 plants | 3.93 GW | 0.055 GW | 100% |
| 💧 **Hydro Power** | 190 MW | 111/184 plants | 83 GW | — | 91% |
| ⚛️ **Nuclear** | — | 95/95 plants | 103 GW | — | 100% |
| 🛢️ **Oil** | 860 MW | 6/70 plants | 22.5 GW | 1.07 GW | 29.2% |
| ☀️ **Solar** | 200 MW | 292/1219 plants | 185 GW | 0.045 GW | 85% |
| 🌊 **Windoff** | 200 MW | 4/7 plants | 5.2 GW | — | 100% |
| 💨 **Windon** | 260 MW | 263/690 plants | 166 GW | 0.034 GW | 100% |
| 🔋 **Pumped Storage** | 190 MW | 26/27 plants | 20 GW | — | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| ⚫ **Coal** | 860 MW | 0/2 plants | 0.8 GW | 40.5% |
| 🔥 **Gas** | 860 MW | 36/59 plants | 71 GW | 44.6% |
| 🌋 **Geothermal** | 190 MW | 5/10 plants | 4.09 GW | 100% |
| 💧 **Hydro Power** | 190 MW | 0/2 plants | 0.149 GW | 100% |
| ⚛️ **Nuclear** | — | 30/30 plants | 7.36 GW | 100% |
| ☀️ **Solar** | 200 MW | 226/387 plants | 94 GW | 100% |
| 🌊 **Windoff** | 200 MW | 39/44 plants | 49.1 GW | 100% |
| 💨 **Windon** | 260 MW | 67/109 plants | 35.7 GW | 100% |
| 🔋 **Pumped Storage** | 190 MW | 92/94 plants | 84 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment. This is particularly useful for hydro and pumped storage as country-wise potential is not readily available. We also get grid locations of all these units.

### 🔄 CCS Retrofit Potential
| **Fuel Type** | **Retrofit Host Capacity** | **Retrofit Potential Capacity**
|---------------|----------------------------|-------------------------------|
| ⚫ **Coal** | 224 GW | 137 GW after capacity penalty |
| 🔥 **Gas** | 566 GW | 478 GW after capacity penalty |


## Data, Assumptions & Coverage

### Primary Data Sources

#### Base-Year Power Plant Specifications
- **Global Energy Monitor (GEM)** [🌐](https://globalenergymonitor.org)  
  Open-access database of individual power plants worldwide, including location, capacity, fuel type, commissioning year, and technical specifications.
- **International Renewable Energy Agency (IRENA)** [🌐](https://www.irena.org/Statistics)  
  Global renewable energy capacity and generation statistics (2000–2022), disaggregated by country and technology.
- **EMBER Climate** [🌐](https://ember-climate.org/data/)  
  Global dataset tracking electricity generation, installed capacity, and emissions intensity (2000–2022).

#### Enhanced Renewable Energy Characterization
- **GEM-REZoning-Atlite Integration** [`re_units_cf_grid_cell_mapping.csv`]  
  Enhanced renewable energy units with capacity factors from Atlite weather data and precise grid cell locations from REZoning database. This integration provides spatially-resolved capacity factors for existing renewable plants, enabling accurate performance modeling and grid cell assignment for spatial optimization.
- **Capacity Factor Enhancement**: Individual renewable plants receive location-specific capacity factors derived from 2013 hourly weather patterns
- **Spatial Grid Assignment**: Plants mapped to 50x50km REZoning grid cells for consistent spatial modeling

### Data Processing Notes
- **Individual Plant Coverage**: 98%% of total capacity from plant-level GEM data
- **Total Capacity Tracked**: 1739 GW GW from all sources
- **Plants Above Threshold**: 2292 individual plants tracked
- **Total Plants Processed**: 3605 plants in database
- **Missing Capacity Added**: - **IRENA data**:
  - **solar**: 40.34 GW
  - **bioenergy**: 3.76 GW
  - **hydro**: 11.36 GW


## Model Structure

### Files Included
- **Source Data**: `source_data/VerveStacks_USA.xlsx` - the full dataset in a model-agnostic format
- **VEDA Model Files**: Complete model ready for Veda-TIMES execution
- **Scenario Files**: NGFS climate scenarios and policy assumptions


## Renewable Energy Characterization

VerveStacks provides comprehensive renewable energy potential analysis at unprecedented spatial resolution, 
combining global resource assessments with realistic deployment constraints to deliver actionable insights 
for energy system planning.

### **Data Foundation: REZoning Integration**

Our renewable energy characterization builds on the REZoning database, providing detailed potential 
assessments at 50×50 km grid resolution across 190+ countries. This high-resolution spatial data 
captures the nuanced variations in renewable energy resources that are critical for accurate energy 
system modeling.

**Data Sources:**
- **Solar Potential**: REZoning solar resource data with capacity factors and LCOE estimates
- **Wind Onshore**: REZoning onshore wind potential with economic viability assessments  
- **Wind Offshore**: REZoning offshore wind resources with marine-specific constraints
- **Hourly Profiles**: Atlite-derived capacity factor time series for each grid cell

### **Land Use Conflict Resolution: Conservative Overlap Management**

A critical challenge in renewable energy assessment is avoiding double-counting of land areas suitable 
for both solar and wind development. VerveStacks implements a **conservative overlap resolution algorithm** 
that ensures realistic deployment scenarios:

**Most Pessimistic Assumption:**
- When grid cells overlap between solar and wind potential, we apply **LCOE-based allocation**
- The technology with **higher LCOE (less competitive)** receives a **reduced share** of the overlapping area
- This conservative approach ensures our estimates represent **deployable potential** rather than theoretical maximums
- **No double-counting**: Each grid cell contributes to less than the REZoning resource limits in cells with overlap

This methodology reflects real-world deployment patterns where developers choose the most economically 
viable technology for each location, ensuring our supply curves represent **realistic, achievable 
renewable energy potential**.

### **Supply Curve Visualization**

The resulting supply curves reveal the economic characteristics of renewable energy deployment, 
showing how costs evolve as more capacity is developed:

**Chart Features:**
- **LCOE vs Cumulative Capacity**: Economic viability as deployment scales
- **LCOE vs Cumulative Generation**: Resource potential in energy terms
- **Technology Comparison**: Solar, Wind Onshore, and Wind Offshore potential
- **Original vs Landuse-Adjusted**: Impact of conservative overlap management

<div align="center">
<img src="VerveStacks_USA/renewable_energy/supply_curves_USA.svg" alt="Renewable Energy Supply Curves" width="100%">
</div>

This analysis provides the foundation for understanding renewable energy economics and informs 
capacity expansion decisions in the VEDA/TIMES energy system models.


### Renewable Energy Clustering

VerveStacks employs **intelligent spatial clustering** to transform high-resolution renewable energy 
grid cells into manageable clusters while preserving essential resource characteristics and geographic diversity.

#### **Clustering Overview**

| **Clustering Metric** | **Value** | **Description** |
|----------------------|-----------|-----------------|
| **Grid Cells Processed** | 3772 | 50×50km renewable energy grid cells |
| **Clusters Generated** | 139 | Dynamically determined using n = cells^0.6 |
| **Average Cluster Size** | 27.1 grid cells | Mean grid cells per cluster |
| **Cluster Size Range** | 7 to 102 grid cells | Variation in cluster composition |
| **Grid Definition** | Cities as transmission bus proxies | Transmission infrastructure basis |

#### **Multi-Feature Clustering Algorithm**

The clustering process combines multiple data dimensions to create economically and spatially coherent renewable energy zones:
        
**Technical Implementation:**
- **Algorithm**: Hierarchical clustering with Ward linkage
- **Preprocessing**: PCA dimensionality reduction (50 components per technology)
- **Standardization**: All features normalized before clustering
- **Distance Metric**: Euclidean distance in transformed feature space

#### **Capacity-Weighted Profile Aggregation**

Each cluster receives a **capacity-weighted hourly profile** that preserves the temporal characteristics 
of constituent grid cells while accounting for their relative renewable energy potential:

```
cluster_profile[hour] = Σ(grid_cell_profile[hour] × capacity_weight[cell]) / Σ(capacity_weight[cell])
```

This approach ensures that grid cells with higher renewable energy potential have proportionally 
greater influence on the cluster's temporal generation pattern, maintaining economic rationality 
in the aggregated profiles.

#### **Geographic Hedging Benefits**

**Why Clustering Matters**: Even in non-grid models, renewable energy clustering preserves critical 
**geographic hedging** effects that are essential for realistic energy system modeling:

- **Wind Resource Diversity**: Captures spatial variations in wind patterns and seasonal differences
- **Solar Complementarity**: Preserves east-west and north-south solar resource variations
- **Grid Connection Costs**: Maintains distance-based connection costs to transmission infrastructure
- **Temporal Smoothing**: Geographic diversity reduces overall system variability

**Universal Application**: Both grid and non-grid models use identical clustering methodology, 
differing only in their synthetic grid definition (actual transmission vs. population centers).

#### **Quality Filtering**

Only economically viable renewable resources are included in the clustering process:
- **Solar PV**: Grid cells with <5% capacity factor excluded
- **Onshore Wind**: Grid cells with <8% capacity factor excluded
- **Resource Focus**: Ensures clustering represents deployable potential, not theoretical maximums

#### **Clustering Visualizations**

The following visualizations show the spatial distribution of renewable energy clusters for each technology, 
demonstrating how the algorithm balances resource quality, geographic diversity, and grid connectivity:

**Solar PV Clustering:**
<div align="center">
  <img src="VerveStacks_USA/source_data/clustering_results_USA_solar.png" 
       alt="Solar PV Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Solar PV clustering showing 139 clusters from 3772 grid cells using Cities as transmission bus proxies</em></p>
</div>

**Onshore Wind Clustering:**
<div align="center">
  <img src="VerveStacks_USA/source_data/clustering_results_USA_wind_onshore.png" 
       alt="Onshore Wind Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Onshore wind clustering showing 139 clusters from 3772 grid cells using Cities as transmission bus proxies</em></p>
</div>

**Offshore Wind Clustering:**
<div align="center">
  <img src="VerveStacks_USA/source_data/clustering_results_USA_wind_offshore.png" 
       alt="Offshore Wind Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Offshore wind clustering showing 139 clusters from 3772 grid cells using Cities as transmission bus proxies</em></p>
</div>

**Visualization Features:**
- **Technology-specific clustering**: Each renewable technology clustered independently
- **Color-coded clusters**: Each cluster shown in distinct colors
- **Grid cell boundaries**: 50×50km renewable energy zones
- **Transmission infrastructure**: Cities as transmission bus proxies overlaid for context
- **Resource quality**: Cluster composition reflects capacity factor variations


## 💧 Hydro Availability Scenarios

### Planning for Hydro Uncertainty

Hydroelectric generation is inherently variable due to seasonal patterns, year-to-year climate variations, and long-term climate change. Traditional energy models often assume constant hydro availability based on historical averages, which can lead to significant underestimation of backup capacity needs and inadequate drought preparedness.

**VerveStacks addresses this critical gap** by generating probabilistic hydro availability scenarios that capture:
- **Natural variability**: Seasonal wet/dry cycles and multi-year persistence
- **Climate change impacts**: Declining mean availability and increasing extremes  
- **Extreme events**: Drought sequences that stress energy systems
- **Country-specific patterns**: Drought thresholds based on historical operational experience

### **Methodology Overview**

Our approach combines **24 years of historical data** (2000-2023) from EMBER Climate with advanced scenario generation to create realistic future pathways:

1. **Historical Analysis**: Extract seasonal patterns, drought frequencies, and country-specific thresholds
2. **Regime Classification**: Model persistence of wet, normal, and dry conditions  
3. **Climate Adjustment**: Apply declining trends and increasing variability
4. **Scenario Generation**: Create 100+ plausible futures preserving historical characteristics

**Key Innovation**: Drought thresholds are derived from each country's bottom 20% of historical capacity factors, ensuring definitions reflect actual operational stress rather than arbitrary percentages.

### **USA Hydro Profile**

| **Planning Parameter** | **Value** | **Application** |
|----------------------|-----------|-----------------|
| **Hydro Dependency** | N/A% of generation | System vulnerability assessment |
| **P10 (Dry Scenario)** | 34.5% annual average | Security planning, reserve sizing |
| **P50 (Base Scenario)** | 36.6% annual average | Expected case, financial planning |
| **P90 (Wet Scenario)** | 39.0% annual average | Export opportunities, minimum backup |
| **Historical Average** | 36.8% (2000-2023) | Validation benchmark |
| **Drought Threshold** | 34.1% (P20 of historical) | Operational stress indicator |

### **Monthly Availability Patterns**

<div align="center">
  <img src="VerveStacks_USA/source_data/USA_hydro_monthly_profile.png" 
       alt="Monthly Hydro Availability Profile" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Monthly hydro availability showing P10/P50/P90 future scenarios validated against historical patterns</em></p>
</div>

### **Long-term Trajectory Analysis**

<div align="center">
  <img src="VerveStacks_USA/source_data/USA_hydro_annual_trajectory.png" 
       alt="Annual Hydro Availability Trajectory" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Annual hydro trajectories connecting historical data (2000-2023) to future scenarios (2025-2050)</em></p>
</div>

### **Planning Applications**

**Capacity Planning**: Use P50 for base case sizing, verify adequacy with P10 scenarios  
**Investment Analysis**: P10 scenarios for downside risk, P90 for upside potential  
**System Operations**: P10 for emergency preparedness, P50 for maintenance scheduling  
**Policy Analysis**: Understand drought impacts on energy security and backup requirements

**Key Insight**: The future will not match historical averages. Planning for hydro variability using P10/P50/P90 scenarios is essential for reliable, cost-effective energy systems.


## Temporal Modeling & Timeslice Analysis

### Advanced Stress Period Identification

This model employs sophisticated **statistical scenario generation** to identify critical periods in high-renewable energy systems:

#### 🔥 **Scarcity Periods** - Renewable Shortage Crisis
- Days with lowest renewable energy coverage relative to demand
- Critical for capacity planning and storage requirements
- Identifies when conventional backup power is most needed

#### ⚡ **Surplus Periods** - Renewable Excess Management  
- Days with highest renewable generation exceeding demand
- Essential for curtailment analysis and export/storage strategies
- Shows opportunities for demand shifting and industrial electrification

#### 🌪️ **Volatile Periods** - Operational Challenges
- Days with highest generation variability and unpredictability
- Important for grid stability and flexible resource planning
- Captures rapid ramping requirements for dispatchable assets

### Comprehensive Stress Period Analysis

The following visualizations provide detailed insights into temporal patterns and critical periods:

#### **Renewable Energy Analysis Overview**
<div align="center">
<img src="VerveStacks_USA/timeslice_analysis/re_analysis_summary_USA.svg" alt="Renewable Energy Analysis Summary" width="100%">
</div>

#### **Aggregated days and hours (upto 12 seasons X 8 day-night periods)**
<div align="center">
<img src="VerveStacks_USA/timeslice_analysis/aggregation_justification_USA_ts_096.svg" alt="Aggregated slices clustering" width="100%">
</div>


#### **Triple-5 Critical Periods (Comprehensive Stress Analysis)**
<div align="center">
<img src="VerveStacks_USA/timeslice_analysis/stress_periods_s5p5v5_d_USA.svg" alt="Triple-5 Critical Periods" width="100%">
</div>

### Timeslice Structure Generation
**Multi-Scale Temporal Resolution:**
- **Base Aggregation**: 6 seasons × 8 daily periods = 48 base timeslices
- **Critical Period Enhancement**: Additional segments for identified stress periods


## AR6 Climate Scenarios - R10NORTH_AM

This model incorporates climate scenario drivers from the IPCC AR6 database for the **R10NORTH_AM** region, 
derived from 350 vetted scenario-model combinations spanning 5 climate categories 
from ambitious 1.5°C pathways (C1) to limited mitigation trajectories (C7). The scenarios cover 
7 years from 2020 to 2050, providing comprehensive 
pathways for energy system transformation under different climate policy futures.


### Climate Scenario Trajectories

<div align="center">
  <img src="VerveStacks_USA/scenario_drivers/ar6_scenarios_USA.png" 
       alt="AR6 Climate Scenario Trajectories" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Climate scenario trajectories showing CO2 prices, electricity growth, and hydrogen deployment across different climate ambitions</em></p>
</div>

**Key Insights:**
- **5 Climate Categories**: From 1.5°C pathways to baseline scenarios
- **350 Scenario-Model Combinations**: Comprehensive coverage of transformation pathways  
- **Regional Context**: R10NORTH_AM region-specific climate policy patterns
- **Temporal Coverage**: 2020-2050 transformation trajectories


### Scenario-Model Divergence Analysis

**Model Agreement**: Analysis across 350 scenario-model combinations reveals:
- **High Convergence**: CO2 pricing trajectories (CV: inf%) and electricity growth (CV: 16.0%)
- **Moderate Uncertainty**: Transport electrification rates (CV: 85.8%) 
- **High Divergence**: Hydrogen deployment pathways (CV: inf%)

**Regional Characteristics**: The R10NORTH_AM region shows moderate convergence compared to global 
averages, with region-specific climate policy patterns reflecting economic and policy context.


## Quality Assurance

- Cross-validation between IRENA, EMBER, and UNSD statistics
- Capacity-generation consistency checks
- Technology classification verification
- Historical data reconciliation for base year (2022)
- Renewable resource potential validated against REZoning database
- Temporal analysis verified through statistical scenario methods


## Usage Notes

- For questions about specific data sources or methodology, refer to online documentation
- Model parameters can be adjusted manually in the model files

---
*Generated by VerveStacks Energy Model Processor*
*For more information: [VerveStacks Documentation](https://vervestacks.readthedocs.io/en/latest/)*
