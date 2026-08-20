# MCA Strategic Review Agent

Local v0.1 scaffold for MCA's AI-assisted strategic company review workflow.

This project is methodology-first. The review intelligence lives in `SKILL.md`, `memory/`, and `templates/`. The Python CLI should stay thin and handle local mechanics such as creating case folders, printing workflow guidance, and preparing empty files.

## Current Scope

- Create repeatable case folders.
- Preserve an evidence trail for major conclusions.
- Keep company-provided claims separate from verified facts.
- Generate a research plan before research begins.
- Require a human checkpoint before the final MCA deliverable.
- Produce Markdown and JSON artifacts only.

## Quick Start

```powershell
python -m mca_review_agent.cli show-workflow
python -m mca_review_agent.cli new-case "Example Company" --reviewer "Reviewer Name"
```

## Project Map

- `PROJECT_CONTEXT.md`: Source of truth for the project.
- `SKILL.md`: Agent operating instructions for the MCA review workflow.
- `memory/`: Permanent methodology and MCA review standards.
- `templates/`: Editable output and workflow templates.
- `cases/`: Company-specific review folders and evidence.
- `cases/prized/`: First blind-test case scaffold.
- `examples/prized/benchmark_after_blind_run/`: Place Hash's completed Prized deliverable here only after the blind run.
- `references/`: Supporting research and category reference material.
- `outputs/`: Cross-case exports or compiled outputs.
- `mca_review_agent/`: Thin local CLI and project utilities.

## Version 0.1 Boundary

Do not build a large application, CRM, proposal generator, dashboard, authentication system, or PDF export layer yet. The first version should prove the review methodology before the interface is expanded.
