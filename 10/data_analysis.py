# Import the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed user data from the CSV file
user_df = pd.read_csv("user_data_preprocessed.csv")

# Summarize the user data using descriptive statistics
print(user_df.describe())

# Plot the distribution of each numerical column using histograms
user_df.hist(figsize=(10,10))
plt.show()

# Plot the correlation matrix of the numerical columns using a heatmap
sns.heatmap(user_df.corr(), annot=True, cmap="Blues")
plt.show()

# Plot the relationship between two numerical columns using a scatter plot
sns.scatterplot(x="sessions", y="conversion_rate", data=user_df)
plt.show()

# Plot the frequency of each categorical column using bar charts
user_df["q1"].value_counts().plot(kind="bar")
plt.show()
user_df["q2"].value_counts().plot(kind="bar")
plt.show()
user_df["q3"].value_counts().plot(kind="bar")
plt.show()

# Plot the distribution of a numerical column by a categorical column using box plots
sns.boxplot(x="q1", y="bounce_rate", data=user_df)
plt.show()
sns.boxplot(x="q2", y="bounce_rate", data=user_df)
plt.show()
sns.boxplot(x="q3", y="bounce_rate", data=user_df)
plt.show()

# Plot the geographical location of the users using a map
# Note: this requires installing geopandas and geoplot libraries
import geopandas as gpd
import geoplot as gplt

# Load the world map shapefile
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Convert the user address column to a geoseries of points
user_points = gpd.GeoSeries.from_wkt(user_df["address"])

# Create a geodataframe from the user points and the user dataframe
user_gdf = gpd.GeoDataFrame(user_df, geometry=user_points)

# Plot the user points on the world map using a point plot
gplt.pointplot(user_gdf, hue="conversion_rate", cmap="Reds", legend=True, figsize=(15,15), ax=gplt.polyplot(world))
plt.show()
