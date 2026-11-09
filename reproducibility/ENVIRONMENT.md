# Recorded environment and chronology

The following software versions are **reported in the archived base statistical workbook**; Python 3.13.18 is also recorded in the Stage 8 results.

| Component | Reported version |
| --- | --- |
| Python | `3.13.18` |
| NumPy | `2.1.3` |
| pandas | `2.2.3` |
| SciPy | `1.16.3` |
| statsmodels | `0.15.0` |
| ruptures | `1.1.10` |
| joblib | `1.6.0` |

The notebook also installs or imports `openpyxl`, `tabulate`, `matplotlib`, `numba` and `psutil`, without a fixed version for each. [`requirements-recorded.txt`](requirements-recorded.txt) is a partial transcription of the reported versions, **not** a complete lockfile, historical `pip freeze`, container image or guarantee that the environment can be reconstructed exactly.

## Workbook metadata dates

The `docProps/core.xml` metadata of the **seven** base/Stage 5/6/6B/7/7B/7C workbooks records creation or modification on **2026-11-01 UTC**. The Stage 8 workbook records **2026-11-02 UTC**. These are file metadata timestamps, not authenticated execution-start timestamps and not evidence of an independent re-run. Python 3.13.18 was released on [2026-10-25](https://www.python.org/downloads/release/python-31318/), so the reported Python version does not conflict with the workbook metadata dates.

Checkpoint/version identifiers containing `2026-09-11` or `2026-09-12` in the notebook are literal software/run-label strings. They must not automatically be interpreted as actual execution dates or as contradictory timestamps. Full historical Colab session logs were not supplied.

## Re-execution limits

The first notebook code cell installs dependencies without complete fixed versions. On fresh execution, versions and upstream data snapshots can change. The notebook records observed installed versions in `scientific_environment_lock.json` and checks the version record when resuming in the same output folder; this protects a particular local run against some environment drift, but does not reconstruct the historical environment from the partial requirements file. Configure a separate output directory to protect the archived workbooks from being overwritten.
