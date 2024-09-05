from producer import Producer

if __name__ == '__main__':
    # Kafka server configurations
    kafka_servers = ['kafka:9092']

    # Kafka topic to publish
    topic = 'music_streaming_data'

    data_generator = Producer(kafka_servers, topic)

    # Run the data generator every 0.1 seconds
    data_generator.run(interval=0.1)
