from google import genai
import streamlit as st
from dotenv import load_dotenv
import as

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)