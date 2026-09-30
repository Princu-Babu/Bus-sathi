# analysis — reproducing every result

Twenty-three modules, one runner. Each module reads frozen inputs from `data/raw/` (and caches in
`data/cache/`), writes JSON/CSV to `data/derived/` and tables to `results/tables/`, and never touches the
network. Configuration, parameter ranges and the random seed (`20260823`) live in [`common.py`](common.py).

```bash
python analysis/run_all.py --list     # modules, stages, cache state
python analysis/run_all.py --quick    # everything except rebuilding the heavy caches
python analysis/run_all.py --module a09_monte_carlo_sobol
python analysis/fig_generate_all.py   # all figures
```

| Stage | Modules | What they establish |
|---|---|---|
| 0 · Inputs | `q01` data quality · `a01` walk graph* · `a02` network catchments* · `a02b` faithfulness | permits → corridors; WorldPop vs Census; the network walkshed and the 37.4 % Euclidean overstatement |
| 1 · Ground truth | `v04` GPS validation | run time, dwell and the per-km cap against 43,809 GPS runs |
| 2 · Index & tiers | `a03` index weights · `a04` class count | equal / entropy / PCA weights; k = 3 by two elbow rules; agreement with published bands |
| 3 · Evaluation | `a05` time of day · `a06` deadhead · `a07` load · `a10` network · `a11` coverage & Moran's I · `a12` equity & losers · `a13` transfers · `a14` cost & CO₂ · `a15` scenarios & funding · `a16` peer cities | what the plan delivers, to whom, at what cost |
| 4 · Robustness | `a08a` catchment grid* · `a08` one-at-a-time · `a09` Monte Carlo & Sobol' · `v01` buildings · `v02` CHALO | validation channels V1, V2, V5, V6 and the fleet interval |
| 5 · Output | `fig_generate_all` | figures |

\* heavy: `a01` ~9 min (needs `india-latest.osm.pbf` in `data/external/`), `a02` ~70 min, `a08a` ~3 h
(resumable). Their outputs are shipped via Git LFS so `--quick` skips them.

`fleet_model.py` is a verified re-implementation of the engine's cycle-time and fleet rules and of the
tiering rule; it asserts exact reproduction of the published plan before any perturbation is trusted.
