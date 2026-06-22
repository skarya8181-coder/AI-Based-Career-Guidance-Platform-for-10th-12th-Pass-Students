import streamlit as st
from utils.helper import save_aptitude_result
from utils.charts import radar_chart

st.set_page_config(page_title="Home - CareerPath AI", layout='wide')

st.markdown("""
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div>
      <h2 style="margin:0;color:#0f172a">Welcome to CareerPath AI</h2>
      <p style="margin:0;color:var(--muted)">Personalized career guidance for 10th and 12th pass students with visual insights and pathways.</p>
    </div>
    <div style="text-align:right">
      <a class="btn btn-primary" href="#">Try Recommendations</a>
    </div>
  </div>

  <div style="margin-top:1.25rem">
    <div class="feature-grid">
      <div class="feature-card card">
        <div class="feature-icon" style="background:linear-gradient(135deg,var(--accent),var(--accent-3))">AI</div>
        <div>
          <p class="feature-title">AI Career Recommendations</p>
          <p class="feature-desc">Get job matches tailored to your marks, interests and aptitude.</p>
        </div>
      </div>
      <div class="feature-card card">
        <div class="feature-icon" style="background:linear-gradient(135deg,var(--accent-2),#00C896)">AT</div>
        <div>
          <p class="feature-title">Aptitude Test</p>
          <p class="feature-desc">15 questions across analytical, creativity, communication and problem solving.</p>
        </div>
      </div>
      <div class="feature-card card">
        <div class="feature-icon" style="background:linear-gradient(135deg,#FF7AA2,#FFB26B)">CF</div>
        <div>
          <p class="feature-title">College Finder</p>
          <p class="feature-desc">Filter colleges by budget, state and course type.</p>
        </div>
      </div>
    </div>

    <div class="metrics">
      <div class="metric card"><div class="label">Users</div><div class="value">1,254</div></div>
      <div class="metric card"><div class="label">Recommendations</div><div class="value">3,890</div></div>
      <div class="metric card"><div class="label">Roadmaps</div><div class="value">25+</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Show sample radar
sample = {'Analytical Thinking': 4, 'Creativity':3.5, 'Communication':3, 'Leadership':2.5, 'Problem Solving':4}
st.plotly_chart(radar_chart(sample, 'Sample Aptitude'))
