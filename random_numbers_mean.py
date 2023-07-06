import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_points = 1000  # Number of random numbers to generate

# Generate random integers
random_numbers = np.random.randint(low=-num_points/2, high=num_points/2, size=num_points)

# Calculate mean average
mean_average = np.cumsum(random_numbers) / np.arange(1, num_points + 1)

# Set plot style with black background
plt.style.use('dark_background')

# Plotting
plt.figure(figsize=(10, 6))

# Plot random numbers
plt.stem(range(num_points), random_numbers, basefmt='g-', label='Random Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Random Numbers - Discrete Values')
#plt.grid(True)

# Plot mean average
plt.plot(range(num_points), mean_average, 'r-', label='Mean Average')
plt.legend()

plt.tight_layout()
plt.show()
