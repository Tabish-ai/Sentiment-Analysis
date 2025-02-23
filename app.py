import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Streamlit App
st.title("🔍 Tabish's Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment (Positive, Negative, or Neutral).")

text = st.text_area("Enter text here:", "")

if st.button("Analyze Sentiment"):
    if text:
        result = sentiment_pipeline(text)[0]
        label = result["label"]
        score = result["score"]
        st.write(f"**Sentiment:** {label} (Confidence: {score:.2f})")
    else:
        st.warning("Please enter some text!")
