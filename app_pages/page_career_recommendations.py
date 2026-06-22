import streamlit as st
from utils.career_data import CAREERS
from utils.recommendation_engine import recommend


def render():
    st.title('Career Recommendations')

    with st.form('rec'):
        cls = st.selectbox('Class', ['10th', '12th'])
        stream = st.selectbox('Stream', ['Science PCM', 'Science PCB', 'Commerce', 'Arts', 'Other'])
        marks = st.number_input('Percentage / Marks (0-100)', min_value=0.0, max_value=100.0, value=70.0)
        interests = st.text_area('Interests (comma separated)', value='programming, data')
        skills = st.text_area('Skills (comma separated)', value='python')
        budget = st.selectbox('Budget', ['Low', 'Medium', 'High'])
        submitted = st.form_submit_button('Generate')

    if submitted:
        profile = {
            'class': cls,
            'stream': stream,
            'marks': marks,
            'interests': interests,
            'skills': skills,
            'budget': budget,
            'aptitude': st.session_state.get('aptitude_result', {}),
        }
        recs = recommend(CAREERS, profile, top_k=8)
        for r in recs:
            st.markdown(f"### {r['name']} — {r.get('match_percentage', 0)}% match")
            st.write(r.get('overview'))
            st.write('Required skills:', ', '.join(r.get('skills', [])))
            st.write('Future:', r.get('future'))
            st.write('Average salary:', r.get('salary', {}).get('avg'))
            st.markdown('---')
