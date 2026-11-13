#!/usr/bin/env python3
"""
Build "Hemodialysis Fundamentals" on the Fresenius Medical Care template.

The deck is generated from the uploaded FMC template deck so that the real
slide master, layouts, theme (FMC 02 colours, Verdana), logo and footer bar
are kept. All existing template slides are removed except the photo title
slide (slide 1) and the photo "Thank you" slide (slide 42), which are reused.
Content slides use the template layouts "1_Only title" (content) and
"1_Chapter" (section divider). Text, tables and charts are native, editable
PowerPoint objects. Three illustrations are cropped from the uploaded AREP
module screenshots.

Usage (from the repository root):
    python3 build/build_deck.py
    python3 build/build_deck.py --template "other.pptx" --out output/deck.pptx

Requires: python-pptx, Pillow.  Original input files are never modified.
"""
import argparse
import copy
import io
import os
import zipfile

from PIL import Image
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

FOOTER_TEXT = ""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- FMC template palette (theme "FMC 02") ---------------------------------
NAVY = RGBColor(0x07, 0x1B, 0x45)    # accent1
BLUE = RGBColor(0x00, 0x33, 0xA0)    # dk2 / accent2
MID = RGBColor(0x37, 0x7C, 0xB5)     # accent6
LIGHT = RGBColor(0xAB, 0xCB, 0xE5)   # accent5
SAND = RGBColor(0xEE, 0xED, 0xEB)    # lt2
GREY = RGBColor(0xA8, 0xA3, 0x9D)    # accent3
GREY_L = RGBColor(0xDC, 0xDA, 0xD8)  # accent4
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x1E, 0x1E, 0x1E)
TINT = RGBColor(0xE8, 0xF0, 0xF8)
GREY_TXT = RGBColor(0x5F, 0x5B, 0x57)  # darker tone of accent3 for small text    # very light blue tint for cards
FILLS = {"navy": NAVY, "blue": BLUE, "mid": MID, "light": LIGHT, "sand": SAND,
         "grey": GREY, "greyl": GREY_L, "white": WHITE, "tint": TINT}

CONTENT_LAYOUT = "1_Only title"
CHAPTER_LAYOUT = "1_Chapter"
KEEP_TITLE_IDX = 0     # slide 1 of template: photo title slide
KEEP_END_IDX = 41      # slide 42 of template: photo "Thank you" slide


# ---------------------------------------------------------------- helpers ---
def layout(prs, name):
    for lay in prs.slide_masters[0].slide_layouts:
        if lay.name == name:
            return lay
    raise KeyError(name)


def delete_slides(prs, keep):
    sldIdLst = prs.slides._sldIdLst
    for i, sldId in reversed(list(enumerate(list(sldIdLst)))):
        if i in keep:
            continue
        prs.part.drop_rel(sldId.rId)
        sldIdLst.remove(sldId)


def set_text_keep_format(shape, lines):
    """Replace text in a shape, keeping the first run's formatting per paragraph."""
    txBody = shape.text_frame._txBody
    paras = txBody.findall(qn("a:p"))
    proto = paras[0]
    for p in paras:
        txBody.remove(p)
    for i, line in enumerate(lines):
        src = paras[i] if i < len(paras) else proto
        p = copy.deepcopy(src)
        runs = p.findall(qn("a:r"))
        for r in runs[1:]:
            p.remove(r)
        for br in p.findall(qn("a:br")):
            p.remove(br)
        if runs:
            runs[0].find(qn("a:t")).text = line
        txBody.append(p)


def set_source(ph, text):
    """Source line in the layout's reference placeholder: small, grey, no bullet."""
    tf = ph.text_frame
    tf.text = text
    tf.word_wrap = True
    p = tf.paragraphs[0]
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", "0"); pPr.set("indent", "0")
    pPr.append(pPr.makeelement(qn("a:buNone"), {}))
    for r in p.runs:
        r.font.size = Pt(9)
        r.font.color.rgb = GREY_TXT


def add_footer(slide, lay):
    """Copy footer + slide-number placeholders from the layout onto the slide."""
    for ph in lay.placeholders:
        t = ph.placeholder_format.type
        tname = str(t).split(".")[-1].split(" ")[0]
        if tname in ("SLIDE_NUMBER", "FOOTER"):
            el = copy.deepcopy(ph._element)
            slide.shapes._spTree.append(el)
            if tname == "FOOTER":
                for t_el in el.iter(qn("a:t")):
                    t_el.text = ""
                ts = list(el.iter(qn("a:t")))
                if ts:
                    ts[0].text = FOOTER_TEXT


def tb(slide, x, y, w, h, paras, size=14, color=INK, bold=False, align=PP_ALIGN.LEFT,
       anchor=MSO_ANCHOR.TOP, margin=0.05, name=None, bullet=False, space_after=4):
    """Text box. paras: list of str or (str, dict) where dict may set size/bold/color/level/bullet."""
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(margin))
    if isinstance(paras, str):
        paras = [paras]
    for i, item in enumerate(paras):
        text, o = (item, {}) if isinstance(item, str) else item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = o.get("align", align)
        p.space_after = Pt(o.get("space_after", space_after))
        use_bullet = o.get("bullet", bullet)
        lvl = o.get("level", 0)
        if use_bullet:
            _bullet(p, lvl, o.get("bullet_color", BLUE))
        run = p.add_run()
        run.text = text
        f = run.font
        f.size = Pt(o.get("size", size))
        f.bold = o.get("bold", bold)
        f.italic = o.get("italic", False)
        f.color.rgb = o.get("color", color)
    return box


def _bullet(p, level, color):
    pPr = p._p.get_or_add_pPr()
    indent = 0.22 + 0.25 * level
    pPr.set("marL", str(int(Inches(indent))))
    pPr.set("indent", str(int(-Inches(0.2))))
    for tag in ("a:buClr", "a:buFont", "a:buChar", "a:buNone"):
        for e in pPr.findall(qn(tag)):
            pPr.remove(e)
    buClr = pPr.makeelement(qn("a:buClr"), {})
    srgb = buClr.makeelement(qn("a:srgbClr"), {"val": str(color)})
    buClr.append(srgb)
    buFont = pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
    buChar = pPr.makeelement(qn("a:buChar"), {"char": "•" if level == 0 else "–"})
    pPr.append(buClr)
    pPr.append(buFont)
    pPr.append(buChar)


def box(slide, x, y, w, h, fill="tint", line=None, shape=MSO_SHAPE.RECTANGLE, name=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        s.name = name
    s.fill.solid()
    s.fill.fore_color.rgb = FILLS.get(fill, fill) if isinstance(fill, str) else fill
    if line:
        s.line.color.rgb = FILLS.get(line, line) if isinstance(line, str) else line
        s.line.width = Pt(1)
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    s.text_frame.text = ""
    return s


def card(slide, x, y, w, h, title, body, fill="tint", head="blue", size=13, title_size=15,
         head_h=0.5, name=None):
    """Card = coloured header band + body panel (both native shapes, editable)."""
    box(slide, x, y, w, h, fill=fill, name=(name or title) + " panel")
    hb = box(slide, x, y, w, head_h, fill=head, name=(name or title) + " header")
    tf = hb.text_frame
    tf.margin_left = Inches(0.12)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = True
    r = tf.paragraphs[0].add_run()
    r.text = title
    r.font.size = Pt(title_size)
    r.font.bold = True
    r.font.color.rgb = WHITE if head in ("navy", "blue", "mid", "grey") else NAVY
    if body:
        paras = [(b, {"bullet": True}) if isinstance(b, str) else b for b in body]
        tb(slide, x + 0.08, y + head_h + 0.08, w - 0.16, h - head_h - 0.12, paras, size=size)


def circle_num(slide, x, y, d, label, fill="blue", size=16):
    c = box(slide, x, y, d, d, fill=fill, shape=MSO_SHAPE.OVAL, name=f"Number {label}")
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(label)
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = WHITE if fill in ("navy", "blue", "mid", "grey") else NAVY
    return c


def table(slide, x, y, w, rows, col_w, size=12, row_h=0.36, head_fill=BLUE, first_col_bold=True,
          name="Table", head_h=None):
    nrows, ncols = len(rows), len(rows[0])
    gf = slide.shapes.add_table(nrows, ncols, Inches(x), Inches(y), Inches(w),
                                Inches(row_h * nrows))
    gf.name = name
    tbl = gf.table
    # remove template table style banding look by explicit fills
    for ci, cw in enumerate(col_w):
        tbl.columns[ci].width = Inches(cw)
    for ri, row in enumerate(rows):
        tbl.rows[ri].height = Inches(head_h if (ri == 0 and head_h) else row_h)
        for ci, val in enumerate(row):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if ri == 0:
                cell.fill.fore_color.rgb = head_fill
            else:
                cell.fill.fore_color.rgb = TINT if ri % 2 == 1 else WHITE
            tf = cell.text_frame
            tf.word_wrap = True
            lines = val if isinstance(val, list) else [val]
            for li, line in enumerate(lines):
                p = tf.paragraphs[0] if li == 0 else tf.add_paragraph()
                if isinstance(val, list):
                    _bullet(p, 0, BLUE)
                r = p.add_run()
                r.text = line
                r.font.size = Pt(size)
                r.font.bold = ri == 0 or (first_col_bold and ci == 0)
                r.font.color.rgb = WHITE if ri == 0 else INK
    return gf


def style_chart(chart, size=12):
    chart.font.size = Pt(size)
    chart.font.color.rgb = INK


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def crop_images(zip_dir, out_dir):
    """Crop illustrations from the uploaded AREP screenshots (inside the zips)."""
    crops = {
        "hd_circuit.png": ("Dialysis.zip", "Dialysis/Screenshot 2026-11-12 141030.png",
                           (80, 295, 1455, 1082)),
        "water_treatment.png": ("Dialysis.zip", "Dialysis/Screenshot 2026-11-12 141808.png",
                                (0, 295, 1532, 790)),
        "rope_ladder.png": ("vascular access.zip",
                            "vascular access/Screenshot 2026-11-12 151911.png",
                            (1040, 291, 2081, 1061)),
        "buttonhole.png": ("vascular access.zip",
                           "vascular access/Screenshot 2026-11-12 152109.png", (894, 270, 2083, 1040)),
        "dialysate_circuit.png": ("Dialysis.zip", "Dialysis/Screenshot 2026-11-12 141056.png",
                                  (260, 340, 1200, 1075)),
        "fluid_balance.png": ("Water Treatment.zip", "Water Treatment/Screenshot 2026-11-12 155202.png",
                              (150, 370, 1560, 1105)),
    }
    os.makedirs(out_dir, exist_ok=True)
    paths = {}
    for out, (zname, member, bb) in crops.items():
        with zipfile.ZipFile(os.path.join(zip_dir, zname)) as z:
            im = Image.open(io.BytesIO(z.read(member))).convert("RGB")
        im = im.crop(bb)
        p = os.path.join(out_dir, out)
        im.save(p, optimize=True)
        paths[out] = p
    return paths


def picture_fit(slide, path, x, y, w, h, name):
    """Insert picture scaled to fit (no distortion), centred in the box."""
    with Image.open(path) as im:
        iw, ih = im.size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    pic = slide.shapes.add_picture(path, Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2),
                                   Inches(pw), Inches(ph))
    pic.name = name
    return pic


