import streamlit as st
import google.generativeai as genai

# ✅ STEP 1: SECURELY FETCH API KEY
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]  # ✅ Correct way!
else:
    st.error("🔴 API Key is missing! Please add it in Streamlit Secrets.")
    st.stop()

# ✅ STEP 2: CONFIGURE GEMINI API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ STEP 3: FUNCTION TO GET RESPONSE FROM GEMINI API
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(user_input)
        return response.text  
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# ✅ STEP 4: STREAMLIT APP UI
st.title("💡 AI Healthcare Chatbot 🏥🤖")
st.write("💬 *Ask me any health-related question!*")

# ✅ STEP 5: MAINTAIN CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! How can I help you with healthcare queries today?"}
    ]

# ✅ STEP 6: DISPLAY CHAT HISTORY
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ STEP 7: HANDLE USER INPUT
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": f"🧑‍💻 **You:** {user_input}"})

    # ✅ GET AI RESPONSE
    response = get_gemini_response(user_input)

    # ✅ DISPLAY AI RESPONSE
    with st.chat_message("assistant"):
        st.markdown(f"🤖 **AI:** {response}")

    # ✅ STORE RESPONSE IN CHAT HISTORY
    st.session_state.messages.append({"role": "assistant", "content": f"🤖 **AI:** {response}"})
