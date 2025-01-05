import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json
import random

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

f=open('intents.json')
data=json.load(f)
vectorizer = TfidfVectorizer()
model = LogisticRegression()

tags = []
patterns = []
for intent in data:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
model.fit(x, y)


def bot(user_input):
    input_text = vectorizer.transform([user_input])
    tag = model.predict(input_text)[0]
    for intent in data:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response

import streamlit as st
st.title("Intent-Based Chatbot")
st.write("Ask me anything, and I'll try my best to help!")
if "messages" not in st.session_state:
        st.session_state.messages = []
user_input = st.text_input("You: ", key="input")
if user_input:
        # Add user message to chat history
        st.session_state.messages.append(("You", user_input))

        intent = bot(user_input)
        if intent:
           response = random.choice(intent["responses"])
        else:
            response = "Sorry, reword the question"  # Default response

        # Add bot response to chat history
        st.session_state.messages.append(("Bot", response))

  # Display chat history
for sender, message in st.session_state.messages:
        if sender == "You":
            st.write(f"**You:** {message}")
        else:
            st.write(f"**Bot:** {message}")        
