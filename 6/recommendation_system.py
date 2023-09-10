# Import the necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

# Read the new content and user data from files
new_content_df = pd.read_csv("new_content_data.csv")
new_user_df = pd.read_csv("new_user_data.csv")

# Load the content model, the user model, and the recommendation model from the previous files
content_model = tf.keras.models.load_model("content_model.h5")
user_model = tf.keras.models.load_model("user_model.h5")
recommendation_model = tf.keras.models.load_model("recommendation_model.h5")

# Predict the content embeddings and the user embeddings for the new data using the trained models
new_content_embeddings = content_model.predict([new_content_df["title"], new_content_df["description"]]) # Predict the content embeddings for the new content data
new_user_embeddings = user_model.predict(new_user_df["user_id"]) # Predict the user embeddings for the new user data

# Predict the recommendation scores for each user-content pair using the trained model
new_recommendation_scores = recommendation_model.predict([new_user_embeddings, new_content_embeddings]) # Predict the recommendation scores for each user-content pair
new_recommendation_scores = new_recommendation_scores.reshape(-1) # Reshape the prediction array to a one-dimensional vector

# Create a dataframe that contains the user id, content id, and recommendation score for each pair
new_recommendation_df = pd.DataFrame({"user_id": new_user_df["user_id"], "content_id": new_content_df["id"], "recommendation_score": new_recommendation_scores}) # Create a dataframe with user id, content id, and recommendation score columns

# Sort the dataframe by recommendation score in descending order
new_recommendation_df = new_recommendation_df.sort_values(by="recommendation_score", ascending=False) # Sort the dataframe by recommendation score in descending order

# Save the dataframe to a new file
new_recommendation_df.to_csv("new_recommendation_data.csv", index=False) # Save the dataframe to a CSV file without row indices

# Visualize the results using graphs and charts

# Plot a histogram to show the distribution of recommendation scores
plt.figure(figsize=(8,6)) # Set the figure size
plt.hist(new_recommendation_scores, bins=20) # Plot the histogram with 20 bins
plt.title("Distribution of Recommendation Scores") # Set the title
plt.xlabel("Recommendation Score") # Set the x-axis label
plt.ylabel("Frequency") # Set the y-axis label
plt.show() # Show the plot

# Plot a bar plot to show the top 10 contents with highest recommendation scores for a given user (not provided here)
user_id = 123 # The user id of interest (example value)
user_recommendations = new_recommendation_df[new_recommendation_df["user_id"] == user_id] # Filter the dataframe by user id
user_recommendations = user_recommendations.merge(new_content_df[["id", "title"]], on="id", how="left") # Merge with content title column
user_recommendations = user_recommendations.head(10) # Get the top 10 recommendations for the user
plt.figure(figsize=(10,8)) # Set the figure size
sns.barplot(x="recommendation_score", y="title", data=user_recommendations) # Plot the bar plot with recommendation score on x-axis and title on y-axis
plt.title(f"Top 10 Recommendations for User {user_id}") # Set the title with user id
plt.xlabel("Recommendation Score") # Set the x-axis label
plt.ylabel("Content Title") # Set the y-axis label
plt.show() # Show the plot

# Plot a heat map to show the recommendation scores for each user-content pair in a matrix form
recommendation_matrix = new_recommendation_df.pivot(index="user_id", columns="content_id", values="recommendation_score") # Pivot the dataframe into a matrix form with user id as rows, content id as columns, and recommendation score as values
plt.figure(figsize=(12,12)) # Set the figure size
sns.heatmap(recommendation_matrix, annot=True, cmap="Blues") # Plot the heat map with annotation and color map
plt.title("Recommendation Matrix") # Set the title
plt.xlabel("Content ID") # Set the x-axis label
plt.ylabel("User ID") # Set the y-axis label
plt.show() # Show the plot

# Provide some suggestions for improving the recommendation system based on the results

print("Some suggestions for improving the recommendation system are:")
print("- Optimize the hyperparameters of the models, such as learning rate, number of epochs, batch size, number of layers, number of units, and regularization.")
print("- Update the models regularly with new data and feedback from the users.")
print("- Incorporate other features and information into the models, such as content ratings, user reviews, user preferences, and user interests.")
print("- Experiment with different algorithms and architectures for the models, such as matrix factorization, neural collaborative filtering, or transformer networks.")

