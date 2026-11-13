# -*- coding: utf-8 -*-
"""Day 4 · Lecture 08: Hemodialysis Quality Indicators: Nursing Responsibilities, Documentation, and Reporting."""
from program._common import *  # noqa: F401,F403

TITLE = "Hemodialysis Quality Indicators: Nursing Responsibilities, Documentation, and Reporting"
SUBTITLE = "Day 4 · Emergencies & Quality Improvement · Lecture 08"
FOOTER_TEXT = "Day 4 · Lecture 08"
REFS = ["KDOQI_ADEQ15", "KDOQI_VA19", "NHSN", "CDC_CORE", "CFR494", "FLYTHE11", "KDOQI_CV05", "GARRICK12",
        "IHI_SBAR", "AREP_VA", "SA_MOH_IPC"]

SLIDES = [
    {"kind": "title", "notes": """
Day 4, Lecture 08 – final lecture (30–40 min).
All dashboard and trend values are ILLUSTRATIVE TRAINING DATA. Suggested targets are examples drawn from cited guidelines or are left for local definition; they are NOT official Fresenius Medical Care requirements. Use the organisation's approved indicator set and national programme definitions.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 08 objectives",
     "items": [
         ("Define", ["Define an indicator with numerator, denominator, period and source"]),
         ("Measure", ["Calculate 3 nursing indicators from illustrative data"]),
         ("Document", ["Name documentation gaps that distort indicators"]),
         ("Improve", ["Plan one PDSA cycle and report results"]),
     ],
     "notes": "Assessed in the case (slide 15) and knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening question: what the chart did not say",
     "source": "Fictional teaching scenario",
     "story": ["The monthly report shows 100% of treatments 'completed as prescribed'.",
               "A spot check finds 9 sessions ended early, recorded with the prescribed time."],
     "prompts": ["What happened to the indicator?", "Who was affected by the wrong data?", "How would you prevent this?"],
     "notes": "Expected: documentation of prescribed instead of actual time inflated the indicator; patients with under-delivered dialysis were not identified; adequacy interpretation was distorted. Prevention: record actual start/stop times, structured fields, audits. Returns in the case (slide 15)."},

    {"kind": "table_only", "title": "Anatomy of an indicator (1): treatment and adequacy",
     "source": "KDOQI 2015 · Flythe JE, et al. 2011 · KDOQI CVD 2005 · definitions are examples: adapt locally",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.35, 3.0, 2.75, 1.85, 2.1], "row_h": 0.92, "size": 11,
               "rows": [["Indicator", "Numerator", "Denominator", "Period", "Data source"],
                        ["Treatment time delivered", "Actual treatment minutes", "Prescribed minutes", "Month", "Treatment records"],
                        ["Sessions shortened > 15 min", "Sessions ending > 15 min early", "All sessions", "Month", "Treatment records"],
                        ["Adequacy (spKt/V ≥ 1.2)", "Patients with spKt/V ≥ 1.2", "Patients measured (thrice weekly)", "Month", "Lab, adequacy sheet"],
                        ["High UF rate sessions", "Sessions with UFR > 13 mL/kg/h", "All sessions", "Month", "Treatment records"]]},
     "notes": "Example definitions. spKt/V ≥ 1.2 minimum: KDOQI 2015. UFR > 13 mL/kg/h: observational mortality association (Flythe 2011) – used here as a monitoring flag, not a safety limit. The 15-minute threshold for 'shortened' sessions is an EXAMPLE – define locally."},

    {"kind": "table_only", "title": "Anatomy of an indicator (2): access, infection, safety",
     "source": "CDC NHSN · CDC Core Interventions · KDOQI 2019 · KDOQI CVD 2005 · definitions are examples: adapt locally",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.35, 3.0, 2.75, 1.85, 2.1], "row_h": 0.74, "size": 11,
               "rows": [["Indicator", "Numerator", "Denominator", "Period", "Data source"],
                        ["Bloodstream infection rate", "Positive blood cultures (NHSN definition)", "Patient-months × 1/100", "Month", "NHSN/HESN, lab"],
                        ["Long-term CVC use", "Patients with CVC > 90 days", "All prevalent patients", "Month", "Access register"],
                        ["IDH episodes", "Sessions with IDH (unit definition)", "All sessions", "Month", "Treatment records"],
                        ["Water safety compliance", "Shifts with documented chlorine test", "Shifts operated", "Month", "Water log"],
                        ["Hand hygiene compliance", "Opportunities performed", "Opportunities observed", "Month", "Audit tool"]]},
     "notes": "NHSN reports dialysis events per 100 patient-months (NHSN protocol). CVC > 90 days is a common long-term catheter metric (e.g. CMS ESRD QIP; verify current specification). Audit-based indicators follow CDC core intervention tools. Saudi reporting via HESN (secondary) – CONFIRM LOCALLY."},

    {"kind": "dashboard", "title": "Illustrative nursing quality dashboard",
     "source": ILLUS,
     "kpis": [("96.8%", "Treatment time delivered", "Unit goal: set locally"), ("91.5%", "Patients spKt/V ≥ 1.2", "KDOQI minimum 1.2"),
              ("1.4", "BSI per 100 pt-months", "Trend: lower is better"), ("8.2%", "Sessions with IDH", "Unit definition"),
              ("97%", "Chlorine tests logged", "Every shift per policy")],
     "chart": {"name": "Dashboard trend", "title": "Monthly trends",
               "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
               "series": [("Sessions with IDH (%)", [11.0, 10.4, 9.8, 9.1, 8.6, 8.2], BLUE),
                          ("Sessions shortened > 15 min (%)", [12.5, 11.4, 10.2, 8.1, 7.4, 7.0], MID)],
               "min": 0, "max": 14, "major": 2, "y_title": "% of sessions"},
     "side": {"head": "How to read it", "fill": "sand", "body": ["Each tile = one defined indicator", "Trend over months, not one value", "Look behind each % at patients", "Share monthly with the team"], "size": 12},
     "notes": "Visual 1 (dashboard) and visual 2 (trend). ALL VALUES ARE ILLUSTRATIVE TRAINING DATA – not facility results. Both trend lines share one % axis. Targets shown are either guideline-based (spKt/V 1.2) or to be set locally; none are official FMC targets."},

    {"kind": "formula", "title": "Calculate: treatment time and infection rate",
     "source": "Illustrative training data · NHSN rate convention",
     "formulas": [
         ("Treatment time delivered (%)", "actual minutes ÷ prescribed minutes × 100", "Uses ACTUAL start and stop times"),
         ("BSI rate per 100 patient-months", "BSI events ÷ patient-months × 100", "Patient-months = patients × months on HD"),
     ],
     "below": ["Same definitions every month", "Small units: one event changes the rate a lot: use trends"],
     "example": {"head": "Worked example (illustrative training data)", "body": [
         "Month: 1,120 sessions × 240 prescribed min = 268,800 min",
         "Actual delivered: 260,200 min",
         ("Time delivered = 260,200 ÷ 268,800 = 96.8%", {"bold": True, "color": NAVY, "space_after": 6}),
         "80 patients for 1 month = 80 patient-months",
         "1 bloodstream infection",
         ("BSI rate = 1 ÷ 80 × 100 = 1.25 per 100 pt-months", {"bold": True, "color": NAVY})]},
     "notes": "Calculations: 260200/268800 = 0.968 → 96.8%; 1/80 × 100 = 1.25. ILLUSTRATIVE TRAINING DATA. NHSN uses per 100 patient-months for dialysis event rates."},

    {"kind": "checklist", "title": "Documentation that makes indicators reliable",
     "source": "CMS 42 CFR 494.170 (records) · ANNA Core Curriculum 2015 · local documentation policy",
     "row_h": 0.55, "size": 12, "h": 4.3,
     "columns": [
         ("Treatment", ["Actual start and stop times", "Achieved Qb, Qd, UF volume", "Pre/post weight and target", "Reason for any shortening"]),
         ("Events", ["IDH episodes and actions", "Access problems, infiltration", "Infection signs, cultures, IV antibiotics", "Incidents and near misses"]),
         ("Education and safety", ["Fluid/salt education given", "Access care education", "Water log entries", "Audit observations"]),
     ],
     "banner": "Document in real time, in structured fields, with time and signature",
     "notes": "Each item maps to an indicator on slides 4–5. Structured fields allow counting; free text cannot be trended."},

    {"kind": "matrix", "title": "Documentation gaps and their effect on data",
     "source": "Lectures 01–07 · local quality programme",
     "rows": [
         ("Prescribed time recorded", "Actual time not entered", "Delivered time and adequacy look better than reality"),
         ("Weight copied", "Scale, clothing or last value reused", "False IDWG, UF goal and UFR data"),
         ("Missing BP during HD", "Busy changeover, alarms", "IDH episodes not detected or counted"),
         ("Event not reported", "'Minor', resolved, no harm", "Infection and safety rates under-estimated"),
         ("Free text only", "No structured field", "Cannot be counted or trended"),
     ],
     "fills": ["navy", "blue", "mid", "blue", "grey"],
     "notes": "Teaching slide linking documentation quality to indicator validity. Examples are typical patterns, not audit results."},

    {"kind": "pathway", "title": "Incident reporting workflow",
     "source": "Garrick R, et al. Clin J Am Soc Nephrol. 2012 · NHSN · local incident and IPC policy",
     "nodes": [("1 Make safe", "patient first"), ("2 Escalate", "SBAR to physician/charge"), ("3 Report", "incident system, near misses too"),
               ("4 Review", "facts, causes, no blame"), ("5 Act", "fix systems, not people"), ("6 Feed back", "share learning")],
     "cards": [("What to report", ["Patient harm and near misses", "Water/dialysate deviations", "Equipment faults (device ID)"]),
               ("Infection events", ["Positive blood culture", "IV antimicrobial start", "Pus/redness/swelling at access"]),
               ("Escalate trends", ["Rising rates for 2+ months", "Clusters", "Repeated near misses"])],
     "notes": "Visual 3 (workflow). Safety culture and reporting in HD (Garrick R, et al. CJASN 2012, cited in AREP). NHSN dialysis event types (Lecture 04). Device incidents may need manufacturer/regulatory reporting per local policy (FMC complaint process)."},

    {"kind": "pdsa", "title": "Improvement example: Plan–Do–Study–Act",
     "source": "Institute for Healthcare Improvement, Model for Improvement · illustrative example",
     "centre": "PDSA",
     "steps": [("Plan", "Aim: reduce sessions shortened > 15 min from 12% to < 5% in 3 months. Change: record actual times; huddle on late starts."),
               ("Do", "Test on the Monday–Wednesday–Friday morning shift for 4 weeks; collect actual times daily."),
               ("Study", "Illustrative result: shortened sessions 12% → 7%; most causes were late starts and alarms."),
               ("Act", "Adopt time recording; adapt start times; next cycle: alarm response. Share results.")],
     "notes": "Visual 4 (PDSA diagram, native chart). Model for Improvement/PDSA (IHI). All numbers ILLUSTRATIVE TRAINING DATA."},

    {"kind": "line_chart", "title": "Show improvement with a run chart",
     "source": ILLUS,
     "chart": {"name": "Run chart", "title": "Sessions shortened > 15 min (% per week)",
               "categories": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10"],
               "series": [("Shortened sessions (%)", [12.5, 11.8, 12.9, 12.1, 9.6, 8.4, 7.9, 7.1, 6.8, 7.0], BLUE),
                          ("Baseline median 12.3%", [12.3] * 10, GREY, True), ("Aim < 5%", [5] * 10, RED, True)],
               "min": 0, "max": 15, "major": 3, "labels": True, "fmt": "0.0", "note": ILLUS + " · change introduced in week 5"},
     "side": {"head": "Reading a run chart", "body": ["Plot in time order", "Mark when the change started", "Several points below baseline = signal", "Aim not reached yet: next PDSA cycle"]},
     "notes": "Visual 5 (run chart). ILLUSTRATIVE TRAINING DATA. Baseline median of weeks 1–4: (12.1, 12.5) → 12.3. Run-chart rules (e.g. 6+ consecutive points below the median as a shift) per IHI guidance – keep simple for nurses."},

    {"kind": "case", "title": "Case: a documentation gap",
     "source": "Fictional teaching case (illustrative training data)",
     "case": ["Quarterly report: BSI rate rose from 0.8 to 2.4 per 100 patient-months.",
              "All new infections are in CVC patients.", "Audit: hub scrub seen in 5 of 10 connections; hand hygiene 72%.",
              "Two IV antimicrobial starts were not recorded as dialysis events."],
     "questions": ["Is the rise real, an artefact, or both?", "Which documentation gap is present?", "Which core interventions are failing?", "Design one PDSA test of change."],
     "notes": "1. Probably real (all in CVC patients) and still under-counted (two unreported IV antimicrobial starts). 2. Dialysis events not documented/reported → rates under-estimated. 3. Hub disinfection, hand hygiene, catheter care observations and feedback (CDC core interventions). 4. E.g. one shift uses a hub-scrub checklist with peer observation for 2 weeks; measure weekly compliance and monthly BSI rate; share results."},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("3 BSIs, 120 patient-months. Rate per 100?", ["A. 0.4", "B. 2.5", "C. 3.6", "D. 25"]),
         ("Delivered 228 min of 240 prescribed. %?", ["A. 90%", "B. 92%", "C. 95%", "D. 105%"]),
         ("Which gap inflates adequacy?", ["A. Recording actual time", "B. Recording prescribed time", "C. Reporting near misses", "D. Structured fields"]),
         ("PDSA 'Study' means…", ["A. Read a textbook", "B. Compare results with prediction", "C. Start a new project", "D. Write the policy"]),
     ],
     "notes": "Q1 B – 3/120 × 100 = 2.5. Q2 C – 228/240 = 95%. Q3 B – prescribed instead of actual time hides shortened treatments. Q4 B – compare data with the prediction and baseline (IHI)."},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 08 and programme summary",
     "items": [
         ("Define before you measure", "Numerator, denominator, period and data source for every indicator."),
         ("Nursing data drive quality", "Actual time, Qb, weights, events and audits."),
         ("Report everything", "Incidents, near misses, dialysis events and water deviations."),
         ("Trends, not snapshots", "Rates per 100 patient-months, run charts, monthly feedback."),
         ("Improve in small cycles", "Plan, Do, Study, Act; illustrative targets are not FMC requirements."),
     ],
     "notes": "Close the programme: link Day 1 (fluid/IDH), Day 2 (access/infection), Day 3 (adequacy/water), Day 4 (emergencies/QI) to their indicators."},

    refs_slide(),
]
