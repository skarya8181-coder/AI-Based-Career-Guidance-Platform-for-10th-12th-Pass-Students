import streamlit as st
from utils.helper import save_aptitude_result
from utils.charts import radar_chart

st.set_page_config(page_title="Home - CareerPath AI", layout='wide')

st.markdown("# CareerPath AI")
st.markdown("A friendly platform to help 10th and 12th pass students choose the right career.")

col1, col2 = st.columns([2,1])
with col1:
    st.markdown("## Features")
    st.write("- AI Career Recommendations\n- Aptitude Test\n- Career Explorer\n- College Finder\n- Roadmap Generator\n- AI Career Counselor")
    st.button('Start Aptitude Test', key='home_start')
with col2:
    st.markdown('## Statistics')
    st.metric('Users', '1,254')
    st.metric('Recommendations generated', '3,890')

st.markdown('---')

# Show sample radar
sample = {'Analytical Thinking': 4, 'Creativity':3.5, 'Communication':3, 'Leadership':2.5, 'Problem Solving':4}
st.plotly_chart(radar_chart(sample, 'Sample Aptitude'))
