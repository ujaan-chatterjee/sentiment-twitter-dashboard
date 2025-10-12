import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

st.title("Social Media Sentiment Dashboard")
st.write("Monitoring Twitter sentiment for #AIethics")

# Simulated sample tweets
tweets = [
    "AI is changing society!",
    "Worried about ethics in AI.",
    "Great progress, but risks remain."
]
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
sentiments = [sentiment_analyzer(tw)[0]['label'] for tw in tweets]

df = pd.DataFrame({"Tweet": tweets, "Sentiment": sentiments})
st.dataframe(df)

fig, ax = plt.subplots()
df['Sentiment'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.write("Bias metrics are covered in the notebook and README notes.")
