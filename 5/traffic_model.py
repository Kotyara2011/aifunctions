# Import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Read the processed traffic data from the previous file
traffic_df = pd.read_csv("processed_traffic_data.csv")

# Define the features and the target variable
X = traffic_df.drop("quality", axis=1) # The features are all the columns except quality
y = traffic_df["quality"] # The target variable is quality

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Use 20% of the data for testing and set a random seed for reproducibility

# Build and train a K-Nearest Neighbors classifier using scikit-learn
knn = KNeighborsClassifier(n_neighbors=5) # Create an instance of the classifier with 5 neighbors
knn.fit(X_train, y_train) # Fit the classifier to the training data

# Predict the quality of the test data using the trained classifier
y_pred = knn.predict(X_test) # Predict the labels for the test data

# Evaluate the performance of the classifier using various metrics
accuracy = accuracy_score(y_test, y_pred) # Calculate the accuracy as the fraction of correct predictions
precision = precision_score(y_test, y_pred) # Calculate the precision as the fraction of true positives among positive predictions
recall = recall_score(y_test, y_pred) # Calculate the recall as the fraction of true positives among actual positives
f1 = f1_score(y_test, y_pred) # Calculate the F1-score as the harmonic mean of precision and recall

# Print the results
print("The accuracy of the classifier is {:.2f}%".format(accuracy * 100))
print("The precision of the classifier is {:.2f}%".format(precision * 100))
print("The recall of the classifier is {:.2f}%".format(recall * 100))
print("The F1-score of the classifier is {:.2f}%".format(f1 * 100))

