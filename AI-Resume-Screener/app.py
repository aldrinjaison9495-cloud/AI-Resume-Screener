import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
from groq import Groq
from styles import page_style
from pdf_generator import generate_pdf
import plotly.graph_objects as go
import re


load_dotenv()

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(page_style, unsafe_allow_html=True)


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.markdown(
    """
    <div class="sidebar-title">
        🚀 Resume AI
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# -----------------------------------
# MODERN NAVIGATION
# -----------------------------------

st.sidebar.markdown(
    """
    <div class="nav-title">
    🚀 Navigation
    </div>
    """,
    unsafe_allow_html=True
)

# DEFAULT PAGE

if "page" not in st.session_state:
    st.session_state.page = "📄 Upload Resume"

# BUTTONS

if st.sidebar.button("📄 Upload Resume"):
    st.session_state.page = "📄 Upload Resume"

if st.sidebar.button("📊 Resume Score"):
    st.session_state.page = "📊 Resume Score"

if st.sidebar.button("📈 ATS Score"):
    st.session_state.page = "📈 ATS Score"

if st.sidebar.button("🧠 AI Analysis"):
    st.session_state.page = "🧠 AI Analysis"

if st.sidebar.button("⬇ Download PDF"):
    st.session_state.page = "⬇ Download PDF"

# CURRENT PAGE

page = st.session_state.page

st.sidebar.markdown("---")
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("## ✨ Features")

st.sidebar.success("AI Resume Analysis")
st.sidebar.success("ATS Optimization")
st.sidebar.success("Skill Detection")
st.sidebar.success("Career Suggestions")
st.sidebar.success("Learning Roadmap")
st.sidebar.success("PDF Report Download")

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style='text-align:center;
    color:#94A3B8;
    font-size:15px;
    margin-top:20px;'>


    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# GROQ API
# -----------------------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
# -----------------------------------
# TITLE
# -----------------------------------

st.markdown(
    """
    <div class="title">
        AI <span>RESUME</span><br>
        <span>SCREENER</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Smart Resume Analysis • ATS Optimization • AI Career Insights
    </div>
    """,
    unsafe_allow_html=True
)
# -----------------------------------
# UPLOAD SECTION
# -----------------------------------

if page == "📄 Upload Resume":

    st.header("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

# -----------------------------------
# PROCESS RESUME
# -----------------------------------

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # -----------------------------------
    # READ PDF
    # -----------------------------------

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page_pdf in pdf_reader.pages:

        extracted_text = page_pdf.extract_text()

        if extracted_text:
            text += extracted_text

    # -----------------------------------
    # AI PROMPT
    # -----------------------------------

    prompt = f"""
You are an advanced AI Resume Analyzer.

Analyze the resume carefully.

Return the output EXACTLY in this format:

Skills:

Missing Skills:

Recommended Role:

Resume Score:
Give an accurate score out of 10 based on:
- Skills
- Projects
- Experience
- ATS compatibility
- Resume formatting
- Technical depth

ATS Score:
Give an ATS compatibility score out of 10 based on:
- Keywords
- Structure
- Readability
- Technical relevance

Strengths:

Weaknesses:

Improvement Suggestions:

Learning Roadmap:

Resume:
{text}
"""

    # -----------------------------------
    # AI ANALYSIS
    # -----------------------------------

    with st.spinner("🤖 AI is analyzing the resume..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response.choices[0].message.content

    # -----------------------------------
    # EXTRACT ANALYSIS SECTIONS
    # -----------------------------------

    sections = [
        "Skills:",
        "Missing Skills:",
        "Recommended Role:",
        "Resume Score:",
        "ATS Score:",
        "Strengths:",
        "Weaknesses:",
        "Improvement Suggestions:",
        "Learning Roadmap:"
    ]

    extracted_sections = {}

    for i in range(len(sections)):

        start = str(result).find(sections[i])

        if start != -1:

            end = len(str(result))

            for j in range(i + 1, len(sections)):

                next_start = str(result).find(sections[j])

                if next_start != -1 and next_start > start:
                    end = next_start
                    break

            content = str(result)[start:end].replace(
                sections[i],
                ""
            ).strip()

            extracted_sections[sections[i]] = content

    # -----------------------------------
    # RESUME SCORE
    # -----------------------------------

    resume_match = re.search(
        r"Resume Score:\s*(\d+(\.\d+)?)\/10",
        str(result),
        re.IGNORECASE
    )

    if resume_match:

        resume_score = float(resume_match.group(1))
        resume_score = int(resume_score * 10)

        if page == "📊 Resume Score":

            st.markdown(
                '<div class="score-card">',
                unsafe_allow_html=True
            )

            st.subheader("📊 Resume Score")

            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = resume_score,
                title = {'text': "Resume Score"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#38BDF8"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "#0F172A",
                    'steps': [
                        {'range': [0, 50], 'color': "#1E293B"},
                        {'range': [50, 80], 'color': "#334155"},
                        {'range': [80, 100], 'color': "#0EA5E9"}
                    ]
                }
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "white", 'size': 18},
                height=350
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

    # -----------------------------------
    # ATS SCORE
    # -----------------------------------

    ats_match = re.search(
        r"ATS Score.*?(\d+(\.\d+)?)\/10",
        str(result),
        re.IGNORECASE | re.DOTALL
    )
    if ats_match:

        ats_score = float(ats_match.group(1))
        ats_score = int(ats_score * 10)

        if page == "📈 ATS Score":

            st.markdown(
                '<div class="score-card">',
                unsafe_allow_html=True
            )

            st.subheader("📈 ATS Score")

            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = ats_score,
                title = {'text': "ATS Score"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#6366F1"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "#0F172A",
                    'steps': [
                        {'range': [0, 50], 'color': "#1E293B"},
                        {'range': [50, 80], 'color': "#334155"},
                        {'range': [80, 100], 'color': "#6366F1"}
                    ]
                }
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "white", 'size': 18},
                height=350
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

    else:

        if page == "📈 ATS Score":

            st.error("ATS Score not found")

    # -----------------------------------
    # AI ANALYSIS PAGE
    # -----------------------------------

    if page == "🧠 AI Analysis":

        st.markdown(
            """
            <h1 style='
            color:#00FFD1;
            font-size:42px;
            font-weight:800;
            margin-top:20px;
            margin-bottom:25px;
            '>
            🧠 AI Resume Analysis
            </h1>
            """,
            unsafe_allow_html=True
        )

        for heading, content in extracted_sections.items():

            st.markdown(
                f"""
                <div class="section-card">

                <div class="section-title">
                {heading}
                </div>

                <div class="section-content">
                {content.replace(chr(10), "<br>")}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    
    # -----------------------------------
# DOWNLOAD PDF
# -----------------------------------

    pdf_buffer = generate_pdf(extracted_sections)

    if page == "⬇ Download PDF":

        st.download_button(
            label="⬇ Download Analysis PDF",
            data=pdf_buffer,
            file_name="AI_Resume_Analysis.pdf",
            mime="application/pdf"
        )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown(
    '<div class="footer">🚀 Developed by Aldrin Jaison</div>',
    unsafe_allow_html=True
)