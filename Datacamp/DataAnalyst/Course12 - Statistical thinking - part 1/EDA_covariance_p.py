# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course12 - Statistical thinking - part 1\\'
df = pd.read_csv(filepath+'species.csv')

versicolor_petal_length = np.array(df.loc[df['species'] == 'versicolor','petal length (cm)'])
versicolor_petal_width = np.array(df.loc[df['species'] == 'versicolor','petal width (cm)'])

#print(versicolor_petal_width)

sns.set()
# Make a scatter plot
plt.plot(versicolor_petal_length,versicolor_petal_width,marker = '.',linestyle='none')


# Label the axes
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')


# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length,versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length,versicolor_petal_width)

# Print the result
print(r)
