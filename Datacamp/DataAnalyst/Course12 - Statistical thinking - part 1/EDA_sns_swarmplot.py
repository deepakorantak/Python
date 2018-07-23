# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course12 - Statistical thinking - part 1\\'
df = pd.read_csv(filepath+'species.csv')

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species',y='petal length (cm)',data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()