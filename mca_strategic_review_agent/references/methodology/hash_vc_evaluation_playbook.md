# Evaluating a Company Through a VC / Angel Lens

A reusable framework for assessing an early-stage company. Distilled from live deal work. Use it to structure a first read, a scoring call, and a diligence conversation. It is written to apply to most software, marketplace, and infrastructure businesses, with notes where a category (network effects, crypto, custody, hardware) changes the questions.

---

## 0. The one question everything serves

VCs are not asking "is this a good business." They are asking "**could this return the fund**." That requires a market large enough that a *plausible* outcome is a *very large* outcome. A company can be a genuinely good business and still be a "no" for venture if its ceiling is too low.

Two framings to hold at once:

- **The ceiling.** If everything goes right, how big is this? A niche with a €20M ceiling is a pass for venture even if it's a great business.
- **The entry price.** Return is a function of outcome *and* entry valuation. A modest outcome on a low entry can still be a strong multiple. Always evaluate the opportunity *at the specific valuation offered*, not in the abstract.

> The multiple math: outcome ÷ entry (adjusted for dilution). A $3M entry needs only a ~$100M outcome for ~30x; a $30M entry needs a $1B outcome for the same. Cheap entry lowers the bar for a good return and widens the set of acceptable outcomes.

---

## 1. What to weigh, and how much (stage-adjusted)

Rough weighting shifts by stage. At **pre-seed / seed**, team and market are the majority of the decision because there is little else to underwrite. By **Series A+**, traction and unit economics carry more.

| Factor | What you're testing | Weight at seed |
|---|---|---|
| **Team & founder-market fit** | Unfair advantages: domain insight, distribution, technical edge, prior exits, relationships | Highest (often 40-60%) |
| **Market & "why now"** | Size, growth, and a tailwind that *recently* opened | High |
| **Problem** | Painkiller vs vitamin — acute, frequent, expensive problems win | High |
| **Product & moat** | What *compounds*: network effects, data, switching costs, brand | Medium (thesis-level) |
| **Traction & retention** | Real usage, and whether users stay | Low-Med (little exists yet) |
| **Unit economics** | Net take per transaction, CAC:LTV, gross margin, path to default-alive | Medium |
| **Business model** | How it monetizes, pricing power, leakage | Medium |
| **Competition / defensibility** | Who else is here and why they lose | Medium |
| **The ask** | Raise, use of funds, milestones it de-risks | Medium |

**Do not give a single blended number as the headline.** Score the sub-factors. The sub-scores are where the decision actually lives, and they tell you *what would move a 6 to a 9*.

---

## 2. Core mental models (the reusable lenses)

These recur across deals. Each is a question you can ask of almost any company.

### Team
- **Full-time is non-negotiable signal.** Part-time founders at a priced round are a yellow flag. Ask what *specifically* triggers full-time and when. Tie conviction to it.
- **Founder-market fit** > raw pedigree. What unfair access or insight do *these* founders have that others can't buy?
- **Advisor depth: contractual and active, or a logo on a slide?** Named heavyweights mean little unless they have time, equity, and have *concretely opened doors already.* Always ask "what has this person actually done for you so far?"
- **Split focus is risk.** If a founder also runs another company, probe time allocation, IP/non-compete overlap, and what happens to *this* company if the other one needs them.

### Market & timing
- **"Why now."** Great companies ride a tailwind that only recently opened (a regulation, a platform shift, a cost curve, a behavior change). No credible "why now" is a warning.
- **Fat-tail TAM vs serviceable reality.** Founders lead with the biggest possible number ("$335B market"). The real question is the *serviceable* slice and the **median unit**, not the trophy example. Make them show the economics on a *typical* customer/item, not the headline one.

### Problem & wedge
- **Painkiller vs vitamin.** Acute, frequent, expensive → painkiller. "Nice to have" → vitamin → hard to sell.
- **A feature vs a company.** Could an incumbent replicate this in a sprint? If yes, where's the durable wedge?
- **Useful at low coverage?** For registries, aggregators, and data products: is there a wedge that's valuable at 5% coverage, or is it worthless until near-complete? (See cold-start.)

### Moat — what compounds over time
- Network effects, proprietary data, switching costs, brand, regulatory capture, economies of scale. Without something that compounds, success just invites competition that erodes returns.
- **Stress-test the stated moat.** If the pitch says "the moat is X," ask what breaks X. (Example: if the moat is *neutrality*, the moat breaks the moment the company also becomes a competing participant — see the neutrality trap below.)

