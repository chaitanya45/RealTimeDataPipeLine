from flask import Flask, request, jsonify
from app_kafka_producer import produce_message
from app_config import KAFKA_TOPIC

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "Text is required"}), 400
    produce_message(KAFKA_TOPIC, text)
    return jsonify({"message": "Data sent to Kafka"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)