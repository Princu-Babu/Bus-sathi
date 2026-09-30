# 05 · Reproducibility

## Everything, from caches (~8 minutes)

```bash
git lfs pull
pip install -r requirements.txt           # Python 3.14; pinned versions
python analysis/run_all.py --quick
pytest -q
```

`run_all.py` runs each module in its own process, logs to `logs/<module>.log`, verifies that each
declared output exists, and writes a machine-readable summary to `logs/LATEST_RUN.json`. The seed is fixed
(`20260823`), so derived results are identical run to run (only runtime and timestamp fields differ).

## Rebuilding the heavy caches

| Cache | Command | Time | Needs |
|---|---|---|---|
| Pedestrian walk graph | `python analysis/a01_build_walk_graph.py --pbf data/external/india-latest.osm.pbf` | ~9 min | Geofabrik India extract |
| Network catchments | `python analysis/a02_network_catchments.py` | ~70 min | walk graph |
| Catchment grid (W, stop spacing) | `python analysis/a08a_catchment_grid.py` | ~3 h, resumable | walk graph |
| Microsoft footprints | download the tiles listed in `data/external/ms_buildings/kashmir_tiles.csv`, then `python analysis/v01_spatial_crossval.py --re-extract` | ~1 h download | internet |

Each rebuild reproduces the shipped cache exactly (checked: the a08a grid at 400 m matches a02 with zero
error on all 186 routes).

## The engine

Rebuilding the plan itself requires OSRM; see [`engine/README.md`](../engine/README.md). The analysis does
not need it — it starts from the published plan in `data/raw/`.

## Tested

The suite checks exact reproduction of the published plan (cycle time and fleet on all 186 routes), scope
and denominator invariants, absence of superseded figures, honest reporting (e.g. that the V2 failure and
its circularity are recorded), secret scanning, and — with LFS present — a full pipeline run.
