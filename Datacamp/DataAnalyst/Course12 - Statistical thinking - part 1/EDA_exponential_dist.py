import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)
    print(t1)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)
    print(t2)

    return t1 + t2

sns.set()
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,100000)
print(waiting_times)

# Make the histogram
plt.hist(waiting_times,bins=100,normed=True,histtype='step')


# Label axes
plt.xlabel('waiting time for no-hitter and cycle')
plt.ylabel('probability')

# Show the plot
plt.show()    