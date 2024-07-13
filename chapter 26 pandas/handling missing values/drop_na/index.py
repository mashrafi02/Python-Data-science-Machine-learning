import numpy as np
import pandas as pd


# creating data frame

data = {
    'A' : [ 1, 2, np.nan, 4, 5],
    'B' : [np.nan, 2.5, 3.5, np.nan, 5.5],
    'C' : ['a', 'b', np.nan, 'd', 'e']
}

df = pd.DataFrame(data)
print(df, end="\n\n")


print(df.isnull().sum(), end="\n\n") # to see how many NaN values are there by sum of every NaN values in each column

df_dropna_row = df.dropna() # by default it's axis is 0 for row
print(df_dropna_row, end="\n\n")

df_dropna_column = df.dropna(axis=1)
print(df_dropna_column, end="\n\n")

df_dropna_all_rows = df.dropna(how="all") # if there is a NaN value in every column, only then that entire row will be dropped
print(df_dropna_all_rows, end="\n\n")

df_dropna_any_rows = df.dropna(how="any") # if there is a NaN value in any column then that entire row will be dropped.
print(df_dropna_any_rows, end="\n\n")



# interpolate missing values using linear method
df_interpolate = df.interpolate()
print(df_interpolate, end="\n\n") # it only works numerically. it just fill the NaN values with 1 time increased value of previous row
