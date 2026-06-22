import streamlit as st
from utils.load_careers import load_careers


def render():
    st.title('Skill Gap Analyzer')
    careers = load_careers()
    career_names = [c['name'] for c in careers]
    if not career_names:
        st.info('No career data available yet')
        return
    selected = st.selectbox('Choose a career', career_names)
    user_skills = st.text_area('Your skills (comma separated)')

    if st.button('Analyze'):
        c = next((x for x in careers if x['name'] == selected), None)
        if not c:
            st.error('Career data not found')
            return
        required = set([s.lower() for s in c.get('skills', [])])
        have = set([s.strip().lower() for s in user_skills.split(',') if s.strip()])
        missing = required - have
        st.subheader('Skill gap')
        if missing:
            for m in missing:
                st.markdown(f'- **{m}** — Suggested course: Search on Coursera / Udemy')
        else:
            st.success('You have all core skills for this career (based on sample data)')
