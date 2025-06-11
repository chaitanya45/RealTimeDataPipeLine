from transformers import pipeline

def analyze_sentiment(text):
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(text)[0]
    return {"text": text, "label": result["label"], "score": result["score"]}