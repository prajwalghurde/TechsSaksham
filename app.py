import streamlit as st
import google.generativeai as genai
import os

# ✅ STEP 1: DEBUG STREAMLIT SECRETS
st.write("🔍 Debugging Secrets:", dict(st.secrets))

# ✅ STEP 2: FETCH API KEY (FIRST TRY ST.SEARCHES, THEN FALLBACK TO ENV VAR)
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not GEMINI_API_KEY:
    st.error("❌ API Key is missing! Please add it in Streamlit Secrets or as an environment variable.")
    st.stop()

# ✅ STEP 3: CONFIGURE GEMINI API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ STEP 4: FUNCTION TO GET RESPONSE
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(user_input)
        return response.text  
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# ✅ STEP 5: STREAMLIT APP UI
st.title("💡 AI Healthcare Chatbot 🏥🤖")
st.write("💬 *Ask me any health-related question!*")

# ✅ STEP 6: CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hi! How can I help you today?"}]

# ✅ STEP 7: DISPLAY CHAT HISTORY
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ STEP 8: HANDLE USER INPUT
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": f"🧑‍💻 **You:** {user_input}"})

    # ✅ GET AI RESPONSE
    response = get_gemini_response(user_input)

    # ✅ DISPLAY AI RESPONSE
    with st.chat_message("assistant"):
        st.markdown(f"🤖 **AI:** {response}")

    st.session_state.messages.append({"role": "assistant", "content": f"🤖 **AI:** {response}"})
