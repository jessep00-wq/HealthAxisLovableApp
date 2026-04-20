# HealthAxisLovableApp

Internal Lovable app for workflows, memory, and admin systems.

## Brand Voice Brief assets

This repository includes two implementation assets for a reusable Brand Voice Brief:

1. `brand_voice_brief_template.py` — ReportLab generator for a PDF template.
2. `artifacts/brand_voice_brief_template.md` — Markdown artifact template with explicit governance and human-review checkpoints.

## Generate the PDF (when ReportLab is available)

```bash
python3 brand_voice_brief_template.py
```

Generated artifact:

- `output/Brand_Voice_Brief_Template.pdf`

## Use the markdown artifact directly

If Python dependencies are unavailable in your environment, use:

- `artifacts/brand_voice_brief_template.md`

This path preserves deterministic structure and required review checkpoints for regulated workflows.
