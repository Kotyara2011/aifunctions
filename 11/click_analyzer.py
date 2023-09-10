# Import modules
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Load the processed data from click_data.py
click_data = pd.read_csv("click_data_processed.csv")

# Encode categorical features as numerical values
le = LabelEncoder()
click_data["source"] = le.fit_transform(click_data["source"])
click_data["device"] = le.fit_transform(click_data["device"])
click_data["ip_address"] = le.fit_transform(click_data["ip_address"])
click_data["outcome"] = le.fit_transform(click_data["outcome"])

# Apply anomaly detection using Isolation Forest algorithm
model = IsolationForest(contamination=0.05)
model.fit(click_data[["duration", "cost", "revenue", "outcome"]])
click_data["anomaly"] = model.predict(click_data[["duration", "cost", "revenue", "outcome"]])
click_data["anomaly"] = click_data["anomaly"].map({1: 0, -1: 1})

# Plot the distribution of clicks by source and device
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
click_data["source"].value_counts().plot(kind="bar")
plt.xlabel("Source")
plt.ylabel("Count")
plt.title("Clicks by Source")
plt.subplot(1, 2, 2)
click_data["device"].value_counts().plot(kind="bar")
plt.xlabel("Device")
plt.ylabel("Count")
plt.title("Clicks by Device")
plt.tight_layout()
plt.show()

# Plot the distribution of clicks by ip address and anomaly
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
click_data["ip_address"].value_counts().head(10).plot(kind="bar")
plt.xlabel("IP Address")
plt.ylabel("Count")
plt.title("Top 10 IP Addresses by Clicks")
plt.subplot(1, 2, 2)
click_data["anomaly"].value_counts().plot(kind="pie", labels=["Normal", "Anomalous"], autopct="%1.1f%%")
plt.title("Anomaly Detection Results")
plt.tight_layout()
plt.show()

# Generate a report that summarizes the analysis results
report = f"""
The click data contains {len(click_data)} records with {len(click_data.columns)} features.
The features are: {', '.join(click_data.columns)}.

The click data has {len(click_data["source"].unique())} unique sources and {len(click_data["device"].unique())} unique devices.
The most frequent source is {le.inverse_transform([click_data["source"].mode().iloc[0]])[0]} with {click_data["source"].value_counts().max()} clicks.
The most frequent device is {le.inverse_transform([click_data["device"].mode().iloc[0]])[0]} with {click_data["device"].value_counts().max()} clicks.

The click data has {len(click_data["ip_address"].unique())} unique IP addresses.
The most frequent IP address is {le.inverse_transform([click_data["ip_address"].mode().iloc[0]])[0]} with {click_data["ip_address"].value_counts().max()} clicks.

The anomaly detection algorithm identified {click_data["anomaly"].sum()} anomalous clicks, which is {click_data["anomaly"].mean()*100:.2f}% of the total clicks.
The anomalous clicks have different patterns from the normal clicks in terms of duration, cost, revenue, and outcome.
"""

# Print the report
print(report)
