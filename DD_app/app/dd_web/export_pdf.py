from __future__ import annotations

import argparse
import io
import re
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Frame, Paragraph


ROOT = Path(__file__).resolve().parents[2]
PAGE_W, PAGE_H = A4

TEAL = colors.HexColor("#12B8C4")
TEAL_DARK = colors.HexColor("#0F8390")
NAVY = colors.HexColor("#091824")
TEXT = colors.HexColor("#182533")
MUTED = colors.HexColor("#6F8192")
LINE = colors.HexColor("#D9E1E6")
CARD_LINE = colors.HexColor("#B7E2E6")
CARD_FILL = colors.HexColor("#FCFEFE")
WARN_FILL = colors.HexColor("#FFF7E8")
WARN_LINE = colors.HexColor("#E8B15A")
WHITE = colors.white

LOGO_TOP = ROOT / "assets" / "brand" / "mca_logo_top.jpg"
LOGO_FOOTER = ROOT / "assets" / "brand" / "mca_logo_footer_transparent.png"
FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


@dataclass
class DDReport:
    company: str
    subtitle: str
    meta: list[str]
    bottom_line: str
    snapshot: list[tuple[str, str]]
    news: list[str]
    watchouts: list[str]
    questions: list[str]
    sources: list[str]
    meeting_prep: dict[str, list[str]]
    product_breakdown: dict[str, list[str]]
    market_landscape: dict[str, list[str]]
    evidence_matrix: dict[str, list[str]]


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


def styles() -> dict[str, ParagraphStyle]:
    return {
        "eyebrow": ParagraphStyle("eyebrow", fontName=FONT_BOLD, fontSize=6.6, leading=8.0, textColor=TEAL_DARK),
        "muted": ParagraphStyle("muted", fontName=FONT_REGULAR, fontSize=7.4, leading=10.2, textColor=MUTED),
        "body": ParagraphStyle("body", fontName=FONT_REGULAR, fontSize=8.2, leading=11.4, textColor=TEXT),
        "body_small": ParagraphStyle("body_small", fontName=FONT_REGULAR, fontSize=7.35, leading=10.0, textColor=TEXT),
        "body_dark": ParagraphStyle("body_dark", fontName=FONT_REGULAR, fontSize=8.0, leading=11.3, textColor=colors.HexColor("#DDEAF0")),
        "card_title": ParagraphStyle("card_title", fontName=FONT_BOLD, fontSize=7.4, leading=9.0, textColor=NAVY),
        "section_note": ParagraphStyle("section_note", fontName=FONT_REGULAR, fontSize=7.0, leading=9.0, textColor=MUTED),
        "question": ParagraphStyle("question", fontName=FONT_REGULAR, fontSize=8.1, leading=11.8, textColor=TEXT, alignment=TA_LEFT),
        "source": ParagraphStyle("source", fontName=FONT_REGULAR, fontSize=6.25, leading=8.1, textColor=TEXT),
        "prep_body": ParagraphStyle("prep_body", fontName=FONT_REGULAR, fontSize=7.65, leading=10.8, textColor=TEXT),
        "prep_dark": ParagraphStyle("prep_dark", fontName=FONT_REGULAR, fontSize=8.1, leading=11.5, textColor=colors.HexColor("#DDEAF0")),
    }


def tracked(text: str) -> str:
    return " ".join(text.upper())


def clean_inline(text: str) -> str:
    text = re.sub(r"\s*\[Source\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    tokens = {
        "<b>": "__B_OPEN__",
        "</b>": "__B_CLOSE__",
        "<br/>": "__BR__",
    }
    for tag, token in tokens.items():
        text = text.replace(tag, token)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    for tag, token in tokens.items():
        text = text.replace(token, tag)
    return text


