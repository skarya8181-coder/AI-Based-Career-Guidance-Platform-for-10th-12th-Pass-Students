import streamlit as st


def render():
    st.title('Scholarships')

    SCH = [
        {'name':'Merit Scholarship A','eligibility':'Top 10% in state board','amount':'50,000','deadline':'2026-09-30'},
        {'name':'Need-Based B','eligibility':'Family income < 5 LPA','amount':'30,000','deadline':'2026-12-31'},
    ]

    for s in SCH:
        st.subheader(s['name'])
        st.write('Eligibility:', s['eligibility'])
        st.write('Amount:', s['amount'])
        st.write('Deadline:', s['deadline'])
        st.markdown('---')
