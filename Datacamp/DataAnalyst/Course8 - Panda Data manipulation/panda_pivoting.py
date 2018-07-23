import pandas as pd

users = pd.DataFrame({'weekday':['Sun','Sun','Mon','Mon'],
                      'city':['Austin','Dallas','Austin','Dallas'],
                      'visitors':[139,237,326,456],
                      'signups':[7,12,3,5]  })


# Pivot the users DataFrame: visitors_pivot

visitors_pivot = users.pivot(index='weekday',columns='city',values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)

# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday',columns='city',values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday',columns='city')

# Print the pivoted DataFrame
print(pivot)

print(pivot.columns)

users = pd.DataFrame({'weekday':['Sun','Sun','Mon','Mon'],
                      'city':['Austin','Dallas','Austin','Dallas'],
                      'visitors':[139,237,326,456],
                      'signups':[7,12,3,5]  })

users.set_index(['city','weekday'],inplace=True)   
users.sort_index(inplace=True)

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))
                 
