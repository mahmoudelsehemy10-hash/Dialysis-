# -*- coding: utf-8 -*-
"""Lecture 06 - Day 3: Water and Dialysate Safety: Essential Nursing Monitoring and Escalation."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Water_Dialysate_Safety"
TITLE = "Water and Dialysate Safety: Essential Nursing Monitoring and Escalation"
SUBTITLE = "Day 3 · Dialysis Quality & Water Safety · Lecture 06"
FOOTER_TEXT = "L06 Water and dialysate safety"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 06 of the Hemodialysis Nursing Programme (Day 3). 45–60 minutes.
Focus on what nurses check and when they escalate. Technical maintenance belongs to the water/technical team and the IFU of the installed FMC water treatment system.
Standards: ISO 23500 series (2024 editions), US CMS 42 CFR 494.40 (incorporating AAMI RD52:2004). National requirements may differ.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 06",
     "items": [
         ("Explain", ["Why water quality is patient safety", "The stages of water treatment"]),
         ("Monitor", ["Total chlorine before each shift", "Conductivity, pH, temperature"]),
         ("Recognise", ["Patient signs of contamination", "Clusters of reactions"]),
         ("Escalate", ["Stop, protect, notify", "Document and follow up"]),
     ],
     "notes": "Objectives for Lecture 06."},

    {"kind": "water", "title": "Why water quality is patient safety",
     "source": "Ward RA, Ing TS. Handbook of Dialysis. 2015:89-98 · Payne G. Core Curriculum for Nephrology Nursing. 2015:101-113",
     "caption": "Water treatment illustration: FMC AREP, Introduction to Hemodialysis (uploaded screenshot)",
     "stages": [
         ("Pre-treatment", ["Multimedia filter", "Carbon tanks: chlorine/chloramine", "Softener: Ca, Mg"]),
         ("Primary purification", ["Reverse osmosis (RO) removes ions, bacteria, endotoxin"]),
         ("Post-treatment", ["Storage / distribution loop", "Endotoxin (ultra) filter"]),
     ],
     "stat": ("120–150 L", "of dialysate per 4-hour session"),
     "stat_body": ["Contaminants cross the dialyzer membrane directly into blood.",
                   "Nurses are often the first to see the warning signs."],
     "notes": """
AREP [Dialysis / 141622, 141808–142031]: patients are exposed to 120–150 L of dialysis solution during each 4-hour treatment; water treatment ensures water used for HD meets AAMI standards; stages: pre-treatment (multimedia filter, carbon filter, softener), primary purification (RO), post-treatment (storage, endotoxin filter).
Configuration depends on the installed system; follow its IFU."""},

    {"kind": "table_only", "title": "Chemical limits and why they matter",
     "source": "AAMI limits as shown in AREP (Ward RA, Ing TS. 2015:89-98; AAMI 2014) · ISO 23500-3",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.8, 2.6, 6.65], "row_h": 0.44, "size": 12,
               "rows": [["Agent", "Maximum level", "Effects of excess"],
                        ["Chloramine / total chlorine", "0.1 mg/L", "Hemolytic anemia, methemoglobinemia"],
                        ["Aluminum", "0.01 mg/L", "Bone disease, encephalopathy, anemia"],
                        ["Fluoride", "0.2 mg/L", "Pruritus, nausea, ventricular fibrillation"],
                        ["Copper / Zinc", "0.1 mg/L each", "Hemolytic anemia"],
                        ["Calcium / Magnesium", "2 / 4 mg/L", "Weakness, nausea, cardiac disturbances (hard water syndrome)"],
                        ["Sodium / Potassium", "70 / 8 mg/L", "Thirst, fatigue / ECG changes"],
                        ["Sulfate", "100 mg/L", "Nausea, vomiting, metabolic acidosis"]]},
     "banner": "Chlorine and chloramine can break through carbon within hours: that is why nurses test every shift",
     "banner_y": 5.45,
     "notes": """
