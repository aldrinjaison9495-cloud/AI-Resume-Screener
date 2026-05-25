page_style = """
<style>

html {
    scroll-behavior: smooth;
}
/*HIDE STREAMLIT HEADER*/
            header{
            visibility:hidden;
            }
            [data-testid="stToolbar"]{
            display: none;
            }
            [data-testid="stDecoration"]{
            display: none;
            }
            [data-testid="stStatusWidget"]{
            display: none;
            }


            
.stApp {
    background: linear-gradient(135deg, #0F172A, #1E293B);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid rgba(255,255,255,0.1);
    width: 260px !important;
}

/* MAIN CONTAINER */

.block-container {
    padding-top: 2rem;
    padding-left: 5rem;
    padding-right: 5rem;
    max-width: 1200px;
}

/* TITLE */

.title {
    text-align: center;
    font-size: 55px;
    font-weight: 800;
    color: #00FFD1;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #CBD5E1;
    margin-bottom: 40px;
}

/* BUTTONS */

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #00FFD1, #00BFFF);
    color: black;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 15px rgba(0,255,209,0.5);
}

/* PROGRESS BAR */

.stProgress > div > div > div > div {
    background: linear-gradient(to right, #00FFD1, #00BFFF);
}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    max-width: 900px;
    margin: auto;
}

/* SCORE CARDS */

.score-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(8px);
}
            
            

/* ANALYSIS CARDS */


.section-card {
    background: rgba(255,255,255,0.04);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 20px;
    border-left: 4px solid #00FFD1;
    transition: 0.3s;
}

.section-card:hover {
    transform: translateY(-2px);
    box-shadow: 0px 0px 20px rgba(0,255,209,0.15);
}

.section-title {
    color: #00FFD1;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 15px;
}

.section-content {
    color: #E2E8F0;
    font-size: 16px;
    line-height: 1.9;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94A3B8;
    margin-top: 60px;
    font-size: 15px;
}

</style>
"""