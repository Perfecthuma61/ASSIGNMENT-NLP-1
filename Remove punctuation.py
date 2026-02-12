import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#Python function to remove punctuation from text.
import string
df = df.applymap(
    lambda x: x.translate(str.maketrans("", "", string.punctuation)) if isinstance(x, str) else x
)
df.head()
