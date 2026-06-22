from typing import List
import streamlit as st
from utils.load_careers import load_careers


def render():
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">CareerPath AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">A modern AI-powered career guidance platform for 10th and 12th pass students.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-left:auto"><a class="btn btn-primary" href="#">Get Recommendations</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('\n')
    st.markdown('## Welcome to CareerPath AI')
    st.write('AI Career Recommendations — Get personalized career suggestions. Aptitude Test — Assess strengths across skills. College Finder — Filter colleges by state, budget, and type.')

    # Features
    st.markdown('---')
    careers = load_careers() or []
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown('### Features')
        st.write('- AI Career Recommendations')
        st.write('- Aptitude Test')
        st.write('- Career Explorer')
        st.write('- College Finder')
        st.write('- Roadmap Generator')
        st.write('- AI Career Counselor')
        if st.button('Start Aptitude Test'):
            st.session_state['navigate_to'] = 'Aptitude Test'
    with col2:
        st.markdown('### Stats')
        st.metric('Users','1,254')
        st.metric('Recommendations','3,890')

    st.markdown('---')
    st.markdown('### Sample Careers')
    for c in careers[:6]:
        st.markdown(f"**{c.get('name')}** — {c.get('overview')}")
        st.write(c.get('skills'))
        st.markdown('---')
