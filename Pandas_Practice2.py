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
print(s['f'])  # """ KeyError: 'f' """