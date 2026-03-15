"""
agent/sales_agent.py
--------------------
The core reasoning engine for the AI sales agent.

The agent works in three sequential steps, each making its own call to
Gemini.  The output of each step is passed as input to the next, so the
reasoning builds progressively rather than being crammed into one giant prompt.

  Step 1 – Analyze context     : understand the company type and persona role.
  Step 2 – Identify pain points: derive 2-3 grounded problems from step 1.
  Step 3 – Generate outreach   : write a cold email anchored in those pains.

Authentication — two modes supported:
  Option A (Gemini API key): pass api_key="your_key"
    → Easiest to set up. Get a free key at aistudio.google.com/app/apikey.
  Option B (Vertex AI service account): pass project_id="your-gcp-project"
    → Requires GOOGLE_APPLICATION_CREDENTIALS env var pointing to a service account JSON.
"""

import textwrap
from google import genai


class SalesAgent:
    """
    Encapsulates the three-step sales reasoning workflow.

    Supports two authentication modes — whichever is available in the environment:
      - Direct Gemini API key  (simplest, free tier available)
      - Vertex AI service account (GCP-based, no quota limits on paid projects)

    Usage (API key mode):
        agent = SalesAgent(api_key="your_key")
        agent.run(company="Stripe", persona="Head of Payments", product="AI fraud detection")

    Usage (Vertex AI mode):
        agent = SalesAgent(project_id="my-gcp-project")
        agent.run(company="Stripe", persona="Head of Payments", product="AI fraud detection")
    """

    def __init__(
        self,
        api_key: str = None,
        project_id: str = None,
        location: str = "us-central1",
        model_name: str = "gemini-2.0-flash",
    ):
        """
        Configure the Gemini client in whichever auth mode is available.

        Exactly one of api_key or project_id must be provided. run_agent.py
        checks the environment and passes the right one automatically.

        Args:
            api_key    : Gemini API key from aistudio.google.com (Option A).
            project_id : GCP project ID for Vertex AI (Option B).
            location   : Vertex AI region — only used in Option B.
            model_name : Which Gemini model to call. gemini-2.0-flash is the
                         default — works on both direct API key and Vertex AI paths.
        """
        if api_key:
            # Option A — direct Gemini API. Simple, no GCP setup needed.
            self.client = genai.Client(api_key=api_key)
        elif project_id:
            # Option B — Vertex AI. Uses GOOGLE_APPLICATION_CREDENTIALS from env.
            # The service account JSON is loaded automatically by google-auth.
            self.client = genai.Client(
                vertexai=True,
                project=project_id,
                location=location,
            )
        else:
            raise ValueError(
                "SalesAgent requires either api_key (Gemini) or project_id (Vertex AI). "
                "Set GEMINI_API_KEY or GOOGLE_CLOUD_PROJECT in your .env file."
            )

        self.model_name = model_name

    # ─────────────────────────────────────────────────────────────────
    # Private helper
    # ─────────────────────────────────────────────────────────────────

    def _call_gemini(self, prompt: str) -> str:
        """
        Send a single prompt to Gemini and return the plain-text response.

        Keeping this as a thin wrapper means every step goes through the
        same path, and we can swap the model or backend later without
        touching any of the step methods.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text.strip()

    # ─────────────────────────────────────────────────────────────────
    # Step 1 — Context Analysis
    # ─────────────────────────────────────────────────────────────────

    def step1_analyze_context(self, company: str, persona: str, product: str) -> str:
        """
        Ask Gemini to reason about the business environment before we do
        anything sales-related.

        This step deliberately avoids mentioning our product in the output.
        The goal is to build a factual picture of:
          - What type of business the company is and what pressures it faces.
          - What the target persona owns, cares about, and is measured on.
          - Where a product in our category typically sits in that world.

        By doing this first, Steps 2 and 3 are grounded in real context
        rather than generic assumptions.

        Returns:
            A short paragraph (4–6 sentences) of context analysis.
        """
        prompt = f"""
You are a senior B2B sales strategist preparing an outreach campaign.

Your job right now is purely to understand the prospect — not to pitch anything.

Prospect details:
  Company       : {company}
  Target Persona: {persona}
  Product we sell (for context only): {product}

Write a short analysis of 4–6 sentences covering:
1. What kind of business {company} typically is, its scale, and the pressures it usually operates under.
2. What the {persona} role typically owns, cares about day-to-day, and is measured on.
3. Where a product category like "{product}" generally fits into the challenges this persona faces.

