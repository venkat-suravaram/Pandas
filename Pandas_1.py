import os
print(os.getcwd())
import pandas as pd  # as here is an alias or short form
pd.DataFrame
"""
# in pandas we are dealing with 2 major data types
# 1. Series
        Series is a 1-dimentional data type
# 2. DataFrame
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