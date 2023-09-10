# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Import scikit-learn libraries for model training and evaluation
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

# Read the processed data from the CSV file
df = pd.read_csv("data_processed.csv")

# Separate the input features and the output label
X = df.drop("label", axis=1)
y = df["label"]

# Split the data into training and testing sets (80/20 ratio)
train_size = int(len(df) * 0.8)
X_train = X[:train_size]
y_train = y[:train_size]
X_test = X[train_size:]
y_test = y[train_size:]

# Define a list of models to compare
models = [
    ("Logistic Regression", LogisticRegression()),
    ("Random Forest", RandomForestClassifier()),
    ("Support Vector Machine", SVC()),
    ("K-Means Clustering", KMeans(n_clusters=2)),
    ("Anomaly Detection", LocalOutlierFactor(novelty=True))
]

# Define a function to evaluate a model on the test set
def evaluate_model(model, X_test, y_test):
    # Predict the labels for the test set
    y_pred = model.predict(X_test)

    # Calculate the metrics for the test set
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    auc = auc(fpr, tpr)

    # Return a dictionary of metrics
    return {
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1-score": f1,
        "roc-auc": auc
    }

# Create an empty dataframe to store the results
results = pd.DataFrame(columns=["model", "accuracy", "precision", "recall", "f1-score", "roc-auc"])

# Loop over the models
for name, model in models:
    # Train the model on the training set
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    metrics = evaluate_model(model, X_test, y_test)

    # Append the results to the dataframe
    results = results.append({"model": name, **metrics}, ignore_index=True)

# Print the results
print(results)
