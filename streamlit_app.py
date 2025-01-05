import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json
import random
import streamlit as st

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load intents.json
with open("intents.json", "r") as file:
    intents = json.load(file)  # Load JSON as a list

# Initialize preprocessing and model
lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer()
model = LogisticRegression()

# Prepare data for training
tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Train model
x = vectorizer.fit_transform(patterns)
y = tags
model.fit(x, y)

# Bot response function
def bot(user_input):
    input_text = vectorizer.transform([user_input])  # Transform input for prediction
    tag = model.predict(input_text)[0]  # Predict intent tag
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])  # Return random response
    return "Sorry, I don't understand that."  # Default response

# Streamlit UI
st.title("Intent-Based Chatbot")
st.write("Ask me anything, and I'll try my best to help!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You: ", key="input")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append(("You", user_input))

    # Get bot response
    response = bot(user_input)
    st.session_state.messages.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.messages:
    if sender == "You":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Bot:** {message}")


#Streamlit link: https://intent-based-chatbot-nvqnx47kpeof3xmfqexwvy.streamlit.app/
#Github Link: https://github.com/Somukas/intent-based-chatbot/edit/main/streamlit_app.py
