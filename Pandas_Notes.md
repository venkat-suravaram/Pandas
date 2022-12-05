Pandas is built on top of the NumPy package. alot of structure replicated to Pandas.

Data in pandas is often used to feed statistical analysis in SciPy, plotting functions from Matplotlib, and machine learning algorithms in Scikit-learn.

Install Pandas package:

    !pip install pandas // ! runs cells as if they were in a terminal
Import Pandas

    import pandas as pd

Core components of pandas:

    Series
    DataFrames
Series + Series = DataFrame

Series = column / 1-dimentional 

Data frame = multi-dimentional table made upof collection if Series

There are many ways to create a DataFrame from scratch, but a great option is to just use a simple dict.

    import pandas as pd
    
    data = {
        'apples': [3, 2, 0, 1],  # Series 1
        'oranges': [0, 3, 7, 2] #Series 2
        }
    purchases = pd.DataFrame(data)
    print(purchases)
   
    purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
    print(purchases)
    """   apples  oranges
    0       3        0
    1       2        3
    2       0        7
    3       1        2
            apples  oranges
    June         3        0
    Robert       2        3
    Lily         0        7
    David        1        2  """

you can create your own indexes instead of 0,1,2,3

Each (key, value) item in data corresponds to a column in the resulting DataFrame.

The advantage is you could locate customer data using name instead index id.

    print(purchases.loc['Lily'])
    """apples     0
    oranges    7
    Name: Lily, dtype: int64"""

Read data from source:

    df = pd.read_csv('purchases.csv')
    df = pd.read_csv('purchases.csv', index_col=0) # Define first column has index names
    df = pd.read_json('purchases.json')

    import sqlite3
    con = sqlite3.connect("database.db")
    df = pd.read_sql_query("SELECT * FROM purchases", con)

Convert to files:

    df.to_csv('new_purchases.csv')
    df.to_json('new_purchases.json')
    df.to_sql('new_purchases', con)
