# 04 · Validation

A plan built without demand data cannot be validated by predicting a withheld ridership series — there
is none. The design is **convergent**: six channels, each biased differently, so that agreement raises
confidence and each disagreement points at a specific weakness. Thresholds were fixed before the results
were seen and are reported pass or fail without adjustment. Machine-readable summary: Table 7 in
[`CLAIM_LEDGER.md`](CLAIM_LEDGER.md).

**Two disclosures first.** (1) The only ridership data (CHALO, on the e-bus backbone) is not independent:
it calibrates a plausibility term and is also benchmark V2. (2) Driver GPS measures vehicles, not people;
it can test the supply chain (geometry → speed → run time → fleet) and nothing about demand.

## V1 · Population surface vs building footprints

Does WorldPop put people where buildings are? Spearman ρ between population and footprint area, target
ρ > 0.60, at the route-catchment scale (n = 186) and on a 1 km grid. WorldPop itself uses footprints as a
covariate, so agreement is partly expected by construction: this is a consistency check.

| Source | Footprints in the division | Route catchments (area) | Route catchments (count) | 1 km grid (all / populated) |
|---|---|---|---|---|
| **Microsoft Global ML Building Footprints** | 1,852,714 | **0.975 pass** | **0.940 pass** | **0.907 / 0.950 pass** |
| OpenStreetMap | 12,343 | 0.657 pass | 0.544 fail | 0.316 / 0.312 fail |

With the near-complete Microsoft layer (99.8 % of residents live in a 1 km cell containing a footprint)
the population surface passes at every scale. OpenStreetMap maps any building in only 4–31 % of populated
cells, depending on district, so its weaker result is a mapping gap rather than a population error
(Tables 6d, 6e; CL-53).

## V2 · Operator benchmark (CHALO) — circular

CHALO runs 98 buses on the 30 backbone routes, about 855 bus-trips a day. Scaled to the plan's 15-minute
headway that is 179–220 buses (13–16 h service day). The plan's backbone fleet is 283: a ratio of
**1.29–1.58 — fails the ±15 % band under every assumption**. Route-level rank agreement is weak
(ρ = 0.22, p = 0.24). (Table 6f, CL-54.)

## V3 · Expert weight elicitation

**Not conducted.** Weights are derived three data-driven ways (equal, entropy, principal component);
V5 shows the population weight governs the tiers, which is where an expert panel would matter most.

## V4 · Driver GPS (supply side)

- **Passes:** 183 of 186 alignments run on roads carrying bus traffic; the 2.2 city-core congestion
  multiplier reproduces observed moving speed to +1.4 %.
- **Fails:** dwell is 1.76 min/km observed vs 1.0 modelled and is fixed layover, not distance-driven;
  plan one-way time is a median 0.51 of observed; the per-km cap binds on 169 routes below real pace.
  (Tables 6a–6c, CL-15–17, 31–35.)

## V5 · Global sensitivity (Sobol')

15,360 evaluations. The fleet as specified depends almost only on the spare ratio (0.94), because the cap
discards run-time parameters; at observed pace, spare ratio 0.55 and observed pace 0.45. Tiers depend on
the index's population weight (0.93); coverage on the walk-radius definition (0.97). (Table 7c, CL-58.)

## V6 · Decision robustness

- **Tiers pass:** 97.8 % agreement with the baseline partition (90 % interval 94.6–100 %) against an
  80 % target; 179 of 186 routes keep their tier in >80 % of draws.
- **Fleet only as a range:** 989–1,058 as specified; **1,130–1,266 at observed pace**, which excludes the
  published 1,011. (Table 7b, CL-56–57.)

## Reading the six together

Geometry, network structure and the service hierarchy survive every channel that can test them. Time
does not: the run-time model is too fast, the cap hides it, and the fleet at observed pace is higher than
published. Demand is untested — the honest ceiling is **decision-robustness of the supply plan**.
