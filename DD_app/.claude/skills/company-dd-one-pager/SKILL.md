---
name: company-dd-one-pager
description: Research a company for MCA internal BD call preparation and produce a concise, evidence backed executive due diligence one pager covering what the company does, material company news from the last 30 calendar days, major risk signals, a PRIME venture lens, and priority call questions. Use when asked to research, diligence, prepare for a call with, or quickly assess a company.
---

# MCA Company DD One Pager

Research the company supplied in `$ARGUMENTS` and produce an internal MCA executive due diligence one pager.

## Required Resources

Read these files before researching:

1. `${CLAUDE_SKILL_DIR}/references/research_method.md` for the evidence, search, risk, PRIME, and quality rules.
2. `${CLAUDE_SKILL_DIR}/references/output_template.md` for the mandatory final structure and length.

## Input Handling

Treat the input as potentially incomplete.

1. Require a company name.
2. Prefer an official website or official profile.
3. Resolve the company identity before wider research.
4. If multiple plausible companies remain, ask 1 focused clarification question. Do not guess.
5. Use any supplied deck, transcript, notes, data room, or call context as private source material and label private claims separately from public confirmation.

## Workflow

1. Establish the official domain, legal or brand identity, operating geography, founders, product, buyer, and business model.
2. Compute the exact 30 calendar day news window using the runtime date and show the start date, end date, and timezone.
3. Research the company baseline using authoritative primary sources and credible independent sources.
4. Search official and independent channels for material company specific developments during the exact news window.
5. Run the adverse information sweep across legal, regulatory, financial, structural, operational, product, technology, security, reputation, and sector specific risks.
6. Apply the Osler lenses: PRIME, internal coherence, differentiation, why this company and why now, structural cleanliness, founder quality, risk reduction, AI efficiency where relevant, and mutual fit where relevant.
7. Build the evidence register before drafting. Separate confirmed, reported, alleged, unverified, and not found items.
8. Draft only the most material findings using the required template.
9. Save the evidence register to `outputs/company_dd/YYYYMMDD_company_slug_evidence.json`.
10. Save the final report to `outputs/company_dd/YYYYMMDD_company_slug_dd_one_pager.md`.
11. Run `python "${CLAUDE_SKILL_DIR}/scripts/validate_one_pager.py" "<report path>"`.
12. Fix every validation failure before returning the result.

## Evidence Rules

1. Open and review source pages. Do not rely on search snippets for material claims.
2. Prefer official records for identity, legal, funding, security, and regulatory facts.
3. Use credible independent reporting to test official claims.
4. Deduplicate syndicated releases and repeated coverage.
5. Distinguish publication date from event date.
6. Require 1 authoritative primary source or 2 credible independent sources for a high impact negative claim.
7. Treat social and community content as a signal unless stronger evidence confirms it.
8. Never present an allegation as fact.
9. Never infer that missing public information proves wrongdoing.
10. When evidence conflicts, state the conflict and keep the point open if it cannot be resolved.
11. If no material recent news or adverse item is found, say exactly what was searched and avoid claiming the company is risk free.
12. If current web research is unavailable, stop and state that the one pager cannot be completed reliably. Do not fabricate current findings.

## Output Rules

1. Follow `output_template.md` exactly.
2. Keep the report between 450 and 650 words, excluding Sources.
3. Use no more than 5 recent developments and no more than 5 watchouts.
4. Include exactly 3 priority call questions.
5. Give every recent development an absolute date and source URL.
6. Give every watchout a severity, evidence status, and source URL.
7. Keep the tone direct, concise, and neutral on facts while decisive on what matters.
8. Do not provide a final invest, reject, or partner recommendation unless the user explicitly asks for one and the available evidence supports it.
9. Do not include generic disclaimers. State specific evidence limits where they affect the read.

Return the saved report path, the company identity used, the exact news window, and a 1 sentence summary of the central diligence tension.
