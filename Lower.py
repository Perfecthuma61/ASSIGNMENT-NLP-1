import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#code to convert a text string to lowercase.
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
df.head()
