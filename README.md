# Intraday XAUUSD multifractality — code and scientific results

This repository accompanies the manuscript *Temporal organization of intraday multifractality in XAUUSD: surrogates, temporal ablations, and conditional volatility models*.

## Scientific code

`notebooks/XAUUSD_COLAB_ALL_STAGES.ipynb` is the **single definitive public scientific notebook**. It generates the modules in a Google Colab session and implements the entire analytical pipeline: configuration and Stages 1–8, including 6B, 7B and 7C. This publication contains no alternative notebook versions or separately maintained stage scripts.

The eight workbooks in `outputs/` preserve the completed scientific results **byte-for-byte**. Their stored filenames, relative output paths, relevant field labels and stage configuration have been checked against the notebook. No Excel workbook was opened and resaved for cosmetic renaming. See `reproducibility/ARTIFACT_INTEGRITY.md` and `reproducibility/SCHEMA_ALIGNMENT.md` for these checks.

## Repository contents

- `notebooks/`: one Colab scientific notebook
- `outputs/`: eight verified Excel files covering the base analysis and Stages 5, 6, 6B, 7, 7B, 7C and 8
- `data/README.md`: authorized input-data acquisition and format requirements
- `reproducibility/`: SHA-256 documentation, software version notes, random seeds and filename/field alignment
- `manifest_sha256.txt`: SHA-256 checksums for the single notebook and eight archived Excel workbooks; documentation files may be edited independently
- `LICENSE`: MIT license for the original code and documentation; not a license to redistribute third-party market data

## Reproduction instructions

1. Open `notebooks/XAUUSD_COLAB_ALL_STAGES.ipynb` in Google Colab with a CPU runtime.
2. Obtain the three input files `OHLCV15MIN.csv`, `DTWEXBGS.csv`, and `VIXCLS.csv` as documented in `data/README.md`, with authorization appropriate to each data source.
3. Set `DATA_FOLDER` to the input directory or follow the notebook's upload prompt. Set `DRIVE_OUTPUT_DIR` to a separate Google Drive directory to avoid overwriting the archived outputs.
4. Execute the notebook cells in sequence. The initialization installs required packages, records the environment and configures checkpoints.
5. Compare the resulting output tables and numerical values using the archived workbooks as reference material.

From the repository root, verify the notebook and Excel workbooks on Linux/macOS (with `sha256sum` available):

```bash
sha256sum -c manifest_sha256.txt
```

On Windows, use `python reproducibility/verify_manifest.py` to verify the same nine files. The input CSV hashes documented in `data/README.md` refer to the original source exports. They are useful for identifying the inputs but depend on the exact file contents and vendor export format.

## Output files

| Stage | Workbook |
|---|---|
| Base analysis | `outputs/statistical_results.xlsx` |
| 5 | `outputs/stage5_mechanism_v3_results.xlsx` |
| 6 | `outputs/stage6/stage6_dh_calibration_results.xlsx` |
| 6B | `outputs/stage6/stage6b_rolling_overlap_results.xlsx` |
| 7 | `outputs/stage7/stage7_structural_discrimination_results.xlsx` |
| 7B | `outputs/stage7b/stage7b_jump_regime_results.xlsx` |
| 7C | `outputs/stage7c/stage7c_garcht_jump_results.xlsx` |
| 8 | `outputs/stage8/stage8_temporal_ablation_results.xlsx` |

Stage 6B includes the `Summary`, `Replications` and `Parameters` sheets, including 240 model–horizon–replicate records (four models × two horizons × 30 replicates).

## Data rights and citation

The notebook's source metadata identify Dukascopy as the recorded XAUUSD quote source and StrategyQuant as the export software. Third-party raw price data and original FRED downloads are not distributed in this package. Read `data/README.md` for provenance and usage conditions. Before public distribution, confirm the redistribution rights applicable to any market-data-derived information within the workbooks.

The repository source URL is recorded in `CITATION.cff`. Add the Zenodo DOI to the manuscript and repository README after the archived release is published. The DOI is not required in `CITATION.cff` for the first release.
