# -*- coding: utf-8 -*-
"""Lecture 03 - Day 2: Vascular Access Care: AVF/AVG Cannulation and CVC Safety."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Vascular_Access_Care"
TITLE = "Vascular Access Care: AVF/AVG Cannulation and CVC Safety"
SUBTITLE = "Day 2 · Vascular Access & Infection Control · Lecture 03"
FOOTER_TEXT = "L03 Vascular access care"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 03 of the Hemodialysis Nursing Programme (Day 2). 45–60 minutes.
Content from the AREP Vascular Access module (uploaded screenshots) and the KDOQI Vascular Access 2019 update; CVC care aligned with CDC core interventions.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 03",
     "items": [
         ("Know", ["Compare AVF, AVG and CVC", "Know maturation criteria"]),
         ("Examine", ["Look, listen, feel every time", "Detect early dysfunction"]),
         ("Cannulate", ["Choose technique and needle", "Prepare skin aseptically"]),
         ("Protect", ["Connect and disconnect CVCs safely", "Prevent complications"]),
     ],
     "notes": "Objectives for Lecture 03."},

    {"kind": "table_pie", "title": "Three access types, different risks",
     "source": "Blake PG, et al. Kidney Int. 2012;82(6):623-625 · Lok CE, et al. KDOQI Vascular Access 2019 · DOPPS Practice Monitor, Nov 2015",
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
             "note": "Adapted in AREP from the DOPPS Practice Monitor (Nov 2015); population as reported in the module. Shares vary by country."},
     "notes": """
