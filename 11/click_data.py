# Import modules
import pandas as pd
import glob

# Define the path to the click data files
path = "/path/to/files/*.csv"

# Load all csv files in the path
files = glob.glob(path)

# Concatenate files to a new dataframe
click_data = pd.concat([pd.read_csv(file) for file in files])

# Print the shape and summary of the data
print(click_data.shape)
print(click_data.info())

# Remove duplicates
click_data.drop_duplicates(inplace=True)

# Remove outliers based on click duration
click_data = click_data[click_data["duration"] < click_data["duration"].quantile(0.99)]

# Fill missing values with median for numerical columns
num_cols = ["duration", "cost", "revenue"]
click_data[num_cols] = click_data[num_cols].fillna(click_data[num_cols].median())

# Fill missing values with mode for categorical columns
cat_cols = ["source", "device", "ip_address", "outcome"]
click_data[cat_cols] = click_data[cat_cols].fillna(click_data[cat_cols].mode().iloc[0])

# Save the processed data to a new csv file
click_data.to_csv("click_data_processed.csv", index=False)
