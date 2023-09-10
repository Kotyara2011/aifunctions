# Import the modules you need
import pandas as pd
import numpy as np

# Define the path to your data file
data_file = "data.csv"

# Load the data into a pandas dataframe
data = pd.read_csv(data_file)

# Define the size of your groups (e.g. 0.5 for 50% split)
group_size = 0.5

# Define a random seed for reproducibility
random_seed = 42

# Shuffle the data and split it into two groups
data = data.sample(frac=1, random_state=random_seed) # shuffle the data
split_index = int(len(data) * group_size) # calculate the split index
group_a = data[:split_index] # assign the first group
group_b = data[split_index:] # assign the second group

# Save the groups into separate files
group_a.to_csv("group_a.csv", index=False)
group_b.to_csv("group_b.csv", index=False)

# Print a message to confirm the split
print(f"Split the data into two groups of size {group_size}")
print(f"Group A has {len(group_a)} rows and Group B has {len(group_b)} rows")
