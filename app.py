import streamlit as st
import google.generativeai as genai

# ✅ Step 1: Fetch API Key Securely
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]  # ✅ Correct way!
else:
    st.error("❌ API Key is missing! Please add it in Streamlit Secrets.")
    st.stop()

# ✅ Step 2: Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Step 3: Function to Get Response from Gemini API
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(user_input)
        return response.text  
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# ✅ Step 4: Streamlit UI
st.title("💡 AI Healthcare Chatbot 🏥🤖")
st.write("💬 *Ask me any health-related question!*")

# ✅ Step 5: Maintain Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! How can I help you with healthcare queries today?"}
    ]

# ✅ Step 6: Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ Step 7: Handle User Input
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": f"🧑‍💻 **You:** {user_input}"})

    # ✅ Get AI Response
    response = get_gemini_response(user_input)

    # ✅ Display AI Response
    with st.chat_message("assistant"):
        st.markdown(f"🤖 **AI:** {response}")

    # ✅ Store Response in Chat History
    st.session_state.messages.append({"role": "assistant", "content": f"🤖 **AI:** {response}"})
