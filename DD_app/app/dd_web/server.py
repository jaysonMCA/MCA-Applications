from __future__ import annotations

import json
import os
import re
from io import BytesIO
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.dd_web.export_pdf import build_pdf_bytes


ROOT = Path(__file__).resolve().parents[2]
STATIC_DIR = Path(__file__).resolve().parent / "static"
SKILL_DIR = ROOT / ".claude" / "skills" / "company-dd-one-pager"
OUTPUT_DIR = ROOT / "outputs" / "company_dd"

load_dotenv(ROOT / ".env")

app = FastAPI(title="MCA Company DD")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class DDRequest(BaseModel):
    company: str = Field(..., min_length=1)
    website: str | None = None
    profile: str | None = None
    region: str | None = None
    sector: str | None = None
    call_context: str | None = None
    supplied_notes: str | None = None
    timezone: str = "Asia/Manila"


class PDFRequest(BaseModel):
    company: str = "company"
    report_markdown: str = Field(..., min_length=1)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "company"


def read_skill_text() -> str:
    parts = []
    for relative in ("SKILL.md", "references/research_method.md", "references/output_template.md"):
        path = SKILL_DIR / relative
        if path.exists():
            parts.append(f"\n\n--- {relative} ---\n{path.read_text(encoding='utf-8')}")
    return "\n".join(parts)


def build_prompt(payload: DDRequest) -> dict[str, Any]:
    researched_at = date.today()
    start = researched_at - timedelta(days=29)
    company = payload.company.strip()
    optional_context = {
        "official_website": payload.website,
        "official_profile": payload.profile,
        "region": payload.region,
        "sector": payload.sector,
        "call_context": payload.call_context,
        "supplied_notes": payload.supplied_notes,
    }
    skill_text = read_skill_text()
    prompt = f"""
You are producing an internal MCA BD company due diligence one pager.

Target company: {company}
Research date: {researched_at.isoformat()}
News window: {start.isoformat()} through {researched_at.isoformat()}, inclusive
Timezone: {payload.timezone}
Optional context: {json.dumps(optional_context, ensure_ascii=False, indent=2)}

Use current web research. Open and evaluate underlying sources. Do not rely on search snippets for material claims. If the company identity is ambiguous, do not produce a mixed report; return JSON with needs_clarification=true and one focused clarification question.

Follow this MCA skill and methodology:
{skill_text}

Return JSON only, with this shape:
{{
  "needs_clarification": false,
  "clarification_question": "",
  "company": "{company}",
  "identity": {{
    "brand_name": "",
    "official_domain": "",
    "legal_entity": "",
    "base": "",
    "leadership": "",
    "product": ""
  }},
  "news_window": {{
    "start": "{start.isoformat()}",
    "end": "{researched_at.isoformat()}",
    "timezone": "{payload.timezone}"
  }},
  "central_tension": "",
  "report_markdown": "",
  "evidence_register": {{
    "company": "",
    "official_domain": "",
    "researched_at": "{researched_at.isoformat()}",
    "news_window_start": "{start.isoformat()}",
    "news_window_end": "{researched_at.isoformat()}",
    "claims": []
  }},
  "source_urls": []
}}
"""
    return {
        "prompt": prompt.strip(),
        "researched_at": researched_at.isoformat(),
        "news_window_start": start.isoformat(),
        "news_window_end": researched_at.isoformat(),
        "company_slug": slugify(company),
    }


def extract_output_text(response: dict[str, Any]) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"]
    chunks: list[str] = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if isinstance(content, dict) and isinstance(content.get("text"), str):
                chunks.append(content["text"])
    return "\n".join(chunks)


def parse_json_output(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.DOTALL | re.IGNORECASE)
    if fence:
        cleaned = fence.group(1).strip()
    return json.loads(cleaned)