Rules:
- Be factual and grounded. If {company} is a well-known company, use only broad, reasonable public knowledge.
- Do NOT invent specific metrics, revenue figures, or internal details.
- Do NOT mention our product by name or pitch anything — this step is purely analytical.
- Write in plain prose, no bullet points or headers.
        """.strip()

        return self._call_gemini(prompt)

    # ─────────────────────────────────────────────────────────────────
    # Step 2 — Pain Point Identification
    # ─────────────────────────────────────────────────────────────────

    def step2_identify_pain_points(
        self, company: str, persona: str, product: str, context_analysis: str
    ) -> list[str]:
        """
        Using the context from Step 1 as grounding, ask Gemini to surface
        the 2–3 specific pain points this persona most likely experiences
        that our product is positioned to address.

        Passing `context_analysis` into this prompt is what makes this
        genuinely multi-step: Gemini isn't starting from scratch, it's
        reasoning on top of the analysis it just produced.

        Returns:
            A list of 2–3 plain-English pain point strings.
        """
        prompt = f"""
You are a B2B sales strategist. You've already analyzed this prospect:

--- Context from Step 1 ---
{context_analysis}
--- End Context ---

Now go one level deeper.

Prospect details:
  Company       : {company}
  Target Persona: {persona}
  Product we sell: {product}

Based on the context above, identify exactly 2–3 specific pain points this
{persona} at a company like {company} is most likely experiencing — pain
points that "{product}" is directly positioned to address.

Rules:
- Each pain point must describe a concrete, recognizable problem — not a vague category.
- Do NOT name or describe our product in the pain points. Describe the pain only.
- Do NOT invent statistics or specific internal details.
- Write each pain point as a single, clear sentence.
- Format: one pain point per line, each line starting with a dash (-).
- Output only the pain points. No intro text, no headers, no commentary.
        """.strip()

        raw = self._call_gemini(prompt)

        # Parse lines that start with "-" into a clean Python list.
        # This makes the list easy to iterate over in Step 3 and in the output.
        pain_points = [
            line.lstrip("- ").strip()
            for line in raw.splitlines()
            if line.strip().startswith("-")
        ]

        # Fallback: if the model ignored the "-" format, split by newline
        if not pain_points:
            pain_points = [line.strip() for line in raw.splitlines() if line.strip()]

        # Cap at 3 to stay within the brief's requirement
        return pain_points[:3]

    # ─────────────────────────────────────────────────────────────────
    # Step 3 — Outreach Generation
    # ─────────────────────────────────────────────────────────────────

    def step3_generate_outreach(
        self, company: str, persona: str, product: str, pain_points: list[str]
    ) -> str:
        """
        Generate the final personalized cold outreach email.

        The pain points from Step 2 are injected directly into this prompt so
        the message is always anchored to real, grounded pains — never a
        generic pitch.

        The prompt is written from the perspective of a veteran enterprise
        sales operator: every sentence must earn its place, every word must
        move the prospect closer to replying. The structure follows the
        pattern that top-performing reps use consistently:
          Hook (company-specific observation) →
          Stakes (cost of doing nothing) →
          Social proof (peer pattern) →
          Bridge (single outcome sentence) →
          CTA (confident, low-friction, specific)

        Returns:
            The cold email as a string (Subject line + body).
        """
        # Format the pain points as a numbered list for the prompt
        pain_points_block = "\n".join(f"  {i}. {p}" for i, p in enumerate(pain_points, 1))

        prompt = f"""
You are one of the highest-performing enterprise sales professionals alive.
You have 30 years of B2B sales experience, have closed over $2B in deals,
and you personally mentor the top 1% of sales reps at Fortune 500 companies.
You think in buyer psychology, not vendor language.

You are writing a cold outreach email for the following prospect.
This email must be so good that a busy senior executive stops scrolling and replies.

━━━ PROSPECT CONTEXT ━━━
Company        : {company}
Target Persona : {persona}
Product we sell: {product}

Confirmed pain points (derived from deep research into this persona):
{pain_points_block}

━━━ EMAIL STRUCTURE — follow this exactly ━━━

1. SUBJECT LINE
   - 4–7 words maximum. No fluff. No yes/no questions.
   - Format options (pick the sharpest one):
     • Name the exact pain: "fraud false positives at {company}?"
     • Peer pattern: "how [peer company type] cut manual fraud review"
     • Provocative observation: "[specific cost] of your current fraud ops"
   - Never mention the product name. Never use generic words like "solution" or "platform".
   - The goal: make them think "how do they know that about us?"

2. OPENING LINE — the hook (1 sentence)
   - Open with a bold, specific observation about {company} or this type of company.
   - Reference the most acute pain point. State it as a fact, not a guess.
   - Pattern: "[Company/companies like X] [specific situation] — and [specific consequence]."
   - NEVER start with: I, We, Our, Hope, Just, Quick, Reaching out, Touching base.
   - Do NOT use: "must", "likely", "probably", "might", "perhaps", "I believe" — no hedging.

