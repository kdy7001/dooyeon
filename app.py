import openai
import streamlit as st

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"  # 반드시 자신의 OpenAI API 키로 교체하세요.

# Streamlit 앱 설정
st.title("ChatGPT 챗봇")
st.write("이 웹앱은 OpenAI API를 사용하여 사용자와 대화할 수 있는 챗봇입니다.")

# 사용자 입력 받기
user_input = st.text_input("질문이나 지시를 입력하세요:", "")

# ChatGPT 응답 출력
if st.button("응답 생성하기"):
    if user_input:
        with st.spinner("응답 생성 중..."):
            try:
                # OpenAI API를 이용한 응답 생성
                response = openai.Completion.create(
                    engine="text-davinci-003",  # 원하는 모델 선택
                    prompt=user_input,
                    max_tokens=150,
                    temperature=0.7
                )
                chatgpt_response = response.choices[0].text.strip()
                
                # 응답 출력
                st.success("ChatGPT의 응답:")
                st.write(chatgpt_response)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("먼저 입력을 제공해주세요!")

# 하단 설명 추가
st.markdown("---")
st.caption("이 웹 앱은 OpenAI의 GPT 모델을 사용하여 만들어졌습니다.")
