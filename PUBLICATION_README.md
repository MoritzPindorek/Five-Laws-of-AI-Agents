# The Five Laws of AI Agents — Public Research Edition v1.0

**Author:** Moritz Pindorek. **Date:** 11 November 2026. **Status:** independent, non-peer-reviewed philosophical research paper.

## One authoritative manuscript

The PDF `The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.pdf` is the single public-release reading copy; the corresponding `.md` and `.html` contain the same authored argument. The supplementary files form an accompanying reproducible *educational* research artifact, not an independently evaluated implementation.

## What is inside

- **Paper:** PDF, semantic HTML, Markdown, accessible text and 50 literature references.
- **Research inputs:** 12 synthetic cases in `Cases_v2.jsonl` and `.csv`, blind inputs, schema, codebook, v1 provenance, and adjudication/paired-result blank forms.
- **Executable proof of concept:** `reference_gate.py`, `analysis_template.py` and tests. The gate remains bypassable by hostile code in the same Python process and is **not** a production security control.
- **Methods and provenance:** `Study_Protocol.md`, `Source_Verification_Register.csv` (50 entries), `Passage_Evidence_Matrix.csv` (39 claim anchors, varying verification depth), reviewer matrix, threat model, and dated audit.
- **Citation and rights:** `CITATION.cff`, `CITATION.bib`, `PUBLICATION_METADATA.json`, `RIGHTS_AND_ATTRIBUTION.md`, checksums.

## Reproduce the local claims

On Python 3.10+ in the extracted directory, with no additional Python dependencies for the tests:

```bash
python -m unittest test_reference_gate test_analysis_template test_additional_integrity -v
python validate_corpus.py
python -O validate_corpus.py
python analysis_template.py Paired_Results_Blank_Template.csv
python verify_release.py
```

The analysis-template command is **expected to exit nonzero** because the template contains no real study observations. That negative check is intentional: it prevents invented or empty results from being interpreted as experimental evidence. `verify_release.py` validates the release manifest and PDF structure, not the moral correctness of the paper.

## Publication and disclosure

This is a **published Zenodo research artifact**, not a peer-reviewed article, certified accessible PDF, independently validated safety system, completed empirical comparison, or Nobel-related endorsement. The manuscript discloses substantial generative-AI assistance in research, drafting, coding and editing. The registered version DOI is **[10.5281/zenodo.24417028](https://doi.org/10.5281/zenodo.24417028)**; no ORCID or institution is invented. The author retains copyright while granting file-specific open licenses to original scholarly and software materials, as defined in `RIGHTS_AND_ATTRIBUTION.md`.

**Archival record:** Version **1.0.0**, published on Zenodo on **21 November 2026**: [10.5281/zenodo.24417028](https://doi.org/10.5281/zenodo.24417028). The PDF's **11 November 2026** date identifies the manuscript edition; see [`MANUSCRIPT_HISTORY.md`](MANUSCRIPT_HISTORY.md). The GitHub repository is a companion with additional documentation and a link to the [AI-generated YouTube research explainer](https://www.youtube.com/watch?v=ewEHGMFizdo); the MP4 is not included in GitHub or in the Zenodo deposit.

## Interpretation of the self-audit

The original 39 code unit-tests, PDF geometry checks, 243-state truth table, and corpus validation are local implementation checks. External philosophy review, independent case adjudication, benchmark deployment tests and full PDF/UA validation have **not** been performed. Do not describe them as completed.


**Public-release update (21 November 2026):** The later rights grant in `RIGHTS_AND_ATTRIBUTION.md` supersedes earlier all-rights-reserved preparation notices for the author-owned content; code is Apache 2.0, scholarly content CC BY 4.0, video separately rights-reserved. The original manuscript edition remains dated 11 November.
