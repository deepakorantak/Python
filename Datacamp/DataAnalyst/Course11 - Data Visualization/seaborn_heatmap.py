import matplotlib.plyplot as plt
import pandas as pd
import seaborn as sns

# Print the covariance matrix
print(cov_matrix)

# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)

# Display the heatmap
plt.show()
