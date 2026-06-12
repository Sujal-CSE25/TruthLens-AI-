"""
TruthLens AI — Main Application Entry Point
Run with: streamlit run app.py
"""
import streamlit as st

# ── Page config (must be first Streamlit call) ─────────────────
st.set_page_config(
    page_title="TruthLens AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Imports after set_page_config ─────────────────────────────
from styles.design_system import CSS
from components.navbar import render_navbar
from pages.home import render_home
from pages.detection import render_detection
from pages.analytics import render_analytics
from pages.team import render_team
from pages.about import render_about

# ── Inject global CSS ─────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "text_result" not in st.session_state:
    st.session_state.text_result = None
if "image_result" not in st.session_state:
    st.session_state.image_result = None
if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

# ── Render navbar (always at top) ─────────────────────────────
render_navbar()

# ── Route to page ─────────────────────────────────────────────
page = st.session_state.page

if page == "Home":
    render_home()
elif page == "Detection":
    render_detection()
elif page == "Analytics":
    render_analytics()
elif page == "Team":
    render_team()
elif page == "About":
    render_about()
else:
    st.session_state.page = "Home"
    st.rerun()
