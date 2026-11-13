# -*- coding: utf-8 -*-
"""Shared settings for the eight programme decks (build/program/D*_*.py)."""
from pptx.dml.color import RGBColor

PRESENTER = ["Mr. Mahmoud Elsehemy BSN, MQM", "Clinical Application Specialist Critical Care"]
DATE_LOCATION = "Date | Location"
ACCESSED = "accessed 13 Nov 2026"
ILLUS = "Illustrative training data: not actual patient or facility results"

BLUE = RGBColor(0x00, 0x33, 0xA0)
MID = RGBColor(0x37, 0x7C, 0xB5)
GREY = RGBColor(0xA8, 0xA3, 0x9D)
NAVY = RGBColor(0x07, 0x1B, 0x45)
LIGHTB = RGBColor(0xAB, 0xCB, 0xE5)
RED = RGBColor(0xC0, 0x39, 0x2B)

DISCLAIMER = ("Training material prepared for nurse education. It is NOT an approved Fresenius Medical Care "
              "procedure or policy. Always follow local policies, the physician's prescription and the IFU of the "
              "specific machine, water system and consumables in use. Thresholds marked 'per protocol' are set locally. "
              "Saudi-specific requirements were not available as primary text during preparation; confirm with the "
              "local IPC team and national MOH/SCOT guidance.")

END_NOTES = ("Thank you. Questions and discussion.\n\nSelf-study: FMC Advanced Renal Education Program (AREP) "
             "eLearning modules.\n" + DISCLAIMER)


def refs_slide():
    return {"kind": "references", "title": "References", "refs": "AUTO",
            "source": "Verification status of each source: see Source_Register.md (accessed 13 Nov 2026)",
            "notes": "Full references with links and verification status are in output/program/Source_Register.md. "
                     "Uploaded-file references point to AREP screenshot time-stamps in the speaker notes of each slide."}
