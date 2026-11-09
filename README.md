# Intraday multifractality in XAUUSD

Research code, documented inputs and archived results associated with *Temporal organization of intraday multifractality in XAUUSD: surrogates, temporal ablations, and conditional volatility models* (Baldiviezo Romero, 2026).

The study investigates the temporal organization of scaling statistics in 15-minute XAUUSD returns (2003–2026), with a 30-minute analysis for comparison. It uses DFA/MF-DFA, surrogate constructions, temporal ablations, conditional-volatility benchmarks, and secondary analyses of jump-related event windows. Comparisons among the tested mechanisms do not, by themselves, identify a unique causal mechanism.

## Repository contents

The executable analysis is in [`notebooks/XAUUSD_COLAB_ALL_STAGES.ipynb`](notebooks/XAUUSD_COLAB_ALL_STAGES.ipynb). When run in Google Colab, its cells write Python modules for the base analysis and Stages 1–8, including Stages 6B, 7B and 7C. The notebook has 14 code cells and two Markdown cells; it contains no saved execution outputs.

| Analysis | Archived workbook |
| --- | --- |
| Base statistics, DFA and MF-DFA | [`outputs/statistical_results.xlsx`](outputs/statistical_results.xlsx) |
| Stage 5: jump/event study | [`outputs/stage5_mechanism_v3_results.xlsx`](outputs/stage5_mechanism_v3_results.xlsx) |
| Stage 6: calibration of D_H | [`outputs/stage6/stage6_dh_calibration_results.xlsx`](outputs/stage6/stage6_dh_calibration_results.xlsx) |
| Stage 6B: overlapping windows | [`outputs/stage6/stage6b_rolling_overlap_results.xlsx`](outputs/stage6/stage6b_rolling_overlap_results.xlsx) |
| Stage 7: structural discrimination | [`outputs/stage7/stage7_structural_discrimination_results.xlsx`](outputs/stage7/stage7_structural_discrimination_results.xlsx) |
| Stage 7B: jump-regime comparisons | [`outputs/stage7b/stage7b_jump_regime_results.xlsx`](outputs/stage7b/stage7b_jump_regime_results.xlsx) |
| Stage 7C: GARCH-t with BNS-anchored jumps | [`outputs/stage7c/stage7c_garcht_jump_results.xlsx`](outputs/stage7c/stage7c_garcht_jump_results.xlsx) |
| Stage 8: temporal ablations and benchmark models | [`outputs/stage8/stage8_temporal_ablation_results.xlsx`](outputs/stage8/stage8_temporal_ablation_results.xlsx) |

The eight workbooks are archived numerical outputs, not files generated during verification of this documentation. They were produced with an earlier notebook revision. Some field labels and data-provenance defaults differ between the archived outputs and the current notebook; see [`reproducibility/SCHEMA_ALIGNMENT.md`](reproducibility/SCHEMA_ALIGNMENT.md).

## Inputs and execution

Three source CSV files are required: `OHLCV15MIN.csv` (XAUUSD OHLCV), `DTWEXBGS.csv` (U.S. dollar index), and `VIXCLS.csv` (VIX). They are **not included**. Consult [`data/README.md`](data/README.md) for their providers, formats, timestamp conventions, study cutoff, reported input hashes and limitations of fresh downloads. The optional economic calendar was not supplied for the archived run.

1. Obtain the source files through channels and under terms applicable to your use. Preserve an acquisition log, timestamps, gaps and file checksums. Obtaining equivalent data is not the same as obtaining the identical historical input export.
2. Open the notebook in a Google Colab CPU runtime. Configure `DATA_FOLDER` or use the notebook's file-upload prompt. Configure `DRIVE_OUTPUT_DIR` to an output location separate from these archived workbooks.
3. Execute cells in their displayed order, following the notebook's runtime checks and dependency installation. A complete run can require considerable computation. A fresh run can have different software versions, data revisions or outputs.
4. Compare resulting tables and diagnostic values with the archived workbooks; do not infer numerical equivalence solely from matching filenames or column names.

The software-version record and its limitations are in [`reproducibility/ENVIRONMENT.md`](reproducibility/ENVIRONMENT.md). Random seed rules are in [`reproducibility/SEEDS.md`](reproducibility/SEEDS.md).

## Artifact checks

From the directory containing this README, check the recorded SHA-256 digest for the notebook and all eight result workbooks:

```bash
sha256sum -c manifest_sha256.txt
# or, with Python on Windows/macOS/Linux:
python reproducibility/verify_manifest.py
```

The manifest establishes the integrity of these **nine archived files as distributed**. It does not establish that the provided notebook reproduces all numbers from the unavailable historical input CSV files. See [`reproducibility/ARTIFACT_INTEGRITY.md`](reproducibility/ARTIFACT_INTEGRITY.md).

## Data provenance and rights

XAUUSD source quotes were recorded as Dukascopy CFD market data and exported through StrategyQuant Data Manager as closed 15-minute OHLCV bars. The literal source-clock label `EST+07` is preserved, without converting it into an assumed UTC offset. The additional `DTWEXBGS` and `VIXCLS` series come from FRED; VIX is attributed to Cboe. Raw quotes, FRED snapshots and the historical export pipeline logs are not supplied.

The `LICENSE` file grants MIT rights to original repository code and associated original documentation only. It does **not** license third-party input data. Numeric workbooks may include aggregate statistics and series-derived quantities with different redistribution implications. Rights for sharing such derived material, and for any previously deposited copies, should be evaluated against the applicable source terms and permissions before further public distribution. See [`data/README.md`](data/README.md).

## Citation and archived versions

- **Archived v1.0.0 (2026-11-05):** [GitHub release](https://github.com/ramirobaldiviezo532/xauusd-intraday-multifractality/releases/tag/v1.0.0), commit `b211531df4b6539c2715cea12ba013b94f3592cc`, and Zenodo version DOI [10.5281/zenodo.23970440](https://doi.org/10.5281/zenodo.23970440). The Zenodo v1.0.0 archive has been checked against the release archive by MD5 and individual files.
- **All versions:** Zenodo concept DOI [10.5281/zenodo.23970439](https://doi.org/10.5281/zenodo.23970439) resolves to the most recent archived version. It is not the DOI of a specific software version.
- **v1.0.1:** documentation/provenance refresh, with the eight archived XLSX files unchanged and no claimed new numerical run; see [`CHANGELOG.md`](CHANGELOG.md). When Zenodo archives a newly published GitHub release it assigns a **new version-specific DOI**. Consult its version record before citing it; no unissued DOI is asserted here.

For reproducible citations of an exact software snapshot, prefer the version-specific Zenodo DOI and the corresponding GitHub release/tag. The release archives a research software snapshot and its historical results; checksum agreement does not demonstrate a complete rerun from the original, unavailable input CSV files.
