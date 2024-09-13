FROM bitnami/spark:3.5.0

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source Code
COPY src/ .

# Set environment variables
ENV SPARK_HOME=/opt/bitnami/spark
ENV PYSPARK_PYTHON=python3

# Run the application
CMD [ "spark-submit", \
"--master", "spark://spark-master:7077", \
"--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0", \
"main.py", "--topic", "music_streaming_data", "--app", "streaming"]