### Traction & retention
- **Retention is the truth serum.** Growth can be bought; retention can't. A leaky bucket disguised by paid growth is the most common trap. Ask for cohort retention, not just top-line growth.
- **Engagement over vanity metrics.** Signups and GMV are easy to inflate; repeat usage and settled transactions are not.

### Unit economics & survival
- **Net take, not headline take.** A "2.5% fee" that's *shared* with a partner might net ~1%. Always ask for the number the company actually *keeps* after splits and pass-throughs.
- **Thin take → volume game.** A slim net margin turns the business into a volume play, and volume depends on liquidity/demand that usually doesn't exist yet. Ask: **what settled volume gets you to default-alive** (self-sustaining without another raise)?
- **CAC:LTV and payback** where relevant; **gross margin** always.

### Business model & pricing power
- **Who controls the price?** A take rate holds only if the company has leverage. If the essential participants are powerful incumbents, they can **compress the fee** ("we'll integrate at 1%, not 2.5%") or **refuse to participate** and starve the model. Ask what holds pricing if the biggest players squeeze or decline.
- **Leakage / disintermediation.** On high-value transactions, the fee is a large absolute number and a real incentive for two matched parties to transact *off-platform*. What structurally keeps them on it (escrow, custody, guarantees, provenance, remedies) beyond good intentions?

### Distribution
- **Distribution beats product.** Great products die from no distribution. How does this reach customers, and is it single-channel/platform-dependent (fragile) or durable?

### Competition & defensibility
- Map the *specific* incumbents, not a generic field. For each: why do they lose, and what stops them from adding this as a feature?
- **"They could build it" is not fatal — lead time is the question.** What's been built or *signed* that a well-capitalized incumbent can't quickly replicate?

---

## 3. Category-specific traps

### Network-effect / marketplace / infrastructure plays
- **Cold-start / chicken-and-egg is the whole game.** The registry/book/network is worthless until it has density. Ask: what's the *first* wedge that's useful before the network exists, and **who seeds the first liquidity/supply** (the company, the first partner, or organic)?
- **Minimum viable density.** At what point does the flywheel run *without subsidy*? How much must be seeded to get there, and is that capital in the raise?
- **Integrator retention in a "neutral" network.** If the network aggregates competitors, what stops participant #2 from pulling out when they see their demand routed to a rival? Neutrality is fragile.

### The neutrality trap (protocol vs marketplace)
A recurring, important tension: a company pitches itself as a **neutral layer everyone builds on** *and* runs **its own competing surface** that captures the full transaction. These conflict. If neutrality is the stated moat, the company disqualifies itself the moment it becomes a node competing with its own integrators. Force the choice, and if they run both, ask for the *documented* rules that prevent the owned surface from getting hidden preference.

### Marketplaces for non-fungible goods (fungibility / match-time risk)
When a bid is placed against an *abstraction* (a "grade," a "spec," a "SKU") but a specific, non-identical physical item fills it, deals can break at match time on condition, quality, or authenticity. Ask: **expected failure rate, who bears the cost, and what the remedies are.** A "liquid order book" that still needs a human to eyeball the actual item before money moves is less liquid than it looks — and it frays exactly where the money is (high-value items).

### Crypto / on-chain components
- **Is the chain load-bearing or decoration?** Good use: a shared, auditable state across parties who don't share a database; atomic settlement; portable provenance. Bad use: crypto for its own sake, adding wallet friction to a problem users don't feel.
- **Friction & UX.** Is there a wallet in the flow, or is onboarding walletless/custodial so the UX stays familiar?
- **Regulatory surface.** Funds held on-chain = a security and money-transmission surface. **Fractionalization** invites securities questions. Ask whether they've taken specific legal advice (money transmission, custody, sanctions, consumer protection) and the cost/timeline to be compliant at launch.
- **Financing signal.** A token/crypto raise this early brings a harder-to-manage holder base than VCs; often premature.

### Custody / physical-asset / hardware
- **Not asset-light.** Holding real inventory means theft, damage, insurance, and authentication liability, plus a long *trust curve* vs incumbents who spent years earning it. "Just software underneath" framing often hides a custody business.

### Data-as-a-second-business
- Frequently pitched as upside. Correctly sequenced, it comes *after* the company has earned proprietary transaction/custody data through its core product. Treat it as a credible second line, not current revenue — and be skeptical if it's presented as near-term money.

---

## 4. Scoring

Score sub-factors 1-10, then reason about the blend. Example structure:

