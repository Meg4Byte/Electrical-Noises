import random
import matplotlib.pyplot as plt

N = 10000  # Number of coin tosses
M = 10  # Number of toss sets
means = []

for _ in range(N):
    tosses = [random.choice(['H', 'T']) for _ in range(M)]
    num_heads = tosses.count('H')
    num_tails = tosses.count('T')
    mean = (num_heads - num_tails) / M
    means.append(mean)

plt.style.use('dark_background')

plt.hist(means, bins=50 , color='orange')
plt.xlabel('Mean')
plt.ylabel('Frequency')
plt.title('Distribution of Means for {} Coin Toss Sets'.format(N))
plt.show()
