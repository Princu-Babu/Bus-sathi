# Contributing

Thank you for helping. This repository backs a research paper, so the bar for changes is
**traceability**: every number must come from code that anyone can run.

## Ground rules

1. **A number without a module does not exist.** If you add a result, add the module that produces it
   (`analysis/`), register it in `analysis/run_all.py`, and add a row to
   [`docs/CLAIM_LEDGER.md`](docs/CLAIM_LEDGER.md).
2. **Never edit generated files by hand** — `data/derived/`, `results/figures/`, `results/tables/` are
   written by the pipeline. Change the code and re-run.
3. **No personal data.** Raw GPS, device identifiers or anything that identifies a driver or passenger
   must never be committed. `tests/checkers/test_checker_f_release.py` scans for secrets; run it.
4. **Report results as they come out.** A failed validation channel is a result. Do not tune a threshold
   after seeing the data.
5. **Keep the engine snapshot as run (content unchanged).** `engine/` and `ground-truth/` are the versions that produced the
   published plan. Improvements belong in their development repositories; bring a new snapshot here with
   a version bump.

## Workflow

```bash
git lfs pull
pip install -r requirements.txt
python analysis/run_all.py --quick      # must end "OVERALL STATUS: SUCCESS"
pytest -q                               # must pass
```

Open a pull request against `main` describing what changed and which claims (CL IDs) move. Keep commits
focused; one module or one document per commit is ideal.

## Reporting problems

Use the issue templates: **Bug** (something does not run or reproduce) or **Data question** (provenance,
licensing, or a number you cannot trace). Please include the module name and the log from `logs/`.
