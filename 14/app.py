# Import libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the best model from model.pkl
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the features and their ranges for user input
features = ["purchase_history", "usage_frequency", "social_media", "survey_response_2", "survey_response_3", "survey_response_4", "survey_response_5", "CLV", "ARPU", "CSAT"]
ranges = [(0, 1000), (0, 30), (0, 1), (1, 5), (1, 5), (1, 5), (1, 5), (0, 10000), (0, 1000), (1, 5)]

# Create a streamlit web app for user interface
st.title("User Churn Prediction")
st.write("This app predicts the probability of a user churning based on their features")

# Create sliders for each feature and store the values in a dictionary
inputs = {}
for feature, range in zip(features, ranges):
    inputs[feature] = st.slider(feature, range[0], range[1])

# Convert the inputs into a dataframe
input_df = pd.DataFrame([inputs])

# Predict the probability of churn using the model
prob = model.predict_proba(input_df)[0, 1]

# Display the probability of churn as a percentage
st.write(f"The probability of churn is {prob*100:.2f}%")

# Monitor the model performance and feedback over time using streamlit metrics and charts
# For example, use st.metric to show the accuracy and recall scores of the model on a test dataset
test_df = pd.read_csv("test_data.csv") # Load a test dataset with features and labels
X_test = test_df.drop("churn", axis=1) # Independent variables
y_test = test_df["churn"] # Dependent variable
y_pred = model.predict(X_test) # Predicted labels
y_prob = model.predict_proba(X_test)[:, 1] # Predicted probabilities

# Calculate the accuracy and recall scores
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Display the metrics using st.metric
st.metric("Accuracy", accuracy)
st.metric("Recall", recall)

# Use st.line_chart to show the ROC curve of the model on the test dataset
fpr, tpr, thresholds = roc_curve(y_test, y_prob) # False positive rate, true positive rate, thresholds
roc_df = pd.DataFrame({"FPR": fpr, "TPR": tpr}) # Create a dataframe with FPR and TPR columns
st.line_chart(roc_df) # Plot the line chart

# Save the web app code in a file named app.py
# To do this, copy and paste this code in a text editor and save it as app.py
