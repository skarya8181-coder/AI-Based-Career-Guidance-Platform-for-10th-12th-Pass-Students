import streamlit as st
from utils.career_data import CAREERS
from utils.charts import salary_bar


def render():
    st.title('Salary Insights')

    choices = st.multiselect('Select careers to compare', [c['name'] for c in CAREERS[:12]], default=[CAREERS[0]['name'], CAREERS[1]['name']])
    selected = [c for c in CAREERS if c['name'] in choices]
    if selected:
        data = []
        for c in selected:
            data.append({'career':c['name'], 'freshers':c['salary']['freshers'], 'avg':c['salary']['avg'], 'experienced':c['salary']['experienced']})
        st.plotly_chart(salary_bar(data))
    else:
        st.info('Select at least one career to visualize salary insights')
