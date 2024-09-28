import streamlit as st
from llm_integration import get_diagnosis
from pdf_handler import handle_pdf_upload
import google.generativeai as genai
import os
import time
from google.api_core.exceptions import InternalServerError

# Set the page configuration
st.set_page_config(
    page_title="Healthcare Symptom Checker",
    page_icon="🩺",
    layout="wide",
)

# Title of the app
st.title("🩺 Healthcare Symptom Checker")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to get response from Gemini API with retry mechanism
def get_gemini_response(prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    retries = 3
    for attempt in range(retries):
        try:
            response = model.generate_content([prompt])
            return response.text + "\n\nI'm not an expert. Please consult a doctor or physician near you."
        except InternalServerError as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise e

# Sidebar for chat history and new chat
st.sidebar.title("Chat History")
if st.sidebar.button("New Chat"):
    st.session_state.chat_history = []

if st.session_state.chat_history:
    for i, chat in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"Chat {i+1}: {chat['message'][:20]}...")

# Input area for symptoms and follow-up questions
def send_message():
    user_input = st.session_state.input
    if user_input:
        st.session_state.chat_history.append({"message": user_input, "is_user": True})
        with st.spinner("Generating response..."):
            response = get_gemini_response(user_input)
        st.session_state.chat_history.append({"message": response, "is_user": False})
        st.session_state.input = ""

# Display chat history
if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        with st.chat_message("user" if chat["is_user"] else "assistant"):
            st.markdown(chat["message"])

# Input box at the bottom with an arrow icon as the send button
st.markdown("""
    <style>
    .stTextInput {
        position: fixed;
        bottom: 3rem;
        width: calc(100% - 6rem);
    }
    .send-button {
        position: fixed;
        bottom: 3rem;
        right: 1rem;
        font-size: 2rem;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.text_input("Enter your symptoms or ask a follow-up question:", key="input", on_change=send_message)
st.markdown('<span class="send-button" onclick="document.querySelector(\'button[aria-label=Send]\').click()">➡️</span>', unsafe_allow_html=True)