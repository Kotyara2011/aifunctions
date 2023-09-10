# Import the necessary libraries
import pandas as pd
import numpy as np

# Define the data sources and file paths
web_data = "web_data.csv" # The file path for the web analytics data
social_data = "social_data.csv" # The file path for the social media data
sensor_data = "sensor_data.csv" # The file path for the sensor data

# Read the data from the sources and store them in dataframes
web_df = pd.read_csv(web_data) # The dataframe for the web analytics data
social_df = pd.read_csv(social_data) # The dataframe for the social media data
sensor_df = pd.read_csv(sensor_data) # The dataframe for the sensor data

# Merge the dataframes into one based on a common key, such as session_id or user_id
# You may need to rename or drop some columns to avoid duplication or inconsistency
traffic_df = pd.merge(web_df, social_df, on="session_id", how="outer") # Merge web and social data
traffic_df = pd.merge(traffic_df, sensor_df, on="user_id", how="outer") # Merge with sensor data

# Perform some data cleaning and preprocessing steps
traffic_df = traffic_df.dropna() # Drop rows with missing values
traffic_df = traffic_df[traffic_df["duration"] > 0] # Drop rows with zero or negative duration
traffic_df = traffic_df[traffic_df["bounce_rate"] <= 1] # Drop rows with bounce rate greater than 1
traffic_df = traffic_df[traffic_df["conversion_rate"] <= 1] # Drop rows with conversion rate greater than 1
traffic_df = traffic_df[(np.abs(traffic_df["duration"] - traffic_df["duration"].mean()) <= (3 * traffic_df["duration"].std()))] # Remove outliers based on duration using 3 standard deviations rule
traffic_df["source"] = traffic_df["source"].str.lower() # Convert source column to lowercase
traffic_df["location"] = traffic_df["location"].str.title() # Capitalize location column

# Normalize the numerical columns using min-max scaling
num_cols = ["duration", "bounce_rate", "conversion_rate", "wind", "humidity"] # The numerical columns to normalize
traffic_df[num_cols] = (traffic_df[num_cols] - traffic_df[num_cols].min()) / (traffic_df[num_cols].max() - traffic_df[num_cols].min()) # Apply min-max scaling

# Save the processed dataframe to a new file
traffic_df.to_csv("processed_traffic_data.csv", index=False) # Save the file without row indices

