# Output file and field alignment

The published notebook expects three external input CSVs (`OHLCV15MIN.csv`, `DTWEXBGS.csv`, `VIXCLS.csv`) and writes the eight workbooks at the paths listed in the main `README.md`.

**Verified output naming:** all eight workbook basenames and their relative stage directories occur in the notebook code. The output files are the supplied completed Excel workbooks copied without editing their contents. The `sha256sum` manifest protects the precise published bytes.

**Field-label corrections retained in the definitive notebook:**

| Workbook or analysis | Aligned field label |
|---|---|
| MF-DFA export | `N_escalas` |
| Base PELT multispecification tables | `Multiplicador_penalizacion` |
| Base Yang–Zhang multiday robustness | `Yang_Zhang_MultiDia_22d` |
| Stage 6 decision table | `Cumple` |

These labels were checked against the corresponding Excel column headers. The Stage 6B `Summary`, `Replications`, and `Parameters` sheets were also inspected; its `Parameters` sheet and 240 records match the module configuration.

The two data-provenance defaults in the public notebook are `DATA_VENDOR = "Dukascopy"` and `SOURCE_TIMEZONE = "EST+07"`. The notebook retains a validation branch for the literal `PENDING_DOCUMENTATION`, but it is not its default value.

**External input note:** the raw input CSV files are not bundled. The required filenames and declared CSV field requirements are listed in `data/README.md`; the full contents of those absent CSVs cannot be checked from this repository alone.
