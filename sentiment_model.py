import streamlit as st
from transformers import pipeline

# Cache the model (loads only once)
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        return_all_scores=True
    )

sentiment_pipeline = load_model()


def analyze_sentiment(text):

    results = sentiment_pipeline(text)[0]

    scores = {
        "negative": 0,
        "neutral": 0,
        "positive": 0
    }

    for r in results:

        label = r["label"].lower()

        if label in ["label_0", "negative"]:
            scores["negative"] = r["score"]

        elif label in ["label_1", "neutral"]:
            scores["neutral"] = r["score"]

        elif label in ["label_2", "positive"]:
            scores["positive"] = r["score"]

    return scores