# Recorded scientific environment

The base statistical workbook records the following software versions:

| Component | Recorded version |
|---|---|
| Python | 3.13.18 (also recorded by Stage 8) |
| NumPy | 2.1.3 |
| pandas | 2.2.3 |
| SciPy | 1.16.3 |
| statsmodels | 0.15.0 |
| ruptures | 1.1.10 |
| joblib | 1.6.0 |

The Colab setup dynamically installs `ruptures`, `openpyxl`, `tabulate`, `joblib`, `scipy`, `statsmodels`, `matplotlib`, `numba` and `psutil` without pinned versions. The notebook records versions in `scientific_environment_lock.json` at runtime and prevents silently mixing checkpoints from different environments.

The Colab notebook records the active environment in `scientific_environment_lock.json` when executed. For maximum numerical reproducibility, use the recorded dependency versions and the same input-data snapshots.
