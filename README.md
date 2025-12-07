# VerveStacks
**Professional Energy System Models - Ready to Use**

[![Countries](https://img.shields.io/badge/countries-190+-green.svg)](#global-coverage)
[![Data Sources](https://img.shields.io/badge/datasets-8+-orange.svg)](#data-foundation)
[![License](https://img.shields.io/badge/models-freely%20available-blue.svg)](#license)

---

## 🏗️ **Understanding the Real System Before the Model**

VerveStacks inverts the traditional modeling sequence:

**Traditional Approach: Model → Reality**
1. Build abstract model structure
2. Populate with aggregated data
3. Hope it represents reality
4. Struggle to validate

**VerveStacks Approach: Reality → Model**
1. Start with real power plants, actual grid, observed generation
2. Process into model structure preserving detail
3. Validate against multiple sources during construction
4. Deliver pre-validated, explorable model

**The result:** Models grounded in observable reality that domain experts can immediately recognize and trust.

---

## ✓ **The Validation Journey**

Open any country model in VEDA. Within hours, you can verify against your domain knowledge:

- **Base Year Reality Check**: Does 2022 installed capacity match official statistics?
- **Technology Mix Recognition**: Do you recognize the fuel composition?
- **Geographic Credibility**: Are power plants in expected locations?
- **Grid Infrastructure**: Does transmission topology reflect reality?
- **Resource Potential**: Are renewable zones appearing where they should?
- **Scenario Plausibility**: Do 2050 pathways align with country context?
- **Technology Roles**: Is offshore wind, CCS, hydrogen deployment reasonable?

**This is how you START with VerveStacks** - verifying a complete, structured model against what you already know about your country's energy system.

Then you focus on what matters: **policy analysis, scenario design, stakeholder engagement, and decision support.**

---

## 🎯 **Start Where Others End**

**The Traditional Path:**
```
Person-Years → Data Collection → Model Building → Validation → Analysis
     ↓              ↓                  ↓              ↓           ↓
  2 years      6 months          12 months      6 months    (if time remains)
```

**The VerveStacks Path:**
```
Verification → Analysis → Policy Testing → Stakeholder Engagement
     ↓            ↓              ↓                    ↓
  2 days     Weeks/Months   Continuous          Continuous
```

**Most modeling projects never reach comprehensive validation.** 

**VerveStacks users start there.**

---

## 📊 **What You Get: Curated, Structured Data**

Each country model includes professionally curated data structured for immediate use in VEDA/TIMES:

### **Existing Power Generation Fleet**
- **Individual Plant Detail**: Units >10-200 MW threshold with actual specifications
- **Geographic Precision**: GPS coordinates with grid location assignment
- **Technical Parameters**: Vintage-based efficiency, capacity factors, commissioning years
- **Calibrated Reality**: 2022 capacity/generation matching IRENA/EMBER statistics

### **Grid Infrastructure** (where available)
- **Transmission Network**: Actual topology from OpenStreetMap data
- **Spatial Regions**: Mathematically consistent clustering (4-400+ regions)
- **Load Distribution**: Industrial demand mapped to transmission buses
- **Renewable Zones**: 50×50km grid cells with location-specific capacity factors

### **Renewable Energy Potential**
- **Supply Curves**: Technology-specific LCOE vs. capacity curves
- **Hourly Profiles**: 8760-hour generation patterns by cluster
- **Conservative Estimates**: Land-use constraints and overlap resolution
- **Quality Filtering**: Only economically viable resources included

### **Temporal Modeling**
- **Intelligent Timeslices**: 1-600 timeslices capturing critical periods
- **Stress Period Identification**: Scarcity, surplus, and volatility analysis
- **Flexible Resolution**: From simple seasonal to detailed hourly representation

### **Climate Scenarios**
- **IPCC AR6 Integration**: 5 climate categories with sectoral trajectories
- **NGFS Pathways**: Carbon pricing and policy assumptions
- **Regional Mapping**: ISO codes mapped to AR6 R10 regions
- **Technology Evolution**: Dynamic cost reductions 2022-2050

### **Validation & Documentation**
- **Model vs. Reality Charts**: Base year calibration verification
- **Data Lineage**: Complete traceability to source datasets
- **Technical Methodology**: Assumptions and processing documented
- **Visual Diagnostics**: Grid maps, supply curves, stress periods

---

## 🔬 **Methodological Innovations**

These sophisticated methodologies distinguish VerveStacks models from simple aggregated datasets:

### **🔥 Stress-Based Timeslice Design**

**Revolutionary temporal modeling** that identifies when storage and flexibility face maximum operational stress:

**The Core Innovation:**  
Instead of fixed timeslice structures (12 months, 3 day types), VerveStacks identifies critical periods through coverage analysis:

1. **Baseline Construction**: Current demand profile with existing nuclear (flat dispatch) and hydro (load-following within monthly constraints)
2. **Renewable Portfolio**: Solar/wind mix based on relative LCOEs from REZoning data to meet annual demand
3. **Coverage Analysis**: Calculate hourly renewable supply adequacy:  
   `Coverage = (Solar + Wind + Hydro) / Demand × 100%`
4. **Stress Period Identification**: Rank days/weeks by:
   - **Scarcity** (<100% coverage) - when conventional backup is needed
   - **Surplus** (>100% coverage) - when curtailment or storage charging occurs
   - **Volatility** (high variability) - when ramping requirements peak
5. **Intelligent Aggregation**: Select combinations of critical periods to create 1-600 timeslices based on system complexity

**Why This Matters:**  
Timeslices capture the periods that matter most for grid operations - when storage must work hardest, ramping is most critical, and dispatchable generation faces peak demand. This enables accurate capacity planning and investment decisions.

**Result:** Traditional fixed timeslices miss critical events. Stress-based timeslices focus computational effort where it matters most.

---

### **🗺️ Multi-Resolution Spatial Clustering**

**Mathematically rigorous regional modeling** that scales from small countries (4 regions) to large countries (400+ regions):

**The Challenge:**  
Real energy systems have different spatial patterns for demand centers, existing power plants, and renewable resources. Simple geographic clustering forces artificial uniformity.

**The VerveStacks Solution:**

1. **Separate Resolution Levels**:
   - **Demand Regions**: Clustered by population and industrial centers (fewer, larger regions)
   - **Generation Clusters**: Existing power plants grouped by grid connectivity
   - **Renewable Zones**: 50×50km cells clustered by resource quality and hourly profiles

2. **Voronoi Tessellation**:
   - **Non-Overlapping Boundaries**: Mathematically guaranteed regional consistency
   - **Proximity-Based Assignment**: Each point assigned to nearest cluster center
   - **Flexible Topology**: Adapts to country size and complexity

3. **Transmission Modeling**:
- **Trade Link Optimization**: Connections from generation/renewable clusters to closest demand centers
   - **NTC Estimation**: Net Transfer Capacity using OpenStreetMap grid data
   - **Distance-Based Costs**: Transmission efficiency and investment costs from actual distances

4. **Intelligent Aggregation**:
   - **Unit-Level Detail**: Plants >100 MW modeled individually with vintage parameters
   - **Smart Aggregation**: Smaller units grouped preserving capacity-weighted characteristics

**Why This Matters:**  
Enables realistic representation of transmission constraints, renewable integration challenges, and regional electricity trade opportunities.

---

### **⚙️ Vintage-Based Technology Modeling**

**Realistic representation of existing infrastructure** capturing the full complexity of real energy systems:

**The Problem:**  
Real power plants vary dramatically in efficiency, cost, and performance based on age, technology generation, and maintenance history. Simple average parameters miss this heterogeneity.

**The VerveStacks Approach:**

1. **Age-Dependent Parameters**:
   - Efficiency degradation curves by commissioning year
   - Operating cost variations reflecting technology generation
   - Maintenance cost escalation for aging units

2. **Individual Plant Tracking**:
   - Each unit >threshold modeled separately
   - Actual commissioning years preserved
   - Real capacity and fuel type from plant-level data

3. **Retrofit Pathways**:
   - **CCS Integration**: EPA-based methodology for CO2 capture retrofits
   - **Capacity Penalties**: Realistic auxiliary power consumption (~15-25%)
   - **Efficiency Impacts**: Performance degradation from capture equipment
   - **Cost Estimates**: Transport and storage at $30/t CO2

4. **Regional Cost Adjustments**:
   - Country-specific multipliers reflecting local economic conditions
   - Regional fuel price variations
   - Labor cost differences

**Why This Matters:**  
Enables realistic fossil phase-out planning, retrofit evaluation, and understanding of stranded asset risks. Critical for transition pathway design.

---

### **🌐 Multi-Source Data Reconciliation**

**Systematic integration and validation** across multiple authoritative datasets:

**The Challenge:**  
IRENA, EMBER, GEM, and national statistics often disagree. Using any single source means missing data or accepting errors.

**The VerveStacks Solution:**

1. **Hierarchical Integration**:
   - **Individual Plants**: Global Energy Monitor (GEM) as primary source
   - **Total Capacity**: IRENA statistics as validation benchmark
   - **Generation & Emissions**: EMBER data for base year calibration
   - **Gap Filling**: Synthetic units to match official statistics

2. **Conflict Resolution**:
   - Cross-validate capacity totals across sources
   - Technology classification with fuel-specific efficiency assumptions
   - Geographic assignment using GPS coordinates
   - Commissioning year reconciliation

3. **Quality Assurance**:
   - Base year generation must match EMBER within 5%
   - Capacity factors consistent with technology and location
   - Emissions validate efficiency assumptions
   - Missing capacity flagged and documented

4. **Transparent Lineage**:
   - Every parameter traceable to source dataset
   - Assumptions documented and justified
   - Synthetic additions clearly identified
   - Validation charts included in model documentation

**Why This Matters:**  
Builds confidence in model outputs. Users can verify against known data and trust results for future scenarios.

---

### **💧 Probabilistic Hydro Scenarios**

**Planning for hydrological uncertainty** using historical patterns and climate projections:

**The Problem:**  
Hydro availability varies dramatically year-to-year. Using historical average capacity factors underestimates backup capacity needs and drought vulnerability.

**The VerveStacks Solution:**

1. **Historical Analysis**: 24 years (2000-2023) of EMBER generation data
2. **Regime Classification**: Model persistence of wet, normal, and dry conditions
3. **Drought Thresholds**: Country-specific P20 (bottom 20% of historical) capacity factors
4. **Climate Adjustment**: Apply declining trends and increasing variability
5. **Scenario Generation**: Create P10/P50/P90 future pathways with:
   - Monthly seasonal patterns preserved
   - Multi-year persistence captured
   - Extreme events included
   - Climate change impacts reflected

**Why This Matters:**  
High-hydro countries (>30% of generation) face energy security risks during drought sequences. P10 scenarios enable adequate backup capacity planning.

---

### **🌍 Renewable Zone Clustering**

**Preserving geographic diversity** while reducing computational complexity:

**The Challenge:**  
50×50km REZoning grid produces thousands of zones per country. Direct use in optimization models is computationally prohibitive, but simple aggregation loses geographic hedging benefits.

**The VerveStacks Solution:**

1. **Multi-Feature Clustering**:
   - **Hourly Profiles**: 8760-hour capacity factor time series
   - **Economic Parameters**: LCOE and connection cost data
   - **Spatial Coordinates**: Geographic location for transmission modeling
   - **Resource Quality**: Mean capacity factor and potential capacity

2. **Hierarchical Algorithm**:
   - PCA dimensionality reduction (50 components per technology)
   - Ward linkage clustering with Euclidean distance
   - Dynamic cluster count: n = cells^0.6
   - Standardization across all features

3. **Capacity-Weighted Aggregation**:
   - Each cluster receives weighted hourly profile
   - Higher potential zones have greater influence
   - Economic rationality preserved in aggregation

4. **Geographic Hedging**:
   - Wind resource diversity (spatial variation in patterns)
   - Solar complementarity (east-west and north-south effects)
   - Grid connection costs (distance-based)
   - Temporal smoothing (geographic diversity reduces volatility)

**Why This Matters:**  
Enables both grid and non-grid models to capture realistic renewable resource diversity. Prevents unrealistic technology monopolization in optimization results.

---

## 🌐 **Radical Openness**

VerveStacks models are **more open than traditional "open source"** because they impose **zero cognitive load** to start using:

| **Traditional Open Source** | **VerveStacks Open Models** |
|----------------------------|----------------------------|
| 10,000 lines of code to understand | Open in VEDA, explore immediately |
| Setup environments, dependencies | Pre-structured, ready to run |
| Data scattered across scripts | All data in organized Excel files |
| Build first, verify later | Verify first, customize as needed |
| **Cognitive barrier to entry** | **Cognitive ramp as you go** |

### **Freedom to Explore**

- **Start with Results**: Models are complete and validated - begin exploring immediately
- **Optional Deep Dive**: Understand methodology at your own pace, if desired
- **Full Transparency**: Every assumption, data source, and calculation documented
- **Modify Freely**: Fork any country model, adjust parameters, add technologies
- **No Black Boxes**: Complete data lineage from global datasets to model parameters

**Users have the OPTION to break the builder's habit** - you can start with a working model and explore results, or dive into methodology first. Your choice.

---

## 🚀 **Getting Started**

### **Browse Country Models**

Each country has its own branch with a complete, ready-to-use model:

```bash
# Clone any country model
git clone -b vervestacks-CHE https://github.com/your-org/vervestacks-models.git

# Models are immediately usable in VEDA/TIMES
# - Open .veda files in Veda-TIMES
# - Explore existing scenarios
# - Add your own policy assumptions
# - Run analyses
```

### **Explore What's Included**

Every model branch contains:
- `source_data/` - Complete dataset in model-agnostic Excel format
- `vt_*.xlsx` - VEDA transformation files
- `Sets-vervestacks.xlsx` - Technology and commodity definitions
- `Scen_*.xlsx` - AR6 climate scenarios and policy assumptions
- `grid_analysis/` - Network visualization and topology data
- `renewable_energy/` - Supply curves and cluster assignments
- `timeslice_analysis/` - Stress period identification charts
- `README.md` - Country-specific validation and specifications

### **Typical Workflow**

1. **Verify**: Open model in VEDA, check if base year matches your understanding
2. **Explore**: Run existing scenarios, examine 2030/2050 pathways
3. **Customize**: Add country-specific policies, adjust assumptions
4. **Analyze**: Test policy options, generate insights
5. **Communicate**: Use built-in visualizations for stakeholders

---

## 🎓 **Use Cases**

### **Policy Analysis & Planning**
- **NDC Development**: Evaluate nationally determined contribution pathways
- **Decarbonization Strategies**: Test fossil phase-out scenarios
- **Investment Planning**: Identify optimal infrastructure timing and sizing
- **Energy Security**: Assess resilience under supply disruptions

### **Academic Research**
- **Cross-Country Comparison**: Consistent methodology across 190+ countries
- **Technology Assessment**: Evaluate emerging technology roles
- **Climate Impact Analysis**: Scenario-based transition studies
- **Methodology Development**: Build on validated baseline models

### **Capacity Building**
- **Training Programs**: Ready-made models for university courses
- **Institutional Development**: Enable in-house modeling capabilities
- **Technical Workshops**: Pre-validated examples for hands-on learning
- **Stakeholder Engagement**: Professional models for policy dialogue

---

## 📚 **Data Foundation**

### **Global Datasets Integrated**

| Dataset | Purpose | Coverage |
|---------|---------|----------|
| **[Global Energy Monitor](https://globalenergymonitor.org)** | Individual power plants | 40,000+ plants worldwide |
| **[IRENA Statistics](https://www.irena.org/Statistics)** | Renewable capacity/generation | 200+ countries, 2000-2022 |
| **[EMBER Climate](https://ember-climate.org/data/)** | Electricity generation/emissions | Global, hourly resolution |
| **[REZoning](https://www.irena.org/publications/2022/Mar/Renewable-Energy-Zoning-for-Energy-Transition)** | Renewable energy potential | 50×50km global grid |
| **[Atlite](https://github.com/PyPSA/atlite)** | Hourly capacity factor profiles | ERA5 weather data |
| **[NGFS Scenarios](https://www.ngfs.net)** | Climate policy projections | 5 scenarios, 2020-2100 |
| **[IPCC AR6](https://www.ipcc.ch/report/ar6/wg3/)** | Climate scenario trajectories | 350+ scenario-model combinations |
| **[IEA WEO](https://www.iea.org/weo)** | Technology costs | Global, 2020-2050 |

---

## 🌍 **Vision: Democratizing Energy System Modeling**

### **The Challenge**

**Energy modeling expertise is concentrated in wealthy institutions.** Decision-makers in developing countries, cities, and smaller organizations lack access to credible, usable models for policy analysis. This creates an **energy modeling divide** where those who need models most have the least access.

### **The VerveStacks Response**

**Shift focus from model building to model application.** By providing professionally curated, pre-validated models, we enable domain experts and policy makers to focus on their actual goal: **understanding energy transition options and making better decisions.**

### **Not Replacing Expertise - Reallocating It**

- **Traditional**: Spend person-years collecting data and building models
- **VerveStacks**: Spend person-years analyzing policies and engaging stakeholders
- **Result**: More time for what matters - decision support, not data wrangling

### **The ESOM OS Vision**

VerveStacks is evolving toward an **Energy System Operating System (ESOM OS)** - a comprehensive platform where:
- Models are **generated and maintained systematically** (like software updates)
- Users **apply models without building them** (like using applications)
- **Transparency and rigor** are built-in, not optional add-ons
- **Global coverage** enables cross-country learning and comparison

*Just as operating systems democratized computing by abstracting complexity, ESOM OS aims to democratize energy modeling by providing ready-to-use professional tools.*

---

## 🔄 **Sustainability Through Automation**

VerveStacks models are maintained through automated data processing pipelines. This enables:

- **Regular Updates**: New data releases integrated efficiently
- **Global Coverage**: 190+ country models maintainable
- **Consistent Quality**: Systematic validation and quality checks
- **Scalable Delivery**: Professional models available at sustainable cost

**The automation is not the value proposition - it's what makes the curated data sustainable.** These models could have been created by hundreds of researchers (like OSeMOSYS Global). What matters to users is: **professionally curated, validated, ready to use.**

---

## 📖 **Documentation**

### **Country-Specific Documentation**
Each model branch includes a detailed README with:
- Base year calibration results
- Power plant inventory and thresholds
- Grid topology statistics
- Renewable zone clustering
- Timeslice design justification
- Scenario trajectory charts

### **General Documentation**
- **Methodology Guide**: Complete processing methodology (coming soon)
- **VEDA Integration**: Using VerveStacks models in VEDA-TIMES (coming soon)
- **Customization Guide**: Adding policies and technologies (coming soon)
- **Validation Framework**: Quality assurance procedures (coming soon)

---

## 🤝 **Community & Contributions**

### **How to Contribute**

VerveStacks grows through **application-focused** community engagement:

- **Share Use Cases**: Document how you applied models in real policy contexts
- **Validation Feedback**: Report discrepancies with local data or knowledge
- **Country Requests**: Suggest priority countries for new models
- **Documentation**: Improve guides for model application and interpretation
- **Impact Stories**: Share how VerveStacks influenced decisions or analysis

### **Custom Models**

Need a model variant with specific assumptions or features?

```bash
# Standard models: Clone freely
git clone -b vervestacks-<ISO> https://github.com/your-org/vervestacks-models.git

# Custom variants: Request generation
# Email: requests@vervestacks.org
# We can generate models with your specific requirements
```

---

## 📞 **Contact**

- **🌐 Website**: [vervestacks.cloud](https://vervestacks.cloud)
- **📧 Email**: info@vervestacks.org  
- **📖 Documentation**: [docs.vervestacks.org](https://docs.vervestacks.org)

---

## 📄 **License**

VerveStacks models are freely available for:
- Academic research and publication
- Policy analysis and planning
- Educational and training purposes
- Non-commercial applications

**Attribution Required**: Please cite VerveStacks in publications and policy documents that use these models.

Commercial applications are welcome - contact us for formal licensing if needed for your organizational requirements.

---

**VerveStacks: Start with validated models. Focus on analysis. Make better decisions.**

*"Shifting expertise from model building to model application"*

---

*Copyright © 2025 VerveStacks*
