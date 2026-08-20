# MCA Strategic Review Agent File Map

This file defines the role of the source materials used to build and test the MCA Strategic Review Agent.

Files must not be treated interchangeably.

## 1. Project Context

File:
PROJECT_CONTEXT.md

Role:
Primary project source of truth.

Use:
Read before making architectural or methodology decisions.

Contains:
MCA context
Project objectives
Hash's requirements
Intended workflow
Scope restrictions
Desired outputs

## 2. Hash VC Evaluation Playbook

File:
references/methodology/hash_vc_evaluation_playbook.md

Role:
Primary practitioner methodology source.

Use:
Use when developing and refining the MCA review methodology.

Contains:
VC and angel evaluation principles
Founder and team analysis
Market analysis
Why now
Problem
Moat
Traction
Economics
Distribution
Competition
Category specific traps
Scoring
Red and yellow flags
Diligence questions
Objectivity rules

Important:
This is methodology material, not a company specific benchmark output.

## 3. Early Stage VC Research

File:
references/research/early_stage_vc_research.docx
references/research/early_stage_vc_research.md

Role:
External evidence base for the methodology.

Use:
Validate, challenge, and expand the practitioner framework.

Contains:
Research on startup success signals
VC selection factors
Pre seed versus seed differences
Fundability versus company quality
Traction
Retention
Distribution
Economics
Capital efficiency
Stage adjusted scoring
Risk factors

## 4. Hash Final Prized Review

File:
examples/prized/benchmark/hash_final_review.pdf

Role:
Benchmark output and answer key.

Use:
Use only after the Prized blind run is complete to evaluate the agent's generated Prized review.

Important:
Do not expose files inside `examples/prized/benchmark/` to the review agent during a blind evaluation.

## 5. Prized Original Materials

Files:
examples/prized/source/
examples/prized/reviewer/

Role:
Test Case 1 inputs.

Use:
Use as inputs for the Prized blind test along with MCA methodology and external research.

## 6. PocketBall / PocketPull Deck

File:
cases/pocketpull/source/deck.pdf
cases/pocketpull/source/deck_extracted.txt

Role:
Test Case 2 input.

Use:
Use to test whether the methodology generalizes to a different company without an answer key.

Important:
Use `pocketpull` as the repository slug unless the company later confirms a different official name.
