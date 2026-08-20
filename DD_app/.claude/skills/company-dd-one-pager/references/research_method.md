# Research Method

Use this method for every MCA company DD one pager. The output is a high quality first screen, not a legal, technical, financial, tokenomics, or investment audit.

## Operating Rules

1. Use the runtime date.
2. Define the news window as the previous 30 calendar days, inclusive of the research date.
3. Show the exact research date, start date, end date, and timezone in every report.
4. Distinguish publication date from event date.
5. Prioritize event date when explaining recency.
6. Deduplicate press release syndication, copied articles, reposts, and repeated coverage.
7. Separate official company claims from independent confirmation.
8. Use primary sources for identity, product, leadership, legal, regulatory, funding, security, and operational claims whenever available.
9. Use credible independent sources to test official claims and identify controversy.
10. Open and review underlying pages. Never use search result snippets as the sole evidence for a material claim.
11. Never treat anonymous posts, engagement bait, or unsupported social claims as confirmed facts.
12. Never hide an absence of evidence. Mark it as unknown or not independently verified.
13. Do not pad the recent developments section with old or irrelevant news.
14. If no material company specific news is found during the window, state that directly and include the date range searched.
15. Keep the final report between 450 and 650 words, excluding Sources.
16. Surface only the 3 to 5 most material watchouts.
17. Include exactly 3 priority questions for the call.
18. Give every material risk an evidence status and at least 1 source.
19. Give every recent development a date and source.
20. Do not use the word FUD as a factual classification. Use risk signal, allegation, disputed claim, community concern, or unverified claim.

## Identity Resolution

Resolve the company identity before conducting full diligence. Build a short identity card with:

1. Brand name.
2. Official domain.
3. Legal entity, if public.
4. Headquarters or operating base.
5. Founders and current senior leadership.
6. Core product or service.
7. Primary market and customer.
8. Relevant token, protocol, application, or parent company.

Cross-check the identity against at least 2 independent identifiers. Useful identifiers include official domain, official social account, founder profile, regulatory filing, app listing, GitHub organization, token contract, or trusted company database. If 2 or more plausible companies remain, ask 1 focused clarification question and show the likely candidates. Do not spend the full research run on an unresolved entity.

## Baseline Company Analysis

Translate the company into plain English. Do not repeat marketing copy. Answer:

1. What problem does the company claim to solve?
2. What product or service does it sell?
3. Who is the buyer or user?
4. How does the company make money, or how is it expected to make money?
5. What stage does public or supplied evidence suggest?
6. What traction is publicly verifiable?
7. What differentiates it from relevant alternatives?
8. What major dependencies exist, including partners, platforms, regulation, liquidity, data access, suppliers, or distribution?

## Last 30 Days Research

Search official and independent channels for material company specific developments during the exact window. Use date filters where available and record both event date and publication date.

Core queries:

```text
"Company Name" news
"Company Name" announcement
"Company Name" press release
"Company Name" partnership
"Company Name" funding
"Company Name" acquisition
"Company Name" launch
"Company Name" update
site:official-domain.com Company Name
```

Review the official newsroom, company blog, documentation, LinkedIn, X, GitHub releases, regulator notices, court records, app stores, and credible media where relevant.

For every candidate item, record:

1. Event date.
2. Publication date.
3. Source title.
4. Publisher.
5. URL.
6. Source type.
7. What happened.
8. Why it matters.
9. Whether the item is independently confirmed.

Exclude generic sector news that does not materially involve the company, reposted releases with no added reporting, low substance promotional posts, old events republished during the current window without a new development, and duplicate announcements.

## Adverse Information Sweep

Run targeted negative searches using the company name, legal entity, founders, major products, and token name where relevant.

General terms:

```text
lawsuit
complaint
investigation
regulator
enforcement
fraud
scam
misleading
bankruptcy
insolvency
default
layoffs
breach
hack
exploit
outage
data leak
sanctions
founder controversy
customer complaints
partner dispute
```

An adverse result does not become a reportable fact because it ranks in search. Verify the underlying source, date, entity match, and evidence.

## Sector Conditional Checks

Apply sector checks only when relevant.

Web3:

```text
token unlock
vesting
treasury
wallet concentration
delisting
withdrawal freeze
smart contract exploit
audit issue
bridge exploit
governance attack
rug pull
market manipulation
wash trading
liquidity risk
validator concentration
regulatory action
```

Check token concentration, unlocks, liquidity, smart contract security, governance, exchange dependence, custody, market maker reliance, chain dependence, bridge exposure, and regulation.

