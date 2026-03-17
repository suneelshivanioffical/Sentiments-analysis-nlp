import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        top_k=None
    )

sentiment_pipeline = load_model()


def analyze_sentiment(text):

    results = sentiment_pipeline(text)

    scores = {
        "negative": 0,
        "neutral": 0,
        "positive": 0
    }

    # Handle nested structure safely
    if isinstance(results, list) and len(results) > 0:
        results = results[0]

    for item in results:

        label = item["label"].lower()
        score = item["score"]

        if "negative" in label:
            scores["negative"] = score

        elif "neutral" in label:
            scores["neutral"] = score

        elif "positive" in label:
            scores["positive"] = score

    return scores