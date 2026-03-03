# VerveStacks Model Generation Notes - ARE
**Generated:** 2026-03-03 16:37:35


## Model Calibration 2022

| **Total Capacity** | **Total Generation** | **CO2 Emissions** | **Calibration to EMBER** |
|--------------|---------------|------------|--------------------------|
| 50 GW | 153 TWh | 77 Mt | 90% |

**Note:** 2022 fossil and bio capacity is calibrated to EMBER and renewable capacities to IRENA. UNSD has incomplete data for fuel consumption, so the calibration is demonstrated against the total CO2 emission reported by EMBER. This shows that the efficiency assumptions are good.


## Power Generation Assets

### Existing Capacity

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Active Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 1/2 plants | 0.22 GW | 21.4% |
| ⚫ **Coal** | 50 MW | 2/2 plants | 1.2 GW | 28.6% |
| 🔥 **Gas** | 50 MW | 120/127 plants | 47.9 GW | 34.8% |
| 💧 **Hydro Power** | 10 MW | 1/1 plants | 0.25 GW | 100% |
| ⚛️ **Nuclear** | — | 4/4 plants | 5.67 GW | 100% |
| ☀️ **Solar** | 200 MW | 13/31 plants | 6.7 GW | 100% |
| 💨 **Windon** | 200 MW | 0/4 plants | 0.099 GW | 100% |


### Future Projects (offered for endogenous selection)

| **Fuel Type** | **Threshold** | **Plants Above Threshold** | **Total Capacity** | **Wtd Avg Efficiency** |
|---------------|---------------|----------------------------|--------------------|-----------------|
| 🌱 **Bioenergy** | 50 MW | 2/2 plants | 0.14 GW | 30.7% |
| 🔥 **Gas** | 50 MW | 4/4 plants | 9 GW | 39.5% |
| ☀️ **Solar** | 200 MW | 12/14 plants | 11.4 GW | 100% |


Announced and pre-construction projects are offered as options to the model for endogenous investment. This is particularly useful for hydro and pumped storage as country-wise potential is not readily available. We also get grid locations of all these units.

### 🔄 CCS Retrofit Potential
| **Fuel Type** | **Retrofit Host Capacity** | **Retrofit Potential Capacity**
|---------------|----------------------------|-------------------------------|
| ⚫ **Coal** | 1.2 GW | 0.873 GW after capacity penalty |
| 🔥 **Gas** | 47.9 GW | 40.5 GW after capacity penalty |


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
- **Individual Plant Coverage**: 97%% of total capacity from plant-level GEM data
- **Total Capacity Tracked**: 83 GW GW from all sources
- **Plants Above Threshold**: 136 individual plants tracked
- **Total Plants Processed**: 191 plants in database
- **Missing Capacity Added**: - **EMBER data**:
  - **gas**: 1.29 GW


## Model Structure

### Files Included
- **Source Data**: `source_data/VerveStacks_ARE.xlsx` - the full dataset in a model-agnostic format
- **VEDA Model Files**: Complete model ready for Veda-TIMES execution
- **Scenario Files**: NGFS climate scenarios and policy assumptions


## Grid Network Visualization

### 🗺️ **Grid Network Overview**

This model includes a **comprehensive grid visualization** showing the complete transmission infrastructure and renewable energy integration:

<div align="center">
  <img src="VerveStacks_ARE_grids_kan/grid_analysis/ARE_network_visualization.svg" 
       alt="Grid Network Visualization" 
       style="max-width: 100%; height: auto; border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><em>🗺️ Grid network showing transmission infrastructure, power plants, and renewable energy zones</em></p>
</div>

**What you can explore:**
- **Transmission Network**: High-voltage lines and substations from real grid data
- **Power Plant Locations**: Actual generating facilities mapped to grid buses
- **Renewable Energy Zones**: 50×50km grid cells with solar/wind potential
- **Load Centers**: Industrial demand distribution across the network
- **Grid Constraints**: Bottlenecks and transmission limitations


### Grid Topology Statistics

#### 📊 **Transmission Infrastructure**

| **Metric** | **Value** | **Description** |
|------------|-----------|-----------------|
| **Total Buses** | 137 | Transmission substations and connection points |
| **Transmission Lines** | 218 | High-voltage transmission corridors |
| **Voltage Levels** | 220.0, 400.0 | Multi-level transmission system (220kV, 380kV, etc.) |

#### ⚡ **Power Plant Integration**

