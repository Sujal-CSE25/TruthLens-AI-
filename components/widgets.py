"""TruthLens AI — Reusable UI widgets."""
import streamlit as st
from utils.helpers import get_risk_color, get_verdict_emoji


# ── Section header ────────────────────────────────────────────
def section_header(title: str, icon: str = ""):
    st.markdown(
        f'<div class="section-hdr">{icon} {title}</div>',
        unsafe_allow_html=True,
    )


# ── Verdict banner ────────────────────────────────────────────
def render_verdict(verdict: str):
    emoji = get_verdict_emoji(verdict)
    v = verdict.upper()
    if "REAL" in v or "AUTHENTIC" in v:
        cls = "verdict-real"
    elif "FAKE" in v or "GENERATED" in v or "DEEPFAKE" in v:
        cls = "verdict-fake"
    else:
        cls = "verdict-uncertain"

    st.markdown(
        f"""
        <div class="{cls}">
          <span class="verdict-icon">{emoji}</span>
          <div>
            <div class="verdict-sub">Verdict</div>
            <div>{verdict}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Score progress bar ────────────────────────────────────────
def score_bar(label: str, score: int, description: str = ""):
    color = get_risk_color(score)
    desc_html = (
        f"<div style='font-size:0.74rem;color:var(--tx-d);margin-top:3px'>{description}</div>"
        if description
        else ""
    )
    st.markdown(
        f"""
        <div class="score-bar-wrap">
          <div class="score-bar-hdr">
            <span class="score-bar-lbl">{label}</span>
            <span class="score-bar-num" style="color:{color}">{score}%</span>
          </div>
          <div class="score-bar-track">
            <div class="score-bar-fill" style="width:{score}%;background:linear-gradient(90deg,{color}99,{color})"></div>
          </div>
          {desc_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Score metric row (4 cards) ────────────────────────────────
def score_row(result: dict):
    items = [
        ("Fake Score",    result.get("fake_score", 0),         "Likelihood of being fabricated"),
        ("Trust Score",   result.get("trust_score", 0),        "Content trustworthiness"),
        ("Bias Score",    result.get("bias_score", 0),         "Editorial / political bias"),
        ("Manipulation",  result.get("manipulation_score", 0), "Manipulative language used"),
    ]
    cols = st.columns(4)
    for col, (lbl, val, sub) in zip(cols, items):
        color = get_risk_color(val)
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                  <div class="kpi-val" style="font-size:2rem;background:none;
                       -webkit-text-fill-color:{color};color:{color}">{val}%</div>
                  <div class="kpi-lbl">{lbl}</div>
                  <div style="font-size:0.72rem;color:var(--tx-d);margin-top:3px">{sub}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ── Red flags list ────────────────────────────────────────────
def render_flags(flags: list):
    if not flags:
        return
    section_header("Red Flags Detected", "")
    for f in flags:
        st.markdown(f'<div class="flag-item">&#9654; {f}</div>', unsafe_allow_html=True)


# ── Image findings ────────────────────────────────────────────
def render_findings(findings: list, title: str = "Analysis Findings"):
    if not findings:
        return
    section_header(title, "")
    for f in findings:
        st.markdown(f'<div class="finding-item">{f}</div>', unsafe_allow_html=True)


# ── Metadata flags ────────────────────────────────────────────
def render_meta_flags(flags: list):
    if not flags:
        return
    section_header("Metadata Flags", "")
    for f in flags:
        st.markdown(f'<div class="meta-item">{f}</div>', unsafe_allow_html=True)


# ── AI explanation box ────────────────────────────────────────
def ai_explanation(text: str):
    st.markdown(
        f'<div class="ai-box"><div class="ai-box-lbl">AI Analysis</div>{text}</div>',
        unsafe_allow_html=True,
    )


# ── Info banner ────────────────────────────────────────────────
def info_banner(title: str, body: str, icon: str = ""):
    st.markdown(
        f"""
        <div class="glass-card" style="border-color:rgba(124,77,255,0.2);padding:18px 22px">
          <div style="display:flex;align-items:flex-start;gap:12px">
            <div style="font-size:1.3rem;flex-shrink:0">{icon}</div>
            <div>
              <div style="font-weight:700;font-size:0.92rem;color:var(--tx);margin-bottom:4px">{title}</div>
              <div style="font-size:0.83rem;color:var(--tx-m);line-height:1.55">{body}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