def plain(text: str) -> str:
    text = re.sub(r"\s*\[Source\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def clip(text: str, limit: int) -> str:
    text = plain(text)
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:")
    cut = re.sub(r"\b(and|or|with|by|to|plus|for|of)$", "", cut, flags=re.IGNORECASE).rstrip(" ,;:")
    return cut + "."


def parse_sections(markdown: str) -> dict[str, list[str]]:
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


def numbered_items(lines: list[str]) -> list[str]:
    items: list[str] = []
    for line in lines:
        match = re.match(r"^\d+\.\s+(.*)", line)
        if match:
            items.append(match.group(1).strip())
        elif line and not line.startswith("|") and not line.startswith("---"):
            items.append(line)
    return items


def table_rows(lines: list[str]) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in lines:
        if not line.startswith("|") or "---" in line or "Field" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2:
            rows.append((plain(cells[0]), plain(cells[1])))
    return rows


def subsection_bullets(lines: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    current = ""
    for line in lines:
        if line.startswith("### "):
            current = plain(line[4:])
            out[current] = []
        elif current and line.startswith("- "):
            out[current].append(plain(line[2:]))
        elif current and line:
            out[current].append(plain(line))
    return out


def parse_report(markdown: str) -> DDReport:
    sections = parse_sections(markdown)
    header = sections.get("Header", [])
    title = next((line[2:].strip() for line in header if line.startswith("# ")), "Company | Executive DD")
    if "|" in title:
        company, subtitle = [part.strip() for part in title.split("|", 1)]
    else:
        company, subtitle = title, "Executive DD"
    meta = [plain(line) for line in header if line.startswith("**")]
    bottom_line = " ".join(line for line in sections.get("Bottom Line", []) if not line.startswith("#"))
    return DDReport(
        company=company,
        subtitle=subtitle,
        meta=meta,
        bottom_line=plain(bottom_line),
        snapshot=table_rows(sections.get("Company Snapshot", [])),
        news=numbered_items(sections.get("Last 30 Days", [])),
        watchouts=numbered_items(sections.get("DD Watchouts", [])),
        questions=numbered_items(sections.get("Call Priorities", [])),
        sources=numbered_items(sections.get("Sources", [])),
        meeting_prep=subsection_bullets(sections.get("Meeting Prep", [])),
        product_breakdown=subsection_bullets(sections.get("Product Breakdown", [])),
        market_landscape=subsection_bullets(sections.get("Market Landscape", [])),
        evidence_matrix=subsection_bullets(sections.get("Evidence Matrix", [])),
    )


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean_inline(text), style)


def draw_para(c, text: str, style: ParagraphStyle, x: float, y_top: float, w: float, h: float) -> None:
    frame = Frame(x, y_top - h, w, h, showBoundary=0, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame.addFromList([para(text, style)], c)


def draw_image(c, path: Path, x: float, y: float, width: float) -> None:
    if not path.exists():
        return
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
        c.rect(strip_x, y, w / steps + 0.8, h, stroke=0, fill=1)
    c.restoreState()


def draw_top_brand(c) -> None:
    draw_horizontal_gradient(c, 0, PAGE_H - 4, PAGE_W, 4, TEAL_DARK, TEAL)


def draw_footer(c) -> None:
    draw_horizontal_gradient(c, 0, 0, PAGE_W, 44, TEAL_DARK, TEAL)
    draw_image(c, LOGO_FOOTER, 45, 12, 62)
    c.setFillColor(WHITE)
    c.setFont(FONT_REGULAR, 6.8)
    c.drawCentredString(PAGE_W * 0.78, 19, tracked("Company DD - Confidential"))


def draw_header(c, label: str = "Company DD") -> None:
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
    c.drawRightString(PAGE_W - 45, PAGE_H - 55, tracked(label))


def draw_badge(c, text: str, x: float, y: float, fill=TEAL_DARK) -> None:
    w = max(42, pdfmetrics.stringWidth(text.upper(), FONT_BOLD, 5.8) + 13)
    c.setFillColor(fill)
    c.roundRect(x, y - 12, w, 14, 7, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont(FONT_BOLD, 5.8)
    c.drawCentredString(x + w / 2, y - 7.6, text.upper())


def split_watchout(item: str) -> tuple[str, str, str, str]:
    clean = plain(item)
    match = re.match(r"^([^|.]+)\s*\|\s*([^|.]+)\s*\|\s*([^.]*)\.\s*(.*)", clean)
    if not match:
        return "Watchout", "", clean, ""
    severity, status, title, body = match.groups()
    body = re.sub(r"\s+Source$", "", body.strip())
    return severity.strip(), status.strip(), title.strip(), body


def prep_items(report: DDReport, key: str, fallback: list[str], limit: int = 4) -> list[str]:
    items = report.meeting_prep.get(key) or fallback
    return [plain(item) for item in items[:limit]]


def watchout_titles(report: DDReport) -> list[str]:
    return [split_watchout(item)[2] for item in report.watchouts if split_watchout(item)[2]]


def draw_panel(c, title: str, items: list[str], x: float, y: float, w: float, h: float, max_chars: int = 92) -> None:
    s = styles()
    c.setFillColor(CARD_FILL)
    c.setStrokeColor(CARD_LINE)
    c.setLineWidth(0.85)
    c.roundRect(x, y - h, w, h, 7, stroke=1, fill=1)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.35)
    c.line(x + 5, y, x + w - 5, y)
    draw_para(c, title, s["card_title"], x + 12, y - 13, w - 24, 13)
    item_y = y - 34
    for item in items[:4]:
        c.setFillColor(TEAL_DARK)
        c.circle(x + 16, item_y - 4.8, 2.2, stroke=0, fill=1)
        draw_para(c, clip(item, max_chars), s["prep_body"], x + 25, item_y, w - 38, 34)
        item_y -= 36


def draw_page_three(c, report: DDReport) -> None:
    s = styles()
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 34

    draw_top_brand(c)
    draw_footer(c)

    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, top, "Product and traction")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, top - 15, "What the company is actually trying to build and what needs proof.")

    product_thesis = prep_items(
        report,
        "Product Thesis",
        [report.bottom_line],
        limit=1,
    )[0]
    c.setFillColor(NAVY)
    c.roundRect(left, top - 102, right - left, 62, 8, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.setFont(FONT_BOLD, 6.8)
    c.drawString(left + 14, top - 56, tracked("Product thesis"))
    draw_para(c, clip(product_thesis, 210), s["prep_dark"], left + 14, top - 71, right - left - 28, 38)

    col_gap = 12
    col_w = (right - left - col_gap) / 2
    row_h = 180
    first_y = top - 132
    second_y = first_y - row_h - 14

    product = report.product_breakdown or {}
    panels = list(product.items())[:4]
    if len(panels) < 4:
        snapshot_fallback = {
            "What it does": [value for field, value in report.snapshot if field.lower() == "what it does"],
            "Customer": [value for field, value in report.snapshot if field.lower() == "customer"],
            "Business model": [value for field, value in report.snapshot if field.lower() == "business model"],
            "Traction": [value for field, value in report.snapshot if "traction" in field.lower()],
        }
        panels.extend((key, value) for key, value in snapshot_fallback.items() if value)
    panels = panels[:4]

    positions = [
        (left, first_y),
        (left + col_w + col_gap, first_y),
        (left, second_y),
        (left + col_w + col_gap, second_y),
    ]
    for (title, items), (x, y) in zip(panels, positions):
        draw_panel(c, title, items, x, y, col_w, row_h)

    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 6.6)
    c.drawString(left, 62, "Use this page to separate live product evidence from roadmap or narrative.")


