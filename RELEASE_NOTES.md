# Release notes — 1.0.0 (11 November 2026)

## Substantive changes from Final Verification Master

1. Added a close reading and fair-priority limitation concerning Seth Lazar's October 2026 Oxford monograph, with a directly identifiable original chapter and a new bibliography entry (now 50 sources).
2. Added a matching primary-passage evidence record (now 39 individually classified anchors), explicitly bounded by what was accessible rather than inventing page quotations.
3. Improved one unnatural English phrase ("defendable" to "defensible").
4. Added a publication-transparency section declaring the hypothetical nature of the case corpus, educational code limits and extensive generative-AI involvement, without inventing affiliations, funders or an assigned DOI.

## Research/package changes

5. Prepared versioned publication metadata, author citation formats, public landing page, documented copyright default, SHA-256 integrity manifest, and a self-check program.
6. Retained all 17 numbered chapters, five principles, original 49 references, the reviewer-response ledger and the twelve-case research corpus.
7. Reran the complete unit-test suite and the corpus validator; results appear in the release audit. No real participant study, external review or runtime penetration testing was invented.

## Known limits

Primary texts inaccessible for a subset of the 50 references; evidence matrix is claim-selective. PDF is tagged but not certified PDF/UA. The mock's real deployment security properties are not established. No independent tests of the theory's superiority have been conducted.

## Public distribution preparation — 21 November 2026

Added split licensing (CC BY 4.0 scholarly content and original datasets; Apache 2.0 original code), explicit video-rights exception, explainer video and preview, contribution instructions, updated release metadata, and refreshed manifest. The original dated manuscript PDF/HTML/Markdown and original research code/data are preserved unchanged. This is a distribution update, not new empirical validation.

## DOI-linked GitHub companion — 21 November 2026

The independent preprint was published on Zenodo as version **1.0.0**, DOI **[10.5281/zenodo.24417028](https://doi.org/10.5281/zenodo.24417028)**. The PDF and companion ZIP uploaded there match the recorded original MD5 hashes; see `ZENODO_PUBLICATION_RECORD.md`.

This GitHub distribution adds the real DOI to the README, citation files, index, and metadata, and includes the video and preview **only in GitHub**. The original PDF, HTML/Markdown scientific manuscript, research cases, protocols, and educational gate are unchanged. Older pre-deposit notices in the frozen manuscript remain historical statements. Reproducibility checks do not imply peer review, source-exhaustive validation, or production-level AI safety.

## GitHub companion update — YouTube-linked video presentation (21 November 2026)

The explainer is now available at [https://www.youtube.com/watch?v=ewEHGMFizdo](https://www.youtube.com/watch?v=ewEHGMFizdo). The GitHub README's full-width, sharp academic thumbnail links directly to YouTube, with corresponding updates to the standalone landing page, video notes, rights statement, and publication metadata. The 22 MB MP4 was removed from the **GitHub source ZIP** to keep repository clones lightweight and avoid splitting views between GitHub and YouTube. The new local thumbnail and a 2:1 social preview image are included. Historical notes above describe earlier package iterations and do not mean the MP4 remains in this edition.

**No original scholarly manuscript, case corpus, reference software, or code test was modified.** The DOI and archived Zenodo v1.0.0 files remain unchanged. This is a GitHub presentation/distribution-only change, not a revised Zenodo research release.

## Final GitHub launch verification — 21 November 2026

An independent **fresh Git checkout** test identified and resolved a release-blocking CSV newline conversion: eight original research CSV files contain CRLF data and must not be converted to LF when Git checks out the repository. The `.gitattributes` rule now preserves those bytes, so both the original research file hashes and the repository release manifest remain reproducible on Linux and Windows. The GitHub Actions workflow uses maintained official checkout/setup-python major versions. An obsolete pre-deposit worksheet was removed from this GitHub-only companion; the actual Zenodo publication record and historical manuscript files remain available. No research finding or original scholarly artifact was revised. See `GITHUB_LAUNCH_QA.md` for the scope and remaining limits of local verification.
