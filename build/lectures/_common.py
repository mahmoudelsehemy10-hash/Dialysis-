# -*- coding: utf-8 -*-
"""Shared settings for the 8-lecture hemodialysis nursing programme decks."""
from pptx.dml.color import RGBColor

PRESENTER = ["Mr. Mahmoud Elsehemy BSN, MQM", "Clinical Application Specialist Critical Care"]
DATE_LOCATION = "Date | Location"
ACCESSED = "accessed 13 Nov 2026"
PROGRAMME = "Hemodialysis Nursing Programme"

BLUE = RGBColor(0x00, 0x33, 0xA0)
MID = RGBColor(0x37, 0x7C, 0xB5)
GREY = RGBColor(0xA8, 0xA3, 0x9D)
NAVY = RGBColor(0x07, 0x1B, 0x45)

DISCLAIMER = ("Educational material. Always follow local policies and procedures, the physician's "
              "prescription and the Instructions for Use (IFU) of the specific machine, water system "
              "and consumables in use. Thresholds marked 'per protocol' must be set locally.")

END_NOTES = ("Thank you. Questions and discussion.\n\nSelf-study: FMC Advanced Renal Education Program "
             "(AREP) eLearning modules.\n" + DISCLAIMER)

# Short reference strings reused across lectures
R = {
    "kdoqi_adeq": "KDOQI Clinical Practice Guideline for Hemodialysis Adequacy: 2015 Update. Am J Kidney Dis. 2015;66(5):884-930.",
    "kdoqi_va": "Lok CE, et al. KDOQI Clinical Practice Guideline for Vascular Access: 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164.",
    "kdoqi_cv": "K/DOQI Clinical Practice Guidelines for Cardiovascular Disease in Dialysis Patients. Am J Kidney Dis. 2005;45(4 Suppl 3):S1-S153.",
    "ebpg_hd": "Kooman J, et al. EBPG guideline on haemodynamic instability. Nephrol Dial Transplant. 2007;22(Suppl 2):ii22-ii44.",
    "cdc_2001": "CDC. Recommendations for preventing transmission of infections among chronic hemodialysis patients. MMWR Recomm Rep. 2001;50(RR-5):1-43.",
    "cdc_core": "CDC. Core Interventions for Dialysis Bloodstream Infection Prevention (Dialysis Safety). cdc.gov/dialysis-safety.",
    "nhsn": "CDC NHSN. Dialysis Event Surveillance Protocol (January 2026).",
    "cms_cfc": "CMS. ESRD Conditions for Coverage, 42 CFR Part 494 (incl. §494.30 infection control, §494.40 water and dialysate quality, §494.80 patient assessment).",
    "iso23500": "ISO 23500 series (2024): Preparation and quality management of fluids for haemodialysis and related therapies (Parts 1-5).",
    "saha": "Saha M, Allon M. Diagnosis, treatment, and prevention of hemodialysis emergencies. Clin J Am Soc Nephrol. 2017;12(2):357-369.",
    "greenberg": "Greenberg KI, Choi MJ. Hemodialysis emergencies: Core Curriculum 2021. Am J Kidney Dis. 2021;77(5):796-809.",
    "flythe": "Flythe JE, Kimmel SE, Brunelli SM. Rapid fluid removal during dialysis is associated with cardiovascular morbidity and mortality. Kidney Int. 2011;79(2):250-257.",
    "handbook": "Daugirdas JT, Blake PG, Ing TS (eds). Handbook of Dialysis. 5th ed. Wolters Kluwer; 2015.",
    "anna": "Counts CS (ed). Core Curriculum for Nephrology Nursing. 6th ed. ANNA; 2015.",
    "arep": "Fresenius Medical Care. Advanced Renal Education Program (AREP) eLearning modules (screenshots provided).",
    "daug_ktv": "Daugirdas JT. Second generation logarithmic estimates of single-pool variable volume Kt/V. J Am Soc Nephrol. 1993;4(5):1205-1213.",
    "garrick": "Garrick R, et al. Patient safety in hemodialysis. Clin J Am Soc Nephrol. 2012;7(4):680-688.",
    "ifu": "Fresenius Medical Care. Operator's manual / IFU of the hemodialysis machine and water treatment system in use (local version).",
}