# ------------------------------------------------------------ slide kinds ---
def build_chapter(prs, spec):
    lay = layout(prs, CHAPTER_LAYOUT)
    s = prs.slides.add_slide(lay)
    for ph in s.placeholders:
        if ph.placeholder_format.idx == 29:
            ph.text_frame.text = spec["title"]
    notes(s, spec.get("notes", ""))
    return s


def build_content(prs, spec, images):
    lay = layout(prs, CONTENT_LAYOUT)
    s = prs.slides.add_slide(lay)
    for ph in s.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:
            ph.text_frame.text = spec["title"]
        elif idx == 15:
            set_source(ph, spec.get("source", ""))
    add_footer(s, lay)
    RENDER[spec["kind"]](s, spec, images)
    notes(s, spec.get("notes", ""))
    return s


# Each renderer draws the body of one content slide (area x 0.64–12.69, y 1.45–6.5)
def r_agenda(s, sp, im):
    n = len(sp["items"])
    gap = 0.3
    w = (12.05 - gap * (n - 1)) / n
    for i, (head, objs) in enumerate(sp["items"]):
        x = 0.64 + i * (w + gap)
        box(s, x, 1.6, w, 4.75, fill="tint", name=f"Agenda card {i+1}")
        circle_num(s, x + 0.2, 1.8, 0.7, i + 1, fill="blue", size=20)
        tb(s, x + 0.15, 2.65, w - 0.3, 0.5, [(head, {"bold": True, "size": 16, "color": NAVY})])
        tb(s, x + 0.15, 3.2, w - 0.3, 3.0, [(o, {"bullet": True, "space_after": 8}) for o in objs], size=14)


def r_split_cards(s, sp, im):
    """Left highlight panel + right 2x2 cards."""
    lp = sp["left"]
    box(s, 0.64, 1.6, 4.3, 4.75, fill="navy", name="Highlight panel")
    tb(s, 0.84, 1.8, 3.9, 0.6, [(lp["head"], {"bold": True, "size": 18, "color": WHITE})])
    tb(s, 0.84, 2.5, 3.9, 3.7, [(t, {"color": WHITE, "space_after": 10}) for t in lp["body"]],
       size=14)
    cw, chh = 3.6, 2.2
    for i, (head, body) in enumerate(sp["cards"]):
        x = 5.25 + (i % 2) * (cw + 0.25)
        y = 1.6 + (i // 2) * (chh + 0.35)
        card(s, x, y, cw, chh, head, body, head="blue" if i % 3 == 0 else "mid", size=13)


def r_criteria(s, sp, im):
    n = len(sp["criteria"])
    for i, (head, body) in enumerate(sp["criteria"]):
        y = 1.6 + i * 1.25
        circle_num(s, 0.64, y + 0.12, 0.8, "✓", fill="blue", size=20)
        tb(s, 1.65, y, 6.2, 0.45, [(head, {"bold": True, "size": 16, "color": NAVY})])
        tb(s, 1.65, y + 0.45, 6.2, 0.7, [body], size=13)
    hb = sp["highlight"]
    box(s, 8.4, 1.6, 4.29, 3.6, fill="sand", name="Key message panel")
    tb(s, 8.6, 1.8, 3.9, 0.5, [(hb["head"], {"bold": True, "size": 16, "color": BLUE})])
    tb(s, 8.6, 2.35, 3.9, 2.8, [(t, {"space_after": 10}) for t in hb["body"]], size=14)
    if sp.get("stat"):
        st = sp["stat"]
        tb(s, 8.4, 5.3, 4.29, 0.65, [(st[0], {"bold": True, "size": 28, "color": BLUE})])
        tb(s, 8.4, 5.9, 4.29, 0.6, [(st[1], {"size": 12, "color": INK})])


def r_image_two_lists(s, sp, im):
    picture_fit(s, im[sp["image"]], 0.64, 1.5, 6.2, 4.6, sp["image_alt"])
    tb(s, 0.64, 6.1, 6.2, 0.4, [(sp["caption"], {"size": 10, "italic": True, "color": GREY})])
    y = 1.6
    for head, items, fill in sp["lists"]:
        h = 0.55 + 0.36 * len(items)
        card(s, 7.15, y, 5.54, h, head, items, head=fill, size=13)
        y += h + 0.3


def r_columns(s, sp, im):
    cols = sp["columns"]
    n = len(cols)
    gap = 0.3
    w = (12.05 - gap * (n - 1)) / n
    for i, col in enumerate(cols):
        x = 0.64 + i * (w + gap)
        heads = ["blue", "mid", "navy", "grey"]
        card(s, x, 1.6, w, sp.get("h", 3.75), col["head"], None, head=heads[i % 4])
        rows = []
        for label, text in col["rows"]:
            rows.append((label, {"bold": True, "size": 13, "color": BLUE, "space_after": 2}))
            rows.append((text, {"size": 14, "space_after": 14}))
        tb(s, x + 0.1, 2.2, w - 0.2, sp.get("h", 3.75) - 0.65, rows)
    if sp.get("banner"):
        box(s, 0.64, sp.get("banner_y", 5.6), 12.05, 0.8, fill="sand", name="Key message")
        tb(s, 0.84, sp.get("banner_y", 5.6), 11.65, 0.8, [(sp["banner"], {"size": 14, "bold": True, "color": NAVY})],
           anchor=MSO_ANCHOR.MIDDLE)


def r_table_side(s, sp, im):
    t = sp["table"]
    table(s, 0.64, 1.6, t["w"], t["rows"], t["col_w"], size=t.get("size", 12),
          row_h=t.get("row_h", 0.4), head_h=t.get("head_h"))
    side = sp.get("side")
    if side:
        x = 0.64 + t["w"] + 0.35
        w = 12.69 - x
        box(s, x, 1.6, w, side.get("h", 4.75), fill="sand", name="Side panel")
        tb(s, x + 0.2, 1.75, w - 0.4, 0.5, [(side["head"], {"bold": True, "size": 15, "color": BLUE})])
        tb(s, x + 0.2, 2.3, w - 0.4, side.get("h", 4.75) - 0.8,
           [(b, {"bullet": True, "space_after": 6}) if isinstance(b, str) else b for b in side["body"]],
           size=13)


def r_water(s, sp, im):
    picture_fit(s, im["water_treatment.png"], 0.64, 1.35, 8.3, 2.75, "Water treatment system diagram")
    tb(s, 0.64, 4.05, 8.3, 0.3, [(sp["caption"], {"size": 10, "italic": True, "color": GREY})])
    w = (8.3 - 0.5) / 3
    for i, (head, body) in enumerate(sp["stages"]):
        card(s, 0.64 + i * (w + 0.25), 4.4, w, 2.05, head, body, head=["grey", "blue", "navy"][i],
             size=12, title_size=14, head_h=0.45)
    box(s, 9.25, 1.45, 3.44, 5.0, fill="navy", name="Stat panel")
    st = sp["stat"]
    tb(s, 9.45, 1.75, 3.04, 1.0, [(st[0], {"bold": True, "size": 36, "color": WHITE})])
    tb(s, 9.45, 2.75, 3.04, 1.1, [(st[1], {"size": 14, "color": WHITE})])
    tb(s, 9.45, 4.0, 3.04, 2.3, [(t, {"size": 13, "color": WHITE, "space_after": 8}) for t in sp["stat_body"]])


def r_adequacy(s, sp, im):
    card(s, 0.64, 1.6, 5.6, 2.9, sp["left"]["head"], sp["left"]["body"], head="blue", size=14)
    box(s, 0.64, 4.75, 5.6, 1.6, fill="sand", name="Dialysate note")
    tb(s, 0.84, 4.8, 5.2, 1.5, [(t, {"size": 13, "space_after": 6}) for t in sp["left_note"]],
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, 6.6, 1.6, 6.09, 0.5, [(sp["right_head"], {"bold": True, "size": 16, "color": NAVY})])
    for i, (num, label) in enumerate(sp["stats"]):
        x = 6.6 + i * 3.1
        box(s, x, 2.2, 2.9, 1.9, fill="tint", name=f"Stat {num}")
        tb(s, x, 2.3, 2.9, 0.9, [(num, {"bold": True, "size": 40, "color": BLUE, "align": PP_ALIGN.CENTER})])
        tb(s, x + 0.1, 3.2, 2.7, 0.85, [(label, {"size": 13, "align": PP_ALIGN.CENTER})])
    tb(s, 6.6, 4.35, 6.09, 2.0, [(b, {"bullet": True, "space_after": 6}) for b in sp["right_body"]], size=13)


def r_table_pie(s, sp, im):
    t = sp["table"]
    table(s, 0.64, 1.6, t["w"], t["rows"], t["col_w"], size=t.get("size", 12), row_h=t.get("row_h", 0.4), head_h=t.get("head_h"))
    cd = CategoryChartData()
    cd.categories = [c for c, _ in sp["pie"]["data"]]
    cd.add_series("Share of patients (%)", [v for _, v in sp["pie"]["data"]])
    x = 0.64 + t["w"] + 0.3
    gf = s.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(x), Inches(1.6), Inches(12.69 - x),
                            Inches(4.1), cd)
    gf.name = "Access type share chart"
    ch = gf.chart
    style_chart(ch, 12)
    ch.has_title = True
    ch.chart_title.text_frame.text = sp["pie"]["title"]
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
    ch.has_legend = True
    ch.legend.position = XL_LEGEND_POSITION.BOTTOM
    ch.legend.include_in_layout = False
    plot = ch.plots[0]
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.number_format = '0.0"%"'
    dl.number_format_is_linked = False
    dl.font.size = Pt(12)
    dl.font.bold = True
    dl.font.color.rgb = WHITE
    dl.position = XL_LABEL_POSITION.CENTER
    for i, col in enumerate([BLUE, MID, GREY]):
        pt = plot.series[0].points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = col
    tb(s, x, 5.75, 12.69 - x, 0.75, [(sp["pie"]["note"], {"size": 10, "italic": True, "color": INK})])


