# Import pandas library
import pandas as pd

# Load the historical revenue data from a csv file
df = pd.read_csv("revenue_data.csv")

# Drop columns that are not useful for the AI model, such as ID, name, etc.
df = df.drop(["ID", "name"], axis=1)

# Drop rows with missing values in any column
df = df.dropna()

# Convert categorical columns to numerical values using one-hot encoding
df = pd.get_dummies(df, columns=["location", "product"])

# Normalize numerical columns to have values between 0 and 1
df = (df - df.min()) / (df.max() - df.min())

# Save the cleaned and transformed dataset to a new csv file
df.to_csv("cleaned_data.csv", index=False)
