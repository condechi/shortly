# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (Cloud Run expects port 8080)
EXPOSE 8080

# Run Gunicorn via shell form so $PORT is expanded from environment.
ENTRYPOINT ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} run:app"]