def r_flow(s, sp, im):
    steps = sp["steps"]
    n = len(steps)
    gap = 0.35
    w = (12.05 - gap * (n - 1)) / n
    for i, (head, body) in enumerate(steps):
        x = 0.64 + i * (w + gap)
        card(s, x, 1.6, w, 2.45, head, [body] if isinstance(body, str) else body,
             head=["navy", "blue", "mid", "blue"][i % 4], size=13, title_size=14, head_h=0.55)
        if i < n - 1:
            a = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + w + 0.05), Inches(2.6),
                                   Inches(gap - 0.1), Inches(0.35))
            a.fill.solid(); a.fill.fore_color.rgb = GREY; a.line.fill.background()
    lb = sp["bottom_left"]
    card(s, 0.64, 4.35, 5.9, 2.0, lb["head"], lb["body"], head="grey", size=13)
    rb = sp["bottom_right"]
    box(s, 6.85, 4.35, 5.84, 2.0, fill="tint", name="AVF site order panel")
    tb(s, 7.0, 4.42, 5.6, 0.45, [(rb["head"], {"bold": True, "size": 14, "color": NAVY})])
    for i, t in enumerate(rb["items"]):
        circle_num(s, 7.05, 4.95 + i * 0.45, 0.36, i + 1, fill="blue", size=12)
        tb(s, 7.55, 4.93 + i * 0.45, 5.0, 0.4, [t], size=13, anchor=MSO_ANCHOR.MIDDLE)


def r_rule6(s, sp, im):
    tb(s, 0.64, 1.45, 12.05, 0.45, [(sp["lead"], {"size": 15, "bold": True, "color": NAVY})])
    for i, (num, label) in enumerate(sp["sixes"]):
        x = 0.64 + i * 3.08
        c = box(s, x + 0.55, 1.95, 1.7, 1.7, fill=["blue", "mid", "blue", "mid"][i], shape=MSO_SHAPE.OVAL,
                name=f"Rule of 6 {i+1}")
        tf = c.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = num; r.font.size = Pt(22); r.font.bold = True; r.font.color.rgb = WHITE
        tb(s, x, 3.7, 2.8, 0.7, [(label, {"size": 13, "align": PP_ALIGN.CENTER})])
    card(s, 0.64, 4.45, 5.9, 1.95, sp["left"]["head"], sp["left"]["body"], head="navy", size=13)
    card(s, 6.85, 4.45, 5.84, 1.95, sp["right"]["head"], sp["right"]["body"], head="grey", size=13)


def r_image_cards(s, sp, im):
    picture_fit(s, im[sp["image"]], 0.64, 1.5, 5.6, 4.2, sp["image_alt"])
    tb(s, 0.64, 5.75, 5.6, 0.7, [(sp["caption"], {"size": 10, "italic": True, "color": GREY})])
    y = 1.5
    for head, body, fill in sp["cards"]:
        h = 0.5 + 0.34 * len(body) + 0.15
        card(s, 6.55, y, 6.14, h, head, body, head=fill, size=13, title_size=14, head_h=0.45)
        y += h + 0.2


def r_bar_compare(s, sp, im):
    c = sp["chart"]
    cd = CategoryChartData()
    cd.categories = c["categories"]
    for name, vals in c["series"]:
        cd.add_series(name, vals)
    gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.64), Inches(1.5), Inches(7.4),
                            Inches(c.get("h", 4.9)), cd)
    gf.name = c["name"]
    ch = gf.chart
    style_chart(ch, 12)
    ch.has_title = True
    ch.chart_title.text_frame.text = c["title"]
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
    ch.has_legend = len(c["series"]) > 1
    if ch.has_legend:
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM
        ch.legend.include_in_layout = False
    va = ch.value_axis
    va.maximum_scale = c.get("max", 100)
    va.minimum_scale = 0
    va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = GREY_L
    va.tick_labels.font.size = Pt(11)
    va.format.line.fill.background()
    if c.get("axis_title"):
        va.has_title = True
        va.axis_title.text_frame.text = c["axis_title"]
        va.axis_title.text_frame.paragraphs[0].runs[0].font.size = Pt(11)
    ch.category_axis.tick_labels.font.size = Pt(12)
    plot = ch.plots[0]
    plot.gap_width = 80
    plot.has_data_labels = True
    plot.data_labels.number_format = c.get("fmt", '0"%"')
    plot.data_labels.number_format_is_linked = False
    plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
    plot.data_labels.font.size = Pt(12)
    cols = c.get("colors", [BLUE, GREY])
    for i, ser in enumerate(plot.series):
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = cols[i % len(cols)]
    if c.get("point_colors"):
        for i, col in enumerate(c["point_colors"]):
            pt = plot.series[0].points[i]
            pt.format.fill.solid(); pt.format.fill.fore_color.rgb = col
    side = sp["side"]
    box(s, 8.35, 1.5, 4.34, 4.9, fill="sand", name="Interpretation panel")
    tb(s, 8.55, 1.65, 3.94, 0.5, [(side["head"], {"bold": True, "size": 15, "color": BLUE})])
    tb(s, 8.55, 2.2, 3.94, 4.1,
       [(b, {"bullet": True, "space_after": 8}) if isinstance(b, str) else b for b in side["body"]], size=13)


def r_six_grid(s, sp, im):
    items = sp["items"]
    cw, chh = 3.85, 2.3
    for i, (head, stat, body) in enumerate(items):
        x = 0.64 + (i % 3) * (cw + 0.25)
        y = 1.55 + (i // 3) * (chh + 0.25)
        box(s, x, y, cw, chh, fill="tint", name=f"{head} card")
        tb(s, x + 0.15, y + 0.1, cw - 0.3, 0.45, [(head, {"bold": True, "size": 15, "color": NAVY})])
        tb(s, x + 0.15, y + 0.55, cw - 0.3, 0.65, [(stat, {"bold": True, "size": 22, "color": BLUE})])
        tb(s, x + 0.15, y + 1.2, cw - 0.3, 1.05, [body], size=12)


def r_two_cards(s, sp, im):
    w = (12.05 - 0.3) / 2
    for i, (head, body) in enumerate(sp["cards"]):
        card(s, 0.64 + i * (w + 0.3), 1.6, w, sp.get("h", 4.75), head, body,
             head=["blue", "navy"][i], size=sp.get("size", 14))
    if sp.get("banner"):
        by = 1.6 + sp.get("h", 4.75) + 0.3
        box(s, 0.64, by, 12.05, 0.7, fill="sand", name="Key message")
        tb(s, 0.84, by, 11.65, 0.7, [(sp["banner"], {"size": 14, "bold": True, "color": NAVY})],
           anchor=MSO_ANCHOR.MIDDLE)


def r_compartments(s, sp, im):
    c = sp["chart"]
    cd = CategoryChartData()
    cd.categories = [""]
    for name, v in c["series"]:
        cd.add_series(name, [v])
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED, Inches(0.64), Inches(1.5), Inches(7.6),
                            Inches(2.6), cd)
    gf.name = "Body water compartments chart"
    ch = gf.chart
    style_chart(ch, 12)
    ch.has_title = True
    ch.chart_title.text_frame.text = c["title"]
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
    ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
    ch.has_legend = True
    ch.legend.position = XL_LEGEND_POSITION.BOTTOM
    ch.legend.include_in_layout = False
    plot = ch.plots[0]
    plot.gap_width = 30
    plot.has_data_labels = True
    plot.data_labels.number_format = '0.0" L"'
    plot.data_labels.number_format_is_linked = False
    plot.data_labels.position = XL_LABEL_POSITION.CENTER
    plot.data_labels.font.size = Pt(12)
    plot.data_labels.font.bold = True
    plot.data_labels.font.color.rgb = WHITE
    for ser, col in zip(plot.series, [BLUE, MID, NAVY]):
        ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
    va = ch.value_axis
    va.minimum_scale = 0; va.maximum_scale = c["max"]
    va.has_major_gridlines = False
    va.tick_labels.font.size = Pt(11)
    ch.category_axis.visible = False
    tb(s, 0.64, 4.1, 7.6, 0.4, [(c["note"], {"size": 10, "italic": True, "color": INK})])
    # key facts
    for i, (num, label) in enumerate(sp["facts"]):
        x = 0.64 + i * 2.6
        box(s, x, 4.65, 2.4, 1.75, fill="tint", name=f"Fact {i+1}")
        tb(s, x + 0.1, 4.72, 2.2, 0.7, [(num, {"bold": True, "size": 22, "color": BLUE})])
        tb(s, x + 0.1, 5.4, 2.2, 0.95, [label], size=12)
    side = sp["side"]
    box(s, 8.55, 1.5, 4.14, 4.9, fill="sand", name="Side panel")
    tb(s, 8.75, 1.65, 3.74, 0.5, [(side["head"], {"bold": True, "size": 15, "color": BLUE})])
    tb(s, 8.75, 2.2, 3.74, 4.1, [(b, {"bullet": True, "space_after": 8}) for b in side["body"]], size=13)


