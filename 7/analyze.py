# Import the modules you need
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Define the path to your report file
report_file = "report.csv"

# Load the report data into a pandas dataframe
report = pd.read_csv(report_file)

# Calculate the CTR for each variant
report["CTR"] = report["adClicks"] / report["sessions"]

# Calculate the mean and standard deviation of CTR for each variant
mean_a = report[report["experimentVariant"] == "A"]["CTR"].mean()
std_a = report[report["experimentVariant"] == "A"]["CTR"].std()
mean_b = report[report["experimentVariant"] == "B"]["CTR"].mean()
std_b = report[report["experimentVariant"] == "B"]["CTR"].std()

# Print the summary statistics
print(f"Summary statistics for variant A: mean = {mean_a:.4f}, std = {std_a:.4f}")
print(f"Summary statistics for variant B: mean = {mean_b:.4f}, std = {std_b:.4f}")

# Plot the CTR over time for each variant
plt.plot(report[report["experimentVariant"] == "A"]["date"], report[report["experimentVariant"] == "A"]["CTR"], label="Variant A")
plt.plot(report[report["experimentVariant"] == "B"]["date"], report[report["experimentVariant"] == "B"]["CTR"], label="Variant B")
plt.xlabel("Date")
plt.ylabel("CTR")
plt.title("CTR over time for each variant")
plt.legend()
plt.show()

# Perform a t-test to compare the CTR of the two variants
t_stat, p_value = stats.ttest_ind(report[report["experimentVariant"] == "A"]["CTR"], report[report["experimentVariant"] == "B"]["CTR"])

# Define the significance level (alpha)
alpha = 0.05

# Print the t-test results
print(f"T-test results: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")

# Draw conclusions based on the p-value and alpha
if p_value < alpha:
    print(f"The difference in CTR between the two variants is statistically significant at alpha = {alpha}")
    if mean_a > mean_b:
        print(f"Variant A has a higher CTR than variant B by {mean_a - mean_b:.4f}")
    else:
        print(f"Variant B has a higher CTR than variant A by {mean_b - mean_a:.4f}")
else:
    print(f"The difference in CTR between the two variants is not statistically significant at alpha = {alpha}")
