# -*- coding: utf-8 -*-
"""Lecture 08 - Day 4: Hemodialysis Quality Indicators: Nursing Responsibilities, Documentation, and Reporting."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Quality_Indicators"
TITLE = "Hemodialysis Quality Indicators: Nursing Responsibilities, Documentation, and Reporting"
SUBTITLE = "Day 4 · Emergencies & Quality Improvement · Lecture 08"
FOOTER_TEXT = "L08 Quality indicators"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 08 – final lecture of the Hemodialysis Nursing Programme (Day 4). 45–60 minutes.
Quality indicators shown are EXAMPLES drawn from KDOQI/KDIGO guidelines, CDC NHSN and CMS programmes; each unit must use the indicator set and targets of its national programme and organisation (e.g. FMC clinical quality programme).
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 08",
     "items": [
         ("Know", ["Core HD quality indicators", "Their targets and sources"]),
         ("Measure", ["Collect accurate data", "Document at the right time"]),
         ("Report", ["Incidents and NHSN events", "Escalate trends"]),
         ("Improve", ["Use PDSA cycles", "Share results with the team"]),
     ],
     "notes": "Objectives for Lecture 08."},

    {"kind": "flow", "title": "Quality improvement is a cycle, not a report",
     "source": "AREP Vascular Access (CQI) · CMS 42 CFR 494.110 (QAPI) · Institute for Healthcare Improvement",
     "steps": [
         ("Plan", ["Choose an indicator", "Set a target and a change"]),
         ("Do", ["Test the change on a small scale", "Collect data"]),
         ("Study", ["Compare with baseline", "Ask: did it work?"]),
         ("Act", ["Adopt, adapt or abandon", "Share and repeat"]),
     ],
     "bottom_left": {"head": "Nurses make the data", "body": [
         "Most indicators come from nursing records", "Missing or late entries distort results",
         "Accurate data shows where to improve"]},
     "bottom_right": {"head": "CQI for vascular access (AREP)", "items": [
         "Performance measures", "Track access types and complications", "Establish a database and process"]},
     "notes": """
PDSA (Plan-Do-Study-Act) model (IHI). CMS ESRD Conditions for Coverage require a Quality Assessment and Performance Improvement (QAPI) programme (42 CFR 494.110) – US; use national equivalent.
AREP [vascular access / 152758]: Continuous Quality Improvement (CQI) – performance measures, track access types and complications, establish database and process (Faratro R 2015; Lok 2020)."""},

    {"kind": "table_only", "title": "Core indicators and nursing contribution",
     "source": "KDOQI 2015 · KDOQI Vascular Access 2019 · CDC NHSN · Flythe JE, et al. 2011 · targets are examples: use your programme's values",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.7, 3.9, 5.45], "row_h": 0.55, "size": 12,
               "rows": [["Indicator", "Example target / measure", "Nursing contribution"],
                        ["Dialysis adequacy", "spKt/V ≥ 1.2 (target 1.4); URR ≥ 65%", "Full time, achieved Qb, correct sampling"],
                        ["Vascular access", "AVF/AVG use ↑, long-term CVC use ↓", "Access exam, referral, cannulation skill"],
                        ["Bloodstream infection", "BSI per 100 patient-months (NHSN)", "Asepsis, hub care, event reporting"],
                        ["Fluid management", "UFR > 13 mL/kg/h and IDH episodes ↓", "Weights, UF calculation, education"],
                        ["Anemia and mineral", "Hb, phosphate, calcium within unit targets", "Timely samples, medication on schedule"],
                        ["Treatment delivery", "Missed and shortened sessions ↓", "Record actual time; follow up absences"],
                        ["Safety events", "Falls, medication errors, VND, water events", "Report every event, including near misses"],
                        ["Patient experience", "Survey results (e.g. ICH CAHPS)", "Communication, respect, education"]]},
     "notes": """
