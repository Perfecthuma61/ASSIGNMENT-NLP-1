import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#stopword removal using NLTK.
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
df["text"] = df["text"].apply(
    lambda x: " ".join(word for word in str(x).split() if word.lower() not in stop_words)
)
df.head()
