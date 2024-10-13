# MediSenseAI
## Project Overview

The **Healthcare Symptom Checker & Recommendation System** is a web application designed to provide users with personalized health advice based on their symptoms or medical report submissions. The application uses advanced AI models, including **Gemini API 1.5 Flash** and Replicate API, to analyze symptoms and medical history, providing potential diagnoses and action recommendations. It also suggests nearby hospitals or pharmacies using Google Maps API and stores query history for future reference.

This project is built with the following stack:
- **Backend**: Flask (Python)
- **Frontend**: React.js (JavaScript)
- **AI Integration**: Streamlit (Python), Replicate API, Gemini API 1.5 Flash
- **Database**: MongoDB Atlas
- **Location Services**: Google Maps API

---

## Features

- Symptom input through a chat interface.
- Medical report analysis via PDF uploads.
- AI-powered diagnosis and recommendations using Replicate API and Gemini API 1.5 Flash.
- Query history display for future reference.
- Nearby hospital and pharmacy recommendations using Google Maps API.
- Secure storage of medical history and queries using MongoDB Atlas.

---

## Project Structure

```plaintext
health-chatbot-app/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   │   ├── llm_analyzer.py          # Handles LLM-based diagnosis logic.
│   │   │   ├── symptom_analyzer.py      # Processes symptom input.
│   │   │   ├── database.py              # Handles MongoDB operations.
│   │   │   └── config.py                # Configures environment variables and API keys.
│   │   ├── models/
│   │   ├── routes.py                    # API routes for Flask backend.
│   │   ├── wsgi.py                      # Flask WSGI entry point.
│   │   └── Dockerfile                   # Docker config for backend.
│   ├── requirements.txt                 # Backend dependencies.
│   ├── venv/                            # Virtual environment for the backend.
├── frontend/
│   ├── components/
│   │   ├── ChatBox.js                   # Chat component for user input.
│   │   ├── QueryHistory.js              # Displays query history.
│   ├── pages/
│   │   └── index.js                     # Main frontend entry point.
│   ├── package.json                     # Frontend dependencies.
│   └── Dockerfile                       # Docker config for frontend.
├── streamlit_app/
│   ├── app.py                           # Main Streamlit app for AI interactions.
│   ├── llm_integration.py               # LLM interaction logic using Replicate API and Gemini API.
│   ├── streamlit.toml                   # Streamlit configuration for API keys.
│   ├── requirements.txt                 # Streamlit dependencies.
│   ├── Dockerfile                       # Docker config for Streamlit app.
│   └── venv/                            # Virtual environment for the Streamlit app.
├── database/
│   ├── db_config.py                     # MongoDB Atlas connection config.
├── config/
│   ├── google_maps.py                   # Google Maps API configuration.
│   ├── api_keys.py                      # Manages API keys.
├── tests/
│   ├── test_backend.py                  # Unit tests for backend functionality.
│   ├── test_streamlit.py                # Unit tests for Streamlit app.
├── .env                                 # Environment variables for sensitive data.
├── docker-compose.yml                   # Docker Compose configuration for multi-service deployment.
└── README.md                            # Project documentation (this file).
```
