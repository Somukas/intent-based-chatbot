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

def preprocess_input(user_input):
   tokens = word_tokenize(user_input.lower())  # Tokenize and convert to lowercase
   filtered_tokens = [lemmatizer.lemmatize(tokens)]
   return filtered_tokens

def match_intent(user_input):
    processed_input = preprocess_input(user_input)
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess_input(pattern)
            if set(processed_input).intersection(pattern_tokens):  # Check for common words
                return intent
    return None
