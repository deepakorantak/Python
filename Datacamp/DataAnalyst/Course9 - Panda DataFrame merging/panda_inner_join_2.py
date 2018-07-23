import pandas as  pd

filepath = 'D:\Deepa\Training\GitHub\Python\Datacamp\DataAnalyst\Course9 - Panda DataFrame merging\\'
china = pd.read_csv(filepath+'china.csv',index_col='Year',parse_dates=True)
us = pd.read_csv(filepath+'us.csv',index_col='Year',parse_dates=True)

# print(china.info())
# print(us.info())

# Resample and tidy china: china_annual

china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],axis=1,join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())