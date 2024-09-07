from streaming_pipeline import StreamingPipeline
from database_helper.db_manager import PostgresDataManager

if __name__ == "__main__":
    # Database configuration
    db_config = {
        'host': 'musicDB',
        'database': 'music_db',
        'port': '5432',
        'user': 'pyspark',
        'password': 'pyspark1234'
    }

    kafka_config = {
        'bootstrap_servers': 'kafka:9092'
    }

    db_manager = PostgresDataManager(db_config)

    # Create an instance of StreamingPipeline
    pipeline = StreamingPipeline(kafka_config, db_manager)

    try:
        pipeline.process_stream(topic="music_streaming_data")
    except Exception as e:
        print(f"Error running streaming pipeline: {e}")
    finally:
        db_manager.close()
