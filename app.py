import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CareerPath AI", layout="wide")

# Load custom css
css_file = Path(__file__).parent / "styles" / "custom.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("CareerPath AI")
st.write("A modern AI-powered career guidance platform for 10th and 12th pass students.")

st.sidebar.title("Navigate")
pages = [
    "Home",
    "Aptitude Test",
    "Career Recommendations",
    "Career Explorer",
    "College Finder",
    "Entrance Exams",
    "Scholarships",
    "Salary Insights",
    "Roadmap Generator",
    "AI Counselor",
    "About",
]
choice = st.sidebar.radio("Go to", pages)

# Simple navigation — Streamlit multipage will also show the pages/ files in the app.
st.info("This repository uses a pages/ directory for fully-featured pages. Use the Streamlit app menu (top-right) to jump to a numbered page or use the sidebar.")

if choice == "Home":
    st.header("Welcome to CareerPath AI")
    st.markdown("\n".join([
        "**AI Career Recommendations** — Get personalized career suggestions.",
        "**Aptitude Test** — Assess strengths across skills.",
        "**College Finder** — Filter colleges by state, budget, and type.",
    ]))
    st.button("Open Home Page (pages/1_Home.py)")
else:
    st.write(f"Use the Streamlit app menu to open the {choice} page for the full experience.")
