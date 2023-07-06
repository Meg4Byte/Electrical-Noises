import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(0)

# Parameters
n_numbers = 1000
generation_interval = 1e-4
#interval_range = (-n_numbers/2 , n_numbers/2)
interval_range = (0 , 2)

# Initialize data arrays
x = []
y = []
mean_values = []

# Set plot style with black background
plt.style.use('dark_background')

# Create the figure and axis
fig, ax = plt.subplots()

# Generate and plot random numbers
for i in range(n_numbers):
    # Generate a random number
    rand_num = np.random.randint(interval_range[0] , interval_range[1])
    
    ##print(rand_num)
    # Append the number and its index to the data arrays
    x.append(i * generation_interval)
    y.append(rand_num)
    
    # Plot the random number as a dot
    ax.plot(i * generation_interval, rand_num, marker='x' , markersize = 2,  color='orange')
    
    # Update the mean
    mean = np.mean(y)
    mean_values.append(mean)
    
    # Plot the mean as a line
    ax.plot(x, mean_values, 'r-' , lw=1)
    
    # Update the title with the mean value
    ax.set_title(f'Mean: {mean:.2f}')
    
    # Set x and y limits
    ax.set_xlim(0, n_numbers * generation_interval)
    ax.set_ylim(-0.25 , 1.25) 
    
    # Pause to observe the plot
    plt.pause(generation_interval)

# Save the plot as a PNG image
plt.savefig('random_numbers_plot.png')

# Show the plot
plt.show()
