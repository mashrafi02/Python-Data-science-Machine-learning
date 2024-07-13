import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris


data = load_iris()
# print(data)

X = data.data
Y = data.target


# Convert to pandas DataFrame for easier manipulation
df = pd.DataFrame(X, columns=data.feature_names)
df["target"] = Y

# print(df)


# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)


# Scale the features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Initialize the model
model = LogisticRegression()


# train the model
model.fit(X_train, Y_train)


# make predictions with the model
Y_pred = model.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(Y_test, Y_pred)
report = classification_report(Y_test, Y_pred)

# print(accuracy, report)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)