def fallback_packet(payload: DDRequest, message: str | None = None) -> dict[str, Any]:
    packet = build_prompt(payload)
    company = payload.company.strip()
    report = f"""# {company} | Executive DD

**As of:** {packet["researched_at"]}, {payload.timezone}
**News window:** {packet["news_window_start"]} to {packet["news_window_end"]}
**Official:** {payload.website or "Unknown"} | {payload.profile or "Unknown"}

## Bottom Line

Run the generated research prompt in Claude or ChatGPT with web access, then paste the completed one pager here for export.

## Company Snapshot

| Field | Read |
|---|---|
| What it does | Pending current web research. |
| Customer | Pending current web research. |
| Business model | Pending current web research. |
| Stage and traction | Pending current web research. |
| Leadership and base | Pending current web research. |
| Venture lens | Pending current web research using PRIME. |

## Last 30 Days

No validated research has been run yet.

## DD Watchouts

1. **Medium | Unverified | Automation credentials missing.** The app could not run live research without a server-side API key.

## Call Priorities

1. What must be true commercially for this company to matter to MCA?
2. Which public claims need private confirmation on the call?
3. What risk, structure, or market issue could change MCA's next step?

## Sources

Add sources after live research.
"""
    return {
        "mode": "manual_packet",
        "message": message
        or "OPENAI_API_KEY is not configured on the server. Use the research prompt below in Claude/ChatGPT with web access, or add a server-side key and rerun.",
        "prompt": packet["prompt"],
        "report_markdown": report,
        "evidence_register": {
            "company": company,
            "official_domain": payload.website or "",
            "researched_at": packet["researched_at"],
            "news_window_start": packet["news_window_start"],
            "news_window_end": packet["news_window_end"],
            "claims": [],
        },
        "news_window": {
            "start": packet["news_window_start"],
            "end": packet["news_window_end"],
            "timezone": payload.timezone,
        },
        "central_tension": "Automation credentials are missing, so the app generated a research packet instead of a verified one pager.",
    }


async def call_openai(prompt: str) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("missing_api_key")

    model = os.getenv("DD_APP_MODEL", "gpt-5.6")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body: dict[str, Any] = {
        "model": model,
        "tools": [{"type": "web_search"}],
        "input": prompt,
    }
    if os.getenv("DD_APP_REASONING", "high"):
        body["reasoning"] = {"effort": os.getenv("DD_APP_REASONING", "high")}

    async with httpx.AsyncClient(timeout=240) as client:
        response = await client.post("https://api.openai.com/v1/responses", headers=headers, json=body)
        if response.status_code == 400 and "reasoning" in body:
            body.pop("reasoning", None)
            response = await client.post("https://api.openai.com/v1/responses", headers=headers, json=body)
        response.raise_for_status()
        raw = response.json()
    text = extract_output_text(raw)
    try:
        parsed = parse_json_output(text)
        parsed["mode"] = "automated"
        return parsed
    except (json.JSONDecodeError, TypeError) as exc:
        return {
            "mode": "raw_model_output",
            "message": f"The model returned non-JSON output: {exc}",
            "report_markdown": text,
            "evidence_register": {},
            "source_urls": [],
        }


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
async def health() -> dict[str, Any]:
    return {
        "ok": True,
        "automation_ready": bool(os.getenv("OPENAI_API_KEY")),
        "model": os.getenv("DD_APP_MODEL", "gpt-5.6"),
    }


@app.post("/api/generate")
async def generate(payload: DDRequest) -> dict[str, Any]:
    if not payload.company.strip():
        raise HTTPException(status_code=400, detail="Company name is required.")
    if not os.getenv("OPENAI_API_KEY"):
        return fallback_packet(payload)
    packet = build_prompt(payload)
    try:
        result = await call_openai(packet["prompt"])
    except httpx.HTTPStatusError as exc:
        detail = exc.response.text[:800]
        if exc.response.status_code in {401, 403, 429} or "insufficient_quota" in detail or "credit_balance_exhausted" in detail:
            return fallback_packet(
                payload,
                "Automated research is configured, but the API request was rejected by OpenAI billing/auth/rate limits. The app generated a manual research packet instead.",
            )
        raise HTTPException(status_code=502, detail=f"OpenAI request failed: {detail}") from exc
    except RuntimeError:
        return fallback_packet(payload)
    result.setdefault("prompt", packet["prompt"])
    result.setdefault(
        "news_window",
        {
            "start": packet["news_window_start"],
            "end": packet["news_window_end"],
            "timezone": payload.timezone,
        },
    )
    return result


@app.post("/api/export-pdf")
async def export_pdf(payload: PDFRequest) -> StreamingResponse:
    try:
        pdf = build_pdf_bytes(payload.report_markdown)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Could not export PDF: {exc}") from exc
    filename = f"{slugify(payload.company)}_dd_one_pager.pdf"
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return StreamingResponse(BytesIO(pdf), media_type="application/pdf", headers=headers)