| **Integration Type** | **Count** | **Total Capacity** | **Description** |
|---------------------|-----------|-------------------|-----------------|
| **Plants Mapped to Buses** | 79 | 79 GW | GEM power plants assigned to grid locations |


### Spatial Resolution & Renewable Zones

#### 🗺️ **High-Resolution Grid Modeling**

This model employs **50×50km spatial resolution** for detailed renewable energy analysis:

| **Spatial Metric** | **Value** | **Technical Detail** |
|-------------------|-----------|---------------------|
| **Grid Cells** | 277 | 50×50km renewable energy zones |
| **Solar/Wind Onshore Zones** | 158 | Grid cells with solar and onshore wind potential |
| **Wind Offshore Zones** | 118 | Grid cells with offshore wind potential |
| **Zone-Bus Mappings** | 277 | REZoning zones assigned to transmission buses |

#### 🔌 **Spatial Commodity System**

Each grid cell generates location-specific electricity commodities:
- **Solar**: `elc_spv_<cluster_id>`
- **Wind Onshore**: `elc_won_<cluster_id>`
- **Wind Offshore**: `elc_wof_<cluster_id>`

This enables **grid-aware optimization** where renewable generation is constrained by:
- Transmission capacity between zones
- Grid stability requirements
- Spatial resource quality variations
- Inter-zone electricity trade opportunities


### Load Distribution Analysis

#### 🏭 **Industrial Demand Mapping**

Industrial electricity demand is spatially distributed across the transmission network using **Voronoi tessellation**:

| **Load Distribution Method** | **Buses with Load** | **Total Industrial Load** | **Methodology** |
|------------------------------|---------------------|---------------------------|-----------------|
| **Voronoi Tessellation** | 8 | 1.0 GW | Geometric proximity-based allocation |

#### 📈 **Load Concentration Analysis**

- **Highest Load Bus**: way/29495366-400 (0.48 GW)
- **Load Distribution CV**: 0% (coefficient of variation)
- **Load Balancing**: Balanced distribution across transmission buses

This spatial load distribution enables **realistic grid modeling** where:
- Industrial demand varies by location
- Transmission constraints affect supply-demand balancing
- Grid bottlenecks impact renewable integration
- Regional electricity trade opportunities are identified


### Technical Implementation

#### 🔬 **Grid Processing Methodology**

**1. Network Extraction & Clustering**
- **Source**: OpenStreetMap transmission data via PyPSA-Eur
- **Clustering**: DBSCAN algorithm reduces bus count by 0.0%
- **Topology Preservation**: Critical transmission lines maintained during clustering
- **Voltage Hierarchy**: Multi-level transmission system (220kV, 380kV, 500kV)

**2. Renewable Zone Integration**
- **REZoning Database**: 50×50km grid cells with LCOE and capacity factor data
- **Spatial Mapping**: Zones assigned to nearest transmission buses
- **Resource Quality**: Capacity factors vary by location and technology
- **Grid Constraints**: Transmission capacity limits renewable integration

**3. Power Plant Assignment**
- **GEM Database**: Global Energy Monitor power plant locations
- **Spatial Proximity**: Plants assigned to nearest transmission buses
- **Capacity Aggregation**: Multiple plants at same bus aggregated
- **Technology Classification**: Fuel type and generation technology preserved

**4. Load Distribution Algorithm**
- **Industrial Database**: Hotmaps industrial electricity consumption
- **Voronoi Tessellation**: Geometric proximity-based allocation to nearest transmission buses
- **Grid Integration**: Load assigned to transmission buses, not individual consumers

#### 🎯 **Model Capabilities**

This grid modeling enables:
- **Transmission Constraint Analysis**: Identify grid bottlenecks and expansion needs
- **Renewable Integration Studies**: Optimize renewable deployment considering grid limits
- **Inter-Regional Trade**: Model electricity exchange between grid zones
- **Grid Stability Assessment**: Analyze system stability with high renewable penetration
- **Investment Planning**: Identify optimal transmission and generation investments


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
<img src="VerveStacks_ARE_grids_kan/renewable_energy/supply_curves_ARE.svg" alt="Renewable Energy Supply Curves" width="100%">
</div>

This analysis provides the foundation for understanding renewable energy economics and informs 
capacity expansion decisions in the VEDA/TIMES energy system models.


### Renewable Energy Clustering

VerveStacks employs **intelligent spatial clustering** to transform high-resolution renewable energy 
grid cells into manageable clusters while preserving essential resource characteristics and geographic diversity.

#### **Clustering Overview**

