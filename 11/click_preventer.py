# Import modules
import pandas as pd
import requests

# Load the processed data from click_data.py
click_data = pd.read_csv("click_data_processed.csv")

# Load the prediction results from click_model.py
click_pred = pd.read_csv("click_pred.csv")

# Merge the data and the prediction results
click_data = pd.merge(click_data, click_pred, on="id")

# Define a threshold for fraud probability
threshold = 0.8

# Filter the clicks that have fraud probability above the threshold
fraud_clicks = click_data[click_data["fraud_prob"] > threshold]

# Print the number and percentage of fraud clicks
print(f"There are {len(fraud_clicks)} fraud clicks, which is {len(fraud_clicks)/len(click_data)*100:.2f}% of the total clicks.")

# Define a list of actions to prevent click fraud
actions = ["block", "bid", "report"]

# Define a function to block certain IP addresses, domains, or devices
def block(items, column):
    # Create an empty list to store the blocked items
    blocked = []
    # Loop through the items to block
    for item in items:
        # Check if the item is already in the blocked list
        if item not in blocked:
            # Append the item to the blocked list
            blocked.append(item)
            # Print a message to confirm the action
            print(f"Blocked {column}: {item}")
    # Return the blocked list
    return blocked

# Define a function to adjust the bidding strategy based on fraud probability
def bid(clicks):
    # Create an empty list to store the adjusted bids
    adjusted = []
    # Loop through the clicks to adjust the bids
    for index, row in clicks.iterrows():
        # Get the original bid and the fraud probability
        original_bid = row["cost"]
        fraud_prob = row["fraud_prob"]
        # Calculate the adjusted bid by multiplying the original bid by (1 - fraud probability)
        adjusted_bid = original_bid * (1 - fraud_prob)
        # Append the adjusted bid to the adjusted list
        adjusted.append(adjusted_bid)
        # Print a message to confirm the action
        print(f"Adjusted bid from {original_bid:.2f} to {adjusted_bid:.2f} for click id: {row['id']}")
    # Return the adjusted list
    return adjusted

# Define a function to report the fraudsters to the authorities
def report(clicks):
    # Create an empty list to store the reported items
    reported = []
    # Loop through the clicks to report
    for index, row in clicks.iterrows():
        # Get the IP address and the fraud probability
        ip_address = row["ip_address"]
        fraud_prob = row["fraud_prob"]
        # Check if the IP address is already in the reported list
        if ip_address not in reported:
            # Append the IP address to the reported list
            reported.append(ip_address)
            # Send a request to a fake API endpoint to report the IP address (this is just for illustration purposes, not a real API call)
            response = requests.post("https://fake-api.com/report", data={"ip_address": ip_address, "fraud_prob": fraud_prob})
            # Print a message to confirm the action
            print(f"Reported IP address: {ip_address} with fraud probability: {fraud_prob:.2f}")
    # Return the reported list
    return reported

# Loop through the actions and apply them to the fraud clicks
for action in actions:
    # Check which action to take
    if action == "block":
        # Block certain IP addresses, domains, or devices based on some criteria (this is just an example, not a definitive rule)
        block(fraud_clicks["ip_address"].unique(), "IP address")
        block(fraud_clicks[fraud_clicks["source"] == "bot"]["device"].unique(), "device")
        block(fraud_clicks[fraud_clicks["outcome"] == "bounce"]["domain"].unique(), "domain")
    elif action == "bid":
        # Adjust the bidding strategy based on fraud probability
        bid(fraud_clicks)
    elif action == "report":
        # Report the fraudsters to the authorities
        report(fraud_clicks)
