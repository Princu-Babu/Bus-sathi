# Changelog

## 1.0.0 — 2026-09-30

First consolidated, citable release.

- **Plan** — v3.4.5-geo: 186 active routes, 1,011 buses (187 HPV / 754 MPV / 70 LPV), 15 of 18 stale
  geometries redrawn from GPS evidence.
- **Engine** — snapshot of `kashmir-transit-rationalisation` at `c8cab92`.
- **Ground truth** — snapshot of `bus-sathi-trace-intelligence` at `03c7fe0` (code and aggregate
  outputs only; no raw GPS).
- **Analysis** — 23 modules from `bus-sathi-paper` at `a4ba64a`, adapted to this layout:
  network catchments, six validation channels (V1–V6), one-at-a-time and Monte Carlo/Sobol' uncertainty,
  scenarios and funding sequencing, equity, transfers, cost and emissions (provisional).
- **V1** re-run with Microsoft Global ML Building Footprints alongside OpenStreetMap.
- **Privacy** — the per-driver duty table is published only in de-identified form; results unchanged.
