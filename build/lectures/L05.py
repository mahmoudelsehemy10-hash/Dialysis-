# -*- coding: utf-8 -*-
"""Lecture 05 - Day 3: Dialysis Adequacy: Kt/V, URR, and Correct Urea Sampling."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Dialysis_Adequacy"
TITLE = "Dialysis Adequacy: Kt/V, URR, and Correct Urea Sampling"
SUBTITLE = "Day 3 · Dialysis Quality & Water Safety · Lecture 05"
FOOTER_TEXT = "L05 Dialysis adequacy"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 05 of the Hemodialysis Nursing Programme (Day 3). 45–60 minutes.
Primary reference: KDOQI Hemodialysis Adequacy 2015 Update; Daugirdas second-generation Kt/V formula. Bring calculators for the worked example and case.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 05",
     "items": [
         ("Understand", ["What Kt/V and URR measure", "Targets for thrice-weekly HD"]),
         ("Calculate", ["URR and spKt/V by hand", "Interpret the result"]),
         ("Sample correctly", ["Pre- and post-dialysis BUN", "Avoid dilution and rebound errors"]),
         ("Protect the dose", ["Find causes of low delivered dose", "Document and report"]),
     ],
     "notes": "Objectives for Lecture 05."},

    {"kind": "stat_cards", "title": "Adequacy targets for thrice-weekly HD",
     "source": "KDOQI Hemodialysis Adequacy 2015 Update. Am J Kidney Dis. 2015;66(5):884-930",
     "stats": [("1.4", "target spKt/V per session"), ("1.2", "minimum delivered spKt/V"), ("≈ 65%", "URR that corresponds to spKt/V 1.2"), ("2.3 / 2.1", "weekly std Kt/V target / minimum (other schedules)")],
     "cards": [
         ("Kt/V", ["K = dialyzer urea clearance", "t = treatment time", "V = urea volume (≈ body water)"]),
         ("URR", ["% fall in blood urea in one session", "Simple, but ignores UF and urea generation"]),
         ("Measured", ["Usually monthly, per unit policy", "Also when the prescription changes"]),
     ],
     "notes": """
[WEB] KDOQI 2015, Guideline 3.1: target spKt/V 1.4 per session for thrice-weekly HD; minimum delivered spKt/V 1.2 (1B; unchanged from 2006). Other schedules: target weekly standard Kt/V 2.3, minimum 2.1. spKt/V 1.2 corresponds approximately to URR 65%. PubMed https://pubmed.ncbi.nlm.nih.gov/26498416/ ; https://ajkdblog.org/2015/11/30/the-2015-kdoqi-hemodialysis-adequacy-guideline-update-whats-new/ (""" + ACCESSED + """).
Measurement frequency: monthly is common practice and a regulatory expectation in many systems (e.g. CMS) – confirm local requirement.
V ≈ total body water (AREP Fluid Management [Water Treatment / 155139])."""},

    {"kind": "formula", "title": "Calculate URR and spKt/V",
     "source": "Daugirdas JT. J Am Soc Nephrol. 1993;4(5):1205-1213 · KDOQI 2015",
     "formulas": [
         ("Urea reduction ratio", "URR = (pre-BUN − post-BUN) ÷ pre-BUN × 100", "R = post-BUN ÷ pre-BUN"),
         ("Daugirdas second-generation spKt/V", "−ln(R − 0.008 × t) + (4 − 3.5 × R) × UF ÷ W", "t = hours · UF = litres removed · W = post-weight (kg)"),
     ],
     "below": ["Use the same units for pre and post (mg/dL or mmol/L)", "Machine online clearance gives an estimate, not a replacement for blood samples unless validated locally"],
     "example": {"head": "Worked example (educational)", "body": [
         "Pre-BUN 70, post-BUN 22 mg/dL; t = 4 h; UF 3.0 L; post-weight 70 kg",
         "R = 22 ÷ 70 = 0.314",
         "URR = (70 − 22) ÷ 70 = 68.6%",
         "−ln(0.314 − 0.032) = 1.265",
         "(4 − 3.5 × 0.314) × 3.0 ÷ 70 = 0.124",
         ("spKt/V = 1.265 + 0.124 = 1.39", {"bold": True, "color": NAVY, "size": 15, "space_after": 4}),
         "Above minimum 1.2, just below target 1.4"]},
     "notes": """