def draw_page_four(c, report: DDReport) -> None:
    s = styles()
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 34

    draw_top_brand(c)
    draw_footer(c)

    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, top, "Market and competitors")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, top - 15, "Where the company sits versus direct, adjacent, and substitute offerings.")

    col_gap = 12
    col_w = (right - left - col_gap) / 2
    row_h = 178
    first_y = top - 42
    second_y = first_y - row_h - 14
    market = report.market_landscape or {
        "Direct competitors": prep_items(report, "Market Map", [], limit=4),
        "Sector context": [
            "Map companies by customer job, not token category.",
            "Ask which incumbent or centralized workflow the buyer would replace.",
            "Separate infrastructure supply from revenue-generating demand.",
        ],
    }
    panels = list(market.items())[:4]
    positions = [
        (left, first_y),
        (left + col_w + col_gap, first_y),
        (left, second_y),
        (left + col_w + col_gap, second_y),
    ]
    for (title, items), (x, y) in zip(panels, positions):
        draw_panel(c, title, items, x, y, col_w, row_h, 118)

    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 6.6)
    c.drawString(left, 62, "Competitor pages should name companies, verticals, substitutes, and the evidence bar for differentiation.")


def draw_page_five(c, report: DDReport) -> None:
    s = styles()
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 34

    draw_top_brand(c)
    draw_footer(c)

    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, top, "Evidence gaps and call plan")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, top - 15, "What to verify before MCA spends more time.")

    stance = prep_items(
        report,
        "Recommended Stance",
        ["Take the call, but keep it proof-led. Push for evidence on traction, economics, legal structure, and what would de-risk MCA's next step."],
        limit=1,
    )[0]
    c.setFillColor(NAVY)
    c.roundRect(left, top - 92, right - left, 52, 8, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.setFont(FONT_BOLD, 6.8)
    c.drawString(left + 14, top - 56, tracked("Recommended stance"))
    draw_para(c, clip(stance, 210), s["prep_dark"], left + 14, top - 71, right - left - 28, 28)

    col_gap = 12
    col_w = (right - left - col_gap) / 2
    row_h = 168
    first_y = top - 120
    second_y = first_y - row_h - 14

    proof = prep_items(report, "Proof To Request", report.questions, limit=4)
    signals = prep_items(
        report,
        "Lean-In Signals",
        [
            "The company can show traction data that is independent of token incentives.",
            "The team can explain the wedge in one sentence and support it with live evidence.",
        ],
        limit=4,
    )
    red_flags = prep_items(report, "Deal-Killer Answers", watchout_titles(report), limit=4)
    evidence = report.evidence_matrix.get("Open Gaps") or report.evidence_matrix.get("Need From Team") or red_flags

    draw_panel(c, "Proof to request", proof, left, first_y, col_w, row_h, 88)
    draw_panel(c, "Lean-in signals", signals, left + col_w + col_gap, first_y, col_w, row_h, 88)
    draw_panel(c, "Deal-killer answers", red_flags, left, second_y, col_w, row_h, 88)
    draw_panel(c, "Open evidence gaps", evidence, left + col_w + col_gap, second_y, col_w, row_h, 88)

    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 6.6)
    c.drawString(left, 62, "Use this page to drive the call toward proof, not category enthusiasm.")


