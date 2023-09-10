# Import flask library
from flask import Flask, request, jsonify

# Import pickle library to load the saved model
import pickle

# Create an instance of the flask app
app = Flask(__name__)

# Load the saved model from the file
model = pickle.load(open("model.pkl", "rb"))

# Define a route for the API
@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the request as a JSON object
    data = request.get_json()

    # Extract the features from the data
    features = [data["SepalLengthCm"], data["SepalWidthCm"], data["PetalLengthCm"], data["PetalWidthCm"]]

    # Convert the features to a numpy array
    features = np.array(features).reshape(1, -1)

    # Predict the label using the model
    label = model.predict(features)[0]

    # Return the prediction as a JSON response
    return jsonify({"prediction": label})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
