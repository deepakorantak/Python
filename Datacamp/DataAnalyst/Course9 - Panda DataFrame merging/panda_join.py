import pandas as pd

filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course9 - Panda DataFrame merging\\'
managers = pd.read_csv(filepath+'manager_state.csv')
revenue = pd.read_csv(filepath+'revenue_state.csv')
sales = pd.read_csv(filepath+'sales_state.csv')

revenue_and_sales = pd.merge(revenue,sales,on=['city', 'state'],how='right')
print(revenue_and_sales)


sales_and_managers =  pd.merge(sales,managers,left_on=['city', 'state'],right_on=['branch', 'state'],how='left')
print(sales_and_managers)

# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers,revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers,revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers,revenue_and_sales,on=['city','state'],how='outer')

# Print merge_outer_on
print(merge_outer_on)

