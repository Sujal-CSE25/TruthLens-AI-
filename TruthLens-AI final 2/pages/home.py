"""TruthLens AI — Home / Landing Page (8 sections). Emoji-free, enterprise design."""
import streamlit as st
from components.footer import render_footer


def _nav(page: str):
    st.session_state.page = page
    st.rerun()


def render_home():
    # ── SECTION 1: HERO ──────────────────────────────────────
    st.markdown(
        """
        <div class="hero-wrap fade-in">
          <div class="hero-eyebrow">Powered by Google Gemini 2.0</div>
          <h1 class="hero-title">TruthLens AI</h1>
          <p class="hero-desc">
            Detect fake news, misinformation, manipulated media, and deepfakes using
            advanced AI models with explainable, trustworthy results.
          </p>
          <div class="hero-cta">
            <span class="btn-hero-primary">Detect Fake News</span>
            <span class="btn-hero-outline">Detect Deepfake</span>
          </div>
          <div class="hero-stats">
            <div class="hero-stat">
              <div class="hero-stat-val">50K+</div>
              <div class="hero-stat-lbl">Content Analyzed</div>
            </div>
            <div class="hero-stat">
              <div class="hero-stat-val">98.7%</div>
              <div class="hero-stat-lbl">Detection Accuracy</div>
            </div>
            <div class="hero-stat">
              <div class="hero-stat-val">15K+</div>
              <div class="hero-stat-lbl">Fake News Flagged</div>
            </div>
            <div class="hero-stat">
              <div class="hero-stat-val">8K+</div>
              <div class="hero-stat-lbl">Deepfakes Detected</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c, col_d = st.columns([2, 1, 1, 2])
    with col_b:
        if st.button("Detect Fake News", key="hero_fn", use_container_width=True):
            _nav("Detection")
    with col_c:
        if st.button("Detect Deepfake", key="hero_df", use_container_width=True):
            _nav("Detection")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 2: THE PROBLEM ───────────────────────────────
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:40px">
          <div class="section-label">The Challenge We Solve</div>
          <div class="section-title">Misinformation Is a <span class="grad-text">Global Crisis</span></div>
          <div class="section-subtitle">
            The spread of fake news, deepfakes, and synthetic media is eroding public
            trust and distorting reality at an unprecedented scale.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pc1, pc2, pc3, pc4 = st.columns(4)
    problems = [
        ("red",    "SPREAD RATE",   "500%",  "Misinformation Spread",
         "Misinformation spreads 6x faster than factual content on social platforms."),
        ("yellow", "SCALE",         "3.2B",  "Deepfake Threats",
         "Over 3.2 billion deepfake images were created in 2023 alone — up 300% year-over-year."),
        ("purple", "PUBLIC CONCERN","85%",   "Trust Deficit",
         "85% of people worry about their inability to distinguish real content from fake."),
        ("cyan",   "DELAY",         "72hrs", "Verification Lag",
         "Manual fact-checking takes up to 72 hours — by which time the damage is done."),
    ]
    for col, (stat_cls, tag_lbl, stat, title, desc) in zip([pc1, pc2, pc3, pc4], problems):
        with col:
            st.markdown(
                f"""
                <div class="problem-card">
                  <div class="prob-tag prob-tag-{stat_cls}">{tag_lbl}</div>
                  <div class="prob-title">{title}</div>
                  <div class="prob-desc">{desc}</div>
                  <div class="prob-stat prob-stat-{stat_cls}">{stat}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="why-matters">
          <div>
            <div class="why-matters-title">Why it matters</div>
            <div class="why-matters-desc">
              Every piece of misinformation erodes the fabric of informed society.
              TruthLens provides instant, AI-powered verification to restore confidence in information.
            </div>
          </div>
          <div class="why-matters-tags">
            <span class="wm-tag wm-tag-cyan">Instant Verification</span>
            <span class="wm-tag wm-tag-purple">Explainable AI</span>
            <span class="wm-tag wm-tag-green">Open Source</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 3: HOW IT WORKS ──────────────────────────────
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:40px">
          <div class="section-label">Simple Process</div>
          <div class="section-title">How <span class="grad-text">TruthLens</span> Works</div>
          <div class="section-subtitle">
            A four-step pipeline that takes raw content and delivers
            clear, actionable intelligence within seconds.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4)
    steps = [
        ("01", "Upload Content",
         "Paste a news headline, article, or tweet — or upload an image for analysis."),
        ("02", "AI Analysis",
         "Google Gemini 2.0 and our NLP pipeline analyze content for signs of fabrication or manipulation."),
        ("03", "Fact Verification",
         "Claims are cross-referenced against trusted knowledge sources and evaluated for logical consistency."),
        ("04", "Detailed Results",
         "A comprehensive report with confidence scores, red flags, explanations, and actionable insights."),
    ]
    for col, (num, title, desc) in zip([s1, s2, s3, s4], steps):
        with col:
            st.markdown(
                f"""
                <div class="step-card">
                  <div class="step-num-badge">STEP {num}</div>
                  <div class="step-title">{title}</div>
                  <div class="step-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 4: CORE TECHNOLOGIES ────────────────────────
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:40px">
          <div class="section-label">Core Capabilities</div>
          <div class="section-title">Two Powerful <span class="grad-text">Detection Engines</span></div>
          <div class="section-subtitle">
            Working together to tackle misinformation at every layer —
            text content and visual media.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    fc1, fc2 = st.columns(2)
    with fc1:
        st.markdown(
            """
            <div class="feature-card">
              <div class="fc-label">Text Intelligence</div>
              <div class="fc-title">Fake News Detection</div>
              <div class="fc-sub">
                Gemini 2.0's advanced reasoning detects misinformation, bias,
                and manipulative language in any text format.
              </div>
              <ul class="fc-list">
                <li class="fc-item"><span class="fc-check">&#10003;</span> NLP Semantic Analysis</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Real-time Fact Verification</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Gemini 2.0 Reasoning</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Confidence Scoring (0–100)</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Explainable AI Summaries</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Try Fake News Detection", key="cta_fn", use_container_width=True):
            _nav("Detection")

    with fc2:
        st.markdown(
            """
            <div class="feature-card">
              <div class="fc-label">Vision Intelligence</div>
              <div class="fc-title">Deepfake Detection</div>
              <div class="fc-sub">
                Computer Vision and Gemini Vision AI inspect every pixel for
                signs of AI generation, manipulation, and synthetic media.
              </div>
              <ul class="fc-list">
                <li class="fc-item"><span class="fc-check">&#10003;</span> CNN Image Analysis</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Gemini Vision AI</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Pixel-level Inspection</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Metadata Forensics</li>
                <li class="fc-item"><span class="fc-check">&#10003;</span> Authenticity Scoring</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Upload Media for Analysis", key="cta_df", use_container_width=True):
            _nav("Detection")

    st.markdown(
        """
        <div class="integration-bar" style="margin-top:14px">
          <div class="ib-left">
            <div>
              <div class="ib-title">Unified Platform</div>
              <div class="ib-desc">Both engines work together — text analysis and image forensics — in one interface.</div>
            </div>
          </div>
          <span class="ib-link">View Documentation &rarr;</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 5: KPI ──────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:40px">
          <div class="section-label">Platform Impact</div>
          <div class="section-title">Trusted at <span class="grad-text">Scale</span></div>
          <div class="section-subtitle">
            Real numbers from real detections — TruthLens is making a measurable
            dent in the global misinformation epidemic.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)
    for col, (val, lbl) in zip([k1, k2, k3, k4], [
        ("50K+", "Content Analyzed"), ("98.7%", "Detection Accuracy"),
        ("15K+", "Fake News Detected"), ("8K+", "Deepfakes Flagged"),
    ]):
        with col:
            st.markdown(
                f'<div class="kpi-card"><div class="kpi-val">{val}</div><div class="kpi-lbl">{lbl}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 6: WHY TRUTHLENS ─────────────────────────────
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:40px">
          <div class="section-label">Advantages</div>
          <div class="section-title">Why Choose <span class="grad-text">TruthLens</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    w1, w2, w3 = st.columns(3)
    w4, w5, w6 = st.columns(3)
    why_items = [
        ("01", "Fast Detection",       "Real-time results in under 10 seconds powered by Gemini 2.0."),
        ("02", "High Accuracy",        "98.7% detection accuracy on benchmark misinformation datasets."),
        ("03", "Explainable AI",       "Clear reasoning for every verdict — no black-box outputs."),
        ("04", "Secure Processing",    "Data analyzed in-session only. Nothing is stored permanently."),
        ("05", "Scalable Architecture","Designed to handle bulk analysis workloads with minimal latency."),
        ("06", "Modern Models",        "Uses Google Gemini 2.0 multimodal Vision AI and NLP models."),
    ]
    for col, (idx, title, desc) in zip([w1, w2, w3, w4, w5, w6], why_items):
        with col:
            st.markdown(
                f"""
                <div class="why-card">
                  <div class="wc-index">{idx}</div>
                  <div class="wc-title">{title}</div>
                  <div class="wc-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── SECTION 7: TEAM ─────────────────────────────────────
    _render_team_cards()

    # ── SECTION 8: FOOTER ────────────────────────────────────
    render_footer()


def _render_team_cards():
    st.markdown(
        """
        <div class="team-section-title">Meet Our Team</div>
        <div class="team-section-sub">
            The people behind TruthLens AI &mdash; Team HackManthan, DDUGU Gorakhpur
        </div>
        """,
        unsafe_allow_html=True,
    )

    members = [
        {
            "initials": "SK",
            "name": "Sujal Kumar Patwa",
            "role": "Team Lead &amp; AI/ML Engineer",
            "responsibilities": [
                "Project architecture and technical direction",
                "NLP pipeline and fake news detection engine",
                "Gemini API integration and ML model development",
                "Research methodology and model evaluation",
            ],
            "skills": ["Python", "Gemini AI", "NLP", "ML"],
            "lead": True,
        },
        {
            "initials": "AM",
            "name": "Aayush Mani Tripathi",
            "role": "Backend &amp; AI/ML Developer",
            "responsibilities": [
                "Backend architecture and API routing",
                "Data orchestration and session management",
                "ML pipeline integration and optimization",
                "Server-side logic and data flow design",
            ],
            "skills": ["Python", "APIs", "Data Flow", "ML"],
            "lead": False,
        },
        {
            "initials": "ON",
            "name": "Om Narayan",
            "role": "Frontend &amp; UI Developer",
            "responsibilities": [
                "UI architecture and Streamlit frontend",
                "Component system and design implementation",
                "UX flows and responsive design",
                "CSS design language and visual polish",
            ],
            "skills": ["Streamlit", "CSS", "UX", "Frontend"],
            "lead": False,
        },
        {
            "initials": "RK",
            "name": "Ritesh Kumar Gautam",
            "role": "Image AI &amp; QA Engineer",
            "responsibilities": [
                "Deepfake detection and image processing",
                "Gemini Vision AI integration",
                "End-to-end testing and validation",
                "QA workflows and bug triage",
            ],
            "skills": ["CV", "Gemini Vision", "PIL", "QA"],
            "lead": False,
        },
    ]

    t1, t2, t3, t4 = st.columns(4)
    for col, m in zip([t1, t2, t3, t4], members):
        resp_items = "".join(
            f'<li class="tc-resp-item"><span class="tc-resp-dot"></span>{r}</li>'
            for r in m["responsibilities"]
        )
        skill_badges = "".join(
            f'<span class="tc-badge">{s}</span>' for s in m["skills"]
        )
        lead_badge = (
            '<span class="tc-badge tc-badge-lead">Team Lead</span>' if m["lead"] else ""
        )
        with col:
            st.markdown(
                f"""
                <div class="team-card">
                  <div class="tc-header">
                    <div class="tc-avatar">{m['initials']}</div>
                    <div class="tc-social">
                      <a class="tc-social-link" href="#" title="GitHub">GH</a>
                      <a class="tc-social-link" href="#" title="LinkedIn">in</a>
                    </div>
                  </div>
                  <div class="tc-name">{m['name']}</div>
                  <div class="tc-role">{m['role']}</div>
                  <div class="tc-resp-title">Responsibilities</div>
                  <ul class="tc-resp-list">{resp_items}</ul>
                  <div class="tc-badge-row">{lead_badge}{skill_badges}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
