# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy Spark Streaming script
COPY streaming.py db_writer.py .

# Command to run Spark job
CMD ["python", "streaming.py"]
