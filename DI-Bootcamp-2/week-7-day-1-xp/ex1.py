# 1.
# Write a function to create a numpy array using only the input: start, length, and stop.
# Use the function to create an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def create_array(start, length, stop):
    return np.linspace(start, length, stop)

arr = create_array(6, 100, 6 + 4 * 99)
print(arr)

# 2.
# Drop all nan values from the following numpy array.

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
a = a[~np.isnan(a)]

print(a)

# 3.
# create a random numpy array that has a shape of (5, 6) filled with integers between 1 and 100.
# Then compute the maximum int for each row in the array
arr2 = np.random.randint(1, 101, size=(5,6)) 
# generate a random number between 1 and 101 within 5 rows and 6 columns
max_int = np.max(arr2, axis=1)
# finding the maximum number from each row

print(arr2)
print(max_int)

# 4.
# use a pandas Series function to find the unique values and their frequencies of the following Series:

series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
unique_values = series.value_counts()
print(unique_values)

# 5.
# Get the day of month, week number, day of year and day of week from this pandas series

series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

date_series = pd.to_datetime(series, errors='coerce')

day_of_month = date_series.dt.day
week_number = date_series.dt.isocalendar().week
day_of_year = date_series.dt.dayofyear
day_of_week = date_series.dt.day_name()

df = ({'Dates': series, 'DayofMonth': day_of_month, 'WeekNumber': week_number, 'DayOfYear': day_of_year, 'DayOfWeek': day_of_week})

print(df)

# 6.
# Read the data from https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv into a pandas dataframe.
# Do not download the file.

# Then
# - print how many columns are of each datatype.
# - Change the column name “Type” to “TypeOfCar” and print the head of the dataframe

# How many values are missing from each of the columns?
# Which columns has the most missing values? (answer with code, without sorting)

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

df = pd.read_csv(url)

print(df.dtypes.value_counts())

df = df.rename(columns={'Type':'TypeOfCar'})

print(df.head())

# 7.
# Delete the columns: “EngineSize” and “Length” in 2 different ways. Check (with code) that these columns are indeed gone.
# ----------first way--------------
# del df['EngineSize'], df['Length']
# ----------second way-------------
# df = df.drop(df.columns[[0, 1, 3]], axis=1)

# 8.
# Join the following two dataframes by two columns, so they have only the common rows. Remove duplicate
# columns (meaning that all values are the same) to keep only one.

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

merged_df = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'])

merged_df = merged_df.drop('price_y', axis=1)


print(merged_df)



# 9.
# Split this dataframe with a string column to form a dataframe with 3 columns named “STD”, “City”, and “State.”

# Desired Output:
# 0 STD        City        State
# 1  33     Kolkata  West Bengal
# 2  44     Chennai   Tamil Nadu
# 3  40   Hyderabad    Telengana
# 4  80   Bangalore    Karnataka

df4 = pd.DataFrame(["STD,City\tState",
                    "33,Kolkata\tWest Bengal",
                    "44,Chennai\tTamil Nadu",
                    "40,Hyderabad\tTelengana",
                    "80,Bangalore\tKarnataka"], columns=['row'])

df4 = df4['row'].str.split('[,\t]', expand=True)
df4.columns = ['STD', 'City', 'State']

print(df4)


# 10.
# Create a function called scatter_plot that takes the dataframe df and plots the relationship between the following two
# features:
# - displacement over x-axis
# - acceleration over y-axis

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

def scatter_plot(df):
    plt.scatter(df['displacement'], df['acceleration'])
    plt.xlabel('displacement')
    plt.ylabel('acceleration')
    plt.title('Displacement v/s Acceleration Scatter Plot')
    plt.show()
scatter_plot(df_mpg)  

# 11.
# Create a function bar_plot that takes the dataframe df 
# and compares the cylinders of all the cars from 1978 model_year and toyota company



def bar_plot(df):
    
    df_filtered = df[(df['model_year'] == 78) & (df['car_name'].str.startswith('toyota'))]
    
    counts = df_filtered.groupby('cylinders').size().reset_index(name='count')
    
    plt.bar(counts['cylinders'], counts['count'])
    plt.xlabel('Cylinders')
    plt.ylabel('Count')
    plt.title('Cylinder Counts for 1978 Toyota Cars')
    plt.show()

bar_plot(df_mpg)



# 12.
# Create a function line_plot that takes the dataframe df 
# and plots the change in weight throughout the years for the cars of toyota company.

def line_plot(df):
    
    df_filtered = df[df['car_name'].str.startswith('toyota')]
    
    weights = df_filtered.groupby('model_year')['weight'].mean().reset_index(name='mean_weight')
    
    plt.plot(weights['model_year'], weights['mean_weight'])
    plt.xlabel('Model Year')
    plt.ylabel('Mean Weight')
    plt.title('Change in Weight for Toyota Cars')
    plt.show()
line_plot(df_mpg)


# 13.
# Come up with your own plot that shows an interesting relationship in the auto-mpg data.
# Remember, that finding relationships between features and the target feature is valuable.
# Pick a feature here that would be a good target value and make in interesting plot.
# Don’t forget to label your axis and legends to make sure the plot is understood!

def mpg_vs_horsepower(df):
    x = df['horsepower']
    y = df['mpg']
    plt.scatter(x, y)
    plt.xlabel('Horsepower')
    plt.ylabel('Miles per Gallon')
    plt.title('Miles per Gallon vs. Horsepower')
    plt.show()
mpg_vs_horsepower(df_mpg)
