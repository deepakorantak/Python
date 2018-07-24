import matplotlib.pyplot as plt

# populate year and population
year = [1950,1970,1990,2010]
pop = [2.519,3.692,5.263,6.972]
col = ['red','green','blue','yellow']
s_pop = [i*6 for i in pop]

# Change the line plot below to a scatter plot

plt.scatter(pop,year,s=s_pop,c=col)

# Put the x-axis on a logarithmic scale
#plt.xscale('log')
plt.xlabel('population')
plt.ylabel('year')
plt.title('World population')
plt.xticks([0,1,2,3,4,5,6,7],
           ['0B','1B','2B','3B','4B','5B','6B','7B'] )

# Show plot
plt.show()
