# 4-Day Hemodialysis Nursing Training Package

Eight editable PowerPoint lectures built on the uploaded **Fresenius Medical Care** template. The template's slide master, layouts, theme (FMC 02 colours, Verdana), logo, footer bar and 16:9 dimensions are kept. Every lecture also has a PDF preview.

> These are training materials. They are **not** an approved Fresenius Medical Care procedure, policy or target set. Clinical and local-policy review is required before use (see below).

## Files

| Day | File | Slides |
|---|---|---|
| 1 Patient Assessment & Safety | `D1_01_Pre_Dialysis_Assessment.pptx` | 19 |
| | `D1_02_Fluid_Assessment_UF_Safety.pptx` | 19 |
| 2 Vascular Access & Infection Control | `D2_03_Vascular_Access_Care.pptx` | 19 |
| | `D2_04_Infection_Prevention.pptx` | 18 |
| 3 Dialysis Quality & Water Safety | `D3_05_Dialysis_Adequacy.pptx` | 19 |
| | `D3_06_Water_Dialysate_Safety.pptx` | 17 |
| 4 Emergencies & Quality Improvement | `D4_07_Hemodialysis_Emergencies.pptx` | 20 |
| | `D4_08_Quality_Indicators.pptx` | 17 |

- `*.pdf`: previews rendered with LibreOffice.
- `Source_Register.md` / `.csv`: every reference with its link, the lectures that use it, and its verification status.

Every lecture contains:
- title slide with the day and lecture number
- 4 measurable objectives
- an opening scenario
- core content, with 4–8 visuals (flowcharts, native editable charts, comparison tables, uploaded AREP illustrations, editable schematics)
- a checklist or summary aid
- a case, plus two scenarios in L07
- a 4-question knowledge check (answers and rationales in the speaker notes)
- key takeaways and references

Detailed teaching points, citations, links, AREP screenshot time-stamps and "NEEDS REVIEW" flags are in the speaker notes.

## Regenerate

```bash
pip install python-pptx Pillow           # dependencies (LibreOffice for PDF previews)
python3 build/build_deck.py --deck program
```

Run the command from the repository root.

- **Content:** each lecture is in `build/program/D*_*.py`; shared text is in `build/program/_common.py`. The source register is generated from `build/program/sources.py`.
- **Layout engine:** `build/build_deck.py`. The originals (template PPTX and screenshot zips) are only read, never modified.
- **PDF previews:** `soffice --headless --convert-to pdf output/program/*.pptx --outdir output/program`

## Evidence notes

- **Uploaded sources:** the template plus AREP eLearning screenshots (Introduction to HD, Vascular Access, Fluid Management, Acid–Base). No IFUs, local policies or Saudi documents were uploaded.
- **Blocked sites:** cdc.gov and PubMed Central could not be opened from the build environment. CDC, Saha & Allon and KDOQI 2006 points were verified through search summaries only. Their status is "Secondary only" in the register.
- **Paywalled standards:** the ISO 23500 texts are paywalled.
  - ISO 23500-5:2024 dialysis-fluid limits were confirmed from the ISO/CEN preview text.
  - Dialysis-water limits and action levels were confirmed only through secondary summaries.
  - The chemical limits table is reproduced from AREP (AAMI, as cited there).

## Items requiring clinical or local-policy review

1. **Local thresholds:** BP, SpO₂, potassium and critical-lab triggers; saline bolus volumes; monitoring intervals (shown as "per protocol").
2. **UF policy:** whether oral intake and rinse-back are added to the UF goal, and which weight is used for the UF rate.
3. **Machine-specific steps (FMC machine IFU):** pre-treatment tests, internal disinfection, post-dialysis sampling function, and defibrillation/blood return during an arrest.
4. **Water policy:** chlorine testing frequency (sources conflict: per shift / every 4 h / daily at both tanks), culture schedule, action levels for dialysis fluid, and role split.
5. **Emergencies (L07):**
   - Air embolism positioning: sources conflict (left lateral head-down vs modified Trendelenburg).
   - Type A dialyzer reaction "do not return blood": textbook teaching, not verified online.
   - Medicines only per protocol and the nurse's authorised scope.
6. **Infection control (L04):**
   - The CDC 2001 HBV/HCV testing intervals need checking against the MMWR table.
   - Vaccine products and schedules available in Saudi Arabia.
   - Saudi MOH/SCOT dialysis safety requirements and HESN reporting (primary texts not found).
7. **Adequacy sampling (L05):** confirm the KDOQI slow-flow method against the guideline and machine IFU. The unit must use one method only.
8. **Data and targets:**
   - DOPPS 2015 access shares (L03) are not local data.
   - All dashboard, trend and case values are illustrative training data.
   - Indicator definitions and targets in L08 are examples, not FMC requirements.
9. **Font:** Verdana (the template font) was not installed in the build environment, so previews use a substitute. Check line breaks in PowerPoint.
