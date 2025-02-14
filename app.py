import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

# Set up Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_input):
    model = genai.GenerativeModel(model_name="gemini-pro")  
    response = model.generate_content(user_input)
    return response.text 

# Streamlit UI
st.title("AI Healthcare Chatbot 🏥🤖")
st.write("Ask me any health-related question!")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input:
        response = get_gemini_response(user_input)
        st.text_area("Bot:", value=response, height=1000, disabled=True)
