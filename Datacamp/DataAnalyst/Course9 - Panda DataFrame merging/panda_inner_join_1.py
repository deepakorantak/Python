import pandas as pd
filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course9 - Panda DataFrame merging\\'
bronze = pd.read_csv(filepath+'bronze.csv',index_col='Country')
silver = pd.read_csv(filepath+'silver.csv',index_col='Country')
gold = pd.read_csv(filepath+'gold.csv',index_col='Country')

# print(bronze)
# print(silver)
# print(gold)

# Create the list of DataFrames: medal_list
medal_list = [bronze, silver,  gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list,keys=['bronze', 'silver', 'gold'],axis=1,join='inner')

# Print medals
print(medals)



