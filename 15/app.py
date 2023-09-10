# Import libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the best model from model.pkl
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the features and their ranges for user input
features = ["CTR", "ad_text_length", "ad_image_size", "page_content_length", "page_keywords_count", "page_topics_count", "ad_relevance_score", "ad_quality_score"]
ranges = [(0, 1), (0, 1000), (0, 1000000), (0, 10000), (0, 100), (0, 10), (0, 1), (0, 100)]

# Create a streamlit web app for user interface
st.title("Ad Optimization")
st.write("This app predicts the optimal CPC and CPA for an ad based on its features")

# Create sliders for each feature and store the values in a dictionary
inputs = {}
for feature, range in zip(features, ranges):
    inputs[feature] = st.slider(feature, range[0], range[1])

# Convert the inputs into a dataframe
input_df = pd.DataFrame([inputs])

# Predict the optimal CPC and CPA using the model
cpc, cpa = model.predict(input_df)[0]

# Display the optimal CPC and CPA as metrics
st.metric("CPC", cpc)
st.metric("CPA", cpa)

# Monitor the model performance and feedback over time using streamlit metrics and charts
# For example, use st.metric to show the MSE and MAE of the model on a test dataset
test_df = pd.read_csv("test_data.csv") # Load a test dataset with features and labels
X_test = test_df.drop(["CPC", "CPA"], axis=1) # Independent variables
y_test = test_df[["CPC", "CPA"]] # Dependent variables
y_pred = model.predict(X_test) # Predicted labels

# Calculate the MSE and MAE for CPC and CPA separately
for i, col in enumerate(["CPC", "CPA"]):
    mse = mean_squared_error(y_test[col], y_pred[:, i]) # Mean squared error
    mae = mean_absolute_error(y_test[col], y_pred[:, i]) # Mean absolute error
    
    # Display the metrics using st.metric
    st.metric(f"MSE for {col}", mse)
    st.metric(f"MAE for {col}", mae)

# Use st.line_chart to show the actual vs predicted values for CPC and CPA on the test dataset
cpc_df = pd.DataFrame({"Actual": y_test["CPC"], "Predicted": y_pred[:, 0]}) # Create a dataframe with actual and predicted CPC values
cpa_df = pd.DataFrame({"Actual": y_test["CPA"], "Predicted": y_pred[:, 1]}) # Create a dataframe with actual and predicted CPA values

st.line_chart(cpc_df) # Plot the line chart for CPC
st.line_chart(cpa_df) # Plot the line chart for CPA

# Save the web app code in a file named app.py
# To do this, copy and paste this code in a text editor and save it as app.py
