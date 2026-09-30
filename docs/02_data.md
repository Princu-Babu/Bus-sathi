# 02 · Data

Hashes, sizes and upstream paths for every file are in [`data/MANIFEST.md`](../data/MANIFEST.md);
licences in [`DATA_LICENSE.md`](../DATA_LICENSE.md).

| Input | What it is | Used for | Known weakness |
|---|---|---|---|
| Permit register (`existing-routes.csv`) | 614 digitised stage-carriage permits with geocoded origin, destination and via points | the network being rationalised | 80.5 % name-token join to engine rows; vernacular spelling variants |
| WorldPop 2026 (`kashmir_worldpop.tif`) | 100 m constrained, UN-adjusted population | every catchment and coverage figure; denominator 6,584,762 | 4.4 % below the 2011 Census for the same districts; 8 of 10 districts show implausible implied growth |
| OpenStreetMap | boundaries (10 districts, 39 tehsils), 2,431 POIs, 18,533 km walkable network | catchments, opportunities, walk graph | POIs 65 % in Srinagar; volunteer mapping effort |
| OSRM | car routing on the same OSM network | distances and free-flow times | free-flow; understates observed in-motion time (MAPE 65 %) |
| Bus Sathi driver GPS | 43,809 clean runs, ~157 drivers, Feb–Jun 2026 (aggregates only here) | run-time validation, observed pace, duty | self-selected drivers, Srinagar-weighted; no ridership |
| CHALO / SSCL | 12 months of e-bus boardings and trips; per-route deployment; April 2026 hourly boardings | benchmark V2, time-of-day profile, load | not independent of the plan (calibration anchor) |
| Building footprints | OSM closed ways; Microsoft Global ML Building Footprints | validation V1 | WorldPop uses footprints as a covariate (partial circularity) |
| Census of India 2011 | district and city populations | WorldPop check; peer-city regression | 15 years old |
| ASRTU *SRTU Fleet Handbook 2024* | city bus fleets of 36 Indian cities | peer benchmark | public fleets only, whereas the plan is all-operator |
