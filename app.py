import streamlit as st
import google.generativeai as genai

# Securely fetch API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["AIzaSyCu7kmVCQuMJPa_O0Gko4Z6WgynH1qo-w8"]
genai.configure(api_key=GEMINI_API_KEY)

# Function to get response from Gemini API
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")  # Correct model
        response = model.generate_content(user_input)
        return response.text  # Extract and return text response
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit App UI
st.title("AI Healthcare Chatbot 🏥🤖")
st.write("Ask me any health-related question!")

# Chat history for better UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI Response
    response = get_gemini_response(user_input)

    # Display AI Response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
