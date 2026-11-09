# Deterministic random-state conventions

The notebook declares `RANDOM_SEED = 42` for the base analysis and `STAGE5_SEED = 20260911` for Stage 5. These are integer initializers, not provenance timestamps.

Other stages use stable offsets derived from the base seed:

| Stage | Definition in notebook | Base value |
| --- | --- | --- |
| 6 | `RANDOM_SEED + 600_000` | `600042` |
| 6B | `RANDOM_SEED + 1_600_000` | `1600042` |
| 7 | `RANDOM_SEED + 700_000` | `700042` |
| 7B | `RANDOM_SEED + 770_000` | `770042` |
| 7C | `RANDOM_SEED + 780_000` | `780042` |
| 8 | `RANDOM_SEED + 880_000` | `880042` |

Offsets are combined with stage-specific inputs rather than consumed as a single universal seed. The implementation must be consulted for each analysis. Examples verified against the notebook code:

- The base shuffled MF-DFA draws use `RANDOM_SEED + 10_000 + i`, and IAAFT draws use `RANDOM_SEED + 100_000 + i`.
- Stage 6B initializes each replicate with `SEED + rep * 100 + (int(SHA256(model UTF-8)[:6], 16) % 100)`, where `SHA256` denotes its hexadecimal digest and `rep` is the loop identifier.
- Stage 8 identifies mechanisms by stable strings, combines its base with frequency and replicate index, and uses `RNG_BASE + freq * 1_000_000 + _stable_int(mech) + i`. Here `_stable_int(mech) = int(SHA256(mech UTF-8)[:12], 16) % 1_000_000_007`, and the stored `Replicate` equals `i + 1`.

The default Stage 8 target is **199 replicates per mechanism–frequency combination** (`XAUUSD_STAGE8_REPS` can override this on a new run). The code computes candidate draws deterministically by index, but candidate generation does not guarantee an accepted/valid result. In particular, Stages 7/7B/7C apply validity or rejection logic: the planned candidate count and number of **accepted** library members are separate quantities. Stage 7C's `Library_Diagnostics` workbook sheet records the accepted `N` by frequency, window and role; it should not be replaced by the nominal target. Checkpoint state, input variation, dependencies and filters may affect a re-execution.

This documentation describes code-visible seed derivations. It is not evidence that a fresh full execution recreates the historical scientific results. Historical workbook-specific parameters are archived in the original workbooks.
