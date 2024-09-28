import streamlit as st
from llm_integration import get_diagnosis
from pdf_handler import handle_pdf_upload
import google.generativeai as genai
import os
import time
from google.api_core.exceptions import InternalServerError
import pdfplumber  # Add this import for PDF handling

# Set the page configuration
st.set_page_config(
    page_title="MediSenseAI",
    page_icon="🩺",
    layout="wide",
)

# Title of the app
st.title("🩺 MediSenseAI")

# Initialize session state for chat history
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

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

# Sidebar for chat history, new chat, and PDF upload
st.sidebar.title("Chat History")
if st.sidebar.button("New Chat"):
    if st.session_state.current_chat:
        st.session_state.chat_sessions.append(st.session_state.current_chat)
    st.session_state.current_chat = []

# Display chat sessions in the sidebar
if st.session_state.chat_sessions:
    for i, session in enumerate(st.session_state.chat_sessions):
        st.sidebar.write(f"Chat Session {i+1}")
        for message in session:
            st.sidebar.write(f"{'User' if message['is_user'] else 'Assistant'}: {message['message'][:20]}...")

# PDF upload button and analyze button
with st.sidebar.form(key='pdf_form'):
    uploaded_file = st.file_uploader("Upload PDF for Analysis", type=["pdf"])
    analyze_button = st.form_submit_button(label='Analyze PDF')

if analyze_button and uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        st.session_state.current_chat.append({"message": text, "is_user": True})
        with st.spinner("Analyzing PDF..."):
            response = get_gemini_response(text)
        st.session_state.current_chat.append({"message": response, "is_user": False})

# Input area for symptoms and follow-up questions
def send_message():
    user_input = st.session_state.input
    if user_input:
        st.session_state.current_chat.append({"message": user_input, "is_user": True})
        with st.spinner("Generating response..."):
            response = get_gemini_response(user_input)
        st.session_state.current_chat.append({"message": response, "is_user": False})
        st.session_state.input = ""

# Display current chat
if st.session_state.current_chat:
    for chat in st.session_state.current_chat:
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