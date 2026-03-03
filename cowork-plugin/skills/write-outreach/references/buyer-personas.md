# Buyer Personas — B2B Tech Seller Reference

**How to use this file:**
1. Identify which type your contact is (ITDM / Architect / Practitioner)
2. Read their card — what they care about, what pain to probe, likely hurdle
3. Map to one value driver before writing or calling

---

## THE 3 BUYER TYPES

All B2B tech buyers fall into one of three types. Know which one you're talking to FIRST.

| Type | Who | What Drives Them |
|------|-----|-----------------|
| **IT Decision Makers (ITDMs)** | CTO, CIO, VP Engineering, VP IT Ops, Head of Database, Head of DevOps, Head of Security, Head of Architecture, Head of Procurement | Business outcomes, risk, cost, strategic alignment |
| **Architects** | Enterprise Architect, Chief Architect, Head of Architecture, Solutions Architect | Platform standards, technical debt, modernization, workload portability |
| **Practitioners** | Software Engineers, DBAs, Data Engineers, AI/ML Engineers | Developer experience, performance, ops simplicity, day-to-day tools |

**For each persona, know 3 things:**
1. What they care about (top 2-3 goals / what they're measured on)
2. Strategic opening (the #1 pain your product is positioned to solve for them)
3. The likely hurdle (most common objection + how to handle it)

---

## PERSONA CARDS

---

### CTO

**What they care about:**
- Innovation velocity — can the tech stack keep up with the product roadmap?
- Engineering productivity — are teams shipping or managing infrastructure?
- AI/ML readiness — is the data and tooling foundation ready for AI?

**Pain to probe:**
- "When a new product requirement comes in, how long does it take from decision to shipping?"
- "What percentage of your engineering time goes to infrastructure vs. product features?"

**Likely hurdle:** "We're already on [current system]."
→ "The question is whether that system handles [their AI/scale use case] without adding operational overhead. What does that look like today?"

**Lead with:** Peer company outcomes. Innovation velocity evidence. AI readiness angle.
**Do NOT lead with:** Feature lists. ROI spreadsheets. Technical comparisons.

---

### CIO

**What they care about:**
- Total cost of ownership across the entire tech stack
- Vendor rationalization — fewer tools, fewer contracts, fewer risks
- Security and compliance posture across all systems
- Enabling the business without being the bottleneck

**Pain to probe:**
- "How many different [relevant tool category] vendors are you paying today?"
- "Who owns the security compliance review for each of those?"

**Likely hurdle:** "Not a budget priority right now."
→ "Understood. Is that because the current setup hasn't caused an incident yet? What would a gap across one of those systems cost you?"

**Lead with:** Cost consolidation, vendor risk reduction, peer CIO outcomes.
**Do NOT lead with:** Technical specs. Developer-focused benefits.

---

### VP / Director of Engineering

**What they care about:**
- Developer velocity — how fast can teams ship?
- On-call burden — how much does infrastructure wake people up at night?
- Recruiting/retention — are engineers excited or frustrated by the stack?
- Scaling without re-architecting everything

**Pain to probe:**
- "When you need to add a new data type or workload, how long does it take to provision?"
- "What's your on-call story for [relevant system] incidents?"
- "Are your AI engineers blocked waiting on a different team or system?"

**Likely hurdle:** "We have [current system] and it works fine."
→ "It works for [current use case]. How is it handling [adjacent use case]? That's usually where teams start adding a second system, and then a third."

**Lead with:** Dev velocity stories. On-call reduction. Stack consolidation angle.
**Do NOT lead with:** Feature details. Pricing.

---

### Enterprise Architect / Head of Architecture

**What they care about:**
- Platform standards — consistency across the enterprise
- Workload portability — can we move this to any cloud?
- Long-term technical debt — are we building on a foundation that lasts?
- Governance, security, and compliance baked into the platform

**Pain to probe:**
- "If your current data infrastructure stays unchanged for a year, what becomes more complex or riskier?"
- "How much 'tool sprawl' happens because the provisioning process is too slow for dev teams?"
- "If you could simplify one part of your tech stack, where would you start?"

**Likely hurdle:** "We've standardized on [existing platform]."
→ "Standardization on one system usually creates pressure when new workloads (search, AI, time-series) need to be added. Is that creating any friction today?"

**Use messaging architecture (3-part):**
1. **Insight:** "Most companies in your position struggle with fragmented data infrastructure that slows teams and inflates operational overhead."
2. **Counter-intuitive truth:** "The standard fix is to add specialized tools for each workload. But each one adds sync pipelines, security gaps, and vendor contracts."
3. **Value prop:** "Your product consolidates that — one platform, lower TCO, no schema migrations."

---

### Head of Database / DBA

**What they care about:**
- Operational simplicity — fewer late-night incidents
- Managed service eliminating manual ops (patching, backups, failover)
- Migration risk — "don't break what works"
- Security compliance coverage

**Pain to probe:**
- "How many hours per week goes to operational tasks vs. query optimization and architecture work?"
- "What's the recovery process if [their primary system] has a failover?"

**Likely hurdle:** "We have DBAs who know the current system."
→ "That expertise stays valuable — managed service just removes the 3am alerts and gives your team time for higher-value work."

**Lead with:** Ops simplicity. Managed service value. Migration path (not migration risk).

---

### AI / ML Engineer

**What they care about:**
- Eliminating data sync overhead between operational data and AI pipelines
- Fast iteration — no DevOps bottlenecks on the AI stack
- Production-ready AI infrastructure that scales without re-architecting
- Keeping the embedding/vector layer close to the operational data

**Pain to probe:**
- "How are you managing the sync between your operational data and your AI/vector layer?"
- "When you embed new data, how long before it's queryable in production?"
- "Who owns the bill for the separate AI data infrastructure?"

**Lead with:** Data colocation. Elimination of sync pipelines. AI-native architecture stories.
**Do NOT lead with:** Traditional database benefits. Business ROI language.

---

## QUICK TARGETING TABLE

| Play | Primary Target | Secondary Target | Opening hook |
|------|---------------|-----------------|--------------|
| Cost consolidation | CIO, VP IT Ops | Head of Architecture | Vendor sprawl → hidden TCO |
| Dev velocity / AI build | VP Engineering, AI/ML Engineer | CTO | Stack fragmentation → slow iteration |
| Ops simplicity | Head of Database | VP IT Ops | Manual ops → team burn |
| Platform standardization | Head of Architecture | CTO | Tech debt → portability risk |
| Tool replacement | VP Engineering, Head of DB | CTO | Specific tool pain → consolidation |

---

## OUTREACH LENGTH RULES BY PERSONA

| Persona | LinkedIn Connection | Email | InMail |
|---------|--------------------|----|--------|
| CxO / CIO / CTO | ≤200 chars — exec-brief | ≤200 words — lead with business outcome | ≤300 words |
| VP Engineering / Director | ≤250 chars | ≤250 words — lead with team impact | ≤400 words |
| Architect / Tech Lead | ≤300 chars | ≤300 words — lead with technical problem | ≤400 words |
| DBA / Data Engineer | ≤300 chars | ≤300 words — lead with ops pain | ≤400 words |
| AI / ML Engineer | ≤300 chars | ≤300 words — lead with specific technical problem | ≤400 words |
