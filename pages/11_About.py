import streamlit as st

st.set_page_config(page_title='About')

st.markdown("""
<div class="card about-section">
  <div class="about-grid">
    <div>
      <h1 style="margin:0;color:#0f172a">About CareerPath AI</h1>
      <p style="color:var(--muted)">CareerPath AI is designed to help students make informed career choices by combining aptitude profiling, sample data and recommendation logic. The platform is lightweight and built with Streamlit for fast iteration.</p>

      <h3 style="margin-top:1rem">Mission</h3>
      <p class="small-muted">Help students make informed career choices.</p>

      <h3>Vision</h3>
      <p class="small-muted">Democratize career guidance using AI and data.</p>

      <h3>Future Roadmap</h3>
      <ul>
        <li>Connect to richer college datasets and APIs</li>
        <li>Improve AI Counselor with OpenAI integration and context</li>
        <li>Deploy to Streamlit Cloud with CI/CD</li>
      </ul>
    </div>
    <div>
      <div class="card">
        <h4 style="margin:0">Statistics</h4>
        <div style="margin-top:0.5rem">
          <p style="margin:0"><strong>Users:</strong> 1,254</p>
          <p style="margin:0"><strong>Recommendations:</strong> 3,890</p>
          <p style="margin:0"><strong>Roadmaps:</strong> 25+</p>
        </div>
      </div>

      <div class="card" style="margin-top:1rem">
        <h4 style="margin:0">Developer</h4>
        <p style="margin:0;color:var(--muted)">skarya8181-coder</p>
        <p style="margin-top:0.5rem;color:var(--muted)">Contact: update README with your preferred contact method.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
