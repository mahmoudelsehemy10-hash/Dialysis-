# -*- coding: utf-8 -*-
"""Lecture 04 - Day 2: Infection Prevention in Hemodialysis: Aseptic Practice, Disinfection, and Isolation."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Infection_Prevention"
TITLE = "Infection Prevention in Hemodialysis: Aseptic Practice, Disinfection, and Isolation"
SUBTITLE = "Day 2 · Vascular Access & Infection Control · Lecture 04"
FOOTER_TEXT = "L04 Infection prevention"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 04 of the Hemodialysis Nursing Programme (Day 2). 45–60 minutes.
Primary references: CDC 2001 MMWR recommendations for chronic hemodialysis units, CDC Dialysis Core Interventions, NHSN Dialysis Event Surveillance. cdc.gov pages could not be opened from the build environment; key points were verified through search summaries and are flagged for review against the current CDC text and national policy.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 04",
     "items": [
         ("Explain", ["Why HD patients are high risk", "How pathogens spread in the unit"]),
         ("Practise", ["Hand hygiene and gloves", "Aseptic technique and medication safety"]),
         ("Disinfect", ["Clean the station between patients", "Separate clean and dirty"]),
         ("Isolate and report", ["Apply HBV isolation", "Report NHSN dialysis events"]),
     ],
     "notes": "Objectives for Lecture 04."},

    {"kind": "stat_cards", "title": "Why HD patients are at high infection risk",
     "source": "AREP Vascular Access (USRDS 2019; Schild AF 2008; Daugirdas 2014) · CDC MMWR 2001;50(RR-5)",
     "stats": [("3×/week", "blood access, shared space and equipment"), ("10% vs 1%", "access infection: AVG vs AVF"), ("40%", "of HD patients carry S. aureus (27% general population)"), ("CVC", "highest bloodstream infection risk")],
     "cards": [
         ("Patient factors", ["Reduced immunity (uremia, diabetes)", "Frequent hospital contact", "Skin breaks at access sites"]),
         ("Environment factors", ["Blood on surfaces, many patients", "Shared machines and chairs", "Busy changeover times"]),
         ("Main routes", ["Hands of staff", "Contaminated surfaces and items", "Medication preparation"]),
     ],
     "notes": """
Figures as reported in AREP [vascular access / 152433, 153446]: infection rates ~10× higher with AVG (10% vs 1% AVF); S. aureus nasal/skin carriage 40% of HD patients vs 27% of the general population.
CVCs carry the highest BSI risk (CDC; KDOQI 2019). Transmission routes and the HD environment: CDC MMWR 2001;50(RR-5)."""},

    {"kind": "checklist", "title": "CDC Core Interventions for bloodstream infection prevention",
     "source": "CDC Core Interventions for Dialysis Bloodstream Infection Prevention (cdc.gov/dialysis-safety) · NHSN",
     "row_h": 0.62, "size": 13, "h": 4.25,
     "columns": [
         ("Unit level", ["Surveillance and feedback (NHSN)", "Monthly hand hygiene observations", "Catheter / access care observations", "Staff education and competency", "Patient education and engagement"]),
         ("At the chair", ["Catheter reduction efforts", "CHG skin antisepsis (> 0.5% with alcohol)", "Catheter hub disinfection every time", "Antimicrobial ointment at exit site (per protocol)"]),
     ],
     "banner": "Share audit results with the team every month: feedback changes practice",
     "notes": """
[WEB] CDC Core Interventions (verified via search summaries; cdc.gov not reachable from build environment – NEEDS REVIEW against https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/): surveillance and feedback using NHSN; hand hygiene observations (monthly, results shared with staff); catheter/vascular access care observations; staff education and competency; patient education/engagement; catheter reduction; chlorhexidine for skin antisepsis; catheter hub disinfection (scrub hubs with an appropriate antiseptic after the cap is removed and before accessing, every time); antimicrobial ointment at catheter exit sites. Summary source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5332080/table/table5-2054358116669129 (""" + ACCESSED + """).
Ointment choice must be compatible with the catheter material (manufacturer instructions)."""},

    {"kind": "two_cards", "title": "Hand hygiene and gloves at the dialysis station",
     "source": "CDC MMWR 2001;50(RR-5) · WHO My 5 Moments for Hand Hygiene · CDC Dialysis Safety",
     "h": 3.75,
     "cards": [
         ("Clean hands", ["Before touching the patient or the machine", "Before aseptic tasks (cannulation, CVC)",
                          "After blood or body fluid exposure", "After touching the patient or station", "When moving between patients or stations"]),
         ("Gloves", ["Wear when caring for the patient or touching the station", "Remove and clean hands between patients and stations",
                     "Change between dirty and clean tasks", "Gloves never replace hand hygiene", "No gloves in clean (medication) areas"]),
     ],
     "banner": "Alcohol-based hand rub at every station; soap and water when hands are visibly soiled",
     "notes": """
