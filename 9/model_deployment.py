# Import Flask library
from flask import Flask, render_template, request

# Import joblib library
import joblib

# Load the trained model from the previous file
model = joblib.load("model.pkl")

# Create a Flask app object
app = Flask(__name__)

# Define the home page route
@app.route("/")
def home():
    # Render the home.html template
    return render_template("home.html")

# Define the result page route
@app.route("/result", methods=["POST"])
def result():
    # Get the features from the user input form
    sepal_length = request.form["sepal_length"]
    sepal_width = request.form["sepal_width"]
    petal_length = request.form["petal_length"]
    petal_width = request.form["petal_width"]

    # Convert the features to a list
    features = [sepal_length, sepal_width, petal_length, petal_width]

    # Predict the revenue based on the features
    revenue = model.predict([features])[0]

    # Render the result.html template with the revenue value
    return render_template("result.html", revenue=revenue)

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
