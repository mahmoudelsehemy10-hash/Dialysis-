# -*- coding: utf-8 -*-
"""
Slide content for "Hemodialysis Fundamentals" (edit this file, then re-run build_deck.py).

Primary source: uploaded AREP (Advanced Renal Education Program, Fresenius Medical Care)
eLearning screenshots, referenced in the notes as  [Folder / screenshot time-stamp].
  - Dialysis.zip           -> "Introduction to Hemodialysis" module
  - vascular access.zip    -> "Vascular Access" module
  - Water Treatment.zip    -> actually the "Fluid Management / Fluid Overload" module
  - Acid Base.zip          -> "Fluids, Electrolytes, Acids and Bases" (intro screens only)
Web-verified items are marked [WEB] in the notes, with URL and access date.
"""
from pptx.dml.color import RGBColor

TITLE = "Hemodialysis Fundamentals"
SUBTITLE = "Principles, vascular access, fluid management and patient safety"
PRESENTER = ["Mr. Mahmoud Elsehemy BSN, MQM", "Clinical Application Specialist Critical Care"]
DATE_LOCATION = "Date | Location"
FOOTER_TEXT = "Hemodialysis Fundamentals"
ACCESSED = "accessed 13 Nov 2026"

BLUE = RGBColor(0x00, 0x33, 0xA0)
MID = RGBColor(0x37, 0x7C, 0xB5)
GREY = RGBColor(0xA8, 0xA3, 0x9D)
NAVY = RGBColor(0x07, 0x1B, 0x45)

