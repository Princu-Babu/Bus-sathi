# data

| Folder | Contents | Written by |
|---|---|---|
| `raw/` | Frozen inputs: the plan, the permit register, POIs, boundaries, WorldPop (LFS), Census, CHALO aggregates, peer cities, aggregate GPS tables | staged once; hashes in [`MANIFEST.md`](MANIFEST.md) |
| `derived/` | Every module's JSON/CSV output — the only source a reported number may come from | `analysis/` |
| `cache/` | Expensive intermediates via Git LFS: pedestrian walk graph, network catchments, OSRM responses, clipped building footprints, the a08a grid checkpoint | `a01`, `a02`, `a08a`, `v01` |
| `external/` | Download manifests (Microsoft building-footprint tiles for the study area); the downloads themselves are not committed | `v01` |

Licensing per source: [`../DATA_LICENSE.md`](../DATA_LICENSE.md). After cloning, run `git lfs pull` to
replace LFS pointer files with the real caches.
