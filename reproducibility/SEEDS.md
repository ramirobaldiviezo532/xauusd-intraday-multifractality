# Seed strategy

- Base pipeline random seed: `42` (as recorded in original base statistical outputs).
- Stage 5 uses a dedicated fixed seed: `20260911`.
- Stages 6–8 include deterministic seed derivation based on base seed, labels, frequency, mechanism, trial/candidate identifiers, and stable hashes; the exact derivations remain in the single Colab notebook.
- Stage 8 ran 199 retained surrogate/model replicates per mechanism × frequency; Stage 7C used rejection sampling and had effective accepted counts below some nominal targets. A scheduled candidate identifier is **not** necessarily an accepted replicate.

The public notebook contains the deterministic seed-derivation procedures for the reported analyses. The recorded base and Stage 5 seeds are given above, with the stage-specific seed logic preserved in the code.