[WEB] Daugirdas second-generation formula: spKt/V = −ln(R − 0.008 × t) + (4 − 3.5R) × UF/W, R = post/pre BUN, t in hours, UF in litres, W = post-dialysis weight in kg (Daugirdas JT. JASN 1993;4(5):1205-1213); URR = (1 − R) × 100. Summary verified at https://open-exam-prep.com/study-guides/bonent-chn/principles-dialysis-adequacy/dialysis-adequacy (""" + ACCESSED + """).
Worked example is a CALCULATION: R = 0.3143; ln(0.2823) = −1.2648; (4 − 1.1) × 3/70 = 0.1243; spKt/V = 1.389.
Online clearance monitoring (OCM) on machines estimates delivered Kt/V per session; its use instead of blood-based measurement depends on local validation and the machine IFU."""},

    {"kind": "steps", "title": "Pre-dialysis sample: avoid dilution",
     "source": "KDOQI Hemodialysis Adequacy guidelines (2006, 2015) · ANNA Core Curriculum 2015 · Local protocol",
     "steps": [
         ("Timing", "Before any saline, heparin or treatment has started"),
         ("AV access", "Draw from the arterial needle before connecting or flushing with saline"),
         ("CVC", "Withdraw and discard the lock volume (+ dead space) per protocol, then sample"),
         ("Label", "Patient, date, 'PRE', time; same lab method as post sample"),
         ("Check", "Note anything unusual (missed session, short session, sample delay)"),
     ],
     "side": {"head": "If the pre sample is diluted", "fill": "navy", "body": [
         "Pre-BUN falsely low", "URR and Kt/V falsely low", "Patient may get an unnecessary prescription increase",
         "Saline and heparin locks are the usual cause"]},
     "notes": """
Pre-dialysis BUN must be drawn before dialysis starts and must not be diluted by saline or heparin (KDOQI adequacy guideline sampling recommendations; ANNA Core Curriculum).
CVC: remove lock solution first; discard volume per catheter labelling and local protocol.
Effect: dilution lowers pre-BUN → R rises → URR and Kt/V calculated LOWER than delivered."""},

    {"kind": "steps", "title": "Post-dialysis sample: slow-flow or stop-dialysate method",
     "source": "KDOQI Hemodialysis Adequacy guidelines (2006, 2015) · Local protocol",
     "steps": [
         ("End treatment", "Turn UF off; set dialysate to bypass (or reduce UF to minimum) per method"),
         ("Slow-flow method", "Reduce blood pump to about 100 mL/min for ~15 s"),
         ("Sample site", "Draw from the arterial sampling port, then stop the pump"),
         ("Alternative: stop-dialysate", "Dialysate off/bypass for ~3 min with blood flow maintained, then sample"),
         ("Then rinse back", "Never sample after saline rinse-back or from the venous line"),
     ],
     "side": {"head": "Why these steps?", "fill": "sand", "body": [
         "Slow flow clears access recirculation from the line", "Too early or from the venous side: post-BUN falsely low",
         "Too late (> 2–3 min): urea rebound starts", "Use one method consistently in the unit"]},
     "notes": """
[WEB] Slow-flow technique: reduce blood pump flow to ~100 mL/min (some protocols 50–100) for about 15 seconds, then draw from the arterial sampling port; UF off and dialysate in bypass. Stop-dialysate-flow alternative: dialysate off for ~3 minutes while blood flow continues, then sample. Slow flow addresses access recirculation, not all rebound. Sources: KDOQI adequacy guideline sampling recommendations; summary https://open-exam-prep.com/study-guides/nncc-ccht-a/fluid-dynamics-volume-kinetic-modeling/dialysis-adequacy-ktv-urr and review https://www.hdcn.com/7/710ndwu.htm (""" + ACCESSED + """).
Exact timings must follow the unit protocol and the machine IFU (some machines have a dedicated sampling function)."""},

    {"kind": "bar_compare", "title": "Sampling errors change the result, not the dialysis",
     "source": "Illustrative calculation · KDOQI Hemodialysis Adequacy guidelines (2006, 2015)",
     "chart": {"name": "Sampling error URR chart", "title": "Calculated URR (%) for the same treatment (illustrative)",
               "categories": ["Correct samples", "Post diluted by recirculation", "Post drawn late (rebound)", "Pre diluted with saline"],
               "series": [("URR (%)", [68.6, 74.3, 62.9, 63.3])],
               "point_colors": [BLUE, MID, GREY, GREY], "max": 80, "fmt": '0.0"%"'},
     "side": {"head": "How to read this", "body": [
         "True result: pre 70, post 22 mg/dL → URR 68.6%",
         "Post-BUN 18 (recirculation) → URR looks better than it is",
         "Post-BUN 26 (rebound) → URR looks worse",
         "Pre-BUN 60 (saline) → URR looks worse",
         ("Check sampling first before changing the prescription", {"bold": True, "color": NAVY, "space_after": 4})]},
     "notes": """
