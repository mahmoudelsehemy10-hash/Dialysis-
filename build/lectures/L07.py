# -*- coding: utf-8 -*-
"""Lecture 07 - Day 4: Recognition and Immediate Management of Hemodialysis Emergencies."""
from lectures._common import *  # noqa: F401,F403

SLUG = "HD_Emergencies"
TITLE = "Recognition and Immediate Management of Hemodialysis Emergencies"
SUBTITLE = "Day 4 · Emergencies & Quality Improvement · Lecture 07"
FOOTER_TEXT = "L07 Hemodialysis emergencies"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 07 of the Hemodialysis Nursing Programme (Day 4). 45–60 minutes; ideally followed by a simulation drill.
Main references: Saha & Allon, CJASN 2017 (Diagnosis, treatment, and prevention of hemodialysis emergencies) and Greenberg & Choi, AJKD Core Curriculum 2021. The full texts could not be opened from the build environment; steps reflect standard practice described in these reviews and the Handbook of Dialysis and must be aligned with the local emergency protocol and machine IFU.
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 07",
     "items": [
         ("Recognise", ["Early signs of each emergency", "Machine alarms vs patient signs"]),
         ("Act", ["First actions in the first minute", "When not to return blood"]),
         ("Call", ["Who to call and when", "Use the emergency kit"]),
         ("Prevent", ["Link emergencies to checks", "Debrief and report"]),
     ],
     "notes": "Objectives for Lecture 07."},

    {"kind": "six_grid", "title": "Emergencies to recognise in the dialysis unit",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · Greenberg KI, Choi MJ. Am J Kidney Dis. 2021;77(5):796-809",
     "items": [
         ("Blood loss", "VND, disconnection", "Life-threatening within minutes at Qb 400–500 mL/min."),
         ("Air embolism", "Rare, severe", "Sudden dyspnea, chest pain, cough, neurological signs."),
         ("Hemolysis", "Water or dialysate", "Dark venous blood, back/chest pain; hyperkalemia risk."),
         ("Dialyzer reaction", "Type A or B", "Early anaphylaxis (A) or milder chest/back pain (B)."),
         ("Cardiac", "Arrhythmia, arrest", "Potassium and calcium shifts, ischemia, hypotension."),
         ("Neurological", "Seizure, disequilibrium", "Headache, confusion, seizures; first sessions, high urea."),
     ],
     "notes": """
Overview per Saha & Allon 2017 and Greenberg & Choi 2021. Saha & Allon note that most HD emergencies can be attributed to human error and that serious complications are uncommon thanks to modern machines and water treatment – prevention is mostly about checks (Lectures 01, 03, 06).
VND blood flow figure from AREP [vascular access / 152609] (Axley B 2012; Sandroni S 2008; Garrick R 2012)."""},

    {"kind": "steps", "title": "Bleeding and venous needle dislodgement",
     "source": "AREP Vascular Access (Axley B 2012; Sandroni S 2008) · Saha M, Allon M. 2017 · Local protocol",
     "steps": [
         ("Stop the blood pump", "Clamp the blood lines and needle tubing"),
         ("Apply pressure", "Direct pressure on the bleeding site with gauze"),
         ("Call for help", "Stay with the patient; activate emergency response if unstable"),
         ("Assess", "BP, pulse, consciousness; estimate blood loss"),
         ("Restore safely", "New needle / site by experienced nurse; volume per order"),
         ("Report", "Incident report; review taping, visibility and alarms"),
     ],
     "side": {"head": "Key point", "fill": "navy", "body": [
         "The venous pressure alarm may NOT trigger when a venous needle dislodges",
         "Keep the access and lines visible at all times",
         "Secure taping; use blood-leak or wetness detectors if available",
         "Higher risk: agitation, cognitive impairment, cramps, hypotension"]},
     "notes": """
VND: venous needle slips out of the access, resulting in blood loss; life-threatening at Qb 400–500 mL/min (AREP [152609]). Associated factors: agitation/cognitive impairment, dialysis outside the unit, inadequate taping, hypotension or cramps.
Venous pressure monitoring is not reliable for detecting VND because pressure may change only slightly when the needle is out (widely described in VND safety literature, e.g. Axley B, et al. Nephrol Nurs J 2012) – mitigation: secure taping, visible access, monitoring, wetness detectors (Hawley CM 2008; AREP [152716]).
Steps align with local emergency protocol; volume replacement per physician order."""},

    {"kind": "steps", "title": "Air embolism",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · Handbook of Dialysis 2015 · Machine IFU",
     "steps": [
         ("Clamp and stop", "Clamp the venous line and stop the blood pump immediately"),
         ("Do not return blood", "The circuit may contain air"),
         ("Position", "Left side, head down (per protocol) to trap air in the right heart"),
         ("Oxygen and help", "100% oxygen; call emergency team; monitor airway and rhythm"),
         ("Escalate", "Physician may consider aspiration (CVC) or hyperbaric oxygen"),
     ],
     "side": {"head": "How air gets in", "fill": "sand", "body": [
         "Incomplete priming of lines or dialyzer", "Loose or broken connection before the pump",
         "Open CVC lumen during connection or removal", "Air detector bypassed or not armed",
         ("Never bypass the air detector", {"bold": True, "color": NAVY, "space_after": 4})]},
     "notes": """
[WEB] Saha & Allon 2017: venous air embolism is rare but signs mimic common complications; air can enter via residual air after incomplete priming or a broken/loose luer connection before the pump. Acute management in emergency teaching material: 100% oxygen, aspiration of air if a catheter is in place, blood pump management; positioning matters. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC5293333 (summary via search); Koh T. "Hemodialysis emergencies" slide deck (""" + ACCESSED + """).
The left lateral head-down (Durant) position and venous line clamping are standard textbook teaching (Handbook of Dialysis) but could NOT be verified in the reviews accessed in this session – NEEDS REVIEW against local emergency protocol."""},

    {"kind": "steps", "title": "Hemolysis",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · Greenberg KI, Choi MJ. Am J Kidney Dis. 2021",
     "steps": [
         ("Recognise", "Port-wine / dark venous blood, chest or back pain, dyspnea, hypotension"),
         ("Stop and clamp", "Stop the blood pump; clamp lines; do NOT return the blood"),
         ("Treat", "O₂, vital signs, ECG; urgent potassium and Hb per order"),
         ("Check the source", "Water (chloramine, copper), concentrate, temperature, kinked lines"),
         ("Other patients", "Check all patients on the same water or concentrate"),
         ("Preserve and report", "Keep lines, dialyzer and samples; incident report"),
     ],
     "side": {"head": "Why not return blood?", "fill": "navy", "body": [
         "Hemolysed red cells release potassium", "Returning them can cause life-threatening hyperkalemia",
         "Hemolysis may also come from overheated or hypotonic dialysate"]},
     "notes": """
Hemolysis during HD: causes include chloramines, nitrates, copper in water, overheated (> ~46 °C) or hypotonic dialysate, and mechanical causes (kinked lines, pump malocclusion, needle problems) (Saha & Allon 2017; Greenberg & Choi 2021; FPnotebook summary https://fpnotebook.com/Renal/ER/EmrgncyCrInEsrd.htm, """ + ACCESSED + """).
"Do not return blood" because of hyperkalemia risk is standard teaching (Handbook of Dialysis) – confirm in local protocol."""},

    {"kind": "two_cards", "title": "Dialyzer reactions: type A vs type B",
     "source": "Saha M, Allon M. Clin J Am Soc Nephrol. 2017;12(2):357-369 · Handbook of Dialysis. 5th ed. 2015",
     "h": 3.75,
     "cards": [
         ("Type A (anaphylactic): emergency", ["Starts within minutes of starting HD", "Dyspnea, urticaria, angioedema, hypotension",
                                               "Stop HD, clamp, do NOT return blood", "Anaphylaxis treatment per order (e.g. epinephrine)",
                                               "Report; future: different dialyzer or rinsing"]),
         ("Type B (non-specific): usually mild", ["Within the first hour", "Chest or back pain, often mild",
                                                   "Supportive care; HD usually continues", "Rule out cardiac ischemia and hemolysis",
                                                   "Report to physician"]),
     ],
     "banner": "Any reaction with airway, breathing or circulation problems: treat as anaphylaxis and call for help",
     "notes": """
Classification of dialyzer reactions into type A (anaphylactic, early, severe) and type B (non-specific, milder chest/back pain, during the first hour) is standard (Handbook of Dialysis 2015; covered in Saha & Allon 2017). The reviews could not be opened from the build environment; type A/B details from textbook knowledge – NEEDS REVIEW against local anaphylaxis protocol.
Medication doses and routes per physician order and local anaphylaxis algorithm."""},

    {"kind": "steps", "title": "Hyperkalemia, arrhythmia and cardiac arrest",
     "source": "Saha M, Allon M. 2017 · Resuscitation guidelines (local / ERC / AHA) · Machine IFU",
     "steps": [
         ("Recognise", "Palpitations, weakness, slow or irregular pulse, collapse; ECG changes"),
         ("Call", "Emergency team / cardiac arrest call; bring defibrillator"),
         ("Stop UF and pump", "Follow local protocol to return blood (if quick and safe) or disconnect"),
         ("Resuscitate", "BLS/ALS per guidelines; patient flat on a firm surface"),
         ("Check causes", "Potassium, calcium, dialysate bath, hypoxia, bleeding, air"),
         ("Debrief", "Document times and actions; review dialysate and prescription"),
     ],
     "side": {"head": "Prevent", "fill": "sand", "body": [
         "Match dialysate K to serum K (Lecture 01)", "Verify concentrate before every treatment",
         "Monitor high-risk patients", "Emergency drills every year"]},
     "notes": """
Hyperkalemia and arrhythmia are among the most important HD emergencies (Saha & Allon 2017). Cardiac arrest management follows current resuscitation guidelines (AHA/ERC or national); whether to return blood or disconnect depends on the local protocol and machine design – the defibrillation procedure with the patient connected must follow the machine IFU.
Wrong dialysate potassium or calcium bath is a preventable cause (Lecture 01, 06)."""},

    {"kind": "matrix", "title": "Other urgent situations",
     "source": "Saha M, Allon M. 2017 · Greenberg KI, Choi MJ. 2021 · Kooman J, et al. EBPG 2007",
     "rows": [
         ("Severe hypotension", "BP falls, reduced consciousness", "Stop UF, flat/legs up, saline per order, call physician (Lecture 02)"),
         ("Chest pain", "New or typical cardiac pain", "Stop UF, O₂, ECG, physician now; consider hemolysis or air"),
         ("Seizure", "Convulsion during HD", "Stop pump, protect airway, side position, check glucose, call help"),
         ("Disequilibrium", "Headache, nausea, confusion in first sessions", "Slow or stop per order; prevent with short, gentle first sessions"),
         ("Hypoglycemia", "Sweating, confusion in diabetic patient", "Check glucose; treat per protocol; review insulin timing"),
     ],
     "fills": ["blue", "navy", "navy", "mid", "grey"],
     "notes": """
Brief management summaries based on Saha & Allon 2017, Greenberg & Choi 2021 and EBPG 2007 (hypotension). Dialysis disequilibrium syndrome occurs mainly in new patients with high urea; prevention is gentle initial dialysis (lower dose/shorter sessions) per physician order.
All actions per local emergency protocol."""},

    {"kind": "case", "title": "Case: ten minutes after starting",
     "source": "Fictional teaching case",
     "case": [
         "Mrs J, new to HD (session 2), new dialyzer type started today.",
         "Ten minutes after starting she says her throat is tight, has urticaria and wheezing.",
         "BP 78/40 (pre 150/85), SpO₂ 89%.",
         "Venous blood looks normal; no alarms."],
     "questions": [
         "What is the most likely emergency?",
         "What are your first three actions?",
         "Do you return the blood? Why?",
         "What must happen before her next session?"],
     "notes": """
Suggested answers (educational):
1. Type A (anaphylactic) dialyzer reaction – early, with airway and circulation involvement.
2. Stop blood pump and HD, clamp lines; call emergency help/physician; airway, O₂, lay flat, anaphylaxis treatment per order.
3. No – do not return the blood (may contain the allergen/trigger), per type A management.
4. Report; physician decides on different dialyzer/sterilisation method, pre-rinsing; document allergy prominently."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 07 summary",
     "items": [
         ("Stop the pump, clamp, call", "The first minute matters in every HD emergency."),
         ("Know when not to return blood", "Hemolysis, air in the circuit, type A reaction."),
         ("Alarms do not see everything", "Keep access visible; the venous alarm may miss dislodgement."),
         ("Think of the source", "Water, concentrate, temperature and potassium bath."),
         ("Prevent and practise", "Most emergencies relate to errors: checks, drills, debriefs."),
     ],
     "notes": "Summarise and link to Lecture 08 (quality indicators, documentation and reporting). Suggest an emergency simulation drill."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["saha"], R["greenberg"], R["handbook"], R["ebpg_hd"], "Axley B, et al. Nephrol Nurs J. 2012;39(6):435-445.",
              "Hawley CM, et al. Hemodial Int. 2008;12 Suppl 1:S21-5.", "Current resuscitation guidelines (AHA / ERC or national equivalent).",
              R["arep"], R["ifu"]],
     "notes": "References for Lecture 07."},
]
