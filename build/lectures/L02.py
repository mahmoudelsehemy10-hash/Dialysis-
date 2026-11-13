# -*- coding: utf-8 -*-
"""Lecture 02 - Day 1: Fluid Assessment, Ultrafiltration Safety, and Intradialytic Hypotension."""
from lectures._common import *  # noqa: F401,F403

SLUG = "Fluid_UF_Safety_IDH"
TITLE = "Fluid Assessment, Ultrafiltration Safety, and Intradialytic Hypotension"
SUBTITLE = "Day 1 · Patient Assessment & Safety · Lecture 02"
FOOTER_TEXT = "L02 Fluid, UF and hypotension"

SLIDES = [
    {"kind": "title", "notes": """
Lecture 02 of the Hemodialysis Nursing Programme (Day 1). 45–60 minutes.
Builds on Lecture 01 (UF goal calculation). Focus: assessing fluid status, keeping ultrafiltration safe, and recognising and managing intradialytic hypotension (IDH).
""" + DISCLAIMER},

    {"kind": "agenda", "title": "Learning objectives",
     "source": "Programme objectives, Lecture 02",
     "items": [
         ("Assess", ["Assess fluid status clinically", "Use RBV and BIS data"]),
         ("Plan", ["Apply dry weight and IDWG", "Keep UF rate tolerable"]),
         ("Respond", ["Recognise IDH early", "Act in the right order"]),
         ("Prevent", ["Reduce IDH risk factors", "Educate on salt and fluid"]),
     ],
     "notes": "Objectives for Lecture 02."},

    {"kind": "compartments", "title": "UF removes plasma water; refill protects blood pressure",
     "source": "AREP Fluid Management · Mulroney S, Myers A. Netter's Essential Physiology. 2016 · Verbalis JG. Brenner and Rector's The Kidney. 2012",
     "chart": {"title": "Total body water ≈ 42 L (example: 70 kg adult, 60%)",
               "series": [("Intracellular fluid (2/3)", 28.0), ("Interstitial fluid (3/4 of ECF)", 10.5), ("Plasma (1/4 of ECF)", 3.5)],
               "max": 42,
               "note": "Educational example (calculated): 70 kg × 60% = 42 L; ICF 28 L, ECF 14 L. Real values vary with age, sex and body fat."},
     "facts": [("~3.5 L", "plasma volume in this example"), ("Refill", "from interstitial space during UF"), ("UFR > refill", "→ blood volume falls → hypotension")],
     "side": {"head": "What this means at the bedside", "body": [
         "UF only takes water from plasma", "Plasma must refill from the tissues",
         "If UF is faster than refill, blood volume and BP fall", "High IDWG + short session = high UFR"]},
     "notes": """
AREP Fluid Management [Water Treatment / 155238, 155920–160005]: dialysis and UF remove fluid from plasma; plasma volume decreases; plasma refills from the intracellular and interstitial spaces.
Chart values are a CALCULATED TEACHING EXAMPLE (70 kg × 0.60 = 42 L; ICF 2/3 = 28 L; ECF 14 L: interstitial 10.5 L, plasma 3.5 L), consistent with the AREP example (28 L ICF, 14 L ECF). Not patient data.
Key teaching point: hypotension occurs when the UF rate exceeds the plasma refill rate."""},

    {"kind": "six_grid", "title": "Clinical signs of fluid status",
     "source": "AREP Fluid Management (Lindley E, et al. Technical Problems in Patients on Hemodialysis. 2011:185-198) · Antlanger M, et al. BMC Nephrol. 2013;14:266",
     "items": [
         ("Weight", "IDWG", "Compare with usual gain and target weight; same scale, same clothing."),
         ("Blood pressure", "↑ or ↓", "High pre-HD BP may mean overload; low BP may mean depletion or drugs."),
         ("Edema", "Legs, sacrum", "Pitting edema suggests extracellular overload (not always)."),
         ("Lungs", "Crackles, SpO₂", "Dyspnea, orthopnea or crackles: possible pulmonary congestion."),
         ("Neck veins", "JVP", "Distended jugular veins suggest volume overload."),
         ("Symptoms", "Cramps, dizziness", "After HD: cramps or fatigue may mean target weight is too low."),
     ],
     "notes": """
AREP [Water Treatment / 160831]: clinical evaluation looks for edema, dyspnea, ↑ body weight, ↑ BP, turgid jugular vein, pulmonary congestion, before, during and after dialysis; helpful in guiding UF rate and dry weight.
Consequences of overload [Water Treatment / 155644]: LVH, hypertension, heart failure, pulmonary edema, ascites, ↑ mortality (Antlanger M, et al. BMC Nephrol 2013;14:266).
Clinical signs are late and non-specific – combine with trends and, where available, device measurements (slide 6)."""},

    {"kind": "levers", "title": "Dry weight is a target that must be re-checked",
     "source": "AREP Fluid Management · KDOQI 2015 · KDIGO BP in CKD 2012",
     "def_head": "Dry weight: extracellular volume at or near normal, but not below normal",
     "def_body": "Sets the UF goal. It changes with nutrition, illness and season: reassess regularly (AREP: at least every 2 weeks) and after hospital stays.",
     "levers": [
         ("Too high", ["Rising pre-HD BP", "Edema, dyspnea", "IDWG seems 'normal' but BP high"]),
         ("Too low", ["Cramps, dizziness late in HD", "Post-HD fatigue, hypotension", "Loss of residual urine"]),
         ("Diet", ["Anuric: fluid ~1.0–1.5 L/day", "Sodium < 2 g/day (KDIGO)", "Salt drives thirst"]),
         ("Dialysate Na", ["Usually 138–140 mEq/L", "High Na: thirst, ↑ IDWG", "Per physician order"]),
     ],
     "banner": "Report patterns to the physician: the target weight is a prescription, not a nursing decision",
     "notes": """
AREP [Water Treatment / 155714]: at dry weight the extracellular volume is at or near normal but not less than normal; may vary between sessions; monitor regularly (at least every 2 weeks); often determined by trial and error.
Diet [155835–155900]: anuric patients generally 1.0–1.5 L/day; KDIGO: < 2 g sodium/day; KDOQI: reduce dietary sodium.
Dialysate sodium [160302]: KDOQI recommends against high dialysate sodium; most patients 138–140 mEq/L.
"Too high / too low" signs are clinical clues, not diagnostic criteria."""},

    {"kind": "ufr", "title": "Ultrafiltration rate: keep it tolerable",
     "source": "Flythe JE, et al. Kidney Int. 2011;79(2):250-257 · Assimon MM, Flythe JE. Curr Opin Nephrol Hypertens. 2015;24(6):525-530",
     "formula": "UF goal (mL) ÷ [weight (kg) × time (h)]",
     "example": {"head": "Worked example (educational)", "body": [
         "UF goal 3.2 L, weight 64 kg",
         "4 h: 3,200 ÷ (64 × 4) = 12.5 mL/kg/h",
         "3.5 h: 3,200 ÷ (64 × 3.5) = 14.3 mL/kg/h",
         ("Shortening the session raises the UFR above 13", {"bold": True, "color": NAVY, "space_after": 4})]},
     "zones_head": "Observational data (HEMO study)",
     "zones": [("≤ 10", "Reference group"),
               ("10–13", "Higher risk in patients with heart failure"),
               ("> 13", "↑ all-cause (HR 1.59) and CV mortality (HR 1.71)")],
     "balance": ["Too slow → fluid stays, overload persists",
                 "Too fast → hypotension, cramps, myocardial stunning",
                 "Association only: no randomised trial yet"],
     "notes": """
[WEB] Flythe JE, Kimmel SE, Brunelli SM. Kidney Int. 2011;79(2):250-257 – HEMO post hoc: UFR > 13 vs ≤ 10 mL/kg/h adjusted HR 1.59 (all-cause) and 1.71 (CV); 10–13 associated only with heart failure; risk began rising above ~10 mL/kg/h. https://pmc.ncbi.nlm.nih.gov/articles/PMC3091945 (""" + ACCESSED + """).
AREP [Water Treatment / 160042–160218]: rapid UF + weight gain + short treatment times → hypotension, myocardial stunning, hypovolemia; ↑ morbidity and mortality (observational).
Worked example is a CALCULATION for teaching."""},

    {"kind": "table_only", "title": "Tools that support fluid decisions",
     "source": "AREP Fluid Management · Rodriguez HJ, et al. Kidney Int. 2005;68(2):854-861 · Moissl U, et al. Clin J Am Soc Nephrol. 2013;8(9):1575-1582",
     "y": 1.45,
     "table": {"w": 12.05, "col_w": [2.7, 3.6, 2.9, 2.85], "row_h": 0.78, "size": 12,
               "rows": [["Tool", "What it shows", "Nursing use", "Limits"],
                        ["Clinical assessment", "Edema, lungs, BP, weight, symptoms", "Every session, before, during, after", "Late, subjective"],
                        ["Relative blood volume (RBV)", "Real-time % change in blood volume", "Spot steep falls early; check refill", "No absolute volume; posture, IV fluids"],
                        ["Bioimpedance (BIS)", "Over-hydration in litres, body composition", "Support target weight review", "Not with pacemakers, metal joints"],
                        ["Lung ultrasound, biomarkers", "Lung water; BNP/NT-proBNP", "Physician-led", "Value still being defined"]]},
     "banner": "Published RBV guide (patient-specific): −3 to −8% in hour 1, then −3 to −6.5%/h; about −16% max at end",
     "banner_y": 5.55,
     "notes": """
AREP [Water Treatment / 160905–161414].
RBV: measures hematocrit optically in the blood line → calculated % change in blood volume; a steep fall warns of impending hypotension; plateau after UF-off suggests plasma refill (Rodriguez HJ, et al. Kidney Int 2005).
RBV figures in the banner as presented by AREP [160953] citing Reddan DN (JASN 2005), Rodriguez HJ (KI 2005), Jain SR (Pediatr Nephrol 2001), Goldstein SL (JASN 2003) – observational; "ideal rate of RBV change is patient-specific".
BIS: low-frequency currents pass through ECF only; BIS-guided management reduced relative fluid overload in studies (Moissl U, et al. CJASN 2013; Onofriescu M, et al. AJKD 2014). Device availability and approval vary – follow product IFU; no outcome claims beyond the cited studies."""},

    {"kind": "stat_cards", "title": "Intradialytic hypotension (IDH): what counts",
     "source": "K/DOQI Cardiovascular Disease in Dialysis Patients. Am J Kidney Dis. 2005;45(4 Suppl 3) · Kooman J, et al. Nephrol Dial Transplant. 2007;22(Suppl 2):ii22-44",
     "stats": [("≥ 20 mmHg", "fall in systolic BP"), ("≥ 10 mmHg", "fall in mean arterial pressure"), ("+ symptoms", "or need for intervention"), ("< 90 mmHg", "nadir SBP: strongest link with mortality")],
     "cards": [
         ("Early warning signs", ["Yawning, sighing, restlessness", "Dizziness, blurred vision", "Nausea, vomiting, cramps", "Sweating, pallor, chest pain"]),
         ("Risk factors", ["High IDWG / high UFR", "Low or wrong target weight", "Antihypertensives, meals during HD", "Heart disease, diabetes, older age"]),
         ("Why it matters", ["Organ ischemia (heart, brain, gut)", "Incomplete treatment and UF", "Loss of residual kidney function", "Associated with higher mortality"]),
     ],
     "notes": """
[WEB] KDOQI 2005 cardiovascular guideline definition: decrease in SBP ≥ 20 mmHg or MAP ≥ 10 mmHg associated with symptoms (or need for intervention). Definitions vary (e.g. UK Renal Association 2011); some reviews note low nadir SBP (< 90 mmHg) correlates more strongly with mortality than the size of the fall. Source review: https://academic.oup.com/ckj/article/13/6/981/5868598 (Clin Kidney J 2020) (""" + ACCESSED + """).
Symptoms and risk factors: EBPG on haemodynamic instability (Kooman J, et al. NDT 2007;22 Suppl 2:ii22-44); Handbook of Dialysis 2015.
Frequency figures are not shown because they vary widely with the definition used."""},

    {"kind": "steps", "title": "Respond to IDH in this order",
     "source": "Kooman J, et al. EBPG. Nephrol Dial Transplant. 2007;22(Suppl 2):ii22-44 · Handbook of Dialysis. 5th ed. 2015 · Local protocol",
     "steps": [
         ("Recognise and check", "Symptoms → measure BP and pulse now; check RBV trend if available"),
         ("Position", "Lay flat / raise legs (Trendelenburg per protocol); airway and SpO₂"),
         ("Reduce or stop UF", "Pause UF; consider lower blood flow only if protocol allows"),
         ("Restore volume", "Saline bolus per standing order (e.g. 100–250 mL); O₂ if hypoxic"),
         ("Call and reassess", "Notify physician if no quick response, chest pain or reduced consciousness"),
         ("Document and review", "BP trend, actions, fluid given; review target weight and UFR"),
     ],
     "side": {"head": "Do not", "fill": "navy", "body": [
         "Leave a symptomatic patient alone", "Restart full UF before BP recovers", "Ignore chest pain: treat as cardiac",
         "Forget glucose in diabetic patients", "Add the saline given to the UF goal without an order"]},
     "notes": """
Typical stepwise IDH management (EBPG 2007; Handbook of Dialysis 2015; unit protocol): recognise, measure, position, reduce/stop UF, give saline bolus per standing order, oxygen if hypoxic, notify physician, reassess and document.
The saline volume (e.g. 100–250 mL) is an EXAMPLE; volumes and the decision to reduce blood flow must follow the local standing order and physician prescription.
Evidence for many IDH interventions is limited; reviews describe the evidence base as thin – protocols are consensus-based. Chest pain, arrhythmia or reduced consciousness → treat as emergency (Lecture 07)."""},

    {"kind": "two_cards", "title": "Prevent the next episode",
     "source": "Kooman J, et al. EBPG. Nephrol Dial Transplant. 2007;22(Suppl 2):ii22-44 · KDOQI 2015 · Flythe JE, et al. Kidney Int. 2011",
     "h": 3.75,
     "cards": [
         ("Patient-related", ["Limit salt to reduce thirst and IDWG", "Review antihypertensive timing on HD days", "Avoid large meals during HD if prone",
                              "Treat anemia; review cardiac status", "Educate: report dizziness early"]),
         ("Prescription-related (physician)", ["Reassess target weight", "Longer or extra sessions to lower UFR", "Cooler dialysate (e.g. 0.5 °C below body temperature)",
                                               "Avoid low dialysate sodium", "Consider RBV-guided monitoring"]),
     ],
     "banner": "Repeated IDH is a signal: report the pattern, not just the single event",
     "notes": """
Prevention strategies per EBPG 2007 haemodynamic instability guideline: reassess dry weight, limit IDWG (salt restriction), avoid food intake during dialysis in prone patients, review antihypertensives, cool dialysate (e.g. dialysate temperature around 0.5 °C below body temperature / isothermic dialysis), longer or more frequent sessions to lower UFR, avoid low dialysate sodium.
Prescription changes are physician decisions; nurses identify patterns and communicate them."""},

    {"kind": "case", "title": "Case: dizzy in the third hour",
     "source": "Fictional teaching case",
     "case": [
         "Mr C, 72 years, heart failure. Target weight 68.0 kg; pre-weight 71.5 kg.",
         "Prescribed 3.5 h; UF goal 3.5 L. Took his antihypertensive this morning.",
         "Hour 3: yawning, nauseated, BP 84/48 (pre 142/80), pulse 108. RBV −14%.",
         "He says his legs are cramping."],
     "questions": [
         "What is his UFR? Is it in the risk zone?",
         "List your first four actions in order.",
         "When do you call the physician urgently?",
         "What would you recommend for his next sessions?"],
     "notes": """
Suggested answers (educational):
1. UFR = 3500 ÷ (68 × 3.5) = 14.7 mL/kg/h → above 13 mL/kg/h; with heart failure, risk already rises above 10.
2. Check BP/symptoms → lay flat, legs up → stop UF → saline bolus per standing order; monitor BP, O₂ if needed.
3. If no prompt response, chest pain, arrhythmia, reduced consciousness or SpO₂ falling.
4. Report: high UFR, antihypertensive timing, possible target weight review, longer/extra session, salt/fluid education."""},

    {"kind": "takeaways", "title": "Key takeaways",
     "source": "Lecture 02 summary",
     "items": [
         ("UF removes plasma water", "Hypotension happens when UF is faster than refill."),
         ("Assess fluid status with several signs", "Weight, BP, edema, lungs, JVP, symptoms and device data."),
         ("Keep UFR tolerable", "Above 13 mL/kg/h is linked to mortality; risk rises above 10 in heart failure."),
         ("Respond to IDH in order", "Check, position, stop UF, restore volume, call, document."),
         ("Prevent recurrence", "Report patterns: target weight, UFR, medicines, salt, dialysate temperature."),
     ],
     "notes": "Summarise and link to Day 2 (vascular access and infection control)."},

    {"kind": "references", "title": "References",
     "source": "Web-verified items marked in speaker notes; accessed 13 Nov 2026",
     "refs": [R["kdoqi_cv"], R["ebpg_hd"], R["flythe"], "Assimon MM, Flythe JE. Curr Opin Nephrol Hypertens. 2015;24(6):525-530.",
              R["kdoqi_adeq"], "KDIGO Clinical Practice Guideline for the Management of Blood Pressure in CKD. Kidney Int Suppl. 2012;2(5).",
              "Rodriguez HJ, et al. Kidney Int. 2005;68(2):854-861.", "Moissl U, et al. Clin J Am Soc Nephrol. 2013;8(9):1575-1582.",
              "Antlanger M, et al. BMC Nephrol. 2013;14:266.", "Review of IDH definitions. Clin Kidney J. 2020;13(6):981-993.",
              R["handbook"], R["arep"]],
     "notes": "References for Lecture 02."},
]