def r_levers(s, sp, im):
    box(s, 0.64, 1.55, 12.05, 1.15, fill="navy", name="Dry weight definition")
    tb(s, 0.84, 1.6, 11.65, 1.05,
       [(sp["def_head"], {"bold": True, "size": 15, "color": WHITE, "space_after": 2}),
        (sp["def_body"], {"size": 13, "color": WHITE})], anchor=MSO_ANCHOR.MIDDLE)
    n = len(sp["levers"])
    w = (12.05 - 0.25 * (n - 1)) / n
    for i, (head, body) in enumerate(sp["levers"]):
        card(s, 0.64 + i * (w + 0.25), 2.95, w, 2.45, head, body,
             head=["blue", "mid", "blue", "mid"][i], size=13, title_size=14, head_h=0.5)
    box(s, 0.64, 5.65, 12.05, 0.75, fill="sand", name="Key message")
    tb(s, 0.84, 5.65, 11.65, 0.75, [(sp["banner"], {"size": 14, "bold": True, "color": NAVY})],
       anchor=MSO_ANCHOR.MIDDLE)


def r_ufr(s, sp, im):
    # formula + worked example
    box(s, 0.64, 1.55, 6.0, 1.3, fill="navy", name="UFR formula")
    tb(s, 0.84, 1.6, 5.6, 1.2,
       [("UF rate (mL/kg/h) =", {"size": 14, "color": WHITE, "bold": True, "space_after": 2}),
        (sp["formula"], {"size": 15, "color": WHITE})], anchor=MSO_ANCHOR.MIDDLE)
    ex = sp["example"]
    card(s, 0.64, 3.05, 6.0, 3.35, ex["head"], ex["body"], head="grey", size=13)
    # zones
    tb(s, 6.95, 1.55, 5.74, 0.45, [(sp["zones_head"], {"bold": True, "size": 15, "color": NAVY})])
    zf = [MID, BLUE, NAVY]
    for i, (zone, txt) in enumerate(sp["zones"]):
        y = 2.1 + i * 1.05
        z = box(s, 6.95, y, 1.9, 0.9, fill=zf[i], name=f"Zone {zone}")
        tf = z.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = zone; r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = WHITE
        tb(s, 8.95, y, 3.74, 0.9, [txt], size=12, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 6.95, 5.3, 5.74, 1.1, fill="sand", name="Too slow too fast")
    tb(s, 7.1, 5.3, 5.5, 1.1, [(t, {"size": 12, "space_after": 3}) for t in sp["balance"]],
       anchor=MSO_ANCHOR.MIDDLE)


def r_table_only(s, sp, im):
    t = sp["table"]
    table(s, 0.64, sp.get("y", 1.55), t["w"], t["rows"], t["col_w"], size=t.get("size", 12),
          row_h=t.get("row_h", 0.4), head_h=t.get("head_h"))
    if sp.get("banner"):
        box(s, 0.64, sp.get("banner_y", 5.8), 12.05, 0.65, fill="sand", name="Key message")
        tb(s, 0.84, sp.get("banner_y", 5.8), 11.65, 0.65,
           [(sp["banner"], {"size": 13, "bold": True, "color": NAVY})], anchor=MSO_ANCHOR.MIDDLE)


def r_electrolytes(s, sp, im):
    t = sp["table"]
    table(s, 0.64, 1.55, t["w"], t["rows"], t["col_w"], size=12, row_h=0.42)
    # pH scale (native shapes)
    x0, y0, wseg = 7.9, 1.95, 4.79 / 15
    tb(s, 7.9, 1.5, 4.79, 0.4, [(sp["ph_head"], {"bold": True, "size": 15, "color": NAVY})])
    cols = ["C0392B", "D35400", "E67E22", "F39C12", "F1C40F", "F7DC6F", "FCF3CF", "FFFFFF",
            "D6EAF8", "AED6F1", "85C1E9", "5DADE2", "3498DB", "2874A6", "1B4F72"]
    for i, c in enumerate(cols):
        b = box(s, x0 + i * wseg, y0, wseg, 0.55, fill=RGBColor.from_string(c), line="greyl",
                name=f"pH {i}")
        tb(s, x0 + i * wseg - 0.05, y0 + 0.58, wseg + 0.1, 0.3, [(str(i), {"size": 10, "align": PP_ALIGN.CENTER})],
           margin=0)
    # normal blood pH marker (7.35–7.45 sits just above 7)
    mx = x0 + 7.35 * wseg + wseg / 2 - 0.02
    m = box(s, mx - 0.06, y0 - 0.1, 0.12 + 0.1 * wseg, 0.68, fill="navy", name="Normal blood pH marker")
    tb(s, 7.9, 2.95, 4.79, 0.35, [("Acidic  ←   7 = neutral   →  Basic", {"size": 11, "align": PP_ALIGN.CENTER})])
    box(s, 7.9, 3.4, 4.79, 0.7, fill="navy", name="Normal pH box")
    tb(s, 7.9, 3.4, 4.79, 0.7, [(sp["ph_normal"], {"bold": True, "size": 15, "color": WHITE, "align": PP_ALIGN.CENTER})],
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, 7.9, 4.25, 4.79, 2.2, [(b, {"bullet": True, "space_after": 6}) for b in sp["ph_body"]], size=13)


def r_takeaways(s, sp, im):
    for i, (head, body) in enumerate(sp["items"]):
        y = 1.5 + i * 1.0
        circle_num(s, 0.64, y + 0.1, 0.7, i + 1, fill="blue", size=18)
        tb(s, 1.55, y, 11.1, 0.42, [(head, {"bold": True, "size": 15, "color": NAVY})])
        tb(s, 1.55, y + 0.42, 11.1, 0.5, [body], size=13)


def r_references(s, sp, im):
    refs = sp["refs"]
    half = (len(refs) + 1) // 2
    for col, chunk in enumerate((refs[:half], refs[half:])):
        start = 1 if col == 0 else half + 1
        tb(s, 0.64 + col * 6.15, 1.45, 5.9, 5.1,
           [(f"{start + i}. {r}", {"size": 10, "space_after": 3}) for i, r in enumerate(chunk)])





def r_steps(s, sp, im):
    """Numbered vertical action steps (left) + side panel (right)."""
    steps = sp["steps"]
    gap = sp.get("gap", 0.08)
    avail = 4.95
    h = min(0.95, (avail - gap * (len(steps) - 1)) / len(steps))
    w = sp.get("w", 7.6)
    for i, (head, body) in enumerate(steps):
        y = 1.5 + i * (h + gap)
        box(s, 0.64, y, w, h, fill="tint", name=f"Step {i+1}")
        circle_num(s, 0.76, y + (h - 0.5) / 2, 0.5, i + 1, fill="blue", size=14)
        tb(s, 1.4, y, w - 0.85, h, [(head, {"bold": True, "size": 14, "color": NAVY, "space_after": 1}),
                                    (body, {"size": 12})], anchor=MSO_ANCHOR.MIDDLE)
    side = sp.get("side")
    if side:
        x = 0.64 + w + 0.3
        sw = 12.69 - x
        box(s, x, 1.5, sw, 4.95, fill=side.get("fill", "navy"), name="Side panel")
        light = side.get("fill", "navy") in ("navy", "blue")
        tc = WHITE if light else INK
        tb(s, x + 0.2, 1.65, sw - 0.4, 0.6, [(side["head"], {"bold": True, "size": 16,
                                                             "color": WHITE if light else BLUE})])
        tb(s, x + 0.2, 2.3, sw - 0.4, 4.0,
           [(b, {"bullet": True, "space_after": 7, "color": tc, "bullet_color": LIGHT if light else BLUE})
            if isinstance(b, str) else b for b in side["body"]], size=13)


