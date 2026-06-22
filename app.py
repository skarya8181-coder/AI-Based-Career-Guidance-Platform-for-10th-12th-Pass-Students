import streamlit as st
from pathlib import Path
import importlib.util
import sys

st.set_page_config(page_title="CareerPath AI", layout="wide")

# Load custom css
css_file = Path(__file__).parent / "styles" / "custom.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation map: label -> file path
PAGES = {
    "Home": Path("pages/1_Home.py"),
    "Aptitude Test": Path("pages/2_Aptitude_Test.py"),
    "Career Recommendations": Path("pages/3_Career_Recommendations.py"),
    "Career Explorer": Path("pages/4_Career_Explorer.py"),
    "College Finder": Path("pages/5_College_Finder.py"),
    "Entrance Exams": Path("pages/6_Entrance_Exams.py"),
    "Scholarships": Path("pages/7_Scholarships.py"),
    "Salary Insights": Path("pages/8_Salary_Insights.py"),
    "Roadmap Generator": Path("pages/9_Roadmap_Generator.py"),
    "AI Counselor": Path("pages/10_AI_Counselor.py"),
    "About": Path("pages/11_About.py"),
    "Resume Builder": Path("pages/13_Resume_Builder.py"),
    "Skill Gap Analyzer": Path("pages/14_Skill_Gap_Analyzer.py"),
    "Admin": Path("components/admin.py"),
}

st.sidebar.title("Navigate")
page_names = list(PAGES.keys())
# allow session navigation override
if 'navigate_to' not in st.session_state:
    st.session_state['navigate_to'] = None

# current choice
choice = st.sidebar.radio("Go to", page_names, index=0)
# prefer an explicit navigate_to request from pages (set by a button)
if st.session_state.get("navigate_to"):
    choice = st.session_state.pop("navigate_to")


def load_and_render(path: Path):
    if not path.exists():
        st.error(f"Page file not found: {path}")
        return
    module_name = f"page_{path.stem}"
    try:
        spec = importlib.util.spec_from_file_location(module_name, str(path))
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        if hasattr(module, "render"):
            module.render()
        else:
            st.error(f"The page module {path.name} does not expose a render() function.")
    except Exception as e:
        st.exception(e)

# Load selected page
load_and_render(PAGES[choice])
