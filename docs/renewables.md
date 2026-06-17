# Renewable Energy Potential — MAR

---

## REZoning Data Foundation

VerveStacks builds on the REZoning database, providing detailed potential assessments at 50×50 km
grid resolution across 190+ countries. This high-resolution spatial data captures nuanced variations
in renewable energy resources critical for accurate energy system modelling.

**Data Sources:**

- **Solar Potential** — REZoning solar resource data with capacity factors and LCOE estimates
- **Wind Onshore** — REZoning onshore wind potential with economic viability assessments
- **Wind Offshore** — REZoning offshore wind resources with marine-specific constraints
- **Hourly Profiles** — Atlite-derived capacity factor time series for each grid cell

---

## Land Use Conflict Resolution

Where solar and wind potential overlaps, VerveStacks applies a conservative LCOE-based allocation:
the less competitive technology receives a reduced share of the overlapping area. This ensures supply
curves represent **deployable potential** rather than theoretical maximums, with no double-counting
across technologies.

*→ [Land-use conflict resolution methodology](https://vervestacks.readthedocs.io/en/latest/methods/renewable-characterization.html#stage-1-land-use-conflict-resolution)*

---

## Supply Curves

The supply curves reveal the economic characteristics of renewable energy deployment as capacity scales:

- **LCOE vs Cumulative Capacity** — Economic viability as deployment grows
- **LCOE vs Cumulative Generation** — Resource potential in energy terms
- **Technology Comparison** — Solar, Wind Onshore, and Wind Offshore side-by-side
- **Original vs Land-use Adjusted** — Impact of conservative overlap management

<div align="center">
  <img src="assets/supply_curves_MAR.svg"
       alt="Renewable Energy Supply Curves" style="max-width:100%;">
</div>

---

## Renewable Energy Clustering

| Technology | Grid Cells | Clusters | Avg Cluster Size | Size Range |
|------------|-----------|---------|-----------------|------------|
| ☀️ **Solar PV** | 204 | 24 | 8.5 cells | 4 to 17 cells |
| 💨 **Wind Onshore** | 173 | 22 | 7.9 cells | 3 to 16 cells |
| 🌊 **Wind Offshore** | 56 | 11 | 5.1 cells | 3 to 10 cells |

**Grid Definition:** Grid definition: kan10

Clustering preserves critical **geographic hedging** effects: spatial variations in wind patterns,
east-west and north-south solar resource differences, and distance-based grid connection costs all
survive the aggregation. Each cluster carries a capacity-weighted hourly profile so higher-potential
cells drive the representative generation shape. Only economically viable grid cells enter the process
(Solar PV > 5% CF, Onshore Wind > 8% CF).

*→ [Clustering algorithm details](https://vervestacks.readthedocs.io/en/latest/methods/renewable-characterization.html#stage-2-renewable-resource-clustering)*

---

### Solar PV Clustering

<div align="center">
  <img src="assets/clustering_results_MAR_solar.png"
       alt="Solar PV Clustering" style="max-width:100%; border:1px solid #ddd; border-radius:8px;">
  <p><em>Solar PV: 24 clusters from 204 grid cells</em></p>
</div>

### Wind Onshore Clustering

<div align="center">
  <img src="assets/clustering_results_MAR_wind_onshore.png"
       alt="Onshore Wind Clustering" style="max-width:100%; border:1px solid #ddd; border-radius:8px;">
  <p><em>Wind Onshore: 22 clusters from 173 grid cells</em></p>
</div>

### Wind Offshore Clustering

<div align="center">
  <img src="assets/clustering_results_MAR_wind_offshore.png"
       alt="Offshore Wind Clustering" style="max-width:100%; border:1px solid #ddd; border-radius:8px;">
  <p><em>Wind Offshore: 11 clusters from 56 grid cells</em></p>
</div>
