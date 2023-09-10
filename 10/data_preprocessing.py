# Import the required modules
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the user data from the CSV file
user_df = pd.read_csv("user_data.csv")

# Check the summary of the user data
print(user_df.describe())

# Check the number of missing values in each column
print(user_df.isnull().sum())

# Drop the rows with missing values
user_df = user_df.dropna()

# Check for duplicates and drop them if any
user_df = user_df.drop_duplicates()

# Check for outliers using boxplots and remove them if any
for col in user_df.columns:
    sns.boxplot(x=user_df[col])
    plt.show()
    # Remove the outliers using interquartile range method
    Q1 = user_df[col].quantile(0.25)
    Q3 = user_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    user_df = user_df[(user_df[col] > lower_bound) & (user_df[col] < upper_bound)]

# Create dummy variables for categorical columns
user_df = pd.get_dummies(user_df, drop_first=True)

# Normalize and scale the numerical columns using StandardScaler
scaler = StandardScaler()
user_df[user_df.columns] = scaler.fit_transform(user_df[user_df.columns])

# Save the preprocessed user data to a new CSV file
user_df.to_csv("user_data_preprocessed.csv", index=False)

# Print a success message
print("User data preprocessed and saved to user_data_preprocessed.csv.")
