import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
# print(data)


X = data.data
Y = data.target


df = pd.DataFrame(X, columns=data.feature_names)
df["MEDV"] = Y

# print(df)


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

scale = StandardScaler()

X_train = scale.fit_transform(X_train)
X_test = scale.transform(X_test)


model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)


print(f"mse: {mse:.2f}")
print(f"r2 score: {r2:.2f}")