def r_checklist(s, sp, im):
    """Two (or three) checklist columns with tick circles."""
    cols = sp["columns"]
    n = len(cols)
    gap = 0.3
    w = (12.05 - gap * (n - 1)) / n
    hgt = sp.get("h", 4.95)
    for i, (head, items) in enumerate(cols):
        x = 0.64 + i * (w + gap)
        box(s, x, 1.5, w, hgt, fill="tint", name=f"{head} panel")
        hb = box(s, x, 1.5, w, 0.5, fill=["blue", "navy", "mid"][i % 3], name=f"{head} header")
        tf = hb.text_frame; tf.margin_left = Inches(0.12); tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        r = tf.paragraphs[0].add_run(); r.text = head; r.font.size = Pt(15); r.font.bold = True
        r.font.color.rgb = WHITE
        step = sp.get("row_h", 0.5)
        for j, it in enumerate(items):
            y = 2.12 + j * step
            c = box(s, x + 0.15, y + 0.06, 0.28, 0.28, fill="blue", shape=MSO_SHAPE.OVAL, name="tick")
            ctf = c.text_frame; ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
            ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
            pp = ctf.paragraphs[0]; pp.alignment = PP_ALIGN.CENTER
            rr = pp.add_run(); rr.text = "✓"; rr.font.size = Pt(11); rr.font.bold = True; rr.font.color.rgb = WHITE
            tb(s, x + 0.55, y, w - 0.7, step, [it], size=sp.get("size", 13))
    if sp.get("banner"):
        by = 1.5 + hgt + 0.2
        box(s, 0.64, by, 12.05, 6.45 - by, fill="sand", name="Key message")
        tb(s, 0.84, by, 11.65, 6.45 - by, [(sp["banner"], {"size": 14, "bold": True, "color": NAVY})],
           anchor=MSO_ANCHOR.MIDDLE)


def r_case(s, sp, im):
    """Case scenario: patient story (left) and discussion questions (right). Answers go in the notes."""
    box(s, 0.64, 1.5, 6.3, 4.95, fill="navy", name="Case panel")
    tb(s, 0.84, 1.62, 5.9, 0.5, [(sp.get("case_head", "Case scenario"), {"bold": True, "size": 16, "color": WHITE})])
    tb(s, 0.84, 2.15, 5.9, 4.2, [(t, {"size": 14, "color": WHITE, "space_after": 10}) for t in sp["case"]])
    box(s, 7.25, 1.5, 5.44, 4.95, fill="sand", name="Questions panel")
    tb(s, 7.45, 1.62, 5.04, 0.5, [("Discuss", {"bold": True, "size": 16, "color": BLUE})])
    for i, q in enumerate(sp["questions"]):
        y = 2.2 + i * 1.0
        circle_num(s, 7.45, y + 0.05, 0.45, i + 1, fill="blue", size=13)
        tb(s, 8.05, y, 4.45, 0.95, [q], size=13)


def r_stat_cards(s, sp, im):
    """Row of 3–4 big-number stat cards + bullet panel below."""
    stats = sp["stats"]
    n = len(stats)
    gap = 0.25
    w = (12.05 - gap * (n - 1)) / n
    for i, (num, label) in enumerate(stats):
        x = 0.64 + i * (w + gap)
        box(s, x, 1.5, w, 1.75, fill=["blue", "navy", "mid", "navy"][i % 4], name=f"Stat {i+1}")
        tb(s, x + 0.15, 1.58, w - 0.3, 0.8, [(num, {"bold": True, "size": 28, "color": WHITE})])
        tb(s, x + 0.15, 2.38, w - 0.3, 0.85, [(label, {"size": 12, "color": WHITE})])
    lc = sp.get("cards")
    if lc:
        gw = (12.05 - 0.3) / len(lc)
        for i, (head, body) in enumerate(lc):
            card(s, 0.64 + i * (gw + 0.3), 3.5, gw, 2.95, head, body,
                 head=["blue", "grey", "mid"][i % 3], size=13, title_size=14, head_h=0.45)


def r_formula(s, sp, im):
    """Formula panels (left) + worked example card (right) + optional native chart."""
    y = 1.5
    for head, formula, note in sp["formulas"]:
        box(s, 0.64, y, 6.4, 1.45, fill="navy", name=f"{head} formula")
        tb(s, 0.84, y + 0.05, 6.0, 1.35,
           [(head, {"bold": True, "size": 13, "color": LIGHT, "space_after": 2}),
            (formula, {"bold": True, "size": 16, "color": WHITE, "space_after": 2}),
            (note, {"size": 11, "color": WHITE})], anchor=MSO_ANCHOR.MIDDLE)
        y += 1.6
    if sp.get("below"):
        tb(s, 0.64, y, 6.4, 6.45 - y, [(b, {"bullet": True, "space_after": 5}) for b in sp["below"]], size=13)
    ex = sp["example"]
    card(s, 7.35, 1.5, 5.34, 4.95, ex["head"], ex["body"], head="blue", size=13)


def r_matrix(s, sp, im):
    """Decision/escalation matrix: coloured level labels with actions (table-like, shapes)."""
    rows = sp["rows"]
    h = min(1.05, (4.95 - 0.1 * (len(rows) - 1)) / len(rows))
    fills = sp.get("fills", ["mid", "blue", "navy", "grey"])
    for i, (level, trigger, action) in enumerate(rows):
        y = 1.5 + i * (h + 0.1)
        lb = box(s, 0.64, y, 2.4, h, fill=fills[i % len(fills)], name=f"Level {i+1}")
        tf = lb.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; tf.word_wrap = True
        tf.margin_left = Inches(0.1)
        r = tf.paragraphs[0].add_run(); r.text = level; r.font.size = Pt(14); r.font.bold = True
        r.font.color.rgb = WHITE
        box(s, 3.1, y, 4.0, h, fill="tint", name=f"Trigger {i+1}")
        tb(s, 3.2, y, 3.8, h, [trigger], size=12, anchor=MSO_ANCHOR.MIDDLE)
        box(s, 7.16, y, 5.53, h, fill="sand", name=f"Action {i+1}")
        tb(s, 7.26, y, 5.33, h, [action], size=12, anchor=MSO_ANCHOR.MIDDLE)



# ===================================================== programme renderers (v2) ===
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.chart import XL_MARKER_STYLE

ILLUSTRATIVE = "Illustrative training data: not actual patient or facility results"


