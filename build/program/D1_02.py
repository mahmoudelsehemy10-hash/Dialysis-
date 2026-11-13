# -*- coding: utf-8 -*-
"""Day 1 · Lecture 02: Fluid Assessment, Ultrafiltration Safety, and Intradialytic Hypotension."""
from program._common import *  # noqa: F401,F403

TITLE = "Fluid Assessment, Ultrafiltration Safety, and Intradialytic Hypotension"
SUBTITLE = "Day 1 · Patient Assessment & Safety · Lecture 02"
FOOTER_TEXT = "Day 1 · Lecture 02"
REFS = ["AREP_FM", "FLYTHE11", "IDH_REVIEW", "KDOQI_CV05", "EBPG_HI07", "KDOQI_ADEQ15", "KDIGO_BP12",
        "HANDBOOK", "ANNA", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 1, Lecture 02 (30–40 min). Builds on Lecture 01 (UF goal). Key message: fluid removal is individualised; no single UF rate threshold guarantees safety.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 02 objectives",
     "items": [
         ("Assess", ["Interpret target weight, IDWG and clinical fluid signs"]),
         ("Calculate", ["Calculate UF volume and UF rate with correct units"]),
         ("Respond", ["Recognise intradialytic hypotension and act in order"]),
         ("Prevent", ["Explain 3 prevention strategies and teach patients"]),
     ],
     "notes": "Each objective is assessed in the case (slide 15) and knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening question: can we remove it all?",
     "source": "Fictional teaching scenario",
     "story": ["Mrs L gained 4.1 kg since Saturday. She wants to finish in 3 hours today.",
               "Last session she had cramps and dizziness in the final hour."],
     "prompts": ["What else do you need to know?", "What happens to the UF rate in 3 hours?", "Who decides the plan?"],
     "notes": "Collect ideas; return to Mrs L in the worked example (slide 7). Expected: target weight, BP trend, cardiac history, residual urine, intake during HD; shorter time = higher UFR; plan is a physician prescription informed by nursing assessment."},

    {"kind": "image_side", "title": "Fluid balance: intake must match output",
     "source": "AREP Fluid Management (Mulroney S, Myers A. Netter's Essential Physiology 2016:2-11)",
     "image": "fluid_balance.png", "image_alt": "Fluid balance scale: input about 2.5 L, output about 2.5 L (AREP)",
     "caption": "Fluid balance in health. Source: FMC AREP Fluid Management (uploaded screenshot 155202)",
     "side": {"head": "In kidney failure", "body": [
         "Urine output falls or stops", "Intake stays: fluid accumulates between sessions",
         "Dialysis must remove the gain in a few hours", "Salt drives thirst and intake"]},
     "notes": """
Visual 1 (uploaded illustration): AREP [Water Treatment / 155202] – daily input ~2.5 L (1.3 L beverages, 0.9 L food, 0.3 L metabolism) and output ~2.5 L (1.5 L urine, 0.9 L sweat and respiration, 0.1 L GI) in health.
Anuric patients cannot excrete the ~1.5 L normally lost as urine, so it accumulates as interdialytic weight gain."""},

    {"kind": "line_chart", "title": "Weight trend: read the pattern, not one value",
     "source": "Illustrative training data · AREP Fluid Management",
     "chart": {"name": "Weight trend chart", "title": "Pre- and post-dialysis weight over 2 weeks (kg)",
               "categories": ["Mon", "Wed", "Fri", "Mon", "Wed", "Fri"],
               "series": [("Pre-dialysis weight", [72.9, 71.8, 72.0, 73.6, 72.1, 72.3], BLUE),
                          ("Post-dialysis weight", [70.6, 70.5, 70.4, 70.9, 70.5, 70.4], MID),
                          ("Target weight 70.5 kg", [70.5] * 6, GREY, True)],
               "min": 69, "max": 75, "major": 1, "y_title": "kg", "note": ILLUS},
     "side": {"head": "What to notice", "body": [
         "Monday gains are largest (long gap)", "Post-weight not reaching target on Mondays",
         "Rising pre-weights + BP: target may be too high", "Cramps at target: target may be too low",
         ("Report patterns to the physician", {"bold": True, "color": NAVY})]},
     "notes": """
Visual 2 (line chart). ILLUSTRATIVE TRAINING DATA – not patient results.
Interpretation: largest IDWG after the long interdialytic interval; post-weight above target on the second Monday (UF goal not achieved).
Dry (target) weight: extracellular volume at or near normal, not below; reassess regularly (AREP: at least every 2 weeks) [Water Treatment / 155714]."""},

    {"kind": "six_grid", "title": "Clinical fluid assessment",
     "source": "AREP Fluid Management (Lindley E, et al. 2011) · Antlanger M, et al. BMC Nephrol. 2013",
     "items": [
         ("Weight", "IDWG", "Compare with usual gain; same scale, same clothing."),
         ("Blood pressure", "↑ or ↓", "High pre-HD BP: possible overload. Low: depletion or medicines."),
         ("Edema", "Legs, sacrum", "Pitting edema suggests extracellular overload."),
         ("Lungs", "Crackles, SpO₂", "Dyspnea, orthopnea, crackles: pulmonary congestion."),
         ("Neck veins", "JVP", "Distended jugular veins: volume overload."),
         ("After HD", "Cramps, fatigue", "Repeated symptoms at target: target may be too low."),
     ],
     "notes": """
AREP [Water Treatment / 160831, 155644]. Clinical signs are late and non-specific; combine with weight trends and device data (RBV, bioimpedance) where available (AREP [160905–161309]).
Fluid overload consequences: hypertension, LVH, heart failure, pulmonary edema, increased mortality (Antlanger M, et al. BMC Nephrol 2013;14:266, cited in AREP)."""},

    {"kind": "stacked", "title": "Build the UF volume step by step",
     "source": "Illustrative training data · AREP Fluid Management · local UF policy",
     "chart": {"name": "UF volume composition", "title": "Total planned UF volume for one session (L)",
               "categories": ["Planned UF"],
               "series": [("Weight above target: 3.1 L", [3.1]), ("Planned intake: 0.2 L", [0.2]), ("Rinse-back/saline: 0.3 L", [0.3])],
               "max": 4.0, "labels": False, "h": 2.6, "note": ILLUS},
     "below": ["Mrs L: pre-weight 65.1 kg, target 62.0 kg",
               "Weight above target = 65.1 − 62.0 = 3.1 L",
               "Total UF = 3.1 + 0.2 + 0.3 = 3.6 L (only if local policy adds intake and rinse-back)"],
     "side": {"head": "Units matter", "body": [
         "1 kg weight ≈ 1 L fluid", "UF volume in mL for the rate", "Rate: mL per kg per hour",
         "Which weight for 'kg'? Follow local policy (often target weight)",
         "Saline boluses during HD add to the volume"]},
     "notes": """
Visual 3 (stacked bar). ILLUSTRATIVE TRAINING DATA. Whether oral intake, rinse-back saline and infusions are added to the UF goal is a LOCAL POLICY decision (NEEDS LOCAL CONFIRMATION); the target weight is a physician prescription.
Calculation: 65.1 − 62.0 = 3.1; 3.1 + 0.2 + 0.3 = 3.6 L."""},

    {"kind": "bar_side", "title": "Shorter time means a faster UF rate",
     "source": "Illustrative calculation · Flythe JE, et al. Kidney Int. 2011;79(2):250-257 (observational)",
     "chart": {"name": "UFR by session length", "title": "UF rate for 3.6 L at 62 kg (mL/kg/h)",
               "categories": ["3.0 h", "3.5 h", "4.0 h", "4.5 h", "5.0 h"],
               "series": [("UF rate", [19.4, 16.6, 14.5, 12.9, 11.6])],
               "point_colors": [NAVY, NAVY, BLUE, MID, MID], "max": 22, "fmt": '0.0', "h": 4.55,
               "note": ILLUS + " · calculated: 3,600 mL ÷ (62 kg × hours)"},
     "side": {"head": "How to use this", "body": [
         "Same volume, different time: the rate changes a lot",
         "In observational data, > 13 mL/kg/h was linked to higher mortality",
         "Risk rose above about 10 in heart failure",
         ("No rate is automatically safe: assess the patient", {"bold": True, "color": NAVY}),
         "Options: longer or extra session, target review"]},
     "notes": """
Visual 4 (column chart, calculated). 3600 ÷ (62 × 3) = 19.4; ÷ (62 × 3.5) = 16.6; ÷ (62 × 4) = 14.5; ÷ (62 × 4.5) = 12.9; ÷ (62 × 5) = 11.6 mL/kg/h.
[WEB] Flythe JE, et al. Kidney Int 2011;79(2):250-257 (HEMO post hoc, observational): UFR > 13 vs ≤ 10 mL/kg/h adjusted HR 1.59 all-cause, 1.71 CV mortality; 10–13 associated with mortality only in heart failure; spline suggested risk rising above ~10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3091945 (""" + ACCESSED + """).
Do NOT present 13 mL/kg/h as a safety limit: it is an association; tolerance depends on cardiac function, refill, residual function, intake, and the prescription."""},

    {"kind": "two_cards", "title": "Who is at higher risk during fluid removal?",
     "source": "Kooman J, et al. EBPG 2007 · Flythe JE, et al. 2011 · AREP Fluid Management",
     "h": 3.7,
     "cards": [
         ("Patient factors", ["Heart failure, ischemic heart disease", "Diabetes with autonomic neuropathy", "Older age, low muscle mass, low albumin",
                              "Previous intradialytic hypotension", "Antihypertensives taken before HD"]),
         ("Treatment factors", ["High IDWG and short session (high UFR)", "Target weight set too low", "Warm or low-sodium dialysate",
                                "Eating during HD in prone patients", "Missed or shortened previous session"]),
     ],
     "banner": "Same UF goal, different patients: plan and monitor each one individually",
     "notes": "Risk factors per EBPG on haemodynamic instability (Kooman J, et al. NDT 2007; not accessed online – textbook-level knowledge, NEEDS REVIEW) and AREP UF rate slides [Water Treatment / 160132–160218]."},

    {"kind": "stat_cards", "title": "Intradialytic hypotension (IDH): what counts",
     "source": "K/DOQI CVD in Dialysis 2005 (via Clin Kidney J 2020 review) · definitions vary",
     "stats": [("≥ 20 mmHg", "fall in systolic BP (KDOQI 2005)"), ("≥ 10 mmHg", "fall in mean arterial pressure"), ("+ symptoms", "or need for nursing intervention"), ("< 90 mmHg", "low nadir SBP: strongest mortality link in studies")],
     "cards": [
         ("Early warning signs", ["Yawning, sighing, restlessness", "Dizziness, blurred vision", "Nausea, cramps, sweating", "Chest pain, confusion"]),
         ("Monitor", ["BP and pulse at set intervals", "More often in high-risk patients", "Relative blood volume trend if available"]),
         ("Why it matters", ["Heart, brain and gut ischemia", "Incomplete treatment and UF", "Loss of residual kidney function"]),
     ],
     "notes": """
[WEB] KDOQI 2005 definition: SBP fall ≥ 20 mmHg or MAP fall ≥ 10 mmHg associated with symptoms (or need for intervention). Other definitions exist (e.g. UK Renal Association 2011); low nadir SBP < 90 mmHg correlated more strongly with mortality in some studies. Source: Clin Kidney J 2020 review https://academic.oup.com/ckj/article/13/6/981/5868598 (""" + ACCESSED + """).
Monitoring frequency per local policy and machine IFU."""},

    {"kind": "line_chart", "title": "Spot the trend before the patient collapses",
     "source": "Illustrative training data",
     "chart": {"name": "Intradialytic BP trend", "title": "Systolic BP during one session (mmHg)",
               "categories": ["0", "30", "60", "90", "120", "150", "180", "210"],
               "series": [("Systolic BP", [146, 140, 131, 124, 116, 104, 88, 112], BLUE),
                          ("Pre-dialysis SBP − 20 mmHg", [126] * 8, GREY, True)],
               "min": 80, "max": 160, "major": 10, "y_title": "mmHg", "x_title": "Minutes on dialysis", "labels": True, "note": ILLUS},
     "side": {"head": "Teaching points", "body": [
         "Steady fall from 60 min: rising risk", "Crossed the −20 mmHg line at 120 min",
         "Symptoms at 180 min (88 mmHg): IDH", "210 min: recovered after UF stop and saline",
         ("Act on the trend and symptoms, early", {"bold": True, "color": NAVY})]},
     "notes": "Visual 5 (line chart). ILLUSTRATIVE TRAINING DATA. Dashed line = pre-dialysis SBP minus 20 mmHg (KDOQI 2005 threshold when symptomatic). Discuss which earlier actions could have prevented the 180-min episode (UF review, earlier reassessment)."},

    {"kind": "algorithm", "title": "IDH: first response, reassess, escalate",
     "source": "Kooman J, et al. EBPG 2007 · Handbook of Dialysis 2015 · local standing orders",
     "w": 5.4, "no_w": 3.2,
     "nodes": [
         {"t": "start", "text": "Symptoms or BP fall during HD"},
         {"t": "action", "text": "Check BP, pulse, consciousness; stay with patient"},
         {"t": "action", "text": "Flat / legs raised; stop or reduce UF"},
         {"t": "action", "text": "Saline bolus per standing order; O₂ if hypoxic"},
         {"t": "decision", "text": "Improving in minutes?", "no": "Call physician now; consider emergency (L07); prepare to end treatment per order"},
         {"t": "end", "text": "Resume UF cautiously per order; document; review plan"},
     ],
     "side": {"head": "Avoid", "fill": "navy", "body": [
         "Leaving the patient", "Restarting full UF before recovery", "Missing chest pain or hypoglycemia",
         "Adding saline to the UF goal without an order"]},
     "notes": """
Visual 6 (algorithm). Typical stepwise IDH management (EBPG 2007; Handbook of Dialysis 2015) – EBPG text not accessed online during preparation; steps are standard nursing practice: NEEDS REVIEW against the local IDH protocol.
Saline volume, oxygen use, blood-flow reduction and when to end treatment must follow local standing orders and physician prescription (nurse's authorised scope).
'Yes' continues down; 'No' branches right."""},

    {"kind": "two_cards", "title": "Prevent the next episode and teach the patient",
     "source": "Kooman J, et al. EBPG 2007 · KDIGO BP in CKD 2012 · AREP Fluid Management",
     "h": 3.7,
     "cards": [
         ("Team actions (physician-led)", ["Reassess target weight", "Longer or extra sessions to lower UF rate", "Cooler dialysate (e.g. 0.5 °C below body temp.)",
                                            "Avoid low dialysate sodium", "Review antihypertensive timing"]),
         ("Patient education", ["Salt < 2 g sodium/day (KDIGO): less thirst", "Fluid allowance as advised (anuric: ~1.0–1.5 L/day)",
                                "Spread drinks; ice chips, sugar-free sweets", "Weigh daily at home if possible", "Report dizziness early"]),
     ],
     "banner": "Repeated IDH is a signal: report the pattern, not only the single event",
     "notes": """
Prevention: EBPG 2007 (not accessed online – NEEDS REVIEW); cool dialysate example 0.5 °C below body temperature.
Education: KDIGO 2012 BP guideline (< 2 g sodium/day); AREP [Water Treatment / 155835–155900]: anuric patients generally 1.0–1.5 L/day; anuric HD patients with sodium-induced thirst drink ~1 L water per 8 g salt (as cited by AREP)."""},

    {"kind": "checklist", "title": "UF safety checklist",
     "source": "Summary aid compiled from Lectures 01–02 · adapt to local policy",
     "row_h": 0.55, "size": 12, "h": 4.95,
     "columns": [
         ("Before start", ["Weight on correct scale", "IDWG compared with usual", "Fluid signs assessed", "UF volume and rate calculated", "High-risk factors flagged"]),
         ("During", ["BP/pulse at set intervals", "Symptoms asked, not waited for", "RBV trend if available", "UF paused if symptoms", "Saline per standing order only"]),
         ("After", ["Post-weight vs target", "Symptoms recorded", "IDH episodes documented", "Pattern reported", "Education given and recorded"]),
     ],
     "notes": "Summary aid. Print as a pocket card or include in the treatment record."},

    {"kind": "case", "title": "Case: plan today's fluid removal",
     "source": "Fictional teaching case (illustrative training data)",
     "case": [
         "Mr N, 70 years, heart failure. Target weight 68.0 kg. Session 4 h.",
         "Pre-weight 72.0 kg (previous post 68.4). BP 162/90, crackles at bases, SpO₂ 94%.",
         "Last two sessions: cramps and BP 86/50 in the final hour.",
         "He drank 0.3 L during the last session; rinse-back is 0.3 L."],
     "questions": [
         "Calculate IDWG, UF volume and UF rate (4 h).",
         "Interpret: overloaded, depleted, or both at different times?",
         "Propose a UF plan to discuss with the physician.",
         "What will you monitor, and when will you escalate?"],
     "notes": """
Suggested answers (illustrative):
1. IDWG = 72.0 − 68.4 = 3.6 kg. Weight above target = 4.0 L; with intake 0.3 + rinse-back 0.3 (if policy adds them) = 4.6 L. UFR = 4600 ÷ (68 × 4) = 16.9 mL/kg/h (4.0 L only: 14.7).
2. Overloaded now (BP, crackles) but hypotensive late in sessions: UF too fast and/or target possibly too low for refill; heart failure limits tolerance.
3. Discuss: longer session or extra session, accept partial UF today, review target weight, antihypertensive timing, cool dialysate, salt/fluid education.
4. BP/pulse more often, symptoms, SpO₂, RBV if available; escalate for SpO₂ fall, chest pain, symptomatic hypotension not responding."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("UF 3.0 L, weight 60 kg, 4 h. UF rate?", ["A. 8.3 mL/kg/h", "B. 12.5 mL/kg/h", "C. 15.0 mL/kg/h", "D. 50 mL/kg/h"]),
         ("Same UF in 3 h instead of 4 h: the UF rate…", ["A. falls by 25%", "B. stays the same", "C. rises by about one third", "D. doubles"]),
         ("First nursing action for symptomatic IDH?", ["A. Increase blood flow", "B. Position flat/legs up and stop UF", "C. Give antihypertensive", "D. End the session immediately"]),
         ("Which statement is correct?", ["A. Below 13 mL/kg/h is always safe", "B. UFR tolerance is individual", "C. IDWG does not matter", "D. Target weight never changes"]),
     ],
     "notes": """
Q1 B – 3000 ÷ (60 × 4) = 12.5 mL/kg/h.
Q2 C – rate ∝ 1/time: 4/3 = 1.33, about one third higher.
Q3 B – position and stop/reduce UF first, then saline per standing order; increasing Qb or giving antihypertensives is wrong; ending the session is a physician decision if no response.
Q4 B – thresholds are population associations (Flythe 2011); target weight is reassessed regularly."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 02 summary",
     "items": [
         ("Weight trends tell the story", "IDWG, post-weight vs target, and symptoms together."),
         ("Calculate with units", "UF volume in mL; UF rate in mL/kg/h; know what policy adds."),
         ("No universal safe UF rate", "> 13 mL/kg/h is an observational warning, not a guarantee below it."),
         ("Respond to IDH in order", "Check, position, stop UF, saline per order, reassess, escalate."),
         ("Prevent and educate", "Report patterns; teach salt and fluid habits."),
     ],
     "notes": "Bridge to Day 2: vascular access and infection control."},

    refs_slide(),
]
