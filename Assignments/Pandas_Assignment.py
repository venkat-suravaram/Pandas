import os
print(os.getcwd())
#Q1. How do you load a CSV file into a Pandas DataFrame?
import pandas as pd
df=pd.read_csv('C:\DE\Python_WorkSpace\Pandas\Assignments\student.csv')
print(df)

# Q2. How do you check the data type of a column in a Pandas DataFrame?
print(df.dtypes)
"""OP:
id         int64
name      object
class     object
mark       int64
gender    object
dtype: object"""

## Q3. How do you select rows from a Pandas DataFrame based on a condition?
print(df.loc[6]) # Display specific row using index
print(df.loc[df['class'] == 'Six'])
"""OP:
    id        name class  mark  gender
8    9     Tes Qry   Six    78    male
10  11      Ronald   Six    89  female
11  12       Recky   Six    94  female
16  17       Tumyu   Six    54    male
29  30   Reppy Red   Six    79  female
32  33   Kenn Rein   Six    96  female
34  35  Rows Noump   Six    88  female
"""

## Q4. How do you rename columns in a Pandas DataFrame?
print("\n Before Modifying cloumns: \n",df.columns)
df.rename(columns = {'class':'grade'}, inplace = True)
print("\n After Modifying cloumns: \n",df.columns)

"""OP:
 Before Modifying cloumns: 
 Index(['id', 'name', 'class', 'mark', 'gender'], dtype='object')

 After Modifying cloumns: 
 Index(['id', 'name', 'grade', 'mark', 'gender'], dtype='object')"""

## Q5. How do you drop columns in a Pandas DataFrame?
print("\n Before deletion cloumns: \n",df.columns)
df.drop(['gender'], axis=1, inplace=True) # What is axis=1 ?  bydefault axis=0 row , axis=1 -> column
print("\n After deletion cloumns: \n",df.columns)

"""OP:
 Before deletion cloumns: 
 Index(['id', 'name', 'grade', 'mark', 'gender'], dtype='object')

 After deletion cloumns: 
 Index(['id', 'name', 'grade', 'mark'], dtype='object') """

## Q6. How do you find the unique values in a column of a Pandas DataFrame?

print(df.grade.unique()) # for 1 column
"""OP: ['Four' 'Three' 'Fifth' 'Five' 'Six' 'Seven' 'Nine' 'Eight']  """
for i in df:
    print(df[i].unique()) # for all columns

## Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
print("\n find missng values:\n")
print(df.isna())
print("\n find missing values count:\n")
print(df.isna().sum())

"""OP:
       id   name  grade   mark
9   False  False  False  False
10  False  False   True  False
11  False  False  False  False
12  False  False  False   True
13  False  False  False  False

 find missing values count:

id       0
name     0
grade    1
mark     1
dtype: int64
"""

##  Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
print("\n fill missng values:\n")
print(df.fillna(0.0))
print("\n find missing values count:\n")
print(df.isna().sum())
print(df)

## Q9. How do you concatenate two Pandas DataFrames?
d1 = {
    'apples': [3, 2, 0, 1],  # Series 1
    'oranges': [0, 3, 7, 2] #Series 2
    }
d2 = {
    'Banana': [3, 2, 0, 1],  # Series 1
    'GraPE': [0, 3, 7, 2] #Series 2
    }
d3 = {
    'tomato': [3, 2, 0, 1],  # Series 1
    'permisen': [0, 3, 7, 2] #Series 2
    }
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)
print(df1,"\n",df2,"\n",df3)
df_row_concat=pd.concat([df1,df2], axis=0)
df_col_concat=pd.concat([df1,df2],axis=1)
print("\n Row concat display: \n", df_row_concat)
print("\n col concat display: \n", df_col_concat)

"""OP:
Row concat display: 
    apples  oranges  Banana  GraPE
0     3.0      0.0     NaN    NaN
1     2.0      3.0     NaN    NaN
2     0.0      7.0     NaN    NaN
3     1.0      2.0     NaN    NaN
0     NaN      NaN     3.0    0.0
1     NaN      NaN     2.0    3.0
2     NaN      NaN     0.0    7.0
3     NaN      NaN     1.0    2.0

 col concat display: 
    apples  oranges  Banana  GraPE
0       3        0       3      0
1       2        3       2      3
2       0        7       0      7
3       1        2       1      2
"""

## Q10. How do you merge two Pandas DataFrames on a specific column?
# creating a dataframe
df1 = pd.DataFrame({'Name': ['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit'],
                    'Marks': [80, 90, 75, 88, 59]})

# creating another dataframe with different data
df2 = pd.DataFrame({'Name': ['Raju', 'Divya', 'Geeta', 'Sita'],
                    'Grade': ['A', 'A', 'B', 'A'],
                    'Rank': [3, 1, 4, 2],
                    'Gender': ['Male', 'Female', 'Female', 'Female']})

print("\n",df1,"\n",df2)
print("\n",df1.merge(df2[['Name','Grade','Gender']]))
print("\n",df1.merge(df2[['Name','Grade','Gender']], on='Name', how='left'))
"""OP:
     Name  Marks Grade  Gender
0   Raju     80     A    Male
1  Geeta     75     B  Female
2   Sita     88     A  Female

     Name  Marks Grade  Gender
0   Raju     80     A    Male
1   Rani     90   NaN     NaN
2  Geeta     75     B  Female
3   Sita     88     A  Female
4  Sohit     59   NaN     NaN
"""

## Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?

## Q12. How do you pivot a Pandas DataFrame?
print(df.pivot('name','id','mark'))
"""OP:
id             1     2     3     4     5   ...    10    11    12  13    14
name                                       ...                            
Alex John     NaN   NaN   NaN   NaN   NaN  ...   NaN   NaN   NaN NaN   NaN
Arnold        NaN   NaN  55.0   NaN   NaN  ...   NaN   NaN   NaN NaN   NaN
Asruid        NaN   NaN   NaN   NaN   NaN  ...   NaN   NaN   NaN NaN   NaN
Big John      NaN   NaN   NaN   NaN   NaN  ...  55.0   NaN   NaN NaN   NaN
"""

## Q13. How do you change the data type of a column in a Pandas DataFrame?
print("\n Data types before change: \n",df.dtypes)
df=df.astype(str)
print("\n Data types after change: \n",df.dtypes)
"""OP:
 Data types before change: 
 id         int64
name      object
grade     object
mark     float64
dtype: object

 Data types after change: 
 id       object
name     object
grade    object
mark     object
dtype: object
"""

## Q14. How do you sort a Pandas DataFrame by a specific column?
df_sort=df.sort_values(by='name')
print("\n Sorting order: ",df_sort)
"""OP:
Sorting order:      id         name  grade  mark
5    6    Alex John   Four  55.0
2    3       Arnold  Three  55.0
7    8       Asruid   Five  85.0
9   10     Big John   Four  55.0
"""

## Q15. How do you create a copy of a Pandas DataFrame?
df_copy=df.copy(deep=False)
print("\n copy only structure: \n", df_copy)
df_copy_data=df.copy(deep=True)
print("\n copy only structure & Data: \n", df_copy_data)