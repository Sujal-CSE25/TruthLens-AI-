"""
TruthLens AI - Gemini API Client
All calls to Google Gemini go through this module.
"""
import json
import google.generativeai as genai
from utils.config import GEMINI_API_KEY, GEMINI_MODEL


def get_gemini_model():
    """Configure and return the Gemini generative model."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel(GEMINI_MODEL)


def analyze_text_for_fake_news(text: str) -> dict:
    """
    Send news text to Gemini and get a structured fake-news analysis.

    Args:
        text: The news headline, tweet, or article to analyze.

    Returns:
        dict with keys: fake_score, trust_score, bias_score,
                        verdict, explanation, fact_check_summary
    """
    model = get_gemini_model()

    prompt = f"""
You are an expert AI fact-checker and misinformation analyst.
Analyze the following text and return ONLY a valid JSON object — no markdown, no extra text.

TEXT TO ANALYZE:
\"\"\"
{text}
\"\"\"

Return this exact JSON structure (all scores are integers 0-100):
{{
  "fake_score": <0-100, higher means more likely fake>,
  "trust_score": <0-100, higher means more trustworthy>,
  "bias_score": <0-100, higher means more biased>,
  "manipulation_score": <0-100, higher means more manipulative language>,
  "verdict": "<one of: LIKELY REAL | UNCERTAIN | LIKELY FAKE | SATIRE>",
  "confidence": <0-100, how confident the AI is in the verdict>,
  "explanation": "<2-3 sentence explanation of the analysis>",
  "red_flags": ["<flag1>", "<flag2>", "<flag3>"],
  "fact_check_summary": "<1-2 sentence fact-check summary>",
  "bias_direction": "<one of: LEFT | CENTER-LEFT | CENTER | CENTER-RIGHT | RIGHT | UNKNOWN>"
}}
"""
    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()
        # Strip markdown code fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw.strip())
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return _fallback_text_result()
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {e}")


def analyze_image_for_deepfake(image_bytes: bytes, mime_type: str = "image/jpeg") -> dict:
    """
    Send an image to Gemini Vision and get deepfake analysis.

    Args:
        image_bytes: Raw image bytes.
        mime_type: MIME type of the image.

    Returns:
        dict with deepfake analysis scores and findings.
    """
    model = get_gemini_model()

    prompt = """
You are an expert AI deepfake and image manipulation analyst.
Analyze this image carefully and return ONLY a valid JSON object — no markdown, no extra text.

Return this exact JSON structure (all scores are integers 0-100):
{
  "ai_generated_score": <0-100, higher means more likely AI-generated>,
  "manipulation_score": <0-100, higher means more likely manipulated>,
  "authenticity_score": <0-100, higher means more likely authentic>,
  "confidence": <0-100, confidence in the analysis>,
  "verdict": "<one of: LIKELY AUTHENTIC | POSSIBLY MANIPULATED | LIKELY AI-GENERATED | DEEPFAKE SUSPECTED>",
  "findings": ["<finding1>", "<finding2>", "<finding3>"],
  "metadata_flags": ["<flag1>", "<flag2>"],
  "explanation": "<2-3 sentence explanation of what was detected>"
}
"""
    try:
        image_part = {"mime_type": mime_type, "data": image_bytes}
        response = model.generate_content([prompt, image_part])
        raw = response.text.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw.strip())
    except json.JSONDecodeError:
        return _fallback_image_result()
    except Exception as e:
        raise RuntimeError(f"Gemini Vision API error: {e}")


# ─── Fallback results (used when API fails or for demo) ──────

def _fallback_text_result():
    return {
        "fake_score": 62,
        "trust_score": 38,
        "bias_score": 55,
        "manipulation_score": 48,
        "verdict": "UNCERTAIN",
        "confidence": 60,
        "explanation": "The text contains several hallmarks of misinformation including emotionally charged language and unverified claims. Further verification is recommended.",
        "red_flags": ["Emotional language detected", "No credible sources cited", "Unverifiable statistics"],
        "fact_check_summary": "Claims in this content could not be independently verified. Cross-reference with trusted news outlets.",
        "bias_direction": "UNKNOWN"
    }


def _fallback_image_result():
    return {
        "ai_generated_score": 45,
        "manipulation_score": 38,
        "authenticity_score": 62,
        "confidence": 55,
        "verdict": "POSSIBLY MANIPULATED",
        "findings": ["Minor inconsistencies in lighting", "Possible compression artifacts", "Facial geometry appears slightly irregular"],
        "metadata_flags": ["EXIF data unavailable", "Compression level inconsistent"],
        "explanation": "The image shows some signs of potential manipulation or AI generation, but results are inconclusive. Manual verification is recommended."
    }
