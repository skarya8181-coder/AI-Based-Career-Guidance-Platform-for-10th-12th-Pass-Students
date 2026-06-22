import streamlit as st

st.set_page_config(page_title='Entrance Exams')

st.title('Entrance Exams')

exams = {
    'JEE':{'eligibility':'12th PCM','pattern':'Physics, Chemistry, Math','tips':'Practice problem solving daily'},
    'NEET':{'eligibility':'12th PCB','pattern':'Biology, Physics, Chemistry','tips':'Strong fundamentals in biology'},
    'CUET':{'eligibility':'12th','pattern':'Subject specific','tips':'Practice previous papers'},
    'CLAT':{'eligibility':'12th','pattern':'English, GK, Logical Reasoning','tips':'Improve reading speed'},
    'NDA':{'eligibility':'12th','pattern':'Maths, General Ability','tips':'Physical fitness'},
    'CAT':{'eligibility':'Graduate','pattern':'VARC, DILR, QA','tips':'Timed mocks and fundamentals'},
}

tabs = st.tabs(list(exams.keys()))
for t, name in zip(tabs, list(exams.keys())):
    with t:
        e = exams[name]
        st.header(name)
        st.write('Eligibility:', e['eligibility'])
        st.write('Pattern:', e['pattern'])
        st.write('Preparation tips:', e['tips'])
