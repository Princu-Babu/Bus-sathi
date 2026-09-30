# Convenience targets. Every target is a thin wrapper around a documented
# command, so Windows users can run the command directly.

PY ?= python

.PHONY: help setup reproduce figures test list clean

help:
	@echo "setup      install dependencies and fetch Git LFS caches"
	@echo "list       show the 23 analysis modules and their state"
	@echo "reproduce  run every analysis module (uses cached walk graph and catchments)"
	@echo "figures    redraw all figures"
	@echo "test       run the test suite"

setup:
	git lfs pull
	$(PY) -m pip install -r requirements.txt

list:
	$(PY) analysis/run_all.py --list

reproduce:
	$(PY) analysis/run_all.py --quick

figures:
	$(PY) analysis/fig_generate_all.py

test:
	$(PY) -m pytest -q

clean:
	rm -rf logs/*.log .pytest_cache analysis/__pycache__
