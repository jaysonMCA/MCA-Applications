"""Local project mechanics for MCA strategic review cases.

The CLI intentionally avoids embedding review methodology. Keep analysis rules in
SKILL.md, memory files, and templates.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CASE_DIRS = [
    "source/supporting_documents",
    "reviewer",
    "research",
    "analysis",
    "output",
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "unnamed_company"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def new_case(args: argparse.Namespace) -> None:
    company_name = args.company_name.strip()
    case_slug = args.slug or slugify(company_name)
    case_root = PROJECT_ROOT / "cases" / case_slug

    for relative_dir in CASE_DIRS:
        (case_root / relative_dir).mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    manifest = {
        "company_name": company_name,
        "case_slug": case_slug,
        "created_date": today,
        "mca_reviewer": args.reviewer,
        "stage": None,
        "review_type": "complete_pending_deck",
        "inputs": {
            "pitch_deck": None,
            "transcript": None,
            "company_links": "source/company_links.md",
            "supporting_documents": "source/supporting_documents/",
            "reviewer_notes": "reviewer/reviewer_notes.md",
        },
        "workflow_state": {
            "materials_read": False,
            "reviewer_interview_complete": False,
            "research_plan_approved": False,
            "external_research_complete": False,
            "human_checkpoint_complete": False,
            "final_deliverable_generated": False,
        },
        "evidence_categories": [
            "company_claim",
            "reviewer_judgment",
            "external_research",
            "agent_inference",
        ],
    }

    write_if_missing(case_root / "case_manifest.json", json.dumps(manifest, indent=2) + "\n")
    write_if_missing(
        case_root / "README.md",
        f"# {company_name}\n\nCase folder for an MCA strategic company review.\n\nStart by adding the pitch deck to `source/` and reviewer notes to `reviewer/reviewer_notes.md`.\n",
    )
    write_if_missing(
        case_root / "source" / "company_links.md",
        "# Company Links\n\n- Website:\n- Socials:\n- GitHub:\n- Product:\n- Whitepaper / docs:\n",
    )
    write_if_missing(
        case_root / "reviewer" / "reviewer_notes.md",
        "# Reviewer Notes\n\nCapture raw MCA reviewer opinion here. Polished writing is not required.\n",
    )
    write_if_missing(
        case_root / "research" / "research_plan.md",
        "# Research Plan\n\nUse `templates/research_plan.md` after materials and reviewer notes are reviewed.\n",
    )
    write_if_missing(
        case_root / "analysis" / "evidence_log.md",
        "# Evidence Log\n\nUse `templates/evidence_log.md` to classify major claims and conclusions.\n",
    )
    write_if_missing(
        case_root / "output" / "final_deliverable.md",
        "# Final Deliverable\n\nDo not draft until the mandatory human checkpoint is complete.\n",
    )

    print(f"Created case scaffold: {case_root}")


def show_workflow(_: argparse.Namespace) -> None:
    files = [
        "PROJECT_CONTEXT.md",
        "SKILL.md",
        "memory/mca_context.md",
        "memory/vc_review_methodology.md",
        "memory/vc_success_signals.md",
        "memory/research_rules.md",
        "memory/mca_output_standard.md",
        "memory/diligence_question_bank.md",
        "templates/reviewer_interview.md",
        "templates/research_plan.md",
        "templates/evidence_log.md",
        "templates/internal_analysis.md",
        "templates/human_checkpoint.md",
        "templates/final_deliverable.md",
    ]
    print("MCA Strategic Review Agent workflow files:")
    for item in files:
        print(f"- {item}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="MCA strategic review local utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_case_parser = subparsers.add_parser("new-case", help="Create a new company case folder")
    new_case_parser.add_argument("company_name", help="Company name")
    new_case_parser.add_argument("--slug", help="Optional case folder slug")
    new_case_parser.add_argument("--reviewer", default=None, help="MCA reviewer name")
    new_case_parser.set_defaults(func=new_case)

    workflow_parser = subparsers.add_parser("show-workflow", help="List the editable workflow files")
    workflow_parser.set_defaults(func=show_workflow)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
