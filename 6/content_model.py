# Import the necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Conv1D, MaxPooling1D, Flatten, Concatenate

# Read the processed content data and the feature matrices from the previous file
content_df = pd.read_csv("processed_content_data.csv")
title_features = np.load("title_features.npy")
description_features = np.load("description_features.npy")

# Define the input and output dimensions
input_dim = title_features.shape[1] + description_features.shape[1] # The input dimension is the sum of the title and description feature dimensions
output_dim = 128 # The output dimension is an arbitrary number of 128

# Define the model architecture using Keras functional API
# The model consists of two branches: one for title features and one for description features
# Each branch has a convolutional layer followed by a max pooling layer and a flattening layer
# The outputs of the two branches are concatenated and passed to a dense layer that generates the content embeddings

# Define the title branch
title_input = Input(shape=(input_dim, 1), name="title_input") # Define the input layer for title features
title_conv = Conv1D(filters=32, kernel_size=3, activation="relu", name="title_conv")(title_input) # Define the convolutional layer for title features
title_pool = MaxPooling1D(pool_size=2, name="title_pool")(title_conv) # Define the max pooling layer for title features
title_flat = Flatten(name="title_flat")(title_pool) # Define the flattening layer for title features

# Define the description branch
description_input = Input(shape=(input_dim, 1), name="description_input") # Define the input layer for description features
description_conv = Conv1D(filters=32, kernel_size=3, activation="relu", name="description_conv")(description_input) # Define the convolutional layer for description features
description_pool = MaxPooling1D(pool_size=2, name="description_pool")(description_conv) # Define the max pooling layer for description features
description_flat = Flatten(name="description_flat")(description_pool) # Define the flattening layer for description features

# Concatenate the outputs of the two branches
concat = Concatenate(name="concat")([title_flat, description_flat]) # Define the concatenation layer

# Define the output layer that generates the content embeddings
content_output = Dense(output_dim, activation="linear", name="content_output")(concat) # Define the dense layer for content embeddings

# Create the model object
content_model = Model(inputs=[title_input, description_input], outputs=content_output, name="content_model") # Create the model object with inputs and outputs

# Compile the model with loss function and optimizer
content_model.compile(loss="mean_squared_error", optimizer="adam") # Compile the model with mean squared error loss function and adam optimizer

# Print the model summary
content_model.summary() # Print the model summary

# Train the model with the feature matrices and the content data as labels
content_model.fit([title_features, description_features], content_df, epochs=10, batch_size=32) # Train the model for 10 epochs with batch size of 32

# Evaluate the model performance on a test set (not provided here)
test_loss = content_model.evaluate([test_title_features, test_description_features], test_content_df) # Evaluate the model on a test set and get the test loss
print("The test loss is {:.4f}".format(test_loss)) # Print the test loss

# Save the model to a file
content_model.save("content_model.h5") # Save the model to a HDF5 file

