# Data licence and terms

The **code** in this repository is licensed under the [GNU GPL v3.0](LICENSE). Data are licensed
separately, by source, as below. When a derived file combines sources, the most restrictive terms of its
inputs apply (in practice, ODbL share-alike for anything built from OpenStreetMap or Microsoft
footprints).

## Data produced by this project

| What | Where | Licence |
|---|---|---|
| The rationalised route plan (routes, headways, fleet, timetables, stops register) | `plan/`, `data/raw/Rationalised_Routes_*`, `data/raw/Kashmir_Stops_Master_v4.csv` | **CC BY 4.0**; route geometries derived from OpenStreetMap are also subject to **ODbL 1.0** |
| Module outputs, tables and figures | `data/derived/`, `results/` | **CC BY 4.0** (ODbL where derived from OSM / Microsoft footprints) |
| Aggregate GPS summaries (corridor speeds, dwell, route evidence) | `data/raw/gps/`, `ground-truth/outputs/` | **CC BY 4.0** |

Attribution: *Bus Sathi research team (2026), github.com/Princu-Babu/Bus-sathi*.

## Third-party data

| Source | Files | Terms |
|---|---|---|
| OpenStreetMap contributors | boundaries, POIs, walk graph, OSM buildings | [ODbL 1.0](https://opendatacommons.org/licenses/odbl/) — "© OpenStreetMap contributors" |
| Microsoft Global ML Building Footprints | `data/cache/ms_buildings_kashmir.csv.gz` (centroids + areas, clipped) | [ODbL 1.0](https://github.com/microsoft/GlobalMLBuildingFootprints) |
| WorldPop 2026 (constrained, UN-adjusted, 100 m) | `data/raw/kashmir_worldpop.tif` | [CC BY 4.0](https://www.worldpop.org/) — WorldPop, University of Southampton |
| Census of India 2011 | `census2011_kashmir_districts.csv`, peer-city populations | Open government data |
| ASRTU *SRTU Fleet Handbook 2024* | `peer_cities.csv` (city fleet column) | Public document; cited, not relicensed |
| J&K stage-carriage permit register | `existing-routes.csv` | Public regulatory record, digitised and geocoded by the project |
| SSCL / CHALO e-bus operations | `chalo_ridership.csv`, `chalo_deployed_buses.csv`, `Hourly_Passenger_Count.csv` | Monthly/hourly **aggregates** as provided to the project; redistributed for reproducibility only. They carry no personal data. If the data owner asks, they will be withdrawn and replaced by the derived outputs. |

## Personal data

Raw driver GPS from the Bus Sathi app is personal data and is **never** published here or in any
companion repository. The only per-driver table the analysis uses (daily service minutes) is released in
de-identified form: identifiers, dates and distances removed, rows shuffled
([`tools/deidentify_driver_days.py`](tools/deidentify_driver_days.py)). Analysis results are identical
with either form.

Questions about data use: open an issue.
