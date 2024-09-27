import os
import logging
import streamlit as st
import google.generativeai as ggi
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_symptoms(symptoms: str) -> bool:
    if not symptoms or not isinstance(symptoms, str):
        logger.warning("Invalid symptoms input.")
        return False
    if len(symptoms.strip()) < 5:
        logger.warning("Symptoms input is too short.")
        return False
    return True

def initialize_gemini_api():
    api_key = st.secrets["GOOGLE_API_KEY"]
    ggi.configure(api_key=api_key)

def get_diagnosis(symptoms: str) -> Optional[str]:
    if not validate_symptoms(symptoms):
        st.error("Invalid symptoms input. Please provide more detailed symptoms.")
        return None

    try:
        initialize_gemini_api()
        model = ggi.GenerativeModel(model_name="gemini-1.5-flash")
        chat = model.start_chat()
        logger.info(f"Generating diagnosis for symptoms: {symptoms}")
        response = chat.send_message(symptoms)
        logger.info("Diagnosis generated successfully.")
        return response.text
    except Exception as e:
        logger.error(f"Error during diagnosis generation: {e}")
        st.error("An error occurred while generating the diagnosis.")
        return None