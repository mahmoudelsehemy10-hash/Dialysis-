# -*- coding: utf-8 -*-
"""Day 1 · Lecture 01: Pre-Dialysis Patient Assessment and Prescription Verification."""
from program._common import *  # noqa: F401,F403

TITLE = "Pre-Dialysis Patient Assessment and Prescription Verification"
SUBTITLE = "Day 1 · Patient Assessment & Safety · Lecture 01"
FOOTER_TEXT = "Day 1 · Lecture 01"
REFS = ["KDOQI_ADEQ15", "KDOQI_VA19", "CFR494", "CDC_2001", "SAHA17", "FLYTHE11", "GARRICK12", "IHI_SBAR",
        "ANNA", "HANDBOOK", "AREP_HD", "AREP_VA", "AREP_FM", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 1, Lecture 01 (30–40 min incl. discussion). Audience: HD nurses with mixed experience.
Flow: opening scenario (3 min) → routine and assessment (10 min) → prescription verification (10 min) → red flags and escalation (7 min) → case and knowledge check (8 min).
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 01 objectives",
     "items": [
         ("Identify", ["Confirm patient identity with two identifiers", "State isolation and allergy status"]),
         ("Assess", ["Perform a structured pre-dialysis assessment", "Calculate IDWG and UF goal"]),
         ("Verify", ["Match every prescription parameter to machine and record", "Confirm concentrate and anticoagulation"]),
         ("Escalate", ["Recognise 5 red flags that stop the start", "Report a discrepancy using SBAR"]),
     ],
     "notes": "Objectives are measurable: by the end, the nurse can perform and document each step on the checklist (slide 14) and pass the knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening scenario: ready to connect?",
     "source": "Fictional teaching scenario",
     "story": ["Bed 6 is primed. The machine shows dialysate potassium 2.0 mmol/L.",
               "The printed prescription says 3.0. The patient says: \"I felt my heart racing last night.\""],
     "prompts": ["Which source do you trust: machine, paper or patient?", "What do you check before you touch the access?", "Who needs to know, and how fast?"],
     "notes": """
Ask the group to answer in pairs (2 minutes). Expected discussion:
- None of the three alone: a discrepancy between machine and prescription must be resolved before starting.
- Check identity, latest potassium result, ECG/pulse, medications (e.g. digoxin), and the active order.
- Notify the nurse in charge/physician before connection; document. This scenario returns as the main case (slide 15)."""},

    {"kind": "pathway", "title": "One routine for every patient, every treatment",
     "source": "CMS 42 CFR 494 · KDOQI 2015 · Garrick R, et al. Clin J Am Soc Nephrol. 2012",
     "nodes": [("1 Identify", "2 identifiers, allergies, isolation"), ("2 Assess", "history, vitals, weight, fluid, access"),
               ("3 Review", "labs and medicines"), ("4 Verify", "prescription vs machine vs record"),
               ("5 Check", "machine, dialysate, lines"), ("6 Start", "only when all match")],
     "markers": [(0, "Wristband/record match; HBsAg status decides the station"), (1, "Compare with the patient's own baseline"),
                 (2, "Potassium, Hb, anticoagulants, antihypertensives"), (3, "Read-back: order = machine = treatment record"),
                 (4, "Alarm tests passed, conductivity and pH independently checked"), (5, "Any doubt: pause and escalate (slide 11)")],
     "notes": """
Visual 1 (workflow). Six steps in a fixed order so nothing is skipped. Most hemodialysis emergencies are linked to human error (Saha & Allon, CJASN 2017 – secondary summary), and safety culture depends on standard processes (Garrick R, et al. CJASN 2012;7(4):680-688, cited in AREP [Dialysis / 145115]).
US CMS ESRD Conditions for Coverage (42 CFR 494) require assessment and safe water/dialysate; apply the national equivalent (Saudi MOH IPC auditor guide includes an HD unit element – see Source Register)."""},

    {"kind": "two_cards", "title": "Identify the patient and take a focused history",
     "source": "Joint Commission-type patient identification practice · CDC MMWR 2001;50(RR-5) · ANNA Core Curriculum 2015",
     "h": 3.7,
     "cards": [
         ("Identification", ["Two identifiers: name + date of birth or ID number", "Match wristband, record, prescription, machine",
                             "Allergies (including heparin, latex, dialyzer)", "Hepatitis B status: assigns station and staff",
                             "Advance care or special instructions"]),
         ("Since the last session", ["Breathlessness, chest pain, palpitations", "Dizziness, falls, cramps after last HD",
                                     "Bleeding, new bruising, procedures", "Fever, access pain or discharge",
                                     "Hospital visits, new or stopped medicines"]),
     ],
     "banner": "Ask open questions first: \"How have you been since your last dialysis?\"",
     "notes": """
Two-identifier patient identification is a standard patient-safety requirement (e.g. Joint Commission NPSG; apply the Saudi/organisational equivalent – NEEDS LOCAL CONFIRMATION of the approved identifiers).
HBsAg status determines station, machine and staff assignment (CDC MMWR 2001 – Lecture 04).
History items follow ANNA Core Curriculum pre-treatment assessment."""},

    {"kind": "checklist", "title": "Vital signs, weight and fluid: compare with baseline",
     "source": "AREP Fluid Management (Lindley E, et al. 2011) · ANNA Core Curriculum 2015",
     "row_h": 0.58, "size": 13, "h": 4.25,
     "columns": [
         ("Measure", ["BP and pulse (sitting; standing if at risk)", "Temperature, respiratory rate, SpO₂", "Pre-dialysis weight, same scale", "Blood glucose if diabetic"]),
         ("Look for fluid signs", ["Edema: legs, sacrum, face", "Crackles, orthopnea, dyspnea", "Distended neck veins", "BP far above usual"]),
         ("Compare", ["Last pre- and post-weight", "Target (dry) weight in the order", "Usual BP range for this patient", "Last session's problems"]),
     ],
     "banner": "A value is only abnormal or normal compared with this patient's own trend",
     "notes": """
AREP [Water Treatment / 160831]: clinical evaluation before, during and after dialysis – edema, dyspnea, ↑ body weight, ↑ BP, turgid jugular vein, pulmonary congestion; helps guide UF rate and dry weight.
Orthostatic BP for fall-risk patients: AREP best practices [Dialysis / 145139].
Weight: same scale, similar clothing; record items such as prosthesis or wheelchair."""},

    {"kind": "rule6", "title": "Quick vascular access check before every use",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019 · AREP Vascular Access",
     "lead": "AVF/AVG: look, listen, feel. CVC: look, check, never force.",
     "sixes": [("Look", "swelling, redness, aneurysm"), ("Listen", "continuous low-pitched bruit"), ("Feel", "thrill, pulse, warmth"), ("CVC", "exit site, dressing, clamps")],
     "left": {"head": "Stop and report if", "body": ["No thrill or bruit (possible thrombosis)", "Redness, pus, fever (possible infection)", "New arm swelling or hand pain/coldness"]},
     "right": {"head": "Then plan cannulation", "body": ["Sites, direction, needle gauge for Qb", "Who cannulates (competency)", "Details in Lecture 03"]},
     "notes": """
KDOQI 2019 physical examination (AREP [vascular access / 153406, 153427]). Physical exam detects stenosis with PPV 70–80% in AVGs and 93% in AVFs (as reported in AREP).
This is the pre-dialysis screen only; full access care is Lecture 03."""},

    {"kind": "table_only", "title": "Labs and medicines that change today's plan",
     "source": "KDOQI 2015 · Saha M, Allon M. Clin J Am Soc Nephrol. 2017 · ANNA Core Curriculum 2015",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.9, 4.4, 4.75], "row_h": 0.6, "size": 12,
               "rows": [["Item", "Why it matters", "Nurse action"],
                        ["Potassium", "Dialysate K bath must fit the serum value", "Check result date; query K bath if mismatch"],
                        ["Hemoglobin", "Bleeding, anemia, ESA dosing", "Report a fall; check bleeding history"],
                        ["HBsAg / viral status", "Station and staff assignment", "Confirm current result is on file"],
                        ["Anticoagulants, antiplatelets", "Heparin dose, bleeding after needles", "Confirm heparin order; report recent procedures"],
                        ["Antihypertensives", "Risk of low BP during HD", "Record timing; report if taken before HD and BP low"],
                        ["Insulin / oral hypoglycemics", "Hypoglycemia during HD", "Check glucose per protocol"],
                        ["Digoxin, antiarrhythmics", "Low potassium raises arrhythmia risk", "Flag with low K bath; escalate"]]},
     "notes": """
Wrong dialysate potassium for the serum level is a recognised and preventable cause of arrhythmia (Saha & Allon, CJASN 2017 – secondary summary; Handbook of Dialysis).
Interaction between hypokalemia and digoxin toxicity is standard pharmacology – escalate to physician.
Numeric 'critical' lab values are set by the local laboratory/protocol (NEEDS LOCAL CONFIRMATION)."""},

    {"kind": "table_only", "title": "Verify the prescription: parameter by parameter",
     "source": "KDOQI 2015 · CMS 42 CFR 494 · Machine IFU",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.75, 4.5, 4.8], "row_h": 0.5, "size": 12,
               "rows": [["Parameter", "Check against the active order", "Typical error to catch"],
                        ["Modality", "HD or HDF; single or double needle", "Wrong program selected"],
                        ["Duration", "Prescribed time entered", "Shortened time not recorded"],
                        ["Blood flow (Qb)", "Target Qb; achievable with access/needles", "Qb limited by needle gauge"],
                        ["Dialysate flow (Qd)", "As ordered", "Default value left unchanged"],
                        ["Dialysate composition", "K, Ca, Na, HCO₃, temperature", "Wrong acid concentrate (K or Ca)"],
                        ["Dialyzer", "Type and surface area", "Different dialyzer after stock change"],
                        ["Anticoagulation", "Drug, bolus, infusion, stop time", "Dose error, contraindication missed"],
                        ["Fluid removal", "UF goal from today's weight; UF rate", "Weight entry or calculation error"]]},
     "banner": "Read back: order → machine screen → treatment record. All three must match",
     "banner_y": 6.0,
     "notes": """
Prescription elements: KDOQI 2015 adequacy (time, blood flow, dialyzer), dialysate composition, anticoagulation and UF.
Modality and screens depend on the machine (e.g. HD vs online HDF): follow the FMC machine IFU in local use (not uploaded – NEEDS LOCAL CONFIRMATION)."""},

    {"kind": "formula", "title": "Calculate fluid removal before connection",
     "source": "AREP Fluid Management · Flythe JE, et al. Kidney Int. 2011;79(2):250-257",
     "formulas": [
         ("Interdialytic weight gain (IDWG, kg)", "pre-weight − previous post-weight", "1 kg of weight gain ≈ 1 L of fluid"),
         ("UF goal (L)", "pre-weight − target weight (+ planned intake, rinse-back per policy)", "Target weight is a physician prescription"),
         ("UF rate (mL/kg/h)", "UF goal (mL) ÷ [target weight (kg) × time (h)]", "Report rates that are high for this patient"),
     ],
     "example": {"head": "Worked example (illustrative training data)", "body": [
         "Previous post-weight 70.8 kg; today 73.0 kg",
         "IDWG = 73.0 − 70.8 = 2.2 kg",
         "Target 70.5 kg: UF goal = 73.0 − 70.5 = 2.5 L",
         "4 h: 2,500 mL ÷ (70.5 kg × 4 h) = 8.9 mL/kg/h",
         ("No single UF rate is 'safe' for everyone: Lecture 02", {"bold": True, "color": NAVY, "space_after": 4})]},
     "notes": """
Formulas: AREP Fluid Management; UF rate expressed per kg per hour as in Flythe JE, et al. Kidney Int 2011 (observational association of higher UFR with mortality).
Worked example: illustrative training data (calculated: 2500 / (70.5 × 4) = 8.87 mL/kg/h).
Local policy decides whether rinse-back saline, oral intake or infusions are added to the UF goal, and which weight is used in the denominator."""},

    {"kind": "image_two_lists", "title": "Machine and dialysate ready: confirm independently",
     "source": "AREP Introduction to Hemodialysis (Ahmad S, et al. Handbook of Dialysis 2015) · CMS 42 CFR 494.40 · Machine IFU",
     "image": "dialysate_circuit.png", "image_alt": "Dialysate circuit: acid and bicarbonate concentrates, mixer, heater, conductivity and temperature monitors, blood leak detector (AREP)",
     "caption": "Dialysate circuit with conductivity and temperature monitors. Source: FMC AREP, Introduction to Hemodialysis (uploaded screenshot 141056)",
     "lists": [
         ("Machine", ["Self-test and alarm checks passed", "Residual disinfectant: negative", "Lines primed; no air; clamps correct",
                      "Transducer protectors dry"], "blue"),
         ("Dialysate", ["Acid and bicarbonate match the order", "Conductivity and pH checked independently", "Temperature as prescribed",
                        "Never override a conductivity alarm"], "navy"),
     ],
     "notes": """
Visual 3 (annotated uploaded illustration). AREP [Dialysis / 141056]: dialysate pump, mixer, heater, degasser, temperature and conductivity monitors, blood leak detector; acid and bicarbonate concentrates with purified water.
Independent verification of conductivity/pH and residual disinfectant testing per machine IFU and CMS ESRD interpretive guidance (US); wet transducer protectors must be replaced (CDC MMWR 2001).
Exact pre-treatment test sequence: FMC machine IFU (not uploaded) – NEEDS LOCAL CONFIRMATION."""},

    {"kind": "matrix", "title": "Red flags: pause before starting",
     "source": "Saha M, Allon M. 2017 · KDOQI Vascular Access 2019 · CDC MMWR 2001",
     "rows": [
         ("Cardio-respiratory", "Chest pain, new dyspnea, low SpO₂, new arrhythmia, very low or very high BP", "Physician now; do not start until reviewed"),
         ("Fluid", "IDWG far above usual, crackles, orthopnea", "Notify; review UF goal, time, target weight"),
         ("Infection", "Fever, rigors, pus or redness at access or exit site", "Notify; cultures per protocol; do not use infected site"),
         ("Access", "No thrill/bruit, new swelling, CVC not aspirating", "Do not cannulate or force; notify"),
         ("Prescription", "Order, machine and record do not match", "Hold; clarify with prescriber; document"),
     ],
     "fills": ["navy", "blue", "mid", "blue", "grey"],
     "notes": """
Typical triggers; numeric thresholds (BP, SpO₂, K⁺) are defined in the unit protocol (NEEDS LOCAL CONFIRMATION).
Do not cannulate an access without thrill/bruit; do not cannulate infected sites (KDOQI 2019; CDC 2001)."""},

    {"kind": "algorithm", "title": "Discrepancy found: what next?",
     "source": "Garrick R, et al. Clin J Am Soc Nephrol. 2012 · IHI SBAR · Local policy",
     "nodes": [
         {"t": "start", "text": "Finding or mismatch before start"},
         {"t": "decision", "text": "Patient unstable?", "no": "Hold the start; check source documents (order, labs, record)", "no_label": "No"},
         {"t": "action", "text": "Yes: call physician / emergency help now"},
         {"t": "decision", "text": "Resolved with a clear order?", "no": "Escalate to nurse in charge; do not start", "no_label": "No"},
         {"t": "action", "text": "Yes: read back the order and correct machine settings"},
         {"t": "end", "text": "Document and start; reassess at 15 min"},
     ],
     "side": {"head": "SBAR", "fill": "navy", "body": ["S: what is wrong now", "B: relevant history and order", "A: what you think is happening", "R: what you need"]},
     "notes": """
Visual 4 (algorithm). Note: in the decision node 'Patient unstable?' the 'No' branch goes right (hold and check), 'Yes' continues downward (call now).
SBAR from IHI; safety culture and communication (Garrick R, et al. CJASN 2012). The 15-minute reassessment interval is an example – use local monitoring frequency."""},

    {"kind": "checklist", "title": "Pre-dialysis nursing checklist",
     "source": "Summary aid compiled from Lecture 01 content · adapt to local policy",
     "row_h": 0.52, "size": 12, "h": 4.95,
     "columns": [
         ("Patient", ["Two identifiers matched", "Allergies and isolation status", "History since last HD", "Vitals, SpO₂, glucose if needed",
                      "Weight, IDWG, fluid signs", "Access checked (look/listen/feel)", "Labs and medicines reviewed"]),
         ("Prescription", ["Modality and duration", "Qb and Qd", "K, Ca, Na, HCO₃, temperature", "Dialyzer type", "Anticoagulation",
                           "UF goal and rate calculated", "Order = machine = record"]),
         ("Machine and start", ["Self-test and alarms passed", "Residual disinfectant negative", "Conductivity and pH independent check",
                                "Lines primed, no air", "Red flags escalated", "SBAR documented if used", "Reassess after start"]),
     ],
     "notes": "Summary aid: can be printed as a pocket card. Adapt items and wording to the local treatment record and machine IFU."},

    {"kind": "case", "title": "Case: the prescription does not fit the patient",
     "source": "Fictional teaching case (illustrative training data)",
     "case": [
         "Mr K, 66 years, AVF. On digoxin. Target weight 74.0 kg.",
         "Pre-weight 76.8 kg (previous post 74.3). BP 152/88, pulse 104 irregular.",
         "Today's K⁺ 3.2 mmol/L. Order: K 3.0 bath. Machine: K 2.0 acid connected.",
         "Order says 4 h; the machine is set to 3 h 30 min."],
     "questions": [
         "List every discrepancy you find.",
         "Which finding makes this urgent, and why?",
         "Calculate IDWG and UF goal.",
         "Write your SBAR to the physician."],
     "notes": """
Suggested answers (educational):
1. Wrong acid concentrate (K 2.0 vs ordered 3.0); time 3.5 h vs 4 h; irregular pulse 104 (new?); patient on digoxin with low-normal K⁺.
2. Low K bath + K⁺ 3.2 + digoxin + irregular pulse → arrhythmia risk: do not start; call physician; ECG per protocol.
3. IDWG = 76.8 − 74.3 = 2.5 kg; UF goal = 76.8 − 74.0 = 2.8 L (+ local allowances).
4. S: irregular pulse 104, K bath 2.0 connected but order is 3.0, K⁺ 3.2, on digoxin. B: AVF, 4 h order, IDWG 2.5 kg. A: arrhythmia risk, setup errors. R: review now; confirm K bath and time; ECG? I have not started."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Which TWO items confirm patient identity?", ["A. Bed number and name", "B. Name and date of birth/ID number", "C. Machine number and name", "D. Diagnosis and age"]),
         ("Pre-weight 68.4 kg, target 66.0 kg, 4 h. UF goal?", ["A. 1.4 L", "B. 2.0 L", "C. 2.4 L", "D. 3.4 L"]),
         ("No thrill or bruit in an AVF. Best action?", ["A. Use smaller needles", "B. Cannulate and check flow", "C. Do not cannulate; notify", "D. Apply warm compress and start"]),
         ("Machine K bath differs from the order. First step?", ["A. Start and inform later", "B. Hold and clarify the order", "C. Use the machine value", "D. Ask the patient"]),
     ],
     "notes": """
Answers and rationales:
Q1 B – two person-specific identifiers; bed or machine numbers are locations, not identifiers.
Q2 C – 68.4 − 66.0 = 2.4 L (plus any local allowances per policy).
Q3 C – absent thrill/bruit suggests thrombosis; cannulation risks hematoma/embolisation; notify for assessment (KDOQI 2019).
Q4 B – any order/machine mismatch is resolved before starting; the order is clarified with the prescriber."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 01 summary",
     "items": [
         ("Same routine, every patient", "Identify, assess, review, verify, check, then start."),
         ("Trends beat single values", "Compare weight, BP and symptoms with the patient's own baseline."),
         ("Calculate before you connect", "IDWG, UF goal and UF rate, double-checked."),
         ("Order = machine = record", "Especially concentrate (K, Ca), time, Qb and anticoagulation."),
         ("Pause, escalate, document", "Use SBAR; never start with an unresolved discrepancy."),
     ],
     "notes": "Bridge to Lecture 02: the UF goal is only the first step of safe fluid removal."},

    refs_slide(),
]
