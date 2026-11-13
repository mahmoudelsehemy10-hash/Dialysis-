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

from content import SLIDES, FOOTER_TEXT, TITLE, SUBTITLE, PRESENTER, DATE_LOCATION

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
             head=["navy", "blue", "mid", "blue"][i % 4], size=12, title_size=14, head_h=0.55)
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
                            Inches(4.9), cd)
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


RENDER = {
    "agenda": r_agenda, "split_cards": r_split_cards, "criteria": r_criteria,
    "image_two_lists": r_image_two_lists, "columns": r_columns, "table_side": r_table_side,
    "water": r_water, "adequacy": r_adequacy, "table_pie": r_table_pie, "flow": r_flow,
    "rule6": r_rule6, "image_cards": r_image_cards, "bar_compare": r_bar_compare,
    "six_grid": r_six_grid, "two_cards": r_two_cards, "compartments": r_compartments,
    "levers": r_levers, "ufr": r_ufr, "table_only": r_table_only, "electrolytes": r_electrolytes,
    "takeaways": r_takeaways, "references": r_references,
}


# -------------------------------------------------------------------- main ---
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default=os.path.join(ROOT, "Multiorgan Support With Outline  -  Repaired.pptx"))
    ap.add_argument("--zips", default=ROOT, help="folder holding Dialysis.zip, vascular access.zip …")
    ap.add_argument("--out", default=os.path.join(ROOT, "output", "Hemodialysis_Fundamentals_FMC.pptx"))
    args = ap.parse_args()

    images = crop_images(args.zips, os.path.join(ROOT, "build", "images"))
    prs = Presentation(args.template)     # opened read-only; saved under a new name
    delete_slides(prs, keep={KEEP_TITLE_IDX, KEEP_END_IDX})
    title_slide, end_slide = prs.slides[0], prs.slides[1]

    # Title slide: fill the existing template placeholders / presenter text box
    for sh in title_slide.shapes:
        if sh.is_placeholder and sh.placeholder_format.idx == 20:
            set_text_keep_format(sh, [TITLE])
            # subtitle as a second, smaller paragraph
            p = sh.text_frame.add_paragraph()
            r = p.add_run(); r.text = SUBTITLE; r.font.size = Pt(14); r.font.bold = False
        elif sh.is_placeholder and sh.placeholder_format.idx == 22:
            set_text_keep_format(sh, [DATE_LOCATION])
        elif sh.shape_type == 17 and sh.has_text_frame and "Elsehemy" in sh.text_frame.text:
            set_text_keep_format(sh, PRESENTER)
            sh.top = Inches(6.45)
            for p in sh.text_frame.paragraphs:
                p.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(13)
    notes(title_slide, SLIDES[0]["notes"])

    for spec in SLIDES[1:]:
        if spec["kind"] == "chapter":
            build_chapter(prs, spec)
        else:
            build_content(prs, spec, images)

    # move the reused "Thank you" slide to the end
    lst = prs.slides._sldIdLst
    end_id = lst[1]
    lst.remove(end_id)
    lst.append(end_id)
    for sh in end_slide.placeholders:
        if sh.placeholder_format.idx == 21:
            sh.text_frame.text = "Questions and discussion"
    notes(end_slide, "Thank you. Questions and discussion.\n\nInvite participants to the AREP eLearning "
                     "modules (Introduction to Hemodialysis; Vascular Access; Fluid Management; Fluids, "
                     "Electrolytes, Acids and Bases) for self-paced review.")

    prs.core_properties.title = TITLE
    prs.core_properties.subject = SUBTITLE
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    prs.save(args.out)
    print("Saved", args.out)


if __name__ == "__main__":
    main()
