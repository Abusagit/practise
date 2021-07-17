import pandas as pd
df = pd.read_csv('Crimes.csv')
print(df.loc[df["Date"].str.contains('2015', regex=True)]["Primary Type"].value_counts())
