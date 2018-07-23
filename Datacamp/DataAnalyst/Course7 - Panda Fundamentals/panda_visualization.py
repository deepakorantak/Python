import pandas as pd
import matplotlib.pyplot as plt

# Create a plot with color='red'
df.plot(color = 'red')
# Add a title
plt.title('Temperature in Austin')
# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')
# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')
# Display the plot
plt.show()

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots = True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()

df= pd.DataFrame({Month:[Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec],
AAPL:[117.160004,128.460007,124.430000,125.150002,130.279999,125.430000,121.300003,112.760002,110.300003,119.500000,118.300003,105.260002],
GOOG:[534.522445,558.402511,548.002468,537.340027,532.109985,520.510010,625.609985,618.250000,608.419983,710.809998,742.599976,758.880005],
IBM:[153.309998,161.940002,160.500000,171.289993,169.649994,162.660004,161.990005,147.889999,144.970001,140.080002,139.419998,137.619995],
})

# Create a list of y-axis column names: y_columns
y_columns = ['AAPL','IBM']
# Generate a line plot
df.plot(x='Month', y=y_columns)
# Add the title
plt.title('Monthly stock prices')
# Add the y-axis label
plt.ylabel('Price ($US)')
# Display the plot
plt.show()


# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)
# Add the title
plt.title('Fuel efficiency vs Horse-power')
# Add the x-axis label
plt.xlabel('Horse-power')
# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')
# Display the plot
plt.show()

# Make a list of the column names to be plotted: cols
cols = ['weight' , 'mpg']
# Generate the box plots
df[cols].plot(kind='box',subplots = True)
# Display the plot
plt.show()

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)
# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))
plt.show()
# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, normed=True, cumulative=True, range=(0,.3))
plt.show()

# Print the minimum value of the Engineering column
print(df['Engineering'].min())
# Print the maximum value of the Engineering column
print(df['Engineering'].max())
# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')
# Plot the average percentage per year
mean.plot()
# Display the plot
plt.show()


# Print summary statistics of the fare column with .describe()
print(df.fare.describe())
# Generate a box plot of the fare column
df.fare.plot(kind = 'box')
# Show the plot
plt.show()

# Print the number of countries reported in 2015
print(df['2015'].count())
# Print the 5th and 95th percentiles
print(df['2015'].quantile([0.05,0.95]))
# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()


# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')
# Display the plot
plt.show()

#plotting Panda date time series

# Plot the raw data before setting the datetime index
df.plot()
plt.show()

# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column
df.set_index('Date',inplace = True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()

# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()


