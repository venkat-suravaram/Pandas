import os
print(os.getcwd())
import pandas as pd  # as here is an alias or short form
pd.DataFrame
"""
# in pandas we are dealing with 2 major data types
# 1. Series
        Series is a 1-dimentional data type
# 2. DataFrame
        # in DataFrame you get result in Horizanl manner
        # DataFrame Datatype having more than 2-dimentions
    Dimentions nothing but number of columns
    
"""
l=[1,2,3,4]
print(type(l))
Newvariable_series = pd.Series(l)
print(type(Newvariable_series))
"""  OP:
<class 'list'>
<class 'pandas.core.series.Series'>
"""
ser1 = pd.Series([1,2,3,4,5,6,7])
print(ser1)
"""
0    1
1    2
2    3
3    4
4    5
5    6
6    7
dtype: int64
"""
## Series is 1-dimentional datatype
l=[[1,2,3,4,5],[5,6,7,8]]
ser2 = pd.Series(l)
print(ser2)
""" OP 
0 index , 1st index results , result in vertical manner
0    [1, 2, 3, 4, 5]
1       [5, 6, 7, 8]
dtype: object
"""

# in DataFrame you get result in Horizanl manner
# DataFrame Datatype having more than 2-dimentions
df1 = pd.DataFrame(l)
print(df1)
"""OP
   0  1  2  3    4
0  1  2  3  4  5.0
1  5  6  7  8  NaN
"""

# example of readability of a source data using pandas - Read CSV data
# Read Dataset
df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df)
''' op:
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
'''

print(df.head())  # display top 5 rows
print(df.head(10)) # display top 10 rows
print(df.tail()) # display bottom 5 rows
print(df.tail(2)) #Display botton 2 rows

print(df.dtypes) ## Data types of each column
"""OP:
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
"""
print(df.describe()) # More details about the column

