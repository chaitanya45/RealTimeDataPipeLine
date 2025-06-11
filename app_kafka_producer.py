from confluent_kafka import Producer
from app_config import KAFKA_BOOTSTRAP_SERVERS

def produce_message(topic, message):
    producer = Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})
    producer.produce(topic, value=message.encode("utf-8"))
    producer.flush()