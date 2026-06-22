import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CareerPath AI", layout="wide")

# Load custom css
css_file = Path(__file__).parent / "styles" / "custom.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header / Hero area
st.markdown(
    """
    <div class="hero">
      <div class="hero-content">
        <h1 class="hero-title">CareerPath AI</h1>
        <p class="hero-sub">Smart, friendly career guidance for 10th & 12th pass students — AI recommendations, roadmaps and colleges.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="#">Get Recommendations</a>
          <a class="btn btn-outline" href="#">Take Aptitude Test</a>
        </div>
      </div>
      <div class="hero-visual"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Navigate")
st.sidebar.markdown("""
- Home
- Aptitude Test
- Career Recommendations
- Career Explorer
- College Finder
- Entrance Exams
- Scholarships
- Salary Insights
- Roadmap Generator
- AI Counselor
- About
""")

st.info("Use the sidebar to navigate. For the full multi-page UI open the pages/ files via the Streamlit app menu.")
