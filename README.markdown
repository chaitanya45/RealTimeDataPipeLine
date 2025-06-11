# Real-Time Data Processing Pipeline

A Python-based pipeline for real-time data streaming and processing using Apache Kafka, Flask, and Hugging Face Transformers for sentiment analysis. Stores results in AWS S3, uses Redis for caching, and deploys on Kubernetes.

## Setup
1. Install Python 3.11, Docker, and Kubernetes (minikube).
2. Configure AWS CLI with S3 access.
3. Set up Kafka and Redis.
4. Install dependencies: `pip install -r requirements.txt`.
5. Update `app/config.py` with Kafka, Redis, and S3 details.

## Running Locally
1. Start Flask app: `python app/main.py`.
2. Start Kafka consumer: `python app/kafka_consumer.py`.
3. Test with: `curl -X POST http://localhost:5000/process -H "Content-Type: application/json" -d '{"text": "I love this product!"}'`.

## Deploying to Kubernetes
1. Build Docker image: `docker build -t real-time-data-pipeline .`.
2. Apply Kubernetes configs: `kubectl apply -f kubernetes/deployment.yaml` and `kubectl apply -f kubernetes/service.yaml`.

## Features
- Real-time data streaming with Kafka.
- Sentiment analysis using Hugging Face Transformers.
- AWS S3 storage, Redis caching, Kubernetes orchestration.