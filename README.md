# VerveStacks Model Generation Notes - ITA
**Generated:** 2025-09-06 12:45:00


## Processing Parameters

### Individual Plant Tracking
| **Fuel Type** | **Threshold** | **Plants Above Threshold** |
|---------------|---------------|---------------------------|
| 🌱 **Bioenergy** | 50.0 MW | 14/18 plants |
| ⚫ **Coal** | 150.0 MW | 14/14 plants |
| 🔥 **Gas** | 150.0 MW | 136/265 plants |
| 🌋 **Geothermal** | 40.0 MW | 10/27 plants |
| 💧 **Hydro** | 40.0 MW | 141/161 plants |
| 🛢️ **Oil** | 150.0 MW | 103/174 plants |
| ☀️ **Solar** | 200.0 MW | 0/369 plants |
| 🌊 **Windoff** | 200.0 MW | 0/1 plants |
| 💨 **Windon** | 200.0 MW | 4/275 plants |


### 🔄 CCS Retrofit Potential
| **Fuel Type** | **Retrofit Host Capacity** | **Retrofit Potential Capacity**
|---------------|----------------------------|-------------------------------|
| ⚫ **Coal** | 6.8 GW | 4.7 GW after capacity penalty |
| 🔥 **Gas** | 60.2 GW | 50.8 GW after capacity penalty |


## Data, Assumptions & Coverage

### Primary Data Sources

#### Base-Year Power Plant Specifications
- **Global Energy Monitor (GEM)** [🌐](https://globalenergymonitor.org)  
  Open-access database of individual power plants worldwide, including location, capacity, fuel type, commissioning year, and technical specifications.
- **International Renewable Energy Agency (IRENA)** [🌐](https://www.irena.org/Statistics)  
  Global renewable energy capacity and generation statistics (2000–2022), disaggregated by country and technology.
- **EMBER Climate** [🌐](https://ember-climate.org/data/)  
  Global dataset tracking electricity generation, installed capacity, and emissions intensity (2000–2022).

### Data Processing Notes
- **Individual Plant Coverage**: 78.1%% of total capacity from plant-level GEM data
- **Total Capacity Tracked**: 182.9 GW GW from all sources
- **Plants Above Threshold**: 474 individual plants tracked
- **Total Plants Processed**: 1304 plants in database
- **Missing Capacity Added**: - **IRENA data**:
  - **hydro**: 6.73 GW
  - **windon**: 0.24 GW
- **EMBER data**:
  - **gas**: 6.44 GW
  - **bioenergy**: 3.58 GW
  - **coal**: 1.62 GW


## Model Structure

### Files Included
- **Source Data**: `source_data/VerveStacks_ITA.xlsx` - the full dataset in a model-agnostic format
- **VEDA Model Files**: Complete model ready for Veda-TIMES execution
- **Scenario Files**: NGFS climate scenarios and policy assumptions


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

### Timeslice Structure Generation
**Multi-Scale Temporal Resolution:**
- **Base Aggregation**: 6 seasons × 8 daily periods = 48 base timeslices
- **Critical Period Enhancement**: Additional segments for identified stress periods


## Interactive Grid Network Visualization

### 🗺️ **Real-Time Grid Exploration**

This model includes an **interactive network visualization** showing the complete transmission infrastructure and renewable energy integration:

<div align="center">
  <iframe src="source_data/grid_analysis/ITA_network_visualization.html" 
          width="900" height="650" 
          frameborder="0" 
          style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
  <p><em>Interactive grid network - Click to explore transmission topology, power plants, and renewable zones</em></p>
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
| **Total Buses** | {total_buses} | Transmission substations and connection points |
| **Transmission Lines** | {total_lines} | High-voltage transmission corridors |
| **Voltage Levels** | {voltage_levels} | Multi-level transmission system (220kV, 380kV, etc.) |
| **Grid Coverage** | {grid_coverage_area} km² | Geographic area covered by transmission network |
| **Average Line Length** | {avg_line_length} km | Mean distance between connected buses |

#### ⚡ **Power Plant Integration**

| **Integration Type** | **Count** | **Total Capacity** | **Description** |
|---------------------|-----------|-------------------|-----------------|
| **Plants Mapped to Buses** | {plants_mapped} | {plants_capacity_gw} GW | GEM power plants assigned to grid locations |
| **Renewable Plants** | {renewable_plants} | {renewable_capacity_gw} GW | Solar, wind, hydro plants on the grid |
| **Conventional Plants** | {conventional_plants} | {conventional_capacity_gw} GW | Coal, gas, nuclear plants on the grid |
| **Clustering Efficiency** | {clustering_ratio}% | - | Bus reduction achieved through DBSCAN clustering |


### Spatial Resolution & Renewable Zones

#### 🗺️ **High-Resolution Grid Modeling**

This model employs **50×50km spatial resolution** for detailed renewable energy analysis:

| **Spatial Metric** | **Value** | **Technical Detail** |
|-------------------|-----------|---------------------|
| **Grid Cells** | {total_grid_cells} | 50×50km renewable energy zones |
| **Solar/Wind Onshore Zones** | {solar_wind_onshore_zones} | Grid cells with solar and onshore wind potential |
| **Wind Offshore Zones** | {wind_offshore_zones} | Grid cells with offshore wind potential |
| **Zone-Bus Mappings** | {zone_bus_mappings} | REZoning zones assigned to transmission buses |
| **Spatial Coverage** | {spatial_coverage_area} km² | Total area covered by renewable zones |

#### 🔌 **Spatial Commodity System**

Each grid cell generates location-specific electricity commodities:
- **Solar/Wind Onshore**: `elc_spv-{iso_code}_001` to `elc_spv-{iso_code}_{max_solar_id}` (same zones for both technologies)
- **Wind Offshore**: `elc_wof-{iso_code}_001` to `elc_wof-{iso_code}_{max_offshore_id}`

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
| **Voronoi Tessellation** | {voronoi_buses} | {voronoi_load_gw} GW | Geometric proximity-based allocation |

#### 📈 **Load Concentration Analysis**

- **Highest Load Bus**: {max_load_bus} ({max_load_gw} GW)
- **Load Distribution CV**: {load_cv}% (coefficient of variation)
- **Load Balancing**: {load_balance_description}

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


## Quality Assurance

- Cross-validation between IRENA, EMBER, and UNSD statistics
- Capacity-generation consistency checks
- Technology classification verification
- Historical data reconciliation for base year (2022)
- Renewable resource potential validated against REZoning database
- Temporal analysis verified through statistical scenario methods


## Usage Notes

- This model is generated automatically using VerveStacks methodology
- Timeslice structure is optimized for high-renewable energy system analysis
- For questions about specific data sources or methodology, refer to online documentation
- Model parameters can be adjusted manually in the model files
- Charts and analysis files are located in `2_ts_design/outputs/ITA/`

---
*Generated by VerveStacks Energy Model Processor*
*For more information: [VerveStacks Documentation](https://github.com/your-org/vervestacks)*
