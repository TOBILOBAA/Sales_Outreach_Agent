"""
run_agent.py
------------
Entry point for the AI Sales Agent CLI.

Run with:
    python run_agent.py

The script asks three questions interactively, then runs the three-step
reasoning chain in agent/sales_agent.py and prints each step as it completes.

Authentication — set ONE of the following in your .env file:

  Option A (easiest): GEMINI_API_KEY=your_key
    → Get a free key at https://aistudio.google.com/app/apikey

  Option B (Vertex AI): GOOGLE_CLOUD_PROJECT=your-project-id
                        GOOGLE_APPLICATION_CREDENTIALS=service-account.json
    → Requires a GCP project with Vertex AI enabled and a service account JSON.
"""

import os
import sys

from dotenv import load_dotenv
from agent.sales_agent import SalesAgent


def prompt_input(label: str) -> str:
    """
    Display a labelled prompt and wait for the user to type a non-empty value.

    Keeps asking until something is entered — prevents the agent from running
    with blank inputs, which would produce a meaningless output.
    """
    while True:
        value = input(f"  {label}: ").strip()
        if value:
            return value
        print("  ⚠  This field cannot be empty. Please try again.\n")


def main():
    # ── Load environment variables ────────────────────────────────────
    # load_dotenv() reads .env and injects all variables into os.environ.
    # Must run before any Google SDK call so credentials are available.
    load_dotenv()

    api_key    = os.getenv("GEMINI_API_KEY")
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location   = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # ── Validate that at least one auth mode is configured ────────────
    # We prefer the Gemini API key (simpler setup) but fall back to Vertex AI.
    # If neither is found, give the user a clear, actionable error.
    if not api_key and not project_id:
        print("\n  ✗  No credentials found. Set one of the following in your .env file:")
        print()
        print("     Option A — Gemini API key (easiest):")
        print("       GEMINI_API_KEY=your_key_here")
        print("       Get a free key at: https://aistudio.google.com/app/apikey")
        print()
        print("     Option B — Vertex AI service account:")
        print("       GOOGLE_CLOUD_PROJECT=your-project-id")
        print("       GOOGLE_APPLICATION_CREDENTIALS=service-account.json")
        print()
        print("     See .env.example for reference.\n")
        sys.exit(1)

    # Vertex AI mode requires the service account file to actually exist on disk
    if project_id and not api_key:
        if not creds_path or not os.path.exists(creds_path):
            print(f"\n  ✗  Service account file not found: '{creds_path}'")
            print("     Make sure service-account.json exists in this directory and")
            print("     GOOGLE_APPLICATION_CREDENTIALS=service-account.json is in .env\n")
            sys.exit(1)

    # ── Welcome banner ────────────────────────────────────────────────
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║         AI Sales Agent — Ready           ║")
    print("  ╚══════════════════════════════════════════╝")
    print("  Answer three questions and the agent will:")
    print("    1. Analyse the company and persona")
    print("    2. Identify 2–3 likely pain points")
    print("    3. Write a personalised cold outreach message\n")
    print("  ─" * 24 + "\n")

    # ── Collect the three required inputs ─────────────────────────────
    # These are the only inputs the agent needs; everything else is
    # derived through the three reasoning steps.
    company = prompt_input("Company name   (e.g. Stripe)")
    persona = prompt_input("Target persona (e.g. Head of Payments)")
    product = prompt_input("Your product   (e.g. AI fraud detection platform)")

    print()  # breathing room before the agent output begins

    # ── Initialise and run the agent ──────────────────────────────────
    # Pass whichever auth credential is available. SalesAgent.__init__
    # handles both modes — the rest of the logic is identical either way.
    agent = SalesAgent(
        api_key=api_key or None,
        project_id=project_id or None,
        location=location,
    )
    agent.run(company=company, persona=persona, product=product)


if __name__ == "__main__":
    main()
