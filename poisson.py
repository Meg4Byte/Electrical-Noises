import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Poisson distribution
mu = 6
x_poisson = np.arange(0, 20)


# Create a vectorized version of the factorial function
factorial_vec = np.vectorize(np.math.factorial)

# Calculate the values for the Poisson distribution
poisson = np.exp(-mu) * np.power(mu, x_poisson) / factorial_vec(x_poisson)

# Create a normal distribution with the same mean and variance as the Poisson distribution
sigma = np.sqrt(mu)
x_normal = np.linspace(-10, 20, 100)
normal = np.exp(-0.5*np.power((x_normal - mu)/sigma, 2)) / (sigma * np.sqrt(2*np.pi))

# Plot the distributions on the same graph
plt.style.use('dark_background')
plt.plot(x_poisson, poisson, 'bo', ms=4, label='Poisson distribution')
plt.plot(x_normal, normal, 'g-', lw=1, label='Gaussian distribution')
plt.legend(loc='best')
plt.show()
