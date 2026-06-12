"""
TruthLens AI - Image Analyzer Model
Orchestrates the deepfake / image manipulation analysis pipeline.
"""
from PIL import Image
import io
from utils.gemini_client import analyze_image_for_deepfake
from utils.config import GEMINI_API_KEY, SUPPORTED_IMAGE_TYPES


def run_image_analysis(uploaded_file) -> dict:
    """
    Run full image deepfake analysis pipeline.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        Analysis result dict.
    """
    if uploaded_file is None:
        return {"error": "No image uploaded."}

    # Validate file type
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext not in SUPPORTED_IMAGE_TYPES:
        return {"error": f"Unsupported file type: .{ext}. Please upload JPG, PNG, or WEBP."}

    # Read image bytes
    image_bytes = uploaded_file.read()

    # Validate image can be opened
    try:
        img = Image.open(io.BytesIO(image_bytes))
        img.verify()  # check not corrupt
    except Exception:
        return {"error": "Could not open image. Please upload a valid image file."}

    # Determine MIME type
    mime_map = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}
    mime_type = mime_map.get(ext, "image/jpeg")

    if not GEMINI_API_KEY:
        return _demo_image_result()

    try:
        result = analyze_image_for_deepfake(image_bytes, mime_type)
        # Attach basic image metadata
        img2 = Image.open(io.BytesIO(image_bytes))
        result["image_size"] = f"{img2.width} × {img2.height} px"
        result["image_mode"] = img2.mode
        result["file_size"] = f"{len(image_bytes) / 1024:.1f} KB"
        return result
    except Exception as e:
        return {"error": str(e)}


def _demo_image_result() -> dict:
    return {
        "ai_generated_score": 42,
        "manipulation_score": 35,
        "authenticity_score": 68,
        "confidence": 65,
        "verdict": "POSSIBLY MANIPULATED",
        "findings": [
            "Demo mode — set GEMINI_API_KEY for live analysis",
            "Minor lighting inconsistencies around edges",
            "Compression artifacts detected in facial regions",
            "Metadata timestamp appears altered",
        ],
        "metadata_flags": [
            "EXIF GPS data stripped",
            "Editing software: Unknown",
        ],
        "explanation": (
            "DEMO MODE: In live mode, Gemini Vision AI analyzes pixel-level inconsistencies, "
            "lighting physics, facial geometry, and metadata signatures to detect deepfakes. "
            "Add your GEMINI_API_KEY to .env to enable real analysis."
        ),
        "image_size": "N/A (demo)",
        "image_mode": "RGB",
        "file_size": "N/A",
    }