def _line(s, x1, y1, x2, y2, color, width=3, dash=False, name=None, arrow=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(width)
    if dash:
        c.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    if arrow:
        ln = c.line._get_or_add_ln()
        ln.append(ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"}))
    if name:
        c.name = name
    return c


def _label(s, x, y, w, h, text, size=12, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE):
    return tb(s, x, y, w, h, [(text, {"size": size, "color": color, "bold": bold, "align": align})],
              anchor=anchor, margin=0.02)


def _side_panel(s, side, x, y=1.5, h=4.95):
    sw = 12.69 - x
    fill = side.get("fill", "sand")
    box(s, x, y, sw, h, fill=fill, name="Side panel")
    dark = fill in ("navy", "blue")
    tb(s, x + 0.2, y + 0.12, sw - 0.4, 0.55, [(side["head"], {"bold": True, "size": 15,
                                                            "color": WHITE if dark else BLUE})])
    tb(s, x + 0.2, y + 0.7, sw - 0.4, h - 0.85,
       [(b, {"bullet": True, "space_after": 7, "color": WHITE if dark else INK,
             "bullet_color": LIGHT if dark else BLUE}) if isinstance(b, str) else b for b in side["body"]],
       size=side.get("size", 13))


def _chart_note(s, x, y, w, text):
    tb(s, x, y, w, 0.35, [(text, {"size": 10, "italic": True, "color": GREY_TXT})], margin=0.02)


def r_opening(s, sp, im):
    """Opening scenario: wide story band + 2–3 'think about' tiles."""
    box(s, 0.64, 1.5, 12.05, 2.35, fill="navy", name="Opening scenario")
    tb(s, 0.9, 1.62, 11.5, 0.45, [(sp.get("head", "Opening scenario"), {"bold": True, "size": 15, "color": LIGHT})])
    tb(s, 0.9, 2.1, 11.5, 1.7, [(t, {"size": 17, "color": WHITE, "space_after": 6}) for t in sp["story"]])
    qs = sp["prompts"]
    n = len(qs)
    w = (12.05 - 0.25 * (n - 1)) / n
    for i, q in enumerate(qs):
        x = 0.64 + i * (w + 0.25)
        box(s, x, 4.1, w, 2.35, fill="tint", name=f"Prompt {i+1}")
        circle_num(s, x + 0.2, 4.3, 0.55, "?", fill="blue", size=18)
        tb(s, x + 0.2, 5.0, w - 0.4, 1.4, [(q, {"size": 15, "color": NAVY, "bold": True})])


def r_kcheck(s, sp, im):
    """Knowledge check: up to 4 question cards (2 x 2). Answers and rationales go in the notes."""
    qs = sp["questions"]
    cw, chh = 5.9, 2.35
    for i, (q, opts) in enumerate(qs):
        x = 0.64 + (i % 2) * (cw + 0.25)
        y = 1.5 + (i // 2) * (chh + 0.25)
        box(s, x, y, cw, chh, fill="tint", name=f"Question {i+1}")
        circle_num(s, x + 0.15, y + 0.15, 0.5, f"Q{i+1}", fill="blue", size=12)
        tb(s, x + 0.8, y + 0.1, cw - 0.95, 0.75, [(q, {"bold": True, "size": 13, "color": NAVY})])
        if opts:
            tb(s, x + 0.8, y + 0.85, cw - 0.95, chh - 0.95,
               [(o, {"size": 12, "space_after": 2}) for o in opts])


def _add_line_chart(s, c, x, y, w, h):
    cd = CategoryChartData()
    cd.categories = c["categories"]
    for ser in c["series"]:
        cd.add_series(ser[0], ser[1])
    gf = s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS if c.get("markers", True) else XL_CHART_TYPE.LINE,
                            Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = c.get("name", "Line chart")
    ch = gf.chart
    style_chart(ch, 11)
    ch.has_title = True
    ch.chart_title.text_frame.text = c["title"]
    r = ch.chart_title.text_frame.paragraphs[0].runs[0]
    r.font.size = Pt(13); r.font.bold = True
    ch.has_legend = len(c["series"]) > 1
    if ch.has_legend:
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM
        ch.legend.include_in_layout = False
        ch.legend.font.size = Pt(11)
    va = ch.value_axis
    if "min" in c: va.minimum_scale = c["min"]
    if "max" in c: va.maximum_scale = c["max"]
    if "major" in c: va.major_unit = c["major"]
    va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = GREY_L
    va.tick_labels.font.size = Pt(11)
    va.tick_labels.number_format = c.get("axis_fmt", "General")
    va.tick_labels.number_format_is_linked = False
    if c.get("y_title"):
        va.has_title = True
        va.axis_title.text_frame.text = c["y_title"]
        va.axis_title.text_frame.paragraphs[0].runs[0].font.size = Pt(11)
    ca = ch.category_axis
    ca.tick_labels.font.size = Pt(11)
    if c.get("x_title"):
        ca.has_title = True
        ca.axis_title.text_frame.text = c["x_title"]
        ca.axis_title.text_frame.paragraphs[0].runs[0].font.size = Pt(11)
    plot = ch.plots[0]
    for i, ser in enumerate(plot.series):
        spec = c["series"][i]
        col = spec[2] if len(spec) > 2 else BLUE
        dashed = spec[3] if len(spec) > 3 else False
        ser.format.line.color.rgb = col
        ser.format.line.width = Pt(1.5 if dashed else 2.5)
        ser.smooth = False
        if dashed:
            ser.format.line.dash_style = MSO_LINE_DASH_STYLE.DASH
            ser.marker.style = XL_MARKER_STYLE.NONE
        else:
            ser.marker.style = XL_MARKER_STYLE.CIRCLE
            ser.marker.size = 7
            ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = col
            ser.marker.format.line.color.rgb = col
        if c.get("labels") and not dashed and i == 0:
            ser.data_labels.show_value = True
            ser.data_labels.font.size = Pt(10)
            ser.data_labels.number_format = c.get("fmt", "General")
            ser.data_labels.number_format_is_linked = False
            ser.data_labels.position = XL_LABEL_POSITION.ABOVE
    return ch


def r_line_chart(s, sp, im):
    c = sp["chart"]
    w = sp.get("chart_w", 7.6)
    _add_line_chart(s, c, 0.64, 1.45, w, 4.65)
    if c.get("note"):
        _chart_note(s, 0.64, 6.12, w, c["note"])
    if sp.get("side"):
        _side_panel(s, sp["side"], 0.64 + w + 0.3)


def r_stacked(s, sp, im):
    """Horizontal stacked bar (e.g. UF volume composition) + formula/side panel."""
    c = sp["chart"]
    cd = CategoryChartData()
    cd.categories = c["categories"]
    for name, vals in c["series"]:
        cd.add_series(name, vals)
    w = sp.get("chart_w", 7.6)
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED, Inches(0.64), Inches(1.45), Inches(w), Inches(c.get("h", 3.0)), cd)
    gf.name = c.get("name", "Stacked chart")
    ch = gf.chart
    style_chart(ch, 11)
    ch.has_title = True
    ch.chart_title.text_frame.text = c["title"]
    r = ch.chart_title.text_frame.paragraphs[0].runs[0]; r.font.size = Pt(13); r.font.bold = True
    ch.has_legend = True
    ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(11)
    plot = ch.plots[0]
    plot.gap_width = 40
    plot.has_data_labels = c.get("labels", True)
    if plot.has_data_labels:
        plot.data_labels.number_format = c.get("fmt", '0.0" L"'); plot.data_labels.number_format_is_linked = False
        plot.data_labels.position = XL_LABEL_POSITION.CENTER
        plot.data_labels.font.size = Pt(12); plot.data_labels.font.bold = True; plot.data_labels.font.color.rgb = WHITE
    for ser, col in zip(plot.series, c.get("colors", [BLUE, MID, NAVY, GREY])):
        ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
    va = ch.value_axis
    va.minimum_scale = 0
    if "max" in c: va.maximum_scale = c["max"]
    va.has_major_gridlines = False; va.tick_labels.font.size = Pt(11)
    ch.category_axis.tick_labels.font.size = Pt(11)
    yb = 1.45 + c.get("h", 3.0)
    if c.get("note"):
        _chart_note(s, 0.64, yb + 0.02, w, c["note"])
    if sp.get("below"):
        b = sp["below"]
        box(s, 0.64, yb + 0.45, w, 6.45 - yb - 0.45, fill="navy", name="Formula panel")
        tb(s, 0.84, yb + 0.5, w - 0.4, 6.45 - yb - 0.55,
           [(t, {"size": 13 if i else 14, "bold": i == 0, "color": WHITE if i else LIGHT, "space_after": 3})
            for i, t in enumerate(b)], anchor=MSO_ANCHOR.MIDDLE)
    if sp.get("side"):
        _side_panel(s, sp["side"], 0.64 + w + 0.3)


def r_dashboard(s, sp, im):
    kpis = sp["kpis"]
    n = len(kpis)
    gap = 0.2
    w = (12.05 - gap * (n - 1)) / n
    for i, (val, label, ref) in enumerate(kpis):
        x = 0.64 + i * (w + gap)
        box(s, x, 1.45, w, 1.35, fill=["blue", "navy", "mid", "navy", "blue"][i % 5], name=f"KPI {i+1}")
        tb(s, x + 0.12, 1.5, w - 0.24, 0.6, [(val, {"bold": True, "size": 24, "color": WHITE})])
        tb(s, x + 0.12, 2.08, w - 0.24, 0.4, [(label, {"size": 11, "color": WHITE, "bold": True})])
        tb(s, x + 0.12, 2.42, w - 0.24, 0.35, [(ref, {"size": 10, "color": LIGHT})])
    _add_line_chart(s, sp["chart"], 0.64, 2.95, 7.6, 3.2)
    _chart_note(s, 0.64, 6.12, 7.6, ILLUSTRATIVE)
    if sp.get("side"):
        _side_panel(s, sp["side"], 8.55, y=2.95, h=3.5)


def r_algorithm(s, sp, im):
    """Vertical flowchart. nodes: dict(t='start'|'action'|'decision'|'end', text, no=optional side action)."""
    nodes = sp["nodes"]
    n = len(nodes)
    gap = 0.17
    h = min(0.66, (4.95 - gap * (n - 1)) / n)
    x, w = 0.64, sp.get("w", 5.6)
    fills = {"start": "navy", "action": "tint", "decision": "mid", "end": "blue"}
    shapes = {"start": MSO_SHAPE.ROUNDED_RECTANGLE, "action": MSO_SHAPE.RECTANGLE,
              "decision": MSO_SHAPE.FLOWCHART_DECISION, "end": MSO_SHAPE.ROUNDED_RECTANGLE}
    for i, nd in enumerate(nodes):
        y = 1.5 + i * (h + gap)
        t = nd.get("t", "action")
        b = box(s, x, y, w, h, fill=fills[t], shape=shapes[t], name=f"Node {i+1}")
        tf = b.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(0.35 if t == "decision" else 0.1)
        tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = nd["text"]; r.font.size = Pt(12 if t != "decision" else 11.5)
        r.font.bold = t != "action"
        r.font.color.rgb = NAVY if t == "action" else WHITE
        if i < n - 1:
            _line(s, x + w / 2, y + h, x + w / 2, y + h + gap, GREY_TXT, width=1.5, arrow=True)
            if t == "decision":
                _label(s, x + w / 2 + 0.05, y + h - 0.02, 0.5, 0.2, sp.get("yes", "Yes"), size=10, color=GREY_TXT, bold=True)
        if nd.get("no"):
            bx = x + w + 0.45
            _line(s, x + w, y + h / 2, bx, y + h / 2, GREY_TXT, width=1.5, arrow=True)
            _label(s, x + w + 0.02, y + h / 2 - 0.24, 0.45, 0.2, nd.get("no_label", "No"), size=10, color=GREY_TXT, bold=True)
            nb = box(s, bx, y, sp.get("no_w", 3.0), h, fill="sand", name=f"Branch {i+1}")
            tb(s, bx + 0.05, y, sp.get("no_w", 3.0) - 0.1, h, [(nd["no"], {"size": 11})], anchor=MSO_ANCHOR.MIDDLE, margin=0.04)
    if sp.get("side"):
        _side_panel(s, sp["side"], 0.64 + w + 0.45 + sp.get("no_w", 3.0) + 0.3)


def r_pathway(s, sp, im):
    """Horizontal process with optional numbered monitoring points and cards below."""
    nodes = sp["nodes"]
    n = len(nodes)
    gap = 0.32
    w = (12.05 - gap * (n - 1)) / n
    y = 1.55
    hh = sp.get("node_h", 1.35)
    for i, (head, sub) in enumerate(nodes):
        x = 0.64 + i * (w + gap)
        b = box(s, x, y, w, hh, fill=["navy", "blue", "mid"][i % 3] if not sp.get("mono") else "blue",
                shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=f"Step {i+1}")
        tb(s, x + 0.06, y + 0.05, w - 0.12, hh - 0.1,
           [(head, {"bold": True, "size": 13, "color": WHITE, "align": PP_ALIGN.CENTER, "space_after": 2}),
            (sub, {"size": 11, "color": WHITE, "align": PP_ALIGN.CENTER})], anchor=MSO_ANCHOR.MIDDLE, margin=0.03)
        if i < n - 1:
            _line(s, x + w + 0.03, y + hh / 2, x + w + gap - 0.03, y + hh / 2, GREY_TXT, width=2, arrow=True)
    marks = sp.get("markers", [])
    if marks:
        my = y + hh + 0.15
        seen = {}
        for j, (idx, text) in enumerate(marks):
            k = seen.get(idx, 0); seen[idx] = k + 1
            total = sum(1 for m in marks if m[0] == idx)
            x = 0.64 + idx * (w + gap) + w / 2 + (k - (total - 1) / 2) * 0.46
            _line(s, x, y + hh, x, my + 0.05, NAVY, width=1.5)
            circle_num(s, x - 0.19, my + 0.05, 0.38, j + 1, fill="navy", size=12)
        ly = my + 0.55
        cols = sp.get("marker_cols", 2)
        per = (len(marks) + cols - 1) // cols
        cw = (12.05 - 0.3 * (cols - 1)) / cols
        for j, (idx, text) in enumerate(marks):
            cx = 0.64 + (j // per) * (cw + 0.3)
            cy = ly + (j % per) * 0.5
            circle_num(s, cx, cy + 0.06, 0.34, j + 1, fill="navy", size=11)
            tb(s, cx + 0.45, cy, cw - 0.5, 0.48, [text], size=12, anchor=MSO_ANCHOR.MIDDLE)
    if sp.get("cards"):
        cards = sp["cards"]
        cy = y + hh + 0.35
        cw = (12.05 - 0.3 * (len(cards) - 1)) / len(cards)
        for i, (head, body) in enumerate(cards):
            card(s, 0.64 + i * (cw + 0.3), cy, cw, 6.45 - cy, head, body,
                 head=["grey", "blue", "navy"][i % 3], size=13, title_size=14, head_h=0.45)


def r_access_schematic(s, sp, im):
    """Editable schematics of AVF, AVG and tunnelled CVC (not to scale)."""
    RED = RGBColor(0xC0, 0x39, 0x2B)
    VEIN = RGBColor(0x2E, 0x6D, 0xB4)
    GRAFT = RGBColor(0x7F, 0x7F, 0x7F)
    pw, gap = 3.85, 0.25
    titles = ["AV fistula (AVF)", "AV graft (AVG)", "Tunnelled CVC"]
    for i in range(3):
        x = 0.64 + i * (pw + gap)
        box(s, x, 1.45, pw, 2.75, fill="tint", name=f"{titles[i]} panel")
        _label(s, x + 0.1, 1.5, pw - 0.2, 0.35, titles[i], size=14, color=NAVY, bold=True)
    # AVF: artery joined directly to vein
    x = 0.64
    _line(s, x + 0.3, 3.75, x + 3.55, 3.75, RED, 7, name="AVF artery")
    _line(s, x + 0.9, 3.72, x + 3.55, 2.35, VEIN, 9, name="AVF arterialised vein")
    circle = box(s, x + 0.78, 3.6, 0.28, 0.28, fill="navy", shape=MSO_SHAPE.OVAL, name="AVF anastomosis")
    _label(s, x + 0.2, 3.85, 1.6, 0.3, "Anastomosis", size=11, bold=True)
    _label(s, x + 2.4, 3.8, 1.3, 0.3, "Artery", size=11, color=RED, bold=True)
    _label(s, x + 2.05, 2.05, 1.7, 0.3, "Vein (arterialised)", size=11, color=VEIN, bold=True)
    _label(s, x + 0.25, 2.0, 1.6, 0.5, "Own vessels; needles go into the vein", size=10)
    # AVG: synthetic tube between artery and vein
    x = 0.64 + pw + gap
    _line(s, x + 0.3, 3.75, x + 3.55, 3.75, RED, 7, name="AVG artery")
    _line(s, x + 0.3, 2.35, x + 3.55, 2.35, VEIN, 7, name="AVG vein")
    _line(s, x + 0.8, 3.72, x + 3.0, 2.38, GRAFT, 11, name="AVG synthetic graft")
    _label(s, x + 2.4, 3.8, 1.3, 0.3, "Artery", size=11, color=RED, bold=True)
    _label(s, x + 2.6, 2.0, 1.1, 0.3, "Vein", size=11, color=VEIN, bold=True)
    _label(s, x + 0.25, 2.65, 1.75, 0.45, "Synthetic graft: needles go into the graft", size=10, color=INK)
    # CVC: catheter in internal jugular vein, tip near right atrium, tunnel to chest exit site
    x = 0.64 + 2 * (pw + gap)
    _line(s, x + 1.2, 1.95, x + 1.2, 3.55, VEIN, 12, name="Jugular vein and SVC")
    ra = box(s, x + 0.95, 3.5, 0.55, 0.5, fill=RGBColor(0x8E, 0x44, 0xAD), shape=MSO_SHAPE.OVAL, name="Right atrium")
    _line(s, x + 1.2, 2.2, x + 1.2, 3.45, NAVY, 3, name="Catheter in vein")
    _line(s, x + 1.2, 2.2, x + 2.5, 3.2, NAVY, 3, name="Subcutaneous tunnel")
    box(s, x + 2.05, 2.8, 0.18, 0.12, fill="grey", name="Cuff")
    exit_ = box(s, x + 2.42, 3.13, 0.18, 0.18, fill="white", line="navy", shape=MSO_SHAPE.OVAL, name="Exit site")
    _line(s, x + 2.5, 3.22, x + 3.2, 3.75, NAVY, 3, name="External limbs")
    _label(s, x + 0.15, 1.85, 1.0, 0.45, "Internal jugular vein", size=10, color=VEIN, bold=True)
    _label(s, x + 0.1, 3.55, 0.85, 0.45, "Tip near right atrium", size=10, bold=True)
    _label(s, x + 2.3, 2.5, 1.0, 0.3, "Cuff", size=10)
    _label(s, x + 2.65, 3.0, 1.15, 0.3, "Exit site", size=10, bold=True)
    _label(s, x + 2.5, 3.75, 1.3, 0.35, "Red/blue hubs", size=10)
    _chart_note(s, 0.64, 4.22, 12.05, "Editable schematic, not to scale. Sites and configurations vary: follow the access record and surgical/radiology notes.")
    for i, (head, body) in enumerate(sp["implications"]):
        x = 0.64 + i * (pw + gap)
        card(s, x, 4.6, pw, 1.85, head, body, head=["blue", "mid", "navy"][i], size=12, title_size=13, head_h=0.42)


def r_zones(s, sp, im):
    zones = sp["zones"]
    n = len(zones)
    gap = 0.55
    w = (12.05 - gap * (n - 1)) / n
    fills = ["mid", "blue", "grey"]
    for i, (head, items) in enumerate(zones):
        x = 0.64 + i * (w + gap)
        box(s, x, 1.5, w, 3.6, fill="tint", name=f"{head} zone")
        hb = box(s, x, 1.5, w, 0.55, fill=fills[i % 3], name=f"{head} header")
        tf = hb.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; tf.margin_left = Inches(0.12)
        r = tf.paragraphs[0].add_run(); r.text = head; r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = WHITE
        tb(s, x + 0.1, 2.15, w - 0.2, 2.9, [(t, {"bullet": True, "space_after": 6}) for t in items], size=13)
        if i < n - 1:
            a = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + w + 0.07), Inches(3.0), Inches(gap - 0.14), Inches(0.5))
            a.fill.solid(); a.fill.fore_color.rgb = NAVY; a.line.fill.background(); a.name = "One-way arrow"
    box(s, 0.64, 5.3, 12.05, 1.15, fill="navy", name="Rule")
    tb(s, 0.84, 5.3, 11.65, 1.15, [(sp["rule_head"], {"bold": True, "size": 15, "color": WHITE, "space_after": 3}),
                                   (sp["rule"], {"size": 13, "color": WHITE})], anchor=MSO_ANCHOR.MIDDLE)


def r_pdsa(s, sp, im):
    cd = CategoryChartData()
    cd.categories = ["Plan", "Do", "Study", "Act"]
    cd.add_series("PDSA", [1, 1, 1, 1])
    gf = s.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT, Inches(0.64), Inches(1.45), Inches(4.6), Inches(4.6), cd)
    gf.name = "PDSA cycle"
    ch = gf.chart
    style_chart(ch, 12)
    ch.has_title = False
    ch.has_legend = False
    plot = ch.plots[0]
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.show_value = False; dl.show_category_name = True
    dl.font.size = Pt(14); dl.font.bold = True; dl.font.color.rgb = WHITE
    for i, col in enumerate([NAVY, BLUE, MID, GREY]):
        pt = plot.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = col
        pt.format.line.color.rgb = WHITE
    _label(s, 2.0, 3.45, 1.9, 0.6, sp.get("centre", "PDSA"), size=16, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    for i, (head, body) in enumerate(sp["steps"]):
        y = 1.45 + i * 1.25
        box(s, 5.6, y, 7.09, 1.12, fill="tint", name=f"{head} card")
        hb = box(s, 5.6, y, 1.35, 1.12, fill=["navy", "blue", "mid", "grey"][i], name=f"{head} label")
        tf = hb.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = head; r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = WHITE
        tb(s, 7.05, y, 5.55, 1.12, [body], size=12, anchor=MSO_ANCHOR.MIDDLE)
    _chart_note(s, 0.64, 6.12, 4.8, ILLUSTRATIVE)


def r_emergency(s, sp, im):
    """Emergency card: circuit action badge + four quadrants (signs, priorities, avoid, escalate)."""
    level = sp.get("circuit_level", "stop")
    fill = {"stop": NAVY, "continue": MID, "protocol": BLUE}[level]
    b = box(s, 0.64, 1.45, 12.05, 0.62, fill=fill, name="Circuit action")
    tb(s, 0.84, 1.45, 11.65, 0.62, [("Circuit: " + sp["circuit"], {"bold": True, "size": 15, "color": WHITE})],
       anchor=MSO_ANCHOR.MIDDLE)
    quads = [("Warning signs", sp["signs"], "mid"), ("Immediate nursing priorities", sp["priorities"], "blue"),
             ("Avoid", sp["avoid"], "grey"), ("Escalate", sp["escalate"], "navy")]
    cw, chh = 5.9, 2.06
    for i, (head, body, col) in enumerate(quads):
        x = 0.64 + (i % 2) * (cw + 0.25)
        y = 2.25 + (i // 2) * (chh + 0.15)
        card(s, x, y, cw, chh, head, body, head=col, size=12, title_size=13, head_h=0.4)


def r_two_images(s, sp, im):
    pics = sp["images"]
    w = (12.05 - 0.3) / 2
    for i, (key, alt, head, body) in enumerate(pics):
        x = 0.64 + i * (w + 0.3)
        picture_fit(s, im[key], x, 1.45, w, 2.75, alt)
        card(s, x, 4.3, w, 2.15, head, body, head=["blue", "mid"][i], size=12, title_size=14, head_h=0.42)
    if sp.get("caption"):
        _chart_note(s, 0.64, 4.0, 12.05, sp["caption"])


def r_image_side(s, sp, im):
    """One large uploaded picture with annotations panel on the right."""
    w = sp.get("img_w", 7.3)
    picture_fit(s, im[sp["image"]], 0.64, 1.45, w, 4.55, sp["image_alt"])
    _chart_note(s, 0.64, 6.05, w, sp["caption"])
    _side_panel(s, sp["side"], 0.64 + w + 0.3)


def r_bar_side(s, sp, im):
    """Single or clustered column chart + side panel; generalised bar_compare with note."""
    r_bar_compare(s, sp, im)
    if sp["chart"].get("note"):
        _chart_note(s, 0.64, 6.12, 7.4, sp["chart"]["note"])



RENDER = {
    "agenda": r_agenda, "split_cards": r_split_cards, "criteria": r_criteria,
    "image_two_lists": r_image_two_lists, "columns": r_columns, "table_side": r_table_side,
    "water": r_water, "adequacy": r_adequacy, "table_pie": r_table_pie, "flow": r_flow,
    "rule6": r_rule6, "image_cards": r_image_cards, "bar_compare": r_bar_compare,
    "six_grid": r_six_grid, "two_cards": r_two_cards, "compartments": r_compartments,
    "levers": r_levers, "ufr": r_ufr, "table_only": r_table_only, "electrolytes": r_electrolytes,
    "takeaways": r_takeaways, "references": r_references,
    "steps": r_steps, "checklist": r_checklist, "case": r_case, "stat_cards": r_stat_cards,
    "formula": r_formula, "matrix": r_matrix,
    "opening": r_opening, "kcheck": r_kcheck, "line_chart": r_line_chart, "stacked": r_stacked,
    "dashboard": r_dashboard, "algorithm": r_algorithm, "pathway": r_pathway,
    "access_schematic": r_access_schematic, "zones": r_zones, "pdsa": r_pdsa, "emergency": r_emergency,
    "two_images": r_two_images, "image_side": r_image_side, "bar_side": r_bar_side,
}


# -------------------------------------------------------------------- main ---
def build(mod, out, template, images):
    """Build one deck from a content module (see content.py / lectures/Lxx.py)."""
    global FOOTER_TEXT
    FOOTER_TEXT = mod.FOOTER_TEXT
    prs = Presentation(template)          # opened read-only; saved under a new name
    delete_slides(prs, keep={KEEP_TITLE_IDX, KEEP_END_IDX})
    title_slide, end_slide = prs.slides[0], prs.slides[1]

    for sh in title_slide.shapes:
        if sh.is_placeholder and sh.placeholder_format.idx == 20:
            set_text_keep_format(sh, [mod.TITLE])
            if len(mod.TITLE) > 34:
                for r in sh.text_frame.paragraphs[0].runs:
                    r.font.size = Pt(22 if len(mod.TITLE) > 60 else 26)
            p = sh.text_frame.add_paragraph()
            r = p.add_run(); r.text = mod.SUBTITLE; r.font.size = Pt(14); r.font.bold = False
        elif sh.is_placeholder and sh.placeholder_format.idx == 22:
            set_text_keep_format(sh, [mod.DATE_LOCATION])
        elif sh.shape_type == 17 and sh.has_text_frame and "Elsehemy" in sh.text_frame.text:
            set_text_keep_format(sh, mod.PRESENTER)
            sh.top = Inches(6.45)
            for p in sh.text_frame.paragraphs:
                p.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(13)
    notes(title_slide, mod.SLIDES[0]["notes"])

    for spec in mod.SLIDES[1:]:
        if spec.get("refs") == "AUTO":
            from program.sources import S as _SRC
            spec = dict(spec, refs=[_SRC[i]["cite"] for i in mod.REFS])
        if spec["kind"] == "chapter":
            build_chapter(prs, spec)
        else:
            build_content(prs, spec, images)

    lst = prs.slides._sldIdLst
    end_id = lst[1]
    lst.remove(end_id)
    lst.append(end_id)
    for sh in end_slide.placeholders:
        if sh.placeholder_format.idx == 21:
            sh.text_frame.text = "Questions and discussion"
    notes(end_slide, getattr(mod, "END_NOTES", "Thank you. Questions and discussion."))

    prs.core_properties.title = mod.TITLE
    prs.core_properties.subject = mod.SUBTITLE
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    print("Saved", out)


PROGRAM = [("D1_01_Pre_Dialysis_Assessment", "program.D1_01"),
           ("D1_02_Fluid_Assessment_UF_Safety", "program.D1_02"),
           ("D2_03_Vascular_Access_Care", "program.D2_03"),
           ("D2_04_Infection_Prevention", "program.D2_04"),
           ("D3_05_Dialysis_Adequacy", "program.D3_05"),
           ("D3_06_Water_Dialysate_Safety", "program.D3_06"),
           ("D4_07_Hemodialysis_Emergencies", "program.D4_07"),
           ("D4_08_Quality_Indicators", "program.D4_08")]


def build_program(template, images, only=None):
    """Build the eight programme decks and the source register."""
    import csv
    import importlib
    from program.sources import S
    out_dir = os.path.join(ROOT, "output", "program")
    used = {}
    for fname, modname in PROGRAM:
        mod = importlib.import_module(modname)
        for sid in mod.REFS:
            if sid not in S:
                raise KeyError(f"{modname}: unknown source id {sid}")
            used.setdefault(sid, []).append(fname[:5])
        if only and only not in fname:
            continue
        build(mod, os.path.join(out_dir, fname + ".pptx"), template, images)
    rows = [(sid, S[sid]["kind"], S[sid]["status"], ", ".join(used.get(sid, [])) or "-", S[sid]["cite"], S[sid]["url"])
            for sid in S]
    with open(os.path.join(out_dir, "Source_Register.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Type", "Verification status (13 Nov 2026)", "Used in", "Reference", "Link"])
        w.writerows(rows)
    with open(os.path.join(out_dir, "Source_Register.md"), "w", encoding="utf-8") as f:
        f.write("# Source register: 4-day hemodialysis nursing programme\n\n")
        f.write("Verification status: *Uploaded* = read from uploaded AREP screenshots; *Web-verified* = key statements "
                "confirmed by web search (13 Nov 2026); *Secondary only* = primary text not reachable, summaries used; "
                "*Not accessed* = textbook/standard knowledge, reviewer must check.\n\n")
        f.write("| ID | Type | Status | Used in | Reference | Link |\n|---|---|---|---|---|---|\n")
        for r in rows:
            f.write("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |\n")
    print("Saved source register")


def main():
    import importlib
    import sys
    sys.path.insert(0, os.path.join(ROOT, "build"))
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default=os.path.join(ROOT, "Multiorgan Support With Outline  -  Repaired.pptx"))
    ap.add_argument("--zips", default=ROOT, help="folder holding Dialysis.zip, vascular access.zip …")
    ap.add_argument("--deck", default="fundamentals",
                    help="'fundamentals' (overview deck), 'all-lectures', or a lecture id such as L03")
    ap.add_argument("--out", default=None, help="output path (single deck only)")
    args = ap.parse_args()

    images = crop_images(args.zips, os.path.join(ROOT, "build", "images"))
    if args.deck == "program":
        build_program(args.template, images)
        return
    if args.deck == "fundamentals":
        mod = importlib.import_module("content")
        build(mod, args.out or os.path.join(ROOT, "output", "Hemodialysis_Fundamentals_FMC.pptx"),
              args.template, images)
        return
    ids = [f"L{i:02d}" for i in range(1, 9)] if args.deck == "all-lectures" else [args.deck]
    for lid in ids:
        mod = importlib.import_module(f"lectures.{lid}")
        out = args.out if (args.out and len(ids) == 1) else os.path.join(
            ROOT, "output", "lectures", f"{lid}_{mod.SLUG}.pptx")
        build(mod, out, args.template, images)


if __name__ == "__main__":
    main()
