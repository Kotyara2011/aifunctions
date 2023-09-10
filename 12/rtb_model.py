# Import the required libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data from the CSV file
df = pd.read_csv("rtb_data.csv") # Dataframe with normalized RTB data

# Split the data into features and labels
X = df.drop(["average_CTR"], axis=1) # Features are all columns except average_CTR
y = df["average_CTR"] # Label is average_CTR

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% for training, 20% for testing

# Define the model architecture
model = keras.Sequential([
    layers.Dense(64, activation="relu", input_shape=[len(X_train.columns)]), # Input layer with 64 neurons and ReLU activation
    layers.Dense(32, activation="relu"), # Hidden layer with 32 neurons and ReLU activation
    layers.Dense(1) # Output layer with 1 neuron (regression problem)
])

# Compile the model with optimizer, loss function, and metrics
model.compile(
    optimizer="adam", # Adam optimizer for gradient descent
    loss="mse", # Mean squared error as loss function
    metrics=["mae"] # Mean absolute error as metric
)

# Train the model with the training data and validation data
history = model.fit(
    X_train, y_train, # Training features and labels
    validation_data=(X_test, y_test), # Validation features and labels
    batch_size=32, # Batch size for mini-batch gradient descent
    epochs=100, # Number of epochs for training
    verbose=0 # Suppress output
)

# Evaluate the model performance on the test data
test_loss, test_mae = model.evaluate(X_test, y_test) # Test loss and test mae

# Print the results
print(f"Test loss: {test_loss:.4f}")
print(f"Test mean absolute error: {test_mae:.4f}")

# Generate predictions for the test data
y_pred = model.predict(X_test) # Predicted average_CTR values

# Calculate the root mean squared error (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # RMSE formula

# Print the RMSE
print(f"Test root mean squared error: {rmse:.4f}")
