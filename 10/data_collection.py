# Import the required modules
import requests
import pandas as pd
import json

# Define the sources of user data
crm_url = "https://example.com/api/crm" # CRM system API endpoint
pa_url = "https://example.com/api/pa" # Product analytics tool API endpoint
survey_url = "https://example.com/api/survey" # Survey platform API endpoint
sm_url = "https://example.com/api/sm" # Social media platform API endpoint

# Define the parameters for each source
crm_params = {"api_key": "xxxxx", "fields": ["name", "email", "phone", "address"]} # CRM fields to retrieve
pa_params = {"api_key": "xxxxx", "metrics": ["sessions", "pageviews", "bounce_rate", "conversion_rate"]} # Product analytics metrics to retrieve
survey_params = {"api_key": "xxxxx", "questions": ["q1", "q2", "q3"]} # Survey questions to retrieve
sm_params = {"api_key": "xxxxx", "keywords": ["product_name", "brand_name"]} # Social media keywords to retrieve

# Define the output file name
output_file = "user_data.csv"

# Create an empty list to store the user data
user_data = []

# Loop through each source and collect the user data
for source, url, params in zip(["CRM", "PA", "Survey", "SM"], [crm_url, pa_url, survey_url, sm_url], [crm_params, pa_params, survey_params, sm_params]):
    print(f"Collecting user data from {source}...")
    # Send a GET request to the source API and get the response as JSON
    response = requests.get(url, params=params).json()
    # Check if the response is successful
    if response["status"] == "success":
        # Get the data from the response
        data = response["data"]
        # Append the data to the user data list
        user_data.append(data)
        print(f"Collected {len(data)} records from {source}.")
    else:
        # Print an error message if the response is not successful
        print(f"Error: {response['message']}")

# Concatenate the user data from different sources into a single dataframe
user_df = pd.concat(user_data, axis=1)

# Save the user dataframe to a CSV file
user_df.to_csv(output_file, index=False)

# Print a success message
print(f"User data saved to {output_file}.")
