import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
import emoji

text = "Hey how are you😄🔥"

# Convert emojis to words
converted_text = emoji.demojize(text)

print(converted_text)
