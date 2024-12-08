import os
import markdown
import streamlit as st
# from dotenv import load_dotenv
import google.generativeai as genai


# load_dotenv()
API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash') 
# subject = "AI"

# print(markdown.markdown(response.text))
st.title("인공지능 시인")
subject =st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제: " + subject)
if st.button("시 작성"):
    with st.spinner("시 작성중..."):
        response = model.generate_content(subject + "에 대한 시를 써줘")  
        st.write(response.text)

