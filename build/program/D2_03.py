# -*- coding: utf-8 -*-
"""Day 2 · Lecture 03: Vascular Access Care: AVF/AVG Cannulation and CVC Safety."""
from program._common import *  # noqa: F401,F403

TITLE = "Vascular Access Care: AVF/AVG Cannulation and CVC Safety"
SUBTITLE = "Day 2 · Vascular Access & Infection Control · Lecture 03"
FOOTER_TEXT = "Day 2 · Lecture 03"
REFS = ["AREP_VA", "AREP_HD", "KDOQI_VA19", "CDC_CORE", "CDC_2001", "NKF_NEEDLE", "VA_CHAN14", "VA_MUIR14",
        "ANNA", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 2, Lecture 03 (30–40 min). Content: AREP Vascular Access module (uploaded) and KDOQI Vascular Access 2019; CVC care aligned with CDC core interventions. Cannulation technique choice depends on access type, cannulator competency and local policy.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 03 objectives",
     "items": [
         ("Describe", ["Compare AVF, AVG and CVC and their nursing implications"]),
         ("Assess", ["Examine an access and name 4 signs of dysfunction or infection"]),
         ("Cannulate", ["Select technique and needle gauge for the prescribed blood flow"]),
         ("Protect", ["Perform CVC connection, dressing and lock handling steps safely"]),
     ],
     "notes": "Assessed through the case (slide 16) and knowledge check (slide 17)."},

    {"kind": "opening", "title": "Opening question: what is this access telling you?",
     "source": "Fictional teaching scenario",
     "story": ["Tuesday: the upper-arm fistula has a strong, pulsing beat, but you cannot feel a thrill.",
               "Needle sites bled for 35 minutes after the last session."],
     "prompts": ["Is a strong pulse a good sign here?", "Would you cannulate today?", "Who do you inform?"],
     "notes": "Expected: a pulsatile access without thrill plus prolonged bleeding suggests outflow stenosis; do not cannulate before assessment; inform physician/access team (KDOQI 2019). Answered fully in the case."},

    {"kind": "access_schematic", "title": "Three access types: how they are built",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019 · AREP Vascular Access",
     "implications": [
         ("AVF: nursing implications", ["Best long-term option for many", "Needs maturation (weeks)", "Rotate sites (rope ladder)"]),
         ("AVG: nursing implications", ["Earlier use than AVF", "Cannulate the graft, rotate sites", "More stenosis and thrombosis"]),
         ("CVC: nursing implications", ["Immediate use, no needles", "Highest infection risk", "Strict aseptic handling"]),
     ],
     "notes": """
Visual 1 (editable schematic, not to scale). AVF: surgical connection of an artery to a vein; the vein enlarges ('arterialises') and is cannulated. AVG: synthetic tube between artery and vein, cannulated directly. Tunnelled CVC: catheter in a central vein (commonly internal jugular) with the tip near the right atrium, a subcutaneous tunnel with a cuff, and an exit site on the chest (KDOQI 2019; AREP [vascular access / 151058, 151232]).
Schematic drawn as editable shapes to avoid inaccurate anatomical images; actual configuration varies – check the access record."""},

    {"kind": "table_pie", "title": "Advantages and challenges compared",
     "source": "Blake PG, et al. Kidney Int. 2012 · KDOQI 2019 · DOPPS Practice Monitor, Nov 2015 (as shown in AREP)",
     "table": {"w": 8.3, "col_w": [1.5, 3.3, 3.5], "row_h": 1.35, "head_h": 0.45, "size": 11,
               "rows": [["Access", "Advantages", "Challenges"],
                        ["AV fistula (AVF)", ["Very low infection risk", "Long lasting once mature", "Lower mortality association"],
                         ["High primary failure rate", "Pain and bruising early on", "Aneurysm and bleeding risk"]],
                        ["AV graft (AVG)", ["Low infection risk", "Low primary failure rate", "Lower mortality than CVC"],
                         ["High secondary failure rate", "Frequent interventions", "Bleeding risk"]],
                        ["Central venous catheter (CVC)", ["Ease of insertion", "Immediate use", "No cannulation"],
                         ["Highest infection and mortality", "Dysfunction, thrombolytics", "Central vein damage"]]]},
     "pie": {"title": "Access in use, DOPPS 2015 (%)",
             "data": [("AVF", 66.5), ("AVG", 18.4), ("CVC", 15.1)],
             "note": "Adapted in AREP from DOPPS Practice Monitor (Nov 2015); population as reported in the module. Not local data."},
     "notes": """
Visual 2 (table + chart). AREP [Dialysis / 144615, 142509; vascular access / 151232] (Blake PG, et al. Kidney Int 2012).
Pie values from AREP (DOPPS Nov 2015); population not stated (likely US) – NEEDS REVIEW; replace with local registry data where available.
[WEB] KDOQI 2019: individual 'ESKD Life-Plan' rather than a single 'Fistula First' rule."""},

    {"kind": "rule6", "title": "Assess before every use: look, listen, feel",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019 · AREP Vascular Access",
     "lead": "New AVF: usually usable when it meets the 'rule of 6s'",
     "sixes": [("6 wk", "after creation"), ("600", "mL/min access flow"), ("< 0.6 cm", "deep below the skin"), ("≥ 0.6 cm", "vessel diameter")],
     "left": {"head": "Normal findings", "body": ["Continuous low-pitched bruit", "Thrill at the anastomosis", "Vein softens/collapses when arm is raised"]},
     "right": {"head": "Abnormal: report", "body": ["High-pitched or pulsatile only", "Arm, face or breast swelling", "No thrill or bruit: do not cannulate"]},
     "notes": """
KDOQI 2019 physical examination (AREP [vascular access / 153406, 153427]). Physical exam PPV for stenosis: 70–80% AVG, 93% AVF (as reported by AREP). Rule of 6s per KDOQI; 25–50% of AVFs never mature (AREP [151710])."""},

    {"kind": "matrix", "title": "Dysfunction or infection? Signs and actions",
     "source": "Lok CE, et al. KDOQI 2019 · AREP Vascular Access (Achneck HE 2010; Daugirdas 2014)",
     "rows": [
         ("Thrombosis", "No thrill or bruit; clots on aspiration", "Do not cannulate; notify urgently"),
         ("Stenosis", "Pulsatile, high-pitched bruit, prolonged bleeding, high venous pressure", "Report; referral for imaging per protocol"),
         ("Infection", "Redness, pus, warmth, pain, fever", "Do not cannulate the site; cultures; notify"),
         ("Steal / ischemia", "Cold, pale, painful or numb hand", "Notify physician/access surgeon"),
         ("Aneurysm", "Enlarging bulge, thin shiny skin", "Avoid cannulating; urgent review if skin breaks down"),
     ],
     "fills": ["navy", "blue", "mid", "blue", "grey"],
     "notes": "AREP [vascular access / 151733, 152344–152543]: thrombosis 80–85% of access loss; infection 10% AVG vs 1% AVF; steal 1–20% of AV accesses; aneurysm 5% to > 60% (figures as reported in AREP). Shiny thin skin over an aneurysm is a rupture risk – urgent review."},

    {"kind": "two_images", "title": "Choose the cannulation technique",
     "source": "Schmidli J, et al. Eur J Vasc Endovasc Surg. 2018 · KDOQI 2019 · Muir CA, et al. CJASN 2014",
     "images": [("rope_ladder.png", "Rope-ladder cannulation sites (AREP)", "Rope ladder: default",
                 ["New sites each session along the whole AVF or graft", "≥ 3 cm from anastomosis; ≥ 5 cm between tips", "Venous needle in direction of flow"]),
                ("buttonhole.png", "Buttonhole cannulation sites (AREP)", "Buttonhole: AVF only, selected cases",
                 ["Same site, angle, depth each time", "Higher infection risk: strict asepsis", "Only if competent and allowed by policy"])],
     "caption": "Illustrations: FMC AREP Vascular Access (uploaded screenshots 151911, 152109). Area (one-site) puncture is not recommended.",
     "notes": """
Visual 3 (uploaded illustrations). AREP [vascular access / 151911–152452]: rope ladder preferred; buttonhole only for AVFs, not AVGs, limited to special circumstances (higher local and generalised infection: Muir CA, et al. CJASN 2014; O'Brien FJ 2012); area technique no longer recommended (aneurysms, thin skin, prolonged bleeding).
Primary patency similar: buttonhole 86/72/57% vs rope ladder 89/71/60% at 3/6/12 months (Chan MR, et al. Semin Dial 2014, as shown in AREP).
Technique selection also depends on cannulator competency and local policy."""},

    {"kind": "steps", "title": "Safe AVF/AVG cannulation",
     "source": "Lok CE, et al. KDOQI 2019 · AREP Vascular Access · NKF Clinical Update 2016",
     "steps": [
         ("Prepare", "Hand hygiene, clean gloves; access arm washed with soap and water"),
         ("Assess and plan", "Look, listen, feel; sites, direction, gauge for prescribed Qb"),
         ("Skin antisepsis", "2% CHG/70% alcohol, 30 s scrub, dry; or povidone-iodine 2–3 min"),
         ("Insert and secure", "No-touch; angle by depth; flashback; tape securely"),
         ("Check", "Flush/aspirate; arterial pressure; no swelling or pain"),
         ("Keep visible", "Needles and lines uncovered all treatment"),
     ],
     "side": {"head": "Minimum needle gauge", "fill": "sand", "body": [
         ("< 300 mL/min: 17 G", {"size": 14, "space_after": 5}), ("300–350 mL/min: 16 G", {"size": 14, "space_after": 5}),
         ("> 350–450 mL/min: 15 G", {"size": 14, "space_after": 5}), ("> 450 mL/min: 14 G", {"size": 14, "space_after": 10}),
         "Smallest needles for new AVFs", "Max. 2 attempts, then an expert"]},
     "notes": """
KDOQI 2019 skin preparation (AREP [vascular access / 153505]). Needle table: NKF Clinical Update 2016 as reproduced in AREP [153559]. Max 2 attempts before seeking an expert (Schmidli 2018, AREP [153931]).
Insertion angle depends on access depth and type – follow local cannulation policy."""},

    {"kind": "columns", "title": "Prevent infiltration, bleeding and dislodgement",
     "source": "AREP Vascular Access (Axley B 2012; Sandroni S 2008; Lee T) · Hawley CM, et al. 2008",
     "h": 3.4, "banner_y": 5.25,
     "columns": [
         {"head": "Infiltration", "rows": [("Recognise", "Swelling, pain, bruising, high pressure alarms"),
                                           ("Act", "Stop pump per protocol; withdraw needle if needed; pressure, ice; reassess")]},
         {"head": "Bleeding", "rows": [("Recognise", "Oozing at sites, wet dressing"),
                                       ("Act", "Pressure; check needle and tape; review heparin dose with physician")]},
         {"head": "Needle dislodgement", "rows": [("Recognise", "Blood on bed/floor; venous alarm may NOT trigger"),
                                                  ("Act", "Stop pump, clamp, pressure, call help (L07)")]},
     ],
     "banner": "Secure taping, access always visible, regular checks: the best alarm is the nurse",
     "notes": "AREP [vascular access / 152609, 152716, 153817]: VND life-threatening at Qb 400–500 mL/min; infiltration annual rate 6.8% (Lee T, et al., as cited); mitigation: secure taping, access visible, BP/pulse monitoring, wetness detectors, patient education. Venous pressure monitoring may not detect VND (standard safety teaching)."},

    {"kind": "two_cards", "title": "Needle removal and hemostasis",
     "source": "AREP Vascular Access (Clinical Pearls) · KDOQI 2019 · ANNA Core Curriculum 2015",
     "h": 3.7,
     "cards": [
         ("Do", ["Remove tape gently; withdraw at insertion angle", "Pressure only after the needle is out", "Gentle pressure: thrill still palpable",
                 "One site at a time; confirm hemostasis", "Sharps into container immediately"]),
         ("Report", ["Bleeding much longer than usual", "New hematoma", "Loss of thrill or bruit", "Cold, painful or numb hand", "Infection signs at sites"]),
     ],
     "banner": "Prolonged bleeding may mean outflow stenosis or too much anticoagulation",
     "notes": "AREP Clinical Pearls [154022]: use the same angle for insertion and removal to prevent vessel wall damage. Occlusive pressure risks thrombosis. Prolonged bleeding may indicate venous outflow stenosis (KDOQI 2019)."},

    {"kind": "steps", "title": "CVC connection, disconnection and hub care",
     "source": "CDC Core Interventions · CDC MMWR 2001 · KDOQI 2019 · catheter and lock IFU",
     "steps": [
         ("Prepare", "Hand hygiene; masks for staff and patient per policy; clean gloves"),
         ("Inspect exit site", "Redness, discharge, tenderness, dressing intact"),
         ("Hub scrub", "Remove cap; scrub hub with antiseptic each time opened; let dry"),
         ("Aspirate the lock", "Withdraw and discard lock volume per catheter labelling and policy"),
         ("Connect / disconnect", "Aseptic non-touch; clamps closed before opening; no lumen open to air"),
         ("Lock and cap", "Prescribed lock, volume per lumen label; new sterile caps"),
     ],
     "side": {"head": "Never", "fill": "navy", "body": [
         "Leave a lumen open or unclamped", "Force a blocked catheter", "Touch the hub after scrubbing",
         "Use the HD catheter for other infusions without an order", "Ignore fever or exit-site pus"]},
     "notes": """
[WEB] CDC Core Interventions (via summaries; cdc.gov not reachable from the build environment – NEEDS REVIEW against current CDC page): CHG (> 0.5% with alcohol) skin antisepsis; scrub catheter hubs with antiseptic after cap removal and before accessing, every time; antimicrobial ointment at exit site per protocol and catheter compatibility; catheter care observations.
Air embolism risk if a lumen is open to air (Lecture 07)."""},

    {"kind": "two_cards", "title": "Dressings and catheter lock solutions",
     "source": "CDC Core Interventions · catheter and lock solution IFU · local policy",
     "h": 3.7,
     "cards": [
         ("Exit site and dressing", ["Assess every session", "Change per policy or if wet, loose, soiled", "CHG-alcohol skin antisepsis; let dry",
                                     "Ointment only if compatible with catheter", "Secure the external limbs"]),
         ("Lock solutions (prescribed)", ["Use only the prescribed agent", "Volume = lumen fill volume on the catheter", "Label lumens per policy",
                                          "Aspirate and discard before use", "Never flush the lock into the patient"]),
     ],
     "banner": "Lock agent, volume and handling follow the product IFU and the prescription",
     "notes": """
Lock solutions (e.g. heparin, citrate, or other prescribed agents) are prescription medicines; volume follows the lumen fill volume printed on the catheter. Flushing the lock into the patient can cause systemic anticoagulation or other effects – aspirate and discard before use per policy.
Specific agents, concentrations and volumes are NOT given here deliberately: follow the product IFU and local protocol (NEEDS LOCAL CONFIRMATION)."""},

    {"kind": "checklist", "title": "Access care checklist and patient education",
     "source": "AREP Vascular Access (AV Access Care) · KDOQI 2019",
     "row_h": 0.55, "size": 12, "h": 4.95,
     "columns": [
         ("Every AVF/AVG use", ["Look, listen, feel", "Technique and gauge chosen", "Skin antisepsis, dry", "Needles secured, visible", "Hemostasis confirmed", "Findings documented"]),
         ("Every CVC use", ["Mask, hand hygiene, gloves", "Exit site assessed", "Hub scrubbed every time", "Lock aspirated and discarded", "Clamps and caps secure", "Dressing per policy"]),
         ("Teach the patient", ["Check thrill daily", "Wash arm before HD", "No BP/IV on access arm", "No tight clothing, heavy carrying", "Keep CVC dressing dry", "Report fever, pain, swelling"]),
     ],
     "notes": "AREP [vascular access / 152637]: all patients should be taught to compress bleeding, wash skin, recognise infection, palpate thrill, avoid heavy carrying and sleeping on the access arm, and report signs and symptoms."},

    {"kind": "case", "title": "Case: abnormal access findings",
     "source": "Fictional teaching case (illustrative training data)",
     "case": [
         "Ms D, 55 years, left upper-arm AVF, rope ladder.",
         "Last session: sites bled 35 minutes (usual 10).",
         "Today: strong pulse, weak thrill, high-pitched bruit; arm slightly swollen.",
         "Prescribed Qb 400 mL/min; 17 G needles prepared."],
     "questions": [
         "What do the findings suggest?",
         "Would you cannulate? What first?",
         "Is 17 G suitable for Qb 400?",
         "What do you document and report?"],
     "notes": """
1. Pulsatile access, high-pitched bruit, swelling and prolonged bleeding → possible venous outflow stenosis.
2. Notify physician/access team first; cannulate only if instructed, by an experienced cannulator; consider ultrasound guidance.
3. No: > 350–450 mL/min needs at least 15 G (NKF table in AREP).
4. Exam findings, bleeding time, achieved Qb and pressures, notification and orders, referral."""},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Normal AVF finding?", ["A. High-pitched pulsatile bruit", "B. Continuous low-pitched bruit", "C. No thrill", "D. Arm swelling"]),
         ("Minimum gauge for Qb 320 mL/min?", ["A. 17 G", "B. 16 G", "C. 15 G", "D. 14 G"]),
         ("Buttonhole cannulation is…", ["A. Preferred for AVGs", "B. For AVFs only, in selected cases", "C. The same as area puncture", "D. Lower infection risk"]),
         ("Before using a CVC lumen you should…", ["A. Flush the lock into the patient", "B. Aspirate and discard the lock", "C. Leave the cap off to dry", "D. Skip the hub scrub if gloved"]),
     ],
     "notes": """
Q1 B (KDOQI 2019 exam). Q2 B – 300–350 mL/min: 16 G (NKF table). Q3 B – buttonhole for AVFs only, higher infection risk. Q4 B – aspirate and discard lock per policy; hub scrub every time (CDC)."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 03 summary",
     "items": [
         ("Know the access", "AVF, AVG and CVC differ in risks and care."),
         ("Examine before every use", "No thrill/bruit, infection or steal signs: do not cannulate; report."),
         ("Technique by type, competency, policy", "Rope ladder default; buttonhole AVF only; match gauge to Qb."),
         ("CVC = asepsis every time", "Mask, hub scrub, closed clamps, aspirate the lock."),
         ("Visible access, educated patient", "Prevent dislodgement, bleeding and infection together."),
     ],
     "notes": "Bridge to Lecture 04: infection prevention across the whole unit."},

    refs_slide(),
]
