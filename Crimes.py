import pandas as pd

df = pd.read_csv('Crimes.csv')
print(df.head())
print(df.columns)
print(df.loc[:, ["Date", "Primary Type"]])
print(df.groupby(["Date", "Primary Type"]).size())

a = 'asdasdsd'