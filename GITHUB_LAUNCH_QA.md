# GitHub launch QA — 21 November 2026

**Research version:** 1.0.0 · **Zenodo record:** https://doi.org/10.5281/zenodo.24417028 · **YouTube explainer:** https://www.youtube.com/watch?v=ewEHGMFizdo

This report records locally performed publication engineering tests. It does **not** claim independently peer-reviewed scholarship, proof of safe agent execution, an external security assessment, copyright certification, or completed live GitHub Actions/README rendering.

## Verification scope

- All **54 original research-release files** were compared against the initial author-supplied release archive; **44 are byte-identical**, and ten publication/citation/integrity/landing-page files were intentionally updated for the separate GitHub companion. The original PDF, research manuscript HTML/Markdown, original case datasets, tests and gate code are unchanged.
- The original manuscript PDF is unchanged (69 pages) and corresponds to the deposited edition dated 11 November 2026. The public Zenodo date is 21 November 2026; the user supplied the published DOI.
- Locally re-executed 39 Python unit tests, both corpus-validation modes, intentional rejection of the empty empirical results template, and SHA-256 release integrity checking.
- Verified GitHub local link targets and expected DOI/YouTube destinations. External URLs were authored from the publication records; live availability cannot be certified by offline repository tests.
- **Fresh Git checkout regression:** original `.gitattributes` normalized eight source CSVs and made `verify_release.py` fail even though the ZIP passed. Updated `.gitattributes` to preserve CSV bytes and extensionless configuration/license text; retested fresh clones under both `core.autocrlf=false` and `core.autocrlf=true`, including release integrity verification.
- Checked presence and dimensions of GitHub video thumbnail and social preview. The MP4 is hosted on YouTube and is not distributed in this source archive. The video and thumbnail are outside the manuscript/code licenses; soundtrack originality and third-party rights are not independently certified.

## Disclosures and future verification

The scholarly interpretation and source registers require external review; mock code tests do not measure deployment safety or confirm philosophical claims. Once the files have been pushed, inspect the *live* README and social card on mobile/desktop, confirm the YouTube page and DOI resolve for ordinary users, and review the hosted GitHub Actions result. Keep archival research revisions separately versioned and avoid editing the fixed Zenodo deposit in place.
