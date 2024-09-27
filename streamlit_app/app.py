import streamlit as st
from llm_integration import get_diagnosis

st.title("Healthcare Symptom Checker")

symptoms = st.text_area("Enter your symptoms:")
if st.button("Analyze"):
    result = get_diagnosis(symptoms)
    st.write("Diagnosis:", result)
