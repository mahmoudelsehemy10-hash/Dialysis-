# Hemodialysis Fundamentals: build instructions

The script generates `output/Hemodialysis_Fundamentals_FMC.pptx` from the uploaded Fresenius Medical Care template deck and the AREP screenshot zips. The original files are only read, never modified.

## Re-run

```bash
pip install python-pptx Pillow        # if not installed
python3 build/build_deck.py           # run from the repository root
```

Options: `--template <pptx>` (another FMC template), `--zips <folder>` (folder holding `Dialysis.zip` and `vascular access.zip`), `--out <path>`.

PDF preview (requires LibreOffice): `soffice --headless --convert-to pdf output/Hemodialysis_Fundamentals_FMC.pptx --outdir output`

## Files

| File | Purpose |
|---|---|
| `build_deck.py` | Layout engine: keeps the template's master, layouts, theme, logo and footer. Reuses the template's photo title and "Thank you" slides, and builds content on the `1_Only title` and `1_Chapter` layouts. |
| `content.py` | All slide text, table and chart data, sources and speaker notes. Edit this file to change content. |
| `images/` | Illustrations cropped automatically from the AREP screenshots (regenerated on each run). |

## Review points (summary)

- The template font is **Verdana** (FMC theme). It was not installed in the build environment, so the PDF preview uses a substitute font. Check line breaks in PowerPoint.
- Corrected source errors: AREP lists chloride as 8.5–10.4 mg/dL and magnesium as 1.8–2.5 mEq/L. The deck uses MedlinePlus ranges instead (98–107 mEq/L; 1.7–2.2 mg/dL).
- Added from the web: the endotoxin limit (ISO 23500-3), the KDOQI 2019 "ESKD Life-Plan", the KDOQI 2015 Kt/V targets and the Flythe 2011 hazard ratios. URLs are in the speaker notes.
- Values that are calculated or illustrative: the 42 L body-water chart, the 55.0% "normal range" bar (100 − 16.7 − 28.3) and the UF-rate worked example.
- To confirm: the population behind the DOPPS 2015 access chart, the Wabel citation, the "Medication errors" actions, and the water limits against ISO 23500-3:2024.
