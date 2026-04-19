import streamlit as st
from textblob import TextBlob
from collections import Counter
import string

st.set_page_config(page_title="AI Text Analyzer", layout="centered")

st.title("🧠 AI-Powered Text Analyzer")

text = st.text_area("Enter your text here:")

if st.button("Analyze"):

    # Clean text
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()

    # Stopwords
    stopwords = ["the", "is", "and", "in", "to", "of", "a", "for", "i", "am"]
    words = [w for w in words if w not in stopwords]

    # Word count
    word_count = len(words)

    # Frequency
    freq = Counter(words).most_common(5)

    # Sentiment
    sentiment = TextBlob(clean_text).sentiment.polarity

    if sentiment > 0:
        label = "Positive 😊"
        explanation = "The text expresses a positive emotion."
    elif sentiment < 0:
        label = "Negative 😞"
        explanation = "The text expresses a negative emotion."
    else:
        label = "Neutral 😐"
        explanation = "The text has no strong emotional tone."

    # Output
    st.subheader("📊 Analysis Report")
    st.write("**Total Words:**", word_count)

    st.write("**Top Keywords:**")
    for word, count in freq:
        st.write(f"{word} → {count}")

    st.write("**Sentiment Score:**", round(sentiment, 2))
    st.write("**Sentiment:**", label)
    st.info(explanation)

    # Visualization
    if freq:
        words_list = [w for w, c in freq]
        counts = [c for w, c in freq]
        st.bar_chart({"Words": counts}, use_container_width=True)