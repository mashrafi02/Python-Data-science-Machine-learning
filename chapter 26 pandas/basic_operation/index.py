import numpy as np
import pandas as pd

# Create first DataFrame
data1 = {
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
}
df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'A': [4, 5, 6],
    'B': ['d', 'e', 'f']
}
df2 = pd.DataFrame(data2)

# Display the DataFrames
print(df1, end="\n\n")
print(df2, end="\n\n")


# simple concat among rows
df_concat = pd.concat([df1,df2],ignore_index=True)
print(df_concat, end="\n\n")


# simple concat among columns
df_concat_col = pd.concat([df1,df2], axis=1, ignore_index=True)
print(df_concat_col, end="\n\n")


# concatenate and set new index
df_concat_new_index = pd.concat([df1,df2]).reset_index(drop=True)
df_concat_new_index.index = ["row1","row2","row3","row4","row5","row6"]
print(df_concat_new_index, end="\n\n")



#### Merge ####
df3 = pd.DataFrame({'key':['A','B','C'], 'value1':[1,2,3]})
df4 = pd.DataFrame({'key':['B','C','D'], 'value1':[4,5,6]})

# inner merge
result = pd.merge(df3,df4, on="key", how="inner")
print(result,end="\n\n")


# outer merge
result2 = pd.merge(df3,df4, on="key", how="outer")
print(result2, end="\n\n")


# left merge
result3 = pd.merge(df3,df4, on="key", how="left")
print(result3, end="\n\n")


# right merge
result4 = pd.merge(df3,df4, on="key", how="right")
print(result4, end="\n\n")