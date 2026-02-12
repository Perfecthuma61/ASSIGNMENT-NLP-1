import pandas as pd
import numpy as np
df=pd.read_csv("/content/sample.csv")
#Write code to remove HTML tags.
import re
text = "<p>This is a <b>sample</b> text with HTML tags</p>"
clean_text = re.sub(r"<.*?>", "", text)

print(clean_text)
