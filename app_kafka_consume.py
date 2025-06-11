import json
from confluent_kafka import Consumer, KafkaError
from app_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from app_sentiment_analyzer import analyze_sentiment
from app_s3_storage import upload_to_s3
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def consume_messages():
    consumer = Consumer({
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "group.id": "text-processor",
        "auto.offset.reset": "earliest"
    })
    consumer.subscribe([KAFKA_TOPIC])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Consumer error: {msg.error()}")
                break
        text = msg.value().decode("utf-8")
        cache_key = f"sentiment:{hash(text)}"
        cached_result = redis_client.get(cache_key)
        if cached_result:
            result = json.loads(cached_result)
        else:
            result = analyze_sentiment(text)
            redis_client.setex(cache_key, 3600, json.dumps(result))
        upload_to_s3(text, result)

if __name__ == "__main__":
    consume_messages()