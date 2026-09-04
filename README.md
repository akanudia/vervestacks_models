# VerveStacks Energy System Models
**Professional. Pre-Built. Ready to Use.**

[![Models](https://img.shields.io/badge/models-one%20branch%20per%20country-green.svg)](#-get-a-model)
[![Data Sources](https://img.shields.io/badge/data-public%20sources%2C%20fully%20traced-orange.svg)](#data-foundation)
[![License](https://img.shields.io/badge/models-freely%20available-blue.svg)](#license)

[STARTING WITH THE POWER SECTOR]

---

## ⚡ **Get a model**

Every country model is a **branch** of this repository.

```bash
# Switzerland, 10-bus grid
git clone -b CHE_grids_kan10 https://github.com/akanudia/vervestacks_models.git

# Germany, no grid representation
git clone -b DEU https://github.com/akanudia/vervestacks_models.git

# List everything available, without cloning
git ls-remote --heads https://github.com/akanudia/vervestacks_models.git
```

Open the files in Veda-TIMES and run.

**Or run it in your browser, without installing anything.** Fork this repository, sign in to
[Veda Online](https://vedaonline.cloud), point it at your fork, and solve — see
**[Run it in the browser](#run-it-in-the-browser)**.

The `ls-remote` command above is always the current list. See **[Getting Started](#getting-started)**
for the branch naming convention and what each model contains.

---

## 🏗️ **Stay Rooted in the Real System**

**The Traditional Modeling Paradigm:**

You must become rooted in the model:
- Learn model structure and mechanics first
- Understand parameter definitions and relationships
- Build mental models of abstract constructs
- Translate real-world knowledge into model language
- **Cognitive load from mechanics dominates**

Then try to connect it to reality you already know.

**The VerveStacks Paradigm:**

You stay rooted in the real system you already understand:
- Start with domain knowledge (you know your country's energy system)
- Validate the model with your knowledge (does it match reality?)
- Explore scenarios using real-world questions (what if we phase out coal?)
- **Cognitive load from mechanics is near zero**

The model serves you, not the other way around.

**Why This Matters:**

Domain experts, policy makers, and analysts should think about **energy systems**, not **model mechanics**. VerveStacks makes the model invisible - you engage with power plants, transmission lines, renewable zones, and policy scenarios, not with abstract parameters and equations.

**The result:** Your expertise in the real energy system becomes immediately applicable, without requiring months of model training.

---

## 📌 **Current Scope**

VerveStacks delivers **power and heat sector models** with integrated:

- **Grid infrastructure** — real transmission topology, at a spatial resolution you choose
- **CO₂ capture, transport and storage** — industrial emitters, pipelines and geological sinks modeled as a routed network *(where curated grid data supports it)*
- **Heat and cogeneration** — bus-local heat demand, CHP, heat-only boilers and heat pumps
- **Utility-scale storage** — 4-hour and 8-hour batteries with duration-correct capacity credit
- **Electric vehicle charging demand** (transport electrification)
- **Hydrogen production** (electrolysis and other pathways)
- **Data centre siting** — candidate transmission buses scored and pre-selected for new load

**Full Energy System Operating Models (ESOM)** covering all sectors (industry, buildings, transport, agriculture) are on the development roadmap. The current power and heat focus provides the foundation.

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

## 📊 **What You Get: Curated, Structured Data**

Each country model includes professionally curated data structured for immediate use in VEDA/TIMES:

### **Existing Power Generation Fleet**
- **Individual Plant Detail**: Units >10-200 MW threshold with actual specifications
- **Geographic Precision**: GPS coordinates with grid location assignment
- **Technical Parameters**: Vintage-based efficiency, capacity factors, commissioning years
- **Calibrated Reality**: 2022 capacity/generation matching IRENA/EMBER statistics

### **Grid Infrastructure** (where available)
- **Transmission Network**: Actual topology from OpenStreetMap data
- **Readable Node Names**: Buses named for the cities they serve (`e_Warsaw_POL`), not OSM identifiers
- **Spatial Regions**: Mathematically consistent clustering (4-400+ regions)
- **Load Distribution**: Industrial demand mapped to transmission buses
- **Renewable Zones**: 50×50km grid cells with location-specific capacity factors

### **CO₂ Networks** *(where curated grid data supports it)*
- **Industrial Emitters**: Cement, lime, fertiliser, chemicals, glass and non-ferrous sources located at named buses
- **Transport Pipelines**: Bus-to-sink links with levelised $/t costs derived from real distances
- **Geological Sinks**: Storage sites with cumulative injection ceilings, not an unbounded sink
- **Plant Retrofits**: Per-unit CCS retrofit options with capacity penalty and capture economics

### **Heat & Cogeneration**
- **Bus-Local Heat Demand**: Heat commodities alongside electricity at each node
- **Cogeneration**: CHP units with heat-to-power ratios from plant-level data
- **Heat Supply Options**: Heat-only boilers, electric boilers and utility-scale heat pumps

### **Renewable Energy Potential**
- **Supply Curves**: Technology-specific LCOE vs. capacity curves
- **Hourly Profiles**: 8760-hour generation patterns by cluster
- **Conservative Estimates**: Land-use constraints and overlap resolution
- **Quality Filtering**: Only economically viable resources included

### **Temporal Modeling**
- **Intelligent Timeslices**: 1-600 timeslices capturing critical periods
- **Stress Period Identification**: Scarcity, surplus, and volatility analysis
- **Flexible Resolution**: From simple seasonal to detailed hourly representation
- **Capacity Credit**: Per-cluster firmness coefficients splitting variable output into firm, 4-hour and 8-hour storable, and irreducible surplus

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
- **Per-Model Documentation Site**: Every model ships a browsable site covering calibration, grid, renewables, hydro, timeslices and scenarios

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

### **🏭 CO₂ as a Routed Network**

**Carbon capture with geography attached**, rather than a national abatement curve:

**The Problem:**
Most models treat CO₂ storage as a single national bucket with a flat cost adder. That hides the two things that actually bind: how far the CO₂ has to travel, and how fast a given formation will accept it.

**The VerveStacks Solution:**

1. **Emitters at Nodes**: Industrial sources — cement, lime, fertiliser, chemicals, glass, non-ferrous — placed at the transmission bus serving them, each with a sector-specific capture cost
2. **Pipelines as Trade Links**: Bus-to-sink connections priced by distance and throughput, so a plant far from storage genuinely pays more
3. **Sinks with Ceilings**: Geological storage sites carry cumulative injection bounds — capacity is finite and site-specific, not an unbounded backstop
4. **Power Plant Capture**: CCS-equipped generation routes its captured stream into the same network, competing for the same pipelines and the same pore space
5. **Retrofit Economics**: Existing units carry explicit retrofit options with auxiliary load penalty and capture cost

**Why This Matters:**
Net-zero pathways usually hinge on how much CCS is affordable and where. Modelling capture, transport and injection as a network makes that answer specific to a country's actual industrial geography — and makes it challengeable, because every cost traces to a distance and every ceiling to a formation.

**Availability:** CO₂ networks appear in models whose curated grid includes emitter and sink data. Coverage is expanding; models without it are otherwise unaffected.

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

Each country has its own branch with a complete, ready-to-use model. Branch names follow
the pattern below:

| Branch pattern | Meaning |
|---|---|
| `<ISO>` | National model, no grid representation |
| `<ISO>_grids_kan<N>` | With an N-bus reduced transmission network |
| `<ISO>_grids_kan` | With a grid at the default resolution |
| `<ISO>_grids_syn_<N>` | Synthetic grid, where open topology data is unavailable |

The bus count is a modelling choice, not a fixed property of the country: the same country
can be published at several resolutions, and a coarser network solves faster while a finer
one represents congestion better. Multi-country models with endogenous cross-border trade
can also be built from these components — [get in touch](#contact) if you need one.

```bash
# Clone any country model
git clone -b CHE_grids_kan10 https://github.com/akanudia/vervestacks_models.git

# List every available model without cloning
git ls-remote --heads https://github.com/akanudia/vervestacks_models.git

# Models are immediately usable in VEDA/TIMES
# - Open .veda files in Veda-TIMES
# - Explore existing scenarios
# - Add your own policy assumptions
# - Run analyses
```

### **Run it in the browser**

You do not need a Windows machine, a Veda desktop install, or a solver licence. A country
model can be taken from this repository to a solved result entirely in a browser:

1. **Fork this repository** and check out the branch for the model you want
2. **Sign in to [Veda Online](https://vedaonline.cloud)**
3. **Give VO access to your fork** with a GitHub Personal Access Token
4. **Create a model** in VO pointing at your fork
5. **Browse the inputs, define cases, and solve**

Results come back into VO, where you can explore them, build scenarios on top, and share a
link to the model with colleagues.

**Free access.** Veda Online provides a free route to running these models. Current
eligibility, compute limits and queueing are documented
[here](https://vedaonline-documentation.readthedocs.io/en/latest/pages/VO_free_academic.html) —
that page is the authority, not this one.

**Start coarse.** A `kan10` model solves quickly and is the right place to confirm that the
model behaves the way your country should. `kan25` and `kan50` represent congestion in more
detail and take longer. Verify first, then move up.

---

### **Explore What's Included**

Every model branch contains:

**The model** — a complete VEDA-TIMES model folder:
- `SysSettings.xlsx` - Regions, time periods, fuels, grids, heat and CO₂ network settings
- `vt_*.xlsx` - Existing stock, new-build options and CCS retrofits
- `Sets-vervestacks.xlsx` - Technology and commodity definitions
- `SubRES_Tmpl/` - New renewables and conventionals, storage, EV, H₂, data centres
- `SuppXLS/` - Base scenario, AR6 climate drivers, timeslice parameter sets, trade links
- `AppData/` - Pre-configured Veda cases, result views and solver options

**The evidence** — everything needed to check it:
- `source_data/` - Complete dataset in model-agnostic Excel format
- `grid_analysis/` - Network topology, bus assignments and an interactive map
- `renewable_energy/` - Supply curves and cluster assignments
- `timeslice_analysis/` - Stress period identification charts
- `README.md` - Country-specific calibration against published statistics
- `docs/` + `mkdocs.yml` - A browsable documentation site for this model

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

Every model is assembled from public data. Nothing in a VerveStacks model comes from a
source a user cannot go and check.

### **The Existing System**

| Dataset | Purpose |
|---|---|
| **[Global Energy Monitor](https://globalenergymonitor.org)** | Unit-level power plant inventory with coordinates, vintages and status |
| **[IRENA Statistics](https://www.irena.org/Statistics)** | Renewable capacity, used as the calibration benchmark |
| **[EMBER](https://ember-energy.org/data/)** | Generation, emissions and cross-border transfer capacity |
| **[UN Statistics Division](https://unstats.un.org/unsd/energystats/)** | National energy balances |

### **Grid**

| Dataset | Purpose |
|---|---|
| **[OpenStreetMap](https://www.openstreetmap.org)** | Transmission topology — substations, lines and voltages |
| **[Global Transmission Database](https://papers.ssrn.com/abstract=4726771)** | Line capacity reference for NTC estimation |
| **[PyPSA-Eur](https://github.com/PyPSA/pypsa-eur)** | Pre-built European network as a cross-check |

### **Renewable Resource**

| Dataset | Purpose |
|---|---|
| **[REZoning](https://www.irena.org/publications/2022/Mar/Renewable-Energy-Zoning-for-Energy-Transition)** | Land-use-screened potential on a 50×50km global grid |
| **[Atlite](https://github.com/PyPSA/atlite)** / **[ERA5](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5)** | Hourly capacity factors per grid cell from reanalysis weather |
| **[Natural Earth](https://www.naturalearthdata.com)** | Land masks and administrative boundaries |

### **Technology Costs**

| Dataset | Purpose |
|---|---|
| **[IEA World Energy Outlook](https://www.iea.org/weo)** | Regional cost levels across nine world regions |
| **[NREL Annual Technology Baseline](https://atb.nrel.gov)** | Cost trajectory shape, storage and SMR |
| **[Danish Energy Agency catalogues](https://ens.dk/en/analyses-and-statistics/technology-data)** | CHP, district heating, heat pumps, storage and capture modules |
| **[Damodaran country risk premia](https://pages.stern.nyu.edu/~adamodar/)** | Country-specific cost of capital |

Every cost value carries its source, publication version, currency year and a checksum of
the originating workbook, so any number in a model can be traced back to the page it
came from.

### **CO₂ Transport & Storage**

| Dataset | Purpose |
|---|---|
| **[OGCI CO₂ Storage Resource Catalogue](https://www.ogci.com/co2-storage-resource-catalogue)** | Geological storage sites and capacity estimates |
| **Basin hydrogeology (published assessments)** | Pressure-limited injection rates, so storage is a flow constraint and not only a stock |
| **Published pipeline cost correlations** | Levelised transport cost by distance and throughput |
| **[IEA CCUS Projects Database](https://www.iea.org/data-and-statistics/data-product/ccus-projects-database)** | Announced project cross-check |

### **Scenarios, Policy & Demand**

| Dataset | Purpose |
|---|---|
| **[IPCC AR6 Scenario Database](https://data.ece.iiasa.ac.at/ar6/)** | Carbon prices and sectoral demand trajectories by climate category |
| **[NGFS Scenarios](https://www.ngfs.net)** | Climate policy and transition-risk pathways |
| **National targets and plans** | Renewable and capacity targets, each carrying its publisher, date and URL |
| **[PeeringDB](https://www.peeringdb.com)** | Interconnection facilities, used as a spatial prior for data centre siting |

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
git clone -b <branch> https://github.com/akanudia/vervestacks_models.git

# Custom variants: Request generation
# Email: requests@vervestacks.org
# We can generate models with your specific requirements
```

---

## 📞 **Contact**

- **🌐 Website**: [vervestacks.cloud](https://vervestacks.cloud)
- **📧 Email**: info@kanors.com  
- **📖 Documentation**: [vervestacks.readthedocs.io](https://vervestacks.readthedocs.io/en/latest/)

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
