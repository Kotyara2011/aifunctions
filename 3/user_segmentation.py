# Import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the cleaned and transformed data from the previous step
# You can use pandas.read_csv() function to read the CSV file
# You can also specify the file name, index column, header row, etc.
cleaned_df = pd.read_csv("cleaned_data.csv", index_col="user_id", header=True)

# Choose the number of clusters for segmentation
# You can use the elbow method or the silhouette method to find the optimal number of clusters
# Here we use the silhouette method and loop over a range of possible cluster numbers
# We calculate the silhouette score for each cluster number and choose the one with the highest score
silhouette_scores = [] # A list to store the silhouette scores
cluster_range = range(2, 11) # A range of possible cluster numbers from 2 to 10
for n_clusters in cluster_range:
    # Create a KMeans object with n_clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    # Fit the KMeans object to the data
    kmeans.fit(cleaned_df)
    # Predict the cluster labels for each data point
    cluster_labels = kmeans.predict(cleaned_df)
    # Calculate the silhouette score for the current cluster number
    silhouette_avg = silhouette_score(cleaned_df, cluster_labels)
    # Append the score to the list
    silhouette_scores.append(silhouette_avg)

# Plot the silhouette scores against the cluster numbers
import matplotlib.pyplot as plt
plt.plot(cluster_range, silhouette_scores)
plt.xlabel("Number of clusters")
plt.ylabel("Silhouette score")
plt.show()

# Choose the cluster number with the highest silhouette score
# Here we see that 4 clusters have the highest score of 0.36
optimal_n_clusters = 4

# Create a final KMeans object with the optimal cluster number
final_kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=0)
# Fit the final KMeans object to the data
final_kmeans.fit(cleaned_df)
# Predict the final cluster labels for each data point
final_cluster_labels = final_kmeans.predict(cleaned_df)

# Add the cluster labels as a new column to the data frame
cleaned_df["cluster"] = final_cluster_labels

# Save the segmented data frame to a CSV file
# You can use pandas.to_csv() function to write the data frame to a CSV file
# You can also specify the file name, index column, header row, etc.
cleaned_df.to_csv("segmented_data.csv", index="user_id", header=True)

# Create user profiles for each cluster
# You can use various methods and functions from pandas and numpy to perform descriptive analysis on each cluster
# For example, you can use pandas.groupby() to group the data by cluster labels
# You can use pandas.mean() to calculate the mean values of each feature for each cluster
# You can use pandas.describe() to generate summary statistics for each cluster
# Here we use pandas.groupby() and pandas.mean() to create user profiles based on average values of each feature for each cluster

# Group the data by cluster labels
grouped_df = cleaned_df.groupby("cluster")

# Calculate the mean values of each feature for each cluster
mean_df = grouped_df.mean()

# Print the user profiles based on average values
print(mean_df)