def draw_page_one(c, report: DDReport) -> None:
    s = styles()
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 92

    draw_header(c, "Executive Brief")
    draw_footer(c)

    draw_para(c, tracked("Considerations & Next Steps"), s["eyebrow"], left, top, 260, 11)
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 28)
    c.drawString(left, top - 31, report.company)
    draw_para(c, report.subtitle, s["muted"], left, top - 51, 330, 16)

    meta_y = top - 2
    for line in report.meta[:3]:
        draw_para(c, line, s["muted"], right - 230, meta_y, 230, 12)
        meta_y -= 13

    brief_y = top - 82
    c.setFillColor(NAVY)
    c.roundRect(left, brief_y - 78, right - left, 78, 8, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.setFont(FONT_BOLD, 6.8)
    c.drawString(left + 14, brief_y - 19, tracked("In Brief"))
    draw_para(c, clip(report.bottom_line, 620), s["body_dark"], left + 14, brief_y - 34, right - left - 28, 48)

    snapshot_y = brief_y - 104
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left, snapshot_y, "Company snapshot")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.0)
    c.drawString(left, snapshot_y - 15, "Core facts to orient the call.")

    card_gap = 10
    card_w = (right - left - card_gap) / 2
    card_h = 58
    for idx, (field, read) in enumerate(report.snapshot[:6]):
        col = idx % 2
        row = idx // 2
        x = left + col * (card_w + card_gap)
        y = snapshot_y - 32 - row * (card_h + 8)
        c.setFillColor(CARD_FILL)
        c.setStrokeColor(CARD_LINE)
        c.setLineWidth(0.8)
        c.roundRect(x, y - card_h, card_w, card_h, 7, stroke=1, fill=1)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.3)
        c.line(x + 5, y, x + card_w - 5, y)
        draw_para(c, field, s["card_title"], x + 11, y - 12, card_w - 22, 12)
        draw_para(c, clip(read, 108), s["body_small"], x + 11, y - 27, card_w - 22, 30)

    news_y = snapshot_y - 238
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left, news_y, "Last 30 days")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.0)
    c.drawString(left, news_y - 15, "Validated items in the stated research window.")
    y = news_y - 34
    for idx, item in enumerate(report.news[:3], start=1):
        c.setFillColor(TEAL_DARK)
        c.circle(left + 7, y - 5, 7, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont(FONT_BOLD, 6.7)
        c.drawCentredString(left + 7, y - 7.5, str(idx))
        draw_para(c, clip(item, 220), s["body"], left + 22, y, right - left - 22, 42)
        y -= 45


def draw_page_two(c, report: DDReport) -> None:
    s = styles()
    left = 45
    right = PAGE_W - 45
    top = PAGE_H - 34

    draw_top_brand(c)
    draw_footer(c)

    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, top, "DD watchouts")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, top - 15, "Items MCA should validate before leaning in.")

    y = top - 36
    row_h = 72
    for item in report.watchouts[:5]:
        severity, status, title, body = split_watchout(item)
        fill = colors.HexColor("#B0442E") if severity.lower() == "high" else TEAL_DARK
        draw_badge(c, severity, left, y, fill)
        if status:
            c.setFillColor(MUTED)
            c.setFont(FONT_BOLD, 6.2)
            c.drawString(left + 55, y - 9, tracked(status))
        c.setFillColor(NAVY)
        c.setFont(FONT_BOLD, 9.2)
        c.drawString(left + 132, y - 9, clip(title, 60))
        draw_para(c, clip(body, 290), s["body"], left + 132, y - 23, right - left - 132, 37)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.line(left, y - row_h + 7, right, y - row_h + 7)
        y -= row_h

    q_top = y - 4
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 16)
    c.drawString(left, q_top, "Call priorities")
    c.setFillColor(MUTED)
    c.setFont(FONT_REGULAR, 7.2)
    c.drawString(left, q_top - 15, "Use these to force the discussion toward proof.")

    q_y = q_top - 36
    for idx, question in enumerate(report.questions[:3], start=1):
        c.setFillColor(NAVY)
        c.circle(left + 8, q_y - 8, 8.4, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont(FONT_BOLD, 7.8)
        c.drawCentredString(left + 8, q_y - 10.8, str(idx))
        draw_para(c, clip(question, 230), s["question"], left + 26, q_y, right - left - 26, 37)
        q_y -= 47

    source_top = max(102, q_y - 2)
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 10.5)
    c.drawString(left, source_top, "Sources")
    source_y = source_top - 14
    for idx, source in enumerate(report.sources[:7], start=1):
        draw_para(c, f"{idx}. {clip(source, 118)}", s["source"], left, source_y, right - left, 9)
        source_y -= 8.8


def build_pdf_bytes(markdown: str) -> bytes:
    from reportlab.pdfgen import canvas

    report = parse_report(markdown)
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setTitle(f"{report.company} MCA Company DD")
    draw_page_one(c, report)
    c.showPage()
    draw_page_two(c, report)
    c.showPage()
    draw_page_three(c, report)
    c.showPage()
    draw_page_four(c, report)
    c.showPage()
    draw_page_five(c, report)
    c.save()
    return buffer.getvalue()


def build_pdf_file(input_md: Path, output_pdf: Path) -> None:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    output_pdf.write_bytes(build_pdf_bytes(input_md.read_text(encoding="utf-8")))


def main() -> None:
    parser = argparse.ArgumentParser(description="Export an MCA-style DD PDF")
    parser.add_argument("input", type=Path, help="Markdown DD report")
    parser.add_argument("output", type=Path, help="Output PDF path")
    args = parser.parse_args()
    build_pdf_file(args.input, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
