# 01 · Methodology

The framework rationalises an inherited permit network into frequency-specified, fleet-sized routes
**without any origin–destination, boarding or fare data**, and then subjects its own plan to independent
tests. It has two halves: the **engine** that builds the plan, and the **analysis** that audits it.

## The engine (how the plan is built)

1. **Diagnose the register.** 614 permits are hashed by undirected endpoints: they describe 157
   corridors (mean 3.9 permits each, up to 42 on Hazratbal–Lal Ded). "Consolidation" is mostly this
   change of unit.
2. **Catchments.** Each route is sampled into virtual stops every 250 m and given a 400 m walk catchment;
   population comes from WorldPop 2026 (100 m), opportunities from 2,431 OpenStreetMap points of interest
   in three importance tiers.
3. **Composite index.** CDI = β · population density + (1 − β) · opportunity density, each min–max
   normalised per km, β = 0.5.
4. **Consolidate.** Routes overlapping by ≥ 0.65 (80 m line buffers) *and* starting within 2.5 km merge
   into their cluster's leading trunk; duplicate permits on an identical corridor collapse to one.
5. **Tier and headway.** Jenks natural breaks on the CDI give high / medium / low priority; headways are
   15 min on the e-bus backbone, 20 on other high-priority routes, 35 on the rest, and demand-responsive
   35–50 min on rural lifelines.
6. **Size the fleet.** Cycle time = 2 × 1.10 × (OSRM time × congestion + dwell + junction penalties),
   capped per km by route class; fleet = ⌈1.15 × ⌈cycle / headway⌉⌉ with minimum floors.

## The analysis (how the plan is tested)

| Question | Method | Module |
|---|---|---|
| Do straight-line catchments bias coverage? | Multi-source Dijkstra on a 962k-node OSM pedestrian graph; catchment = union of residual discs; compared with Euclidean buffers from the same stops | `a02` |
| Is the three-tier hierarchy real? | Goodness of variance fit, k = 2–7, two pre-registered elbow rules; Cohen's κ against quantile, k-means, equal-interval | `a04` |
| Does the index depend on its weights? | Equal, Shannon-entropy and first-principal-component weights | `a03` |
| How wrong is modelled run time? | 43,809 driver-GPS runs; run-time model decomposed into moving speed, dwell, length and cap | `v04` |
| How much of the fleet is assumption? | One-at-a-time sweeps of 11 parameters (cap on / off); 5,000-draw Monte Carlo and Sobol' indices (15,360 evaluations), with an observed-pace regime from GPS | `a08`, `a09` |
| Who is served, how often, and who loses? | Frequent-network coverage; Moran's I on the uncovered surface; population-weighted accessibility Gini; named losers of consolidation; transfer counts | `a11`, `a12`, `a13` |
| What would the alternatives cost? | Five one-lever scenarios, a frequency–fleet frontier, and greedy funding-constrained sequencing | `a15` |
| Is the population surface plausible? Is the plan consistent with the one operator that publishes data? | Building footprints (OSM, Microsoft); CHALO fleet scaled to the plan's headway | `v01`, `v02` |

A verified re-implementation of the engine's sizing rules ([`analysis/fleet_model.py`](../analysis/fleet_model.py))
reproduces the published cycle time and fleet on all 186 routes before any of it is perturbed.

The claim this design supports is **decision-robustness** — which decisions survive plausible parameter,
speed and data variation — never validation against demand.
