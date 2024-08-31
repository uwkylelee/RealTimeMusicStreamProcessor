from streaming_pipeline import StreamingPipeline

# Database configuration
db_config = {
    'host': 'musicDB',
    'database': 'music_db',
    'port': '5432',
    'user': 'pyspark',
    'password': 'pyspark1234'
}

if __name__ == "__main__":
    # Kafka topic to subscribe
    topic = "music_streaming_data"

    # Create an instance of StreamingPipeline
    pipeline = StreamingPipeline(db_config)

    # Run the streaming pipeline
    pipeline.run(topic)
