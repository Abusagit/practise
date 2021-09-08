import numpy as np
import pandas as pd

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(a))

url = "Cartwheeldata.csv"
df = pd.read_csv(url)
print(type(df))

print(df.head())  # 5 rows

print(df)  # Total print

print(df.columns)  # Columns names

print("""
.loc()
""")
print(df.loc[:, "CWDistance"])  # Return all observations of CWDistance

print(df.loc[:, ["CWDistance", "Height", "Wingspan"]])  # Select all rows for multiple columns,
# ["CWDistance", "Height", "Wingspan"]

print(df.loc[:9, ["CWDistance", "Height", "Wingspan"]])  # Select few rows (up to 9) for multiple columns,
# ["CWDistance", "Height", "Wingspan"]

print(df.loc[10:15])  # Select range of rows for all columns

print("""
.iloc
""")
# .iloc() is integer based slicing, whereas .loc() used labels/column names

print(df.iloc[:4])

print(df.iloc[1:5, 2:4])

# print(df.iloc[1:5, ["Gender", "GenderGroup"]])  # Вылетает ошибка! не позволяет аргументам быть строками и прочими

print(df.iloc[1:5])

print(df.dtypes)  # тип данных каждой колонны

print(df.Gender.unique())  # List unique values in the df['Gender'] column

print(df.GenderGroup.unique())  # for GenderGroup

print(df.loc[:, ["Gender", "GenderGroup"]])  # Use .loc() to specify a list of mulitple column names

"""From eyeballing the output, 
it seems to check out. 
We can streamline this by utilizing the groupby() and size() functions.
"""
print(df.groupby(['Gender', 'GenderGroup']).size())

"""
This output indicates that we have two types of combinations.

Case 1: Gender = F & Gender Group = 1
Case 2: Gender = M & GenderGroup = 2.
This validates our initial assumption that these two fields essentially portray the same information.

import numpy as np
import pandas as pd

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(a))

url = "Cartwheeldata.csv"
df = pd.read_csv(url)
print(type(df))

print(df.head())  # 5 rows

print(df)  # Total print

print(df.columns)  # Columns names

print("""
.loc()
""")
print(df.loc[:, "CWDistance"])  # Return all observations of CWDistance

print(df.loc[:, ["CWDistance", "Height", "Wingspan"]])  # Select all rows for multiple columns,
# ["CWDistance", "Height", "Wingspan"]

print(df.loc[:9, ["CWDistance", "Height", "Wingspan"]])  # Select few rows (up to 9) for multiple columns,
# ["CWDistance", "Height", "Wingspan"]

print(df.loc[10:15])  # Select range of rows for all columns

print("""
.iloc
""")
# .iloc() is integer based slicing, whereas .loc() used labels/column names

print(df.iloc[:4])

print(df.iloc[1:5, 2:4])

# print(df.iloc[1:5, ["Gender", "GenderGroup"]])  # Вылетает ошибка! не позволяет аргументам быть строками и прочими

print(df.iloc[1:5])

print(df.dtypes)  # тип данных каждой колонны

print(df.Gender.unique())  # List unique values in the df['Gender'] column

print(df.GenderGroup.unique())  # for GenderGroup

print(df.loc[:, ["Gender", "GenderGroup"]])  # Use .loc() to specify a list of mulitple column names

"""From eyeballing the output, 
it seems to check out. 
We can streamline this by utilizing the groupby() and size() functions.
"""
print(df.groupby(['Gender', 'GenderGroup']).size())

"""
This output indicates that we have two types of combinations_.

Case 1: Gender = F & Gender Group = 1
Case 2: Gender = M & GenderGroup = 2.
This validates our initial assumption that these two fields essentially portray the same information.
"""
