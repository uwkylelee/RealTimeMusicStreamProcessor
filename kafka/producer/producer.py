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
        self.hashtags = ['#데이터', '#AI', '#빅데이터', '#Kafka', '#Python', '#프로젝트',
                         '#개발자', '#기술']

    def generate_social_media_data(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            'user_id': self.fake.user_name(),
            'timestamp': datetime.utcnow().isoformat(),
            'message': self.fake.sentence(nb_words=10),
            'likes': random.randint(0, 1000),
            'comments': random.randint(0, 500),
            'shares': random.randint(0, 200),
            'hashtags': random.sample(self.hashtags, random.randint(1, 3))
        }
        return data

    def send_data(self, data: Dict[str, Any]) -> None:
        self.producer.send(self.topic, data)
        self.producer.flush()

    def run(self, interval: float = 1.0) -> None:
        try:
            while True:
                data = self.generate_social_media_data()
                print(f"생성된 소셜 미디어 데이터: {data}")
                self.send_data(data)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("데이터 생성기를 종료합니다.")
        finally:
            self.producer.close()


if __name__ == '__main__':
    kafka_servers = ['kafka:9092']  # Kafka 브로커 주소
    topic = 'social_media_data'  # 전송할 토픽 이름

    data_generator = Producer(kafka_servers, topic)
    data_generator.run(interval=1.0)  # 1초마다 데이터 생성