SLIDES = [
    # 1 ---------------------------------------------------------------- title
    {"kind": "title", "notes": """
Purpose: a structured refresher on hemodialysis (HD) fundamentals for nurses and clinical staff who care for patients on HD.
Content is based on the Fresenius Medical Care Advanced Renal Education Program (AREP) eLearning modules provided as screenshots (Introduction to Hemodialysis; Vascular Access; Fluid Management; Fluids, Electrolytes, Acids and Bases), with selected points checked against current guidelines (marked in the notes).
Educational material only: always follow local policies, the device Instructions for Use and the physician's prescription.
Fill in date and location before presenting."""},

    # 2 ---------------------------------------------------------------- agenda
    {"kind": "agenda", "title": "Agenda and learning objectives",
     "source": "Objectives adapted from AREP modules: Introduction to Hemodialysis; Vascular Access; Fluid Management",
     "items": [
         ("HD basics", ["Define HD and its indications", "Describe the circuit, dialyzer and mechanisms", "Explain water treatment"]),
         ("Vascular access", ["Compare AVF, AVG and CVC", "Plan, mature and cannulate safely", "Recognise complications"]),
         ("Fluid management", ["Explain body fluid compartments", "Apply dry weight and UF rate", "Choose assessment tools"]),
         ("Safety and quality", ["Recognise intradialytic complications", "Apply safety best practices", "Summarise key messages"]),
     ],
     "notes": """
Four sections, about 45–60 minutes including discussion.
Objectives are adapted from the AREP module objective screens [Dialysis / 140621] and [vascular access / 140932].
Section 3 combines the AREP Fluid Management module (uploaded as "Water Treatment.zip") with the short Fluids/Electrolytes/Acid-Base screens (Acid Base.zip)."""},

    # 3 ---------------------------------------------------------------- chapter
    {"kind": "chapter", "title": "1  Hemodialysis basics", "notes": "Section 1: what HD is, when it starts, how the circuit works, and why water quality matters."},

    # 4 ---------------------------------------------------------------- what HD replaces
    {"kind": "split_cards", "title": "What hemodialysis replaces",
     "source": "KDOQI. Am J Kidney Dis. 2015;66(5):884-930 · AREP Introduction to Hemodialysis",
     "left": {"head": "What is hemodialysis?",
              "body": ["A form of kidney replacement therapy that takes over key kidney functions in near-total or total loss of kidney function.",
                       "Blood runs through a machine and a specialised filter (dialyzer) that removes toxins and excess water."]},
     "cards": [
         ("Excretion", ["Metabolites", "Drugs", "Toxins"]),
         ("Homeostasis", ["Water balance", "Electrolyte balance", "Acid–base balance"]),
         ("Hormone metabolism", ["Vitamin D conversion"]),
         ("Hormone secretion", ["Erythropoietin", "Renin", "Prostaglandins"]),
     ],
     "notes": """
Kidney functions in four groups [Dialysis / 140655]. HD mainly replaces excretion and parts of homeostasis (water, electrolytes, acid–base). Hormonal functions (erythropoietin, vitamin D activation) are NOT replaced by dialysis and need separate treatment (e.g. ESA, active vitamin D).
Definition [Dialysis / 140732, 141127]. The AREP module states HD is the most common form of KRT in the USA and that about 90% of dialysis treatments in the US are HD – this is a US figure (USRDS-based); do not generalise to other markets without local data.
Reference: KDOQI Clinical Practice Guideline for Hemodialysis Adequacy: 2015 Update. Am J Kidney Dis. 2015;66(5):884-930."""},

    # 5 ---------------------------------------------------------------- indications
    {"kind": "criteria", "title": "When to start hemodialysis",
     "source": "KDOQI Hemodialysis Adequacy 2015 Update. Am J Kidney Dis. 2015;66(5):884-930",
     "criteria": [
         ("Uremic signs and symptoms", "Symptoms or signs attributable to kidney failure (uremia)."),
         ("Protein-energy wasting", "Evidence of malnutrition linked to kidney failure."),
         ("Metabolic abnormalities", "Inability to safely manage metabolic abnormalities (e.g. potassium, acid–base) medically."),
         ("Volume overload", "Inability to safely manage fluid overload with medical therapy."),
     ],
     "highlight": {"head": "Key message",
                   "body": ["The decision to start should NOT be based on a specific level of kidney function alone.",
                            "Chronic kidney failure usually develops over months to years – plan early."]},
     "notes": """
Indications as presented in AREP [Dialysis / 140932], citing KDOQI 2015 (Am J Kidney Dis. 2015;66(5):884-930).
KDOQI 2015 also advises against starting dialysis based on a specific eGFR value alone; the decision combines symptoms, metabolic control, volume status and nutrition.
Planning (education, access creation) should start well before these criteria are met – see the Vascular Access section."""},

    # 6 ---------------------------------------------------------------- circuit
    {"kind": "image_two_lists", "title": "The HD circuit: blood and dialysate pathways",
     "source": "Ahmad S, et al. Handbook of Dialysis. 5th ed. 2015:66-88",
     "image": "hd_circuit.png", "image_alt": "Hemodialysis blood circuit diagram (AREP)",
     "caption": "Blood circuit illustration: FMC AREP, Introduction to Hemodialysis (uploaded screenshot)",
     "lists": [
         ("Blood circuit", ["Arterial bloodline and arterial pressure monitor", "Blood pump and heparin pump",
                            "Dialyzer, venous bloodline and venous pressure monitor", "Air/blood-leak protection"], "blue"),
         ("Dialysate circuit", ["Purified water + acid and bicarbonate concentrates", "Heater, degasser and mixing",
                                "Conductivity and temperature monitors", "Used dialysate to drain"], "mid"),
     ],
     "notes": """
The HD machine pumps the patient's blood and dialysate through the dialyzer (countercurrent) to remove toxins and water [Dialysis / 141030, 141056].
Ancillary supplies [Dialysis / 141345–141550]: bloodlines (arterial = to dialyzer, venous = back to patient), access needles, anticoagulant (heparin) to prevent clotting, normal saline to prime, rinse back and replace fluid.
Needle note from AREP: 17/16 G for initial AVF use, 15 G once the fistula matures – always follow local protocol and the needle-to-blood-flow guidance (slide 18).
Component names differ between machine models: refer to the IFU of the specific FMC machine used locally (e.g. 5008/6008 series) – this slide is generic.
Reference: Ahmad S, et al. Handbook of Dialysis. 5th ed. 2015:66-88."""},

    # 7 ---------------------------------------------------------------- mechanisms
    {"kind": "columns", "title": "Three mechanisms remove solutes and water",
     "source": "Rosner M. South Med J. 2005;98(8):785-791 · Daugirdas JT. Handbook of Dialysis. 5th ed. 2015:34-65 · Locatelli F, et al. Kidney Int. 2002;61(S80):S115-S120",
     "h": 3.3, "banner_y": 5.25,
     "columns": [
         {"head": "Diffusion", "rows": [("Principle", "Solutes move from high to low concentration across the membrane."),
                                        ("Best for", "Small solutes such as urea; smaller molecules diffuse faster.")]},
         {"head": "Ultrafiltration", "rows": [("Principle", "Water moves from high to low pressure across the membrane."),
                                              ("In HD", "Lower pressure on the dialysate side pulls excess plasma water out.")]},
         {"head": "Convection", "rows": [("Principle", "Solutes are dragged with water flow (solvent drag)."),
                                         ("In HD", "Raises middle-molecule clearance; used in hemodiafiltration.")]},
     ],
     "banner": "Removal depends on concentration gradient, molecule size and shape, charge and protein binding",
     "notes": """
AREP [Dialysis / 144649–144923].
Diffusion: rate depends on molecule size; efficient for small solutes (urea).
Ultrafiltration: hydrostatic pressure gradient (blood side > dialysate side) removes plasma water – this is how fluid is removed.
Convection: solutes move with the water (solvent drag); hemodiafiltration combines HD with high-volume UF plus infusion of replacement fluid to increase convective clearance of middle molecules (e.g. β2-microglobulin).
Note: hemodiafiltration availability and settings depend on the machine and local approval – check the product IFU."""},

    # 8 ---------------------------------------------------------------- dialyzer
    {"kind": "table_side", "title": "The dialyzer: where blood and dialysate meet",
     "source": "Ahmad S, et al. Handbook of Dialysis. 2015:66-88 · Castner D. Core Curriculum for Nephrology Nursing, Module 3. 2015:74-100",
     "table": {"w": 7.4, "col_w": [2.2, 2.6, 2.6], "row_h": 0.62, "size": 13,
               "rows": [["Feature", "High-flux", "Low-flux"],
                        ["Pore size", "Larger", "Smaller"],
                        ["Molecular weight cut-off", "Higher", "Lower"],
                        ["Water permeability", "High", "Lower"],
                        ["Middle-molecule clearance", "Higher", "Lower"]]},
     "side": {"head": "How dialyzers are characterised", "h": 4.75,
              "body": ["Membrane type", "Surface area (drives small-solute clearance)", "Blood volume capacity",
                       "Ultrafiltration coefficient (KUF)", "Clearance", "Sterilisation method", "Capacity for reuse"]},
     "notes": """
The dialyzer is a bundle of tightly packed hollow fibres; blood flows inside the fibres, dialysate flows outside in the opposite direction [Dialysis / 141200].
Classification [Dialysis / 141228, 141304]. The ability to remove small solutes such as urea is primarily a function of membrane surface area.
High- vs low-flux is defined by water permeability and middle-molecule clearance.
Reuse: listed by AREP as a dialyzer characteristic; single use is standard practice in many markets – follow local policy and the dialyzer IFU."""},

    # 9 ---------------------------------------------------------------- water treatment
    {"kind": "water", "title": "Water treatment protects every treatment",
     "source": "Ward RA, Ing TS. Handbook of Dialysis. 2015:89-98 · Payne G. Core Curriculum for Nephrology Nursing, Module 3. 2015:101-113",
     "caption": "Water treatment illustration: FMC AREP, Introduction to Hemodialysis (uploaded screenshot)",
     "stages": [
         ("Pre-treatment", ["Multimedia filter", "Carbon filter: removes chlorine/chloramine", "Softener: removes Ca, Mg; protects RO"]),
         ("Primary purification", ["Reverse osmosis (RO): pressurised water forced through a semi-permeable membrane"]),
         ("Post-treatment", ["Storage / distribution", "Endotoxin filter: removes bacteria and endotoxins"]),
     ],
     "stat": ("120–150 L", "of dialysate per 4-hour HD session"),
     "stat_body": ["Small contaminants in dialysate can cross into the bloodstream.",
                   "Dialysate = purified water + acid and bicarbonate concentrates."],
     "notes": """
AREP [Dialysis / 141622, 141808–142031]: water treatment ensures that water used for HD meets AAMI standards. Stages: pre-treatment (multimedia filter, carbon filter, softener with brine tank, micron filter), primary purification (reverse osmosis), post-treatment (storage tank, endotoxin filter/ultrafilter, distribution loop).
Patients are exposed to about 120–150 L of dialysis solution during each 4-hour treatment – far more water than a healthy person drinks – so low-molecular-weight contaminants matter.
Specific configurations depend on the installed FMC water treatment system: refer to its IFU and local monitoring schedule.
References: Ward RA, Ing TS. Handbook of Dialysis 2015:89-98; Payne G. Core Curriculum for Nephrology Nursing, Module 3, 2015:101-113."""},

    # 10 --------------------------------------------------------------- contaminants
    {"kind": "table_only", "title": "Dialysis water: maximum contaminant levels",
     "source": "AAMI limits as shown in AREP (Ward RA, Ing TS. 2015:89-98; Nelson L, et al. Goldfrank's Toxicologic Emergencies. 2011; AAMI 2014) · ISO 23500-3",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.8, 3.0, 6.25], "row_h": 0.335, "size": 11,
               "rows": [["Agent", "Maximum level", "Effects of excess"],
                        ["Aluminum", "0.01 mg/L", "Bone disease, dialysis encephalopathy, anemia"],
                        ["Chloramine", "0.1 mg/L", "Hemolytic anemia"],
                        ["Fluoride", "0.2 mg/L", "Pruritus, nausea, ventricular fibrillation"],
                        ["Copper / Zinc", "0.1 mg/L each", "Hemolytic anemia"],
                        ["Sulfate", "100 mg/L", "Nausea, vomiting, metabolic acidosis"],
                        ["Calcium", "2 mg/L", "Muscle weakness, lethargy, cardiac disturbances, coma"],
                        ["Magnesium", "4 mg/L", "Loss of reflexes, muscular paralysis, bradycardic arrest"],
                        ["Potassium", "8 mg/L", "ECG changes, myocardial depression"],
                        ["Sodium", "70 mg/L", "Thirst, restlessness, fatigue"],
                        ["Microbial count", "100 CFU/mL (action level 50)", "Fever, chills, hypotension, death"],
                        ["Endotoxin [web]", "0.25 EU/mL (action level 0.125)", "Pyrogenic reactions, chronic inflammation"]]},
     "banner": "Check limits against the current ISO 23500 series and local regulation before use",
     "banner_y": 5.85,
     "notes": """
Rows 1–10 are copied from the AREP table [Dialysis / 141732] (AAMI standard as cited there: Ward RA, Ing TS. Handbook of Dialysis 2015:89-98; Nelson L, et al. Goldfrank's Toxicologic Emergencies 2011; AAMI 2014).
[WEB] Endotoxin row added: ISO 23500-3 sets dialysis water endotoxin < 0.25 EU/mL (action level typically 50% of the maximum). Verified only via secondary summaries (ISO preview page: https://webstore.ansi.org/preview-pages/ISO/preview_ISO+23500-3-2019.pdf; summary: https://open-exam-prep.com/study-guides/bonent-cht/water-treatment-and-dialysate/aami-iso-water-quality-standards-testing; ACLAB table: https://referencemanual.aclab.com/welcome/environmental-testing-collection-and-shipping/dialysis/aami-epa-standards-for-water-analysis/), """ + ACCESSED + """.
IMPORTANT: ISO 23500-3:2019 was replaced by ISO 23500-3:2024. Chlorine is expressed differently across documents (USP lists chloramines 0.1 and free chlorine 0.5 mg/L; ISO uses total chlorine 0.1 mg/L). Verify all limits against the official current standard and national rules – NEEDS REVIEW by the local water/technical team."""},

    # 11 --------------------------------------------------------------- adequacy
    {"kind": "adequacy", "title": "Dialysate and dose: getting the prescription right",
     "source": "KDOQI Hemodialysis Adequacy 2015 Update. Am J Kidney Dis. 2015;66(5):884-930",
     "left": {"head": "Dialysate is prepared by mixing",
              "body": ["Acid concentrate (electrolytes, glucose)", "Bicarbonate concentrate (buffer)", "Purified water",
                       ]},
     "left_note": ["Prescriptions vary by time of day, frequency, duration and location.",
                   "Concentrate composition is product-specific: follow the label and the prescription."],
     "right_head": "Adequacy is measured by Kt/V (thrice-weekly HD)",
     "stats": [("1.4", "Target spKt/V per session"), ("1.2", "Minimum delivered spKt/V")],
     "right_body": ["K = urea clearance, t = time, V = urea distribution volume (≈ total body water)",
                    "Other schedules: weekly standard Kt/V target 2.3 (minimum 2.1)"],
     "notes": """
Dialysate: fluid with electrolytes, buffer and glucose that exchanges solutes with blood through the dialyzer [Dialysis / 142057]; prepared from acid concentrate, bicarbonate concentrate and purified water.
Adequacy [Dialysis / 145459, 145532] and [Water Treatment folder / 155139 – V is total body water; Watson/Hume formulas estimate V].
[WEB] KDOQI 2015 Update, Guideline 3.1: target spKt/V 1.4 per session for thrice-weekly HD, minimum delivered 1.2 (graded 1B; unchanged from 2006). For other schedules: target weekly standard Kt/V 2.3, minimum 2.1. PubMed: https://pubmed.ncbi.nlm.nih.gov/26498416/ ; AJKD blog summary: https://ajkdblog.org/2015/11/30/the-2015-kdoqi-hemodialysis-adequacy-guideline-update-whats-new/ (""" + ACCESSED + """).
Bullet "acid concentrate (electrolytes, glucose)": composition of concentrates varies by product – follow the product label."""},

    # 12 --------------------------------------------------------------- chapter
    {"kind": "chapter", "title": "2  Vascular access", "notes": "Section 2: choosing, planning, maturing, cannulating and protecting the vascular access – the patient's lifeline."},

    # 13 --------------------------------------------------------------- access types
    {"kind": "table_pie", "title": "Access types: advantages and challenges",
     "source": "Blake PG, et al. Kidney Int. 2012;82(6):623-625 · Rivara et al. Clin J Am Soc Nephrol. 2016;11(2):298-307 · DOPPS Practice Monitor, Nov 2015",
     "table": {"w": 8.3, "col_w": [1.5, 3.3, 3.5], "row_h": 1.35, "head_h": 0.45, "size": 11,
               "rows": [["Access", "Advantages", "Challenges"],
                        ["AV fistula (AVF)", ["Very low infection risk", "Long lasting once mature", "Lower mortality association"],
                         ["High primary failure rate", "Pain and bruising early on", "Aneurysm and bleeding risk"]],
                        ["AV graft (AVG)", ["Low infection risk", "Low primary failure rate", "Lower mortality than CVC"],
                         ["High secondary failure rate", "Frequent interventions", "Bleeding risk"]],
                        ["Central venous catheter (CVC)", ["Ease of insertion", "Immediate use", "No cannulation"],
                         ["Higher infection and mortality", "Dysfunction, thrombolytics", "Central vein damage"]]]},
     "pie": {"title": "Access in use, DOPPS 2015 (%)",
             "data": [("AVF", 66.5), ("AVG", 18.4), ("CVC", 15.1)],
             "note": "Graph adapted in AREP from the DOPPS Practice Monitor (Nov 2015); population as reported in the module. Shares vary by country."},
     "notes": """
Comparison table [Dialysis / 144615] and [vascular access / 151232] (Blake PG, et al. Kidney Int. 2012;82(6):623-625; Rivara MB, et al. Clin J Am Soc Nephrol. 2016;11(2):298-307; Ravani P, et al. Am J Kidney Dis. 2016).
Chart data copied from AREP pie chart [Dialysis / 142509]: AVF 66.5%, AVG 18.4%, catheter 15.1% ("Graph adapted from DOPPS November 2015"). The module does not state the country/population – most likely US DOPPS Practice Monitor. NEEDS REVIEW before quoting as a current or local figure; replace with current local registry data if available.
AREP order of preference: AVF preferred permanent option; AVG acceptable permanent option; CVC – avoid long-term use [vascular access / 151058].
CVC may be appropriate in acute/hospitalised patients or when AVF/AVG is not feasible (multiple failed surgeries, severe vascular disease, very low cardiac output, small children, some elderly patients) [vascular access / 151213]."""},

    # 14 --------------------------------------------------------------- planning
    {"kind": "flow", "title": "Plan access early, starting at CKD stage 4",
     "source": "Lok CE, et al. KDOQI Vascular Access 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164 · Jindal K, et al. J Am Soc Nephrol. 2006;17(3 Suppl 1):S1-S27",
     "steps": [
         ("Start early", "CKD 4 (GFR < 30 mL/min/1.73 m²)"),
         ("Educate", "Patients with more knowledge are more likely to start HD with an AVF or AVG"),
         ("Evaluate", "Assess vessels and feasibility; build an individual ESKD Life-Plan"),
         ("Create access", "AVF ≥ 6 months and AVG 3–6 weeks before expected HD start"),
     ],
     "bottom_left": {"head": "Why timing matters", "body": [
         "Early creation (≥ 4 months before use) linked to lower sepsis and mortality risk",
         "Challenge: hard to predict when dialysis will be needed",
         "Canadian guideline: surgical referral at eGFR 15–20"]},
     "bottom_right": {"head": "AVF site order: most distal first", "items": ["Radiocephalic (wrist)", "Brachiocephalic (elbow)", "Transposed brachiobasilic"]},
     "notes": """
AREP [vascular access / 151029, 151118, 151425, 151447, 151511, 151540].
- Start education at CKD 4 (GFR < 30). Education programmes associated with longer survival (2.25 years, p = 0.053) and 2.8 months longer to dialysis initiation (p < 0.001); 36% of CKD 3–5 patients report no knowledge about HD (as reported by AREP).
- KDOQI: AVF at least 6 months and AVG 3–6 weeks before anticipated start; Canadian Society of Nephrology: surgeon referral at eGFR 15–20 mL/min/1.73 m² (Jindal K, et al. 2006).
- Early creation (4 months before use): RR of sepsis 0.57 and lower mortality (RR 0.76; 95% CI 0.58–1.00) (Oliver MJ, et al. J Am Soc Nephrol 2004).
- Moist et al.: median 184 days between AVF placement and HD initiation.
[WEB] KDOQI 2019 Vascular Access Guideline (Lok CE, et al. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164) replaced the single "Fistula First" strategy with a patient-centred "ESKD Life-Plan" (P-L-A-N: Patient Life-Plan first, then Access Needs). AVF remains appropriate for many patients, but access choice should match the patient's goals, modality plan and vessels. Sources: https://homedialysis.org/news-and-research/blog/340-the-eskd-life-plan-a-new-concept-in-the-nkf-vascular-access-guideline-update ; https://consultqd.clevelandclinic.org/updated-vascular-access-guidelines-put-emphasis-on-patients-individual-needs/ (""" + ACCESSED + """)."""},

    # 15 --------------------------------------------------------------- maturation
    {"kind": "rule6", "title": "AVF maturation: the rule of 6s",
     "source": "Lok CE, et al. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164 · Zangan SM, et al. 2009 · Achneck HE, et al. Semin Dial. 2010;23(1):25-33",
     "lead": "A fistula is likely mature for cannulation at about:",
     "sixes": [("6 wk", "after creation"), ("600", "mL/min access flow"), ("< 0.6 cm", "deep below the skin"), ("≥ 0.6 cm", "vessel diameter")],
     "left": {"head": "Watch for early maturation failure", "body": [
         "25–50% of AVFs never mature", "Signs occur up to 3 weeks after creation", "Access flow < 400 mL/min: address promptly"]},
     "right": {"head": "Before every session: look, listen, feel", "body": [
         "Look: swelling, infection, aneurysm, stenosis", "Listen: low-pitched continuous bruit", "Feel: thrill, pulse, arm-elevation test"]},
     "notes": """
AREP [vascular access / 151648, 151710, 151733, 151758, 153406, 153427].
Rule of 6s (KDOQI): ~6 weeks, flow ~600 mL/min, depth < 0.6 cm, diameter ≥ 0.6 cm (AREP diagram shows "0.6 cm (max) below surface" and ">0.6 vessel diameter").
AVG: short maturation; early cannulation at 24–72 h for specific early-cannulation grafts; conventional grafts cannulated after ~2 weeks; 3–6 weeks recommended in AREP.
Maturation-failure table (Achneck HE, et al.): outflow vein not maturing (ultrasound, angiography), venous stenosis (arm/breast/face swelling – angioplasty), accessory veins, infection (antibiotics).
Physical examination detects stenosis with a positive predictive value of 70–80% in AVGs and 93% in AVFs (as reported by AREP).
Examination should precede every cannulation."""},

    # 16 --------------------------------------------------------------- cannulation
    {"kind": "image_cards", "title": "Choose the right cannulation technique",
     "source": "Schmidli J, et al. Eur J Vasc Endovasc Surg. 2018;55(6):757-818 · Lok CE, et al. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164",
     "image": "rope_ladder.png", "image_alt": "Rope-ladder cannulation sites on forearm AVF (AREP)",
     "caption": "Rope ladder: new sites each session, ≥ 3 cm from the anastomosis and ≥ 5 cm between needle tips. Illustration: FMC AREP (uploaded screenshot).",
     "cards": [
         ("Rope ladder: preferred", ["Uses the entire length of the AVF or graft", "May reduce aneurysm and infection risk", "Harder with a short AVF; can be painful"], "blue"),
         ("Buttonhole: AVF only, selected cases", ["Same site, angle and depth every time", "Track forms after about 6–10 sessions", "Higher infection risk; strict hygiene"], "mid"),
         ("Area technique: not recommended", ["Repeated punctures in one area", "Causes aneurysm and thin skin"], "grey"),
     ],
     "notes": """
AREP [vascular access / 151841–152237].
Rope ladder: venous needle antegrade (direction of flow); arterial needle antegrade or retrograde; insertion angle chosen from the physical exam.
Buttonhole: only for AVFs, not AVGs; a single cannulator until the track is established; blunt needles once the track forms. May improve comfort and reduce haematoma/infiltration, but carries higher infection risk – limit to special circumstances.
Area technique: less widely used and no longer recommended (aneurysmal dilatation, thinning skin, longer bleeding).
Local cannulation policy and needle IFU apply."""},

    # 17 --------------------------------------------------------------- buttonhole vs RL chart
    {"kind": "bar_compare", "title": "Buttonhole vs rope ladder: patency is similar",
     "source": "Chan MR, et al. Semin Dial. 2014;27(2):210-216 · O'Brien FJ, et al. Clin Kidney J. 2012;5(6):526-529 · Muir CA, et al. Clin J Am Soc Nephrol. 2014;9(1):110-119",
     "chart": {"name": "Primary patency chart", "title": "Primary patency over 12 months (%)",
               "categories": ["3 months", "6 months", "12 months"],
               "series": [("Buttonhole (n = 45)", [86, 72, 57]), ("Rope ladder (n = 38)", [89, 71, 60])],
               "colors": [MID, BLUE], "max": 100},
     "side": {"head": "What this means", "body": [
         "No meaningful patency or quality-of-life difference in this study",
         "Bacteremia: 0.073 per 1000 AVF-days with buttonhole vs 0 with rope ladder",
         "Systematic review: higher AVF infection risk with buttonhole",
         ("Prefer rope ladder; reserve buttonhole for special circumstances", {"bold": True, "color": NAVY, "space_after": 6})]},
     "notes": """
Chart data from AREP table [vascular access / 152213] (Chan MR, et al. Semin Dial. 2014;27(2):210-216): primary patency buttonhole (n = 45) 86% / 72% / 57% and rope ladder (n = 38) 89% / 71% / 60% at 3 / 6 / 12 months; no difference in quality of life. Small single study – interpret with caution.
Infection data [vascular access / 152452]: higher incidence of localised and generalised infection with buttonhole (Faratro R, et al. Hemodial Int. 2015;19 Suppl 1:S80-92); retrospective bacteremia rate 0.073/1000 AVF days vs 0 (O'Brien FJ, et al. Clin Kidney J. 2012); systematic review (Muir CA, et al. CJASN 2014;9(1):110-119)."""},

    # 18 --------------------------------------------------------------- needle & skin prep
    {"kind": "table_side", "title": "Match needle gauge to blood flow, prepare skin aseptically",
     "source": "National Kidney Foundation. Clinical Update 2016 · Lok CE, et al. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164",
     "table": {"w": 5.6, "col_w": [2.9, 2.7], "row_h": 0.55, "size": 13,
               "rows": [["Blood flow rate (BFR)", "Minimum needle gauge"],
                        ["< 300 mL/min", "17 G"],
                        ["300–350 mL/min", "16 G"],
                        ["> 350–450 mL/min", "15 G"],
                        ["> 450 mL/min", "14 G"]]},
     "side": {"head": "KDOQI skin preparation", "h": 4.75, "body": [
         ("1. Locate, inspect and palpate the sites", {"space_after": 6}),
         ("2. Wash with antibacterial soap or scrub and water", {"space_after": 6}),
         ("3. Cleanse with 2% chlorhexidine/70% alcohol and/or 10% povidone-iodine per manufacturer", {"space_after": 10}),
         "Chlorhexidine-alcohol: 30-second back-and-forth scrub, let dry, do not blow",
         "Povidone-iodine: 2–3 minutes contact time",
         "Clean gloves; change if contaminated"]},
     "notes": """
Needle table from AREP [vascular access / 153559] ("Table adapted from The National Kidney Foundation Clinical Update 2016"): minimum recommended gauges for stated BFR. Larger needles reduce pre-pump arterial pressure and increase delivered blood flow.
Needle selection [vascular access / 153539]: smallest needles for initial cannulation; needle size equal or smaller than the vein; increase size if arterial pressure < −250 mmHg or venous pressure > 250 mmHg (as stated in AREP); pre-pump arterial pressure monitoring recommended so pump speed does not exceed what the needle can deliver.
Skin preparation [vascular access / 153446, 153505] (KDOQI 2019): Staphylococcus aureus carriage 40% of HD patients vs 27% of general population (as reported by AREP). Facilities should have a written skin-preparation policy.
Note: the gauge table text shows "<300 / 300–350 / >350–450 / >450 mL/min" – check against local machine BFR practice."""},

    # 19 --------------------------------------------------------------- complications grid
    {"kind": "six_grid", "title": "AV access complications to recognise early",
     "source": "Al-Jaishi AA, et al. 2016 · Daugirdas JT, et al. 2014 · USRDS 2019 · Mudoni A, et al. Clin Kidney J. 2015 · Axley B, et al. Nephrol Nurs J. 2012 · Lee T, et al.",
     "items": [
         ("Thrombosis", "80–85%", "of access loss; causes include stenosis, hypotension, hypercoagulability, flow stasis."),
         ("Infection", "10% vs 1%", "AVG vs AVF; mostly staphylococci. Risks: pruritus, hematoma, pseudo-aneurysm."),
         ("Aneurysm", "5% to > 60%", "reported incidence; more in proximal and cephalic AVFs, poor cannulation."),
         ("Steal syndrome", "1–20%", "of AV accesses; hand ischemia. Risks: upper-arm access, PAD, diabetes."),
         ("Venous needle dislodgement", "400–500 mL/min", "typical blood flow: blood loss can be life-threatening within minutes."),
         ("Infiltration", "6.8% / year", "annual rate in a 5-year study; swelling, bruising, pain. Ice, pressure, reassess."),
     ],
     "notes": """
AREP [vascular access / 152344–152609, 153817].
- Thrombosis: leading cause of loss of AVF patency, accounts for 80–85% of access loss (Al-Jaishi AA, et al. JASN 2016; Axley B, et al. Nephrol Nurs J 2012).
- Infection: most common agent staphylococci; infection rates ~10x higher with AVG (10% vs 1%) (Daugirdas 2014; Schild AF, et al. J Vasc Access 2008; USRDS 2019).
- Aneurysm: incidence 5% to > 60%; proximal 48% vs distal 39% AVFs (Jankovic A, et al. Nephron Clin Pract 2013; Mudoni A, et al. Clin Kidney J 2015).
- Steal: 1–20% of AV accesses.
- VND: life-threatening at typical BFR 400–500 mL/min (Axley 2012; Sandroni S. JASN 2008; Garrick R, et al. CJASN 2012). Associated factors: agitation/cognitive impairment, treatment outside the unit, poor taping, hypotension or cramps.
- Infiltration: annual rate 6.8% (Lee T, et al., as cited in AREP). Management by severity: ice ≥ 10 min and avoid maximising pump speed; withdraw needle and hold pressure if moderate; decide on dialysis that day if large.
Percentages are as reported in AREP; populations differ between studies."""},

    # 20 --------------------------------------------------------------- prevention
    {"kind": "two_cards", "title": "Protect the access: prevent dislodgement and infection",
     "source": "Hawley CM, et al. Hemodial Int. 2008;12 Suppl 1:S21-5 · Ellison KD, et al. · Lok CE, et al. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164",
     "h": 3.55,
     "cards": [
         ("Staff: during every treatment", ["Secure needles, lines and connections (taping)", "Keep the access visible throughout dialysis",
                                             "Monitor BP and pulse; use wetness/blood-leak detectors", "Aseptic cannulation; rope ladder over buttonhole",
                                             "Max. 2 attempts, then call an experienced cannulator"]),
         ("Patients: teach them to", ["Wash the access arm with soap and water before HD", "Check thrill/pulse daily and listen for the bruit",
                                       "Recognise and report infection signs", "Avoid heavy carrying, tight clothing, sleeping on the arm",
                                       "No BP or IV access on the access arm"]),
     ],
     "banner": "Ultrasound-guided cannulation: deep or small AVF, near artery/nerve, repeated failures, critical first attempt",
     "notes": """
AREP [vascular access / 152637, 152716, 152735, 153931, 154022, and Dialysis / 145420].
VND mitigation cycle: secure access site and connections, ensure access visibility, monitor BP/pulse, use wetness detectors, educate/retrain patients, consider single-needle where appropriate (Hawley CM, et al. Hemodial Int 2008; Ellison KD, et al.).
Infection mitigation: aseptic cannulation, eradicating staphylococcal nasal carriage, local sterilisation solutions, rope ladder over buttonhole (Mahadevan K 2004; Hawley 2008; Nesrallah GE, et al. AJKD 2013).
Cannulation competence: a maximum of 2 attempts is recommended before seeking an expert; mentoring programmes; novice nurses should have an expert on hand (Schmidli 2018; Marticorena 2015; Harwood, Clin Kidney J 2016).
Ultrasound may reduce complications; indications listed in AREP (Marticorena RM, et al. CANNT J 2015)."""},

    # 21 --------------------------------------------------------------- chapter
    {"kind": "chapter", "title": "3  Fluid management", "notes": "Section 3: body fluids, fluid overload, dry weight, ultrafiltration rate and tools for assessing fluid status, plus electrolytes and acid–base basics."},

    # 22 --------------------------------------------------------------- compartments
    {"kind": "compartments", "title": "Where body water lives",
     "source": "Mulroney S, Myers A. Netter's Essential Physiology. 2016:2-11 · Verbalis JG. Brenner and Rector's The Kidney. 2012:540-594",
     "chart": {"title": "Total body water ≈ 42 L (example: 70 kg adult, 60%)",
               "series": [("Intracellular fluid (2/3)", 28.0), ("Interstitial fluid (3/4 of ECF)", 10.5), ("Plasma (1/4 of ECF)", 3.5)],
               "max": 42,
               "note": "Educational example (calculated): 70 kg × 60% = 42 L; ICF 28 L, ECF 14 L. Real values vary with age, sex and body fat."},
     "facts": [("45–60%", "of body weight is water"), ("285–295", "mOsm/L plasma osmolality"), ("~2.5 L", "daily intake = output in health")],
     "side": {"head": "Why it matters in HD", "body": [
         "Total body water ≈ V in Kt/V", "Lower with age, more body fat and in females",
         "UF removes plasma water; plasma refills from interstitial and intracellular space",
         "Osmolality differences drive fluid shifts between compartments"]},
     "notes": """
AREP Fluid Management module (uploaded as "Water Treatment.zip") [Water Treatment / 155109, 155139, 155202, 155238, 155351, 155412, 155920–160005].
- TBW 45–60% of body weight; varies with age, body fat and sex.
- Compartments: ICF 2/3, ECF 1/3 (plasma 1/4, interstitial 3/4).
- Normal osmolality 285–295 mOsm/L; fluid moves between compartments according to relative osmolality.
- Daily balance about 2.5 L in (1.3 L beverages, 0.9 L food, 0.3 L metabolism) and 2.5 L out (1.5 L urine, 0.9 L sweat and respiration, 0.1 L GI).
Chart values are a CALCULATED TEACHING EXAMPLE (70 kg × 0.60 = 42 L; 2/3 = 28 L ICF; ECF 14 L split 3/4 interstitial = 10.5 L and 1/4 plasma = 3.5 L), matching the AREP saline example showing 28 L ICF and 14 L ECF. Not patient data.
V for Kt/V can be estimated with Watson or Hume formulas (Tzamaloukas AH, et al. Perit Dial Int 1996)."""},

    # 23 --------------------------------------------------------------- fluid overload
    {"kind": "bar_compare", "title": "Fluid overload is common and harmful",
     "source": "Wabel P, et al. (2,125 European HD patients), as cited in AREP · Antlanger M, et al. BMC Nephrol. 2013;14:266",
     "chart": {"name": "Pre-HD fluid status chart", "title": "Pre-HD fluid status, 2,125 European HD patients (%)",
               "categories": ["Fluid depleted", "Normal range", "Fluid overloaded"],
               "series": [("Share of patients", [16.7, 55.0, 28.3])],
               "point_colors": [GREY, MID, BLUE], "max": 70, "fmt": '0.0"%"'},
     "side": {"head": "Consequences", "body": [
         "Hypertension and left ventricular hypertrophy", "Heart failure and pulmonary edema", "Edema and ascites",
         "Increased risk of death",
         ("No single guideline definition of fluid overload (e.g. relative overhydration > 7–15% or > 2.5 L by BIS)", {"size": 12, "space_after": 4})]},
     "notes": """
Chart from AREP histogram [Water Treatment / 155612]: fluid depleted 16.7% and fluid overloaded 28.3% (time-averaged fluid overload, 2,125 European HD patients; cited there as Wabel P, et al. Dial Transpl. 2010;3(Suppl 3):iii191-iii192). The "normal range" value 55.0% is CALCULATED (100 − 16.7 − 28.3) and was not printed in the source. Citation details look incomplete in the source – NEEDS REVIEW (likely NDT Plus 2010 abstract).
Second AREP study (39 chronic HD patients, ECV/LBM ratio): 51.3% overloaded, 35.9% normal, 7.7% depleted (Dou Y, et al. Semin Dial 2012;25(4):377-387) – not charted.
Definitions [Water Treatment / 155547]: guidelines do not clearly define fluid overload; studies use pre-HD relative hydration > 7–15%, > 2.5 L, ECV/LBM > 0.344, or relative blood volume change < 1.33%/h.
Consequences [Water Treatment / 155644] (Antlanger M, et al. BMC Nephrol 2013;14:266)."""},

    # 24 --------------------------------------------------------------- dry weight levers
    {"kind": "levers", "title": "Dry weight and four levers to control fluid",
     "source": "KDOQI. Am J Kidney Dis. 2004;43(5 Suppl 1):S1-S290 · KDIGO. Kidney Int. 2013;3(Suppl 1):1-150 · KDOQI. Am J Kidney Dis. 2015;66(5):884-930",
     "def_head": "Dry weight: extracellular volume at or near normal, but not below normal",
     "def_body": "Sets the target weight and UF goal; may vary between sessions; reassess regularly (at least every 2 weeks); often found by trial and error.",
     "levers": [
         ("Medication", ["Diuretics if residual kidney function", "ACE inhibitors / ARBs for hypertension"]),
         ("Diet", ["Anuric: fluid ~1.0–1.5 L/day", "Sodium < 2 g/day (KDIGO)", "Salt drives thirst and intake"]),
         ("Ultrafiltration", ["Removes excess fluid during HD", "Volume set by dry weight", "Rate must be tolerated"]),
         ("Dialysate sodium", ["Usually 138–140 mEq/L", "Avoid high Na if high BP or IDWG", "Low Na: risk of instability"]),
     ],
     "banner": "Counsel patients on both known and hidden sources of fluid and sodium",
     "notes": """
AREP [Water Treatment / 155714–155900, 160302–160601].
Dry weight: at dry weight the extracellular volume is at or near normal but not less than normal; used to set target weight; monitor regularly (AREP: at least every 2 weeks).
Pharmacological: KDOQI 2004 recommends diuretics for most CKD patients to control ECF expansion; ACEi/ARB often recommended in hypertensive CKD.
Diet: anuric patients generally limited to 1.0–1.5 L/day; less strict with residual function (Santos SF, et al. Semin Dial 2010; Lindley EJ. Semin Dial 2009). KDIGO 2012 BP guideline: < 2 g sodium/day unless contraindicated; KDOQI 2015: reduce dietary sodium. Average US diet ≈ 3.4 g sodium/day; anuric HD patients with sodium-induced thirst drink ~1 L of water per 8 g of salt.
Dialysate sodium: KDOQI 2015 recommends against high dialysate sodium, especially with elevated BP and/or IDWG; most patients treated with 138–140 mEq/L. High Na: ↑ plasma Na, thirst, hypertension, volume overload. Low Na: ↓ plasma Na, hemodynamic instability, insufficient fluid removal.
Sodium modelling, sodium alignment and individualised prescriptions: benefits and risks are uncertain (Mann H 2000; Raimann JG 2011; Basile C 2016)."""},

    # 25 --------------------------------------------------------------- UF rate
    {"kind": "ufr", "title": "Ultrafiltration rate: find the balance",
     "source": "Flythe JE, et al. Kidney Int. 2011;79(2):250-257 · Assimon MM, Flythe JE. Curr Opin Nephrol Hypertens. 2015;24(6):525-530",
     "formula": "fluid to remove (mL) ÷ [weight (kg) × time (h)]",
     "example": {"head": "Worked example (educational, not a patient)", "body": [
         "Interdialytic weight gain to remove: 2.5 kg = 2,500 mL",
         "Weight 70 kg, session 4 h",
         "2,500 ÷ (70 × 4) = 8.9 mL/kg/h",
         ("Higher gains or shorter sessions push UFR up quickly", {"bold": True, "color": NAVY, "space_after": 4})]},
     "zones_head": "Observational data (HEMO study)",
     "zones": [("≤ 10", "Reference group"),
               ("10–13", "No overall association; higher risk in heart failure"),
               ("> 13", "↑ all-cause (HR 1.59) and CV mortality (HR 1.71)")],
     "balance": ["Too slow → insufficient fluid removal",
                 "Too fast → hypotension, myocardial stunning, hypovolemia",
                 "Association, not proven cause"],
     "notes": """
AREP [Water Treatment / 160042–160218]: UF volume is determined by the prescribed dry weight; UF rate should balance euvolemia, BP control and solute clearance against hemodynamic instability and intradialytic symptoms; UFR > 13 mL/kg/h associated with increased all-cause and CV mortality (KDOQI 2015; Flythe JE, et al. Kidney Int 2011).
Rapid UF + weight gain + short treatment times → hypotension, myocardial stunning → ↑ morbidity and mortality (observational studies; Assimon & Flythe 2015).
[WEB] Flythe JE, Kimmel SE, Brunelli SM. Kidney Int. 2011;79(2):250-257 (HEMO study post hoc): UFR > 13 vs ≤ 10 mL/kg/h adjusted HR 1.59 all-cause and 1.71 CV mortality; 10–13 associated only in patients with heart failure; spline analysis suggests risk rising above ~10 mL/kg/h. Observational – no RCT. https://pmc.ncbi.nlm.nih.gov/articles/PMC3091945 (""" + ACCESSED + """).
Worked example is a CALCULATION for teaching (2500 / (70 × 4) = 8.93 mL/kg/h). Local practice may use post-dialysis (target) weight in the denominator."""},

    # 26 --------------------------------------------------------------- assessment tools
    {"kind": "table_only", "title": "Tools to assess fluid status",
     "source": "Lindley E, et al. 2011 · Rodriguez HJ, et al. Kidney Int. 2005;68(2):854-861 · Moissl U, et al. Clin J Am Soc Nephrol. 2013;8(9):1575-1582 · Onofriescu M, et al. AJKD 2014",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.6, 3.5, 3.0, 2.95], "row_h": 0.66, "size": 11,
               "rows": [["Method", "What it gives", "Benefits", "Challenges"],
                        ["Clinical evaluation", "Edema, BP, weight, dyspnea, JVP, lung congestion", "Before, during and after every HD", "Subjective; late signs"],
                        ["Relative blood volume (RBV) monitoring", "Real-time hematocrit → % blood volume change; plasma refill", "Non-invasive, real-time, reproducible", "No absolute volume; posture, activity, IV fluids; not for PD"],
                        ["Bioimpedance spectroscopy (BIS)", "Over-hydration (L or %), TBW, ICF/ECF, lean and fat mass", "Non-invasive, quantitative, easy", "Not with pacemakers or artificial joints; device variation"],
                        ["Tracer dilution", "Absolute compartment volumes", "Gold standard, reproducible", "Invasive, costly, research use only"],
                        ["Experimental", "BNP/NT-proBNP, IVC diameter, lung ultrasound", "Prognostic, non-invasive options", "Clinical value not yet established"]]},
     "banner": "RBV guide (published, patient-specific): −3 to −8% in hour 1, then −3% to −6.5%/h; about −16% max by end of 3–4 h",
     "banner_y": 5.5,
     "notes": """
AREP [Water Treatment / 160638–161414].
Clinical evaluation: edema, dyspnea, ↑ body weight, ↑ BP, turgid jugular vein, pulmonary congestion (Lindley E, et al. Technical Problems in Patients on Hemodialysis 2011:185-198).
RBV monitoring: measures multi-wavelength light absorption in blood → real-time hematocrit → calculated relative blood volume and hemoglobin; can probe dry weight by checking plasma refill when UF is turned off (Rodriguez HJ, et al. Kidney Int 2005;68(2):854-861).
RBV targets (banner): as presented by AREP [Water Treatment / 160953] citing Reddan DN (JASN 2005), Rodriguez HJ (KI 2005), Jain SR (Pediatr Nephrol 2001), Goldstein SL (JASN 2003). These are observational/expert-based ranges; "ideal rate of RBV change is patient-specific".
BIS: low-frequency currents pass through ECF only, high-frequency through both; BIS-guided management reported to reduce relative fluid overload and improve BP, arterial stiffness and pulse-wave velocity (Onofriescu M, et al. AJKD 2014;64(1):111-118; Hur E, et al. AJKD 2013;61(6):957-965; Moissl U, et al. CJASN 2013).
FMC's Body Composition Monitor is one BIS device – check product IFU and local approval before recommending specific use; do not imply outcome claims beyond the cited studies.
Experimental: biochemical parameters (BNP, NT-proBNP), IVC diameter (ultrasound), lung ultrasound "comets" (Booth J, et al.; Yilmaz Z, et al.; Weitzel WF, et al. Blood Purif 2015)."""},

    # 27 --------------------------------------------------------------- electrolytes / acid-base
    {"kind": "electrolytes", "title": "Electrolytes and acid–base at a glance",
     "source": "Lippincott. Fluids and Electrolytes. 2006:42-192 · MedlinePlus (chloride, magnesium; accessed Nov 2026) · Barrett KE. Ganong's Review of Medical Physiology. 2016",
     "table": {"w": 6.9, "col_w": [2.2, 2.6, 2.1],
               "rows": [["Electrolyte", "Typical serum range", "Main location"],
                        ["Sodium", "135–145 mmol/L", "ECF"],
                        ["Potassium", "3.5–5.0 mmol/L", "ICF"],
                        ["Calcium", "8.5–10.4 mg/dL", "ECF"],
                        ["Chloride", "98–107 mEq/L", "ECF"],
                        ["Phosphate", "2.5–4.5 mg/dL", "ICF"],
                        ["Magnesium", "1.7–2.2 mg/dL", "ICF"],
                        ["Bicarbonate (buffer)", "Lab-specific", "ECF"]]},
     "ph_head": "pH scale",
     "ph_normal": "Normal blood pH 7.35–7.45",
     "ph_body": ["Acids, bases and proteins (Hb, albumin) buffer body fluids",
                 "Dialysate bicarbonate helps correct metabolic acidosis",
                 "Always use your laboratory's reference ranges"],
     "notes": """
AREP Fluids, Electrolytes, Acids and Bases [Acid Base / 161805, 161830, 161903].
Six major electrolytes contribute to ion balance; electrolytes are found in both intracellular and extracellular compartments.
Ranges for sodium, potassium, calcium and phosphate are copied from AREP (Lippincott and Springhouse. Fluids and Electrolytes 2006:42-192).
SOURCE DISCREPANCIES CORRECTED – NEEDS REVIEW:
 - The AREP screen lists chloride as "Serum 8.5–10.4 mg/dL" (this duplicates the calcium range and is not a chloride range). Replaced with 98–107 mEq/L. [WEB] MedlinePlus: https://medlineplus.gov/ency/article/003485.htm (""" + ACCESSED + """).
 - The AREP screen lists magnesium as 1.8–2.5 mEq/L. Replaced with 1.7–2.2 mg/dL (0.70–0.91 mmol/L). [WEB] MedlinePlus: https://medlineplus.gov/ency/article/003487.htm (""" + ACCESSED + """).
 - "Main location" column: general physiology (Na, Ca, Cl, HCO3 mainly extracellular; K, phosphate, Mg mainly intracellular), consistent with the AREP compartment chart [Water Treatment / 155301].
Normal blood pH 7.35–7.45 (Barrett KE. Ganong's Review of Medical Physiology 2016, ch. 2; DiPiro JT. Pharmacotherapy 2014, ch. 34).
The bicarbonate row intentionally shows "lab-specific"; reference ranges vary between laboratories."""},

    # 28 --------------------------------------------------------------- chapter
    {"kind": "chapter", "title": "4  Safety and quality", "notes": "Section 4: intradialytic complications and best practices that keep patients safe."},

    # 29 --------------------------------------------------------------- complications
    {"kind": "two_cards", "title": "Complications during hemodialysis",
     "source": "Maya ID, Allon M. Am J Kidney Dis. 2008;51(4):702-708 · KDOQI. Am J Kidney Dis. 2006;48 Suppl 1:S2-S90 · Sarkar S, et al. Clinical Dialysis. 2005:257",
     "h": 3.55, "size": 15,
     "cards": [
         ("More common", ["Intradialytic hypotension", "Muscle cramps", "Nausea and vomiting", "Headache", "Chest pain and back pain", "Itching"]),
         ("Less common but serious", ["Disequilibrium syndrome", "Dialyzer reactions", "Hemolysis", "Air embolism", "Exsanguination"]),
     ],
     "banner": "Many complications link back to fluid removal, water quality and access: the earlier sections",
     "notes": """
AREP [Dialysis / 145040] (Maya ID, Allon M. AJKD 2008; KDOQI 2006; Sarkar S, et al. Clinical Dialysis 2005).
Teaching links: hypotension and cramps ↔ UF rate and dry weight (slides 24–25); hemolysis ↔ chloramine/copper in water (slide 10); exsanguination ↔ VND (slides 19–20); air embolism ↔ circuit safety systems (follow machine IFU and alarm response procedures)."""},

    # 30 --------------------------------------------------------------- best practices
    {"kind": "table_only", "title": "Best practices for patient monitoring and safety",
     "source": "Garrick R, et al. Clin J Am Soc Nephrol. 2012;7(4):680-688 · Castner D. Core Curriculum for Nephrology Nursing. 2015:69-166 · Vachharajani TJ. Semin Dial. 2011;24(1):92-96",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.9, 9.15], "row_h": 0.72, "size": 12,
               "rows": [["Risk area", "Key actions"],
                        ["Patient falls", "Monitor orthostatic BP · use fall assessment tools and gait assistance · control clutter · in-floor weight scales"],
                        ["Medication errors", "Follow medication-safety policies · verify prescription, dose and timing · educate staff"],
                        ["Access-related events", "Trained needling teams · catheter access clamps · keep access visible · blood-leak detector · aseptic technique"],
                        ["Dialyzer / machine errors", "Know maintenance procedures · don't rely on alarms alone · understand machine response · never clear an alarm without assessing patient and equipment"],
                        ["Excess blood loss / bleeding", "Blood-leak detector · protect the access · avoid tight clothing and heavy carrying · BP on non-access arm"]]},
     "banner": "Culture of safety: quality assessment and improvement (CQI), a dedicated safety team, focus on identified risks",
     "banner_y": 5.85,
     "notes": """
AREP [Dialysis / 145115–145420] and CQI [vascular access / 152758] (Garrick R, et al. CJASN 2012; Castner D 2015; McCann M, et al. J Ren Care 2008; Maya ID 2008; Vachharajani TJ 2011; Faratro R 2015).
Patient safety is the foundation of high-quality health care. Establish a culture of safety (quality assessment and performance improvement), include a dedicated safety team, focus on identified risk areas and set outcome goals.
CQI for access: performance measures, track access types and complications, establish a database and process.
"Medication errors" row: AREP tab content for this item was not captured in the screenshots; the actions listed are general good practice – NEEDS REVIEW against local policy."""},

    # 31 --------------------------------------------------------------- takeaways
    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Summary of AREP modules and cited guidelines (KDOQI 2015 adequacy; KDOQI 2019 vascular access)",
     "items": [
         ("HD replaces excretion and homeostasis, not hormones", "Start based on symptoms, nutrition, metabolic and volume control, not one GFR value."),
         ("Water quality is patient safety", "120–150 L of dialysate per session; treat and monitor water to the current standard."),
         ("Plan access early and individually", "Educate from CKD 4; ESKD Life-Plan; AVF where appropriate; rope ladder; look-listen-feel every time."),
         ("Manage fluid deliberately", "Dry weight, diet and dialysate sodium; keep UF rate tolerable (> 13 mL/kg/h linked to mortality)."),
         ("Make safety routine", "Target spKt/V 1.4 (min. 1.2); visible access; respond to every alarm by assessing the patient."),
     ],
     "notes": "Summarise and invite questions. Each point maps to one section of the deck; refer participants to the AREP eLearning modules for self-paced review."},

    # 32 --------------------------------------------------------------- references
    {"kind": "references", "title": "References",
     "source": "Primary source: Fresenius Medical Care Advanced Renal Education Program (AREP) eLearning modules (uploaded screenshots, Nov 2026)",
     "refs": [
         "FMC Advanced Renal Education Program. eLearning modules: Introduction to Hemodialysis; Vascular Access; Fluid Management; Fluids, Electrolytes, Acids and Bases (screenshots provided).",
         "KDOQI Clinical Practice Guideline for Hemodialysis Adequacy: 2015 Update. Am J Kidney Dis. 2015;66(5):884-930.",
         "Lok CE, et al. KDOQI Clinical Practice Guideline for Vascular Access: 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164.",
         "Ahmad S, et al. Handbook of Dialysis. 5th ed. 2015:66-88; Ward RA, Ing TS. ibid. 2015:89-98; Daugirdas JT. ibid. 2015:34-65.",
         "Castner D; Payne G. Core Curriculum for Nephrology Nursing, Module 3. 2015.",
         "ISO 23500-3:2024 Preparation and quality management of fluids for haemodialysis – Part 3: Water for haemodialysis.",
         "Rosner M. South Med J. 2005;98(8):785-791.",
         "Blake PG, et al. Kidney Int. 2012;82(6):623-625.",
         "Jindal K, et al. J Am Soc Nephrol. 2006;17(3 Suppl 1):S1-S27.",
         "Schmidli J, et al. Eur J Vasc Endovasc Surg. 2018;55(6):757-818.",
         "Chan MR, et al. Semin Dial. 2014;27(2):210-216.",
         "Muir CA, et al. Clin J Am Soc Nephrol. 2014;9(1):110-119.",
         "National Kidney Foundation. Clinical Update on needle gauge and blood flow. 2016.",
         "Flythe JE, Kimmel SE, Brunelli SM. Kidney Int. 2011;79(2):250-257.",
         "Assimon MM, Flythe JE. Curr Opin Nephrol Hypertens. 2015;24(6):525-530.",
         "KDIGO. Clinical Practice Guideline for the Management of Blood Pressure in CKD. Kidney Int Suppl. 2012;2(5).",
         "Rodriguez HJ, et al. Kidney Int. 2005;68(2):854-861.",
         "Moissl U, et al. Clin J Am Soc Nephrol. 2013;8(9):1575-1582; Onofriescu M, et al. Am J Kidney Dis. 2014;64(1):111-118.",
         "Antlanger M, et al. BMC Nephrol. 2013;14:266.",
         "Garrick R, et al. Clin J Am Soc Nephrol. 2012;7(4):680-688.",
         "Maya ID, Allon M. Am J Kidney Dis. 2008;51(4):702-708.",
         "MedlinePlus. Chloride blood test; Magnesium blood test (accessed 13 Nov 2026).",
     ],
     "notes": "Full URLs for web-verified items are in the speaker notes of the slides where they are used (slides 10, 11, 14, 25, 27)."},
]
