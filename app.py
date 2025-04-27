import streamlit as st

st.header('현재 페이지에서 구현 예시')

# 탭으로 페이지 시뮬레이션
tab1, tab2, tab3 = st.tabs(["정보 입력", "선호도 설정", "정보 요약"])

# 초기화
if 'demo_user_data' not in st.session_state:
    st.session_state.demo_user_data = {
        'name': '',
        'age': 0,
        'preferences': []
    }

# 탭 1: 정보 입력
with tab1:
    st.subheader("사용자 정보 입력")
    st.session_state.demo_user_data['name'] = st.text_input(
        '이름', 
        value=st.session_state.demo_user_data['name'],
        key='demo_name'
    )
    st.session_state.demo_user_data['age'] = st.number_input(
        '나이', 
        value=st.session_state.demo_user_data['age'],
        key='demo_age'
    )

# 탭 2: 선호도 설정
with tab2:
    st.subheader("선호도 설정")
    st.session_state.demo_user_data['preferences'] = st.multiselect(
        '관심 분야를 선택하세요',
        ['데이터 과학', '웹 개발', '모바일 앱', '게임 개발', '인공지능'],
        default=st.session_state.demo_user_data['preferences'],
        key='demo_preferences'
    )

# 탭 3: 정보 요약
with tab3:
    st.subheader("사용자 정보 요약")
    
    if st.session_state.demo_user_data['name']:
        st.write(f"이름: {st.session_state.demo_user_data['name']}")
        st.write(f"나이: {st.session_state.demo_user_data['age']}")
        st.write("선호도:")
        if st.session_state.demo_user_data['preferences']:
            for pref in st.session_state.demo_user_data['preferences']:
                st.write(f"- {pref}")
        else:
            st.write("선택된 선호도가 없습니다.")
    else:
        st.info("먼저 정보 입력 탭에서 사용자 정보를 입력해주세요.")

# 세션 상태 초기화 방법
st.header('세션 상태 초기화')

if st.button('초기화하기'):
    # 특정 키만 초기화
    st.session_state.demo_user_data = {
        'name': '',
        'age': 0,
        'preferences': []
    }
    
    # 또는 전체 세션 상태 초기화
    # for key in list(st.session_state.keys()):
    #     del st.session_state[key]
    
    st.success('세션 상태가 초기화되었습니다.')
    st.rerun()  # 페이지 새로고침