CDC 2001 MMWR (HD units): wear disposable gloves when caring for a patient or touching the patient's equipment at the dialysis station; remove gloves and wash hands between each patient or station.
WHO 5 Moments (before patient contact, before aseptic task, after body fluid exposure risk, after patient contact, after touching patient surroundings) adapted to the dialysis station.
CDC Core Interventions include monthly hand hygiene audits with feedback."""},

    {"kind": "steps", "title": "Disinfect the station between patients",
     "source": "CDC MMWR 2001;50(RR-5) · CDC Dialysis Station Routine Disinfection tools · Machine IFU",
     "steps": [
         ("Wait until the patient has left", "Do not disinfect around a seated patient; remove all disposables"),
         ("Discard", "Single-use items and unused supplies taken to the station are discarded or dedicated"),
         ("Clean visible blood first", "Then disinfect with an approved (e.g. EPA-registered) hospital disinfectant"),
         ("Disinfect all touched surfaces", "Chair, side table, machine front and top, control panel, BP cuff"),
         ("Respect contact time", "Keep surfaces wet for the label contact time; let dry"),
         ("Machine internal disinfection", "Per IFU between patients/end of day; test for residual disinfectant"),
     ],
     "side": {"head": "Clean vs dirty", "fill": "sand", "body": [
         "Medications prepared in a clean area away from stations", "No shared medication carts at stations",
         "Single-dose vials, one patient", "Items taken to a station are not returned to the clean area",
         "Separate sinks for hand washing and for blood samples"]},
     "notes": """
CDC MMWR 2001: clean and disinfect the dialysis station (chairs, beds, tables, machines) between patients; give special attention to control panels and other surfaces frequently touched; discard all fluid and clean and disinfect surfaces including containers associated with the prime waste; items taken to the station should be either disposed of, dedicated to a single patient, or cleaned and disinfected before return to a common clean area; prepare medications in a clean area separated from stations; do not use common medication carts; use single-dose vials for a single patient where possible.
[WEB] CDC Collaborative tools include a "routine dialysis station disinfection" observation checklist; the timing "after the patient has left the station" is emphasised in CDC educational material – verify against current CDC tool (not reachable from build environment).
Disinfectant choice and contact time: product label and local infection control policy."""},

    {"kind": "table_only", "title": "Bloodborne viruses: isolation and testing",
     "source": "CDC MMWR 2001;50(RR-5):1-43 · CMS 42 CFR 494.30 · National policy may differ",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.2, 4.85, 5.0], "row_h": 0.92, "size": 12,
               "rows": [["Virus", "Unit practice", "Routine testing (CDC 2001 schedule)"],
                        ["Hepatitis B (HBsAg+)", "Separate room, dedicated machine, equipment, supplies; staff do not care for susceptible patients on the same shift",
                         "HBsAg+: annual HBsAg and anti-HBs · Susceptible (incl. non-responders): HBsAg monthly"],
                        ["HBV immune", "Standard precautions; vaccinate susceptible patients and staff",
                         "Vaccine responders: anti-HBs annually; booster if < 10 mIU/mL"],
                        ["Hepatitis C", "Standard precautions strictly; isolation not routinely required by CDC",
                         "Anti-HCV negative: anti-HCV every 6 months, ALT monthly"],
                        ["HIV", "Standard precautions; no isolation required", "Per national policy"]]},
     "banner": "New positive result (seroconversion): notify infection control and the physician immediately",
     "banner_y": 6.0,
     "notes": """
