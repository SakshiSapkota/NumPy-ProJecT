import numpy as np

# Step 1: Simulate 1000 dice rolls (values from 1 to 6)
rolls = np.random.randint(1, 7, size=1000)

# Step 2: Count how many times each number (1 to 6) appeared
counts = np.bincount(rolls)[1:]  # Skip index 0

# Step 3: Display frequency
print("🎲 Dice Roll Results (1000 Rolls):")
for i in range(6):
    print(f"Face {i+1}: {counts[i]} times")

# Step 4: Calculate and display probabilities
print("\n📊 Estimated Probabilities:")
probabilities = counts / 1000
for i in range(6):
    print(f"Probability of {i+1}: {probabilities[i]:.2f}")



