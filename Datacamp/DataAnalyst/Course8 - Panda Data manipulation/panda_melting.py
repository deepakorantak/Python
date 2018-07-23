import pandas as pd

visitors_by_city_weekday = pd.DataFrame({'weekday':['Mon','Sun'],
                                         'Austin':[326,139],
                                         'Dallas':[456,237]})

visitors_by_city_weekday.set_index('weekday',inplace=True)
visitors_by_city_weekday.sort_index(inplace=True)
visitors_by_city_weekday.index.name='weekday'
visitors_by_city_weekday.columns.name='city'


# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index() 

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars='weekday', value_name='visitors')

# Print visitors
print(visitors)

users = pd.DataFrame({'weekday':['Sun','Sun','Mon','Mon'],
                      'city':['Austin','Dallas','Austin','Dallas'],
                      'visitors':[139,237,326,456],
                      'signups':[7,12,3,5]  })

# Melt users: skinny
skinny = pd.melt(users,id_vars=['city','weekday'])

# Print skinny
print(skinny)    


# Set the new index: users_idx
users_idx = users.set_index( ['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = users_idx.melt(col_level=0)

# Print the key-value pairs
print(kv_pairs)





                                         