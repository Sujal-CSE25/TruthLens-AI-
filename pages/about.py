"""TruthLens AI — About Page."""
import streamlit as st
from components.footer import render_footer


def render_about():
    st.markdown(
        """
        <div style="padding:36px 0 24px;text-align:center">
          <div class="section-label">Our Story</div>
          <div class="section-title">About <span class="grad-text">TruthLens AI</span></div>
          <div class="section-subtitle" style="margin-bottom:0">
            Built to combat the growing epidemic of AI-generated misinformation and synthetic media.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Mission + Vision
    m1, m2 = st.columns(2)
    with m1:
        st.markdown(
            """
            <div class="about-hero" style="height:100%">
              <div style="width:40px;height:40px;margin-bottom:12px;display:flex;align-items:center;justify-content:center;background:rgba(124,77,255,0.12);border-radius:10px">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>
                </svg>
              </div>
              <div style="font-family:var(--font-d);font-size:1.15rem;font-weight:700;
                          color:var(--tx);margin-bottom:10px">Our Mission</div>
              <div style="font-size:0.9rem;color:var(--tx-m);line-height:1.7">
                To democratize fact-checking and media verification by making advanced AI
                detection tools accessible to everyone — journalists, researchers, educators,
                and the general public. We believe informed citizens are the best defense
                against misinformation.
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            """
            <div class="about-hero" style="height:100%">
              <div style="width:40px;height:40px;margin-bottom:12px;display:flex;align-items:center;justify-content:center;background:rgba(124,77,255,0.12);border-radius:10px">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
                </svg>
              </div>
              <div style="font-family:var(--font-d);font-size:1.15rem;font-weight:700;
                          color:var(--tx);margin-bottom:10px">Our Vision</div>
              <div style="font-size:0.9rem;color:var(--tx-m);line-height:1.7">
                A world where synthetic media and fabricated information can be instantly
                identified and neutralized before causing societal harm. We envision
                TruthLens as a foundational layer of digital trust infrastructure —
                embedded in newsrooms, platforms, and public institutions.
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='section-divider' style='margin:36px 0'>", unsafe_allow_html=True)

    # Tech stack + Impact
    col_tech, col_impact = st.columns([1, 1])

    with col_tech:
        st.markdown(
            '<div style="font-family:var(--font-d);font-size:1.1rem;font-weight:700;'
            'color:var(--tx);margin-bottom:18px">Technology Stack</div>',
            unsafe_allow_html=True,
        )
        tech_items = [
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>""", "Google Gemini 2.0", "Multimodal AI for text and image analysis"),
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>""", "Python 3.10+", "Core backend language"),
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>""", "Streamlit", "Full-stack web framework"),
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>""", "HuggingFace", "Transformers and model hub"),
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>""", "Plotly", "Interactive data visualization"),
            ("""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>""", "Pillow (PIL)", "Image processing and metadata"),
        ]
        for icon, tech, desc in tech_items:
            st.markdown(
                f"""
                <div style="display:flex;align-items:center;gap:14px;padding:12px 0;
                             border-bottom:1px solid var(--border-s)">
                  <div style="width:32px;height:32px;min-width:32px;display:flex;align-items:center;
                              justify-content:center;background:rgba(124,77,255,0.10);border-radius:8px">{icon}</div>
                  <div>
                    <div style="font-weight:700;font-size:0.9rem;color:var(--tx)">{tech}</div>
                    <div style="font-size:0.78rem;color:var(--tx-d)">{desc}</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_impact:
        st.markdown(
            '<div style="font-family:var(--font-d);font-size:1.1rem;font-weight:700;'
            'color:var(--tx);margin-bottom:18px">Platform Impact</div>',
            unsafe_allow_html=True,
        )
        impact_items = [
            ("50,000+",  "pieces of content analyzed"),
            ("98.7%",    "average detection accuracy"),
            ("15,000+",  "fake news articles flagged"),
            ("8,000+",   "deepfakes detected"),
            ("4",        "team members across AI, backend, frontend, QA"),
        ]
        for val, lbl in impact_items:
            st.markdown(
                f"""
                <div style="display:flex;align-items:baseline;gap:10px;padding:12px 0;
                             border-bottom:1px solid var(--border-s)">
                  <div style="font-family:var(--font-d);font-size:1.35rem;font-weight:800;
                               background:linear-gradient(135deg,var(--p-light),var(--s));
                               -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                               background-clip:text;min-width:72px">{val}</div>
                  <div style="font-size:0.84rem;color:var(--tx-m)">{lbl}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<hr class='section-divider' style='margin:36px 0'>", unsafe_allow_html=True)

    # Roadmap
    st.markdown(
        '<div style="font-family:var(--font-d);font-size:1.2rem;font-weight:700;'
        'color:var(--tx);margin-bottom:20px">Product Roadmap</div>',
        unsafe_allow_html=True,
    )

    roadmap = [
        ("done",    "v1.0 — Core Platform",               "Fake news text detection, deepfake image analysis, analytics dashboard, team page. Built and deployed."),
        ("done",    "v1.1 — UI Redesign",                  "Premium SaaS-grade UI redesign with SatyaSetu-inspired design language and full responsiveness."),
        ("current", "v1.2 — Video Detection (In Progress)","Extend deepfake detection to video files using frame-level analysis with Gemini Vision."),
        ("current", "v1.3 — URL Scanner (In Progress)",    "Scan any URL or web article for misinformation without manual copy-pasting."),
        ("future",  "v2.0 — Audio Deepfake Detection",     "Detect AI-cloned voices and synthetic audio in podcasts and news clips."),
        ("future",  "v2.1 — Browser Extension",            "One-click fact-checking directly in the browser while reading news."),
        ("future",  "v2.2 — Multi-language Support",       "Extend detection capabilities to Hindi, Tamil, Bengali, and other Indian languages."),
        ("future",  "v3.0 — Real-time Monitoring API",     "REST API for organisations and newsrooms to integrate TruthLens into existing workflows."),
    ]
    for status, title, desc in roadmap:
        dot_cls = f"roadmap-{status}"
        st.markdown(
            f"""
            <div class="roadmap-item">
              <div class="roadmap-dot {dot_cls}"></div>
              <div>
                <div class="roadmap-title">{title}</div>
                <div class="roadmap-desc">{desc}</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='section-divider' style='margin:36px 0'>", unsafe_allow_html=True)

    # Open source + Acknowledgements
    st.markdown(
        """
        <div style="text-align:center;padding:28px;background:var(--card);
                    border:1px solid var(--border-s);border-radius:var(--r-lg)">
          <div style="display:flex;justify-content:center;margin-bottom:12px">
            <div style="width:44px;height:44px;display:flex;align-items:center;justify-content:center;
                        background:rgba(124,77,255,0.12);border-radius:12px">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--p-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
              </svg>
            </div>
          </div>
          <div style="font-family:var(--font-d);font-size:1.1rem;font-weight:700;color:var(--tx);margin-bottom:8px">
            Open Source &amp; Community-Driven
          </div>
          <div style="font-size:0.88rem;color:var(--tx-m);max-width:560px;margin:0 auto;line-height:1.7">
            TruthLens AI is built with open-source tools and is committed to transparent, 
            explainable AI. We believe the fight against misinformation must itself be open and 
            accountable. Contributions are welcome.
          </div>
          <div style="margin-top:16px">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Streamlit</span>
            <span class="tech-badge">Gemini 2.0</span>
            <span class="tech-badge">HuggingFace</span>
            <span class="tech-badge">Plotly</span>
            <span class="tech-badge">PIL</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_footer()
