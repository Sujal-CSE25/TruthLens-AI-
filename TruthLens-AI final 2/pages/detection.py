"""TruthLens AI — Detection Page (Fake News + Deepfake tabs)."""
import streamlit as st
from PIL import Image
import io

from components.widgets import (
    render_verdict, score_bar, score_row,
    render_flags, render_findings, render_meta_flags,
    ai_explanation, info_banner, section_header,
)
from components.charts import (
    make_gauge_chart, make_radar_chart, make_bar_chart,
)
from components.footer import render_footer
from models.text_analyzer import run_text_analysis
from models.image_analyzer import run_image_analysis
from utils.config import GEMINI_API_KEY


def render_detection():
    st.markdown(
        """
        <div style="padding:36px 0 24px;text-align:center">
          <div class="section-label">AI Detection Suite</div>
          <div class="section-title">Analyze <span class="grad-text">Any Content</span></div>
          <div class="section-subtitle" style="margin-bottom:0">
            Choose Fake News or Deepfake detection below and get results in seconds.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not GEMINI_API_KEY:
        st.warning(
            "**Demo Mode** — No GEMINI_API_KEY found. "
            "Add it to your `.env` file to unlock real AI analysis. "
            "Results shown are illustrative.",
            icon="⚠️",
        )

    tab1, tab2 = st.tabs(["  Fake News Detection  ", "  Deepfake Detection  "])

    with tab1:
        _fake_news_tab()

    with tab2:
        _deepfake_tab()


# ─── FAKE NEWS TAB ────────────────────────────────────────────
def _fake_news_tab():
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # Sample selector
    samples = {
        "Select a sample…": "",
        "Credible report":
            "NASA confirms the James Webb Space Telescope has captured its first direct image of "
            "an exoplanet, marking a historic milestone according to the agency's official press release.",
        "Suspicious claim":
            "BREAKING: Scientists CONFIRM drinking bleach cures cancer — Big Pharma is hiding this!! "
            "Share before they DELETE this!!!",
        "Political tweet":
            "The economy has NEVER been worse in the history of the country. Unemployment at record "
            "highs, crime out of control. Vote for change before it is too late!",
    }

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    selected = st.selectbox("Quick sample (optional)", list(samples.keys()), key="sample_sel")
    user_text = st.text_area(
        "Paste text here",
        value=samples[selected],
        height=160,
        placeholder="Paste a news headline, article, or social media post…",
        key="fn_text",
    )
    col_btn, _ = st.columns([1, 4])
    with col_btn:
        analyze = st.button("Analyze Text", key="analyze_text", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if analyze and user_text.strip():
        with st.spinner("Analyzing content..."):
            result = run_text_analysis(user_text)
            st.session_state.text_result = result
            if "error" not in result:
                hist = st.session_state.setdefault("analysis_history", [])
                hist.append({
                    "label": f"#{len(hist)+1}",
                    "fake_score": result.get("fake_score", 0),
                    "verdict": result.get("verdict", ""),
                    "type": "text",
                })

    result = st.session_state.get("text_result")
    if not result:
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        info_banner(
            "How to use",
            "Paste a headline, tweet, or full article above and click Analyze Text. "
            "TruthLens will return a fake score, bias rating, manipulation indicators, and a full AI explanation.",
            "&#128161;",
        )
        render_footer()
        return

    if "error" in result:
        st.error(result["error"])
        render_footer()
        return

    st.markdown("<hr class='section-divider' style='margin:28px 0'>", unsafe_allow_html=True)

    # Verdict
    render_verdict(result.get("verdict", "UNCERTAIN"))
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # Score row
    score_row(result)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # Bars + Radar
    col_l, col_r = st.columns([1, 1])
    with col_l:
        section_header("Score Breakdown", "")
        score_bar("Fake Probability",   result.get("fake_score", 0),        "How likely the content is fabricated")
        score_bar("Trust Score",        result.get("trust_score", 0),       "Overall content credibility")
        score_bar("Bias Score",         result.get("bias_score", 0),        "Editorial or political bias")
        score_bar("Manipulation Score", result.get("manipulation_score", 0),"Manipulative language detected")
        bias_dir = result.get("bias_direction", "UNKNOWN")
        st.markdown(
            f"<div style='margin-top:10px;padding:10px 16px;background:var(--card);border-radius:8px;"
            f"font-size:0.84rem;border:1px solid var(--border-s)'>"
            f"<span style='color:var(--tx-m)'>Bias Direction:</span> "
            f"<strong style='color:var(--p-light)'>{bias_dir}</strong></div>",
            unsafe_allow_html=True,
        )

    with col_r:
        radar = {
            "Fake":         result.get("fake_score", 0),
            "Bias":         result.get("bias_score", 0),
            "Manipulation": result.get("manipulation_score", 0),
            "Distrust":     100 - result.get("trust_score", 0),
            "Confidence":   result.get("confidence", 0),
        }
        st.plotly_chart(make_radar_chart(radar), use_container_width=True)

    # AI explanation
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
    ai_explanation(result.get("explanation", ""))

    # Red flags
    render_flags(result.get("red_flags", []))

    # Fact check
    fcs = result.get("fact_check_summary", "")
    if fcs:
        section_header("Fact-Check Summary", "")
        st.markdown(
            f"<div class='glass-card' style='border-color:rgba(0,229,160,0.2);font-size:0.9rem;line-height:1.7;color:var(--tx-m)'>{fcs}</div>",
            unsafe_allow_html=True,
        )

    # Gauges
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1:
        st.plotly_chart(make_gauge_chart(result.get("confidence", 0),  "AI Confidence", "#7C4DFF"), use_container_width=True)
    with g2:
        st.plotly_chart(make_gauge_chart(result.get("fake_score", 0),  "Fake Score",    "#FF4560"), use_container_width=True)

    render_footer()


# ─── DEEPFAKE TAB ─────────────────────────────────────────────
def _deepfake_tab():
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    uploaded = st.file_uploader(
        "Upload an image for deepfake analysis",
        type=["jpg", "jpeg", "png", "webp"],
        key="df_upload",
        help="Supports JPG, PNG, WEBP up to 10 MB",
    )
    col_btn, _ = st.columns([1, 4])
    with col_btn:
        analyze = st.button("Analyze Image", key="analyze_img", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if analyze and uploaded:
        with st.spinner("Running image analysis..."):
            result = run_image_analysis(uploaded)
            st.session_state.image_result = result
            if "error" not in result:
                hist = st.session_state.setdefault("analysis_history", [])
                hist.append({
                    "label": f"#{len(hist)+1}",
                    "fake_score": result.get("ai_generated_score", 0),
                    "verdict": result.get("verdict", ""),
                    "type": "image",
                })

    result = st.session_state.get("image_result")
    if not result:
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        info_banner(
            "How to use",
            "Upload any image — photo, screenshot, portrait, news image — and click Analyze Image. "
            "TruthLens will check for AI generation, pixel manipulation, and metadata anomalies.",
            "&#128161;",
        )
        render_footer()
        return

    if "error" in result:
        st.error(result["error"])
        render_footer()
        return

    st.markdown("<hr class='section-divider' style='margin:28px 0'>", unsafe_allow_html=True)

    render_verdict(result.get("verdict", "POSSIBLY MANIPULATED"))
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    col_l, col_r = st.columns([1, 1])
    with col_l:
        # Re-open image for display
        if uploaded:
            try:
                uploaded.seek(0)
                img = Image.open(uploaded)
                st.image(img, caption="Uploaded Image", use_container_width=True)
            except Exception:
                pass

        # Metadata
        st.markdown(
            f"""
            <div class="glass-card" style="margin-top:12px;font-size:0.84rem;line-height:2">
              <div style="font-size:0.72rem;font-weight:700;text-transform:uppercase;
                          letter-spacing:0.09em;color:var(--tx-m);margin-bottom:8px">Image Metadata</div>
              <div><span style="color:var(--tx-d)">Dimensions:</span>
                   <strong style="color:var(--tx)">{result.get('image_size','N/A')}</strong></div>
              <div><span style="color:var(--tx-d)">Color Mode:</span>
                   <strong style="color:var(--tx)">{result.get('image_mode','N/A')}</strong></div>
              <div><span style="color:var(--tx-d)">File Size:</span>
                   <strong style="color:var(--tx)">{result.get('file_size','N/A')}</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_r:
        section_header("Authenticity Scores", "")
        score_bar("AI Generated Score", result.get("ai_generated_score", 0), "Probability of AI generation")
        score_bar("Manipulation Score", result.get("manipulation_score", 0), "Signs of pixel-level tampering")
        score_bar("Authenticity Score", result.get("authenticity_score", 0), "Indicators of authentic origin")
        score_bar("AI Confidence",      result.get("confidence", 0),         "Confidence in this analysis")

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        g1, g2 = st.columns(2)
        with g1:
            st.plotly_chart(make_gauge_chart(result.get("ai_generated_score", 0), "AI Generated", "#8B5CF6"), use_container_width=True)
        with g2:
            st.plotly_chart(make_gauge_chart(result.get("manipulation_score", 0), "Manipulation", "#FF4560"), use_container_width=True)

    ai_explanation(result.get("explanation", ""))
    render_findings(result.get("findings", []))
    render_meta_flags(result.get("metadata_flags", []))

    render_footer()
