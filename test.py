import joblib
model = joblib.load('model/lin_reg.pkl')

# Sample data (you can replace these values with whatever you want to test)
test_data = [
    [8.3252, 41, 6.98412698, 1.02380952, 322, 2.55555556, 37.88, -122.23]  # Example values for each feature
]

predicted_value = model.predict(test_data)
print(f"Predicted Value: {predicted_value[0]}")
