"""Generate MCA-style branded PDF deliverables."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Frame, Paragraph


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PAGE_W, PAGE_H = A4

TEAL = colors.HexColor("#12B8C4")
TEAL_DARK = colors.HexColor("#0F8390")
TEAL_FOOTER_LEFT = colors.HexColor("#0F8390")
TEAL_FOOTER_RIGHT = colors.HexColor("#12B8C4")
NAVY = colors.HexColor("#091824")
TEXT = colors.HexColor("#182533")
MUTED = colors.HexColor("#6F8192")
LINE = colors.HexColor("#D9E1E6")
CARD_LINE = colors.HexColor("#B7E2E6")
CARD_FILL = colors.HexColor("#FCFEFE")
WHITE = colors.white
LOGO_TOP = PROJECT_ROOT / "assets" / "brand" / "mca_logo_top.jpg"
LOGO_FOOTER = PROJECT_ROOT / "assets" / "brand" / "mca_logo_footer_transparent.png"
FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


def register_fonts() -> None:
    global FONT_REGULAR, FONT_BOLD
    regular = Path(r"C:\Windows\Fonts\segoeui.ttf")
    bold = Path(r"C:\Windows\Fonts\segoeuib.ttf")
    if not regular.exists() or not bold.exists():
        return
    pdfmetrics.registerFont(TTFont("MCA-Segoe", str(regular)))
    pdfmetrics.registerFont(TTFont("MCA-Segoe-Bold", str(bold)))
    pdfmetrics.registerFontFamily("MCA-Segoe", normal="MCA-Segoe", bold="MCA-Segoe-Bold")
    FONT_REGULAR = "MCA-Segoe"
    FONT_BOLD = "MCA-Segoe-Bold"


register_fonts()


def clean_inline(text: str) -> str:
    preserved = {
        "<b>": "__B_OPEN__",
        "</b>": "__B_CLOSE__",
        "<br/>": "__BR__",
        "<font color='#08A9B5'>": "__TEAL_OPEN__",
        "</font>": "__FONT_CLOSE__",
    }
    for tag, token in preserved.items():
        text = text.replace(tag, token)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    for tag, token in preserved.items():
        text = text.replace(token, tag)
    return text


def tracked(text: str) -> str:
    return " ".join(text.upper())


def load_sections(markdown: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {"Header": []}
    current = "Header"
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        else:
            sections.setdefault(current, []).append(line)
    return sections


def section_text(sections: dict[str, list[str]], name: str) -> str:
    return " ".join(line for line in sections.get(name, []) if not line.startswith("#"))


def clip(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:")
    return cut + "."


def subsections(sections: dict[str, list[str]], name: str) -> list[tuple[str, str]]:
    lines = sections.get(name, [])
    out: list[tuple[str, str]] = []
    title = ""
    body: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if title:
                out.append((title, " ".join(body)))
            title = line[4:].strip()
            body = []
        else:
            body.append(line)
    if title:
        out.append((title, " ".join(body)))
    return out


def swot_groups(sections: dict[str, list[str]]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    current = ""
    for line in sections.get("SWOT", []):
        if line.startswith("### "):
            current = line[4:].strip()
            groups[current] = []
        elif current and line.startswith("- "):
            groups[current].append(line[2:].strip())
    return groups


def questions(sections: dict[str, list[str]]) -> list[tuple[str, str, str, bool]]:
    concise_titles = {
        "1": "Retention by cohort.",
        "2": "Unit economics.",
        "3": "Vendor proof.",
        "4": "Repeat versus first-time volume.",
        "5": "Acquisition quality.",
        "6": "Competitive edge.",
        "7": "The role of Solana.",
        "8": "Compliance review.",
        "9": "The next financing milestone.",
        "10": "Next-round evidence.",
    }
    out = []
    for line in sections.get("Questions for Next Steps", []):
        match = re.match(r"^(\d+)\.\s*(.*)", line)
        if not match:
            continue
        number, question = match.groups()
        priority = question.lower().startswith("priority:")
        question = re.sub(r"^Priority:\s*", "", question, flags=re.IGNORECASE)
        if number in concise_titles:
            out.append((number, concise_titles[number], question.strip(), priority))
        elif "?" in question:
            title, body = question.split("?", 1)
            out.append((number, title.strip() + "?", body.strip(), priority))
        else:
            out.append((number, question.strip(), "", priority))
    return out


def make_styles() -> dict[str, ParagraphStyle]:
    return {
        "subtle": ParagraphStyle("subtle", fontName=FONT_REGULAR, fontSize=8.7, leading=12.8, textColor=MUTED),
        "body": ParagraphStyle("body", fontName=FONT_REGULAR, fontSize=8.8, leading=12.8, textColor=TEXT),
        "body_dark": ParagraphStyle("body_dark", fontName=FONT_REGULAR, fontSize=7.9, leading=11.1, textColor=colors.HexColor("#DDEAF0")),
        "small_head": ParagraphStyle("small_head", fontName=FONT_BOLD, fontSize=8.7, leading=10.8, textColor=NAVY),
        "small": ParagraphStyle("small", fontName=FONT_REGULAR, fontSize=7.6, leading=10.1, textColor=TEXT),
        "tiny": ParagraphStyle("tiny", fontName=FONT_REGULAR, fontSize=6.8, leading=8.8, textColor=TEXT),
        "swot": ParagraphStyle("swot", fontName=FONT_REGULAR, fontSize=7.0, leading=9.2, textColor=TEXT),
        "question_body": ParagraphStyle("question_body", fontName=FONT_REGULAR, fontSize=8.2, leading=12.1, textColor=TEXT, alignment=TA_LEFT),
    }


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean_inline(text), style)


def draw_para(c, text: str, style: ParagraphStyle, x: float, y_top: float, w: float, h: float) -> None:
    frame = Frame(x, y_top - h, w, h, showBoundary=0, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame.addFromList([para(text, style)], c)


def draw_flow(c, flowables: list[Paragraph], x: float, y_top: float, w: float, h: float) -> None:
    frame = Frame(x, y_top - h, w, h, showBoundary=0, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame.addFromList(flowables, c)


def text_width(text: str, font: str, size: float) -> float:
    from reportlab.pdfbase.pdfmetrics import stringWidth

    return stringWidth(text, font, size)


def swot_bullet(item: str) -> str:
    item = clip(item, 118)
    if "." in item:
        lead, rest = item.split(".", 1)
        return f"<b>{lead.strip()}.</b>{rest}"
    return item


def draw_swot_item(c, text: str, style: ParagraphStyle, x: float, y_top: float, w: float) -> None:
    c.setFillColor(TEAL)
    c.circle(x + 3.2, y_top - 4.8, 1.45, stroke=0, fill=1)
    draw_para(c, swot_bullet(text), style, x + 10, y_top, w - 10, 19)


def draw_image(c, path: Path, x: float, y: float, width: float) -> None:
    image = ImageReader(str(path))
    img_w, img_h = image.getSize()
    height = width * img_h / img_w
    c.drawImage(image, x, y, width=width, height=height, mask="auto")


def draw_horizontal_gradient(c, x: float, y: float, w: float, h: float, left_color, right_color, steps: int = 96) -> None:
    c.saveState()
    for idx in range(steps):
        ratio = idx / max(steps - 1, 1)
        red = left_color.red + (right_color.red - left_color.red) * ratio
        green = left_color.green + (right_color.green - left_color.green) * ratio
        blue = left_color.blue + (right_color.blue - left_color.blue) * ratio
        c.setFillColor(colors.Color(red, green, blue))
        strip_x = x + (w * idx / steps)
        strip_w = w / steps + 0.8
        c.rect(strip_x, y, strip_w, h, stroke=0, fill=1)
    c.restoreState()


def draw_top_brand(c) -> None:
    c.saveState()
    draw_horizontal_gradient(c, 0, PAGE_H - 4, PAGE_W, 4, TEAL_FOOTER_LEFT, TEAL_FOOTER_RIGHT)
    c.restoreState()


def draw_footer(c) -> None:
    c.saveState()
    draw_horizontal_gradient(c, 0, 0, PAGE_W, 48, TEAL_FOOTER_LEFT, TEAL_FOOTER_RIGHT)
    draw_image(c, LOGO_FOOTER, 45, 14, 65)
    c.setFillColor(WHITE)
    c.setFont(FONT_REGULAR, 7.0)
    c.drawCentredString(PAGE_W * 0.79, 21, tracked("Market Intelligence - Confidential"))
    c.restoreState()


def draw_header(c) -> None:
    draw_top_brand(c)
    draw_image(c, LOGO_TOP, 45, PAGE_H - 54, 73)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(45, PAGE_H - 73, PAGE_W - 45, PAGE_H - 73)
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 6)
    c.drawRightString(PAGE_W - 45, PAGE_H - 42, tracked("Market Intelligence"))
    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_BOLD, 6)
    c.drawRightString(PAGE_W - 45, PAGE_H - 55, tracked("Deal Review"))


def draw_page_one(c, sections: dict[str, list[str]]) -> None:
    s = make_styles()
    draw_header(c)
    draw_footer(c)

    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 92

    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_BOLD, 6.8)
    c.drawString(left, top, tracked("Considerations & Next Steps"))
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 32)
    c.drawString(left, top - 31, "PocketPull")
    draw_para(
        c,
        "Our initial read following the collector commerce and trading-card deck, and the questions we would like to work through with you.",
        s["subtle"],
        left,
        top - 52,
        330,
        32,
    )
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.8)
    c.drawRightString(right, top - 3, "August 2026")
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 7.8)
    c.drawRightString(right - 29, top - 20, "Prepared by")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.8)
    c.drawRightString(right, top - 20, "MCA")

    draw_para(c, section_text(sections, "Opening Note"), s["body"], left, top - 86, right - left, 42)

    brief_y = top - 148
    c.setFillColor(NAVY)
    c.roundRect(left, brief_y - 72, right - left, 72, 8, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.setFont(FONT_BOLD, 6.8)
    c.drawString(left + 14, brief_y - 19, tracked("In Brief"))
    brief_copy = (
        "PocketPull is most interesting if it becomes a retained collector commerce layer, not simply another "
        "pack-opening product. The questions are retention, vendor-powered inventory, and whether it can defend "
        "a position as Solana card platforms prove demand."
    )
    draw_flow(c, [para(brief_copy, s["body_dark"])], left + 14, brief_y - 32, right - left - 28, 43)

    read_y = brief_y - 96
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left, read_y, "Our read")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.0)
    c.drawString(left, read_y - 16, "Three things stood out on the first pass.")

    read_items = [
        (
            "The real wedge is retention, not pack volume",
            "Pack opening creates the first moment, but the value is in binders, points, levels, guilds, quests, marketplace access and repeat participation.",
        ),
        (
            "Vendor supply defines the operating model",
            "Vendor inventory is capital-light and can become distribution, but only if supply quality, fulfillment, settlement and contribution margin hold together.",
        ),
        (
            "The competitive bar is already higher",
            "Solana physical-card activity validates the timing, but PocketPull still needs a durable answer against vaulted-card, pack and marketplace platforms.",
        ),
    ]
    col_gap = 24
    col_w = (right - left - 2 * col_gap) / 3
    for idx, (title, body) in enumerate(read_items[:3]):
        x = left + idx * (col_w + col_gap)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.5)
        c.line(x, read_y - 36, x, read_y - 128)
        draw_para(c, title, s["small_head"], x + 12, read_y - 38, col_w - 12, 25)
        draw_para(c, body, s["tiny"], x + 12, read_y - 74, col_w - 12, 61)

    swot_y = read_y - 150
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left, swot_y, "SWOT")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.0)
    c.drawString(left, swot_y - 15, "Our first-pass view across the four quadrants.")

    groups = {
        "Strengths": [
            "Live product. Paid volume and pack activity give PocketPull more evidence than a deck-only concept.",
            "Retention framing. Progression, guilds and collection history point beyond one-time pack opening.",
            "Vendor-powered supply. Inventory can expand without buying every card upfront.",
        ],
        "Weaknesses": [
            "Retention unproven. The deck does not yet show cohorts, repeat purchase or guild-driven return frequency.",
            "Thin margin. The stated margin needs a contribution bridge by transaction type.",
            "Vendor dependence. Fulfillment, settlement and disputes sit outside a pure software model.",
        ],
        "Opportunities": [
            "Solana timing. Physical-card activity gives PocketPull a collector audience to build from.",
            "Idle vendor inventory. Local shops may have under-monetized supply and audiences.",
            "Persistent identity. Guilds, points and binders could turn commerce into habit.",
        ],
        "Threats": [
            "Scaled adjacent platforms. Tokenized-card, vaulting, pack and redemption products are already active.",
            "Novelty risk. Pack-opening behavior can fade without repeat purchase and retention.",
            "Operational drag. Fulfillment, authentication, disputes and shipping can make the model heavier.",
        ],
    }
    card_w = (right - left - 12) / 2
    card_h = 116
    positions = [
        ("Strengths", left, swot_y - 31),
        ("Weaknesses", left + card_w + 12, swot_y - 31),
        ("Opportunities", left, swot_y - 160),
        ("Threats", left + card_w + 12, swot_y - 160),
    ]
    for name, x, y in positions:
        c.setFillColor(CARD_FILL)
        c.setStrokeColor(CARD_LINE)
        c.setLineWidth(0.9)
        c.roundRect(x, y - card_h, card_w, card_h, 7, stroke=1, fill=1)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.4)
        c.line(x + 4, y, x + card_w - 4, y)
        c.setFillColor(TEAL_DARK)
        c.setFont(FONT_BOLD, 6.9)
        c.drawString(x + 12, y - 22, tracked(name))
        item_y = y - 39
        for item in groups.get(name, [])[:3]:
            draw_swot_item(c, item, s["swot"], x + 13, item_y, card_w - 28)
            item_y -= 25


def draw_page_two(c, sections: dict[str, list[str]]) -> None:
    s = make_styles()
    draw_top_brand(c)
    draw_footer(c)
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 35

    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, top, "Questions for next steps")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, top - 15, "In rough priority order. The first three matter most.")

    y = top - 34
    row_h = 68
    for number, title, body, priority in questions(sections):
        c.setFillColor(NAVY)
        circle_y = y - 8
        title_base = y - 10.8
        c.circle(left + 8, circle_y, 8.4, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont(FONT_BOLD, 7.8)
        c.drawCentredString(left + 8, circle_y - 2.7, number)
        title_x = left + 25
        c.setFillColor(NAVY)
        c.setFont(FONT_BOLD, 9.8)
        c.drawString(title_x, title_base, title)
        if priority:
            c.setFillColor(TEAL_DARK)
            c.setFont(FONT_BOLD, 6.0)
            c.drawRightString(right, title_base + 0.3, tracked("Priority"))
        draw_para(c, body, s["question_body"], title_x, y - 28, right - title_x, 34)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.line(left, y - row_h + 4, right, y - row_h + 4)
        y -= row_h


def build_pdf(input_md: Path, output_pdf: Path) -> None:
    from reportlab.pdfgen import canvas

    sections = load_sections(input_md.read_text(encoding="utf-8"))
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_pdf), pagesize=A4)
    c.setTitle("PocketPull MCA Market Intelligence")
    draw_page_one(c, sections)
    c.showPage()
    draw_page_two(c, sections)
    c.save()


def main() -> None:
    parser = argparse.ArgumentParser(description="Export an MCA-style branded PDF")
    parser.add_argument("--input", default="cases/pocketpull/output/final_deliverable.md")
    parser.add_argument("--output", default="cases/pocketpull/output/pocketpull_mca_market_intelligence.pdf")
    args = parser.parse_args()
    output = PROJECT_ROOT / args.output
    build_pdf(PROJECT_ROOT / args.input, output)
    print(output)


if __name__ == "__main__":
    main()