Example indicators and targets:
- Adequacy: KDOQI 2015 spKt/V target 1.4, minimum 1.2 (≈ URR 65%).
- Vascular access: KDOQI 2019 (patient-centred Life-Plan; minimise long-term catheters).
- BSI: CDC NHSN dialysis event rates per 100 patient-months.
- UFR: > 13 mL/kg/h associated with mortality (Flythe 2011).
- Anemia/mineral targets follow KDIGO anemia (2012) and CKD-MBD (2017) guidance and local protocol; numbers deliberately not shown – NEEDS LOCAL TARGETS.
- CMS ESRD Quality Incentive Program (QIP) includes measures such as Kt/V, long-term catheter rate, NHSN BSI, hospitalisation/readmission and ICH CAHPS; the measure set changes yearly – verify current year. Outside the US use national registry / FMC internal quality indicators."""},

    {"kind": "checklist", "title": "Documentation that makes indicators reliable",
     "source": "CMS 42 CFR 494.170 (medical records) · ANNA Core Curriculum 2015 · Local documentation policy",
     "row_h": 0.6, "size": 13, "h": 4.3,
     "columns": [
         ("Before", ["Pre-weight, vitals, assessment", "Prescription verified, checks done", "Access findings"]),
         ("During", ["BP and pulse at set intervals", "Machine parameters and alarms", "Events, actions, times", "Medicines given"]),
         ("After", ["Post-weight, vitals, actual time", "Actual Qb, UF removed", "Access hemostasis", "Handover and follow-up"]),
     ],
     "banner": "Document in real time, objectively, with time and signature. Not documented = not done",
     "notes": """
Documentation essentials per ANNA Core Curriculum and local policy; US: medical record requirements 42 CFR 494.170.
Actual delivered time, Qb and UF volume are needed to interpret adequacy and fluid indicators (Lectures 02, 05)."""},

    {"kind": "matrix", "title": "Common documentation errors and their impact",
     "source": "Lectures 01–07 · Local quality programme",
     "rows": [
         ("Wrong weight", "Scale, clothing, or copy of last value", "False UF goal, IDWG and UFR data"),
         ("Prescribed time recorded", "Actual time not entered", "Adequacy looks better than delivered"),
         ("Missing vital signs", "Busy changeover, alarms", "IDH episodes not detected or counted"),
         ("Event not reported", "'Minor', resolved, no harm", "Infection and safety rates under-estimated"),
         ("Free text only", "No structured field", "Data cannot be counted or trended"),
     ],
     "fills": ["blue", "mid", "blue", "navy", "grey"],
     "notes": "Teaching slide linking documentation quality to indicator validity. Examples are typical, not from a specific audit."},

    {"kind": "steps", "title": "Reporting incidents and near misses",
     "source": "Garrick R, et al. Clin J Am Soc Nephrol. 2012;7(4):680-688 · CDC NHSN Dialysis Event Protocol 2026 · Local incident policy",
     "steps": [
         ("Make safe", "Care for the patient first; escalate per protocol"),
         ("Report promptly", "Incident system within the local time limit; include near misses"),
         ("Describe facts", "What, when, where, who, actions; no blame language"),
         ("Notify", "Physician, charge nurse; patient and family per open-disclosure policy"),
         ("Learn", "Root cause review for serious events; share lessons with the team"),
     ],
     "side": {"head": "Report also", "fill": "navy", "body": [
         "NHSN dialysis events: positive blood culture, IV antimicrobial start, pus/redness/swelling at access",
         "Water and dialysate deviations", "Equipment faults (with device ID)", "Medication errors and falls"]},
     "notes": """
