import streamlit as st
from pathlib import Path
from importlib import import_module

st.set_page_config(page_title="CareerPath AI", layout="wide")

# Load custom css
css_file = Path(__file__).parent / "styles" / "custom.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigate")
pages = [
    ("Home", "pages.1_Home"),
    ("Aptitude Test", "pages.2_Aptitude_Test"),
    ("Career Recommendations", "pages.3_Career_Recommendations"),
    ("Career Explorer", "pages.4_Career_Explorer"),
    ("College Finder", "pages.5_College_Finder"),
    ("Entrance Exams", "pages.6_Entrance_Exams"),
    ("Scholarships", "pages.7_Scholarships"),
    ("Salary Insights", "pages.8_Salary_Insights"),
    ("Roadmap Generator", "pages.9_Roadmap_Generator"),
    ("AI Counselor", "pages.10_AI_Counselor"),
    ("About", "pages.11_About"),
]

page_names = [p[0] for p in pages]
choice = st.sidebar.radio("Go to", page_names)

# Dynamically import and render the selected page
module_path = dict(pages)[choice]
try:
    module = import_module(module_path)
    if hasattr(module, "render"):
        module.render()
    else:
        st.error(f"The page module {module_path} does not expose a render() function.")
except Exception as e:
    st.exception(e)
