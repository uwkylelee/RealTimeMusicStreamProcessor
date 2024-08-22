import time
import json
import random
from datetime import datetime
from typing import List, Dict, Any
from kafka import KafkaProducer
from faker import Faker


class Producer:
    def __init__(self, kafka_servers: List[str], topic: str) -> None:
        self.kafka_servers = kafka_servers
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.fake = Faker('ko_KR')

    def generate_base_music_streaming_data(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "user_id": random.randint(1, 1000),
            "track_id": random.randint(1, 50000),
            "timestamp": self.fake.date_time_this_month().isoformat()
        }
        return data

    def send_data(self, data: Dict[str, Any]) -> None:
        self.producer.send(self.topic, data)
        self.producer.flush()

    def run(self, interval: float = 1.0) -> None:
        try:
            while True:
                data = self.generate_base_music_streaming_data()
                print(f"Generate Music Streaming Data: {data}")
                self.send_data(data)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stop generating music streaming data.")
        finally:
            self.producer.close()


if __name__ == '__main__':
    kafka_servers = ['kafka:9092']  # Kafka 브로커 주소
    topic = 'music_streaming_data'  # 전송할 토픽 이름

    data_generator = Producer(kafka_servers, topic)
    data_generator.run(interval=1.0)  # 1초마다 데이터 생성
