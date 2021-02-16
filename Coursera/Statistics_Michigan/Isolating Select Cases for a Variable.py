import pandas as pd

data = pd.read_csv('nhanes_2015_2016.csv').dropna()
pd.set_option('display.max_columns', 100)
print(data.columns)

data.rename(columns={'RIAGENDR': 'Gender', 'RIDAGEYR': 'age'}, inplace=True)
print(data.columns)
data['Gender'] = data.Gender.replace({1: 'Male', 2: 'Female'})

"""1        .loc"""
# subset the entire dataset by age and gender

# females younger than or equal to 40
selectf = data.loc[(data['age'] <= 40) & (data['Gender'] == 'Female'), ]

# males older than 50 and younger than 60

selectm = data.loc[(data['age'] > 50) & (data['age'] < 60) & (data['Gender'] == 'Male'), ]

print(selectf.head(), selectm.head(), sep='\n\n', end='\n\n\n')

# obtain descriptive statistics for weight
print(selectf.BMXWT.describe(), end='\n\n\n')

print(selectm.BMXWT.mean())


"""2         .where"""
# females younger than or equal to 40
selectf = ((data['age'] <= 40) & (data['Gender'] == 'Female'))
data_f = data.where(selectf)

# males older than 50 and younger than 60
selectm = ((data["age"] > 50) & (data["age"] < 60) & (data["Gender"] == "Male"))
data_m = data.where(selectm)

print(data_f.head())
print(data_m.head())

# TODO find out what is wrong (only NaN) and transport it to Jupyter!!!!!!!!!!!!!!!!!!

