# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Producer script
COPY src/ .

# Command to run the producer
CMD ["python3", "main.py"]
