import pandas as pd
import matplotlib.pyplot as plt
data = {
    'apples': [3, 2, 0, 1],  # Series 1
    'oranges': [0, 3, 7, 2] #Series 2
    }
purchases = pd.DataFrame(data)
print(purchases)
"""OP:
   apples  oranges
0       3        0
1       2        3
2       0        7
3       1        2
"""
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)
"""        apples  oranges
June         3        0
Robert       2        3
Lily         0        7
David        1        2"""
print(purchases.loc['Lily'])
"""apples     0
oranges    7
Name: Lily, dtype: int64"""
print(purchases.head())
print(purchases.columns)
"""Index(['apples', 'oranges'], dtype='object')"""

import pandas as pd
info = {'ID' :[101, 102, 103],
        'Department' :['B.Sc','B.Tech','M.Tech',]}
info = pd.DataFrame(info)
print (info)
"""    ID Department
0  101       B.Sc
1  102     B.Tech
2  103     M.Tech       """

################ Create a Empty DataFrame
# importing the pandas library
import pandas as pd
info = pd.DataFrame()
print (info)
"""Empty DataFrame
Columns: []
Index: []
"""

##################  Add column
# importing the pandas library
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

info = pd.DataFrame(info)

# Add a new column to an existing DataFrame object

print("Add new column by passing series")
info['three'] = pd.Series([20, 40, 60], index=['a', 'b', 'c'])
print(info)
print("Add new column using existing DataFrame columns")
info['four'] = info['one'] + info['three']
print(info)
"""
Add new column by passing series
   one  two  three
a  1.0    1   20.0
b  2.0    2   40.0
c  3.0    3   60.0
d  4.0    4    NaN
e  5.0    5    NaN
f  NaN    6    NaN
Add new column using existing DataFrame columns
   one  two  three  four
a  1.0    1   20.0  21.0
b  2.0    2   40.0  42.0
c  3.0    3   60.0  63.0
d  4.0    4    NaN   NaN
e  5.0    5    NaN   NaN
f  NaN    6    NaN   NaN
"""

import pandas as pd
import matplotlib.pyplot as plt
data = {
    'apples': [3, 2, 0, 1],  # Series 1
    'oranges': [0, 3, 7, 2] #Series 2
    }
purchases = pd.DataFrame(data)
print(purchases)
print(" adding new column called banana")
data['banana']=pd.Series([1,2,3,4])
purchases = pd.DataFrame(data)
print(purchases)



 
