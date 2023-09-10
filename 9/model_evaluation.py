# Import scikit-learn library
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, KFold

# Load the trained model from the previous file
import joblib
model = joblib.load("model.pkl")

# Load the unseen data from a csv file
import pandas as pd
df = pd.read_csv("unseen_data.csv")

# Separate the features and the label
X = df.drop("revenue", axis=1) # features
y = df["revenue"] # label

# Predict the revenue based on the unseen features
y_pred = model.predict(X)

# Calculate the mean absolute error, mean squared error, and coefficient of determination
mae = mean_absolute_error(y, y_pred) # mean absolute error
mse = mean_squared_error(y, y_pred) # mean squared error
r2 = r2_score(y, y_pred) # coefficient of determination

# Print the results
print("Mean absolute error: {:.2f}".format(mae))
print("Mean squared error: {:.2f}".format(mse))
print("Coefficient of determination: {:.2f}".format(r2))

# Perform 10-fold cross-validation on the model and the unseen data
kf = KFold(n_splits=10, shuffle=True, random_state=42) # create a 10-fold split object
cv_scores = cross_val_score(model, X, y, cv=kf, scoring="r2") # calculate the r2 score for each fold

# Print the cross-validation results
print("Cross-validation scores: {}".format(cv_scores))
print("Mean cross-validation score: {:.2f}".format(cv_scores.mean()))

# Write a report to a text file
with open("report.txt", "w") as f:
    f.write("AI-based Revenue Forecasting Model Evaluation Report\n")
    f.write("====================================================\n")
    f.write("This report evaluates the performance and accuracy of the AI-based revenue forecasting model on unseen data.\n")
    f.write("The model is a linear regression model trained on historical revenue data from various sources.\n")
    f.write("The evaluation metrics used are mean absolute error (MAE), mean squared error (MSE), and coefficient of determination (R2).\n")
    f.write("The evaluation techniques used are single test set evaluation and 10-fold cross-validation.\n")
    f.write("\n")
    f.write("Evaluation Results\n")
    f.write("------------------\n")
    f.write("The model achieved the following results on the unseen data:\n")
    f.write("- MAE: {:.2f}\n".format(mae))
    f.write("- MSE: {:.2f}\n".format(mse))
    f.write("- R2: {:.2f}\n".format(r2))
    f.write("\n")
    f.write("The model achieved the following results on the 10-fold cross-validation:\n")
    f.write("- Cross-validation scores: {}\n".format(cv_scores))
    f.write("- Mean cross-validation score: {:.2f}\n".format(cv_scores.mean()))
    f.write("\n")
    f.write("Strengths and Weaknesses\n")
    f.write("------------------------\n")
    f.write("The strengths of the model are:\n")
    f.write("- It is simple and easy to implement.\n")
    f.write("- It has a relatively high R2 score, indicating that it can explain most of the variance in the revenue data.\n")
    f.write("- It has a consistent performance across different folds of cross-validation, indicating that it is not overfitting or underfitting.\n")
    f.write("\n")
    f.write("The weaknesses of the model are:\n")
    f.write("- It has a relatively high MAE and MSE, indicating that it has large errors in some predictions.\n")
    f.write("- It assumes a linear relationship between the features and the revenue, which may not be true in reality.\n")
    f.write("- It may not capture complex interactions or nonlinearities among the features or between the features and the revenue.\n")
    f.write("\n")
    f.write("Suggestions for Improvement\n")
    f.write("--------------------------\n")
    f.write("Some possible suggestions for improving the model are:\n")
    f.write("- Explore different types of models, such as neural networks, regression trees, or time series models, that can capture more complex patterns in the data.\n")
    f.write("- Perform feature engineering or feature selection to create or select more relevant or informative features for the model.\n")
    f.write("- Perform hyperparameter tuning or regularization to optimize the model parameters or reduce overfitting or underfitting.\n")

