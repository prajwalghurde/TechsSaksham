import streamlit as st
import google.generativeai as genai

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.error("🔴 API Key is missing! Please add it in Streamlit Secrets.")
    st.stop()  # Stop execution if key is missing

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")  # Use Gemini Pro model
        response = model.generate_content(user_input)
        return response.text  # Extract and return text response
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

st.title("AI Healthcare Chatbot 🏥🤖")
st.write("Ask me any health-related question!")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = get_gemini_response(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
