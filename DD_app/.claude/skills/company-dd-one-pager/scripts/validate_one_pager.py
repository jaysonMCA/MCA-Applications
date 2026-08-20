#!/usr/bin/env python3
"""Validate MCA company DD one pager Markdown structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXIT_FAILED = 1
EXIT_INVALID = 2

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
MONTH_RE = "|".join(MONTHS)
DATE_RE = re.compile(
    rf"\b(?:(?:{MONTH_RE})\s+\d{{1,2}},\s+\d{{4}}|\d{{1,2}}\s+(?:{MONTH_RE})\s+\d{{4}}|\d{{4}}-\d{{2}}-\d{{2}})\b"
)
URL_RE = re.compile(r"https?://[^\s)\]>]+")
NEWS_NO_ITEM_RE = re.compile(
    rf"No material company specific news was located from {DATE_RE.pattern} through {DATE_RE.pattern} across the reviewed official and independent sources\.",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(
    r"(\[[^\]\n]*(?:\s|,|Company|Website|Question|Evidence|Development|Fact|Compact|Buyer|Customer|URL|TBD|TODO)[^\]\n]*\]|\bTBD\b|\bTODO\b|\bN/A\b|https?://(?:example\.com|example\.org|example\.net|dummy|placeholder)[^\s)]*)",
    re.IGNORECASE,
)

REQUIRED_H2 = (
    "## Bottom Line",
    "## Company Snapshot",
    "## Last 30 Days",
    "## DD Watchouts",
    "## Call Priorities",
    "## Sources",
)
SEVERITIES = ("High", "Medium", "Low")
STATUSES = ("Confirmed", "Reported", "Alleged", "Unverified", "Not found")


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    next_heading = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(text)
    return text[match.end() : end].strip()


def numbered_items(section: str) -> list[str]:
    matches = list(re.finditer(r"^\s*\d+\.\s+", section, re.MULTILINE))
    items: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        items.append(section[start:end].strip())
    return items


def source_urls(section: str) -> list[str]:
    return [url.rstrip(".,") for url in URL_RE.findall(section)]


def word_count_before_sources(text: str) -> int:
    before_sources = text.split("## Sources", 1)[0]
    return len(re.findall(r"\b[\w']+\b", before_sources))


def has_public_info_limitation(text: str) -> bool:
    return bool(
        re.search(
            r"(public information limitation|thin public footprint|limited public information|public sources were limited)",
            text,
            re.IGNORECASE,
        )
    )


def validate(text: str) -> list[str]:
    failures: list[str] = []

    title_count = len(re.findall(r"^#\s+.+\s+\|\s+Executive DD\s*$", text, re.MULTILINE))
    if title_count != 1:
        failures.append("Expected exactly 1 H1 title matching '# [Company Name] | Executive DD'.")

    for heading in REQUIRED_H2:
        count = len(re.findall(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE))
        if count != 1:
            failures.append(f"Expected heading '{heading}' exactly once; found {count}.")

    if len(re.findall(r"^\*\*As of:\*\*\s*.+$", text, re.MULTILINE)) != 1:
        failures.append("Expected exactly 1 '**As of:**' metadata line.")

    window_lines = re.findall(r"^\*\*News window:\*\*\s*(.+)$", text, re.MULTILINE)
    if len(window_lines) != 1:
        failures.append("Expected exactly 1 '**News window:**' metadata line.")
    elif len(DATE_RE.findall(window_lines[0])) != 2:
        failures.append("News window must contain exactly 2 absolute dates.")

    count = word_count_before_sources(text)
    if count < 450:
        failures.append(f"Report is below 450 words before Sources; found {count}.")
    elif count > 650:
        failures.append(f"Report is above 650 words before Sources; found {count}.")

    last_30 = extract_section(text, "## Last 30 Days")
    news_items = numbered_items(last_30)
    no_news = bool(NEWS_NO_ITEM_RE.search(last_30))
    if news_items:
        if not 1 <= len(news_items) <= 5:
            failures.append(f"Last 30 Days must contain 1 to 5 numbered items; found {len(news_items)}.")
        for item in news_items:
            label = item.splitlines()[0][:80]
            if not DATE_RE.search(item):
                failures.append(f"News item lacks an absolute date: {label}")
            if not URL_RE.search(item):
                failures.append(f"News item lacks an HTTP or HTTPS URL: {label}")
    elif not no_news:
        failures.append("Last 30 Days must contain 1 to 5 numbered items or the exact no-news statement.")

    watchouts = extract_section(text, "## DD Watchouts")
    watchout_items = numbered_items(watchouts)
    if not 1 <= len(watchout_items) <= 5:
        failures.append(f"DD Watchouts must contain 1 to 5 numbered items; found {len(watchout_items)}.")
    for item in watchout_items:
        label = item.splitlines()[0][:80]
        if not any(re.search(rf"\b{severity}\b", item) for severity in SEVERITIES):
            failures.append(f"Watchout lacks severity label High, Medium, or Low: {label}")
        if not any(re.search(rf"\b{status}\b", item, re.IGNORECASE) for status in STATUSES):
            failures.append(f"Watchout lacks evidence status: {label}")
        if not URL_RE.search(item):
            failures.append(f"Watchout lacks an HTTP or HTTPS URL: {label}")

    call_priorities = extract_section(text, "## Call Priorities")
    priority_count = len(numbered_items(call_priorities))
    if priority_count != 3:
        failures.append(f"Call Priorities must contain exactly 3 numbered items; found {priority_count}.")

    urls = source_urls(text)
    if len(set(urls)) < 5 and not has_public_info_limitation(text):
        failures.append("At least 5 unique source URLs are required unless a public information limitation is explicit.")

    if PLACEHOLDER_RE.search(text):
        failures.append("Placeholder text remains, such as bracketed template text, TBD, TODO, N/A, or dummy URLs.")

    sources = extract_section(text, "## Sources")
    source_url_list = source_urls(sources)
    duplicates = sorted({url for url in source_url_list if source_url_list.count(url) > 1})
    if duplicates:
        failures.append("Duplicate source URLs appear in Sources: " + ", ".join(duplicates))

    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python validate_one_pager.py path/to/report.md")
        return EXIT_INVALID

    path = Path(argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Could not read file: {exc}")
        return EXIT_INVALID
    except UnicodeDecodeError:
        print("File is not valid UTF-8 Markdown.")
        return EXIT_INVALID

    failures = validate(text)
    if failures:
        for index, failure in enumerate(failures, 1):
            print(f"{index}. {failure}")
        return EXIT_FAILED

    print(
        f"Validation passed: {path} has required sections, metadata, length, dated developments, watchouts, priorities, and source hygiene."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
