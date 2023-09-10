# Import scikit-learn library
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the cleaned and transformed dataset from the previous file
import pandas as pd
df = pd.read_csv("cleaned_data.csv")

# Separate the features and the label
X = df.drop("revenue", axis=1) # features
y = df["revenue"] # label

# Split the data into training and testing sets, using 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = model.predict(X_test) # predicted revenue based on test features
mse = mean_squared_error(y_test, y_pred) # mean squared error
r2 = r2_score(y_test, y_pred) # coefficient of determination

# Print the evaluation results
print("Mean squared error: {:.2f}".format(mse))
print("Coefficient of determination: {:.2f}".format(r2))

# Save the model to a file
import joblib
joblib.dump(model, "model.pkl")
