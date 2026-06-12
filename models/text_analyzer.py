"""
TruthLens AI - Text Analyzer Model
Orchestrates the full fake-news analysis pipeline.
"""
import streamlit as st
from utils.gemini_client import analyze_text_for_fake_news
from utils.config import GEMINI_API_KEY


def run_text_analysis(text: str) -> dict:
    """
    Run full text analysis pipeline.
    Falls back to demo result if no API key is set.

    Args:
        text: Input news text / tweet / article.

    Returns:
        Analysis result dict.
    """
    if not text or len(text.strip()) < 10:
        return {"error": "Text is too short. Please provide at least 10 characters."}

    if not GEMINI_API_KEY:
        # Return a demo result so the app is usable without keys
        return _demo_text_result(text)

    try:
        result = analyze_text_for_fake_news(text)
        return result
    except Exception as e:
        return {"error": str(e)}


def _demo_text_result(text: str) -> dict:
    """Return a plausible demo result when API key is missing."""
    import hashlib
    # Seed variation based on text so results feel different each time
    seed = int(hashlib.md5(text.encode()).hexdigest()[:4], 16) % 40

    fake = 55 + seed
    trust = 100 - fake
    bias = 30 + (seed % 30)
    manip = 20 + (seed % 40)

    verdict = "LIKELY FAKE" if fake > 70 else ("UNCERTAIN" if fake > 45 else "LIKELY REAL")

    return {
        "fake_score": fake,
        "trust_score": trust,
        "bias_score": bias,
        "manipulation_score": manip,
        "verdict": verdict,
        "confidence": 72,
        "explanation": (
            "Demo mode — set GEMINI_API_KEY for live analysis. "
            "This sample shows how TruthLens displays results. "
            "The text shows patterns consistent with biased framing and lacks verifiable citations."
        ),
        "red_flags": [
            "Emotionally charged language detected",
            "No credible sources mentioned",
            "Absolute claims without evidence",
        ],
        "fact_check_summary": "DEMO: In live mode, Gemini AI cross-references the claims and provides a detailed fact-check summary here.",
        "bias_direction": "CENTER-RIGHT",
    }
