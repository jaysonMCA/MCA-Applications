MCA STRATEGIC REVIEW AGENT
Master Project Context, Product Specification, and Build Direction
Version: 0.1
Owner: Jayson
Project Sponsor and Reviewer: Hash
Technical Collaboration: Danylo
Company: MultiChain Advisors, MCA
Status: Internal prototype
Primary Goal: Build a reusable AI driven strategic company review system before committing to a full application.
1. Why This Document Exists
This document provides the full context required to understand and build the MCA Strategic Review Agent.
The coding environment should not assume prior knowledge of:
MCA
The MCA team
The Prized project
The VC and PE review methodology
The research completed for this project
The intended client deliverable
The difference between the internal analysis and external output
The reason this tool is being built
The current project scope
Future ideas that are intentionally outside the first version
This document should therefore be treated as the primary project context and source of truth.
The goal is to enable a coding agent, such as Claude Code, Codex, or another VS Code based AI coding system, to understand the project without requiring access to the original conversations that led to it.
2. What MCA Is
MultiChain Advisors, referred to internally as MCA, is a growth and capital markets advisory firm.
MCA works with companies across Web3, emerging technology, Web2, AI, financial markets, and adjacent sectors.
MCA's work can include areas such as:
Capital advisory
Token generation and token strategy
Mergers and acquisitions
Tokenomics
Go to market strategy
Growth
Marketing
Partnerships
Market expansion
Web3 expansion
PR and media
Exchange related strategy
Community and ecosystem growth
AI services and automation
Web2 growth and operational support
MCA is not only a capital provider.
Its value comes from combining strategic thinking with execution experience.
Clients and prospects often work with MCA because they believe MCA can:
Help them scale
Identify problems they are not seeing
Provide experienced strategic input
Execute work their existing team does not have the bandwidth or capability to complete
Open relevant networks, partnerships, markets, and distribution opportunities
Bring practical experience from previous engagements
This context matters because the Strategic Review Agent should not sound like a generic AI investment analyst.
It should reflect MCA's positioning as an experienced strategic operator.
3. Relevant MCA Team Context
For this project, the main stakeholders are:
Hash
Hash initiated the core concept.
His original use case came from reviewing an early stage company called Prized.
Hash manually reviewed the Prized company materials and created a strategic document identifying:
The core company questions
Key strategic observations
Strengths
Weaknesses
Opportunities
Threats
Questions for the next discussion
Hash wants to make this type of work repeatable without requiring the same amount of senior team time on every company.
Hash does not currently want a large BD intelligence platform.
The immediate project is narrower.
The objective is to recreate and improve the strategic review process using AI.
Jayson
Jayson works on Business Development and Strategy at MCA.
Jayson is responsible for:
Turning Hash's concept into a repeatable framework
Researching the VC and PE methodology
Structuring the agent workflow
Defining the human inputs required
Testing whether outputs are useful for real BD conversations
Testing the system against company decks
Refining the methodology
Helping translate the methodology into an internal tool
Jayson frequently speaks with multiple prospects and needs outputs that are useful in real conversations rather than purely academic investment analysis.
Danylo
Danylo may support technical implementation and AI workflow development.
The system architecture should therefore remain understandable and editable rather than becoming an unnecessarily complex application.
4. Where The Project Came From
Hash was approached to review an early stage company called Prized.
Prized was looking for strategic angels and had strong industry connections, including experienced advisors.
Hash reviewed the company's materials and produced a document called:
Prized Considerations and Questions
The document was valuable because MCA was able to provide useful strategic thinking before any paid engagement existed.
The underlying business idea became:
If MCA can provide meaningful strategic value during the early stage of a relationship without spending large amounts of senior team time, MCA can:
Build trust
Demonstrate expertise
Improve the quality of the relationship
Create a stronger reason for another conversation
Potentially improve conversion into future commercial opportunities
The tool is therefore not intended to sell MCA services directly.
The tool itself is a piece of value.
5. Important Scope Clarification From Hash
Earlier versions of this project considered a broader BD intelligence system.
That larger concept included:
Preparing BD before calls
Searching MCA case studies automatically
Surfacing previous MCA campaigns
Matching prospects with previous MCA clients
Generating engagement angles
Supporting proposals
Creating wider BD intelligence
Hash clarified that these features are not necessary for the current project.
MCA currently does not have enough sales call volume to justify building a large automated BD preparation platform.
Hash specifically wants the current tool to focus on:
Reviewing the company
Using the deck as a primary input
Using the MCA team member's own thoughts as an input
Using the transcript where available
Performing external research
Performing macro analysis
Identifying opportunities and threats
Identifying strategic questions
Producing a uniform MCA review deliverable
Commercial engagement angles, MCA case study matching, proposals, and sales recommendations should remain separate from the current review.
6. The Core Product
The simplest description of the product is:
A local AI strategic company review agent for MCA.
The system receives company information and MCA human judgment.
It researches the company and external environment.
It then produces a structured strategic review.
The basic flow is:
Company materials
↓
MCA reviewer opinion
↓
External research
↓
VC and operator analysis
↓
Strategic tensions
↓
SWOT
↓
Prioritized questions
↓
MCA branded review
The system should make this process repeatable across companies.
7. What The Tool Is Not
The first version is not:
A CRM
A lead scoring system
A proposal generator
A full investment committee system
A legal diligence system
A financial modeling system
A BD preparation platform
A case study retrieval platform
A sales automation platform
A client portal
A large SaaS application
An autonomous investment decision maker
The first version should remain narrow enough to test and change quickly.
8. Target User
The primary user is an MCA team member reviewing a company.
The user may be:
A BD team member
A consultant
An engagement manager
A strategy team member
A senior MCA team member
The long term goal is for the tool to be usable by another MCA team member without requiring Jayson to operate it.
The system should therefore guide the user through the process.
The user should not need to understand the underlying prompts or files.
9. Primary Inputs
Required Input
Pitch Deck
The pitch deck is the primary required input.
The system should not begin a full review without a deck unless the user explicitly chooses a limited review.
The deck provides:
Company narrative
Problem
Product
Business model
Market
Team
Traction
Competition
Fundraising information
Strategic claims
The system must remember that information in the deck is company provided information.
A statement appearing in a deck is not automatically a verified fact.
Strongly Recommended Input
MCA Reviewer Opinion
The MCA reviewer's personal opinion is a critical input.
The purpose of the system is not to replace MCA judgment with AI judgment.
The human reviewer should tell the system:
What they think
What impressed them
What concerns them
What they did not believe
What felt unclear
What they think matters most
What they want researched
The AI then strengthens, challenges, validates, and structures this judgment.
Optional Inputs
The system should also accept:
Call transcript
Company website
Social accounts
GitHub
Product links
Whitepaper
Technical documentation
Financial documents
Company data
Existing research
Notes from other MCA team members
Any additional supporting documents
The system should adapt according to what is available.
10. Information Layers
The system should think about information through 4 layers.
Layer 1: Company Narrative
Sources include:
Deck
Website
Company documents
Social accounts
This tells the system how the company presents itself.
Layer 2: Founder Narrative
Sources include:
Call transcript
Written answers
Follow up conversations
This reveals how the founders explain the business when challenged.
Layer 3: MCA Judgment
Sources include:
Reviewer notes
Reviewer interview answers
MCA internal observations
This represents the human strategic perspective.
Layer 4: External Reality
Sources include:
Company research
Competitor research
Market research
Industry research
Regulation
Macro developments
Funding environment
Public evidence
The final assessment should emerge from the interaction between these 4 layers.
11. Reviewer Interview
The system should not require the reviewer to prepare polished notes.
It should interview them conversationally.
The system should explain:
Give me your actual opinion. Do not worry about making it sound polished. Tell me what caught your attention, what you did not believe, what confused you, and what you think matters. I will structure it later.
Core questions:
What do you think this company is actually building?
What stood out positively?
What felt weak, unclear, contradictory, or unsupported?
What do you think the biggest strategic issue is?
What assumption are you least convinced by?
What part of the company would you personally investigate further?
Is there an opportunity you think the founders may be missing?
Is there a threat you think they may be underestimating?
What would you ask the founders next?
Is there anything specific you want the agent to challenge?
The system should behave adaptively.
If the reviewer has already answered several questions naturally, do not repeat them.
If an answer is vague, ask a useful follow up.
Example:
Reviewer:
I don't really buy the GTM.
Agent:
What specifically worries you, lack of distribution, customer acquisition cost, partner dependence, unclear buyer, or something else?
Reviewer:
Mostly partner dependence.
Agent:
Understood. I will treat partner incentives and distribution dependence as research priorities.
12. Transcript Analysis
When a call transcript is provided, the system should analyze it carefully.
The transcript should be used to identify:
Information absent from the deck
Questions already answered
Contradictions
Founder priorities
Founder uncertainty
Weak answers
Strong answers
Strategic decisions that remain unresolved
Claims requiring validation
Follow up questions
Potential misunderstandings by the MCA reviewer
The agent must not ask the founder a question in the final deliverable if it has already been clearly answered in the transcript.
13. Research Requirement
The system should conduct external research.
This is a required part of a complete review.
The purpose of the research is not to create a giant market report.
The purpose is to test whether external reality changes the way MCA should think about the company.
The agent should ask:
Does this information materially change the assessment?
If not, exclude it.
14. Research Planning
Before conducting deep research, the agent should generate a research plan.
Example:
Research Plan
Company: Prized
Competitive position against Alt
Why it matters:
Alt already operates adjacent infrastructure and could affect the defensibility thesis.
Collectibles vault landscape
Why it matters:
The company appears dependent on custody infrastructure and trust.
Availability of grading and certification data
Why it matters:
Access to data may depend on incumbent cooperation.
Marketplace economics
Why it matters:
The deck does not clearly establish economics on typical transactions.
Regulatory exposure
Why it matters:
The onchain structure may create additional security, custody, or compliance requirements.
The MCA reviewer should be able to:
Approve the plan
Add research areas
Remove irrelevant research
15. External Research Areas
The agent may research:
Company
Founders
Team history
Funding
Product
Partnerships
Traction
Previous companies
Public announcements
Customer response
Company claims
Competition
Direct competitors
Adjacent competitors
Incumbents
Existing substitutes
Recently funded companies
Competitor product changes
Competitive advantages
Competitive weaknesses
Likely incumbent response
Market
Market size
Market direction
Customer behavior
Pricing
Demand trends
Industry economics
Market concentration
Distribution structure
Funding conditions
Macro Environment
Regulation
Technology shifts
Economic conditions
Capital availability
Industry consolidation
Platform changes
Geographic developments
Customer sentiment
Structural market changes
Ecosystem developments
16. Opportunities and Threats
Hash specifically requested deeper analysis of company opportunities and threats.
These should come primarily from external analysis.
Opportunities
An opportunity is an external condition that the company may be able to capture.
Examples:
Market growth
New regulation
Competitor weakness
New technology
New distribution
New partnerships
Geographic expansion
Data monetization
New customer behavior
Industry fragmentation
For each opportunity, determine:
What is happening?
Why does it matter?
Why could this company capture it?
What must happen for the opportunity to become real?
Threats
A threat is an external condition that may damage the company's ability to execute.
Examples:
Competitor response
Regulation
Platform dependency
Market contraction
Funding constraints
Customer behavior change
Technology change
Partner resistance
Supply constraints
Industry consolidation
For each threat, determine:
What is the threat?
How does it affect the company?
How serious is it?
What evidence supports it?
What should MCA ask the company about it?
17. VC And PE Lens
Hash asked for the system to review companies through a VC and PE style lens.
The framework should be useful for evaluating early stage companies, particularly pre seed and seed companies.
The objective is not simply to answer:
Is this a good company?
The deeper venture question is:
Can this become a sufficiently large and durable company to justify the risk and entry valuation?
The agent should consider:
Company quality
Fundability
Market ceiling
Entry valuation
Dilution
Execution risk
Future financing risk
Strategic defensibility
18. Key Research Finding: Fundability Is Not The Same As Company Quality
The external research completed for this project identified an important distinction.
Signals that increase the probability of receiving venture funding are not necessarily the same signals that best predict long term company quality.
At very early stages, team quality is heavily weighted by investors.
As companies develop, market quality, product quality, retention, distribution, customer behavior, and economics become increasingly important.
Therefore:
At pre seed, underwrite the people, insight, problem, timing, and ability to discover the correct product.
At seed, increasingly underwrite real evidence, including retention, customer pull, distribution, economics, and repeatability.
The system must adjust its analysis according to stage.
19. Pre Seed Review Priorities
At pre seed, prioritize:
Founder market fit
Team quality
Commitment
Problem severity
Market
Why now
Insight
Product thesis
Learning velocity
Distribution wedge
Potential moat
Early customer validation
Raise logic
Do not automatically punish a pre seed company for having:
No revenue
Limited product
Limited retention data
Small current team
Instead ask:
What is the most credible evidence that should exist at this stage and in this category?
20. Seed Review Priorities
At seed, increase the importance of:
Customer pull
Retention
Revenue quality
Distribution repeatability
Product usage
Growth
Unit economics
Capital efficiency
Competitive evidence
Repeatability
Founder quality remains important, but founder narrative should become less able to compensate for weak real world evidence.
21. Core Evaluation Dimensions
The review should analyze:
Team
Ask:
Why these founders for this problem?
Look for:
Founder market fit
Relevant experience
Technical capability
Commercial capability
Complementary skills
Recruiting ability
Speed
Adaptability
Honesty
Commitment
Access
Relationships
Founder prestige alone is weak evidence.
Advisor logos are weak evidence unless the advisors are genuinely active.
Problem
Determine:
Who experiences the problem?
How painful is it?
How frequently does it happen?
What does the customer do today?
How much money or time is already spent solving it?
Does the problem cause actual behavior change?
Market
Determine:
Serviceable market
Initial target segment
Expansion potential
Market growth
Market structure
Pricing power
Whether the ceiling supports venture outcomes
Avoid relying entirely on large top down TAM numbers.
Why Now
Identify what changed recently.
Possible catalysts:
Technology
Regulation
Infrastructure
Cost
Distribution
Customer behavior
Market structure
A generic statement that a market is growing is not enough.
Product
Determine:
What is differentiated?
What is technically difficult?
What is strategically valuable?
What insight does the company have?
Why does the product win?
Moat
Ask:
What gets stronger as this company succeeds?
Possible answers:
Proprietary data
Network effects
Switching costs
Brand
Distribution
Workflow ownership
Cost advantage
Regulatory advantage
Exclusive access
Ecosystem positioning
Distribution
Determine exactly where customers come from.
Avoid accepting statements like:
We will use sales and marketing.
Instead ask:
Where do the first 10 customers come from?
Where do the first 100 come from?
Where do the first 1,000 come from?
The equivalent question should be used for users, suppliers, developers, liquidity, partners, or marketplace participants.
Traction
Separate:
Interest
Verbal commitment
Signed commitment
Pilot
Paying customer
Repeat customer
Retained customer
Expanded customer
Repeat behavior is stronger evidence than signup.
Retention
When enough operating history exists, retention becomes a major signal.
Growth can be purchased.
Retention is much harder to manufacture.
Economics
Use net economics.
Include:
Gross margin
Contribution margin
Customer acquisition
Revenue sharing
Infrastructure costs
Model costs
Incentives
Custody
Shipping
Payment costs
Other pass through expenses
Capital Efficiency
Ask:
What uncertainty is being removed with every dollar and month of runway?
The question is not simply whether burn is low.
The question is whether the company is using capital to reach a stronger financeable state.
Competition
Do not ask only:
Who are your competitors?
Ask:
Which specific companies are closest?
Why do they lose?
What can they copy?
How quickly can they copy it?
What prevents them from absorbing the product?
How does the company improve faster than competitors?
The Round
Understand:
Raise amount
Valuation
Dilution
Use of funds
Runway
Milestones
Next financing expectations
What the current round actually removes as a risk
22. Central Strategic Tensions
This is one of the most important functions in the entire system.
A strong review should not produce 15 equally important observations.
It should identify the 2 or 3 issues that everything else depends upon.
A strategic tension is usually:
A major strategic choice
A contradiction
A dependency
An assumption
An execution bottleneck
A structural market problem
The Prized review is the reference example.
Hash identified central issues including whether Prized was fundamentally a neutral protocol or an owned marketplace, and where the initial supply would come from.
The final review then built around those issues.
The system should attempt to find the equivalent issues for every company.
Bad conclusion:
Customer acquisition will be important.
Better conclusion:
The business depends on enterprise distribution, but the current GTM assumes founder led sales. The company may therefore be designing for a distribution model it does not yet possess.
The system should prioritize insight over summary.
23. Hash's Prized Evaluation Playbook
Hash created a reusable VC and angel evaluation memory based on the Prized process.
That memory should be considered foundational project material.
Important principles include:
Venture investors are ultimately asking whether the company can generate an outcome large enough to justify the investment
Entry valuation matters
Team and market matter heavily at early stage
Founder market fit matters more than prestige alone
Why now matters
Painkiller problems are stronger than optional problems
Moats should compound
Distribution matters
Retention is a stronger signal than vanity growth
Net economics matter more than headline economics
Pricing power matters
Leakage and disintermediation matter
Cold start matters for networks and marketplaces
Neutral platform models can conflict with owned marketplace models
Crypto components should be tested for whether they are actually necessary
Custody introduces operational and trust risk
Data businesses should not automatically be treated as immediate revenue
Questions should focus on the issues that actually gate conviction
This framework should be preserved while allowing external research to refine or challenge it.
24. Category Overlays
The system should detect the relevant category and apply additional diligence.
AI
Investigate:
Retention
Workflow ownership
Model dependency
Gross margin after inference cost
Reliability
Proprietary data
Switching costs
Distribution
What becomes defensible as foundation models improve
Do not equate rapid ARR with durable product market fit.
Web3
Investigate:
Real human users
Incentive adjusted activity
Organic fees
Liquidity
Token unlocks
Treasury
Security
Custody
Regulation
Jurisdiction
Whether blockchain is actually necessary
Do not automatically equate wallets, TVL, transactions, or token price with sustainable adoption.
Marketplaces
Investigate:
Initial supply
Initial demand
Cold start
Minimum useful density
Cost of reaching density
Match rate
Time to match
Repeat usage
Net take
Multi homing
Disintermediation
Supply retention
The first supply and first demand questions are often central.
SaaS
Investigate:
Retention
Usage
Net retention
Gross retention
Gross margin
CAC
Payback
Sales cycle
Customer concentration
Actual deployment versus contracted revenue
Consumer
Investigate:
Cohort retention
Usage frequency
Organic acquisition
Paid acquisition
Habit formation
Daily, weekly, and monthly usage
Monetization
Whether launch novelty becomes repeat behavior
25. Evidence Model
Every major claim in the system should have an internal evidence type.
Use:
Verified Fact
Externally supported information.
Company Claim
Something stated by the deck, founder, website, or company materials.
MCA Opinion
A judgment from the MCA reviewer.
Research Finding
Something learned through external research.
Agent Inference
A conclusion created by connecting multiple pieces of evidence.
Unknown
Something that cannot currently be established.
This distinction is important.
The agent should never convert a company claim into a verified fact simply because the deck states it confidently.
26. Confidence Model
Every significant internal conclusion should receive a confidence level.
High Confidence
Supported by strong evidence or multiple reliable sources.
Medium Confidence
Reasonably supported but dependent on assumptions.
Low Confidence
Preliminary and requiring validation.
Confidence and company quality are separate variables.
A company can appear strong while the available evidence remains weak.
27. Missing Information
Missing information should not automatically be treated as a weakness.
The default process should be:
Missing information
↓
Explain why it matters
↓
Determine whether it affects the thesis
↓
Convert it into a diligence question
This avoids punishing companies simply for leaving something out of a deck.
28. Contradiction Detection
The system should actively identify contradictions.
Examples:
Deck says enterprise first, founder says consumer first
Deck says decentralized, operations rely on centralized custody
Deck says protocol, founder describes a marketplace
Deck claims a partnership, public information indicates only discussion
Company claims strong distribution, no evidence exists
Reviewer believes the team is fully committed, company materials indicate other active companies
Contradictions should appear internally and may become questions in the final review.
29. Internal Scoring
The scoring model is primarily an internal thinking tool.
It should not dominate the external client deliverable.
Recommended pre seed weighting:
Team and founder market fit, 22%
Problem severity and customer insight, 15%
Market size and timing, 15%
Product differentiation and moat, 12%
Distribution and GTM, 10%
Traction and retention, 7%
Unit economics and capital efficiency, 6%
Business model and pricing, 5%
Competition, regulatory, and geographic risk, 4%
Round, valuation, and milestone logic, 4%
Recommended seed weighting:
Team and founder market fit, 15%
Problem severity and customer insight, 10%
Market size and timing, 12%
Product differentiation and moat, 12%
Distribution and GTM, 12%
Traction and retention, 18%
Unit economics and capital efficiency, 10%
Business model and pricing, 5%
Competition, regulatory, and geographic risk, 3%
Round, valuation, and milestone logic, 3%
Score each dimension from 1 to 5.
The score is not a probability of success.
It is a method for organizing judgment and identifying where the company is strong or unresolved.
30. Hard Gates
Certain problems should not disappear inside a weighted average.
Integrity Gate
Examples:
Fabricated traction
Misrepresented partnerships
Hidden material information
Contradictory evidence suggesting dishonesty
Feasibility Gate
The product depends on an assumption that credible evidence suggests cannot work.
This may be:
Technical
Regulatory
Economic
Operational
Commitment Gate
The core founders do not have enough commitment to execute.
Economics Gate
The business structurally loses money without a credible path to better economics.
Venture Return Gate
Even a strong outcome does not create enough return relative to valuation and likely dilution.
Hard gates should be surfaced before the numerical score.
31. Internal Output
The system should generate a detailed internal analysis file.
Suggested structure:
Company Overview
What the company is.
Stage Assessment
Pre seed, seed, or other.
Reviewer Read
Summary of the MCA reviewer's opinion.
Company Claims
Important claims made by the company.
Verified Research
Externally validated information.
Strategic Tensions
The 2 or 3 issues that matter most.
Strengths
Internal advantages.
Weaknesses
Internal limitations.
Opportunities
External positive developments.
Threats
External negative developments.
Information Gaps
What is still unknown.
Contradictions
Where sources disagree.
Category Analysis
Relevant AI, Web3, SaaS, marketplace, consumer, or other overlay.
Scorecard
Internal scoring.
Confidence
Evidence confidence.
Questions
Prioritized diligence questions.
What Would Change Our View
Specific evidence that would materially increase or decrease conviction.
Sources
Research provenance.
32. External MCA Deliverable
The client facing output should be much shorter than the internal analysis.
The Prized document is the initial standard.
The preferred structure is:
MCA MARKET INTELLIGENCE
DEAL REVIEW
CONSIDERATIONS AND NEXT STEPS
Company name
Date
MCA reviewer
Opening Note
A short paragraph thanking the company for sharing the materials and explaining that the document contains MCA's initial read and the questions MCA would like to work through.
In Brief
1 concise paragraph.
This section should identify the 2 or 3 central strategic questions.
It should not summarize the entire deck.
Our Read
3 to 5 strategic conclusions.
Each conclusion should include:
Headline
Explanation
Why it matters
These should be actual strategic opinions.
SWOT
Strengths
Internal advantages.
Weaknesses
Internal limitations or concerns.
Opportunities
External developments the company may capture.
Threats
External developments that may negatively affect the company.
Questions for Next Steps
6 to 10 questions.
The first 2 or 3 should be marked as priority.
The questions should address the major strategic tensions first.
33. MCA Writing Standard
The output should sound:
Senior
Direct
Thoughtful
Strategic
Commercially aware
Grounded
Constructive
Avoid:
Generic consulting language
Empty praise
Excessive explanation
Generic SWOT points
Repeating the deck
Corporate filler
AI sounding phrasing
Aggressive investor language that damages the relationship
Unsupported certainty
The objective is to challenge the company while still providing useful value.
34. MCA Branding Standard
The first version does not require advanced graphic design.
The system should standardize the textual brand.
Use:
MCA Market Intelligence
Deal Review
Considerations and Next Steps
Confidential
The external output should consistently follow the same section order and writing density.
Future versions may generate styled PDF or document outputs.
The initial version can generate Markdown and later convert it into a branded document.
35. Self Critique Pass
Before finalizing the analysis, the agent should challenge itself.
Ask:
Is this analysis generic?
Could this point apply to 10 unrelated startups?
Are we repeating the deck?
Did we treat company claims as facts?
Are opportunities genuinely external?
Are threats genuinely external?
Are weaknesses genuinely internal?
Did we miss an important competitor?
Is the research current?
Are the first 2 questions genuinely the most important?
Did we ignore the MCA reviewer's opinion?
Did we over rely on the MCA reviewer's opinion?
Is anything speculative presented as fact?
What would Hash consider obvious?
Is there a sharper way to frame the central issue?
If the output fails this review, revise it automatically before presenting the draft.
36. Human Review Loop
The system should remain AI assisted rather than fully autonomous.
Before finalizing the external deliverable, present the central conclusions to the MCA reviewer.
Example:
Draft analysis complete.
I currently believe the 3 central conclusions are:
Conclusion A
Conclusion B
Conclusion C
Do you disagree with any of these before I finalize the MCA review?
The reviewer should be able to respond naturally.
Example:
Conclusion 2 is weak. Distribution is the bigger issue.
The system should then revise the analysis and deliverable.
This is a core feature.
37. Desired User Flow
The local prototype should eventually support the following workflow.
Step 1
User starts a new review.
System asks:
What company are we reviewing?
Step 2
System asks:
Do you have the pitch deck?
If yes, ingest it.
If no, explain that the review will be limited.
Step 3
Read the deck.
Return a short internal understanding.
Ask the reviewer to correct major misunderstandings.
Step 4
Ask for additional materials:
Transcript
Website
Socials
GitHub
Financials
Product
Other documents
Step 5
Conduct the reviewer interview.
Step 6
Analyze all supplied materials.
Step 7
Create the research plan.
Step 8
Ask the reviewer whether to proceed or add research.
Step 9
Conduct external research.
Step 10
Build the internal evidence model.
Step 11
Determine company stage.
Step 12
Apply stage specific review methodology.
Step 13
Apply category overlays.
Step 14
Identify strategic tensions.
Step 15
Generate SWOT.
Step 16
Generate internal scoring.
Step 17
Generate prioritized questions.
Step 18
Run self critique.
Step 19
Present central conclusions to the reviewer.
Step 20
Allow human challenge and revision.
Step 21
Generate the final MCA deliverable.
Step 22
Save all underlying files.
38. Local Prototype Architecture
The initial build should run locally.
Avoid unnecessary infrastructure.
Suggested repository:
mca_strategic_review_agent/

