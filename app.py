# ====================================
# 🔧 Imports
# ====================================
from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

# ====================================
# 🔐 API Setup
# ====================================
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GEMINI_API_KEY")  # Fetch Gemini API key

if not api_key:
    st.error("🚫 API key not found. Please add GEMINI_API_KEY to your .env file.")
    st.stop()

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# ====================================
# 🖥️ Streamlit Page Config
# ====================================
st.set_page_config(page_title="Gemini AI Chat", page_icon="🤖", layout="centered")

# ====================================
# 🧠 App UI
# ====================================
st.title("🤖 Gemini AI Assistant")
st.markdown(
    """
    Ask anything and get an intelligent response powered by **Google Gemini 2.0 Flash**.  
    Built with ❤️ by NOOR UL NISA.
    """
)

# ====================================
# ✍️ Prompt Input
# ====================================
with st.form("gemini_form"):
    prompt = st.text_area(
        "💬 Enter your prompt:",
        height=150,
        placeholder="e.g. What is quantum computing?"
    )
    submitted = st.form_submit_button("🚀 Generate Response")

# ====================================
# ⚙️ Handle Form Submission
# ====================================
if submitted:
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                # Generate content from Gemini
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )

                # ====================================
                # 📤 Show the Response
                # ====================================
                st.markdown("### 🧠 Gemini's Response")
                st.success(response.text)

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
