import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Critical Thinking Analyzer", layout="centered")

st.title("🧠 Critical Thinking Analysis App")
st.write("Write a paragraph and analyze its thinking pattern + visual graph")

text = st.text_area("Enter your paragraph:")

def analyze_text(text):
    text = text.lower()

    # Simple rule-based NLP scoring (no API, no paid model)
    logical = text.count("because") + text.count("therefore") + text.count("so")
    emotional = text.count("feel") + text.count("happy") + text.count("sad")
    analytical = text.count("analyze") + text.count("data") + text.count("result")
    creative = text.count("imagine") + text.count("creative") + text.count("idea")

    clarity = min(len(text.split()) / 10, 10)
    coherence = (logical + analytical) * 2
    confidence = text.count("will") + text.count("must") + text.count("sure")

    scores = {
        "Logical Thinking": logical,
        "Emotional Thinking": emotional,
        "Analytical Thinking": analytical,
        "Creative Thinking": creative,
        "Clarity": clarity,
        "Coherence": coherence,
        "Confidence": confidence
    }

    return scores

if st.button("Analyze"):

    if text.strip():

        scores = analyze_text(text)

        st.subheader("📊 Analysis Result")

        for k, v in scores.items():
            st.write(f"**{k}:** {v}")

        # -------- GRAPH --------
        labels = list(scores.keys())
        values = list(scores.values())

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        plt.xticks(rotation=45)
        ax.set_title("Thinking Pattern Graph")

        st.pyplot(fig)

    else:
        st.warning("Please enter a paragraph first.")
