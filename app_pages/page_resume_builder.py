import streamlit as st
from services.resume_builder import generate_basic_resume_pdf


def render():
    st.title('Resume Builder')
    name = st.text_input('Full name')
    education = st.text_area('Education (brief)')
    skills = st.text_area('Skills (comma separated)')

    if st.button('Generate PDF'):
        if not name:
            st.error('Please enter your name')
        else:
            skills_list = [s.strip() for s in skills.split(',') if s.strip()]
            pdf_bytes = generate_basic_resume_pdf(name, education, skills_list)
            st.download_button('Download Resume (PDF)', data=pdf_bytes, file_name=f'{name}_resume.pdf', mime='application/pdf')
