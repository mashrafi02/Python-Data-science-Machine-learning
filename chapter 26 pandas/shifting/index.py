import numpy as np
import pandas as pd

# creating a data frame
df = pd.DataFrame({'value': [1, 2, 3, 4,5]})
print(df, end="\n\n")


df["shifted"] = df["value"].shift(1)
print(df, end="\n\n")


df["shifted_reverse"] = df["value"].shift(-1)
print(df, end="\n\n")


df["shifted_fill_value"] = df["value"].shift(1, fill_value=0)
print(df, end="\n\n")
