"""Generate a fillable Brand Voice Brief PDF template.

This script produces a reusable template intended for AI-assisted social writing workflows.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "Brand_Voice_Brief_Template.pdf"


# ── Colors ────────────────────────────────────────────────────────────
NAVY = colors.HexColor("#1B2A4A")
TEAL = colors.HexColor("#00A9A5")
LIGHT = colors.HexColor("#F0F4F8")
MID = colors.HexColor("#CBD5E0")
WHITE = colors.white
GRAY = colors.HexColor("#4A5568")
LGRAY = colors.HexColor("#718096")

styles = getSampleStyleSheet()

# ── Paragraph styles ─────────────────────────────────────────────────
H1 = ParagraphStyle(
    "H1",
    parent=styles["Normal"],
    fontSize=22,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    leading=28,
    alignment=TA_CENTER,
)

H2 = ParagraphStyle(
    "H2",
    parent=styles["Normal"],
    fontSize=11,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    leading=16,
    spaceBefore=4,
    spaceAfter=4,
)

LABEL = ParagraphStyle(
    "LABEL",
    parent=styles["Normal"],
    fontSize=8,
    textColor=TEAL,
    fontName="Helvetica-Bold",
    leading=11,
    spaceBefore=2,
    spaceAfter=1,
    tracking=1,
)

BODY = ParagraphStyle(
    "BODY",
    parent=styles["Normal"],
    fontSize=9,
    textColor=GRAY,
    fontName="Helvetica",
    leading=14,
    spaceAfter=4,
)

ITALIC = ParagraphStyle(
    "ITALIC",
    parent=styles["Normal"],
    fontSize=8.5,
    textColor=LGRAY,
    fontName="Helvetica-Oblique",
    leading=13,
    spaceAfter=2,
)

FILL_LABEL = ParagraphStyle(
    "FILL_LABEL",
    parent=styles["Normal"],
    fontSize=8,
    textColor=NAVY,
    fontName="Helvetica-Bold",
    leading=12,
    spaceBefore=6,
    spaceAfter=1,
)

FILL_LINE = ParagraphStyle(
    "FILL_LINE",
    parent=styles["Normal"],
    fontSize=9,
    textColor=GRAY,
    fontName="Helvetica",
    leading=14,
    spaceAfter=2,
)

CODE = ParagraphStyle(
    "CODE",
    parent=styles["Normal"],
    fontSize=8,
    textColor=NAVY,
    fontName="Courier",
    leading=13,
    backColor=LIGHT,
    leftIndent=8,
    rightIndent=8,
    spaceBefore=4,
    spaceAfter=4,
)

FOOTER = ParagraphStyle(
    "FOOTER",
    parent=styles["Normal"],
    fontSize=7.5,
    textColor=LGRAY,
    fontName="Helvetica",
    leading=11,
    alignment=TA_CENTER,
)


def section_header(num: str, title: str) -> Table:
    """Build section header bar."""
    data = [[Paragraph(f"<b>{num}</b>", H2), Paragraph(title.upper(), H2)]]
    table = Table(data, colWidths=[0.35 * inch, 6.4 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("ROUNDEDCORNERS", [4]),
            ]
        )
    )
    return table


def fill_row(label: str, hint: str = "", multiline: bool = False) -> Table:
    """Build standard fill-in row."""
    lines = 3 if multiline else 1
    row_h = lines * 0.22 * inch + 0.15 * inch
    data = [[Paragraph(label, FILL_LABEL), Paragraph(f"<i>{hint}</i>" if hint else "", ITALIC)]]
    table = Table(data, colWidths=[2.2 * inch, 4.55 * inch], rowHeights=[row_h])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), LIGHT),
                ("BACKGROUND", (1, 0), (1, 0), WHITE),
                ("BOX", (1, 0), (1, 0), 0.5, MID),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LINEBELOW", (1, 0), (1, 0), 0.5, MID),
            ]
        )
    )
    return table


def trait_pair_header() -> Table:
    data = [[Paragraph("VOICE IS …", LABEL), Paragraph("VOICE IS NOT …", LABEL)]]
    table = Table(data, colWidths=[3.375 * inch, 3.375 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def trait_pair_row(is_val: str = "", not_val: str = "") -> Table:
    blank = "___________________________"
    data = [[Paragraph(is_val or blank, FILL_LINE), Paragraph(not_val or blank, FILL_LINE)]]
    table = Table(data, colWidths=[3.375 * inch, 3.375 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (0, 0), 0.5, MID),
                ("BOX", (1, 0), (1, 0), 0.5, MID),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, MID),
            ]
        )
    )
    return table


def channel_block(name: str):
    fields = ["Purpose", "Tone", "Typical structure", "CTA style", "Avoid"]
    rows = [[Paragraph(field, FILL_LABEL), Paragraph("", ITALIC)] for field in fields]
    channel_header = Table(
        [
            [
                Paragraph(
                    name,
                    ParagraphStyle(
                        "CH",
                        parent=H2,
                        fontSize=9,
                        textColor=NAVY,
                        fontName="Helvetica-Bold",
                        leading=13,
                        spaceBefore=0,
                        spaceAfter=0,
                    ),
                )
            ]
        ],
        colWidths=[6.75 * inch],
    )
    channel_header.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    inner = Table(rows, colWidths=[1.8 * inch, 4.95 * inch])
    inner.setStyle(
        TableStyle(
            [
                ("BOX", (1, 0), (1, -1), 0.5, MID),
                ("LINEBELOW", (1, 0), (1, -1), 0.5, MID),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("BACKGROUND", (0, 0), (0, -1), LIGHT),
            ]
        )
    )
    return [channel_header, Spacer(1, 2), inner, Spacer(1, 6)]


def generate_pdf(output_file: Path = OUTPUT_FILE) -> None:
    """Generate the Brand Voice Brief PDF file."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    story = []

    cover_data = [
        [Paragraph("BRAND VOICE BRIEF", H1)],
        [
            Paragraph(
                "For AI-Assisted Social Writing",
                ParagraphStyle(
                    "sub",
                    parent=styles["Normal"],
                    fontSize=13,
                    textColor=TEAL,
                    fontName="Helvetica",
                    leading=18,
                    alignment=TA_CENTER,
                ),
            )
        ],
    ]
    cover = Table(cover_data, colWidths=[6.75 * inch])
    cover.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("TOPPADDING", (0, 0), (-1, -1), 18),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("ROUNDEDCORNERS", [6]),
            ]
        )
    )
    story.append(cover)
    story.append(Spacer(1, 10))

    meta_data = [
        [
            Paragraph("Last updated:", LABEL),
            Paragraph("", FILL_LINE),
            Paragraph("Owner:", LABEL),
            Paragraph("", FILL_LINE),
            Paragraph("Approved by:", LABEL),
            Paragraph("", FILL_LINE),
        ]
    ]
    meta = Table(
        meta_data,
        colWidths=[0.9 * inch, 1.2 * inch, 0.6 * inch, 1.2 * inch, 0.85 * inch, 1.2 * inch],
    )
    meta.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (1, 0), (1, 0), 0.5, MID),
                ("LINEBELOW", (3, 0), (3, 0), 0.5, MID),
                ("LINEBELOW", (5, 0), (5, 0), 0.5, MID),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(meta)
    story.append(Spacer(1, 8))

    story.append(section_header("1", "Brand Snapshot"))
    story.append(Spacer(1, 4))
    for label, hint in [
        ("Brand name", "Official name as it appears in all copy"),
        ("Website / social handles", ""),
        ("What we do", "One clear sentence"),
        ("What we want to be known for", ""),
        ("Brand promise (1 sentence)", ""),
        ("Primary offers / services", ""),
    ]:
        story.append(fill_row(label, hint, multiline=(label in ["What we do", "Primary offers / services"])))
    story.append(Spacer(1, 10))

    story.append(section_header("2", "Audience"))
    story.append(Spacer(1, 4))
    for label, hint in [
        ("Primary audience", "Who we are talking to"),
        ("What they care about", "Values, goals, day-to-day priorities"),
        ("Problem we solve", "Pain point or gap we address"),
        ("What they are skeptical of", "Common objections"),
        ("Tone they respond well to", ""),
        ("Tone that turns them off", ""),
    ]:
        story.append(fill_row(label, hint, multiline=True))
    story.append(Spacer(1, 10))

    story.append(section_header("3", "Core Voice"))
    story.append(Spacer(1, 4))
    story.append(Paragraph("VOICE TRAITS (3–4)", LABEL))
    for _ in range(4):
        story.append(fill_row("Trait", "e.g. Clear / Confident / Grounded / Warm"))
    story.append(Spacer(1, 6))
    story.append(Paragraph("VOICE CONTRAST PAIRS", LABEL))
    story.append(trait_pair_header())
    for pair in [
        ("e.g. Clear", "not Clinical"),
        ("e.g. Playful", "not Flippant"),
        ("e.g. Confident", "not Arrogant"),
        ("", ""),
    ]:
        story.append(trait_pair_row(*pair))
    story.append(Spacer(1, 6))
    story.append(
        fill_row(
            "One-line voice summary",
            'e.g. "Smart, grounded, and clear—never stiff, salesy, or overhyped."',
            True,
        )
    )
    story.append(Spacer(1, 10))

    story.append(section_header("4", "Tone by Context"))
    story.append(Spacer(1, 4))
    for context in [
        "Default (most of the time)",
        "When educating",
        "When selling",
        "When celebrating",
        "When responding to criticism",
        "When addressing sensitive topics",
    ]:
        story.append(fill_row(context, "Describe the tone shift here", True))
    story.append(Spacer(1, 10))

    story.append(section_header("5", "Writing Style Rules"))
    story.append(Spacer(1, 4))
    for label, hint in [
        ("Sentence style", "Short / medium / long? Punchy or layered?"),
        ("Reading level", "Simple, conversational, expert"),
        ("Formatting habits", "Short paras, line breaks, bullets, etc."),
        ("Punctuation", "Oxford comma? Em dash? Exclamation points?"),
        ("Capitalization", "Title case, sentence case, branded caps"),
        ("Contractions", "Yes / No"),
        ("Emoji use", "Never / light / moderate / heavy"),
        ("Hashtag use", "None / minimal / campaign-only / always"),
        ("CTA style", "Direct, soft, playful, urgent, advisory"),
    ]:
        story.append(fill_row(label, hint))
    story.append(Spacer(1, 10))

    story.append(section_header("6", "Word Bank"))
    story.append(Spacer(1, 4))
    wb_headers = [Paragraph("ALWAYS SAY", LABEL), Paragraph("NEVER SAY", LABEL)]
    wb_rows = [
        [Paragraph("1. ___________________", FILL_LINE), Paragraph("1. ___________________", FILL_LINE)],
        [Paragraph("2. ___________________", FILL_LINE), Paragraph("2. ___________________", FILL_LINE)],
        [Paragraph("3. ___________________", FILL_LINE), Paragraph("3. ___________________", FILL_LINE)],
        [Paragraph("4. ___________________", FILL_LINE), Paragraph("4. ___________________", FILL_LINE)],
        [Paragraph("5. ___________________", FILL_LINE), Paragraph("5. ___________________", FILL_LINE)],
    ]
    wb_table = Table([wb_headers] + wb_rows, colWidths=[3.375 * inch, 3.375 * inch])
    wb_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.5, MID),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, MID),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(wb_table)
    story.append(Spacer(1, 6))
    story.append(
        fill_row("Required brand terms", "Product names, trademarks, branded capitalization")
    )
    story.append(fill_row("Terms to simplify", "Industry jargon to rewrite for general audiences"))
    story.append(Spacer(1, 10))

    story.append(section_header("7", "Messaging Guardrails"))
    story.append(Spacer(1, 4))
    for label, hint in [
        ("Key messages to reinforce", "Themes that should appear consistently"),
        ("Claims we CAN make", "Approved statements, proven results"),
        ("Claims we CANNOT make", "Unverified, legal risk, out of scope"),
        ("Required disclaimers", "Regulatory, legal, or compliance requirements"),
        ("Topics requiring approval", "Sensitive areas that need sign-off before publishing"),
    ]:
        story.append(fill_row(label, hint, multiline=True))
    story.append(Spacer(1, 10))

    story.append(section_header("8", "Channel Rules"))
    story.append(Spacer(1, 4))
    for channel in ["LinkedIn", "Instagram", "TikTok", "X / Threads / Facebook"]:
        for item in channel_block(channel):
            story.append(item)
    story.append(Spacer(1, 10))

    story.append(section_header("9", "Examples to Match"))
    story.append(Spacer(1, 4))
    for i in range(1, 4):
        story.append(Paragraph(f"EXAMPLE {i}", LABEL))
        story.append(fill_row("Post (paste or link)", "", multiline=True))
        story.append(fill_row("Why it works", "", multiline=True))
        story.append(Spacer(1, 4))
    story.append(Spacer(1, 6))

    story.append(section_header("10", "Examples to Avoid"))
    story.append(Spacer(1, 4))
    for i in range(1, 3):
        story.append(Paragraph(f"EXAMPLE {i}", LABEL))
        story.append(fill_row("What feels off", "", multiline=True))
        story.append(fill_row("What to do instead", "", multiline=True))
        story.append(Spacer(1, 4))
    story.append(Spacer(1, 6))

    story.append(section_header("11", "AI Input Block — Ready-to-Use Prompt Header"))
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "Paste this block at the top of every AI writing prompt, then add your task below.",
            BODY,
        )
    )
    story.append(Spacer(1, 4))

    ai_block = """You are writing social copy for [Brand Name].

AUDIENCE:
[Paste Section 2 — who they are, what they care about, skepticism]

CORE VOICE:
[Paste traits from Section 3]

VOICE IS / IS NOT:
[Paste contrast pairs from Section 3]

STYLE RULES:
[Paste Section 5 — sentence style, emoji, CTA, formatting]

WORD BANK:
Always use: [paste approved language]
Never use: [paste banned language]

MESSAGING GUARDRAILS:
[Paste approved claims and off-limits topics]

CHANNEL: [Platform name]

TASK:
Write [number] social posts about [topic].

OUTPUT REQUIREMENTS:
- Length: [...]
- Goal: [...]
- CTA: [...]
- Include: [...]
- Avoid: [...]

BEFORE FINALIZING, CHECK:
1. Does this sound like our brand voice?
2. Did you use only approved language?
3. Are all claims supported?
4. Does this fit the platform?
5. Does this feel human, specific, and natural?"""

    story.append(Paragraph(ai_block.replace("\n", "<br/>"), CODE))
    story.append(Spacer(1, 10))

    story.append(section_header("12", "Human Review Checklist"))
    story.append(Spacer(1, 4))
    checks = [
        "Voice match — does this sound like us?",
        "Platform fit — right length, format, and tone for this channel?",
        "Factual accuracy — is every claim accurate and supported?",
        "Compliance — does this need legal or regulatory review?",
        "No banned words or phrases",
        "No unsupported or exaggerated claims",
        "CTA is correct and functional",
        "Formatting is clean and readable",
        "Sensitive-topic sign-off completed (if applicable)",
    ]
    check_rows = [[Paragraph("☐", BODY), Paragraph(c, BODY)] for c in checks]
    check_table = Table(check_rows, colWidths=[0.25 * inch, 6.5 * inch])
    check_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LINEBELOW", (0, 0), (-1, -1), 0.3, MID),
            ]
        )
    )
    story.append(check_table)
    story.append(Spacer(1, 10))

    story.append(section_header("13", "Version Notes"))
    story.append(Spacer(1, 4))
    v_headers = [Paragraph(h, LABEL) for h in ["Date", "What changed", "Why it changed", "Approved by"]]
    v_rows = [[Paragraph("", FILL_LINE)] * 4 for _ in range(4)]
    v_table = Table(
        [v_headers] + v_rows,
        colWidths=[0.9 * inch, 2.4 * inch, 2.4 * inch, 1.05 * inch],
    )
    v_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.5, MID),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, MID),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(v_table)
    story.append(Spacer(1, 14))

    story.append(HRFlowable(width="100%", thickness=0.5, color=MID))
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "Brand Voice Brief · AI-Assisted Social Writing · thebrandstudio.studio · Reusable &amp; Editable",
            FOOTER,
        )
    )

    doc.build(story)


def main() -> None:
    generate_pdf()
    if not OUTPUT_FILE.exists():
        raise FileNotFoundError(f"Expected output file was not created: {OUTPUT_FILE}")
    print(f"PDF created successfully at {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
