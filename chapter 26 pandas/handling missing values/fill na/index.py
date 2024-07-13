import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2.5, 3.5, np.nan, 5.5],
    'C': ['a', 'b', np.nan, 'd', 'e']
}
df = pd.DataFrame(data)
print(df)


# filing NaN values with a specific value
print(df.fillna(0))
print(df.fillna(df.mean(numeric_only=True)))

# it won't change the main dataframe. if u want to change the main data frame , either you have to assign it in e new variable or
# make true the in place attribute of fill na 

df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)




data2 = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2.5, 3.5, np.nan, 5.5],
    'C': ['a', 'b', np.nan, 'd', 'e']
}
df2 = pd.DataFrame(data2)
print(df2)

median = df2['A'].median()
print(df2["A"].fillna(median))



# forward fill
print(df2.fillna(method="ffill"))
# df2.ffill()   you can also write like this

# backward fill
print(df2.fillna(method="bfill"))
# df2.bfill()    you can also write like this
