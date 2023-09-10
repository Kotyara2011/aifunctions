# Import pandas library
import pandas as pd

# Define the names of the columns in the CSV files
columns = ["campaign_id", "user_id", "device_id", "location_id", "timestamp", "interaction", "label"]

# Define the paths of the CSV files from different sources
source1 = "source1.csv"
source2 = "source2.csv"
source3 = "source3.csv"

# Read the CSV files into pandas dataframes
df1 = pd.read_csv(source1, names=columns)
df2 = pd.read_csv(source2, names=columns)
df3 = pd.read_csv(source3, names=columns)

# Concatenate the dataframes into one dataframe
df = pd.concat([df1, df2, df3], ignore_index=True)

# Drop any rows that have missing values
df = df.dropna()

# Save the dataframe to a new CSV file
df.to_csv("data.csv", index=False)
