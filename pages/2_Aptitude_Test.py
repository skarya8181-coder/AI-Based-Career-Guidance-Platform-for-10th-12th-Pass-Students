import streamlit as st
from utils.helper import save_aptitude_result
from utils.charts import radar_chart


def render():
    st.title('Aptitude Test')

    questions = [
        ("I enjoy solving logical puzzles.", 'Analytical Thinking'),
        ("I like designing things (UI, posters, products).", 'Creativity'),
        ("I can explain complex ideas simply.", 'Communication'),
        ("I often take lead in group work.", 'Leadership'),
        ("I enjoy debugging technical problems.", 'Problem Solving'),
    ]
    # Duplicate to make 15 questions
    q_list = questions * 3

    if 'answers' not in st.session_state:
        st.session_state['answers'] = [3] * len(q_list)

    with st.form('aptitude'):
        st.progress(0)
        for i, (q, cat) in enumerate(q_list):
            st.slider(f"Q{i+1}. {q}", min_value=1, max_value=5, value=st.session_state['answers'][i], key=f'q{i}')
        submitted = st.form_submit_button('Submit')

    if submitted:
        # compute category averages
        cats = {}
        for i, (q, cat) in enumerate(q_list):
            cats.setdefault(cat, []).append(st.session_state[f'q{i}'])
        scores = {k: round(sum(v) / len(v), 2) for k, v in cats.items()}
        st.success('Test completed')
        st.write('Scores: ', scores)
        save_aptitude_result(scores)
        st.plotly_chart(radar_chart(scores, 'Your Aptitude'))

        # classify
        top = max(scores.items(), key=lambda x: x[1])[0]
        st.info(f'Predicted personality: {top}')