CDC MMWR 2001;50(RR-5) recommendations for chronic HD units (verified via secondary summaries; the MMWR full text could not be opened from the build environment):
- HBsAg-positive patients: dialyze in a separate room using separate machines, equipment, instruments, supplies and medications; staff caring for them should not care for HBV-susceptible patients at the same time (same shift or changeover).
- Anti-HBs booster when level falls below 10 mIU/mL (CDC archived page).
- Testing intervals shown (monthly HBsAg for susceptible; annual anti-HBs for responders; anti-HCV semiannual and ALT monthly for anti-HCV-negative; annual HBsAg/anti-HBs for chronic HBV) are from the CDC 2001 table as commonly cited – NEEDS REVIEW against the MMWR table and current national/local policy (some countries use different schedules or HCV RNA testing).
Sources: https://Www.cdc.gov/mmwr/PDF/rr/rr5005.pdf ; https://ipac-canada.org/photos/custom/OldSite//pdf/hemodialysisHBV.pdf (""" + ACCESSED + """).
CMS 42 CFR 494.30 adopts CDC recommendations for ESRD facilities in the US."""},

    {"kind": "stat_cards", "title": "Recognise and report dialysis events",
     "source": "CDC NHSN Dialysis Event Surveillance Protocol (January 2026) · NHSN FAQ",
     "stats": [("Event 1", "Positive blood culture (outpatient or ≤ 1 day after admission)"), ("Event 2", "Outpatient IV antimicrobial start"), ("Event 3", "Pus, redness or increased swelling at access site"), ("21 days", "rule separates new events")],
     "cards": [
         ("Nurse's role", ["Inspect access and exit sites every session", "Record signs with date and time", "Obtain cultures before antibiotics per order"]),
         ("Report", ["Use the unit form for every event", "Include suspected source", "Link to the infection control lead"]),
         ("Use the data", ["Monthly rates per 100 patient-months", "Compare with previous months", "Feed back to staff (core intervention)"]),
     ],
     "notes": """
[WEB] NHSN Dialysis Event surveillance: three event types – positive blood culture (collected as outpatient or within 1 calendar day after hospital admission), outpatient IV antimicrobial start, and pus, redness or increased swelling at the vascular access site. Separate events require ≥ 21 days between them (IV antimicrobial: between end of first course and start of next; blood cultures: between collection dates). Per NHSN, from 1 Oct 2026 outcome tracking moves to a 30-day window. Current protocol: January 2026. Sources: https://www.cdc.gov/nhsn/faqs/dialysis/faq-dialysis-event-reporting.html ; https://www.tn.gov/health/rpd/healthcare-associated-infections-dialysis-events.html ; https://www.cdc.gov/nhsn/pdfs/dialysis/August-2026-Office-Hours.pdf (""" + ACCESSED + """). Verify details against the protocol before training on rules.
NHSN is a US system; outside the US use the national surveillance system with the same principles."""},

    {"kind": "case", "title": "Case: a busy changeover",
     "source": "Fictional teaching case",
     "case": [
         "Changeover at 11:00. A nurse finishes Mr E (CVC) and moves straight to Mrs F (AVF) with the same gloves.",
         "Chair 3 is wiped while the next patient is already sitting in it.",
         "An opened heparin vial from station 2 is returned to the medication room.",
         "Mr G, newly HBsAg-positive this morning, is waiting for a station."],
     "questions": [
         "Identify each infection control error.",
         "What should have happened at chair 3?",
         "What happens to the heparin vial?",
         "Where and how is Mr G dialyzed today?"],
     "notes": """
Suggested answers (educational):
1. Gloves not changed and no hand hygiene between patients; station disinfected with patient present; multi-use item returned from station to clean area; HBsAg-positive patient not yet isolated.
2. Wait until the patient leaves; remove items; clean visible blood; disinfect all touched surfaces with contact time; then seat next patient.
3. Items taken to a station must be discarded or dedicated to that patient – discard (CDC 2001).
4. Notify physician and infection control; separate room/area with dedicated machine, equipment and staff not caring for susceptible patients on the same shift (CDC 2001); follow local policy."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 04 summary",
     "items": [
         ("Hands and gloves", "Clean hands and change gloves between every patient and station."),
         ("Aseptic access care", "CHG skin antisepsis, hub scrub every time, masks for CVC procedures."),
         ("Station disinfection", "After the patient leaves: all touched surfaces, correct contact time."),
         ("Clean stays clean", "Prepare medications away from stations; nothing returns from a station."),
         ("Isolate HBV, report events", "Dedicated room, machine and staff for HBsAg+; report NHSN events."),
     ],
     "notes": "Summarise and link to Day 3 (adequacy and water safety)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["cdc_2001"], R["cdc_core"], R["nhsn"], "CDC NHSN. Frequently Asked Questions about Dialysis Event Reporting.",
              R["cms_cfc"], "World Health Organization. My 5 Moments for Hand Hygiene. WHO; 2009.", R["kdoqi_va"],
              "Canadian position statement on HBV in hemodialysis (IPAC Canada), citing CDC 2001.", R["arep"]],
     "notes": "References for Lecture 04."},
]