3. STAKES PARAGRAPH (2 sentences max)
   - Make the cost of inaction vivid and visceral. What breaks if they do nothing?
   - Use the persona's language — revenue, chargeback ratio, team burn, declined customers,
     compliance exposure, competitive risk. NOT "efficiency" or "operational overhead."
   - One sentence for the immediate pain. One for the downstream consequence.

4. SOCIAL PROOF BRIDGE (1–2 sentences)
   - Reference a peer pattern: "Other [persona titles] we work with tell us..." or
     "Teams at companies like [industry peer] found that..."
   - ZERO invented metrics. No percentages, no dollar figures, no timeframes unless
     you are 100% certain they are accurate. If unsure — describe the outcome in
     qualitative terms only: "freed up", "stopped manually", "no longer fighting".
   - Then: ONE sentence on what changes after using {product} — describe the outcome
     (what life looks like after), NOT the features.

5. CTA — the close (1 sentence)
   - Confident, direct, specific. Not passive.
   - Pick ONE of these patterns:
     • Time-specific: "15 minutes this week — worth it?"
     • Permission ask: "Would it make sense to show you how we approach this?"
     • Curiosity hook: "Happy to share what we're seeing work — want me to send it over?"
   - Do NOT use: "Curious if this resonates", "Does this sound familiar", "Hope to hear from you"

━━━ ABSOLUTE RULES ━━━
✗ Never: "I'm reaching out", "Hope this finds you", "touching base", "quick question",
         "just wanted to", "synergy", "innovative solution", "end-to-end", "leverage" (verb)
✗ Never: Start a sentence with "I" in the first two lines
✗ Never: Feature dump — ONE outcome only, in the buyer's language
✗ Never: Hedge — no "might", "could potentially", "perhaps", "I believe"
✗ Never: Invent ANY number — no percentages, no dollar amounts, no timeframes.
         If you cannot cite a real source, describe outcomes qualitatively only.
✓ Always: Use "Hi [Name]," as the greeting
✓ Always: Write every sentence as if the prospect will ask "so what does that mean for me?"
✓ Always: Sound like a peer who deeply understands their world, not a vendor pitching

━━━ LENGTH ━━━
Under 130 words total (subject excluded). Every sentence must earn its place.
If a sentence doesn't move the prospect closer to replying — cut it.

Output ONLY the email. Subject line first, then a blank line, then the body.
No preamble, no commentary, no explanation after the email.
        """.strip()

        return self._call_gemini(prompt)

    # ─────────────────────────────────────────────────────────────────
    # Orchestrator — runs all three steps in sequence
    # ─────────────────────────────────────────────────────────────────

    def run(self, company: str, persona: str, product: str) -> None:
        """
        Run the full three-step reasoning chain and print each result to
        the terminal as it arrives.

        Each step's output feeds directly into the next, so the final
        outreach is always grounded in the analysis produced in Steps 1 and 2.

        Args:
            company : The target company name.
            persona : The target job title or role.
            product : A short description of the product being sold.
        """
        divider = "─" * 56

        # ── Header ────────────────────────────────────────────────
        print(f"\n{'═' * 56}")
        print("  AI Sales Agent")
        print(f"{'═' * 56}")
        print(f"  Company  : {company}")
        print(f"  Persona  : {persona}")
        print(f"  Product  : {product}")
        print(f"{'═' * 56}\n")

        # ── Step 1: Context Analysis ───────────────────────────────
        print(divider)
        print("  Step 1 · Analysing company & persona context...")
        print(divider)
        context_analysis = self.step1_analyze_context(company, persona, product)
        # Wrap text at 70 chars so it reads cleanly in any terminal width
        print(textwrap.fill(
            context_analysis,
            width=70,
            initial_indent="  ",
            subsequent_indent="  "
        ))
        print()

        # ── Step 2: Pain Points ────────────────────────────────────
        print(divider)
        print("  Step 2 · Identifying likely pain points...")
        print(divider)
        pain_points = self.step2_identify_pain_points(
            company, persona, product, context_analysis
        )
        for i, pain in enumerate(pain_points, 1):
            # Indent continuation lines so multi-line pains stay readable
            print(textwrap.fill(
                f"  {i}. {pain}",
                width=70,
                subsequent_indent="     "
            ))
        print()

        # ── Step 3: Cold Outreach ──────────────────────────────────
        print(divider)
        print("  Step 3 · Generating personalised outreach message...")
        print(divider)
        outreach = self.step3_generate_outreach(company, persona, product, pain_points)
        # Print each line of the email with a small indent for readability
        for line in outreach.splitlines():
            print(f"  {line}")

        print(f"\n{'═' * 56}\n")
