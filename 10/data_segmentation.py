# Import the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

# Load the preprocessed user data from the CSV file
user_df = pd.read_csv("user_data_preprocessed.csv")

# Define the range of possible number of segments (clusters)
k_range = range(2, 11)

# Create an empty list to store the scores for each number of segments
scores = []

# Loop through each number of segments and apply K-Means clustering
for k in k_range:
    # Create a K-Means object with k clusters
    kmeans = KMeans(n_clusters=k, random_state=42)
    # Fit the K-Means object to the user data
    kmeans.fit(user_df)
    # Predict the cluster labels for each user
    labels = kmeans.predict(user_df)
    # Calculate the silhouette score for the clustering result
    silhouette = silhouette_score(user_df, labels)
    # Append the silhouette score to the scores list
    scores.append(silhouette)

# Plot the scores against the number of segments using a line plot
plt.plot(k_range, scores)
plt.xlabel("Number of segments")
plt.ylabel("Silhouette score")
plt.show()

# Choose the optimal number of segments based on the highest silhouette score
optimal_k = k_range[np.argmax(scores)]
print(f"The optimal number of segments is {optimal_k}.")

# Create a K-Means object with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
# Fit the K-Means object to the user data
kmeans.fit(user_df)
# Predict the cluster labels for each user
labels = kmeans.predict(user_df)

# Alternatively, you can try other clustering algorithms such as hierarchical or DBSCAN
# For example, to use hierarchical clustering with optimal_k clusters and ward linkage:
# hier = AgglomerativeClustering(n_clusters=optimal_k, linkage="ward")
# labels = hier.fit_predict(user_df)

# Or, to use DBSCAN with 0.5 epsilon and 5 min_samples:
# dbscan = DBSCAN(eps=0.5, min_samples=5)
# labels = dbscan.fit_predict(user_df)

# Evaluate the quality of the segmentation using other metrics such as Davies-Bouldin index or Calinski-Harabasz index
dbi = davies_bouldin_score(user_df, labels)
chi = calinski_harabasz_score(user_df, labels)
print(f"The Davies-Bouldin index is {dbi:.2f}.")
print(f"The Calinski-Harabasz index is {chi:.2f}.")

# Save the cluster labels to a new column in the user dataframe
user_df["segment"] = labels

# Save the user dataframe with the segment column to a new CSV file
user_df.to_csv("user_data_segmented.csv", index=False)

# Print a success message
print("User data segmented and saved to user_data_segmented.csv.")
