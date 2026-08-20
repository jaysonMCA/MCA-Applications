# MCA DD App

Internal BD-facing company due diligence app.

## Run

```powershell
cd D:\MCA\AIProject\DD_app
pip install -r requirements.txt
python -m uvicorn app.dd_web.server:app --reload --host 127.0.0.1 --port 8001
```

Open:

```text
http://127.0.0.1:8001
```

## Automation

Without an API key, the app runs in manual packet mode and produces a copy-ready research prompt plus exportable Markdown and evidence JSON shells.

To enable automated web research, create `.env` from `.env.example` and set:

```env
OPENAI_API_KEY=your_new_key_here
DD_APP_MODEL=gpt-5.6
DD_APP_REASONING=high
```

Restart the server after changing `.env`.

## PDF Export

The web app includes a `PDF` button for the current report. PDF exports are built as a meeting brief:

1. Executive summary and company snapshot
2. DD watchouts, call priorities, and sources
3. Product and traction detail, when the report includes a `Product Breakdown` section
4. Market and competitor map, when the report includes a `Market Landscape` section
5. Evidence gaps and call plan, when the report includes `Evidence Matrix` and `Meeting Prep` sections

You can also export a saved Markdown report from the command line:

```powershell
python -m app.dd_web.export_pdf outputs\company_dd\20260820_pavilion_markets_dd_one_pager.md outputs\company_dd\20260820_pavilion_markets_dd_one_pager.pdf
```

## Structure

```text
DD_app/
  assets/brand/                MCA logo assets used in PDF exports
  app/dd_web/                  Web app backend and static frontend
  .claude/skills/company-dd-one-pager/
    SKILL.md                   Claude skill entrypoint
    references/                Research method and output template
    scripts/                   One-pager validator
    tests/                     Validator tests
  outputs/company_dd/          Sample/generated reports and evidence
```
