import numpy as np
import pandas as pd

url = "nhanes_2015_2016.csv"
da = pd.read_csv(url)

print(da.shape, end='\n\n')  # the shape (number of rows and columns) of the data frame

print(da.columns, end='\n\n')  # columns names

print(da.dtypes, end='\n\n')

print(da.loc[1:4, 'RIAGENDR'], end='\n\n')

print(da.iloc[1:4, 22])

print(
    """
Slicing a data set:
"""
)

w = da['DMDEDUC2']
x = da.loc[:, 'DMDEDUC2']
y = da.DMDEDUC2
z = da.iloc[:, 9]  # DMDEDUC2 is in column 9

for i in (w, x, y, z):
    print(i.max())  # печать максимального значения в колонне DMDEDUC2 - разные способы её вырезки
    print(type(i))  # дномерный массив - класс Series
                    # - Pandas data structure for holding a single column (or row) of data
print(type(da))     # - DataFrame

"""extracts row 3 from the data set (which is the fourth row, counting from zero:"""
print(da.iloc[7, :])  # 7th row is extracted

print(da.iloc[3:5, :])  # taking row positions 3 and 4 (counting from 0, which are rows 4 and 5 counting from 1)

print(da.iloc[:, 2:5])  # aking columns 2, 3, and 4 (columns 3, 4, 5 if counting from 1)

"""Missing values"""

print(pd.isnull(da.DMDEDUC2).sum())  # these functions to count the number of missing  DMDEDUC2 values
print(pd.notnull(da.DMDEDUC2).sum())  # ... and non-missing ...

