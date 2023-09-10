# Import the necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Flatten, Dense, Concatenate
from tensorflow.keras.regularizers import l2
from sklearn.metrics import precision_score, recall_score, ndcg_score

# Read the processed content data and the user data from the previous files
content_df = pd.read_csv("processed_content_data.csv")
user_df = pd.read_csv("processed_user_data.csv")

# Load the content model and the user model from the previous files
content_model = tf.keras.models.load_model("content_model.h5")
user_model = tf.keras.models.load_model("user_model.h5")

# Define the input and output dimensions
num_users = user_df["user_id"].nunique() # The number of unique users
num_contents = content_df["id"].nunique() # The number of unique contents
embedding_dim = 128 # The dimension of the embeddings

# Define the model architecture using Keras functional API
# The model consists of two branches: one for user embeddings and one for content embeddings
# Each branch has an embedding layer that maps the user id or content id to a dense vector representation
# The outputs of the two branches are concatenated and passed to a dense layer that generates the recommendation score

# Define the user branch
user_input = Input(shape=(1,), name="user_input") # Define the input layer for user id
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim, name="user_embedding")(user_input) # Define the embedding layer for user id

# Define the content branch
content_input = Input(shape=(1,), name="content_input") # Define the input layer for content id
content_embedding = Embedding(input_dim=num_contents, output_dim=embedding_dim, name="content_embedding")(content_input) # Define the embedding layer for content id

# Concatenate the outputs of the two branches
concat = Concatenate(name="concat")([user_embedding, content_embedding]) # Define the concatenation layer

# Define the output layer that generates the recommendation score
recommendation_output = Dense(1, activation="sigmoid", name="recommendation_output")(concat) # Define the dense layer for recommendation score

# Create the model object
recommendation_model = Model(inputs=[user_input, content_input], outputs=recommendation_output, name="recommendation_model") # Create the model object with inputs and outputs

# Compile the model with loss function and optimizer
recommendation_model.compile(loss="binary_crossentropy", optimizer="adam") # Compile the model with binary cross entropy loss function and adam optimizer

# Print the model summary
recommendation_model.summary() # Print the model summary

# Train the model with the user id and content id as inputs and the rating as labels
recommendation_model.fit([user_df["user_id"], content_df["id"]], content_df["rating"], epochs=10, batch_size=32) # Train the model for 10 epochs with batch size of 32

# Evaluate the model performance on a test set (not provided here)
test_loss = recommendation_model.evaluate([test_user_df["user_id"], test_content_df["id"]], test_content_df["rating"]) # Evaluate the model on a test set and get the test loss
print("The test loss is {:.4f}".format(test_loss)) # Print the test loss

# Predict the recommendation scores for a test set (not provided here)
test_pred = recommendation_model.predict([test_user_df["user_id"], test_content_df["id"]]) # Predict the recommendation scores for a test set
test_pred = test_pred.reshape(-1) # Reshape the prediction array to a one-dimensional vector

# Calculate the precision, recall, and NDCG metrics for a test set (not provided here)
test_precision = precision_score(test_content_df["rating"], test_pred > 0.5) # Calculate the precision as the fraction of true positives among positive predictions using a threshold of 0.5
test_recall = recall_score(test_content_df["rating"], test_pred > 0.5) # Calculate the recall as the fraction of true positives among actual positives using a threshold of 0.5
test_ndcg = ndcg_score(test_content_df[["user_id", "rating"]], test_pred) # Calculate the NDCG as the normalized discounted cumulative gain using user id and rating as groups

# Print the metrics
print("The test precision is {:.2f}%".format(test_precision * 100))
print("The test recall is {:.2f}%".format(test_recall * 100))
print("The test NDCG is {:.4f}".format(test_ndcg))

# Save the model to a file
recommendation_model.save("recommendation_model.h5") # Save the model to a HDF5 file

