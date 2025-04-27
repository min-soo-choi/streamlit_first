import streamlit as st

if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': '',
        'age': 0,
        'preferences': []
    }

st.title('사용자 정보 입력')
st.session_state.user_data['name'] = st.text_input('이름', st.session_state.user_data['name'])
st.session_state.user_data['age'] = st.number_input('나이', value=st.session_state.user_data['age'])
