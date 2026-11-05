# Integrity of archived results

The eight output Excel files were copied **byte-for-byte** from the supplied files, only renamed/moved into the output paths used by the single notebook. Their worksheet names, field names, numbers, formula caches, styles, and internal metadata are unchanged.

Checks against the manuscripts' reported SHA-256 values:

- Stage 5: `34bcff45aef2c0a51017dd9c25a1b892733b8b96b3cd1fd1c8c042650a6a97e1` — matches.
- Stage 7C: `b2495f56af85c666abdc0d5f90f0f382ffcdb5da99cdd6b82f90c067b7d0eb68` — matches.
- Stage 8: `3957ca7cfbde60a7050a26d0d6e1e261915864f4e7f657479602319308cd1ebf` — matches.

The two supplied copies of the Stage 6 workbook had identical SHA-256 values; only one was retained. The historical Excel column labels `N_escalas`, `Multiplicador_penalizacion`, `Yang_Zhang_MultiDia_22d`, and `Cumple` were left unchanged; corresponding label strings in the canonical notebook were restored to these values so future exports follow the historical field naming convention. These are metadata/field-label changes, not mathematical changes.

Use the repository root `manifest_sha256.txt` to check all included files; the manifest is created from physical copied files using the system's `sha256sum` utility. The raw input file hashes are historical reported values and cannot be verified without the original CSV files.

## Stage 6B consistency check

- Original uploaded workbook SHA-256: `02a0d3e00a894cf69558f6b28a4b600ca82175afd79f69cf406391b2bea42577`. Copy in `outputs/stage6/` has the identical hash.
- Three sheets: `Summary`, `Replications`, `Parameters`. The latter lists `ROLL_REPS=30`, `ROLL_DAYS=500`, `HORIZONS=(30, 60)`, `DFA_R2_MIN=0.95`, and the four Stage 6B model names.
- All 240 expected `(model, horizon, replicate)` records are present (four models × two horizons × 30 replicates), with replicate identifiers 1–30 in every group.
- The output schema and parameters agree with the published Stage 6B module.
