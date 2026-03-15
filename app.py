import streamlit as st
import pandas as pd
from sentiment_model import analyze_sentiment

# Page config
st.set_page_config(page_title="AI Sentiment Analyzer", layout="wide")

st.title("AI Sentiment Analysis using Transformers")

# ------------------------
# SINGLE TEXT ANALYSIS
# ------------------------

st.header("Single Text Analysis")

text = st.text_area("Enter text")

if st.button("Analyze Text"):

    if text.strip():

        scores = analyze_sentiment(text)

        neg = scores["negative"] * 100
        neu = scores["neutral"] * 100
        pos = scores["positive"] * 100

        st.subheader("Sentiment Confidence")

        # One line layout
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Negative 😡")
            st.write(f"{neg:.2f}%")
            st.progress(int(neg))

        with col2:
            st.markdown("### Positive 😊")
            st.write(f"{pos:.2f}%")
            st.progress(int(pos))

        with col3:
            st.markdown("### Neutral 😐")
            st.write(f"{neu:.2f}%")
            st.progress(int(neu))

    else:
        st.warning("Please enter some text.")

# ------------------------
# BATCH FILE ANALYSIS
# ------------------------

st.header("Batch Sentiment Analysis (CSV / Excel / TXT)")

uploaded_file = st.file_uploader(
    "Upload CSV, Excel, or TXT file",
    type=["csv", "xlsx", "txt"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    elif uploaded_file.name.endswith(".txt"):
        text_data = uploaded_file.read().decode("utf-8").split("\n")
        df = pd.DataFrame(text_data, columns=["text"])

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Select column
    column = st.selectbox("Select text column", df.columns)

    if st.button("Analyze File"):

        sentiments = []
        negative_scores = []
        neutral_scores = []
        positive_scores = []

        for t in df[column]:

            scores = analyze_sentiment(str(t))

            sentiment = max(scores, key=scores.get)

            sentiments.append(sentiment)

            negative_scores.append(scores["negative"] * 100)
            neutral_scores.append(scores["neutral"] * 100)
            positive_scores.append(scores["positive"] * 100)

        df["Sentiment"] = sentiments
        df["Negative %"] = negative_scores
        df["Neutral %"] = neutral_scores
        df["Positive %"] = positive_scores

        st.subheader("Results")
        st.dataframe(df)

        # Download results
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Results",
            data=csv,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv"
        )