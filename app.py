import streamlit as st
from pathlib import Path
import importlib.util
import sys

# Ensure project root is on sys.path so absolute imports inside page modules work
BASE = Path(__file__).parent
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

st.set_page_config(page_title="CareerPath AI", layout="wide")

# Load custom css
css_file = Path(__file__).parent / "styles" / "custom.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation map: label -> file path (now using app_pages to avoid Streamlit pages auto-listing)
PAGES = {
    "Home": BASE / "app_pages" / "page_home.py",
    "Aptitude Test": BASE / "app_pages" / "page_aptitude_test.py",
    "Career Recommendations": BASE / "app_pages" / "page_career_recommendations.py",
    "Career Explorer": BASE / "app_pages" / "page_career_explorer.py",
    "College Finder": BASE / "app_pages" / "page_college_finder.py",
    "Entrance Exams": BASE / "app_pages" / "page_entrance_exams.py",
    "Scholarships": BASE / "app_pages" / "page_scholarships.py",
    "Salary Insights": BASE / "app_pages" / "page_salary_insights.py",
    "Roadmap Generator": BASE / "app_pages" / "page_roadmap_generator.py",
    "AI Counselor": BASE / "app_pages" / "page_ai_counselor.py",
    "About": BASE / "app_pages" / "page_about.py",
    "Resume Builder": BASE / "app_pages" / "page_resume_builder.py",
    "Skill Gap Analyzer": BASE / "app_pages" / "page_skill_gap_analyzer.py",
    "Admin": BASE / "components" / "admin.py",
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
        # Ensure the project root is available for imports performed by the module
        if str(BASE) not in sys.path:
            sys.path.insert(0, str(BASE))
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
