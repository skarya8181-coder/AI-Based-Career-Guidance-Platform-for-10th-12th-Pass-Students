import streamlit as st


def save_aptitude_result(result):
    st.session_state['aptitude_result'] = result


def get_session_user():
    return st.session_state.get('user', {'name': 'Guest'})
