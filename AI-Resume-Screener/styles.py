page_style = """
<style>

html {
    scroll-behavior: smooth;
}

/* HIDE STREAMLIT */

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    display: none;
}

/* MAIN APP */

.stApp {
    background: linear-gradient(
        135deg,
        #050816 0%,
        #0B1120 40%,
        #111827 100%
    );
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0B1120;
    border-right: 1px solid rgba(255,255,255,0.08);
    width: 250px !important;
}

/* SIDEBAR SELECTBOX */

div[data-baseweb="select"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #E2E8F0 !important;
}

/* FEATURE CARD */

.feature-card {
    background: rgba(255,255,255,0.04);
    padding: 16px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-top: 20px;
    backdrop-filter: blur(8px);
}

/* SIDEBAR TITLE */

.sidebar-title {
    text-align: center;
    color: #38BDF8;
    font-size: 34px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 0px;
}

/* SIDEBAR SUBTITLE */

.sidebar-subtitle {
    text-align: center;
    color: #94A3B8;
    font-size: 13px;
    margin-bottom: 25px;
}

/* MAIN CONTAINER */

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
    max-width: 1300px;
}

/* TITLE */

.title {
    text-align: center;
    font-size: 65px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 10px;
}

.title span {
    color: #38BDF8;
    text-shadow: 0px 0px 25px rgba(56,189,248,0.6);
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #CBD5E1;
    margin-top: 15px;
    margin-bottom: 40px;
}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
}

/* BUTTON */

.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #38BDF8, #6366F1);
    color: white;
    border-radius: 14px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    padding: 14px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(56,189,248,0.5);
}

/* PROGRESS BAR */

.stProgress > div > div > div > div {
    background: linear-gradient(to right, #38BDF8, #6366F1);
}

/* SCORE CARD */

.score-card {
    background: rgba(255,255,255,0.06);
    padding: 25px;
    border-radius: 24px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    box-shadow: 0px 0px 25px rgba(56,189,248,0.08);
}

/* ANALYSIS CARD */

.section-card {
    background: rgba(255,255,255,0.05);
    padding: 24px;
    border-radius: 22px;
    margin-bottom: 22px;
    border-left: 4px solid #38BDF8;
    transition: 0.3s;
    backdrop-filter: blur(12px);
}

.section-card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 0px 25px rgba(56,189,248,0.15);
}

.section-title {
    color: #38BDF8;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 14px;
}

.section-content {
    color: #E2E8F0;
    font-size: 16px;
    line-height: 1.9;
}

/* SIDEBAR TITLE */

.sidebar-title {
    text-align: center;
    color: #38BDF8;
    font-size: 32px;
    font-weight: 800;
    margin-top: 10px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94A3B8;
    margin-top: 70px;
    font-size: 14px;
}

/* NAVIGATION TITLE */

.nav-title{
    color:#38BDF8;
    font-size:22px;
    font-weight:700;
    margin-bottom:15px;
    margin-top:10px;
}

/* SIDEBAR BUTTONS */

section[data-testid="stSidebar"] .stButton > button {

    width:100%;
    background: rgba(255,255,255,0.05);
    color:white;
    border:none;
    border-radius:14px;
    padding:10px;
    margin-bottom:8px;
    font-size:15px;
    font-weight:600;
    text-align:left;

    transition: all 0.3s ease;
}
/* HIDE SIDEBAR COLLAPSE BUTTON */

[data-testid="collapsedControl"] {
    display: none;
}
/* FORCE SIDEBAR VISIBLE */

section[data-testid="stSidebar"] {
    margin-left: 0px !important;
    transform: none !important;
    visibility: visible !important;
}
/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: #0B1120 !important;

    width: 320px !important;
    min-width: 320px !important;
    max-width: 320px !important;

    border-right: 1px solid rgba(255,255,255,0.08);

    visibility: visible !important;
    margin-left: 0px !important;
    transform: none !important;
}

/* KEEP SIDEBAR OPEN */

[data-testid="collapsedControl"] {
    display: none;
}
/* HOVER EFFECT */

section[data-testid="stSidebar"] .stButton > button:hover {

    background: linear-gradient(
        135deg,
        #2563EB,
        #38BDF8
    );

    transform: translateX(5px);

    box-shadow: 0px 0px 18px rgba(56,189,248,0.4);
}

</style>
"""
