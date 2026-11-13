# -*- coding: utf-8 -*-
"""Day 4 · Lecture 07: Recognition and Immediate Management of Hemodialysis Emergencies."""
from program._common import *  # noqa: F401,F403

TITLE = "Recognition and Immediate Management of Hemodialysis Emergencies"
SUBTITLE = "Day 4 · Emergencies & Quality Improvement · Lecture 07"
FOOTER_TEXT = "Day 4 · Lecture 07"
REFS = ["SAHA17", "GREENBERG21", "HEMOLYSIS14", "DDS19", "PYRO_OTT", "AIR_SUMMARY", "KDOQI_CV05", "EBPG_HI07",
        "AREP_VA", "HANDBOOK", "FMC_IFU"]

SLIDES = [
    {"kind": "title", "notes": """
Day 4, Lecture 07 (30–40 min; ideally followed by a simulation drill).
Circuit actions differ by emergency: stopping the blood pump, clamping lines and whether blood in the extracorporeal circuit is returned are NOT the same for every emergency. Verified points: hemolysis – circuit blood should be discarded, not returned (BMC Res Notes 2014); pyrogenic reaction – stop dialysis, do not return blood (Ottawa guideline/secondary). Air embolism positioning advice conflicts between sources (left lateral head-down vs modified Trendelenburg) – noted on the slide. Type A dialyzer reaction 'do not return blood' is textbook teaching not verified online in this session. Medication use is limited to protocols and physician orders; device actions follow the FMC machine IFU (not uploaded).
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Lecture 07 objectives",
     "items": [
         ("Recognise", ["Name warning signs of 8 HD emergencies"]),
         ("Act", ["State the first nursing priorities and the correct circuit action"]),
         ("Avoid", ["Identify when blood must NOT be returned"]),
         ("Escalate", ["Call for help and communicate with SBAR; document"]),
     ],
     "notes": "Assessed in two scenarios (slides 17–18) and the knowledge check (slide 19)."},

    {"kind": "opening", "title": "Opening question: alarm or patient?",
     "source": "Discussion question",
     "story": ["The machine is quiet. No alarm. But your patient suddenly coughs, grabs his chest and turns grey.",
               "What do you do in the next 60 seconds?"],
     "prompts": ["Which emergencies give no alarm?", "What is the first thing you touch: patient or machine?", "Who do you call, and how?"],
     "notes": "Machines do not detect every emergency: a 2026 case report of air embolism with no air-detector, venous-pressure or blood-leak alarm illustrates this (BMC Nephrology 2026, via search). Most HD emergencies are linked to human error (Saha & Allon 2017 – secondary)."},

    {"kind": "pathway", "title": "A structured approach to every emergency",
     "source": "Saha M, Allon M. 2017 · Greenberg KI, Choi MJ. 2021 · local emergency policy",
     "nodes": [("1 Recognise", "signs, alarms, trend"), ("2 Secure circuit", "action depends on cause"), ("3 ABC", "airway, breathing, circulation, O₂"),
               ("4 Call", "help, physician, code team"), ("5 Treat", "per protocol and orders"), ("6 Document", "times, actions, SBAR")],
     "cards": [("Stay with the patient", ["Send someone else for help", "Use the emergency bell"]),
               ("Circuit action is specific", ["Pump stop, clamp, return or not", "See next slide"]),
               ("Scope", ["Medicines only per protocol/order", "Device steps per machine IFU"])],
     "notes": "Visual 1 (workflow). The 'secure circuit' step depends on the emergency (next slide). Team roles and code activation per local emergency policy."},

    {"kind": "table_only", "title": "Circuit actions differ by emergency",
     "source": "BMC Res Notes 2014 (hemolysis) · Ottawa pyrogenic guideline · Saha & Allon 2017 · machine IFU",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.75, 2.0, 2.0, 5.3], "row_h": 0.5, "size": 12,
               "rows": [["Emergency", "Blood pump", "Clamp lines", "Return circuit blood?"],
                        ["Severe hypotension", "Usually continue", "No", "Not routinely; end/return per order if needed"],
                        ["Air embolism", "Stop", "Yes (venous)", "NO: circuit may contain air"],
                        ["Hemolysis", "Stop", "Yes", "NO: discard (hyperkalemia risk)"],
                        ["Type A dialyzer reaction", "Stop", "Yes", "NO per textbook teaching (verify locally)"],
                        ["Needle dislodgement / bleeding", "Stop", "Yes", "Only after safe access and per protocol"],
                        ["Pyrogenic reaction", "Stop", "Yes", "NO; keep supplies; cultures"],
                        ["Cardiac arrest", "Stop", "Yes", "Per local protocol and IFU (no single rule)"],
                        ["Disequilibrium", "Slow/stop per order", "Per order", "Not contraindicated by the condition itself"]]},
     "notes": """
Visual 2 (comparison table). Verified: hemolysis – circuit blood discarded rather than reinfused (BMC Res Notes 2014;7:475, web-verified); pyrogenic reaction – discontinue dialysis, do not return blood, cultures, sequester supplies (Ottawa guideline / study guide, secondary). Air embolism – clamp venous line and stop pump; do not return blood (study guides/secondary, consistent with Saha & Allon). Type A reaction – textbook teaching (Handbook of Dialysis), NOT verified online. Hypotension – UF is stopped; blood pump usually continues (EBPG; local protocol). Cardiac arrest and bleeding – no universal rule: local protocol and FMC machine IFU.
All rows: NEEDS REVIEW against the local emergency protocol and machine IFU before teaching."""},

    {"kind": "emergency", "title": "Severe hypotension",
     "source": "KDOQI CVD 2005 (definition) · Kooman J, et al. EBPG 2007 · local standing orders",
     "circuit": "stop UF; blood pump usually continues; return blood only if ending treatment per order", "circuit_level": "continue",
     "signs": ["SBP falling fast, nadir < 90 mmHg", "Dizziness, yawning, nausea, cramps", "Pallor, sweating, confusion", "Reduced consciousness"],
     "priorities": ["Lay flat, legs raised; airway", "Stop UF", "Saline bolus per standing order; O₂ if hypoxic", "Recheck BP every few minutes"],
     "avoid": ["Restarting full UF early", "Leaving the patient", "Missing chest pain, sepsis, bleeding"],
     "escalate": ["No response within minutes", "Chest pain, arrhythmia, low consciousness", "Physician now; code if unresponsive"],
     "notes": "Detail in Lecture 02. Definition per KDOQI 2005 (via Clin Kidney J 2020 review). Management steps are standard practice (EBPG 2007, not accessed online) – NEEDS REVIEW against local IDH protocol."},

    {"kind": "emergency", "title": "Suspected air embolism",
     "source": "Saha M, Allon M. 2017 · hemodialysis emergency guides (conflicting positioning advice) · machine IFU",
     "circuit": "clamp venous line, stop blood pump; do NOT return blood", "circuit_level": "stop",
     "signs": ["Sudden dyspnea, cough, chest tightness", "Cyanosis, hypotension, arrhythmia", "Confusion, seizure, loss of consciousness", "Foam/air in venous line; may be NO alarm"],
     "priorities": ["Clamp venous line, stop pump", "Position per protocol (often left side, head down)", "100% oxygen; call emergency team", "Monitor airway, rhythm, BP"],
     "avoid": ["Returning blood from the circuit", "Sitting the patient up", "Bypassing or disarming the air detector"],
     "escalate": ["Immediately: code/emergency team", "Physician: aspiration via CVC, hyperbaric O₂", "Incident report; keep the circuit"],
     "notes": """
[WEB] Saha & Allon 2017: air may enter via incomplete priming or a broken/loose connection before the pump; signs mimic common complications. Study guides: clamp venous line and stop pump first; 100% oxygen; positioning – most sources left lateral decubitus with head-down tilt; one recommends modified Trendelenburg (head flat, legs up) and warns against head-down in severe respiratory distress. SOURCES CONFLICT on positioning – follow the local emergency protocol. Small volumes (20–50 mL) can cause severe morbidity (study guide). A 2026 BMC Nephrology case report: no machine alarm triggered (""" + ACCESSED + """)."""},

    {"kind": "emergency", "title": "Suspected hemolysis",
     "source": "BMC Res Notes 2014;7:475 · Saha M, Allon M. 2017 · Greenberg KI, Choi MJ. 2021",
     "circuit": "stop blood pump, clamp lines; do NOT return blood (discard circuit blood)", "circuit_level": "stop",
     "signs": ["Dark, port-wine blood in venous line", "Back or chest pain, dyspnea", "Nausea, abdominal pain, hypotension", "Several patients affected: think water"],
     "priorities": ["Stop pump, clamp, do not reinfuse", "O₂, vital signs, ECG monitoring", "Urgent potassium and Hb per order", "Check other patients on same water/concentrate"],
     "avoid": ["Returning the blood (hyperkalemia)", "Restarting before the cause is found", "Discarding lines and samples"],
     "escalate": ["Physician now", "Medical director and technician (water, temperature, concentrate)", "Incident report; keep evidence"],
     "notes": "[WEB] BMC Res Notes 2014 review: causes include overheating (> 42 °C associated with hemolysis), hypotonic dialysate, chloramine and other water contaminants, kinked or narrowed blood lines; circuit blood should be discarded rather than reinfused. Hyperkalemia risk from lysed red cells is standard physiology. (" + ACCESSED + ")"},

    {"kind": "emergency", "title": "Dialyzer or hypersensitivity reaction",
     "source": "Handbook of Dialysis 2015 · Saha M, Allon M. 2017 · local anaphylaxis protocol",
     "circuit": "type A: stop pump, clamp, do NOT return blood · type B: usually continue with monitoring", "circuit_level": "protocol",
     "signs": ["Type A: minutes after start; dyspnea, urticaria, angioedema, hypotension", "Type B: within first hour; chest or back pain, milder", "Itching, flushing, wheeze"],
     "priorities": ["Type A: stop, clamp; airway, O₂; lay flat", "Anaphylaxis treatment per protocol/order", "Type B: supportive care; rule out ischemia and hemolysis"],
     "avoid": ["Returning blood in a type A reaction", "Giving medicines outside protocol/scope", "Re-using the same dialyzer type without review"],
     "escalate": ["Type A: emergency team and physician now", "Type B: inform physician", "Record allergy; incident report"],
     "notes": "Type A/B classification and management are standard textbook teaching (Handbook of Dialysis 2015; covered in Saha & Allon 2017) but were NOT verified online in this session – NEEDS REVIEW against the local anaphylaxis algorithm. Medicines (e.g. epinephrine) only per protocol and nurse's authorised scope."},

    {"kind": "emergency", "title": "Major blood loss, needle dislodgement, access bleeding",
     "source": "AREP Vascular Access (Axley B 2012; Sandroni S 2008) · Saha M, Allon M. 2017",
     "circuit": "stop blood pump, clamp lines; return blood only after safe access and per protocol", "circuit_level": "stop",
     "signs": ["Blood on bed, floor or dressing", "Needle out or line disconnected", "Falling BP, rising pulse, pallor", "Venous pressure alarm may NOT trigger"],
     "priorities": ["Stop pump, clamp, direct pressure", "Call for help; stay with patient", "Assess BP, pulse, consciousness; estimate loss", "Lay flat; IV access/volume per order"],
     "avoid": ["Relying on alarms", "Covering the access with blankets", "Re-inserting a contaminated needle"],
     "escalate": ["Physician now if unstable or large loss", "Code team if collapse", "Incident report; review taping and visibility"],
     "notes": "AREP [vascular access / 152609, 152716]: VND life-threatening at typical Qb 400–500 mL/min; factors: agitation, cognitive impairment, poor taping, hypotension/cramps; mitigation: secure taping, visible access, monitoring, wetness detectors. Venous pressure monitoring may not detect VND (standard safety teaching)."},

    {"kind": "emergency", "title": "Chest pain, arrhythmias and cardiac arrest",
     "source": "Saha M, Allon M. 2017 · current resuscitation guidelines (local/ERC/AHA) · machine IFU",
     "circuit": "chest pain/arrhythmia: stop UF · arrest: stop pump, clamp; return or disconnect per local protocol and IFU", "circuit_level": "protocol",
     "signs": ["New chest pain, palpitations", "Irregular, very slow or fast pulse", "Collapse, no pulse, no breathing", "Risk: low/high K⁺, wrong K bath, ischemia"],
     "priorities": ["Stop UF; O₂; ECG per protocol", "Arrest: call code, start CPR, defibrillator", "Patient flat on firm surface", "Check potassium, dialysate bath, air, bleeding"],
     "avoid": ["Delaying CPR to finish the treatment", "Assuming the cause is cardiac only", "Unclear team roles"],
     "escalate": ["Physician immediately", "Code team for arrest", "Debrief and incident report"],
     "notes": "Hyperkalemia and arrhythmias are key HD emergencies (Saha & Allon 2017 – secondary). Resuscitation per current guidelines; whether to return blood or disconnect, and defibrillation with the patient connected, follow the local protocol and FMC machine IFU (not uploaded) – NEEDS LOCAL CONFIRMATION."},

    {"kind": "emergency", "title": "Dialysis disequilibrium syndrome (DDS)",
     "source": "Mistry K. Int J Nephrol Renovasc Dis. 2019;12:69-77 · StatPearls (DDS)",
     "circuit": "slow or stop dialysis per physician order; blood return not contraindicated by DDS itself", "circuit_level": "protocol",
     "signs": ["New patient, very high urea, first sessions", "Headache, nausea, vomiting, restlessness", "Confusion, muscle cramps, asterixis", "Seizures, coma (severe)"],
     "priorities": ["Notify physician; slow/stop per order", "Safety: protect airway, side position if seizing", "Check glucose, BP, neuro status", "Supportive care per order"],
     "avoid": ["Aggressive first sessions without an order", "Attributing confusion to DDS without checking glucose/BP", "Leaving the patient alone"],
     "escalate": ["Seizure or reduced consciousness: emergency team", "Physician for all suspected DDS", "Document neuro observations"],
     "notes": "[WEB] DDS reviews: prevention by slowing urea removal in new patients (e.g. short, lower-efficiency initial sessions); symptoms range from headache, nausea, dizziness, cramps, agitation and confusion to seizures and coma; treatment is mainly supportive and often self-limited. https://pmc.ncbi.nlm.nih.gov/articles/PMC6503314 (" + ACCESSED + "). Specific prescriptions (time, Qb, osmotic agents) are physician decisions."},

    {"kind": "emergency", "title": "Fever or suspected pyrogenic reaction",
     "source": "Ottawa Hospital pyrogenic reaction guideline (2013) · pyrogenic reaction outbreak studies · NHSN",
     "circuit": "stop dialysis; do NOT return blood (per pyrogenic reaction protocol); keep supplies", "circuit_level": "stop",
     "signs": ["Fever, chills, rigors in the first hour", "Hypotension", "Several patients: water/dialysate source", "CVC patient: think bacteremia"],
     "priorities": ["Stop dialysis per protocol; vital signs", "Blood cultures (and dialysate/water samples per policy)", "Sequester dialyzer, lines, concentrate", "Physician for antibiotics/antipyretics orders"],
     "avoid": ["Returning blood when a pyrogenic reaction is suspected", "Discarding supplies before investigation", "Missing a catheter infection"],
     "escalate": ["Physician now", "IPC and technician for clusters", "Report NHSN events (culture, IV antimicrobial)"],
     "notes": "[WEB] Pyrogenic reactions: fever/rigors ± hypotension within the first hour, linked to contaminated water/dialysate (outbreak studies); Ottawa guideline: stop dialysis immediately; study guide: discontinue, notify physician, do not return blood, cultures and endotoxin samples per policy, sequester supplies. Catheter bacteremia can mimic pyrogenic reactions – cultures distinguish them. https://kcr.csnscn.ca/... (Ottawa, secondary) – NEEDS REVIEW against local protocol."},

    {"kind": "steps", "title": "Communicate, document and report",
     "source": "IHI SBAR · Garrick R, et al. CJASN 2012 · local incident policy",
     "steps": [
         ("SBAR call", "Situation, background, assessment, recommendation"),
         ("Closed-loop orders", "Repeat back every verbal order"),
         ("Timeline", "Time of signs, actions, drugs, people informed"),
         ("Circuit and device", "Pump/clamp actions, blood returned or not, machine ID, alarms"),
         ("Evidence", "Keep lines, dialyzer, samples when the cause is unclear"),
         ("Incident report and debrief", "Same shift; share learning"),
     ],
     "side": {"head": "Emergency kit check", "fill": "navy", "body": ["Oxygen and suction", "Defibrillator/AED", "Emergency drugs per protocol", "Clamps, gauze, saline", "Daily checklist signed"]},
     "notes": "Documentation and communication principles; SBAR (IHI). Device-related events may also require manufacturer/regulatory reporting – follow local policy and FMC complaint process."},

    {"kind": "case", "title": "Scenario 1: ten minutes after starting",
     "source": "Fictional teaching scenario",
     "case": ["Mrs J, session 2, new dialyzer type today.", "After 10 minutes: tight throat, urticaria, wheeze.", "BP 78/40 (pre 150/85), SpO₂ 89%.", "Venous blood looks normal; no alarms."],
     "questions": ["Most likely emergency?", "Your first three actions?", "Return the blood? Why?", "What before her next session?"],
     "notes": "1. Type A (anaphylactic) dialyzer reaction. 2. Stop pump and clamp; call emergency help; airway, O₂, lay flat; anaphylaxis protocol per order. 3. No – type A: do not return blood (textbook teaching; verify locally). 4. Report; physician decides on different dialyzer/sterilisation; allergy documented."},

    {"kind": "case", "title": "Scenario 2: dark blood and back pain",
     "source": "Fictional teaching scenario",
     "case": ["Two patients on the same water loop develop back pain 40 minutes into treatment.", "Venous lines look dark red-brown.", "This morning's chlorine log is blank.", "One patient's pulse is 50 and irregular."],
     "questions": ["What do you suspect?", "Circuit action for both patients?", "Why is the slow irregular pulse urgent?", "Who must be informed?"],
     "notes": "1. Hemolysis from water contamination (chloramine) – cluster plus missing chlorine test. 2. Stop pumps, clamp, do NOT return blood; O₂; monitor. 3. Possible hyperkalemia from hemolysis → arrhythmia: ECG, urgent K⁺, physician now. 4. Physician/medical director, nurse in charge, technician; stop new starts; incident report; preserve samples (Lecture 06)."},

    {"kind": "kcheck", "title": "Knowledge check",
     "source": "Answers and rationales in the speaker notes",
     "questions": [
         ("Suspected hemolysis: the circuit blood is…", ["A. Returned quickly", "B. Discarded, not returned", "C. Returned after saline", "D. Returned if K⁺ normal"]),
         ("Air embolism: first circuit action?", ["A. Return blood", "B. Increase blood flow", "C. Clamp venous line, stop pump", "D. Silence the alarm"]),
         ("Severe IDH: the blood pump usually…", ["A. Stops at once", "B. Continues while UF stops", "C. Runs faster", "D. Reverses"]),
         ("Fever, rigors in 3 patients in hour 1. Think of…", ["A. Fluid overload", "B. Pyrogenic reaction", "C. DDS", "D. Steal syndrome"]),
     ],
     "notes": "Q1 B (BMC Res Notes 2014). Q2 C (clamp venous line, stop pump; no blood return). Q3 B (stop UF; pump usually continues; per protocol). Q4 B (cluster → water/dialysate; take cultures)."},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 07 summary",
     "items": [
         ("Recognise, secure, ABC, call", "Same structure; stay with the patient."),
         ("Circuit action depends on the cause", "No single 'return the blood' rule."),
         ("Do NOT return blood", "Air embolism, hemolysis, type A reaction, pyrogenic reaction (per protocol)."),
         ("Alarms miss things", "Visible access, observation and trends save lives."),
         ("Communicate and document", "SBAR, closed-loop orders, timeline, evidence, incident report."),
     ],
     "notes": "Bridge to Lecture 08: learning from events through indicators and reporting."},

    refs_slide(),
]