Limits copied from AREP table [Dialysis / 141732] (AAMI as cited: Ward RA, Ing TS 2015; Nelson L, Goldfrank's 2011; AAMI 2014). "Hard water syndrome" and methemoglobinemia: Handbook of Dialysis 2015 (water chapter).
ISO 23500-3:2024 replaced the 2019 edition; chlorine is expressed differently across documents (USP: chloramines 0.1, free chlorine 0.5 mg/L; ISO: total chlorine 0.1 mg/L) – NEEDS REVIEW against the current standard and national rules."""},

    {"kind": "checklist", "title": "Nursing monitoring: what, when, where",
     "source": "CMS 42 CFR 494.40 (AAMI RD52:2004) · ISO 23500 series · Machine and water system IFU",
     "row_h": 0.6, "size": 13, "h": 4.3,
     "columns": [
         ("Every shift / day", ["Total chlorine < 0.1 mg/L before each patient shift", "Sample after first carbon tank", "Water system alarms and RO readings", "Log results and initials"]),
         ("Every treatment", ["Dialysate conductivity (independent check)", "Dialysate pH", "Temperature as prescribed", "Residual disinfectant: negative"]),
         ("Periodic (technical team)", ["Water and dialysate cultures", "Endotoxin testing", "Chemical analysis of product water", "Disinfection records"]),
     ],
     "banner": "No result in the log = test not done. Never start treatments on an untested shift",
     "notes": """
[WEB] US regulation (42 CFR 494.40, incorporating AAMI RD52:2004 §6.2.5): primary and backup carbon tanks in series; if the port after the first tank shows ≥ 0.1 mg/L total chlorine (or > 0.5 free chlorine / > 0.1 chloramines), test after the second tank; if the last tank exceeds limits, act immediately (correct and confirm, or stop treatment) and notify the medical director. CMS S&C 15-44 (portable RO): total chlorine < 0.1 mg/L before each treatment. Sources: https://www.gpo.gov/fdsys/pkg/CFR-2014-title42-vol5/pdf/CFR-2014-title42-vol5-sec494-40.pdf ; https://www.cms.gov/medicare/provider-enrollment-and-certification/surveycertificationgeninfo/downloads/survey-and-cert-letter-15-44.pdf (""" + ACCESSED + """).
"Before each patient shift" testing frequency is common AAMI-based practice; the regulation text found does not state a single frequency for all facilities – follow local policy.
Culture frequency: the regulation text found refers to quarterly or more frequent bacteriology/endotoxin testing for facilities (monthly for portable RO) – many units test monthly. Verify locally.
Independent conductivity/pH verification and residual disinfectant testing: machine IFU and CMS interpretive guidance."""},

    {"kind": "table_only", "title": "Microbiological limits for water and dialysate",
     "source": "ISO 23500-3 and ISO 23500-5 (2024) · AAMI · values to be verified against current standard",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [3.4, 2.9, 2.9, 2.85], "row_h": 0.62, "size": 13,
               "rows": [["Fluid", "Bacteria (CFU/mL)", "Endotoxin (EU/mL)", "Action level"],
                        ["Water for dialysis", "< 100", "< 0.25", "50 CFU/mL · 0.125 EU/mL"],
                        ["Standard dialysate", "< 100", "< 0.5", "50% of maximum"],
                        ["Ultrapure dialysate", "< 0.1", "< 0.03", "Per local programme"]]},
     "banner": "Action level reached: technical team repeats test, disinfects and investigates before the maximum is exceeded",
     "banner_y": 4.25,
     "notes": """
[WEB] Water for dialysis: < 100 CFU/mL and < 0.25 EU/mL (ISO 23500-3), action levels typically 50% (50 CFU/mL; 0.125 EU/mL); AREP lists microbial 100 CFU/mL with action level 50. Sources: https://open-exam-prep.com/study-guides/bonent-cht/water-treatment-and-dialysate/aami-iso-water-quality-standards-testing ; https://referencemanual.aclab.com/welcome/environmental-testing-collection-and-shipping/dialysis/aami-epa-standards-for-water-analysis/ (""" + ACCESSED + """).
Standard and ultrapure dialysate limits (ISO 23500-5: standard < 100 CFU/mL and < 0.5 EU/mL; ultrapure < 0.1 CFU/mL and < 0.03 EU/mL) are from training knowledge of the ISO standard and could NOT be verified online in this session – NEEDS REVIEW against the official ISO 23500-5:2024 text.
Nurses do not usually take these samples, but must know results and escalate reactions (slide 8)."""},

    {"kind": "matrix", "title": "Total chlorine result: what to do",
     "source": "CMS 42 CFR 494.40 (AAMI RD52:2004 §6.2.5) · Local water policy",
     "rows": [
         ("< 0.1 mg/L", "After first carbon tank", "Record result; treatments may start"),
         ("≥ 0.1 mg/L first tank", "Breakthrough of the first carbon tank", "Test after second (final) tank now; notify technician and charge nurse"),
         ("< 0.1 mg/L final tank", "Second tank still protecting", "Continue with increased testing (e.g. hourly) per policy; replace first tank"),
         ("≥ 0.1 mg/L final tank", "No protection left", "Stop treatments or correct and confirm; notify medical director; watch for hemolysis"),
     ],
     "fills": ["mid", "blue", "blue", "navy"],
     "notes": """
Based on 42 CFR 494.40 / AAMI RD52:2004 §6.2.5 as found in the regulation text: if the initial carbon tank port is ≥ 0.1 mg/L total chlorine, test the second tank; if the last tank exceeds limits, take immediate action (correct and verify, or terminate treatment) and notify the medical director. "Increased testing (e.g. hourly)" while running on the backup tank is common practice – frequency per local policy (NEEDS LOCAL CONFIRMATION).
Patients dialyzed during breakthrough: check for hemolysis (Lecture 07) and inform physician."""},

    {"kind": "six_grid", "title": "Patient signs that point to water or dialysate",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · Greenberg KI, Choi MJ. Am J Kidney Dis. 2021 · AREP",
     "items": [
         ("Hemolysis", "Chloramine, copper", "Dark/port-wine blood in venous line, chest/back pain, dyspnea; also overheated or hypotonic dialysate."),
         ("Pyrogenic reaction", "Endotoxin, bacteria", "Fever, chills, rigors, hypotension during HD."),
         ("Conductivity error", "Wrong concentrate", "Headache, nausea, cramps, seizures; hypo-/hypernatremia."),
         ("Potassium / calcium", "Wrong acid bath", "Arrhythmia, weakness, ECG changes."),
         ("Aluminum, fluoride", "Water treatment failure", "Neurological symptoms, bone disease, arrhythmia."),
         ("A cluster", "Several patients", "Same symptoms in more than one patient: think water or dialysate first."),
     ],
     "notes": """
Water/dialysate-related complications: Saha & Allon CJASN 2017; Greenberg & Choi AJKD 2021 Core Curriculum; hemolysis from chloramines, nitrates, copper, or dialysate overheated (> ~46 °C per one summary) or hypotonic; pyrogenic reactions from endotoxin.
[WEB] Summary of hemolysis causes: https://fpnotebook.com/Renal/ER/EmrgncyCrInEsrd.htm (""" + ACCESSED + """).
Effects of excess contaminants per AREP table [Dialysis / 141732]."""},

    {"kind": "steps", "title": "Escalate: stop, protect, notify, preserve",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · CMS 42 CFR 494.40 · Local policy",
     "steps": [
         ("Stop", "Do not start new treatments; stop affected treatments as instructed"),
         ("Protect the patient", "Vital signs, O₂, symptoms; do not return blood if hemolysis is suspected"),
         ("Notify", "Charge nurse, physician / medical director, water technician"),
         ("Check other patients", "Same shift, same water loop, same concentrate batch"),
         ("Preserve evidence", "Keep lines, dialyzer, concentrate, water and blood samples"),
         ("Document and report", "Times, readings, actions; incident report; follow-up results"),
     ],
     "side": {"head": "Remember", "fill": "navy", "body": [
         "Alarms can be silenced; the problem stays", "One patient's reaction can be the first of many",
         "Independent checks catch machine errors", "Restart only after release by the responsible team"]},
     "notes": """
Escalation principles for water/dialysate incidents (Saha & Allon 2017; CMS 494.40 requirement to take immediate action and notify the medical director). In suspected hemolysis, do not return the blood in the circuit (hyperkalemia risk) – see Lecture 07.
Evidence preservation and incident reporting per local policy."""},

    {"kind": "case", "title": "Case: morning chlorine check",
     "source": "Fictional teaching case",
     "case": [
         "06:30, first shift. Total chlorine after the first carbon tank: 0.2 mg/L.",
         "The night log has no reading from yesterday's last shift.",
         "Two patients are already connected. One reports back pain; venous line blood looks darker than usual.",
         "The technician is on call, 40 minutes away."],
     "questions": [
         "What is your next test and where?",
         "What do you do for the two connected patients?",
         "Who do you notify and in what order?",
         "What will you document?"],
     "notes": """
Suggested answers (educational):
1. Test immediately after the second (final) carbon tank. If ≥ 0.1 mg/L → no protection; stop treatments/correct per policy.
2. Suspect hemolysis in the patient with back pain and dark venous blood: stop the blood pump, clamp, do not return blood, check vitals, send blood (K⁺, Hb, hemolysis markers) per order, notify physician; assess the other patient.
3. Charge nurse → physician/medical director → technician (on call) per local escalation chart; do not start more patients.
4. Readings and times, missing log entry, patient symptoms, actions, persons notified, incident report."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 06 summary",
     "items": [
         ("Water quality is patient safety", "120–150 L of dialysate per session crosses the membrane."),
         ("Test total chlorine every shift", "< 0.1 mg/L after the first carbon tank before treatments start."),
         ("Check every treatment", "Conductivity and pH independently, temperature, residual disinfectant."),
         ("Think water when symptoms cluster", "Hemolysis, fever and chills, or several patients with the same signs."),
         ("Stop, protect, notify, preserve", "Escalate early and document everything."),
     ],
     "notes": "Summarise and link to Day 4 (emergencies and quality improvement)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["iso23500"], R["cms_cfc"], "CMS. S&C 15-44: Portable reverse osmosis units in ESRD facilities.",
              "AAMI RD52:2004 Dialysate for hemodialysis (as incorporated in 42 CFR 494.40).",
              "Ward RA, Ing TS. Handbook of Dialysis. 5th ed. 2015:89-98.", "Payne G. Core Curriculum for Nephrology Nursing, Module 3. 2015:101-113.",
              R["saha"], R["greenberg"], R["arep"], R["ifu"]],
     "notes": "References for Lecture 06."},
]
