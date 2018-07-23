import pandas as pd

filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course9 - Panda DataFrame merging\\'
managers = pd.read_csv(filepath+'manager_state.csv')
revenue = pd.read_csv(filepath+'revenue_state.csv')

combined = pd.merge(revenue,managers,left_on='city',right_on='branch')

print(combined)