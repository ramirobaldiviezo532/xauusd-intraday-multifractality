# Workbook paths and output-field conventions

The Colab notebook writes its output workbooks under the stage subdirectories listed in the [repository README](../README.md). The eight workbooks in `outputs/` are fixed archived results produced with an earlier notebook revision, not freshly executed files.

## Selected cross-version field names

| Context / output | Archived field name |
| --- | --- |
| Base MF-DFA scale diagnostics | `N_escalas` |
| Base PELT sensitivity | `Multiplicador_penalizacion` |
| Base Yang–Zhang multiday estimates | `Yang_Zhang_MultiDia_22d` |
| Stage 6 decision tables | `Cumple` |

These exact column labels are needed when locating fields in the original workbooks. They do not represent a complete data dictionary. Stage 6B has `Summary`, `Replications` and `Parameters` worksheets; its replication design comprises four models, two horizons (30 and 60 days), and 30 replicates per combination (240 rows before any separate sheet-level organization).

The notebook's recorded source descriptors are `Dukascopy` (quote origin) and the literal exported clock label `EST+07`. In the archived base results, `XAUUSD data provider` and `Source time zone` were written as `PENDING_DOCUMENTATION`; they were documented subsequently. New execution of the current notebook can write the later descriptors rather than the historical placeholders.

The input names and columns are specified in [`../data/README.md`](../data/README.md). This schema guidance can help reconcile filenames, paths, column labels and descriptive metadata, but **schema agreement is not numerical replication**: identical headings do not prove the same underlying input bytes, stochastic sequences, environment or calculations. No claim of numerical identity from a new full run is implied.
