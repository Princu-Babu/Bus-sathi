# ground-truth — what buses actually do (Bus Sathi driver GPS)

The engine plans from paper permits. This pipeline measures the road: it turns ~5-second GPS pings from
the Bus Sathi driver app (**~157 drivers, 1,213 sessions, February–June 2026**) into clean service runs,
corridors, speeds, dwell times and route evidence. Snapshot of `bus-sathi-trace-intelligence` @
`03c7fe0`.

## What it can and cannot say

- **Can:** which planned alignments buses really drive; moving speed and dwell on observed corridors;
  where the plan's run-time model is wrong. These feed validation channel V4 and the observed-pace
  scenario of the uncertainty analysis.
- **Cannot:** demand, ridership or true frequency. App adoption is partial and Srinagar-concentrated, so
  an unobserved route is not a dormant route.

## Privacy

Raw traces are personal data and are **not** in this repository (they live in the app's Firestore and
are read with a service-account key that is never committed). Everything here is aggregated:

| Path | What |
|---|---|
| `src/` | The pipeline: pull → segment runs → match to routes → corridors → speeds, stops, evidence → exports. |
| `outputs/corridor_verdicts/` | Per-corridor analyst verdicts (Markdown + JSON) for the 18 observed corridors. |
| `outputs/corridors_verdicts.geojson` | Corridor lines with verdicts. |
| `outputs/corridor_queue.csv` | Runs and distinct drivers per corridor (counts only). |
| `../data/raw/gps/` | The aggregate tables the analysis consumes (corridor profiles, reality check, route evidence, a de-identified duty table). |

## Running it

Requires the Firestore service-account key in `secrets/serviceAccount.json` (not distributed) and
`requirements.txt`. The scripts carry their original workstation paths; see the engine README note.
