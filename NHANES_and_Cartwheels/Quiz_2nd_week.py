import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_columns', 100)

os.chdir(r"C:\Users\Fyodor\PycharmProjects\untitled\Coursera")
path = "nhanes_2015_2016.csv"
data = pd.read_csv(path)

print(data.head(), end='\n---------------\n')


var = data['BPXSY2']
var = var.dropna()

print(var.describe())
print(var.describe().to_string(float_format='%.3f'))

# IQR
print(var.quantile(0.75) - var.quantile(0.25))
iqr = stats.iqr(var)
print(iqr)


diff_by_series_method = var.diff()  # calculates the difference
print(diff_by_series_method.values)

# NumPy library instead to find thw same values
diff_by_np_method = np.diff(var)
print(diff_by_np_method)  # ignores the NaN

sns.distplot(var, bins=30).set(title='My title', xlabel='BP', ylabel='Frequency')
plt.show()

sns.boxplot(var).set(title='Boxplot', xlabel='BP')
plt.show()

sns.distplot(a=var)
plt.show()
