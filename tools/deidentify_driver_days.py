#!/usr/bin/env python
"""
deidentify_driver_days.py — produce the public form of the driver-day table.

The source table (one row per driver per day: hashed driver id, date, runs,
first/last trip time, service minutes, km) is a work-schedule record of named
people once the hash is linked back, so it is not published. Module a13 needs
only the distribution of service minutes and trip times plus three counts.
This script keeps exactly that:

  * drops `driver`, `day`, `km`, `span_min`, `util`;
  * shuffles rows with a fixed seed so row order carries no information;
  * writes the three counts a13 needs to a sidecar JSON.

a13 produces byte-identical results from either form (checked in
tests/unit/test_new_modules.py when the private table is present).

Usage
    python tools/deidentify_driver_days.py path/to/driver_days.csv data/raw/gps/
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

KEEP = ["n_runs", "service_min", "first_start", "last_end"]
SEED = 20260823


def main(src: str, out_dir: str) -> None:
    dd = pd.read_csv(src)
    out = Path(out_dir)
    pub = dd[KEEP].sample(frac=1.0, random_state=SEED).reset_index(drop=True)
    pub.to_csv(out / "driver_days_deidentified.csv", index=False)
    meta = dict(n_driver_days=int(len(dd)), n_drivers=int(dd["driver"].nunique()),
                n_calendar_days=int(dd["day"].nunique()),
                window="February-June 2026",
                note="Driver identifiers, dates, km and span removed; rows shuffled (seed 20260823).")
    (out / "driver_days_deidentified.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"wrote {len(pub)} de-identified rows; {meta}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
