import streamlit as st
from utils.career_data import CAREERS


def render():
    st.title('Career Explorer')

    query = st.text_input('Search careers (name, skill, keyword)')

    results = []
    if query:
        q = query.lower()
        results = [
            c
            for c in CAREERS
            if q in c['name'].lower()
            or any(q in s.lower() for s in c.get('keywords', []))
            or any(q in s.lower() for s in c.get('skills', []))
        ]
    else:
        results = CAREERS[:20]

    for c in results:
        st.subheader(c['name'])
        st.write(c['overview'])
        with st.expander('Details'):
            st.write('Eligibility:', c['eligibility'])
            st.write('Courses:', ', '.join(c.get('courses', [])))
            st.write('Entrance Exams:', ', '.join(c.get('entrance_exams', [])))
            st.write('Skills:', ', '.join(c.get('skills', [])))
            st.write('Salary:', c.get('salary'))
            st.write('Future:', c.get('future'))
        st.markdown('---')
