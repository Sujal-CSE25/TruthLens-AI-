"""TruthLens AI — Top Navigation Bar"""
import streamlit as st

PAGES = ["Home", "Detection", "Analytics", "Team", "About"]


def render_navbar():
    current = st.session_state.get("page", "Home")

    # 7 columns: brand | 5 nav items | spacer
    c0, c1, c2, c3, c4, c5, c6 = st.columns([2.6, 0.82, 0.95, 0.95, 0.72, 0.82, 0.4])

    with c0:
        # .nav-marker here identifies this stHorizontalBlock as the navbar via CSS :has()
        st.markdown(
            '<div class="nav-marker nav-brand">'
            '<div class="nav-brand-logo">T</div>'
            '<span class="nav-brand-text">TruthLens AI</span>'
            "</div>",
            unsafe_allow_html=True,
        )

    for page, col in zip(PAGES, [c1, c2, c3, c4, c5]):
        with col:
            if page == current:
                st.markdown(
                    f'<div class="nav-active-item">{page}</div>',
                    unsafe_allow_html=True,
                )
            else:
                if st.button(page, key=f"nav_{page}", use_container_width=True):
                    st.session_state.page = page
                    st.rerun()

    # 8-px breathing room below navbar
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
