# 03 · Results

Every number carries its claim ID in [the ledger](CLAIM_LEDGER.md).

## Diagnosis

- **A permit register is not a route register.** 614 permits → 157 corridors; 156 retained (99.4 %). Of
  the apparent 71.1 % row reduction, 71.0 points are the change of unit (CL-01–08).
- **Straight-line catchments overstate who is served** by a median 37.4 % per route (IQR 30.5–41.7 %);
  network-wide 31.9 %, cutting coverage from 35.5 % to **24.2 %** of 6,584,762 residents (CL-26–28). The
  network catchment is an upper bound on the true walkshed, so 37.4 % is a lower bound on the bias.
- **Modelled run time is too fast.** Plan one-way time is a median 0.51 of observed; the per-km cap binds
  on 169 of 186 routes and sits below real pace (4.62 min/km observed vs a 4.0 urban cap) (CL-15–17, 31–32).

## The plan

- **186 routes** (32 trunk, 154 feeder), **1,011 buses** (+68.5 % on ~600) (CL-06, CL-36). Per 100,000
  residents: 15.4 on the division, 63.5 on the network-served population — above the MoHUA 40–60 band
  (CL-60).
- **Frequent service is scarce**: 10.4 % of residents are near a ≤15-min service, 12.2 % ≤20 min (CL-42).
- **Gaps are clustered** (Moran's I 0.66), so a few new corridors could close them (CL-43).
- **The hierarchy is recoverable from the data** (k = 3 by both elbow rules), but agrees with the
  engine's published bands on only 68.3 % of routes; 20 high-priority routes fall in the bottom objective
  tier (CL-37–39).

## Uncertainty (figures 9, 9b)

| | Median | 90 % interval |
|---|---|---|
| Fleet, as specified | 1,013 | 989–1,058 |
| **Fleet, observed urban/peri-urban pace** | **1,182** | **1,130–1,266** |
| Coverage (walk radius uncertain) | 26.7 % | 22.1–32.2 % |
| Tier agreement | 97.8 % | 94.6–100 % |

The cap absorbs run-time uncertainty (with it on, congestion and dwell move the fleet ≤17 buses; with it
off, up to 956). Sobol': the fleet depends on the spare ratio (0.55) and observed pace (0.45); tiers on the
population weight (0.93); coverage on the walk-radius definition (0.97) (CL-56–58).

## Operations, equity and cost

- **Funding**: 30 % of the fleet reaches 92 % of the plan's coverage (CL-61).
- **Scenarios**: observed pace +15.6 % buses; flat 35-min rural headway +9.4 %; all-urban 15-min +15.9 %
  (raises ≤15-min coverage to 14.5 %); aggressive consolidation −47 % buses but −3.9 points coverage (CL-52).
- **Equity**: accessibility Gini 0.903 (0.599 among the served); 32 via-routings suppressed; **13,087
  residents lose bus access** (CL-44–45).
- **Transfers**: 66 of 68 consolidated O–D pairs keep a one-seat ride; 7.4 % wait longer (CL-46).
- **Load**: day-one ~8 boardings per e-bus trip vs 19–37 today; ridership must grow 2.2–4.5× (CL-50).
- **Deadhead**: 0–5.5 % of bus-km, bounded (no depot register) (CL-49).
- **Cost & CO₂** (provisional constants): ₹206–1,054 crore/yr, 21–103 kt CO₂/yr depending on basis (CL-51).
