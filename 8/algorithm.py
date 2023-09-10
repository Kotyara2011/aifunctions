# Import the modules you need
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

# Load the data from the previous step
from data import data

# Load the objective and constraints from the previous step
from objective import problem, p, x

# Solve the optimization problem using cvxpy
problem.solve()

# Print the optimal prices and impressions
print(f"Optimal prices: {p.value}")
print(f"Optimal impressions: {x.value}")

# Plot the optimal prices and impressions for each ad
plt.scatter(p.value, x.value)
plt.xlabel("Price")
plt.ylabel("Impression")
plt.title("Optimal prices and impressions for each ad")
plt.show()

# Define a function to simulate the feedback from the advertisers and users
def simulate_feedback(p, x):
    # Add some random noise to the prices and impressions
    p = p + np.random.normal(0, 0.1, size=p.shape)
    x = x + np.random.normal(0, 10, size=x.shape)

    # Calculate the revenue and cost for each ad
    r = p * (d - x) # revenue
    c = c * x # cost

    # Return the feedback as a dictionary
    feedback = {
        "prices": p,
        "impressions": x,
        "revenue": r,
        "cost": c
    }

    return feedback

# Define a function to update the prices based on the feedback
def update_prices(p, feedback):
    # Define a learning rate (alpha)
    alpha = 0.01

    # Calculate the gradient of the revenue with respect to the prices
    grad_r = feedback["revenue"] - feedback["cost"]

    # Update the prices using gradient ascent
    p = p + alpha * grad_r

    # Return the updated prices
    return p

# Define a number of iterations to run the algorithm
n_iter = 100

# Initialize a list to store the history of prices and impressions
history = []

# Loop through each iteration
for i in range(n_iter):
    # Simulate the feedback from the advertisers and users
    feedback = simulate_feedback(p.value, x.value)

    # Update the prices based on the feedback
    p.value = update_prices(p.value, feedback)

    # Solve the optimization problem with the updated prices
    problem.solve()

    # Print the optimal prices and impressions for each iteration
    print(f"Iteration {i+1}:")
    print(f"Optimal prices: {p.value}")
    print(f"Optimal impressions: {x.value}")

    # Append the optimal prices and impressions to the history list
    history.append((p.value, x.value))

# Plot the history of prices and impressions for each ad
for i in range(n):
    plt.plot([h[0][i] for h in history], [h[1][i] for h in history], label=f"Ad {i+1}")
plt.xlabel("Price")
plt.ylabel("Impression")
plt.title("History of prices and impressions for each ad")
plt.legend()
plt.show()
