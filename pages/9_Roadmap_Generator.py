import streamlit as st
from utils.roadmap_generator import get_roadmap

st.set_page_config(page_title='Roadmap Generator')

st.title('Roadmap Generator')

career = st.selectbox('Choose career', ['AI Engineer','Data Scientist','Software Engineer','Doctor'] + [f'Career Example {i}' for i in range(4,15)])

if st.button('Generate Roadmap'):
    roadmap = get_roadmap(career)
    for step in roadmap:
        st.markdown(f"- {step}")
