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
"""OP:
PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
"""
print(df.shape) # shape of data frame
"""OP: (891, 12)"""
print(df[15:17])
"""OP:
    PassengerId  Survived  Pclass  ...    Fare Cabin  Embarked
15           16         1       2  ...  16.000   NaN         S
16           17         0       3  ...  29.125   NaN         Q
[2 rows x 12 columns]

"""
print(df.Fare) # Accessing column
print(df[['Fare','Age']]) # Accessing multiple columns

