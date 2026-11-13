# -*- coding: utf-8 -*-
"""Lecture 01 - Day 1: Pre-Dialysis Patient Assessment and Prescription Verification."""
from lectures._common import *  # noqa: F401,F403

SLUG = "PreDialysis_Assessment"
TITLE = "Pre-Dialysis Patient Assessment and Prescription Verification"
SUBTITLE = "Day 1 · Patient Assessment & Safety · Lecture 01"
FOOTER_TEXT = "L01 Pre-dialysis assessment"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 01 of the 4-day Hemodialysis Nursing Programme (Day 1: Patient Assessment & Safety). 45–60 minutes.
Audience: dialysis nurses. Goal: a safe, repeatable pre-treatment routine – assess the patient, verify the prescription and confirm the machine and dialysate are ready before connection.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 01",
     "items": [
         ("Assess", ["Perform a structured pre-dialysis assessment", "Interpret weight and fluid gain"]),
         ("Detect", ["Recognise red flags that delay the start", "Escalate with SBAR"]),
         ("Verify", ["Check every prescription parameter", "Match concentrate and dialyzer"]),
         ("Confirm", ["Complete machine safety checks", "Document before connection"]),
     ],
     "notes": "Four objectives map to the four parts of the routine used on every treatment day."},

    {"kind": "flow", "title": "Every treatment starts with the same safety routine",
     "source": "CMS ESRD Conditions for Coverage, 42 CFR 494 · KDOQI 2015 · Garrick R, et al. Clin J Am Soc Nephrol. 2012;7(4):680-688",
     "steps": [
         ("1 Identify", ["Two patient identifiers", "Allergies, isolation status"]),
         ("2 Assess", ["Weight, vital signs, fluid", "Access and interval history"]),
         ("3 Verify", ["Prescription vs. orders", "Concentrate, dialyzer, heparin"]),
         ("4 Check & start", ["Machine tests passed", "Conductivity, pH, temperature"]),
     ],
     "bottom_left": {"head": "Why a fixed routine?", "body": [
         "Most HD emergencies are linked to human error",
         "Problems found before connection are easiest to fix",
         "Same order every time: nothing is skipped"]},
     "bottom_right": {"head": "Do not start until", "items": [
         "Red flags are escalated and answered", "Prescription and machine settings match",
         "Independent dialysate checks are within range"]},
     "notes": """
The routine: identify → assess → verify → check and start. Each step has its own slide.
Saha & Allon (CJASN 2017) note that most HD emergencies can be attributed to human error; structured checks are the main defence (see also Garrick R, et al. CJASN 2012;7(4):680-688).
CMS ESRD Conditions for Coverage (42 CFR Part 494) require patient assessment, a plan of care and safe water/dialysate. Two-identifier patient identification follows common patient-safety standards (e.g. Joint Commission NPSG) – apply your national equivalent."""},

    {"kind": "checklist", "title": "What to assess before every treatment",
     "source": "ANNA Core Curriculum for Nephrology Nursing. 2015 · AREP Fluid Management · Lok CE, et al. KDOQI Vascular Access 2019",
     "row_h": 0.55, "size": 13, "h": 4.25,
     "columns": [
         ("Vital signs and weight", ["Pre-dialysis weight (same scale)", "BP sitting/standing if at risk", "Pulse, rhythm, temperature", "Respiratory rate, SpO₂", "Blood glucose if diabetic"]),
         ("Fluid and symptoms", ["Edema, lung sounds, dyspnea", "Jugular veins, orthopnea", "Chest pain, palpitations", "Cramps or hypotension last time", "Appetite, nausea, pruritus"]),
         ("Access and interval history", ["Look, listen, feel the access", "CVC exit site and dressing", "Bleeding, falls, new illness", "Hospital visits, new medicines", "Missed or shortened sessions"]),
     ],
     "banner": "Compare with the patient's own baseline and the last treatment record, not only with normal values",
     "notes": """
Structured pre-dialysis assessment (ANNA Core Curriculum 2015; AREP Fluid Management: clinical evaluation before, during and after dialysis – edema, dyspnea, ↑ body weight, ↑ BP, turgid jugular veins, pulmonary congestion [Water Treatment / 160831]).
Access assessment: look, listen, feel before every cannulation (KDOQI 2019; AREP [vascular access / 153406, 153427]).
Orthostatic BP is recommended by AREP as a falls-prevention measure [Dialysis / 145139].
Trend matters: a change from the patient's usual values is often the earliest warning."""},

    {"kind": "formula", "title": "Turn the weight into a safe UF goal",
     "source": "AREP Fluid Management · Flythe JE, et al. Kidney Int. 2011;79(2):250-257 · KDOQI 2015",
     "formulas": [
         ("Interdialytic weight gain (IDWG)", "pre-weight − previous post-weight", "Shows intake since the last session"),
         ("Ultrafiltration (UF) goal", "pre-weight − target (dry) weight", "Add local allowances (e.g. rinse-back, intake) only per policy"),
         ("UF rate (mL/kg/h)", "UF goal (mL) ÷ [target weight (kg) × time (h)]", "> 13 mL/kg/h: associated with higher mortality"),
     ],
     "example": {"head": "Worked example (educational)", "body": [
         "Previous post-weight 70.8 kg; today 73.0 kg",
         "IDWG = 73.0 − 70.8 = 2.2 kg",
         "Target weight 70.5 kg → UF goal 2.5 kg",
         "4-hour session: 2,500 ÷ (70.5 × 4) = 8.9 mL/kg/h",
         ("If the goal needs > 13 mL/kg/h: discuss longer time, extra session or target review", {"bold": True, "color": NAVY, "space_after": 4}),
         ("Check: same scale, similar clothing, no added items", {"size": 12, "space_after": 2})]},
     "notes": """
Weight-based calculations are the most common source of fluid errors; recalculate and double-check.
IDWG = pre-dialysis weight minus post-dialysis weight of the previous session. UF goal = pre-weight minus target (dry) weight; local policies may add rinse-back saline or intake during treatment.
UFR > 13 mL/kg/h was associated with higher all-cause (HR 1.59) and cardiovascular mortality (HR 1.71) in the HEMO post hoc analysis (Flythe JE, et al. Kidney Int. 2011;79(2):250-257) – observational. Some formulas use post-dialysis (target) weight as denominator – follow local convention.
Worked example values are a CALCULATED TEACHING EXAMPLE, not patient data. Lecture 02 covers UF safety in depth."""},

    {"kind": "matrix", "title": "Red flags: pause and escalate before starting",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · KDOQI Vascular Access 2019 · CDC MMWR 2001;50(RR-5)",
     "rows": [
         ("Cardio-respiratory", "Chest pain, new dyspnea, low SpO₂, new arrhythmia, very low or very high BP", "Call physician now; do not start until reviewed"),
         ("Fluid", "IDWG far above usual, crackles, orthopnea, edema", "Notify; review UF goal, time and target weight"),
         ("Infection", "Fever, rigors, redness or pus at access or CVC exit site", "Notify; cultures per protocol; do not cannulate infected site"),
         ("Access", "No thrill or bruit, new swelling, CVC not aspirating", "Do not cannulate or force; notify for assessment"),
         ("Labs / meds", "Critical potassium or Hb, new anticoagulant, active bleeding", "Notify; confirm anticoagulation and dialysate before start"),
     ],
     "fills": ["navy", "blue", "mid", "blue", "grey"],
     "notes": """
These are TYPICAL TRIGGERS for escalation; numeric thresholds (e.g. BP, SpO₂, potassium) must be defined in the unit protocol.
- Absent thrill/bruit suggests thrombosis – cannulation can cause hematoma or clot embolisation; refer per KDOQI 2019.
- Infected access sites should not be cannulated; obtain blood cultures and inform the physician (CDC MMWR 2001; NHSN dialysis event surveillance).
- Hyperkalemia is a common dialysis emergency: the physician may change dialysate potassium or urgency (Saha & Allon 2017).
Use SBAR to escalate (slide 10)."""},

    {"kind": "two_cards", "title": "Review labs and medications that change the plan",
     "source": "KDOQI 2015 · Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · ANNA Core Curriculum 2015",
     "h": 3.7,
     "cards": [
         ("Laboratory results", ["Potassium: matches dialysate K bath?", "Hemoglobin: bleeding or anemia trend", "Calcium, phosphate, bicarbonate trends",
                                 "Hepatitis B status: station assignment", "Recent blood culture results"]),
         ("Medications and history", ["Anticoagulants, antiplatelets: heparin dose", "Heparin allergy or HIT history", "Antihypertensives taken before HD?",
                                      "Insulin, hypoglycemia risk", "ESA, iron, vitamin D due this session"]),
     ],
     "banner": "Any mismatch between results and the prescription: clarify with the physician before starting",
     "notes": """
Laboratory and medication review is part of the pre-treatment assessment (ANNA 2015).
- Dialysate potassium must fit the serum potassium; wrong K bath is a recognised cause of arrhythmia (Saha & Allon 2017).
- Hepatitis B status determines isolation and station assignment (CDC MMWR 2001) – covered in Lecture 04.
- Heparin-induced thrombocytopenia (HIT) history requires heparin-free anticoagulation per physician order.
- Antihypertensives before HD may contribute to intradialytic hypotension (Lecture 02)."""},

    {"kind": "table_only", "title": "Verify every prescription parameter",
     "source": "KDOQI 2015 · CMS ESRD Conditions for Coverage, 42 CFR 494 · Machine IFU",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.7, 4.6, 4.75], "row_h": 0.5, "size": 12,
               "rows": [["Parameter", "Verify", "Typical error"],
                        ["Patient", "Two identifiers; correct record and machine", "Wrong patient's settings or dialyzer"],
                        ["Dialyzer and lines", "Type and size as ordered; integrity; expiry", "Wrong dialyzer surface area or flux"],
                        ["Time", "Prescribed duration entered", "Session shortened, not recorded"],
                        ["Blood and dialysate flow", "Qb target; Qd as ordered", "Low Qb from needle or access issues"],
                        ["Dialysate", "K, Ca, Na, HCO₃ and temperature", "Wrong acid concentrate (K or Ca)"],
                        ["UF goal / rate", "Calculated from today's weight; UFR checked", "Calculation or weight-entry error"],
                        ["Anticoagulation", "Drug, bolus, infusion, stop time", "Dose error; heparin given when contraindicated"],
                        ["Access and needles", "Access type, needle gauge, cannulation plan", "Gauge too small for Qb"]]},
     "banner": "Read back: prescription → machine screen → treatment record. All three must match",
     "banner_y": 6.0,
     "notes": """
Prescription components per KDOQI 2015 adequacy guideline and ANNA: dialyzer, time, blood flow, dialysate flow and composition, UF, anticoagulation.
Wrong acid concentrate (potassium/calcium) is a known, preventable error; many units use a second-person check – follow local policy.
Needle gauge must match the blood flow rate (Lecture 03; NKF Clinical Update 2016).
Exact parameter names and entry screens depend on the machine model: follow the FMC machine IFU."""},

    {"kind": "image_two_lists", "title": "Machine and dialysate checks before connection",
     "source": "CMS 42 CFR 494.40 · ISO 23500 series · Fresenius Medical Care machine IFU",
     "image": "hd_circuit.png", "image_alt": "Hemodialysis blood circuit diagram (AREP)",
     "caption": "Blood circuit illustration: FMC AREP, Introduction to Hemodialysis (uploaded screenshot)",
     "lists": [
         ("Machine ready", ["Self-test and alarm checks passed", "Residual disinfectant test negative", "Lines primed, no air; clamps correct",
                            "Transducer protectors dry and connected"], "blue"),
         ("Dialysate ready", ["Acid and bicarbonate match prescription", "Conductivity and pH checked independently",
                              "Temperature as prescribed", "Never override a conductivity alarm"], "navy"),
     ],
     "notes": """
Pre-treatment machine checks follow the machine IFU (self-test, pressure holding and alarm tests). Residual disinfectant must be confirmed absent after chemical disinfection before the patient is connected.
CMS (42 CFR 494) and AAMI/ISO practice: verify dialysate conductivity and pH with an independent method before each treatment, and confirm that concentrates match the prescription. Wet transducer protectors must be replaced (blood-borne pathogen risk; CDC MMWR 2001).
NEEDS LOCAL CONFIRMATION: exact check sequence and acceptable ranges come from the FMC machine IFU and local policy."""},

    {"kind": "steps", "title": "Escalate clearly: use SBAR",
     "source": "Institute for Healthcare Improvement. SBAR tool · Garrick R, et al. Clin J Am Soc Nephrol. 2012;7(4):680-688",
     "steps": [
         ("Situation", "\"Mr A, bed 4, pre-dialysis BP 82/50 and dizzy.\""),
         ("Background", "\"HD three times weekly, target 70.5 kg, IDWG 1.0 kg, new antihypertensive.\""),
         ("Assessment", "\"I think he is volume depleted or over-treated. I have not started.\""),
         ("Recommendation", "\"Please review UF goal and medication before I connect.\""),
     ],
     "side": {"head": "Then document", "body": [
         "Findings and time", "Who was informed and when", "Orders received (read back)", "Actions taken and patient response"]},
     "notes": """
SBAR (Situation, Background, Assessment, Recommendation) is a structured communication tool (IHI). Safety culture and communication are core to HD patient safety (Garrick R, et al. CJASN 2012).
The example is fictional. Read back verbal orders and document them according to local policy."""},

    {"kind": "case", "title": "Case: is this patient ready to start?",
     "source": "Fictional teaching case",
     "case": [
         "Mrs B, 68 years, AVF left forearm, diabetic. Target weight 62.0 kg.",
         "Pre-weight 65.6 kg (previous post 62.4 kg). BP 168/92, SpO₂ 93% on air, crackles at both bases.",
         "Prescription on machine: 4 h, Qb 350 mL/min, dialysate K 3.0. Today's lab K⁺ 3.2 mmol/L.",
         "Thrill present. She took her insulin and has not eaten."],
     "questions": [
         "Calculate IDWG, UF goal and UFR for 4 h. What concerns you?",
         "Which findings need escalation before you start?",
         "What would you verify in the prescription and why?",
         "Which other safety check is needed for this diabetic patient?"],
     "notes": """
Suggested answers (educational):
1. IDWG = 65.6 − 62.4 = 3.2 kg; UF goal = 65.6 − 62.0 = 3.6 kg; UFR = 3600 ÷ (62 × 4) = 14.5 mL/kg/h → above 13 mL/kg/h; discuss longer or additional session.
2. Signs of fluid overload with SpO₂ 93% and crackles → notify physician before starting; monitor respiratory status.
3. Dialysate K 3.0 with serum K 3.2 mmol/L – low serum K; check whether a higher K bath is intended (arrhythmia risk). Confirm with physician.
4. Insulin taken and not eaten → check blood glucose before and during treatment per protocol."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 01 summary",
     "items": [
         ("Same routine, every patient, every time", "Identify, assess, verify, check, then start."),
         ("Compare with the patient's own baseline", "Weight, BP and symptoms are interpreted against previous sessions."),
         ("Calculate the UF goal and the UF rate", "Flag UFR > 13 mL/kg/h before connection."),
         ("Prescription = machine = record", "Concentrate, dialyzer, flows, time and anticoagulation must match."),
         ("Escalate red flags with SBAR", "Do not start until concerns are answered and documented."),
     ],
     "notes": "Summarise. Link to Lecture 02 (fluid assessment, UF safety and hypotension)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["kdoqi_adeq"], R["kdoqi_va"], R["cms_cfc"], R["cdc_2001"], R["saha"], R["flythe"], R["garrick"],
              R["anna"], R["handbook"], R["iso23500"], "Institute for Healthcare Improvement. SBAR Tool: Situation-Background-Assessment-Recommendation.",
              R["arep"], R["ifu"]],
     "notes": "References for Lecture 01."},
]
END_NOTES = END_NOTES