Safety culture and event reporting in HD (Garrick R, et al. CJASN 2012;7(4):680-688). AREP: establish a culture of safety (quality assessment and performance improvement), dedicated safety team, focus on identified risk areas [Dialysis / 145115].
[WEB] NHSN dialysis event types (Lecture 04): https://www.cdc.gov/nhsn/faqs/dialysis/faq-dialysis-event-reporting.html (""" + ACCESSED + """).
Device-related incidents may also require regulatory/manufacturer reporting (e.g. FMC complaint process) – follow local policy."""},

    {"kind": "formula", "title": "Turn counts into rates you can compare",
     "source": "CDC NHSN Dialysis Event Surveillance · illustrative numbers",
     "formulas": [
         ("BSI rate", "BSI events ÷ patient-months × 100", "per 100 patient-months (NHSN convention)"),
         ("Proportion indicator", "patients meeting target ÷ patients measured × 100", "e.g. % with spKt/V ≥ 1.2"),
     ],
     "below": ["Use the same definitions every month", "Show trends over time, not single months", "Small units: one event changes the rate a lot"],
     "example": {"head": "Worked example (illustrative)", "body": [
         "Unit with 80 patients for 1 month = 80 patient-months",
         "2 bloodstream infections that month",
         "Rate = 2 ÷ 80 × 100 = 2.5 per 100 patient-months",
         "72 of 78 patients measured had spKt/V ≥ 1.2",
         ("Adequacy = 72 ÷ 78 = 92.3%", {"bold": True, "color": NAVY, "size": 15, "space_after": 4}),
         "Ask: who are the 6? Time, Qb, access, sampling?"]},
     "notes": """
NHSN reports dialysis event rates per 100 patient-months (CDC NHSN Dialysis Event Surveillance).
Example numbers are ILLUSTRATIVE CALCULATIONS: 2/80 × 100 = 2.5; 72/78 = 92.3%.
Teaching point: look behind the percentage at individual patients (link to Lecture 05 troubleshooting)."""},

    {"kind": "case", "title": "Case: catheter infections are rising",
     "source": "Fictional teaching case",
     "case": [
         "Quarterly report: BSI rate rose from 0.8 to 2.4 per 100 patient-months.",
         "All new infections are in patients with CVCs.",
         "Hand hygiene audit: 72% compliance; hub scrub observed in 5 of 10 connections.",
         "Two IV antimicrobial starts were not reported as dialysis events."],
     "questions": [
         "Is the rise real or a reporting artefact?",
         "Which core interventions are failing?",
         "Design one small PDSA test of change.",
         "How will you show whether it worked?"],
     "notes": """
Suggested answers (educational):
1. Probably real (all in CVC patients) – and still under-reported (2 unreported IV antimicrobial starts).
2. Hand hygiene, catheter hub disinfection, catheter care observations, event reporting/feedback (CDC core interventions).
3. Example: one shift uses a hub-scrub checklist with peer observation for 2 weeks.
4. Weekly observation compliance and monthly BSI rate per 100 patient-months, shown as a run chart; share with staff."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 08 and programme summary",
     "items": [
         ("Indicators measure nursing care", "Adequacy, access, infection, fluid and safety all start at the chair."),
         ("Accurate, real-time documentation", "Actual time, Qb, weights and events make data trustworthy."),
         ("Report every event", "Including near misses and NHSN dialysis events."),
         ("Use rates and trends", "Per 100 patient-months and run charts, not single numbers."),
         ("Improve in small cycles", "Plan, Do, Study, Act; share results with the team."),
     ],
     "notes": "Close the 4-day programme: link each day to its indicators (Day 1 fluid/IDH; Day 2 access/BSI; Day 3 adequacy/water; Day 4 events/QI)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["kdoqi_adeq"], R["kdoqi_va"], R["nhsn"], R["cms_cfc"] + " §494.110 QAPI, §494.170 medical records.",
              "CMS ESRD Quality Incentive Program (QIP), current payment-year measure specifications.",
              "KDIGO Clinical Practice Guideline for Anemia in CKD. Kidney Int Suppl. 2012;2(4).",
              "KDIGO 2017 CKD-MBD Guideline Update. Kidney Int Suppl. 2017;7(1).", R["flythe"], R["garrick"],
              "Institute for Healthcare Improvement. Model for Improvement / PDSA.", R["anna"], R["arep"]],
     "notes": "References for Lecture 08."},
]
