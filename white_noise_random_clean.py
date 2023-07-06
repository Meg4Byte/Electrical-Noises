import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_points = 200  # Number of random numbers to generate

# Generate random integers
random_numbers = np.random.randint(low=0, high=2, size=num_points)

# Calculate mean average
mean_average = np.cumsum(random_numbers) / np.arange(1, num_points + 1)

# Set plot style with black background
plt.style.use('dark_background')

# Plotting
plt.figure(figsize=(10, 6))
#plt.style.use('dark_background')  # Set black background

# Plot random numbers as dots
plt.scatter(range(num_points), random_numbers, marker='x' , c='cyan', label='Random Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Random Numbers - Discrete Values')
plt.grid(True)

# Plot mean average
plt.plot(range(num_points), mean_average, 'magenta', label='Mean Average')
plt.legend()

plt.tight_layout()
plt.show()
