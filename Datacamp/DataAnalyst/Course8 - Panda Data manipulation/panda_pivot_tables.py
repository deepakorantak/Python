import pandas as pd

users = pd.DataFrame({'weekday':['Sun','Sun','Mon','Mon'],
                      'city':['Austin','Dallas','Austin','Dallas'],
                      'visitors':[139,237,326,456],
                      'signups':[7,12,3,5]  })

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = pd.pivot_table(users,index='weekday',columns='city')

# Print by_city_day
print(by_city_day)

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = pd.pivot_table(users,index='weekday',aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = pd.pivot_table(users,index='weekday',aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = pd.pivot_table(users,index='weekday',values=['signups','visitors'],aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = pd.pivot_table(users,index='weekday',values=['signups','visitors'],aggfunc=sum,margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)