README.md

PROJECT_CONTEXT.md

SKILL.md

memory/
    mca_context.md
    vc_success_signals.md
    vc_review_methodology.md
    category_overlays.md
    research_rules.md
    mca_output_standard.md

templates/
    reviewer_interview.md
    research_plan.md
    internal_analysis.md
    evidence_log.md
    final_deliverable.md

cases/

examples/
    prized/

references/
    vc_research/
    prized/

outputs/

39. Case Structure
Each company should have its own case folder.
Example:
cases/
    prized/
        source/
            deck.pdf
            transcript.txt
            company_links.md
            supporting_documents/

        reviewer/
            reviewer_notes.md

        research/
            research_plan.md
            research_findings.md
            sources.md

        analysis/
            evidence_log.md
            scorecard.md
            strategic_analysis.md

        output/
            internal_review.md
            final_deliverable.md

The system should create this automatically.
40. Why Case Folders Matter
The tool should not rely on 1 huge chat history.
Every review should have its own auditable record.
This gives MCA:
Reproducibility
Transparency
Editability
Easier review
Easier debugging
Easier future automation
A record of how the final conclusion was created
41. Memory Files
The system should keep permanent methodology separate from company specific information.
Recommended memory files:
mca_context.md
Contains:
What MCA is
MCA positioning
Relevant services
Purpose of the review
MCA tone
Scope restrictions
vc_success_signals.md
Contains:
Research backed early stage signals
Stage differences
Fundability versus quality distinction
Evidence hierarchy
Scoring concepts
vc_review_methodology.md
Contains:
Review sequence
Strategic tension logic
Diligence process
Hard gates
Human judgment rules
category_overlays.md
Contains category specific diligence.
research_rules.md
Contains:
Source quality
Research freshness
Research planning
Fact versus inference discipline
Macro research rules
mca_output_standard.md
Contains:
External deliverable structure
MCA tone
Branding
Word density
Content restrictions
42. Skill Versus Application
The first version should primarily be a Skill or agent workflow.
The strategic intelligence belongs in:
SKILL.md
Memory files
Templates
The application interface should remain secondary.
This allows MCA to change:
Scoring
Questions
Research rules
Writing style
Category logic
Output structure
Without rebuilding the entire tool.
43. Future Application
Once the methodology is stable, the same system can later become an internal application.
Potential future interface:
New Review
Company
Deck upload
Transcript upload
Additional documents
Reviewer interview
Research approval
Generate review
Review conclusions
Export MCA deliverable
However, this should not be the immediate priority.
44. Research Access
The agent should use current external research where technically available.
When web research is available:
Prefer credible primary or authoritative sources
Capture sources
Record research date
Distinguish current information from historical information
Revalidate older stored information where necessary
When research access is unavailable:
Do not fabricate research
Complete only the internal document analysis
Mark external opportunity and threat analysis as preliminary
Tell the reviewer which areas require external validation
45. Research Memory
Useful external research may be stored for later use.
Example structure:
Topic:
Collectibles marketplaces

