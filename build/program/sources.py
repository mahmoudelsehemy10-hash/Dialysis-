# -*- coding: utf-8 -*-
"""
Source register for the 4-day hemodialysis nursing programme.

Each entry: id -> dict(cite, url, kind, status)
  kind   : Uploaded | Guideline | Standard | Regulation | Peer-reviewed | Textbook | Secondary | Tool
  status : how the item was verified in this build (13 Nov 2026)
     "Uploaded"          - read directly from the uploaded AREP screenshots
     "Web-verified"      - key statements confirmed via web search of the source or summaries citing it
     "Secondary only"    - only secondary summaries were reachable (primary text blocked or paywalled)
     "Not accessed"      - cited from established textbook knowledge; must be checked by reviewer
build_deck.py writes this register to output/program/Source_Register.csv and .md, with the lectures
that cite each source.
"""

S = {
    # ---- uploaded material -------------------------------------------------------------------------
    "AREP_HD": dict(cite="Fresenius Medical Care. Advanced Renal Education Program (AREP): Introduction to Hemodialysis (uploaded screenshots, Dialysis.zip).",
                    url="(uploaded file)", kind="Uploaded", status="Uploaded"),
    "AREP_VA": dict(cite="Fresenius Medical Care. AREP: Vascular Access module (uploaded screenshots, vascular access.zip).",
                    url="(uploaded file)", kind="Uploaded", status="Uploaded"),
    "AREP_FM": dict(cite="Fresenius Medical Care. AREP: Fluid Management / Fluid Overload module (uploaded screenshots, 'Water Treatment.zip').",
                    url="(uploaded file)", kind="Uploaded", status="Uploaded"),
    "AREP_AB": dict(cite="Fresenius Medical Care. AREP: Fluids, Electrolytes, Acids and Bases (uploaded screenshots, Acid Base.zip).",
                    url="(uploaded file)", kind="Uploaded", status="Uploaded"),
    "FMC_IFU": dict(cite="Fresenius Medical Care. Operator's manual / Instructions for Use of the hemodialysis machine, water treatment system, dialyzers, catheters and lock solutions in local use (not uploaded).",
                    url="(local document)", kind="Tool", status="Not accessed"),
    # ---- guidelines ----------------------------------------------------------------------------------
    "KDOQI_ADEQ15": dict(cite="National Kidney Foundation. KDOQI Clinical Practice Guideline for Hemodialysis Adequacy: 2015 Update. Am J Kidney Dis. 2015;66(5):884-930.",
                         url="https://pubmed.ncbi.nlm.nih.gov/26498416/", kind="Guideline", status="Web-verified"),
    "KDOQI_ADEQ06": dict(cite="National Kidney Foundation. KDOQI Clinical Practice Guidelines for Hemodialysis Adequacy, 2006 Update (incl. CPR on blood sampling). Am J Kidney Dis. 2006;48(Suppl 1):S2-S90.",
                         url="https://www.ajkd.org/issue/S0272-6386(06)X0209-2", kind="Guideline", status="Secondary only"),
    "KDOQI_VA19": dict(cite="Lok CE, et al. KDOQI Clinical Practice Guideline for Vascular Access: 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164.",
                       url="https://www.ajkd.org/article/S0272-6386(19)31137-0/fulltext", kind="Guideline", status="Web-verified"),
    "KDOQI_CV05": dict(cite="K/DOQI Clinical Practice Guidelines for Cardiovascular Disease in Dialysis Patients. Am J Kidney Dis. 2005;45(4 Suppl 3):S1-S153.",
                       url="https://academic.oup.com/ckj/article/13/6/981/5868598", kind="Guideline", status="Secondary only"),
    "EBPG_HI07": dict(cite="Kooman J, et al. EBPG guideline on haemodynamic instability. Nephrol Dial Transplant. 2007;22(Suppl 2):ii22-ii44.",
                      url="https://academic.oup.com/ndt/article/22/suppl_2/ii22/1883925", kind="Guideline", status="Not accessed"),
    "KDIGO_HCV18": dict(cite="KDIGO 2018 Clinical Practice Guideline for the Prevention, Diagnosis, Evaluation, and Treatment of Hepatitis C in CKD. Kidney Int Suppl. 2018;8(3):91-165 (Chapter 3 unchanged in the 2022 update).",
                        url="https://pmc.ncbi.nlm.nih.gov/articles/PMC6336217", kind="Guideline", status="Web-verified"),
    "KDIGO_BP12": dict(cite="KDIGO Clinical Practice Guideline for the Management of Blood Pressure in CKD. Kidney Int Suppl. 2012;2(5):337-414.",
                       url="https://kdigo.org/guidelines/", kind="Guideline", status="Not accessed"),
    "CDC_2001": dict(cite="CDC. Recommendations for preventing transmission of infections among chronic hemodialysis patients. MMWR Recomm Rep. 2001;50(RR-5):1-43.",
                     url="https://www.cdc.gov/mmwr/PDF/rr/rr5005.pdf", kind="Guideline", status="Secondary only"),
    "CDC_CORE": dict(cite="CDC. Dialysis Safety: Core Interventions for Dialysis Bloodstream Infection Prevention.",
                     url="https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/", kind="Tool", status="Secondary only"),
    "CDC_INJ": dict(cite="CDC. Hemodialysis Injection Safety Checklist and Observation Tool.",
                    url="https://www.cdc.gov/dialysis-safety/media/pdfs/Hemodialysis-InjectionSafety-Checklist-P.pdf", kind="Tool", status="Web-verified"),
    "CDC_HBVVAC": dict(cite="CDC. Guidelines for vaccinating kidney dialysis patients and patients with chronic kidney disease (summarised from ACIP recommendations).",
                       url="https://stacks.cdc.gov/view/cdc/143156/cdc_143156_DS1.pdf", kind="Guideline", status="Web-verified"),
    "NHSN": dict(cite="CDC NHSN. Dialysis Event Surveillance Protocol (January 2026) and FAQ on Dialysis Event Reporting.",
                 url="https://www.cdc.gov/nhsn/faqs/dialysis/faq-dialysis-event-reporting.html", kind="Tool", status="Web-verified"),
    "WHO_5M": dict(cite="World Health Organization. WHO Guidelines on Hand Hygiene in Health Care / My 5 Moments for Hand Hygiene. 2009.",
                   url="https://www.who.int/publications/i/item/9789241597906", kind="Guideline", status="Not accessed"),
    # ---- standards & regulation ---------------------------------------------------------------------
    "ISO23500_3": dict(cite="ISO 23500-3:2024 Preparation and quality management of fluids for haemodialysis and related therapies - Part 3: Water for haemodialysis and related therapies.",
                       url="https://standards.iteh.ai/catalog/standards/iso/89c28b50-0248-41d3-afb0-73d742f36334/iso-23500-3-2024", kind="Standard", status="Secondary only"),
    "ISO23500_5": dict(cite="ISO 23500-5:2024 (EN ISO 23500-5:2024) Part 5: Quality of dialysis fluid for haemodialysis and related therapies.",
                       url="https://standards.iteh.ai/catalog/standards/cen/c64b6ed3-ba3e-4f85-8f6d-5ac00fda6a35/en-iso-23500-5-2024", kind="Standard", status="Web-verified"),
    "CFR494": dict(cite="US CMS. ESRD Conditions for Coverage, 42 CFR Part 494 (§494.30 infection control, §494.40 water and dialysate quality incl. AAMI RD52:2004 §6.2.5, §494.110 QAPI, §494.170 records).",
                   url="https://www.gpo.gov/fdsys/pkg/CFR-2014-title42-vol5/pdf/CFR-2014-title42-vol5-sec494-40.pdf", kind="Regulation", status="Web-verified"),
    "CMS_RO": dict(cite="US CMS. S&C 15-44: Portable reverse osmosis units in ESRD facilities.",
                   url="https://www.cms.gov/medicare/provider-enrollment-and-certification/surveycertificationgeninfo/downloads/survey-and-cert-letter-15-44.pdf", kind="Regulation", status="Web-verified"),
    "SA_MOH_IPC": dict(cite="Saudi Ministry of Health, General Directorate of Infection Prevention and Control. National Guide for Auditors - Infection Control, Version 5 (Element D-1 Hemodialysis Unit).",
                       url="https://www.moh.gov.sa/Ministry/Rules/Documents/National-Guide-Auditors-Infection-Control-Version-5.pdf", kind="Regulation", status="Secondary only"),
    "SA_HIV14": dict(cite="Saudi HIV outbreak investigation in a hemodialysis unit (Jizan), describing the national 'Dialysis Safety' guideline requirement to test new and transferred patients for HIV, HCV and HBV. PMC4144264.",
                     url="https://pmc.ncbi.nlm.nih.gov/articles/PMC4144264", kind="Peer-reviewed", status="Secondary only"),
    # ---- peer-reviewed / textbooks -------------------------------------------------------------------
    "FLYTHE11": dict(cite="Flythe JE, Kimmel SE, Brunelli SM. Rapid fluid removal during dialysis is associated with cardiovascular morbidity and mortality. Kidney Int. 2011;79(2):250-257.",
                     url="https://pmc.ncbi.nlm.nih.gov/articles/PMC3091945", kind="Peer-reviewed", status="Web-verified"),
    "IDH_REVIEW": dict(cite="Review of intradialytic hypotension definitions and outcomes. Clin Kidney J. 2020;13(6):981-993.",
                       url="https://academic.oup.com/ckj/article/13/6/981/5868598", kind="Peer-reviewed", status="Web-verified"),
    "DAUG93": dict(cite="Daugirdas JT. Second generation logarithmic estimates of single-pool variable volume Kt/V. J Am Soc Nephrol. 1993;4(5):1205-1213.",
                   url="https://open-exam-prep.com/study-guides/bonent-chn/principles-dialysis-adequacy/dialysis-adequacy", kind="Peer-reviewed", status="Web-verified"),
    "KHI_EKTV": dict(cite="Kidney Health Initiative (ASN). Data standard: single-pool and equilibrated Kt/V calculation.",
                     url="https://khi.asn-online.org/uploads/Single_Pool_Kt-V.pdf", kind="Tool", status="Web-verified"),
    "SAHA17": dict(cite="Saha M, Allon M. Diagnosis, treatment, and prevention of hemodialysis emergencies. Clin J Am Soc Nephrol. 2017;12(2):357-369.",
                   url="https://pmc.ncbi.nlm.nih.gov/articles/PMC5293333", kind="Peer-reviewed", status="Secondary only"),
    "GREENBERG21": dict(cite="Greenberg KI, Choi MJ. Hemodialysis emergencies: Core Curriculum 2021. Am J Kidney Dis. 2021;77(5):796-809.",
                        url="https://pubmed.ncbi.nlm.nih.gov/33771393/", kind="Peer-reviewed", status="Secondary only"),
    "HEMOLYSIS14": dict(cite="Hemolysis as a rare but potentially life-threatening complication of hemodialysis (case report and review). BMC Res Notes. 2014;7:475.",
                        url="https://bmcresnotes.biomedcentral.com/articles/10.1186/1756-0500-7-475", kind="Peer-reviewed", status="Web-verified"),
    "DDS19": dict(cite="Mistry K. Dialysis disequilibrium syndrome: prevention and management. Int J Nephrol Renovasc Dis. 2019;12:69-77.",
                  url="https://pmc.ncbi.nlm.nih.gov/articles/PMC6503314", kind="Peer-reviewed", status="Web-verified"),
    "PYRO_OTT": dict(cite="The Ottawa Hospital. Management of a suspected pyrogenic reaction (hemodialysis clinical guideline, Feb 2013).",
                     url="https://kcr.csnscn.ca/search-by-keyword/hemodialysis/clinical-guidelines/infections/472-ottawa-management-of-a-suspected-pyrogenic-reaction-feb-2013/file", kind="Guideline", status="Secondary only"),
    "VA_CHAN14": dict(cite="Chan MR, et al. Buttonhole vs rope-ladder cannulation: primary patency. Semin Dial. 2014;27(2):210-216.",
                      url="(cited in AREP Vascular Access)", kind="Peer-reviewed", status="Uploaded"),
    "VA_MUIR14": dict(cite="Muir CA, et al. Buttonhole cannulation and clinical outcomes in a home hemodialysis cohort and systematic review. Clin J Am Soc Nephrol. 2014;9(1):110-119.",
                      url="(cited in AREP Vascular Access)", kind="Peer-reviewed", status="Uploaded"),
    "NKF_NEEDLE": dict(cite="National Kidney Foundation. Clinical Update 2016: needle gauge and blood flow rate (table as reproduced in AREP).",
                       url="(cited in AREP Vascular Access)", kind="Guideline", status="Uploaded"),
    "GARRICK12": dict(cite="Garrick R, et al. Patient safety in hemodialysis. Clin J Am Soc Nephrol. 2012;7(4):680-688.",
                      url="(cited in AREP Introduction to Hemodialysis)", kind="Peer-reviewed", status="Uploaded"),
    "HANDBOOK": dict(cite="Daugirdas JT, Blake PG, Ing TS (eds). Handbook of Dialysis. 5th ed. Wolters Kluwer; 2015.",
                     url="(textbook)", kind="Textbook", status="Not accessed"),
    "ANNA": dict(cite="Counts CS (ed). Core Curriculum for Nephrology Nursing. 6th ed. American Nephrology Nurses Association; 2015.",
                 url="(textbook)", kind="Textbook", status="Not accessed"),
    "IHI_SBAR": dict(cite="Institute for Healthcare Improvement. SBAR Tool: Situation-Background-Assessment-Recommendation; Model for Improvement (PDSA).",
                     url="https://www.ihi.org/resources/tools/sbar-tool-situation-background-assessment-recommendation", kind="Tool", status="Not accessed"),
    "MEDLINE_LAB": dict(cite="MedlinePlus Medical Encyclopedia. Chloride blood test; Magnesium blood test.",
                        url="https://medlineplus.gov/ency/article/003485.htm", kind="Secondary", status="Web-verified"),
    "WATER_SUMMARY": dict(cite="AAMI/ISO water quality testing summaries (study guide and laboratory reference tables) used to cross-check limits and testing frequency.",
                          url="https://open-exam-prep.com/study-guides/bonent-cht/water-treatment-and-dialysate/aami-iso-water-quality-standards-testing", kind="Secondary", status="Secondary only"),
    "AIR_SUMMARY": dict(cite="Hemodialysis emergency study guides and case reports on air embolism positioning and management (conflicting positioning advice noted).",
                        url="https://open-exam-prep.com/study-guides/cdn/hemodialysis-complications/dialyzer-reactions-and-air-embolism", kind="Secondary", status="Secondary only"),
}
