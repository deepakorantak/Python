import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
setosa_petal_length = np.array(df.loc[df['species'] == 'setosa','petal length (cm)'])
virginica_petal_length = np.array(df.loc[df['species'] == 'virginica','petal length (cm)'])

# Compute ECDFs
x_set,y_set = ecdf(setosa_petal_length)
x_vers,y_vers = ecdf(versicolor_petal_length)
x_virg,y_virg = ecdf(virginica_petal_length)


# Plot all ECDFs on the same plot
_ = plt.plot(x_set,y_set,marker='.',linestyle = 'none')
_ = plt.plot(x_vers,y_vers,marker='.',linestyle = 'none')
_ = plt.plot(x_virg,y_virg,marker='.',linestyle = 'none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()

