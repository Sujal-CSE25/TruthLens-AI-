"""
TruthLens AI - Helper Utilities
Reusable helper functions for scoring, labels, and colors.
"""
from utils.config import THRESHOLD_HIGH_RISK, THRESHOLD_MEDIUM_RISK


def get_risk_label(score: int) -> str:
    """Convert a numeric score (0-100) to a human-readable risk label."""
    if score >= THRESHOLD_HIGH_RISK:
        return "HIGH RISK"
    elif score >= THRESHOLD_MEDIUM_RISK:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def get_risk_color(score: int) -> str:
    """Return a hex color based on risk score."""
    if score >= THRESHOLD_HIGH_RISK:
        return "#FF4B4B"   # red
    elif score >= THRESHOLD_MEDIUM_RISK:
        return "#FFA500"   # orange
    else:
        return "#00D26A"   # green


def get_verdict_emoji(verdict: str) -> str:
    """Map a verdict string to an emoji."""
    mapping = {
        "LIKELY REAL": "✅",
        "UNCERTAIN": "⚠️",
        "LIKELY FAKE": "❌",
        "SATIRE": "🎭",
        "LIKELY AUTHENTIC": "✅",
        "POSSIBLY MANIPULATED": "⚠️",
        "LIKELY AI-GENERATED": "🤖",
        "DEEPFAKE SUSPECTED": "❌",
    }
    return mapping.get(verdict, "❓")


def score_to_bar_color(score: int) -> str:
    """Gradient-style bar color for Streamlit progress."""
    if score >= THRESHOLD_HIGH_RISK:
        return "#FF4B4B"
    elif score >= THRESHOLD_MEDIUM_RISK:
        return "#FFA500"
    return "#00D26A"


def truncate_text(text: str, max_chars: int = 500) -> str:
    """Truncate text for display with ellipsis."""
    return text[:max_chars] + "..." if len(text) > max_chars else text


def image_bytes_to_base64(image_bytes: bytes) -> str:
    """Convert image bytes to base64 string for embedding."""
    import base64
    return base64.b64encode(image_bytes).decode("utf-8")
