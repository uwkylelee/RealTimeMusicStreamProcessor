import time
import json
from typing import List, Dict, Any
from kafka import KafkaProducer

from fake_track_event_generator import FakeTrackEventGenerator


class Producer:
    def __init__(self, kafka_servers: List[str], topic: str) -> None:
        self.kafka_servers = kafka_servers
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.fake_track_event_generator = FakeTrackEventGenerator()

    def send_data(self, data: Dict[str, Any]) -> None:
        self.producer.send(self.topic, data)
        self.producer.flush()

    def run(self, interval: float = 1.0) -> None:
        try:
            while True:
                data = self.fake_track_event_generator.generate_event()
                print(f"Generate Music Streaming Data: {data}")
                self.send_data(data)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stop generating music streaming data.")
        finally:
            self.producer.close()
