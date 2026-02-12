import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#Write regex code to remove URLs from text.
import re
text = "Visit our website at https://example.com for more details"
clean_text = re.sub(r"http\S+|www\S+", "", text)

print(clean_text)
