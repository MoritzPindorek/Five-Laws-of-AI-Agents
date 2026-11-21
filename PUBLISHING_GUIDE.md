# GitHub publication and maintenance guide — Zenodo DOI linked

The scholarly version of record is **[10.5281/zenodo.24417028](https://doi.org/10.5281/zenodo.24417028)**, published 21 November 2026. Its files are permanently archived; GitHub is the discoverable code, documentation, and educational-media companion.

## Publishing this repository

1. Create a **public GitHub repository** (suggested name: `five-laws-of-ai-agents`). Do not initialize it with another README, license, or `.gitignore`, because all three are already supplied.
2. Extract the **GitHub repository ZIP** so `README.md`, `CITATION.cff`, `.github/`, the Python files, and `assets/` are at the repository root. **Do not upload the ZIP as the only repository file.** The video is hosted on YouTube; the source ZIP contains its preview, not a duplicate MP4.
3. Commit and push the extracted files. The repository contains mixed licenses (CC BY 4.0 research material and Apache 2.0 code), plus a separately rights-reserved video thumbnail and link. Do not create a misleading repo-wide `LICENSE` file that pretends all assets share one license. Refer to `RIGHTS_AND_ATTRIBUTION.md`.
4. On GitHub, verify that the README cover, five-law and DEF diagrams, explainer thumbnail/video link, DOI badge, PDF link, and all section anchors render correctly. Check desktop and mobile.
5. Enable GitHub Issues if you want scholarly input. The contribution guide and CI workflow are already included. Optional: enable Discussions for conceptual critiques distinct from bugs.
6. After the repository is public, optionally add its URL to the Zenodo record metadata as a **related work / software repository**. This does not alter the archived Zenodo files or DOI.

## Recommended GitHub settings

**Description:** Independent philosophical research on the Five Laws of AI Agents, delegated authority, non-entitlement and corrigibility. Zenodo DOI: 10.5281/zenodo.24417028  
**Website:** https://doi.org/10.5281/zenodo.24417028  
**Topics:** `ai-ethics`, `ai-governance`, `ai-agents`, `corrigibility`, `philosophy`, `research`, `reproducibility`, `delegated-authority`  
**Release tag:** `v1.0.0` (repository companion aligned with Zenodo version; tag the exact files you publish)  
**Citation:** GitHub's Cite this repository uses `CITATION.cff` and points to the archived Zenodo DOI.

## Local verification

```bash
python -m unittest test_reference_gate test_analysis_template test_additional_integrity -v
python validate_corpus.py
python -O validate_corpus.py
python verify_release.py
python audit_repository.py
```

`python analysis_template.py Paired_Results_Blank_Template.csv` is **supposed to fail** because no empirical study results are recorded. The research remains independent and non-peer-reviewed; educational tests do not establish an effective deployed security control.

## Editing and integrity discipline

The original research edition (PDF, HTML, Markdown, code and case files) is deliberately preserved from the published Zenodo release. **Do not run `build_publication.py` as part of a routine GitHub setup**: it is the original historical typesetting script, requires optional tools (Pandoc, Beautiful Soup and WeasyPrint), and would regenerate the canonical PDF/HTML rather than simply verify them.

The bundled CSV research files have mixed original CRLF/LF line endings. `.gitattributes` disables Git newline conversion specifically for CSVs; a local ZIP integrity test alone cannot catch the historical failure caused by Git checkout normalization. Always run `python verify_release.py` and `python audit_repository.py` on a **fresh checkout** before making a tagged release. The checksum manifest covers the packaged repository files, and should be regenerated only after intentional changes; never modify the original manuscript merely to fix a checksum.

## DOI/versioning discipline

- **Zenodo v1.0.0 DOI:** [10.5281/zenodo.24417028](https://doi.org/10.5281/zenodo.24417028) — cite this for the fixed original deposit.
- The manuscript edition still says **11 November 2026**; the first public Zenodo release is **21 November 2026**. See `MANUSCRIPT_HISTORY.md`.
- If you make substantive scholarly changes to the paper or data, create a transparently versioned new release and (if appropriate) a new Zenodo version/DOI. Never silently overwrite the archived scientific record.
- The video is hosted on YouTube (not included as an MP4 in either Zenodo or this GitHub source ZIP); its thumbnail and the linked video are not covered by the content/code open licenses.

## YouTube and social preview

- **Watch URL:** [https://www.youtube.com/watch?v=ewEHGMFizdo](https://www.youtube.com/watch?v=ewEHGMFizdo). The README preview is a locally stored, high-resolution image that opens YouTube on click.
- **Social preview asset:** `assets/github-social-preview.jpg` (1280×640). After creating the repository, set it under **Settings → General → Social preview** if the UI offers that control. This is separate from the README image.
- **View consolidation:** Video viewing is directed to YouTube, while the PDF and primary research citation remain anchored to Zenodo. The source repository does not contain a 22 MB duplicated MP4.
- **Live verification:** Open the video in an incognito/private window, verify public access, then test the clickable README thumbnail on both desktop and mobile. Externally hosted availability cannot be guaranteed by local checks.
- **Optional backup:** Keep the original MP4 in private working storage; release it separately only if you decide a downloadable archival copy is needed and have the necessary rights.
