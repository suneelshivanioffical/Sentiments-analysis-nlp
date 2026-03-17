# Sentiment Analysis using Transformers

A sentiment analysis on text using a Transformer-based NLP model. The application analyzes user text or uploaded files and predicts whether the sentiment is positive, negative, or neutral.

## Demo

![]()
![]()

## Live Demo - Streamlit Cloud


## Project Structure

```
SENTIMENT_ANALYSIS_TRANSFORMER
│
├── sentiment_model.py
├── app.py
├── README.md
└── requirements.txt
```

## Project Features

- Analyze single text input
- Perform batch sentiment analysis on CSV, Excel, or TXT files
- Show confidence scores for each sentiment
- Download analyzed results as file.
- Fast model loading using Streamlit caching

## Technologies

- Python
- PyTorch
- Transformers (HuggingFace)
- Streamlit

## Model

Pretrained Transformer Model:

```
cardiffnlp/twitter-roberta-base-sentiment-latest

```

This model is trained on large-scale Twitter data and can classify text into three sentiment categories:

- Positive
- Negative
- Neutral

The model returns confidence scores (probabilities) for each sentiment class.

## Run the Project Locally

1. Install requirements for run
   
    ```bash
    pip install -r requirements.txt
    ```
2. Start the Server
   
    ```bash
    streamlit run app.py
    ```
After running the command, the Streamlit web application will open in your browser where you can analyze text sentiment.