AI and software:

```text
data provenance
privacy complaint
copyright lawsuit
model claims
security incident
vendor dependency
customer churn
hallucination
benchmark dispute
```

Check data rights, privacy, copyright, security, benchmark credibility, product reliability, vendor dependence, customer concentration, churn signals, and automation leverage. For AI native businesses, review revenue per employee, gross margin, and agent enabled go-to-market when credible data exists.

Fintech and marketplaces:

```text
custody issue
chargeback
reserve shortfall
licensing
consumer complaint
payment freeze
counterparty failure
insurance coverage
unit economics
off platform leakage
```

Check licensing, custody, reserves, payment processor dependence, insurance coverage, fraud or chargeback exposure, counterparty risk, unit economics, take rate, liquidity, and off-platform leakage.

## Source Tiers

Tier 1 primary and authoritative sources are preferred for material factual claims:

1. Official company website and documentation.
2. Regulatory filings and regulator notices.
3. Court records.
4. Government registries.
5. Official security disclosures.
6. Audited financial statements.
7. Official GitHub repositories and release notes.
8. Direct company or founder statements, clearly labeled as claims.

Tier 2 credible independent reporting tests official claims and establishes external context:

1. Major financial and business media.
2. Reputable technology or sector publications.
3. Established local media for jurisdiction specific events.
4. Named analyst or institutional research with transparent sourcing.

Tier 3 structured databases and specialist sources support evidence but are not automatic ground truth:

1. Company and funding databases.
2. Blockchain explorers.
3. Security audit repositories.
4. App stores and product review platforms.
5. Developer and usage analytics.

Tier 4 social and community sources are discovery and sentiment signals:

1. X.
2. LinkedIn.
3. Reddit.
4. Discord or Telegram screenshots.
5. Anonymous posts.
6. Unverified review sites.

## Evidence Status

Use these statuses consistently:

1. Confirmed: supported by an authoritative primary source or by strong corroborating independent sources.
2. Reported: stated by credible media, databases, analysts, or named sources, but not directly verified from primary records.
3. Alleged: asserted in a complaint, lawsuit, regulator allegation, named dispute, or other formal claim that has not been adjudicated or confirmed.
4. Unverified: surfaced from weak, social, anonymous, conflicting, or insufficient evidence.
5. Not found: actively searched for and not located in reviewed sources.

Use confidence separately when building the evidence register: high, medium, or low.

## Corroboration And Conflict

For a high impact negative claim, require 1 authoritative primary source or 2 credible independent sources. If that threshold is not met, label the claim alleged or unverified and explain the evidence gap.

When sources disagree:

1. State the disagreement.
2. Prefer the source closest to the event and the most authoritative record.
3. Do not average incompatible claims.
4. Keep the point open if it cannot be resolved.
5. Convert the unresolved issue into a call question when material.

Never write that a company has no risks. If the adverse sweep genuinely finds nothing material, write:

```text
No material adverse item was located in the reviewed public sources during this search. This is not a substitute for legal, financial, technical, or private document diligence.
```

## Risk Taxonomy

Screen every company against the relevant categories. Report only material items.

| Category | Examples |
|---|---|
| Identity and ownership | Unclear legal entity, undisclosed parent, founder mismatch, conflicting location or incorporation claims. |
| Team and governance | Founder departures, part time leadership, concentration of control, undisclosed conflicts, weak governance. |
| Product and technology | Product not live, unsupported capability claims, security weakness, outage history, technical dependence. |
| Traction and claims | Self reported metrics, unverifiable customers, inflated partnerships, misleading volume, weak retention evidence. |
| Business model | Unclear payer, weak margins, subsidy dependence, pricing inconsistency, unit economics that may not scale. |
| Market and competition | Crowded category, undifferentiated product, incumbent response risk, narrow wedge, questionable market claims. |
| Financial and funding | Insolvency, runway pressure, down round, unusual financing terms, unclear use of funds. |
| Legal and regulatory | Licensing gaps, regulator action, lawsuits, sanctions, compliance exposure, jurisdiction mismatch. |
| Reputation | Credible customer complaints, founder controversy, partner dispute, repeated unsupported claims. |
| Security and privacy | Hack, exploit, breach, audit issue, exposed data, inadequate incident response. |
| Web3 and token | Concentration, unlock pressure, liquidity dependence, smart contract risk, governance capture, delisting. |
| Counterparty and operations | Dependence on 1 supplier, chain, exchange, custodian, partner, data source, or distribution channel. |

