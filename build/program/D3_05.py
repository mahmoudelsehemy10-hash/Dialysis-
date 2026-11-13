# -*- coding: utf-8 -*-
"""Day 3 · Lecture 05: Dialysis Adequacy: Kt/V, URR, and Correct Urea Sampling."""
from program._common import *  # noqa: F401,F403

TITLE = "Dialysis Adequacy: Kt/V, URR, and Correct Urea Sampling"
SUBTITLE = "Day 3 · Dialysis Quality & Water Safety · Lecture 05"
FOOTER_TEXT = "Day 3 · Lecture 05"
REFS = ["KDOQI_ADEQ15", "KDOQI_ADEQ06", "DAUG93", "KHI_EKTV", "AREP_HD", "AREP_FM", "HANDBOOK", "ANNA", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 3, Lecture 05 (30–40 min). Bring calculators.
Sampling method: the post-dialysis 'slow-flow' and 'stop-dialysate-flow' techniques are described in the KDOQI Hemodialysis Adequacy guideline (2006 update, clinical practice recommendation on blood sampling), verified here only through secondary summaries. They are TWO ALTERNATIVE methods – do not combine steps. The unit must choose one and specify it in its protocol together with the machine IFU.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 05 objectives",
     "items": [
         ("Explain", ["Explain what Kt/V and URR measure and what they miss"]),
         ("Calculate", ["Calculate URR from labelled illustrative data"]),
         ("Sample", ["Describe correct pre- and post-dialysis urea sampling (one method)"]),
         ("Act", ["List 5 causes of low delivered dose and the nurse's actions"]),
     ],
     "notes": "Assessed in the case (slide 15) and knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening question: is this patient getting enough dialysis?",
     "source": "Discussion question",
     "story": ["Mr H feels well and his potassium is normal. His Kt/V this month is 1.05.",
               "Last month it was 1.45. Nothing in his prescription changed."],
     "prompts": ["Did his dialysis really get worse?", "What could make the number wrong?", "What else besides Kt/V tells you about quality?"],
     "notes": "Collect ideas: shortened sessions, low achieved Qb, recirculation/access stenosis, clotting, sampling error. Kt/V is one small-solute marker; quality also includes fluid control, symptoms, nutrition, phosphate, residual function (KDOQI 2015). Mr H returns in the case (slide 15)."},

    {"kind": "two_cards", "title": "Adequacy: useful, but only one measure",
     "source": "KDOQI Hemodialysis Adequacy 2015 Update · AREP Introduction to Hemodialysis",
     "h": 3.7,
     "cards": [
         ("What Kt/V and URR show", ["Removal of urea (a small solute)", "Delivered dose of one session", "Trends over months",
                                     "Whether delivery matches the prescription"]),
         ("What they do not show", ["Fluid control and blood pressure", "Middle-molecule removal", "Potassium, phosphate, acid–base",
                                    "Symptoms, nutrition, quality of life", "Residual kidney function"]),
     ],
     "banner": "Good adequacy = adequate urea removal + fluid control + well-being. Look at the whole patient",
     "notes": "KDOQI 2015 describes adequacy beyond urea kinetics (volume control, residual function, patient-reported outcomes). AREP [Dialysis / 145459]: adequacy of HD measured by Kt/V; prescriptions vary by time, frequency, duration, location."},

    {"kind": "table_only", "title": "Kt/V, URR and their variants",
     "source": "KDOQI 2015 · Daugirdas JT. JASN 1993 · Kidney Health Initiative (ASN) Kt/V data standard",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.6, 4.9, 4.55], "row_h": 0.78, "size": 12,
               "rows": [["Measure", "What it is", "Nurse's view"],
                        ["URR", "% fall in blood urea during one session", "Simple; ignores UF and urea made during HD"],
                        ["spKt/V (single-pool)", "Clearance × time ÷ urea volume; includes UF term", "Most common monthly report"],
                        ["eKt/V (equilibrated)", "spKt/V corrected for urea rebound after HD", "Usually ~0.2 lower than spKt/V"],
                        ["Standard Kt/V (weekly)", "Weekly dose that allows comparing schedules", "Used for non-thrice-weekly schedules"],
                        ["Online clearance (machine)", "Machine estimate each session", "Use only as validated by unit and IFU"]]},
     "notes": """
[WEB] spKt/V: Daugirdas second-generation formula (JASN 1993). eKt/V: accounts for post-dialysis urea rebound; KHI data standard gives eKt/V = spKt/V × [0.924 − 0.395/(t in hours)] + 0.056 (https://khi.asn-online.org/uploads/Single_Pool_Kt-V.pdf); summaries describe eKt/V as roughly 0.15–0.25 lower than spKt/V. Standard Kt/V targets in KDOQI 2015 for non-thrice-weekly schedules (target 2.3, minimum 2.1). (""" + ACCESSED + """)
Online clearance monitoring depends on machine model and local validation – FMC IFU (not uploaded)."""},

    {"kind": "bar_side", "title": "URR made visible",
     "source": "Illustrative training data · URR formula: KDOQI / Daugirdas",
     "chart": {"name": "Pre and post urea chart", "title": "Blood urea nitrogen (mg/dL) for one session",
               "categories": ["Pre-dialysis BUN", "Post-dialysis BUN"],
               "series": [("BUN", [70, 22])], "point_colors": [NAVY, MID], "max": 80, "fmt": '0', "h": 4.55,
               "note": ILLUS},
     "side": {"head": "Step by step", "body": [
         ("URR = (pre − post) ÷ pre × 100", {"bold": True, "color": NAVY, "space_after": 6}),
         "Removed: 70 − 22 = 48 mg/dL", "48 ÷ 70 = 0.686", ("URR = 68.6%", {"bold": True, "size": 16, "color": BLUE, "space_after": 6}),
         "Same units for both samples (mg/dL or mmol/L)"]},
     "notes": "Visual 1 (chart). ILLUSTRATIVE TRAINING DATA. URR = (70 − 22)/70 × 100 = 68.6%. URR ≈ 65% corresponds approximately to spKt/V 1.2 (KDOQI; summaries)."},

    {"kind": "formula", "title": "spKt/V worked example",
     "source": "Daugirdas JT. J Am Soc Nephrol. 1993;4(5):1205-1213 · KHI Kt/V data standard",
     "formulas": [
         ("Daugirdas second-generation spKt/V", "−ln(R − 0.008 × t) + (4 − 3.5 × R) × UF ÷ W", "R = post ÷ pre BUN · t hours · UF litres · W post-weight kg"),
         ("Equilibrated Kt/V (KHI data standard)", "eKt/V = spKt/V × (0.924 − 0.395 ÷ t) + 0.056", "Corrects for urea rebound; t in hours"),
     ],
     "below": ["Lab or software usually calculates this", "Nurses check that inputs (times, weights, UF) are correct"],
     "example": {"head": "Worked example (illustrative training data)", "body": [
         "Pre 70, post 22 mg/dL; 4 h; UF 3.0 L; post-weight 70 kg",
         "R = 22 ÷ 70 = 0.314",
         "−ln(0.314 − 0.032) = 1.265",
         "(4 − 3.5 × 0.314) × 3.0 ÷ 70 = 0.124",
         ("spKt/V = 1.39", {"bold": True, "color": NAVY, "size": 15, "space_after": 3}),
         "eKt/V = 1.39 × (0.924 − 0.099) + 0.056 = 1.20"]},
     "notes": "Calculation: R = 0.3143; ln(0.2823) = −1.2648; (4 − 1.100) × 3/70 = 0.1243; spKt/V = 1.389. eKt/V = 1.389 × (0.924 − 0.0988) + 0.056 = 1.202. Formula sources: Daugirdas 1993; KHI data standard (web-verified, " + ACCESSED + "). ILLUSTRATIVE TRAINING DATA."},

    {"kind": "stat_cards", "title": "Targets in context",
     "source": "KDOQI Hemodialysis Adequacy 2015 Update. Am J Kidney Dis. 2015;66(5):884-930",
     "stats": [("1.4", "target spKt/V per session (thrice weekly)"), ("1.2", "minimum delivered spKt/V (thrice weekly)"), ("≈ 65%", "URR roughly equal to spKt/V 1.2"), ("2.3 / 2.1", "weekly std Kt/V target / minimum (other schedules)")],
     "cards": [
         ("Applies to", ["Thrice-weekly in-center HD", "Little or no residual kidney function", "Measured regularly (often monthly)"]),
         ("Context", ["Higher dose did not show clear extra benefit in trials", "Residual function may allow individualised targets (physician)"]),
         ("Not a target", ["Machine online values alone (unless validated)", "A single unexplained low result: check first"]),
     ],
     "notes": "[WEB] KDOQI 2015 Guideline 3.1: target spKt/V 1.4 per session, minimum delivered 1.2 for thrice-weekly HD (1B); weekly standard Kt/V target 2.3, minimum 2.1 for other schedules. 1.2 ≈ URR 65% (summaries). https://pubmed.ncbi.nlm.nih.gov/26498416/ (" + ACCESSED + "). Statement on higher dose and residual function: KDOQI 2015 context (HEMO study) – verify wording against the guideline text."},

    {"kind": "line_chart", "title": "Read adequacy as a trend",
     "source": "Illustrative training data · targets: KDOQI 2015",
     "chart": {"name": "Adequacy trend", "title": "Monthly spKt/V for one patient",
               "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
               "series": [("spKt/V", [1.46, 1.42, 1.44, 1.45, 1.05, 1.41], BLUE),
                          ("Target 1.4", [1.4] * 6, MID, True), ("Minimum 1.2", [1.2] * 6, RED, True)],
               "min": 0.8, "max": 1.7, "major": 0.1, "axis_fmt": "0.0", "labels": True, "fmt": "0.00", "note": ILLUS},
     "side": {"head": "May: what happened?", "body": [
         "Sudden single drop, then normal again", "Check sampling and delivered time first",
         "Repeat measurement if technique was doubtful", "A sustained fall: think access, Qb, clotting",
         ("Report with the data", {"bold": True, "color": NAVY})]},
     "notes": "Visual 3 (trend chart). ILLUSTRATIVE TRAINING DATA. Teaching point: an isolated drop followed by recovery suggests a measurement or delivery problem that month, not a prescription failure."},

    {"kind": "steps", "title": "Pre-dialysis sample: avoid dilution",
     "source": "KDOQI Hemodialysis Adequacy 2006 (blood sampling recommendations, via summaries) · local protocol",
     "steps": [
         ("Timing", "Before any saline, heparin or treatment starts"),
         ("AV access", "From the arterial needle before connecting or flushing"),
         ("CVC", "Withdraw and discard lock volume (+ dead space) per protocol, then sample"),
         ("Label", "Patient, date, 'PRE', time; same lab as the post sample"),
         ("Note", "Missed or short previous session, sample delays"),
     ],
     "side": {"head": "If diluted", "fill": "navy", "body": ["Pre-BUN falsely low", "URR and Kt/V falsely low", "Risk of an unnecessary prescription change"]},
     "notes": "Pre-dialysis BUN must not be diluted by saline or heparin; for CVC, remove the lock first (KDOQI adequacy guideline sampling recommendations – secondary summaries; ANNA Core Curriculum). Discard volume per catheter labelling and local protocol."},

    {"kind": "pathway", "title": "Post-dialysis sample: one method, done the same way",
     "source": "KDOQI Hemodialysis Adequacy 2006, blood sampling recommendation (slow-flow method), via secondary summaries · machine IFU",
     "mono": True,
     "nodes": [("1 End of treatment", "time completed"), ("2 UF off", "dialysate bypass per method"),
               ("3 Slow the pump", "~100 mL/min for ~15 s"), ("4 Sample", "from arterial sampling port"),
               ("5 Stop pump", "then rinse back")],
     "cards": [("Why slow flow?", ["Clears recirculated blood from the arterial line", "Sample reflects the patient's blood"]),
               ("Alternative method", ["Stop-dialysate-flow (~3 min, blood flow continues)", "Use ONE method per protocol: never mix steps"]),
               ("Never", ["Sample after saline rinse-back", "Sample from the venous line"])],
     "notes": """
Visual 4 (sampling sequence). Source of the method: KDOQI Hemodialysis Adequacy guideline 2006 update – clinical practice recommendation for post-dialysis BUN sampling (slow-flow: reduce Qb to ~100 mL/min for ~15 s, then draw from the arterial sampling port; alternative stop-dialysate-flow: dialysate off for ~3 min with blood flow maintained, then sample). Verified via secondary summaries only (https://open-exam-prep.com/study-guides/nncc-ccht-a/fluid-dynamics-volume-kinetic-modeling/dialysis-adequacy-ktv-urr ; https://www.hdcn.com/7/710ndwu.htm, """ + ACCESSED + """) – NEEDS REVIEW against the KDOQI text and the FMC machine IFU (some machines have a dedicated sampling function).
Do not combine elements of the two methods; the unit protocol must specify one."""},

    {"kind": "bar_side", "title": "Sampling errors change the number, not the dialysis",
     "source": "Illustrative calculation · KDOQI adequacy guidelines",
     "chart": {"name": "Sampling error chart", "title": "Calculated URR (%) for the same treatment",
               "categories": ["Correct samples", "Post diluted (recirculation)", "Post drawn late (rebound)", "Pre diluted (saline)"],
               "series": [("URR", [68.6, 74.3, 62.9, 63.3])], "point_colors": [BLUE, MID, GREY, GREY], "max": 80, "fmt": '0.0"%"', "h": 4.55,
               "note": ILLUS + " · calculated from BUN values in the notes"},
     "side": {"head": "How to read this", "body": [
         "True: pre 70, post 22 → 68.6%", "Post 18 (recirculation) → looks better", "Post 26 (rebound) → looks worse",
         "Pre 60 (saline) → looks worse", ("Check sampling before changing the prescription", {"bold": True, "color": NAVY})]},
     "notes": "Visual 5 (chart). ILLUSTRATIVE CALCULATED VALUES: (70−22)/70 = 68.6%; (70−18)/70 = 74.3%; (70−26)/70 = 62.9%; (60−22)/60 = 63.3%."},

    {"kind": "algorithm", "title": "Result below expectation: nursing actions",
     "source": "KDOQI 2015 · Handbook of Dialysis 2015 · local adequacy protocol",
     "w": 5.4, "no_w": 3.2,
     "nodes": [
         {"t": "start", "text": "spKt/V or URR below expected"},
         {"t": "decision", "text": "Sampling done correctly?", "no": "Repeat samples with correct method; report", "no_label": "No"},
         {"t": "decision", "text": "Full time, Qb, Qd delivered?", "no": "Correct delivery; find the cause (alarms, late start)", "no_label": "No"},
         {"t": "decision", "text": "Access and dialyzer OK?", "no": "Exam, recirculation, clotting: report to physician", "no_label": "No"},
         {"t": "end", "text": "Report trend and data: physician reviews prescription"},
     ],
     "side": {"head": "Delivered dose falls with", "fill": "navy", "body": ["Shortened time", "Low achieved Qb", "Recirculation, reversed needles", "Dialyzer clotting", "Wrong Qd or bypass periods"]},
     "notes": "Visual 6 (algorithm). Stepwise approach: validate measurement → delivery → access/dialyzer → physician review (consistent with KDOQI 2015 and Handbook of Dialysis). Recirculation increases when needles are too close, reversed, or with outflow stenosis."},

    {"kind": "checklist", "title": "Adequacy sampling checklist",
     "source": "Summary aid · adapt to local protocol and machine IFU",
     "row_h": 0.55, "size": 12, "h": 4.95,
     "columns": [
         ("Before (pre sample)", ["Correct patient and tube labels", "Before saline/heparin", "CVC lock removed first", "Time recorded", "Weight recorded"]),
         ("After (post sample)", ["Prescribed time completed", "UF off / method per protocol", "Slow flow ~100 mL/min ~15 s", "Arterial sampling port", "Before rinse-back"]),
         ("Record", ["Actual treatment minutes", "Achieved Qb and Qd", "UF volume, post-weight", "Interruptions, clotting", "Any sampling deviation"]),
     ],
     "notes": "Summary aid built on the single slow-flow method shown on slide 11. If the unit uses the stop-dialysate-flow method instead, replace the 'After' column accordingly – never mix both."},

    {"kind": "case", "title": "Case: an unexpectedly low result",
     "source": "Fictional teaching case (illustrative training data)",
     "case": [
         "Mr H, AVF, prescribed 4 h, Qb 400 mL/min. Last month spKt/V 1.45; this month 1.05.",
         "Pre-BUN 64, post-BUN 30 mg/dL.",
         "Three sessions ended 30 min early; achieved Qb 300 with high arterial pressure.",
         "The post sample was drawn after rinse-back."],
     "questions": [
         "Calculate the URR. Is it adequate?",
         "Which sampling error is present and what is its effect?",
         "Which delivery problems reduced the dose?",
         "What do you do before the prescription is changed?"],
     "notes": """
1. URR = (64 − 30)/64 = 53.1% → below ~65%.
2. Post sample after saline rinse-back is diluted → post-BUN falsely low → URR/Kt/V look BETTER than true; the true dose may be even lower. Repeat with the correct method.
3. Shortened sessions (time) and low achieved Qb (needle gauge too small or access problem/stenosis).
4. Repeat correct samples; review delivered time and Qb; examine the access; check needle gauge; report data to the physician."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Pre 80, post 28 mg/dL. URR?", ["A. 35%", "B. 52%", "C. 65%", "D. 72%"]),
         ("Post sample drawn after saline rinse-back makes URR…", ["A. falsely high", "B. falsely low", "C. unchanged", "D. impossible to calculate"]),
         ("KDOQI minimum delivered spKt/V (thrice weekly)?", ["A. 1.0", "B. 1.2", "C. 1.4", "D. 2.1"]),
         ("Best first step after an unexpected low Kt/V?", ["A. Increase dialyzer size", "B. Verify sampling and delivered time", "C. Ignore if patient well", "D. Add a session"]),
     ],
     "notes": "Q1 C – (80 − 28)/80 = 65%. Q2 A – diluted post sample lowers post-BUN → URR looks higher. Q3 B – 1.2 (target 1.4). Q4 B – validate measurement and delivery first (prescription changes are physician decisions)."},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 05 summary",
     "items": [
         ("One measure among several", "Kt/V and URR show urea removal, not fluid control or well-being."),
         ("Know the variants", "spKt/V (monthly), eKt/V (~0.2 lower), standard Kt/V (other schedules)."),
         ("Targets in context", "Thrice weekly: spKt/V target 1.4, minimum 1.2 (≈ URR 65%)."),
         ("Sample correctly, one method", "Pre: no dilution. Post: slow flow, arterial port, before rinse-back."),
         ("Protect the delivered dose", "Full time, achieved Qb, no recirculation or clotting; report trends."),
     ],
     "notes": "Bridge to Lecture 06: water and dialysate safety."},

    refs_slide(),
]
