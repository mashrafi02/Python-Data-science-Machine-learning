import pandas as pd

df = pd.read_csv("weather.csv")
print(df, df.shape) # to see the row*column relation or shape of the data frame

print(df.head()) # by default it will show the first 5 rows of your data frame
print(df.tail()) # by default it will show the last 5 rows of your data frame

# but you can also fix the limit of the number of rows to show
print(df.head(3))
print(df.tail(3))


# statustical operation at a glance
print(df.describe())

# data type info at a glance
print(df.info())

# row slicing 
print(df[2:4])

# column slicing
print(df[["Date","Precipitation (mm)"]])

# selecting a specific cell using loc
print(df.loc[2,"Day"])

# selecting a specific cell using iloc
print(df.iloc[6,2])



import pandas as pd

# Sample data creation
data = {
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 
                 'Books', 'Books', 'Books', 'Books', 'Books', 'Books'],
    'product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 
                'Product F', 'Product G', 'Product H', 'Product I', 'Product J', 'Product K'],
    'rating_count': [100, 200, 50, 300, 150, 80, 90, 200, 150, 60, 70]
}

# Convert to DataFrame
df2 = pd.DataFrame(data)

# Group by 'category' and get the top 5 products by 'rating_count'
top_products = df2.groupby('category').apply(lambda x: x.nlargest(5, 'rating_count')).reset_index(drop=True)

print(top_products)