Finding:
Relevant research finding

Research date:
2026_08_14

Source:
Source reference

Relevant companies:
Prized

Tags:
collectibles
marketplace
custody

Confidence:
High

Needs revalidation:
Yes

Stored research should not automatically be treated as current forever.
46. Prized As Reference Case
Prized is the initial reference test.
Hash's completed Prized deliverable should be treated as the benchmark for:
Concision
Strategic thinking
Question prioritization
SWOT quality
Tone
Founder usefulness
Hash's playbook should be treated as the benchmark for internal methodology.
The completed deliverable identified core tensions including protocol versus marketplace and initial supply. It then developed strategic observations around liquidity, company identity, supply, external opportunities and threats, followed by prioritized diligence questions.
47. Testing Method
The first blind test should not give the agent Hash's completed Prized review.
Provide:
Prized deck
Call transcript if available
MCA reviewer notes
Company links
Relevant source materials
Then let the agent independently generate the review.
Afterward, compare the generated output to Hash's completed document.
48. Prized Evaluation Criteria
Score the prototype on:
Strategic Tension Identification
Did it find the issues that actually matter?
Specificity
Could the analysis apply to many unrelated companies?
If yes, it is too generic.
Depth
Did it go beyond summarizing the deck?
Research Quality
Did external research materially improve the analysis?
SWOT Quality
Are strengths and weaknesses internal?
Are opportunities and threats external?
Question Quality
Would the questions create a useful founder discussion?
Prioritization
Did the system identify the most important questions first?
Evidence Quality
Can the major claims be traced back to sources?
Human Judgment Integration
Did the agent meaningfully use MCA reviewer input?
MCA Tone
Would MCA comfortably place its name on the document?
49. Version 0.1 Definition Of Done
Version 0.1 is successful when another MCA team member can open the repository and say:
Start a new MCA review.
The system should then:
Ask for the company
Ask for the deck
Read the deck
Ask for supporting materials
Interview the reviewer
Create a research plan
Conduct research
Analyze the company
Determine stage
Apply relevant category logic
Identify central strategic tensions
Generate SWOT
Score internally
Identify evidence gaps
Generate prioritized questions
Critique its own analysis
Ask the reviewer to challenge the conclusions
Revise where required
Generate the MCA deliverable
Save the underlying research, evidence, analysis, and output
If somebody other than Jayson can complete this process without needing Jayson to explain the methodology, the prototype has achieved its first major objective.
50. Explicitly Outside Version 0.1
Do not build:
CRM integration
Client accounts
User authentication
Complex dashboards
Automatic email sending
MCA proposal generation
MCA service recommendations
MCA case study matching
Large BD preparation workflows
Automated commercial scoring
Large cloud database
Full hosted SaaS interface
Mobile application
Automated investment decisions
These may be reconsidered later.
51. Build Philosophy
Prioritize:
Intelligence quality
Transparency
Editability
Reproducibility
Human control
Strong research
Strong outputs
Ease of testing
Do not prioritize:
Fancy interface
Complex infrastructure
Premature automation
Large databases
Visual polish before methodology quality
The first version is the brain.
The application can come later.
52. Simple Mental Model
The system has 5 core jobs.
READ
Understand the company and supplied materials.
ASK
Extract MCA's human judgment.
RESEARCH
Understand what is happening outside the company.
THINK
Identify what actually matters.
WRITE
Turn the analysis into something valuable enough for MCA to place its name on.
53. What Success Looks Like
The system should eventually allow MCA to go from:
Company deck arrives
To:
MCA delivers a thoughtful strategic review
Without requiring Hash or another senior person to personally spend several hours creating every first draft.
The output should still feel like someone experienced spent meaningful time thinking about the company.
That is the product.
54. Immediate Build Assignment For The Coding Agent
Using this document as the project source of truth:
Create the initial repository structure
Create the permanent memory files
Create the first SKILL.md
Create the case folder system
Create the reviewer interview workflow
Create the research planning workflow
Create the evidence model
Create the internal analysis template
Create the MCA external deliverable template
Create the self critique workflow
Create the human review loop
Ensure methodology and prompts remain modular and editable
Do not build a large graphical application
Keep the first version runnable locally
Prepare the system for a Prized blind test
Do not materially reinterpret this methodology without flagging the proposed change first.
If implementation decisions are required, prefer the simplest architecture that preserves the behavior described in this document.
55. First Coding Agent Instruction
After adding this document to the repository, give the coding agent the following instruction:
Read PROJECT_CONTEXT.md completely before changing any files. Treat it as the source of truth for this project.
Your task is to build Version 0.1 of the MCA Strategic Review Agent described in the document.
Before writing implementation code, first return:
Your understanding of what MCA is
Your understanding of what Hash is trying to accomplish
Your understanding of the end user
Your understanding of the required inputs
Your understanding of the desired internal output
Your understanding of the desired external MCA deliverable
The workflow you plan to implement
The repository structure you recommend
Any contradictions or missing requirements you found
Any implementation decisions that need approval
Do not begin building until this context check is complete.
This prevents the coding agent from immediately making assumptions and building the wrong product.
56. Second Coding Agent Instruction
Once the context check is correct:
Proceed with the minimum local prototype.
Build the methodology as modular instructions, memory files, templates, and case folders first.
The tool should guide the user conversationally through a company review rather than requiring the user to manually understand the internal workflow.
The prototype should be easy to change because the methodology is still being refined.
Do not optimize for production deployment yet.
57. Final Principle
This project is not primarily a software project.
It is a methodology project that will eventually become software.
The methodology must work before the interface matters.
The agent should therefore preserve MCA's human judgment while making the research, analysis, structure, and drafting process substantially faster and more repeatable.
The final standard is simple:
Can MCA give the system a company, its materials, and a human opinion, then receive a review that is specific, evidence based, strategically useful, and strong enough to send under the MCA name?
If yes, the first version works.