AREP [Dialysis / 144615, 142509; vascular access / 151232] (Blake PG, et al. Kidney Int 2012; Rivara MB, et al. CJASN 2016).
Pie values from AREP: AVF 66.5%, AVG 18.4%, catheter 15.1% (DOPPS Nov 2015). Population not stated in the module (likely US) – NEEDS REVIEW; replace with local registry data where available.
[WEB] KDOQI 2019: access choice follows an individual "ESKD Life-Plan" rather than a single "Fistula First" rule (https://homedialysis.org/news-and-research/blog/340-the-eskd-life-plan-a-new-concept-in-the-nkf-vascular-access-guideline-update, """ + ACCESSED + """)."""},

    {"kind": "rule6", "title": "Before every cannulation: look, listen, feel",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164 · AREP Vascular Access",
     "lead": "A new AVF is usually ready when it meets the rule of 6s:",
     "sixes": [("6 wk", "after creation"), ("600", "mL/min access flow"), ("< 0.6 cm", "deep below the skin"), ("≥ 0.6 cm", "vessel diameter")],
     "left": {"head": "Look and feel", "body": [
         "Swelling, redness, aneurysm, skin shine", "Thrill strongest at anastomosis", "Pulse soft; partial collapse on arm elevation"]},
     "right": {"head": "Listen and act", "body": [
         "Low-pitched continuous bruit = normal", "High-pitched or pulsatile = possible stenosis", "No thrill or bruit: do not cannulate, notify"]},
     "notes": """
KDOQI 2019 physical examination steps (AREP [vascular access / 153406, 153427]): Look – well-developed outflow, no aneurysm; vessel partially collapses when arm elevated. Listen – low-pitched continuous systolic and diastolic bruit. Feel – thrill at arterial anastomosis and along outflow, easy to compress.
Physical exam detects stenosis with PPV 70–80% in AVGs and 93% in AVFs (as reported by AREP).
Rule of 6s per KDOQI; 25–50% of AVFs never mature (AREP [151710])."""},

    {"kind": "image_cards", "title": "Choose the cannulation technique",
     "source": "Schmidli J, et al. Eur J Vasc Endovasc Surg. 2018;55(6):757-818 · Lok CE, et al. KDOQI 2019 · Muir CA, et al. Clin J Am Soc Nephrol. 2014;9(1):110-119",
     "image": "rope_ladder.png", "image_alt": "Rope-ladder cannulation sites on forearm AVF (AREP)",
     "caption": "Rope ladder: new sites each session, ≥ 3 cm from the anastomosis and ≥ 5 cm between needle tips. Illustration: FMC AREP (uploaded screenshot).",
     "cards": [
         ("Rope ladder: preferred", ["Rotate along the whole AVF or graft", "Lower aneurysm and infection risk", "Venous needle in direction of flow"], "blue"),
         ("Buttonhole: AVF only, selected cases", ["Same site, angle and depth each time", "Higher infection risk: strict asepsis", "Remove scabs aseptically per protocol"], "mid"),
         ("Area technique: avoid", ["Repeated punctures in one area", "Aneurysm, thin skin, bleeding"], "grey"),
     ],
     "notes": """
AREP [vascular access / 151841–152452]. Rope ladder preferred; buttonhole only for AVFs (not AVGs), limited to special circumstances because of higher infection risk (Muir CA, et al. CJASN 2014; O'Brien FJ, et al. Clin Kidney J 2012); area technique no longer recommended.
Buttonhole: tunnel track after about 6–10 sessions; single cannulator until established; blunt needles afterwards. Scab removal technique per local protocol."""},

    {"kind": "steps", "title": "AVF/AVG cannulation step by step",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019 · AREP Vascular Access · NKF Clinical Update 2016",
     "steps": [
         ("Prepare", "Hand hygiene, clean gloves; patient washed access arm with soap and water"),
         ("Assess and plan", "Look, listen, feel; choose sites, direction and needle gauge for Qb"),
         ("Skin antisepsis", "2% CHG/70% alcohol: 30 s back-and-forth scrub, let dry; or povidone-iodine 2–3 min"),
         ("Insert", "No-touch technique; angle by access depth; flashback; secure with tape"),
         ("Check", "Flush/aspirate, check arterial pressure; no swelling or pain"),
         ("Keep visible", "Access and needles uncovered throughout treatment"),
     ],
     "side": {"head": "Needle gauge for blood flow", "fill": "sand", "body": [
         ("< 300 mL/min: 17 G", {"size": 14, "space_after": 6}),
         ("300–350 mL/min: 16 G", {"size": 14, "space_after": 6}),
         ("> 350–450 mL/min: 15 G", {"size": 14, "space_after": 6}),
         ("> 450 mL/min: 14 G", {"size": 14, "space_after": 12}),
         "Smallest needles for new AVFs", "Max. 2 attempts, then call an expert"]},
     "notes": """
KDOQI 2019 skin preparation (AREP [vascular access / 153505]): locate, inspect and palpate; wash with antibacterial soap/scrub and water; cleanse with 2% chlorhexidine gluconate/70% isopropyl alcohol and/or 10% povidone-iodine per manufacturer. CHG-alcohol: 30-second back-and-forth friction scrub, allow to dry, do not blow; povidone-iodine needs 2–3 minutes contact. Clean gloves, changed if contaminated.
Needle gauge table: NKF Clinical Update 2016 as shown in AREP [153559] (minimum gauge for stated BFR).
Max 2 attempts before seeking an expert (Schmidli 2018, AREP [153931]). Insertion angle depends on access depth and type – follow local cannulation policy."""},

    {"kind": "two_cards", "title": "Needle removal and hemostasis",
     "source": "AREP Vascular Access · Lok CE, et al. KDOQI 2019 · ANNA Core Curriculum 2015",
     "h": 3.75,
     "cards": [
         ("Do", ["Remove tape carefully; withdraw at insertion angle", "Apply gauze only once needle is out",
                 "Gentle pressure: no thrill loss under the finger", "One site at a time; check bleeding has stopped", "Dispose of sharps immediately"]),
         ("Report", ["Bleeding much longer than usual for this patient", "New hematoma or infiltration",
                     "Loss of thrill or bruit after pressure", "Pain, coldness or numbness of the hand", "Signs of infection at needle sites"]),
     ],
     "banner": "Prolonged bleeding can mean outflow stenosis or too much anticoagulation: report it",
     "notes": """
Hemostasis principles (ANNA Core Curriculum; AREP mechanical trauma [vascular access / 153731, 153758]): needle insertion and removal cause mechanical trauma; using the same angle for insertion and removal prevents vessel wall damage (AREP Clinical Pearls [154022]).
Occlusive pressure that stops flow can promote thrombosis – thrill should remain palpable.
Prolonged bleeding may indicate venous outflow stenosis (KDOQI 2019) or excess anticoagulation – report.
Hand pain/coldness/numbness: possible steal syndrome (1–20% of AV accesses, AREP)."""},

    {"kind": "steps", "title": "CVC connection and disconnection safety",
     "source": "CDC Core Interventions for Dialysis BSI Prevention · CDC MMWR 2001;50(RR-5) · Lok CE, et al. KDOQI 2019",
     "steps": [
         ("Prepare", "Hand hygiene; mask for staff and patient (or face turned away) per policy; clean gloves"),
         ("Exit site", "Inspect; change dressing per protocol with CHG-alcohol skin antisepsis"),
         ("Hub scrub", "Remove cap; scrub hub with antiseptic every time it is opened; let dry"),
         ("Aspirate lock", "Withdraw and discard the lock solution volume per protocol; check flow"),
         ("Connect / disconnect", "Aseptic non-touch; clamps closed before opening; no open lumen to air"),
         ("Lock and secure", "Lock solution as prescribed; new sterile caps; secure lines"),
     ],
     "side": {"head": "Never", "fill": "navy", "body": [
         "Use the HD catheter for other infusions unless ordered", "Leave a lumen open or unclamped",
         "Force a blocked catheter", "Touch the hub after scrubbing", "Ignore fever or exit-site pus"]},
     "notes": """
[WEB] CDC Core Interventions include: chlorhexidine (> 0.5% CHG with alcohol) for skin antisepsis at catheter exit site; scrub catheter hubs with an appropriate antiseptic after the cap is removed and before accessing, every time the catheter is accessed or disconnected; antimicrobial ointment at the exit site per protocol; catheter/vascular access care observations; staff competency; patient education; catheter reduction. Sources: CDC clinical safety page (cdc.gov/dialysis-safety/hcp/clinical-safety) and summaries (https://pmc.ncbi.nlm.nih.gov/articles/PMC5332080/table/table5-2054358116669129), """ + ACCESSED + """. Note: cdc.gov could not be opened from this build environment; wording verified via search summaries – NEEDS REVIEW against the current CDC page.
Air embolism risk: CVC lumens must never be open to air (Lecture 07). Lock solution and volume per prescription and catheter labelling."""},

    {"kind": "six_grid", "title": "Complications to recognise early",
     "source": "AREP Vascular Access (Al-Jaishi AA 2016; Daugirdas 2014; Mudoni A 2015; Axley B 2012; Lee T)",
     "items": [
         ("Thrombosis", "80–85%", "of access loss. Clue: no thrill or bruit, clots on aspiration."),
         ("Infection", "10% vs 1%", "AVG vs AVF. Clue: redness, pus, fever. Mostly staphylococci."),
         ("Aneurysm", "5% to > 60%", "reported incidence. Avoid area puncture; report thin, shiny skin."),
         ("Steal syndrome", "1–20%", "of AV accesses. Clue: cold, painful, numb hand."),
         ("Needle dislodgement", "400–500 mL/min", "typical Qb: blood loss can be life-threatening in minutes."),
         ("Infiltration", "6.8% / year", "Swelling, pain at needle. Stop, ice, pressure; reassess."),
     ],
     "notes": """
Figures as reported in AREP [vascular access / 152344–152609, 153817] with their citations (Al-Jaishi AA, et al. JASN 2016; Daugirdas 2014; Schild AF 2008; USRDS 2019; Jankovic A 2013; Mudoni A 2015; Axley B 2012; Sandroni S 2008; Lee T, et al.).
Populations and definitions differ between studies; use as orders of magnitude."""},

    {"kind": "case", "title": "Case: a quiet fistula",
     "source": "Fictional teaching case",
     "case": [
         "Ms D, 55 years, left upper-arm AVF, cannulated with rope ladder.",
         "Last session: needle sites bled for 35 minutes (usually 10).",
         "Today: thrill weak, bruit high-pitched near the upper arm. Arm slightly swollen.",
         "Prescribed Qb 400 mL/min; the nurse plans to use 17 G needles."],
     "questions": [
         "What do the findings suggest?",
         "Would you cannulate? What do you do first?",
         "Is the needle gauge appropriate for the prescribed Qb?",
         "What should be documented and reported?"],
     "notes": """
Suggested answers (educational):
1. Prolonged bleeding + high-pitched bruit + swelling → possible venous outflow stenosis.
2. Notify physician/access team before cannulation; cannulate only if instructed; consider expert cannulator; possibly ultrasound.
3. No – 400 mL/min needs at least 15 G per the NKF table (> 350–450 mL/min: 15 G); 17 G is for < 300 mL/min.
4. Exam findings, bleeding time, Qb achieved and pressures, who was notified and orders; referral for imaging per protocol."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 03 summary",
     "items": [
         ("Examine before every cannulation", "Look, listen, feel; no thrill or bruit means do not cannulate."),
         ("Rope ladder is the default", "Buttonhole for AVFs only, in selected cases with strict asepsis."),
         ("Match needle to blood flow", "Smallest needles for new AVFs; max. two attempts."),
         ("Treat every CVC as a high infection risk", "Mask, hub scrub, aseptic non-touch, never open to air."),
         ("Report early warning signs", "Prolonged bleeding, weak thrill, pain or coldness of the hand."),
     ],
     "notes": "Summarise and link to Lecture 04 (infection prevention)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["kdoqi_va"], R["cdc_core"], R["cdc_2001"], "Schmidli J, et al. Eur J Vasc Endovasc Surg. 2018;55(6):757-818.",
              "Blake PG, et al. Kidney Int. 2012;82(6):623-625.", "Muir CA, et al. Clin J Am Soc Nephrol. 2014;9(1):110-119.",
              "Chan MR, et al. Semin Dial. 2014;27(2):210-216.", "National Kidney Foundation. Clinical Update: needle gauge and blood flow. 2016.",
              "Al-Jaishi AA, et al. J Am Soc Nephrol. 2016.", R["anna"], R["arep"]],
     "notes": "References for Lecture 03."},
]
