import streamlit as st

# 1. 제목 넣기
st.title("나의 첫 번째 스트림릿 테스트 앱 ")

# 2. 버튼 만들기
if st.button("클릭해보세요"):
    st.write("짜잔! 버튼이 눌렸습니다! ")

# 3. 텍스트 입력받기
user_input = st.text_input("당신의 이름은?")
if user_input:
    st.write(f"반가워요, {user_input}님!")