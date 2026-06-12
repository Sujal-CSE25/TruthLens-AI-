"""TruthLens AI — Analytics Dashboard."""
import streamlit as st
from components.charts import (
    make_gauge_chart, make_radar_chart, make_bar_chart, make_history_line_chart,
)
from components.widgets import section_header, info_banner
from components.footer import render_footer
from utils.helpers import get_risk_color


def render_analytics():
    st.markdown(
        """
        <div style="padding:36px 0 24px;text-align:center">
          <div class="section-label">Insights</div>
          <div class="section-title">Analytics <span class="grad-text">Dashboard</span></div>
          <div class="section-subtitle" style="margin-bottom:0">
            Visual intelligence from every analysis run in your session.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    text_result  = st.session_state.get("text_result")
    image_result = st.session_state.get("image_result")
    history      = st.session_state.get("analysis_history", [])

    if not text_result and not image_result:
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        info_banner(
            "No data yet",
            "Run a Fake News or Deepfake analysis first, then return here to see "
            "your analytics, charts, and session statistics.",
            "&#128202;",
        )
        render_footer()
        return

    # ── KPI row ──────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    total    = len(history)
    flagged  = sum(1 for h in history if "FAKE" in h.get("verdict","").upper()
                   or "GENERATED" in h.get("verdict","").upper()
                   or "DEEPFAKE" in h.get("verdict","").upper())
    avg_risk = int(sum(h.get("fake_score",0) for h in history) / total) if total else 0
    txt_cnt  = sum(1 for h in history if h.get("type") == "text")
    img_cnt  = total - txt_cnt

    kpis = [
        ("Analyses Run",  str(total),               "#7C4DFF"),
        ("Flagged",       str(flagged),              "#FF4560"),
        ("Avg Risk Score",f"{avg_risk}%",            get_risk_color(avg_risk)),
        ("Text / Image",  f"{txt_cnt} / {img_cnt}", "#00CFFF"),
    ]
    for col, (lbl, val, color) in zip([k1, k2, k3, k4], kpis):
        with col:
            st.markdown(
                f"""
                <div class="dash-kpi">
                  <div class="dash-kpi-val" style="color:{color}">{val}</div>
                  <div class="dash-kpi-lbl">{lbl}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<hr class='section-divider' style='margin:28px 0'>", unsafe_allow_html=True)

    # ── Text analysis charts ─────────────────────────────────
    if text_result and "error" not in text_result:
        section_header("Fake News Analysis Overview", "")
        col1, col2 = st.columns([1, 1])

        with col1:
            labels = ["Fake Score", "Bias Score", "Manipulation", "Distrust"]
            values = [
                text_result.get("fake_score", 0),
                text_result.get("bias_score", 0),
                text_result.get("manipulation_score", 0),
                100 - text_result.get("trust_score", 0),
            ]
            st.plotly_chart(make_bar_chart(labels, values, "Risk Factor Breakdown"), use_container_width=True)

        with col2:
            radar = {
                "Fake":         text_result.get("fake_score", 0),
                "Bias":         text_result.get("bias_score", 0),
                "Manipulation": text_result.get("manipulation_score", 0),
                "Distrust":     100 - text_result.get("trust_score", 0),
                "Confidence":   text_result.get("confidence", 0),
            }
            st.plotly_chart(make_radar_chart(radar), use_container_width=True)

        g1, g2 = st.columns(2)
        with g1:
            st.plotly_chart(make_gauge_chart(text_result.get("confidence", 0),        "AI Confidence", "#7C4DFF"), use_container_width=True)
        with g2:
            st.plotly_chart(make_gauge_chart(text_result.get("fake_score", 0),        "Fake Score",    "#FF4560"), use_container_width=True)

    # ── Image analysis charts ────────────────────────────────
    if image_result and "error" not in image_result:
        st.markdown("<hr class='section-divider' style='margin:28px 0'>", unsafe_allow_html=True)
        section_header("Deepfake Analysis Overview", "")
        g1, g2, g3 = st.columns(3)
        with g1:
            st.plotly_chart(make_gauge_chart(image_result.get("ai_generated_score", 0), "AI Generated",  "#8B5CF6"), use_container_width=True)
        with g2:
            st.plotly_chart(make_gauge_chart(image_result.get("manipulation_score",  0), "Manipulation",  "#FF4560"), use_container_width=True)
        with g3:
            st.plotly_chart(make_gauge_chart(image_result.get("authenticity_score",  0), "Authenticity",  "#00E5A0"), use_container_width=True)

    # ── History line chart ───────────────────────────────────
    if len(history) > 1:
        st.markdown("<hr class='section-divider' style='margin:28px 0'>", unsafe_allow_html=True)
        section_header("Session History — Fake / Risk Score Trend", "")
        fig = make_history_line_chart(history)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

    # ── Clear button ─────────────────────────────────────────
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([3, 1, 3])
    with btn_col:
        if st.button("Clear Session Data", key="clear_dash", use_container_width=True):
            st.session_state.analysis_history = []
            st.session_state.text_result = None
            st.session_state.image_result = None
            st.rerun()

    render_footer()
