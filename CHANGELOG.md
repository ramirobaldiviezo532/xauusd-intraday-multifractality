# Changes to the research software archive

## v1.0.1 — documentation and provenance update

- Reconcile the public `v1.0.0` archive with the documentation revision, without re-running the scientific analyses.
- Clarify the historical result provenance, environment and reproducibility limits in the README and related documentation.
- Record the two different Zenodo identifiers: the stable all-versions concept DOI `10.5281/zenodo.23970439` and the archived `v1.0.0` version DOI `10.5281/zenodo.23970440`. No DOI for `v1.0.1` is known before Zenodo archives that release.
- Preserve all eight XLSX result workbooks byte-for-byte from `v1.0.0`.
- The notebook's 14 executable code cells have the same functional instructions as `v1.0.0`. The only code-cell difference is three explanatory comment lines in its first code cell; 13 other code cells are byte-identical. The two Markdown cells were revised.
- Refresh `CITATION.cff` version metadata and remove a v1.0.0-only release date/link, which does not describe v1.0.1.
- Retain GitHub's `.gitattributes` file (`* -text`), and exclude the former internal pre-publication status report `ESTADO_PUBLICACION.md` from the proposed public release.

The archive is not a newly validated numerical run. Historical results, source data availability, and data reuse rights remain subject to their documented limitations. Publishing a new snapshot containing derivative data requires a separate rights review.