Severity labels:

1. High: could block engagement, materially change the call, or require immediate escalation.
2. Medium: material enough to test before relying on the company claim or proceeding.
3. Low: worth knowing but unlikely to change the immediate call by itself.

Assign severity based on evidence quality, likelihood, and potential impact, not the volume of online discussion.

## PRIME Venture Lens

Use PRIME as a compact strategic test. Do not force a venture conclusion when information is weak.

| Letter | Test | Evidence To Look For |
|---|---|---|
| P | Popular | A market attracting real demand, capital, adoption, or strategic attention, without a clearly settled winner. |
| R | Required | Regulation, compliance, security, operational necessity, or existential pressure forcing the buyer to act. |
| I | Immediate | Pain that must be solved now, including costly workarounds and visible urgency. |
| M | Market growing | Structural trends that expand the opportunity and make early wins compound. |
| E | Expensive to do manually | Meaningful cost, time, labor, risk, or complexity already spent on the problem. |

Classify each letter internally as Supported, Mixed, Unsupported, or Unknown. Compress the result into 1 Venture lens line in the Company Snapshot. Do not show a fake numeric score.

## Osler Internal Coherence Lens

Use the Osler deck as a diligence lens. Test whether the company story holds together across:

1. Growth plan against hiring and go-to-market capacity.
2. Capital raised or requested against use of funds and stated milestones.
3. Sales motion against burn, pricing, procurement, and sales cycle.
4. Product claims against shipped product, customer evidence, or public usage.
5. Market size claims against actual wedge and buyer budget.
6. Differentiation against named competitors and credible substitutes.
7. Founder narrative against domain fluency and operating evidence.

Do not assume incoherence because private data is unavailable. Mark the point as unverified and turn it into a priority call question.

## Structural And Founder Signals

Use these checks only when public evidence or supplied documents support them.

Structural risks:

1. Dormant or nonfunctional founders with meaningful ownership.
2. Multiple founders with unclear full time commitment.
3. Layered SAFEs or unclear dilution math.
4. Hidden side agreements or unusual investor rights.
5. Advisory equity that appears excessive or poorly justified.
6. Unclear legal entity, ownership, licensing, or control.
7. Heavy dependence on a single platform, partner, supplier, exchange, chain, market maker, custodian, or data provider.

Founder and operating signals:

1. Domain fluency.
2. Narrative coherence.
3. Visible instinct to reduce risk before being asked.
4. Speed and evidence of execution.
5. Coachability, where observable.
6. AI leverage and operating efficiency, where relevant.
7. Integrity, including clean answers and a lack of material surprises.

The company read should test whether the opportunity could become category defining where venture scale is relevant. The useful question is why this company and why now. Hand-wavy market claims require a credible wedge, buyer, budget, and validation. Naming a risk clearly can build trust; state uncertainty plainly.

When the company is assessing an investor, partner, or counterparty, use call questions to test relevant experience, support between rounds or engagements, and behavior when things go wrong.

## Evidence Register

Create an internal evidence register before writing the one pager. Save it beside the report as `outputs/company_dd/YYYYMMDD_company_slug_evidence.json`.

Use this schema:

```json
{
  "company": "",
  "official_domain": "",
  "researched_at": "YYYY-MM-DD",
  "news_window_start": "YYYY-MM-DD",
  "news_window_end": "YYYY-MM-DD",
  "claims": [
    {
      "claim": "",
      "category": "identity | company | news | risk | traction | founder | market | structural",
      "source_title": "",
      "publisher": "",
      "url": "",
      "published_at": "YYYY-MM-DD or null",
      "event_at": "YYYY-MM-DD or null",
      "source_type": "official | regulator | filing | independent_media | trade_media | database | social | community",
      "evidence_status": "confirmed | reported | alleged | unverified | not_found",
      "confidence": "high | medium | low",
      "notes": ""
    }
  ]
}
```

## Final Evidence Audit

Before drafting, check that:

1. The identity is resolved or the workflow has stopped for clarification.
2. The exact 30 day news window is calculated and recorded.
3. Recent developments are company specific, dated, sourced, and deduplicated.
4. Every watchout has severity, evidence status, and a source.
5. High impact adverse claims meet the corroboration rule or are clearly labeled alleged or unverified.
6. Missing evidence is described as unknown, not treated as proof.
7. Official claims are separated from independent confirmation.
8. The PRIME and Osler lenses are compressed into decision-useful observations.
9. The final report follows `output_template.md`.
10. The validator passes before the result is returned.