| **Clustering Metric** | **Value** | **Description** |
|----------------------|-----------|-----------------|
| **Grid Cells Processed** | 277 | 50×50km renewable energy grid cells |
| **Clusters Generated** | 10 | Dynamically determined using n = cells^0.6 |
| **Average Cluster Size** | 4.8 grid cells | Mean grid cells per cluster |
| **Cluster Size Range** | 4 to 7 grid cells | Variation in cluster composition |
| **Grid Definition** | Infrastructure-based transmission buses | Transmission infrastructure basis |

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
  <img src="VerveStacks_ARE_grids_kan/source_data/clustering_results_ARE_solar.png" 
       alt="Solar PV Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Solar PV clustering showing 10 clusters from 277 grid cells using Infrastructure-based transmission buses</em></p>
</div>

**Onshore Wind Clustering:**
<div align="center">
  <img src="VerveStacks_ARE_grids_kan/source_data/clustering_results_ARE_wind_onshore.png" 
       alt="Onshore Wind Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Onshore wind clustering showing 10 clusters from 277 grid cells using Infrastructure-based transmission buses</em></p>
</div>

**Offshore Wind Clustering:**
<div align="center">
  <img src="VerveStacks_ARE_grids_kan/source_data/clustering_results_ARE_wind_offshore.png" 
       alt="Offshore Wind Clustering Results" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Offshore wind clustering showing 10 clusters from 277 grid cells using Infrastructure-based transmission buses</em></p>
</div>

**Visualization Features:**
- **Technology-specific clustering**: Each renewable technology clustered independently
- **Color-coded clusters**: Each cluster shown in distinct colors
- **Grid cell boundaries**: 50×50km renewable energy zones
- **Transmission infrastructure**: Infrastructure-based transmission buses overlaid for context
- **Resource quality**: Cluster composition reflects capacity factor variations


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
<img src="VerveStacks_ARE_grids_kan/timeslice_analysis/re_analysis_summary_ARE.svg" alt="Renewable Energy Analysis Summary" width="100%">
</div>

#### **Aggregated days and hours (upto 12 seasons X 8 day-night periods)**
<div align="center">
<img src="VerveStacks_ARE_grids_kan/timeslice_analysis/aggregation_justification_ARE_ts_096.svg" alt="Aggregated slices clustering" width="100%">
</div>


#### **Triple-5 Critical Periods (Comprehensive Stress Analysis)**
<div align="center">
<img src="VerveStacks_ARE_grids_kan/timeslice_analysis/stress_periods_s5p5v5_d_ARE.svg" alt="Triple-5 Critical Periods" width="100%">
</div>

### Timeslice Structure Generation
**Multi-Scale Temporal Resolution:**
- **Base Aggregation**: 6 seasons × 8 daily periods = 48 base timeslices
- **Critical Period Enhancement**: Additional segments for identified stress periods


## AR6 Climate Scenarios - R10MIDDLE_EAST

This model incorporates climate scenario drivers from the IPCC AR6 database for the **R10MIDDLE_EAST** region, 
derived from 350 vetted scenario-model combinations spanning 5 climate categories 
from ambitious 1.5°C pathways (C1) to limited mitigation trajectories (C7). The scenarios cover 
7 years from 2020 to 2050, providing comprehensive 
pathways for energy system transformation under different climate policy futures.


### Climate Scenario Trajectories

<div align="center">
  <img src="VerveStacks_ARE_grids_kan/scenario_drivers/ar6_scenarios_ARE.png" 
       alt="AR6 Climate Scenario Trajectories" 
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p><em>Climate scenario trajectories showing CO2 prices, electricity growth, and hydrogen deployment across different climate ambitions</em></p>
</div>

**Key Insights:**
- **5 Climate Categories**: From 1.5°C pathways to baseline scenarios
- **350 Scenario-Model Combinations**: Comprehensive coverage of transformation pathways  
- **Regional Context**: R10MIDDLE_EAST region-specific climate policy patterns
- **Temporal Coverage**: 2020-2050 transformation trajectories


### Scenario-Model Divergence Analysis

**Model Agreement**: Analysis across 350 scenario-model combinations reveals:
- **High Convergence**: CO2 pricing trajectories (CV: inf%) and electricity growth (CV: 19.4%)
- **Moderate Uncertainty**: Transport electrification rates (CV: 139.1%) 
- **High Divergence**: Hydrogen deployment pathways (CV: 102.5%)

**Regional Characteristics**: The R10MIDDLE_EAST region shows moderate convergence compared to global 
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
