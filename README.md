AI Healthcare Chatbot 🏥🤖

Overview

This AI Healthcare Chatbot is built using Python, Streamlit, and Google's Gemini API. It allows users to ask health-related questions and receive AI-generated responses in real-time.

Features:

💬 Conversational Interface: Simple and user-friendly chat-based interaction.

🔍 AI-Powered Responses: Uses Google's Gemini API to provide health-related insights.

⚡ Fast and Lightweight: Built with Streamlit for a smooth and interactive UI.

🔒 Secure API Integration: Uses environment variables for API key management.

File Structure

AI_Healthcare_Bot/
│── .venv/                # Virtual environment (optional)
│── app.py                # Main Streamlit app
│── config.py             # API key configuration
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── .gitignore            # Ignore unnecessary files

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/AI_Healthcare_Bot.git
cd AI_Healthcare_Bot

2️⃣ Create and Activate Virtual Environment (Recommended)

python -m venv venv
# Activate venv (Windows)
venv\Scripts\activate
# Activate venv (Mac/Linux)
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up API Key

Create a config.py file and add your Google Gemini API key:

GEMINI_API_KEY = "your-api-key-here"

5️⃣ Run the Chatbot

streamlit run app.py

After running the command, the chatbot will be accessible at:

Local URL: http://localhost:8501

Usage

1️⃣ Open the chatbot in a web browser.
2️⃣ Type your health-related query in the text box.
3️⃣ Click Ask to get an AI-generated response.
4️⃣ Read the response in the chat interface.

Troubleshooting

🔹 Invalid API Key Error? Ensure you have set a valid Google Gemini API key in config.py.

🔹 Module Not Found? Run pip install -r requirements.txt.

🔹 Virtual Environment Not Activating? Use Set-ExecutionPolicy Unrestricted -Scope Process (for Windows PowerShell).

Future Enhancements

✅ Voice-based input/output

✅ Integration with a medical knowledge database

✅ UI enhancements for better user experience

Contributing

Feel free to contribute! Fork this repo, make your changes, and submit a pull request.