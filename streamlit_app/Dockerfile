# Streamlit Dockerfile

# Use a Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy streamlit code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
