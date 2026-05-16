# -------------------------------
# NLP Information Retrieval System
# -------------------------------

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag

# Download required NLTK resources (Run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


# Input text
text = "Natural Language Processing helps computers understand human language."

print("Original Text:")
print(text)


# -----------------------------------
# 1. Text Tokenization
# -----------------------------------

tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)


# -----------------------------------
# 2. Count Word Frequency
# -----------------------------------

freq = FreqDist(tokens)

print("\nWord Frequency:")

for word, count in freq.items():
    print(word, ":", count)


# -----------------------------------
# 3. Remove Stop Words
# -----------------------------------

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("\nAfter Removing Stop Words:")
print(filtered_words)


# -----------------------------------
# 4. POS Tagging
# -----------------------------------

pos_tags = pos_tag(filtered_words)

print("\nPOS Tags:")
print(pos_tags)
