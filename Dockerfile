FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
COPY chatbot/backend/requirements.txt ./chatbot_requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r chatbot_requirements.txt

# Copy application code
COPY app.py .
COPY chatbot/ ./chatbot/

# Set working directory to project root
WORKDIR /app

# Expose port
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