| Sub-factor | Score | Note |
|---|---|---|
| Problem insight | /10 | Is it sharp, specific, non-obvious? |
| Market & timing | /10 | Size + credible "why now" |
| Strategy & moat | /10 | Does something compound? Is the stated moat stress-tested? |
| Product & execution | /10 | Build quality, velocity; craft is itself early signal |
| Business model | /10 | Net take, pricing power, leakage |
| Team | /10 | Full-time? Founder-market fit? Real access? |
| Traction | /10 | Usage, retention, signed vs warm |

**Interpreting the blend:**
- **8-10:** Strong conviction; the decision is on terms/price.
- **6.5-7.5:** "Take the meeting, lean in." Promising, but 1-2 open questions decide it. State explicitly *what would move it to an 8*.
- **<6:** Pass unless the price is asymmetric enough to justify the risk.

Always end a score with: **"what specifically separates this from a 9?"** Usually it's a short, nameable list (team goes full-time; convert a warm intro to signed; prove retention).

---

## 5. Red flags and yellow flags

**Red (hard to get past):**
- Endangering users; dishonesty in the data room; fabricated traction.
- No credible "why now."
- A feature an incumbent replicates trivially, with no compounding moat.
- Unit economics that don't work even in the good case.

**Yellow (probe hard, can be resolved):**
- Part-time founders at a priced round.
- Warm intros presented as traction (necessary, not proof).
- Top-down TAM with no bottom-up build; economics shown only on trophy examples.
- Thin, shared take rate + dependence on powerful incumbents for participation.
- "We'll figure out monetization / retention later."
- Advisor logos with no active involvement.
- Single-channel or platform-dependent distribution.

---

## 6. Diligence question bank (generalize and reuse)

Lead with the 2-3 that *gate the check*. Keep questions pointed so answers are hard to dodge.

**Team**
- What triggers each named founder going full-time, and when? Any split focus, and what happens to this company if the other commitment pulls them away?
- Which advisors are contractual and active (time, equity), and what have they *concretely* opened so far?

**Market & wedge**
- What's the "why now" that didn't exist 2-3 years ago?
- Show the economics on a *median* customer/unit, not the headline example.

**Supply / cold-start (network plays)**
- What's the minimum viable density for the network to feel useful, and who seeds the first liquidity/supply?
- How many participants / what volume before the flywheel runs without subsidy?
- What's the wedge that's useful *before* the network is complete?

**Moat & competition**
- If your moat is X, what breaks X? (Stress-test the stated defensibility.)
- Name the specific incumbents. Why do they lose, and what stops them adding this as a feature? What's your lead time?
- (Neutral networks) What stops participant #2 pulling out when they see demand routed to a rival?

**Economics**
- After all splits and pass-throughs, what do you *net* per transaction?
- What settled volume gets you to default-alive?
- What holds your take rate if the biggest players push to compress it, or decline to participate at all?
- (High-value goods) What's the leakage rate, and what structurally keeps large matched trades on-platform?

**Product / settlement risk**
- (Non-fungible goods) When a bid/spec is matched but the specific item disagrees on quality/condition/authenticity: expected failure rate, who bears the cost, what are the remedies?

**Crypto / regulatory (if applicable)**
- Is the chain load-bearing? Wallet in the flow or walletless? Fractionalization on the roadmap?
- Have you taken specific legal advice (money transmission, custody, sanctions, consumer protection)? Cost and timeline to launch compliant?

**The round**
- What is the raise *for*, in concrete milestones? What does it de-risk for the next round? What's default-alive runway?
- Who else is in or circling, and on what terms?

---

## 7. Objectivity discipline

- **Steelman first, then stress-test.** Write the strongest version of the bull case *and* the specific counter-case (empirical disputes, incumbent responses, failure modes). A one-sided memo is a weak memo.
- **Separate the idea from the team.** The idea can be sound while *this team* is the wrong bet, or vice versa. Say which is carrying the score.
- **Anchor claims to evidence.** Founder-provided figures are unverified until independently sized. Label them as such, and size the serviceable market and median-unit economics yourself before an IC discussion.
- **You are informing a decision, not making it for anyone.** Present the trade-offs and the open questions; let the reader navigate. (And note: this is analysis, not financial or legal advice.)

---

## 8. A compact first-pass template

Use this to structure any initial read:

1. **What it is** — one honest paragraph, no jargon.
2. **The sharpest thing** — the single strongest insight or asset.
3. **10x/100x?** — ceiling, and the multiple math *at this entry price*.
4. **Sub-scores** — the table in §4, with the "what makes it a 9" line.
5. **Concerns & pitfalls** — the 3-5 that actually matter, category traps included.
6. **What determines success** — usually distribution, retention, the supply/cold-start unlock, and whether the team goes full-time and converts access into signed commitments.
7. **Questions that gate the check** — the 2-3 you'd want answered first.
