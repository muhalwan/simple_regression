import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression().fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"Model Test Accuracy: {score}")

# Save the model
joblib.dump(model, "model/lin_reg.pkl")
