import numpy as np
import pandas as pd

# creating a data frame
data = {
    'A' : [ 1, 2, np.nan, 4, 5],
    'B' : [np.nan, 2.5, 3.5, np.nan, 5.5],
    'C' : ['a', 'b', np.nan, 'd', 'e']
}

df = pd.DataFrame(data)
print(df, end="\n\n")

df_replace = df.replace(np.nan, "missing")
print(df_replace, end="\n\n")


# creating another data frame
data2 = {
    'temperature': [25.0, 30.5, -999.9, 22.0, 28.0],
    'wind speed': [5, -999, 15, 10, -999],
    'event': ['Rain', 'Sunny', 'Missing', 'Cloudy', 'Sunny'],
    'description': ['Hot day', 'Very hot day', 'Cold day', 'Windy day', 'Rainy day'],
    'score': ['poor', 'average', 'good', 'exceptional', 'good']
}
df2 = pd.DataFrame(data2)
print(df2, end="\n\n")

df2_replace = df2.replace("Missing", "Gloomy")
print(df2_replace, end="\n\n")


# replacing values based on columns
df2_repalced_columns = df2.replace({"temperature" : -999.9, "event" : "Missing"}, np.nan)
print(df2_repalced_columns, end="\n\n")


# replacing values based on values
df2_replaced_values = df2.replace({-999.9 : np.nan, "poor" : "bad"})
print(df2_replaced_values, end="\n\n")


# replace values based on creating a map
replace_map = {"poor" : 1, "average" : 2, "good" : 3, "exceptional" : 4, "good" : 5}

# replacing new mapped values
df2["score"] = df2["score"].replace(replace_map)
print(df2, end="\n\n")


