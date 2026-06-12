"""TruthLens AI — Team Page. Enterprise-grade, no gradients, no playful badges."""
import streamlit as st
from components.footer import render_footer


def render_team():
    st.markdown(
        """
        <div style="padding:40px 0 36px;text-align:center">
          <div class="section-label">The People</div>
          <div class="section-title">Meet Our <span class="grad-text">Team</span></div>
          <div class="section-subtitle">
            The people behind TruthLens AI &mdash; Team HackManthan from DDUGU Gorakhpur.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    members = [
        {
            "initials": "SK",
            "name": "Sujal Kumar Patwa",
            "role": "Team Lead &amp; AI/ML Engineer",
            "bio": (
                "Leads the project from architecture to execution. Designed and built the core "
                "AI/ML pipeline — NLP-based text classification, Gemini 2.0 API integration, "
                "and the complete fake-news detection engine with explainable outputs."
            ),
            "responsibilities": [
                "End-to-end project architecture and technical direction",
                "NLP pipeline design and fake news detection engine",
                "Gemini API integration and ML model development",
                "Research methodology and performance evaluation",
            ],
            "skills": ["Python", "Gemini AI", "NLP", "ML Models", "LLM Integration"],
            "lead": True,
        },
        {
            "initials": "AM",
            "name": "Aayush Mani Tripathi",
            "role": "Backend &amp; AI/ML Developer",
            "bio": (
                "Architects the backend systems and integrates ML pipelines with the application "
                "layer. Responsible for API routing, data orchestration, session management, "
                "and performance optimization across the stack."
            ),
            "responsibilities": [
                "Backend architecture and API routing design",
                "ML pipeline integration and optimization",
                "Data orchestration and session state management",
                "Server-side logic and inter-component data flow",
            ],
            "skills": ["Python", "API Design", "Data Flow", "ML Pipelines", "Streamlit Backend"],
            "lead": False,
        },
        {
            "initials": "ON",
            "name": "Om Narayan",
            "role": "Frontend &amp; UI Developer",
            "bio": (
                "Owns the entire frontend layer of TruthLens. Built the UI architecture, "
                "CSS design system, all Streamlit components, and every user-facing "
                "interaction — ensuring a consistent and professional visual experience."
            ),
            "responsibilities": [
                "UI architecture and Streamlit frontend development",
                "CSS design language and component system",
                "UX flows, navigation, and interactive states",
                "Responsive layout and visual polish",
            ],
            "skills": ["Streamlit", "CSS", "UX Design", "Frontend", "Component Architecture"],
            "lead": False,
        },
        {
            "initials": "RK",
            "name": "Ritesh Kumar Gautam",
            "role": "Image AI &amp; QA Engineer",
            "bio": (
                "Built the deepfake detection module using Gemini Vision AI and managed "
                "the image preprocessing pipeline. Leads quality assurance across the "
                "entire platform — defining test cases, catching regressions, and ensuring "
                "production readiness."
            ),
            "responsibilities": [
                "Deepfake detection module and image processing pipeline",
                "Gemini Vision AI integration and tuning",
                "End-to-end testing and validation workflows",
                "QA processes, bug triage, and regression testing",
            ],
            "skills": ["Computer Vision", "Gemini Vision", "PIL", "QA Testing", "Image Forensics"],
            "lead": False,
        },
    ]

    t1, t2 = st.columns(2)
    t3, t4 = st.columns(2)
    for col, m in zip([t1, t2, t3, t4], members):
        skill_badges = "".join(
            f'<span class="tc-badge">{s}</span>' for s in m["skills"]
        )
        lead_badge = (
            '<span class="tc-badge tc-badge-lead">Team Lead</span>' if m["lead"] else ""
        )
        with col:
            st.markdown(
                f"""
                <div class="team-card" style="margin-bottom:16px">
                  <div class="tc-header">
                    <div class="tc-avatar">{m['initials']}</div>
                    <div class="tc-social">
                      <a class="tc-social-link" href="#" title="GitHub">GH</a>
                      <a class="tc-social-link" href="#" title="LinkedIn">in</a>
                    </div>
                  </div>
                  <div class="tc-name">{m['name']}</div>
                  <div class="tc-role">{m['role']}</div>
                  <div style="font-size:0.83rem;color:var(--tx-m);line-height:1.6;margin-bottom:14px">{m['bio']}</div>
                  <div class="tc-badge-row">{lead_badge}{skill_badges}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Org card
    st.markdown(
        """
        <div style="text-align:center;margin:36px 0 20px">
          <div style="display:inline-block;background:rgba(124,77,255,0.08);
                      border:1px solid rgba(124,77,255,0.22);border-radius:12px;
                      padding:22px 44px;">
            <div style="font-family:var(--font-d);font-size:1.05rem;font-weight:700;
                        color:var(--tx);margin-bottom:5px">Team HackManthan</div>
            <div style="font-size:0.83rem;color:var(--tx-m)">
              Deen Dayal Upadhyaya Gorakhpur University (DDUGU) &nbsp;&middot;&nbsp; Gorakhpur, Uttar Pradesh
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_footer()
