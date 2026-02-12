import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#stemming using Porter Stemmer on a sample sentence.
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
sentence = "Players are running and playing happily"
stemmed_words = [stemmer.stem(word) for word in sentence.split()]
print(" ".join(stemmed_words))
