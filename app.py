from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/lin_reg.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([list(data.values())])[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

