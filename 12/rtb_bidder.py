# Import the required libraries
import requests
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load the model from the saved file
model = keras.models.load_model("rtb_model.h5") # Load the trained model

# Define the bid URL and headers
bid_url = "https://api.bing.com/v7.0/bid" # Bing bid API
headers = {"Ocp-Apim-Subscription-Key": "some_key"} # Subscription key for Bing API

# Define the campaign goals and constraints
budget = 1000 # Total budget in dollars
max_bid = 10 # Maximum bid in dollars
target_ctr = 0.1 # Target click-through rate

# Define the variables for monitoring the campaign performance
spent = 0 # Total amount spent in dollars
won = 0 # Total number of impressions won
clicked = 0 # Total number of impressions clicked
ctr = 0 # Current click-through rate

# Loop until the budget is exhausted or the target CTR is reached
while spent < budget and ctr < target_ctr:
    # Get a bid request from the bid API
    bid_request = requests.get(bid_url, headers=headers) # Bid request response

    # Check if the response is successful
    if bid_request.status_code == 200:
        # Parse the response as a JSON object
        bid_data = bid_request.json() # Bid data

        # Extract the relevant information from the data
        impression_id = bid_data["impression_id"] # Unique identifier for the impression
        user_profile = bid_data["user_profile"] # User profile information
        ad_relevance = bid_data["ad_relevance"] # Ad relevance score
        historical_performance = bid_data["historical_performance"] # Historical performance score
        auction_type = bid_data["auction_type"] # Auction type (0 for first-price, 1 for second-price)
        floor_price = bid_data["floor_price"] # Floor price in dollars

        # Create a dataframe with the extracted information
        columns = ["user_profile", "ad_relevance", "historical_performance", "auction_type", "floor_price"] # Columns of the dataframe
        df = pd.DataFrame([user_profile, ad_relevance, historical_performance, auction_type, floor_price], columns=columns) # Dataframe with one row

        # Normalize the data to [0, 1] range using the same min and max values as in rtb_data.py
        df = (df - df.min()) / (df.max() - df.min()) # Normalized dataframe

        # Generate a prediction for the average CTR using the model
        average_ctr = model.predict(df) # Predicted average_CTR value

        # Calculate the optimal bid price using a linear bidding strategy
        bid_price = average_ctr / target_ctr * max_bid # Bid price formula

        # Check if the bid price is within the budget and the maximum bid constraints
        if bid_price <= budget - spent and bid_price <= max_bid:
            # Create a bid response with the impression ID and the bid price
            bid_response = {"impression_id": impression_id, "bid_price": bid_price} # Bid response object

            # Send the bid response to the bid API using a POST request
            post_response = requests.post(bid_url, json=bid_response, headers=headers) # Post response

            # Check if the post response is successful
            if post_response.status_code == 200:
                # Parse the post response as a JSON object
                post_data = post_response.json() # Post data

                # Extract the relevant information from the post data
                result = post_data["result"] # Result of the auction (0 for lost, 1 for won)
                final_price = post_data["final_price"] # Final price paid in dollars
                click = post_data["click"] # Click event (0 for no click, 1 for click)

                # Update the campaign performance variables based on the result
                if result == 1: # If won the impression
                    spent += final_price # Update the spent amount
                    won += 1 # Update the won count
                    if click == 1: # If clicked on the impression
                        clicked += 1 # Update the clicked count
                
                # Calculate the current CTR based on the clicked and won counts
                ctr = clicked / won if won > 0 else 0 # CTR formula

                # Print the current campaign performance metrics
                print(f"Spent: ${spent:.2f}")
                print(f"Won: {won}")
                print(f"Clicked: {clicked}")
                print(f"CTR: {ctr:.4f}")

            else:
                # Print an error message if the post response is unsuccessful
                print("An error occurred while sending the bid response. Please check the status code and try again.")
        
        else:
            # Print a message if the bid price is not within the constraints
            print("The bid price is too high or the budget is too low. No bid response sent.")

    else:
        # Print an error message if the bid request response is unsuccessful
        print("An error occurred while fetching the bid request. Please check the status code and try again.")
