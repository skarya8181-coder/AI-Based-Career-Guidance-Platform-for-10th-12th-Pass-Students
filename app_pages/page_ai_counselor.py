import streamlit as st
import openai


def render():
    st.title('AI Career Counselor')

    if 'history' not in st.session_state:
        st.session_state['history'] = []

    api_key = st.text_input('OpenAI API Key (optional)', type='password')
    question = st.text_input('Ask a career question', '')

    if st.button('Send') and question:
        st.session_state['history'].append({'role':'user','msg':question})
        if api_key:
            try:
                openai.api_key = api_key
                resp = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role':'system','content':'You are a helpful career counselor.'}]+[{'role':'user','content':question}], max_tokens=300)
                answer = resp.choices[0].message.content
            except Exception as e:
                answer = f"API error: {e}"
        else:
            q = question.lower()
            if 'stream' in q:
                answer = 'Choose a stream based on your strengths and interests. PCM for engineering, PCB for medical, commerce for CA/Business.'
            elif 'bca' in q:
                answer = 'BCA is good for software fundamentals; BTech offers deeper engineering exposure.'
            else:
                answer = 'Many paths exist — consider aptitude, interests, and budget. Try the aptitude test for personalized guidance.'
        st.session_state['history'].append({'role':'assistant','msg':answer})

    for m in st.session_state['history']:
        if m['role']=='user':
            st.markdown(f"**You:** {m['msg']}")
        else:
            st.markdown(f"**Counselor:** {m['msg']}")
