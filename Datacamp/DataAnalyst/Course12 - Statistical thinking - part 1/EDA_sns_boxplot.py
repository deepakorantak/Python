# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course12 - Statistical thinking - part 1\\'
df = pd.read_csv(filepath+'species.csv')

versicolor_petal_length = np.array(df.loc[df['species'] == 'versicolor','petal length (cm)'])

# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25.0,50.0,75.0,97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length,percentiles)

# Print the result
print(ptiles_vers)

# Compute ECDFs
x_vers,y_vers = ecdf(versicolor_petal_length)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D',color='red',
         linestyle='none')

# Show the plot
plt.show()

plt.clf()

# Create box plot with Seaborn's default settings
sns.boxplot(x='species',y='petal length (cm)',data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')


# Show the plot
plt.show()
