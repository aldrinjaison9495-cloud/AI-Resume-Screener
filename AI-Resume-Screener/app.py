import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
from groq import Groq
from styles import page_style
from pdf_generator import generate_pdf
import re


load_dotenv()

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)
st.markdown(page_style, unsafe_allow_html=True)


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.markdown(
    """
    <h1 style='text-align:center;
    color:#00FFD1;
    font-size:32px;
    font-weight:800;'>
    🚀 Resume AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "📄 Upload Resume",
        "📊 Resume Score",
        "📈 ATS Score",
        "🧠 AI Analysis",
        "⬇ Download PDF"
    ]
)

st.sidebar.markdown("---")

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
    '<div class="title">🚀 AI Resume Screening System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload your resume and get AI-powered career insights</div>',
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

        start = result.find(sections[i])

        if start != -1:

            end = len(result)

            for j in range(i + 1, len(sections)):

                next_start = result.find(sections[j])

                if next_start != -1 and next_start > start:
                    end = next_start
                    break

            content = result[start:end].replace(
                sections[i],
                ""
            ).strip()

            extracted_sections[sections[i]] = content

    # -----------------------------------
    # RESUME SCORE
    # -----------------------------------

    resume_match = re.search(
        r"Resume Score:\s*(\d+(\.\d+)?)\/10",
        result,
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

            st.progress(resume_score)

            st.success(
                f"Resume Score: {resume_score}%"
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

    # -----------------------------------
    # ATS SCORE
    # -----------------------------------

    ats_match = re.search(
        r"ATS Score.*?(\d+(\.\d+)?)\/10",
        result,
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

            st.progress(ats_score)

            st.success(
                f"ATS Score: {ats_score}%"
            )

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