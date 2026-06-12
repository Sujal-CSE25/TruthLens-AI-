"""
TruthLens AI - Configuration
Loads API keys and app settings from environment variables.
"""
import os
from dotenv import load_dotenv

# Load .env file if it exists (for local development)
load_dotenv()

# ─── API Keys ────────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# ─── App Settings ────────────────────────────────────────────
APP_NAME = "TruthLens AI"
APP_VERSION = "1.0.0"
APP_TAGLINE = "AI-Powered Fake News & Deepfake Detection"

# Gemini model to use
GEMINI_MODEL = "gemini-2.5-flash"

# Score thresholds for labeling risk levels
THRESHOLD_HIGH_RISK = 70    # above this → HIGH RISK / FAKE
THRESHOLD_MEDIUM_RISK = 40  # above this → MEDIUM RISK

# Supported image formats for deepfake detection
SUPPORTED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp"]
