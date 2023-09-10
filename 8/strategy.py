# Import the modules you need
import flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the previous step
from data import data

# Load the algorithm from the previous step
from algorithm import problem, p, x

# Create a Flask app object
app = flask.Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    # Render the home page template
    return flask.render_template("home.html")

# Define a route for the pricing page
@app.route("/pricing")
def pricing():
    # Get the optimal prices and impressions from the algorithm
    prices = p.value
    impressions = x.value

    # Convert the prices and impressions to a dictionary
    prices_dict = dict(zip(data["keyword"], prices))
    impressions_dict = dict(zip(data["keyword"], impressions))

    # Render the pricing page template with the prices and impressions
    return flask.render_template("pricing.html", prices=prices_dict, impressions=impressions_dict)

# Define a route for the performance page
@app.route("/performance")
def performance():
    # Get the history of prices and impressions from the algorithm
    history = problem.history

    # Convert the history to a pandas dataframe
    history_df = pd.DataFrame(history)

    # Plot the history of prices and impressions for each ad
    fig, ax = plt.subplots()
    for i in range(n):
        ax.plot(history_df["prices"][i], history_df["impressions"][i], label=f"Ad {i+1}")
    ax.set_xlabel("Price")
    ax.set_ylabel("Impression")
    ax.set_title("History of prices and impressions for each ad")
    ax.legend()

    # Save the figure as an image file
    fig.savefig("performance.png")

    # Render the performance page template with the image file
    return flask.render_template("performance.html", image_file="performance.png")

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
