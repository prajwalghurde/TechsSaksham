import streamlit as st
import google.generativeai as genai

# ✅ Step 1: Debug API Key
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    st.write("✅ API Key Loaded:", GEMINI_API_KEY[:5] + "******")  # Print partial key for security
else:
    st.error("❌ API Key is missing! Please add it in Streamlit Secrets.")
    st.stop()

# ✅ Step 2: Test Gemini API Connection
try:
    genai.configure(api_key=GEMINI_API_KEY)  # Apply the API key

    # ✅ Test a simple request
    model = genai.GenerativeModel(model_name="gemini-pro")
    test_response = model.generate_content("Hello!")  # Test call
    st.write("✅ Gemini API Test Response:", test_response.text)

except Exception as e:
    st.error(f"❌ API Configuration Failed: {e}")
    st.stop()
