import streamlit as st


def render():
    st.title('College Finder')

    COLLEGES = [
        {'name':'Government Engineering College A','state':'State A','city':'City A','fees':50000,'type':'Government','rating':4.1,'placement':600000,'courses':['B.Tech CS','B.Tech ME']},
        {'name':'Private Institute B','state':'State B','city':'City B','fees':150000,'type':'Private','rating':3.8,'placement':400000,'courses':['BCA','BBA']},
    ]

    state = st.selectbox('State', ['All','State A','State B'])
    city = st.selectbox('City', ['All','City A','City B'])
    budget = st.selectbox('Budget', ['Any','Low (<50k)','Medium (50k-150k)','High (>150k)'])
    ctype = st.selectbox('Type', ['All','Government','Private'])

    filtered = COLLEGES
    if state!='All':
        filtered = [c for c in filtered if c['state']==state]
    if city!='All':
        filtered = [c for c in filtered if c['city']==city]
    if ctype!='All':
        filtered = [c for c in filtered if c['type']==ctype]
    if budget!='Any':
        if 'Low' in budget:
            filtered = [c for c in filtered if c['fees']<50000]
        if 'Medium' in budget:
            filtered = [c for c in filtered if 50000<=c['fees']<=150000]
        if 'High' in budget:
            filtered = [c for c in filtered if c['fees']>150000]

    for c in filtered:
        st.markdown(f"**{c['name']}** — {c['type']} | {c['state']} | {c['city']}")
        st.write('Fees:', c['fees'], 'Rating:', c['rating'], 'Avg Placement:', c['placement'])
        st.write('Courses:', ', '.join(c['courses']))
        st.markdown('---')
