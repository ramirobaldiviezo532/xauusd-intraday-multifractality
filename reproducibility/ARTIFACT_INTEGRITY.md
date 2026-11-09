# Artifact integrity and SHA-256 checks

`manifest_sha256.txt` at the repository root records SHA-256 digests of **nine archived files**: the Colab notebook and eight unchanged Excel result workbooks. These digests are content fingerprints of the distributed bytes, not scientific validation tests.

| Group | Paths included in the manifest |
| --- | --- |
| Notebook | `notebooks/XAUUSD_COLAB_ALL_STAGES.ipynb` |
| Base and Stage 5 | `outputs/statistical_results.xlsx`; `outputs/stage5_mechanism_v3_results.xlsx` |
| Stages 6 and 6B | `outputs/stage6/stage6_dh_calibration_results.xlsx`; `outputs/stage6/stage6b_rolling_overlap_results.xlsx` |
| Stages 7 and 7B | `outputs/stage7/stage7_structural_discrimination_results.xlsx`; `outputs/stage7b/stage7b_jump_regime_results.xlsx` |
| Stages 7C and 8 | `outputs/stage7c/stage7c_garcht_jump_results.xlsx`; `outputs/stage8/stage8_temporal_ablation_results.xlsx` |

From the **repository root**, verify all entries:

```bash
sha256sum -c manifest_sha256.txt
# or without GNU coreutils:
python reproducibility/verify_manifest.py
```

For each line, the utility hashes the existing path and compares the value with its recorded digest; all nine must pass. The manifest deliberately excludes frequently edited Markdown files. To inspect a single digest with Python:

```python
from pathlib import Path
from hashlib import sha256
p = Path('outputs/statistical_results.xlsx')
print(sha256(p.read_bytes()).hexdigest())
```

Any content edit to the notebook or workbook changes its SHA-256 and requires an updated manifest **only after the intended content changes are reviewed**. Saving an Excel file can change internal metadata even if the visible cell values remain unchanged. Altering the manifest alone cannot validate a new run.

The workbook outputs were generated with an earlier notebook revision than the file presented here. Documented differences include labels and source-provenance fields; the actual historical generating notebook, original input CSVs, full environment lock and execution logs are not supplied. A direct comparison with the original Zenodo-linked GitHub `v1.0.0` archive shows that **all eight workbooks are byte-identical** and that the 14 notebook code cells are identical after removing three lines of explanatory Python comments added to the first code cell; the other 13 code cells match exactly. Both notebook Markdown cells were rewritten for presentation/provenance. The notebook SHA-256 therefore differs despite no change in executable instructions between these two distributed copies. This comparison is **not** evidence that either copy precisely reproduces the archived workbooks from original source inputs.

See [`SCHEMA_ALIGNMENT.md`](SCHEMA_ALIGNMENT.md), [`ENVIRONMENT.md`](ENVIRONMENT.md) and [`SEEDS.md`](SEEDS.md). Historical source-file hashes are **reported**, not independently checked: [`historical_input_sha256_reported.txt`](historical_input_sha256_reported.txt).
