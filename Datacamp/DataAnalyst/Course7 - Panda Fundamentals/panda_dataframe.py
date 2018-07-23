# Import numpy
import numpy as np

# Create array of DataFrame values: np_vals
np_vals = df.values
# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)
# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)
# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]

import pandas as pd

list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys,list_values))
# Inspect the list using print()
print(zipped)
# Build a dictionary with the zipped list: data
data = dict(zipped)
# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame({a:[1980,1981,1982],
                   b:['Blondie','Chistorpher Cross','Joan Jett'],
                   c:['Call Me','Arthurs Theme','I Love Rock and Roll'],
                   d:[6,3,9]})

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels      

cities = ['Manheim',
 'Preston park',
 'Biglerville',
 'Indiana',
 'Curwensville',
 'Crown',
 'Harveys lake',
 'Mineral springs',
 'Cassville',
 'Hannastown',
 'Saltsburg',
 'Tunkhannock',
 'Pittsburgh',
 'Lemasters',
 'Great bend']

 # Make a string with the value 'PA': state
state = 'PA'
# Construct a dictionary: data
data = {'state':state, 'city':cities}
# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)
# Print the DataFrame
print(df)







