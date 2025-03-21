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
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🚫 API key not found. Please add GEMINI_API_KEY to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# ====================================
# 🎨 Page Config & Styling
# ====================================
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖", layout="centered")

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

st.title("💠 Welcome to Neurovia")
st.markdown(" Ask anything – powered by <b>Google Gemini 2.0 Flash")
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