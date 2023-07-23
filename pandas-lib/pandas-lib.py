# Series is a one-dimensional array with labels. it can contain any data type including
# integers, floats,strings,Python objects and more

# DataFrame is a two-dimensional data structure with labels.
# We can use labels to locate data
import pandas as pd

print(pd.__version__)

# Series create , manipulate, querry, delete
# creating a series from a list
arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)
print(s1)

order = [1, 2, 3, 4, 5]
s2 = pd.Series(arr, index=order)
print(s2)

import numpy as np

n = np.random.randn(5)  # create a random ndarray
index = ['a', 'b', 'c', 'd', 'e']
s2 = pd.Series(n, index=index)
print(s2)

# create series from dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s3 = pd.Series(d)
print(s3)

# you can modify the index
print(s1)
s1.index = ['A', 'B', 'C', 'D', 'E']
print(s1)

# slicing

a = s1[:3]
print(a)

# s4 = s1.append(s3)
# print(s4)

# s4.drop('e')
# print(s4)

# series operations

arr1 = [0, 1, 2, 3, 4, 5, 6, 7]
arr2 = [6, 7, 8, 9, 5]

s5 = pd.Series(arr2)
print(s5)
s6 = pd.Series(arr1)
print(s6)
print(s5.add(s6))
print(s5.add(s6))
print(s5.mul(s6))
print(s5.div(s6))
print('median', s6.median())
print('max', s6.max())
print('min', s6.min())

# create a dataframe

dates = pd.date_range('today', periods=6)  # define time sequence as index
print(dates)

num_arr = np.random.randn(6, 4)  # import numpy random array
print(num_arr)

columns = ['A', 'B', 'C', 'D']  # use the table as the column names
df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
print(df1)

# create a dataframe with dictionary array

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'cat', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(data, index=labels)
print(df2)
print(df2.dtypes)
print(df2.head())
print(df2.head(2))
print(df2.tail(2))
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())  # see statitical data of dataframe
print(df2.T)  # Transpose
print(df2.sort_values(by='age'))

# slicing dataframe
print(df2[1:3])
print(df2.sort_values(by='age')[1:3])

# query dataframe by tag

print(df2[['age', 'visits']])
print(df2.iloc[1:3])  # query rows 2,3

df3 = df2.copy()
print(df3)
print(df3.isnull())

df3.loc['f', 'age'] = 1.5
print(df3)

# df3.mean()

print(df3['visits'].sum())
print(df3['visits'].min())
print(df3['visits'].max())

print(df3.sum())
string = pd.Series(['A', 'C', 'C', 'Aaa', 'BaCa', np.nan, 'CBA', 'cow', 'owl'])
print(string)
print(string.str.upper())

# Operations for DataFrame missing values

df4 = df3.copy()
print(df4)
print(df4.fillna(4))
meanAge = df4['age'].mean()
print(df4['age'].fillna(meanAge))

df5 = df3.copy()
print(df5.dropna(how='any'))

# Dataframe file operations
df3.to_csv('animal.csv')
df_animal = pd.read_csv('animal.csv')
print(df_animal)
print(df_animal.head(3))
df3.to_excel('animal.xlsx', sheet_name='Sheet1')
df_animal2 = pd.read_excel('animal.xlsx', sheet_name='Sheet1', index_col=None, na_values=['NA'])
print(df_animal2)
