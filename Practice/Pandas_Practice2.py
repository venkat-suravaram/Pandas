### Create a Series using various methods , Array, Dict, scalar
import pandas as pd
import numpy as np   ### Pass array values
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)


data = {'a' : 0., 'b' : 1., 'c' : 2.}   ## pass dictionary values
s = pd.Series(data)
print(s)

import numpy as np   # Create series using scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
"""OP:
100    a
101    b
102    c
103    d
dtype: object
a    0.0
b    1.0
c    2.0
dtype: float64
0    5
1    5
2    5
3    5
dtype: int64
"""
#############################################################  Accessing Data from Series
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e']) # scalar passing

#retrieve the first element
print (s[0])#  """OP:  1   """
#Retrieve the first three elements in the Series
print(s[:3])
"""OP: 
a    1
b    2
c    3
dtype: int64"""
print(s[-2:]) # Retrive last 2 values
"""OP:
d    4
e    5
dtype: int64 """

#####################################################   Retrieve Data Using Label (Index)
import pandas as pd
s=pd.Series([1,2,3,4], index=['a','g','r','p'])
print(s['a'])# """ OP: 1 """
#retrieve multiple elements
print (s[['a','r','p']])
#print(s['f'])  # """ KeyError: 'f' """

#####################################################  DataFrame
####
###
#
##
import pandas as pd
df = pd.DataFrame()
print(df)
"""OP:
Empty DataFrame
Columns: []
Index: []"""

data=[1,2,3,4,5] # from list
df=pd.DataFrame(data)
print(df)
"""OP:
   0
0  1
1  2
2  3
3  4
4  5"""

data=[['venkat',30],['Bob',45]]
df=pd.DataFrame(data,columns=['Name', 'Age'], dtype=float)
print(df)
"""OP:
     Name  Age
0  venkat   30
1     Bob   45"""

import pandas as pd
data={'name':['ven','ben','rem'], 'age':[34,45,32]}
df=pd.DataFrame(data)
print(df)
"""OP:
  name  age
0  ven   34
1  ben   45
2  rem   32"""

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])  ## Indexed dataframe
print (df)
"""OP:
        Name  Age
rank1    Tom   28
rank2   Jack   34
rank3  Steve   29
rank4  Ricky   42
"""
###   Create a DataFrame from Dict of Series
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)
print(df['one'])
print("adding new column called three")
df['three']=pd.Series([10,20,30],index=['a','b','d'])
print (df)
"""op:
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4"""

"""OP:
a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64"""

"""OP:
   one  two  three
a  1.0    1   10.0
b  2.0    2   20.0
c  3.0    3    NaN
d  NaN    4   30.0"""


