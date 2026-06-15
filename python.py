import streamlit as st
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

st.set_page_config(page_title="Language Detection App")

st.title("🌍 Language Detection App")
st.write("Enter text and detect its language.")

text = st.text_area("Enter Text")

if st.button("Detect Language"):
    if text.strip():
        try:
            language = detect(text)

            language_names = {
                "en": "English",
                "ur": "Urdu",
                "ar": "Arabic",
                "fr": "French",
                "de": "German",
                "es": "Spanish",
                "it": "Italian",
                "pt": "Portuguese",
                "ru": "Russian",
                "hi": "Hindi",
                "zh-cn": "Chinese",
                "ja": "Japanese",
                "ko": "Korean",
                "tr": "Turkish"
            }

            detected = language_names.get(language, language)

            st.success(f"Detected Language: {detected}")
            st.write(f"Language Code: {language}")

        except Exception as e:
            st.error("Could not detect the language.")
    else:
        st.warning("Please enter some text.")
