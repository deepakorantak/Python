import pandas as pd
import numpy as np


filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course12 - Statistical thinking - part 1\\'
df = pd.read_csv(filepath+'species.csv')

versicolor_petal_length = np.array(df.loc[df['species'] == 'versicolor','petal length (cm)'])

# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit,variance_np)

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))

