import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#Perform lemmatization using spaCy or WordNet.
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
sentence = "The students were studying different subjects and discussing their ideas while running quickly towards the classrooms"
lemmatized_words = [lemmatizer.lemmatize(word) for word in sentence.split()]

print(" ".join(lemmatized_words))
