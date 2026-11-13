# -*- coding: utf-8 -*-
"""Day 2 · Lecture 04: Infection Prevention in Hemodialysis: Aseptic Practice, Disinfection, and Isolation."""
from program._common import *  # noqa: F401,F403

TITLE = "Infection Prevention in Hemodialysis: Aseptic Practice, Disinfection, and Isolation"
SUBTITLE = "Day 2 · Vascular Access & Infection Control · Lecture 04"
FOOTER_TEXT = "Day 2 · Lecture 04"
REFS = ["CDC_2001", "CDC_CORE", "CDC_INJ", "CDC_HBVVAC", "KDIGO_HCV18", "WHO_5M", "NHSN", "CFR494",
        "SA_MOH_IPC", "SA_HIV14", "AREP_VA", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 2, Lecture 04 (30–40 min). Key distinction: hepatitis B requires isolation arrangements (CDC 2001); hepatitis C and HIV do not require isolation when standard precautions are applied strictly (CDC 2001; KDIGO 2018 for HCV). cdc.gov was not reachable from the build environment; CDC statements verified through search summaries and CDC PDF tools – flagged for review.
Saudi requirements: the MOH IPC auditor guide includes an HD unit element and a national 'Dialysis Safety' guideline is described in the literature (testing new/transferred patients for HIV, HCV, HBV), but primary Saudi texts were not accessible – CONFIRM WITH LOCAL IPC.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 04 objectives",
     "items": [
         ("Practise", ["Perform hand hygiene at the 5 moments and use PPE correctly"]),
         ("Prepare", ["Prepare medications safely in a clean area"]),
         ("Disinfect", ["Disinfect a station; distinguish external vs internal disinfection"]),
         ("Isolate and report", ["Apply HBV isolation; explain why HCV/HIV differ; report breaches"]),
     ],
     "notes": "Measured with the observation checklist (slide 14), scenario (slide 15) and knowledge check (slide 16)."},

    {"kind": "opening", "title": "Opening question: where did the virus travel?",
     "source": "Discussion question based on published HD outbreak investigations (no specific facility)",
     "story": ["Several outbreaks of hepatitis C and B in dialysis units were traced to shared items and missed hand hygiene,",
               "not to the dialysis machine itself."],
     "prompts": ["Name three items that could carry blood between stations.", "When do gloves fail to protect?", "What would you change on your shift?"],
     "notes": "Outbreak investigations in HD units commonly identify lapses such as shared medication vials/carts, inadequate cleaning between patients and missed hand hygiene (CDC MMWR 2001; CDC injection safety materials). A Saudi HD-unit HIV outbreak investigation also linked transmission to suboptimal IPC adherence (PMC4144264, secondary). Use as discussion only."},

    {"kind": "two_cards", "title": "Hand hygiene and PPE",
     "source": "WHO My 5 Moments (2009) · CDC MMWR 2001;50(RR-5) · CDC Core Interventions",
     "h": 3.7,
     "cards": [
         ("Hand hygiene: 5 moments", ["Before touching the patient", "Before aseptic tasks (cannulation, CVC)", "After body fluid exposure risk",
                                      "After touching the patient", "After touching the station or machine"]),
         ("PPE in HD", ["Gloves for any patient or station contact", "Change gloves and clean hands between patients/stations",
                        "Gown, face shield/mask for splash risk (connection, disconnection)", "Mask for CVC procedures per policy",
                        "Remove PPE before leaving the station"]),
     ],
     "banner": "Gloves never replace hand hygiene. Monthly audits with feedback are a CDC core intervention",
     "notes": "CDC MMWR 2001: wear gloves when caring for the patient or touching equipment at the station; remove gloves and clean hands between patients/stations. WHO 5 Moments adapted to the station. CDC Core Interventions: monthly hand hygiene observations with feedback."},

    {"kind": "pathway", "title": "Aseptic workflow for access procedures",
     "source": "CDC Core Interventions · KDOQI Vascular Access 2019 · local ANTT policy",
     "nodes": [("1 Hand hygiene", "and clean gloves"), ("2 Prepare", "clean field, supplies ready"), ("3 Antisepsis", "CHG-alcohol, contact time, dry"),
               ("4 No-touch", "key parts never touched"), ("5 Connect / secure", "closed system"), ("6 Dispose", "sharps; remove gloves; hand hygiene")],
     "cards": [("Key parts", ["Needle, hub, line ends, cap inside", "If touched: replace or re-disinfect"]),
               ("Contact time", ["CHG-alcohol: scrub ~30 s, let dry", "Povidone-iodine: 2–3 min"]),
               ("Common failure", ["Touching the site after antisepsis", "Blowing on or fanning the skin"])],
     "notes": "Visual 1 (workflow). Antisepsis times from KDOQI 2019 skin preparation (AREP [vascular access / 153505]). Aseptic non-touch technique terminology per local policy."},

    {"kind": "checklist", "title": "Safe medication preparation and injection",
     "source": "CDC Hemodialysis Injection Safety Checklist · CDC MMWR 2008;57(32) · CDC MMWR 2001",
     "row_h": 0.6, "size": 13, "h": 4.25,
     "columns": [
         ("Prepare", ["Dedicated clean area, away from stations", "No blood, body fluids or tap water nearby", "As close to administration time as possible", "New needle and syringe every time"]),
         ("Vials", ["Single-dose vials: one patient, one entry, discard", "Multi-dose vials kept out of the treatment area", "Never enter a vial with a used syringe", "Label prepared syringes"]),
         ("Transport", ["Carry directly to one patient", "No shared medication carts at stations", "Nothing taken to a station returns to the clean area", "Disinfect injection ports before access"]),
     ],
     "banner": "One needle, one syringe, one patient, one time",
     "notes": """
[WEB] CDC hemodialysis injection safety tools: prep area clearly separated from patient treatment area (ideally a separate room), free of blood, body fluids, contaminated equipment and tap water; medications taken directly from prep area to the individual patient and prepared as close as possible to administration; discard single-dose vials; multi-dose vials not stored or handled in the immediate patient care area. MMWR 2008: single-use medications dedicated to one patient and entered once. Sources: https://www.cdc.gov/dialysis-safety/media/pdfs/Hemodialysis-InjectionSafety-Checklist-P.pdf ; https://www.cdc.gov/dialysis-safety/media/pdfs/Hemodialysis-InjectionSafety-Observations-P.pdf (""" + ACCESSED + """)."""},

    {"kind": "zones", "title": "Clean and contaminated areas",
     "source": "CDC MMWR 2001;50(RR-5) · CDC Injection Safety Checklist",
     "zones": [("Clean area", ["Medication preparation", "Clean supplies storage", "No used items, no blood samples"]),
               ("Patient station", ["Items dedicated to this patient", "Gloves on; disinfect after the patient leaves", "Unused supplies discarded or dedicated"]),
               ("Contaminated area", ["Blood sample handling", "Waste, sharps, used equipment", "Separate sink from hand washing"])],
     "rule_head": "One-way flow: clean → station → discard or reprocess",
     "rule": "Anything taken to a station is never returned to the clean area or to another patient without cleaning and disinfection.",
     "notes": "Visual 2 (diagram). CDC MMWR 2001: items taken to the station are discarded, dedicated to one patient, or cleaned and disinfected before return to a common clean area; clean areas clearly separated from contaminated areas; no common medication carts; blood samples handled in a separate area."},

    {"kind": "steps", "title": "Station disinfection sequence",
     "source": "CDC MMWR 2001 · CDC Dialysis Station Routine Disinfection checklist · disinfectant label",
     "steps": [
         ("After the patient leaves", "Never disinfect around a seated patient"),
         ("Remove and discard", "Disposables, unused supplies, prime waste containers emptied"),
         ("Clean visible blood", "Then disinfect with an approved hospital disinfectant"),
         ("Touched surfaces", "Chair, table, machine front and top, control panel, BP cuff"),
         ("Contact time", "Surfaces stay wet for the label time; let dry"),
         ("Hand hygiene", "Before preparing the station for the next patient"),
     ],
     "side": {"head": "Commonly missed", "fill": "navy", "body": ["Machine control panel and screen", "Chair arms and lever", "Prime bucket / drain area", "Clipboard, pens, phones"]},
     "notes": "Visual 3 (sequence). CDC MMWR 2001: clean and disinfect the station between patients, with special attention to control panels and frequently touched surfaces; discard fluid and disinfect containers associated with prime waste. CDC routine station disinfection checklist emphasises waiting until the patient has left (via summaries – NEEDS REVIEW against current CDC tool). Disinfectant product and contact time: label and local IPC policy."},

    {"kind": "table_only", "title": "External surfaces vs internal machine disinfection",
     "source": "CDC MMWR 2001 · Fresenius Medical Care machine IFU (local) · CMS 42 CFR 494",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.6, 4.7, 4.75], "row_h": 0.7, "size": 12,
               "rows": [["", "External surface disinfection", "Internal (fluid path) disinfection"],
                        ["Purpose", "Remove blood and pathogens from touched surfaces", "Control microbes and biofilm in the dialysate path"],
                        ["Who / when", "Nurse or patient care staff after every patient", "Per machine IFU program and schedule (daily/between patients)"],
                        ["How", "Approved hospital disinfectant, wet contact time", "Machine program: heat and/or chemical per IFU"],
                        ["Check", "Visual check, audit tool", "Program completed; residual disinfectant test negative before use"],
                        ["HBV machine", "Dedicated machine for HBsAg+ patients", "Internal path disinfected by conventional protocols (CDC)"]]},
     "banner": "Wet or damaged transducer protector: replace; check the machine side per IFU",
     "banner_y": 5.85,
     "notes": """
CDC MMWR 2001: if a machine used for an HBsAg-positive patient is needed for a susceptible patient, internal pathways can be disinfected using conventional protocols and external surfaces cleaned with soap and water or a hospital disinfectant (via secondary summaries). Transducer protectors: replace if wetted; check the machine-side protector per IFU.
Internal disinfection programs, agents and frequency are machine-specific: FMC machine IFU (not uploaded) – NEEDS LOCAL CONFIRMATION."""},

    {"kind": "table_only", "title": "Bloodborne viruses: not one rule for all",
     "source": "CDC MMWR 2001;50(RR-5) · KDIGO HCV in CKD 2018 (Ch. 3, unchanged 2022) · national policy",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.1, 3.4, 3.15, 3.4], "row_h": 0.95, "size": 12,
               "rows": [["", "Hepatitis B (HBsAg+)", "Hepatitis C", "HIV"],
                        ["Isolation", "Yes: separate room/area", "Not required (KDIGO 2018)", "Not required (CDC 2001)"],
                        ["Machine and supplies", "Dedicated machine, equipment, supplies", "Standard; strict disinfection", "Standard; strict disinfection"],
                        ["Staffing", "Not caring for HBV-susceptible patients the same shift", "Standard precautions", "Standard precautions"],
                        ["Screening", "HBsAg monthly if susceptible (CDC)", "On admission/transfer, then every 6 months", "Per national policy"]]},
     "banner": "Standard precautions for every patient; HBV adds isolation because the virus spreads easily via surfaces",
     "banner_y": 6.0,
     "notes": """
[WEB] HBV: CDC MMWR 2001 – separate room, dedicated machines/equipment/supplies; staff caring for HBsAg+ patients do not care for susceptible patients at the same time (summaries). Monthly HBsAg for susceptible patients: CDC 2001 schedule as widely cited – NEEDS REVIEW against MMWR table.
[WEB] HCV: KDIGO 2018 – screen all patients on initiation of in-center HD or transfer; screen every 6 months (immunoassay or NAT, grade 1B); isolation of HCV-infected patients not necessary/dedicated machines not recommended (summaries: https://ajkdblog.org/2019/02/22/caring-for-patients-with-hepatitis-c-and-ckd-in-the-modern-era-the-2018-kdigo-guideline/ ; KDIGO PMC6336217). Chapter 3 unchanged in KDIGO 2022.
HIV: CDC 2001 – isolation not required; standard precautions. Saudi 'Dialysis Safety' guideline reportedly requires HIV, HCV, HBV testing of new and transferred patients (PMC4144264, secondary) – CONFIRM LOCALLY."""},

    {"kind": "stat_cards", "title": "Hepatitis B vaccination and follow-up",
     "source": "CDC Guidelines for vaccinating dialysis patients (ACIP-based) · CDC MMWR 2001",
     "stats": [("40 µg", "dose per injection for HD patients (dialysis formulation or double dose)"), ("1–2 months", "after the series: test anti-HBs"), ("≥ 10 mIU/mL", "anti-HBs = protective response"), ("Annually", "anti-HBs in responders; booster if < 10")],
     "cards": [
         ("Non-responders", ["Repeat a full vaccine series", "Test again; if still < 10: test HBsAg", "Treat as susceptible (monthly HBsAg)"]),
         ("Staff", ["Vaccination and anti-HBs status per occupational health", "Post-exposure plan known"]),
         ("Nurse role", ["Track due dates", "Document doses and results", "Escalate missing status"]),
     ],
     "notes": """
[WEB] CDC vaccination guidance for dialysis patients: Recombivax HB dialysis formulation 40 µg at 0, 1, 6 months; Engerix-B 2 × 20 µg (40 µg) at 0, 1, 2, 6 months; test anti-HBs 1–2 months after the last dose; responders tested annually, booster when anti-HBs < 10 mIU/mL; non-responders revaccinated with a second series, then tested for HBsAg if still non-responsive. Source: https://stacks.cdc.gov/view/cdc/143156/cdc_143156_DS1.pdf (""" + ACCESSED + """). Products and schedules available in Saudi Arabia may differ – CONFIRM with pharmacy/national schedule."""},

    {"kind": "algorithm", "title": "Suspected infection-control breach: act and report",
     "source": "CDC MMWR 2001 · NHSN Dialysis Event Protocol 2026 · local IPC and occupational health policy",
     "w": 5.4, "no_w": 3.2,
     "nodes": [
         {"t": "start", "text": "Breach seen or suspected (e.g. shared vial, no glove change)"},
         {"t": "action", "text": "Stop the practice; make the patient and area safe"},
         {"t": "decision", "text": "Blood exposure possible?", "no": "Correct, coach, document; report per policy", "no_label": "No"},
         {"t": "action", "text": "Yes: notify nurse in charge, physician and IPC now"},
         {"t": "action", "text": "IPC decides: patient testing, look-back, staff exposure care"},
         {"t": "end", "text": "Incident report; feedback and learning at team huddle"},
     ],
     "side": {"head": "Also report", "fill": "sand", "body": ["New HBsAg or anti-HCV positive result", "Clusters of fever or bacteremia", "Positive blood culture, IV antimicrobial start, access pus/redness (NHSN dialysis events)"]},
     "notes": "Visual 4 (algorithm). Breach management steps are general IPC practice; testing and look-back decisions belong to IPC/medical leadership. NHSN dialysis event types: positive blood culture, outpatient IV antimicrobial start, pus/redness/increased swelling at the access (https://www.cdc.gov/nhsn/faqs/dialysis/faq-dialysis-event-reporting.html). Saudi MOH collects dialysis events via HESN (secondary) – CONFIRM LOCALLY."},

    {"kind": "checklist", "title": "Observation checklist (peer audit)",
     "source": "Adapted from CDC audit tools (hand hygiene, catheter care, station disinfection, injection safety)",
     "row_h": 0.55, "size": 12, "h": 4.95,
     "columns": [
         ("Hands and PPE", ["Hand hygiene before patient contact", "Hand hygiene before aseptic task", "Gloves changed between patients", "Hand hygiene after glove removal", "Splash PPE at connection/disconnection"]),
         ("Access and meds", ["Skin antisepsis with contact time", "CVC hub scrubbed every time", "Masks for CVC procedures", "Meds prepared in clean area", "Single-dose vial discarded"]),
         ("Environment", ["Station disinfected after patient left", "All touched surfaces covered", "Contact time respected", "No items returned to clean area", "HBV station/machine dedicated"]),
     ],
     "notes": "Summary aid: observe 10 opportunities per item per month, record yes/no, calculate % compliance and share results (feeds Lecture 08 indicators). Adapted from CDC audit tool topics; not an official CDC form."},

    {"kind": "case", "title": "Scenario: a busy changeover",
     "source": "Fictional teaching scenario",
     "case": [
         "11:00 changeover. A nurse finishes Mr E (CVC) and starts Mrs F (AVF) with the same gloves.",
         "Chair 3 is wiped while the next patient is already seated.",
         "An opened heparin vial from station 2 is returned to the medication room.",
         "Mr G, newly HBsAg-positive, waits for a station."],
     "questions": [
         "List each error.",
         "What should have happened at chair 3?",
         "What happens to the heparin vial?",
         "Where and how is Mr G dialysed today?"],
     "notes": """
1. No glove change/hand hygiene between patients; disinfection with patient present; item returned from station to clean area; HBsAg+ patient not yet isolated.
2. Wait until the patient leaves; remove items; clean blood; disinfect touched surfaces with contact time.
3. Discard (items taken to a station are not returned; single-dose vials one patient, one entry).
4. Notify physician/IPC; separate room/area, dedicated machine and equipment; staff not caring for susceptible patients on the same shift (CDC 2001; local policy)."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Which patient needs a dedicated machine and room?", ["A. Anti-HCV positive", "B. HBsAg positive", "C. HIV positive", "D. MRSA carrier only"]),
         ("When do you disinfect the station?", ["A. While the patient is seated", "B. After the patient has left", "C. Once per day", "D. Only if blood is visible"]),
         ("A single-dose vial is…", ["A. Used for two patients if clean", "B. Entered once for one patient", "C. Stored at the station", "D. Kept for the next shift"]),
         ("KDIGO HCV screening in in-center HD?", ["A. Never", "B. Yearly only", "C. At start/transfer and every 6 months", "D. Monthly ALT only"]),
     ],
     "notes": "Q1 B (CDC 2001; HCV/HIV not isolated). Q2 B (CDC). Q3 B (CDC injection safety). Q4 C (KDIGO 2018, grade 1B). MRSA and other MDROs: follow local contact-precaution policy (not covered in detail here)."},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 04 summary",
     "items": [
         ("Hands first, every time", "5 moments; change gloves and clean hands between patients and stations."),
         ("Clean stays clean", "Prepare medications away from stations; nothing returns from a station."),
         ("Disinfect after the patient leaves", "All touched surfaces, wet contact time; internal per IFU."),
         ("HBV is different", "Isolation for HBsAg+; HCV and HIV: strict standard precautions, no isolation."),
         ("Report breaches and events", "Stop, notify, document; IPC decides on follow-up."),
     ],
     "notes": "Bridge to Day 3: adequacy and water safety."},

    refs_slide(),
]