ILLUSTRATIVE CALCULATED VALUES (not study data): same treatment as the worked example. Correct: pre 70, post 22 → 68.6%. Recirculation-diluted post 18 → (70 − 18)/70 = 74.3%. Late post with rebound 26 → 62.9%. Pre diluted to 60 with correct post 22 → (60 − 22)/60 = 63.3%.
Teaching point: an unexpected change in URR/Kt/V should first trigger a check of sampling technique and treatment delivery before the prescription is changed (KDOQI)."""},

    {"kind": "six_grid", "title": "Why the delivered dose falls short",
     "source": "KDOQI 2015 · Handbook of Dialysis. 5th ed. 2015 · AREP Introduction to Hemodialysis",
     "items": [
         ("Time lost", "Shortened t", "Late start, early stop, alarms, interruptions. Record actual minutes."),
         ("Blood flow", "Low Qb", "Small needles, access problems, high arterial pressure limits."),
         ("Recirculation", "Access / needles", "Stenosis, needles too close or reversed."),
         ("Dialyzer", "Clotting", "Inadequate anticoagulation, wrong dialyzer, fibre clotting."),
         ("Dialysate flow", "Low Qd", "Settings not as prescribed, bypass periods."),
         ("Sampling", "Error", "Dilution, wrong timing, venous side, mislabelled tube."),
     ],
     "notes": """
Common causes of low delivered dose (KDOQI 2015; Handbook of Dialysis 2015): reduced treatment time, reduced blood flow, access recirculation, dialyzer clotting/reduced surface area, dialysate flow errors, sampling or laboratory error.
AREP: adequacy measured by Kt/V; prescriptions vary by time, frequency, duration, location [Dialysis / 145459].
Nurses control most of these factors: actual time, achieved Qb, needle placement, anticoagulation and sampling."""},

    {"kind": "matrix", "title": "Low result? Work through it before changing the prescription",
     "source": "KDOQI 2015 · Local adequacy protocol",
     "rows": [
         ("1 Sampling", "Was the sampling technique and timing correct?", "Repeat samples with correct technique if in doubt"),
         ("2 Delivery", "Actual time, Qb, Qd and dialyzer as prescribed?", "Review treatment records; correct deviations"),
         ("3 Access", "Recirculation, stenosis, needle placement?", "Physical exam; recirculation or flow study per order"),
         ("4 Patient", "Weight change, missed sessions, residual function?", "Report to physician with data"),
         ("5 Prescription", "Only then: change time, Qb, dialyzer or frequency", "Physician decision; re-measure"),
     ],
     "fills": ["blue", "mid", "blue", "mid", "navy"],
     "notes": "Stepwise approach consistent with KDOQI 2015: confirm measurement validity, then delivery, access and patient factors, then adjust the prescription. Steps 1–3 are largely nursing actions."},

    {"kind": "case", "title": "Case: Kt/V dropped from 1.45 to 1.05",
     "source": "Fictional teaching case",
     "case": [
         "Mr H, AVF, prescribed 4 h, Qb 400 mL/min. Last month spKt/V 1.45.",
         "This month 1.05. Pre-BUN 64, post-BUN 30 mg/dL.",
         "Records: three sessions ended 30 min early; achieved Qb 300 because of high arterial pressure.",
         "Post sample was taken after rinse-back by a new staff member."],
     "questions": [
         "Calculate the URR. Is it adequate?",
         "Which sampling error could make the result unreliable?",
         "Which delivery problems reduced the dose?",
         "What do you do before the physician changes the prescription?"],
     "notes": """
Suggested answers (educational):
1. URR = (64 − 30)/64 = 53.1% → below 65%.
2. Sampling after saline rinse-back dilutes the post sample (falsely LOW post-BUN → URR would look better), so the true dose may be even lower; repeat with correct technique.
3. Shortened sessions and low Qb (high arterial pressure: needle too small or access problem/stenosis).
4. Repeat correct samples; review time and Qb; assess access (look/listen/feel), needle gauge; report data to physician."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 05 summary",
     "items": [
         ("Know the targets", "spKt/V 1.4 target, 1.2 minimum (≈ URR 65%) for thrice-weekly HD."),
         ("Calculate and sense-check", "URR and Daugirdas spKt/V; compare with last month."),
         ("Pre sample: no dilution", "Before saline or heparin; discard CVC lock first."),
         ("Post sample: slow flow, arterial port", "UF off, ~100 mL/min for ~15 s; never after rinse-back."),
         ("Protect delivered dose", "Full time, achieved Qb, no recirculation, no clotting."),
     ],
     "notes": "Summarise and link to Lecture 06 (water and dialysate safety)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["kdoqi_adeq"], "National Kidney Foundation. KDOQI Clinical Practice Guidelines for Hemodialysis Adequacy, 2006 update. Am J Kidney Dis. 2006;48(Suppl 1):S2-S90.",
              R["daug_ktv"], R["handbook"], R["anna"], R["arep"], R["ifu"]],
     "notes": "References for Lecture 05."},
]
