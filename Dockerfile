FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (optional, if any packages need it)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     && rm -rf /var/lib/apt/lists/*

# Copy requirements first (layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Copy the trained model
COPY ml/models/ ./ml/models/

# Expose the API port
EXPOSE 8000

# Run the API. Uses $PORT if set (Render, K8s), else 8000
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}