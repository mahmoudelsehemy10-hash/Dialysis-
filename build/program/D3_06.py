# -*- coding: utf-8 -*-
"""Day 3 · Lecture 06: Water and Dialysate Safety: Essential Nursing Monitoring and Escalation."""
from program._common import *  # noqa: F401,F403

TITLE = "Water and Dialysate Safety: Essential Nursing Monitoring and Escalation"
SUBTITLE = "Day 3 · Dialysis Quality & Water Safety · Lecture 06"
FOOTER_TEXT = "Day 3 · Lecture 06"
REFS = ["ISO23500_3", "ISO23500_5", "CFR494", "CMS_RO", "WATER_SUMMARY", "AREP_HD", "HEMOLYSIS14", "PYRO_OTT",
        "SAHA17", "GREENBERG21", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 3, Lecture 06 (30–40 min). Focus: what nurses check, what they recognise and how they escalate; technical maintenance belongs to the water/technical team.
Numerical limits: only values verified against accessible sources are shown, with the standard and version named. The ISO 23500 series (2024 editions) is the current international standard; full texts are paywalled – values were verified via the ISO/CEN preview pages and secondary summaries (see Source Register). Chemical limits are shown as listed in the uploaded AREP module (AAMI, 2014 as cited there).
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 06 objectives",
     "items": [
         ("Describe", ["Describe the water pathway and 4 fluid quality categories"]),
         ("Monitor", ["Perform and document total chlorine and dialysate checks"]),
         ("Recognise", ["Link patient symptoms to possible contamination"]),
         ("Escalate", ["Apply the escalation steps and know who does what"]),
     ],
     "notes": "Assessed through the failed-check scenario (slide 15) and knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening question: 120–150 litres",
     "source": "AREP Introduction to Hemodialysis",
     "story": ["In one 4-hour session, a patient's blood meets 120–150 L of dialysis fluid across a thin membrane.",
               "Most people drink about 2 L of water a day."],
     "prompts": ["What could travel from the water into the blood?", "Which check do you do before the first patient?", "Who stops treatments if water fails?"],
     "notes": "AREP [Dialysis / 141622]: patients are exposed to 120–150 L of dialysis solution during each 4-hour treatment; small-molecular-weight contaminants can enter the bloodstream."},

    {"kind": "image_side", "title": "The water treatment pathway",
     "source": "AREP Introduction to Hemodialysis (Ward RA, Ing TS. 2015; Payne G. 2015)",
     "image": "water_treatment.png", "image_alt": "Dialysis water treatment: multimedia filter, carbon filter, softener, micron filter, reverse osmosis, storage tank (AREP)",
     "caption": "Source: FMC AREP, Introduction to Hemodialysis (uploaded screenshot 141808). Configuration varies by installation.",
     "img_w": 8.0,
     "side": {"head": "Three stages", "body": [
         ("Pre-treatment: multimedia filter, carbon (chlorine/chloramine), softener", {"space_after": 6}),
         ("Primary purification: reverse osmosis", {"space_after": 6}),
         ("Post-treatment: storage/loop, endotoxin filter", {"space_after": 6}),
         "Local system: see its IFU and logbook"]},
     "notes": "Visual 1 (uploaded illustration). AREP [Dialysis / 141808–142031]: water treatment ensures water meets AAMI standards; pre-treatment (multimedia filter, carbon filter removes chlorine and chloramine, water softener removes Ca and Mg and protects the RO), primary purification (RO), post-treatment (endotoxin filter)."},

    {"kind": "pathway", "title": "Where the checks happen: monitoring points",
     "source": "CMS 42 CFR 494.40 (AAMI RD52:2004) · ISO 23500 series · system and machine IFU",
     "nodes": [("Feed water", "municipal / tank"), ("Carbon tanks", "primary, then secondary"), ("Softener / filters", "hardness, pressure"),
               ("Reverse osmosis", "conductivity, rejection"), ("Loop / storage", "to machines"), ("Machine", "dialysis fluid")],
     "markers": [(1, "Total chlorine after first carbon tank (nurse/tech, each shift per policy)"), (1, "Second tank tested if the first is ≥ 0.1 mg/L"),
                 (3, "RO product conductivity and alarms (tech; nurse checks display/alarms)"), (4, "Cultures and endotoxin of water (tech, scheduled)"),
                 (5, "Conductivity, pH, temperature before each treatment (nurse)"), (5, "Dialysis fluid cultures/endotoxin (tech, scheduled)")],
     "node_h": 1.2,
     "notes": """
Visual 2 (monitoring-point diagram). 42 CFR 494.40 / AAMI RD52:2004 §6.2.5 (regulation text found): primary and backup carbon in series; test the second tank if the first port shows ≥ 0.1 mg/L total chlorine; immediate action if the final tank exceeds limits.
Testing frequency: summaries of AAMI/ISO practice describe testing before each patient shift and at least every 4 hours; one vendor summary describes daily testing at both tanks – sources conflict, so frequency must follow the LOCAL water policy (NEEDS LOCAL CONFIRMATION).
Who tests: varies by unit – this slide shows a common split (nurse vs technician)."""},

    {"kind": "table_only", "title": "Four fluid quality categories",
     "source": "ISO 23500-3:2024 (water) · ISO 23500-5:2024 (dialysis fluid) · values verified via ISO/CEN previews and summaries",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.6, 2.1, 2.1, 5.25], "row_h": 0.78, "size": 12,
               "rows": [["Category", "Bacteria (max)", "Endotoxin (max)", "Use and notes"],
                        ["Dialysis water", "< 100 CFU/mL", "< 0.25 EU/mL", "Product water used to make dialysis fluid (ISO 23500-3)"],
                        ["Standard dialysis fluid", "< 100 CFU/mL", "< 0.5 EU/mL", "Conventional HD (ISO 23500-5)"],
                        ["Ultrapure dialysis fluid", "< 0.1 CFU/mL", "< 0.03 EU/mL", "Recommended for HDF and widely used for HD (ISO 23500-5)"],
                        ["Online substitution fluid", "Validated process", "Validated process", "Infused into blood (online HDF); sterility cannot be proven by sampling: machine IFU and validation"]]},
     "banner": "Action levels (e.g. 50% of the maximum for water) trigger action BEFORE the maximum is reached",
     "banner_y": 5.6,
     "notes": """
[WEB] ISO 23500-5:2024: standard dialysis fluid total viable count < 100 CFU/mL and endotoxin < 0.5 EU/mL; ultrapure < 0.1 CFU/mL and < 0.03 EU/mL (same values in the 2019 edition). For substitution fluid the 2024 text notes that sterility cannot be proven by sampling (compliance relies on process validation and control). Source: https://standards.iteh.ai/catalog/standards/cen/c64b6ed3-ba3e-4f85-8f6d-5ac00fda6a35/en-iso-23500-5-2024 and https://cdn.standards.iteh.ai/samples/67614/7a20ce32a0ce4b7bbe67251ac7fc7b2f/ISO-23500-5-2019.pdf (""" + ACCESSED + """).
[WEB] Dialysis water < 100 CFU/mL and < 0.25 EU/mL (ISO 23500-3) with action levels typically 50% (50 CFU/mL; 0.125 EU/mL): verified only via secondary summaries (open-exam-prep; ACLAB) – NEEDS REVIEW against ISO 23500-3:2024. AREP lists microbial 100 CFU/mL, action level 50 [Dialysis / 141732].
Secondary sources describe online substitution fluid as 'sterile and non-pyrogenic'; that wording was not confirmed in the ISO text accessed, so the slide states only what was verified.
Action levels for dialysis fluid: set by the local water quality programme per ISO 23500-1/-5 – NEEDS LOCAL CONFIRMATION."""},

    {"kind": "table_only", "title": "Chemical hazards: why limits matter",
     "source": "AAMI maximum levels as shown in AREP (Ward RA, Ing TS 2015; AAMI 2014) · ISO 23500-3:2024 is current",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.9, 2.6, 6.55], "row_h": 0.46, "size": 12,
               "rows": [["Agent", "Maximum level", "Effect of excess"],
                        ["Chloramine", "0.1 mg/L", "Hemolytic anemia"],
                        ["Aluminum", "0.01 mg/L", "Bone disease, dialysis encephalopathy, anemia"],
                        ["Fluoride", "0.2 mg/L", "Pruritus, nausea, ventricular fibrillation"],
                        ["Copper / Zinc", "0.1 mg/L each", "Hemolytic anemia"],
                        ["Calcium / Magnesium", "2 / 4 mg/L", "Weakness, cardiac disturbances / paralysis, bradycardic arrest"],
                        ["Sodium / Potassium", "70 / 8 mg/L", "Thirst, fatigue / ECG changes"],
                        ["Sulfate", "100 mg/L", "Nausea, vomiting, metabolic acidosis"]]},
     "banner": "Microbial hazards: bacteria and endotoxin cause fever, chills and hypotension (pyrogenic reactions)",
     "banner_y": 5.35,
     "notes": "Rows copied from AREP [Dialysis / 141732] (AAMI as cited there). ISO 23500-3:2024 replaced earlier editions; values not re-verified against the paywalled ISO text – NEEDS REVIEW by the technical team. Chlorine terminology varies (USP: chloramines 0.1, free chlorine 0.5 mg/L; ISO: total chlorine 0.1 mg/L)."},

    {"kind": "checklist", "title": "Routine nursing checks and documentation",
     "source": "CMS 42 CFR 494.40 · ISO 23500 series · machine and water system IFU · local policy",
     "row_h": 0.6, "size": 13, "h": 4.3,
     "columns": [
         ("Before patients (per shift)", ["Total chlorine < 0.1 mg/L after first carbon", "Record value, time, initials", "Water system alarms checked", "Failed test: escalate before any start"]),
         ("Before each treatment", ["Concentrates match the prescription", "Conductivity and pH (independent check)", "Temperature as prescribed", "Residual disinfectant: negative"]),
         ("Know the schedule", ["Water and dialysate culture dates", "Endotoxin results and action levels", "Disinfection records", "Who to call (24/7 list)"]),
     ],
     "banner": "No entry in the log = test not done",
     "notes": "Checks per US CMS 494.40/AAMI (regulation text found), CMS S&C 15-44 (portable RO: total chlorine < 0.1 mg/L before each treatment) and machine IFU. Frequency and who performs each check are LOCAL decisions – confirm in the unit water policy."},

    {"kind": "algorithm", "title": "Failed total chlorine test",
     "source": "CMS 42 CFR 494.40 (AAMI RD52:2004 §6.2.5) · local water policy",
     "w": 5.4, "no_w": 3.3,
     "nodes": [
         {"t": "start", "text": "First carbon tank: total chlorine ≥ 0.1 mg/L"},
         {"t": "action", "text": "Do not start new treatments; notify technician and nurse in charge"},
         {"t": "decision", "text": "Second (final) tank < 0.1 mg/L?", "no": "STOP treatments or correct and confirm; notify medical director; assess patients", "no_label": "No"},
         {"t": "action", "text": "Yes: continue only per policy with increased testing"},
         {"t": "action", "text": "Technician replaces/regenerates carbon; retest"},
         {"t": "end", "text": "Document results, times, actions; incident report"},
     ],
     "side": {"head": "Patients already on HD", "fill": "navy", "body": ["Watch for hemolysis (dark blood, back/chest pain)", "If suspected: stop, clamp, do not return blood (L07)", "Inform physician"]},
     "notes": "Visual 3 (escalation flowchart). Based on 42 CFR 494.40 / AAMI RD52:2004 §6.2.5 (regulation text found): test second tank when first ≥ 0.1 mg/L total chlorine; if last tank exceeds limits, immediate action (correct and verify, or terminate treatment) and notify the medical director. Increased testing frequency while relying on the backup tank: per LOCAL policy. Hemolysis management: discard circuit blood rather than return it (BMC Res Notes 2014)."},

    {"kind": "six_grid", "title": "Patient symptoms that point to water or dialysate",
     "source": "Saha M, Allon M. 2017 · BMC Res Notes 2014 (hemolysis) · Ottawa pyrogenic reaction guideline · AREP",
     "items": [
         ("Hemolysis", "Chloramine, copper", "Dark venous blood, back/chest pain, dyspnea; also overheated (> ~42 °C) or hypotonic fluid."),
         ("Pyrogenic reaction", "Endotoxin, bacteria", "Fever, chills, rigors, hypotension, usually in the first hour."),
         ("Conductivity error", "Wrong mixing", "Headache, nausea, cramps, seizures; sodium disturbances."),
         ("Potassium / calcium", "Wrong concentrate", "Arrhythmia, weakness, ECG changes."),
         ("Aluminum, fluoride", "Treatment failure", "Neurological symptoms, arrhythmia, bone disease."),
         ("Cluster", "Several patients", "Same symptoms in more than one patient: think water first."),
     ],
     "notes": "Hemolysis causes (overheating, hypotonic dialysate, chloramine and other water contaminants, kinked lines; > 42 °C associated with hemolysis) from BMC Res Notes 2014 review (web-verified). Pyrogenic reactions: fever/chills ± hypotension, typically within the first hour; contaminated water/dialysate (Ottawa guideline; Vietnam outbreak study; secondary). Effects of chemical excess per AREP table."},

    {"kind": "table_only", "title": "Who does what",
     "source": "CMS 42 CFR 494 (medical director responsibility; QAPI) · ISO 23500-1 water quality management · local policy",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.7, 3.15, 3.15, 3.05], "row_h": 0.72, "size": 12,
               "rows": [["Task", "Nurse", "Technical staff", "Medical leadership"],
                        ["Pre-shift chlorine test", "Perform/verify, record (if assigned)", "Perform/verify; maintain carbon", "Oversight of policy"],
                        ["Machine fluid checks", "Every treatment", "Calibration, maintenance", "-"],
                        ["Cultures, endotoxin", "Know results, report reactions", "Sample, test, trend, disinfect", "Review results, decide actions"],
                        ["Failed check", "Stop starts, escalate, monitor patients", "Investigate, correct, retest", "Decide to stop/resume"],
                        ["Documentation", "Logs, treatment record, incident", "Water logs, maintenance", "QAPI review"]]},
     "banner": "Local policy assigns these roles: know yours before you need it",
     "banner_y": 5.95,
     "notes": "Typical division of responsibilities; under US CMS the medical director is responsible for the water and dialysate quality programme (42 CFR 494). Actual assignments vary – NEEDS LOCAL CONFIRMATION (Saudi MOH/organisational policy)."},

    {"kind": "steps", "title": "Escalation: stop, protect, notify, preserve",
     "source": "Saha M, Allon M. 2017 · CMS 42 CFR 494.40 · local policy",
     "steps": [
         ("Stop", "No new starts; stop affected treatments as instructed"),
         ("Protect", "Vital signs, O₂, symptoms; no blood return if hemolysis suspected"),
         ("Notify", "Nurse in charge, physician/medical director, technician"),
         ("Check others", "Same shift, same loop, same concentrate batch"),
         ("Preserve", "Lines, dialyzer, concentrate, water and blood samples"),
         ("Document", "Readings, times, actions; incident report; follow-up"),
     ],
     "side": {"head": "Remember", "fill": "navy", "body": ["Silencing an alarm does not fix it", "One reaction can be the first of many", "Resume only when released"]},
     "notes": "Escalation principles; CMS 494.40 requires immediate action and notification of the medical director for failed chlorine results (regulation text). Pyrogenic reaction: stop dialysis, do not return blood, cultures, sequester supplies (Ottawa guideline/secondary – NEEDS REVIEW)."},

    {"kind": "case", "title": "Scenario: a failed water safety check",
     "source": "Fictional teaching scenario",
     "case": [
         "06:30, first shift. Total chlorine after the first carbon tank: 0.2 mg/L.",
         "Yesterday's last-shift result is missing in the log.",
         "Two patients are already connected. One reports back pain; venous blood looks darker than usual.",
         "The technician is 40 minutes away."],
     "questions": [
         "What is your next test and where?",
         "What do you do for the two connected patients?",
         "Who do you notify, in what order?",
         "What will you document?"],
     "notes": """
1. Test after the second (final) carbon tank now. If ≥ 0.1 mg/L → no protection: stop/correct per policy; notify medical director.
2. Suspected hemolysis in the patient with back pain and dark venous blood: stop the blood pump, clamp, do not return blood; vital signs, O₂; bloods per order; physician now. Assess the other patient closely.
3. Nurse in charge → physician/medical director → technician (per local escalation chart); no new starts.
4. Results and times, missing log entry, symptoms, actions, people notified, incident report."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Total chlorine limit after carbon (AAMI/ISO, US CMS)?", ["A. < 0.5 mg/L", "B. < 0.1 mg/L", "C. < 1.0 mg/L", "D. No limit"]),
         ("Ultrapure dialysis fluid endotoxin limit (ISO 23500-5)?", ["A. < 0.5 EU/mL", "B. < 0.25 EU/mL", "C. < 0.03 EU/mL", "D. < 1 EU/mL"]),
         ("An action level means…", ["A. Patients must stop dialysis", "B. Act before the maximum is exceeded", "C. Result is acceptable", "D. Only for chemicals"]),
         ("Fever and rigors in 3 patients in the first hour suggest…", ["A. Access infection only", "B. Pyrogenic reaction from fluid", "C. Fluid overload", "D. Dialyzer clotting"]),
     ],
     "notes": "Q1 B (total chlorine < 0.1 mg/L; 42 CFR 494.40, ISO). Q2 C (ISO 23500-5:2024). Q3 B (action levels trigger corrective action before the maximum). Q4 B – a cluster in the first hour points to water/dialysate endotoxin or bacteria; still take blood cultures (catheter bacteremia can mimic)."},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 06 summary",
     "items": [
         ("Water quality is patient safety", "120–150 L of fluid per session meets the blood."),
         ("Know the categories and limits", "Water, standard, ultrapure, online substitution: named standard, version."),
         ("Test, record, verify", "Total chlorine before patients; conductivity, pH, temperature every treatment."),
         ("Think water when symptoms cluster", "Hemolysis, pyrogenic reactions, several patients alike."),
         ("Stop, protect, notify, preserve", "Escalate by policy; resume only when released."),
     ],
     "notes": "Bridge to Day 4: emergencies and quality improvement."},

    refs_slide(),
]
