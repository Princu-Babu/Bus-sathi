# engine — the route-rationalisation engine (v3.4.5-geo)

This is the program that turned 614 stage-carriage permits into the published plan in
[`../plan/`](../plan): 186 active routes, headways, cycle times and a 1,011-bus fleet with its vehicle
mix. It is a **snapshot of the code that produced the plan, unchanged except for line-ending normalisation**
(`kashmir-transit-rationalisation` @ `c8cab92`); development continues in that repository.

> Paths inside several scripts still point at the original workstation layout (e.g. `E:\kash`). They
> are left as run, so the snapshot is an exact provenance record. Adjust them, or set the environment
> variables the scripts read, before running elsewhere.

## Layout

| Path | Role |
|---|---|
| `src/transit_kashmir_v3.py` | The four-phase engine: ingest & geocode → catchments & composite index → consolidation & priority bands → cycle time, fleet, vehicle split, quality gates, exports. |
| `src/route_code_system.py` | Geo-canonical 12-character route codes from point-in-polygon districts and tehsils. |
| `preprocess/` | Geocoding (`geocode_common.py`), gazetteer building and district repair, village recovery, POI extraction from OSM. |
| `postprocess/` | Steps applied after the engine run: v3.4.4 web-verified road distances (`apply_corrections_v344.py`), v3.4.5 GPS-measured cycle times (`apply_reality_v345.py`), v3.4.5-geo geometry redraws (`fix_geometries_v345geo*.py`), CHALO cross-evaluation, timetables. |
| `inputs/` | The permit register, POIs, gazetteer, district/tehsil boundaries. |

## Running it

Requirements: Python ≥ 3.10, `requirements.txt` in this folder, the WorldPop raster
(`../data/raw/kashmir_worldpop.tif` via Git LFS, or `$KASHMIR_WORLDPOP`), and an **OSRM** server with the
India extract on `localhost:5000`:

```bash
docker run -t -v "$PWD:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/india-latest.osm.pbf
docker run -t -v "$PWD:/data" osrm/osrm-backend osrm-partition /data/india-latest.osrm
docker run -t -v "$PWD:/data" osrm/osrm-backend osrm-customize /data/india-latest.osrm
docker run -t -p 5000:5000 -v "$PWD:/data" osrm/osrm-backend osrm-routed --algorithm mld /data/india-latest.osrm

cd inputs && python ../src/transit_kashmir_v3.py
```

Without OSRM the engine falls back to circuity-based times, which changes cycle times; do not compare
such a run with the published plan.

## How the plan is sized — in one paragraph

Each route's one-way time is OSRM free-flow time × a congestion multiplier (2.2 in the Srinagar core,
1.4 elsewhere) + 0.5 min per assumed stop every 500 m + junction penalties; cycle time is 2 × 1.10 ×
one-way, capped at 2 × length × 4.0 / 2.5 / 1.5 min/km for Urban / Peri-Urban / Regional routes. Fleet
= ceil(1.15 × ceil(cycle / headway)), with floors of 2 (urban) and 1 (rural); the e-bus backbone takes the
larger of this and CHALO's current deployment. The analysis in [`../analysis/fleet_model.py`](../analysis/fleet_model.py)
re-implements these rules and reproduces the published cycle time and fleet on all 186 routes — and shows
that the per-km cap, not demand, binds on 169 of them.
