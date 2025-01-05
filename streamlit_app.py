import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
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
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
model.fit(x, y)


def bot(user_input):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response

import streamlit as st
def main():
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
              response = random.choice(data["intents"][-1]["responses"])  # Default response

        # Add bot response to chat history
          st.session_state.messages.append(("Bot", response))

    # Display chat history
  for sender, message in st.session_state.messages:
          if sender == "You":
              st.write(f"**You:** {message}")
          else:
              st.write(f"**Bot:** {message}")        

if __name__ == '__main__':
    main()
