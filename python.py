
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

st.title("😊 Sentiment Analysis App")
st.write("Enter text and analyze its sentiment using a free Hugging Face model.")

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        framework="tf"
    )

classifier = load_model()

user_text = st.text_area(
    "Enter your text:",
    height=150,
    placeholder="Type something here..."
)

if st.button("Analyze Sentiment"):
    if user_text.strip():
        result = classifier(user_text)[0]

        label = result["label"]
        score = round(result["score"] * 100, 2)

        st.subheader("Result")

        if label == "POSITIVE":
            st.success(f"Positive 😊 ({score}%)")
        else:
            st.error(f"Negative 😞 ({score}%)")

        st.write("**Confidence:**", f"{score}%")

    else:
        st.warning("Please enter some text.")
