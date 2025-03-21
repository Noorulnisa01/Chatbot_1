# ====================================
# 🔧 Imports
# ====================================
import google.generativeai as genai # Google Gemini API

import streamlit as st
from dotenv import load_dotenv
import os

# ====================================
# 🔐 API Setup
# ====================================
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🚫 API key not found. Please add GEMINI_API_KEY to your .env file.")
    st.stop()

client = genai.configure(api_key=api_key)

# ====================================
# 🎨 Page Config & Styling
# ====================================
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖", layout="centered")

st.markdown("""
<style>

/* ===========================
🌌 Matching Background - Sidebar & Main
=========================== */
.stApp {
    background: linear-gradient(-45deg, #1b0044, #280659, #7209b7, #00b4d8, #5e60ce);
    background-size: 600% 600%;
    animation: crystalFlow 30s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

/* Crystal gradient animation */
@keyframes crystalFlow {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

/* ===========================
💠 Sidebar Background Style
=========================== */
section[data-testid="stSidebar"] {
    background: rgba(0, 0, 50, 0.6);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    color: #ffffff;
    border-right: 2px solid rgba(255, 255, 255, 0.2);
}

/* Sidebar text styling */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p {
    color: #ffffff !important;
}

/* ===========================
🎯 Sidebar Button Styling
=========================== */
button[data-testid="baseButton-header"] {
    background-color: #00b4d8;
    color: white;
    border-radius: 8px;
    padding: 0.3rem 0.7rem;
    border: none;
    font-weight: bold;
    box-shadow: 0 4px 12px rgba(0, 180, 216, 0.4);
    transition: 0.3s ease-in-out;
    z-index: 9999;
}

button[data-testid="baseButton-header"]:hover {
    background-color: #0096c7;
    transform: scale(1.08);
}

/* Ensure button is visible in all themes */
button[title="Main menu"] svg {
    stroke: white;
    width: 20px;
    height: 20px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar info panel
with st.sidebar:
    st.markdown("## 💠 Neurovia AI")
    st.markdown("Your intelligent crystal-mind assistant ✨")

    st.markdown("### 🧠 Powered By")
    st.markdown("""
    - 🧊 **Google Gemini 2.0 Flash**
    - ⚙️ Streamlit for UI
    - 🔐 Secure with .env API key
    - 🌐 Python-based backend
    """)

    st.markdown("### 💡 What It Can Do")
    st.markdown("""
    - 📖 Explain complex topics clearly  
    - 💬 Answer questions in real-time  
    - 🪄 Creative writing & brainstorming  
    - 🧮 Solve math & logic problems  
    - 🌍 Summarize articles or websites
    """)

    st.markdown("### 🔍 Tips for Best Use")
    st.markdown("""
    - ✅ Ask specific questions  
    - 📝 Use full sentences  
    - ⏳ Wait for responses if slow  
    - 🤝 Try follow-up prompts
    """)

    st.markdown("---")
    st.markdown("👤 *Created by Noor Ul Nisa*")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/noor-ul-nisa-a10738356/)")

# ====================================
# Background and styling
st.markdown("""
<style>

@keyframes crystalFlow {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* 🌌 Crystal Flowing Background */
.stApp {
    background: linear-gradient(-45deg, #1b0044, #280659, #7209b7, #00b4d8, #5e60ce);
    background-size: 600% 600%;
    animation: crystalFlow 30s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

/* 💠 Glassmorphism Container */
.main-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 2rem;
    margin-top: 2rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

/* 🌗 Text Colors Adapt to Theme */
@media (prefers-color-scheme: light) {
    h1, h2, h3, h4, h6, p, label, .stMarkdown {
        color: #000000 !important;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
}

@media (prefers-color-scheme: dark) {
    h1, h2, h3, h4, h6, p, label, .stMarkdown {
        color: #ffffff !important;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #ffffffcc !important;
        color: #000000 !important;
    }
}

/* 🌟 Button Glow */
.stButton>button {
    background-color: #ff4c98;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 4px 20px rgba(255, 76, 152, 0.4);
}

.stButton>button:hover {
    background-color: #d63384;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)




# ====================================
# 🧠 Header
# ====================================


st.markdown("<h1 style='text-align: center;'>🤖 Neurovia AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your intelligent, glowing AI companion — powered by Gemini & crafted with magic 💫</b></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #eeeeee;'>Built with ❤️ by Noor Ul Nisa</p>", unsafe_allow_html=True)

st.title("✨ Chat with Neurovia ")
st.markdown(" Ask anything – powered by Google Gemini 2.0 Flash")
# ====================================
# ✍️ Main Container
# ====================================
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    

    # Your input + form here...

    st.markdown('</div>', unsafe_allow_html=True)


    with st.form("gemini_form"):
        st.markdown("#### ✨ Quick Prompt")
        prompt = st.text_area("💬 Enter your prompt:", height=150, placeholder="e.g. What is quantum computing?")
        submitted = st.form_submit_button("🚀 Generate Response")

    if submitted:
        if not prompt.strip():
            st.warning("⚠️ Please enter a prompt.")
        else:
            with st.spinner("Thinking... 🤔"):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt
                    )
                    st.markdown("### 🧠 Gemini's Response")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")

    # Real-time extra question
    st.markdown("#### 🔍 Ask More")
    user_query = st.text_input("Type your question...")

    if user_query:
        with st.spinner("Generating response..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_query
                )
                message = response.text
                st.markdown("### 💬 AI Says:")
                st.info(message)
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.caption("👆 Try asking something like: *What is the future of AI?*")

    st.markdown('</div>', unsafe_allow_html=True)

# ====================================
# 🔚 Footer
# ====================================
st.markdown("<hr style='border-top: 1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #dddddd;'>✨ Powered by Google Gemini | UI crafted by Noor Ul Nisa</p>",
    unsafe_allow_html=True
)



# User input
user_query = st.text_input("Ask me anything...")

# Generate response
if user_query:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=user_query
    )
    message = response.text
    st.write("### AI Response: ")
    st.write(message)

else:
    st.warning("Please enter a query to get a response.")