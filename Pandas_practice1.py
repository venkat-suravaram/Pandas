import pandas as pd

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