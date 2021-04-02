import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
# print(x)
# print(x_with_nan)

y = np.array(x)  # massive
y_with_nan = np.array(x_with_nan)  # massive
z = pd.Series(x)  # 1D object
z_with_nan = pd.Series(x_with_nan)  # 1D Object
# print(y)
# print(y_with_nan)
# print(z)
# print(z_with_nan)

mean_ = np.mean(y)
mean2_ = np.mean(y_with_nan)
print(mean_, mean2_, sep="; ")

mean_ignore_nan = np.nanmean(y_with_nan)  # ignores any NaN
print(mean2_, mean_ignore_nan, sep=' ---> ')

mean_ = z.mean()
print(mean_)

mean_ = z_with_nan.mean()  # ignores NaN defaultly, parameter 'skipna' is on
print(mean_)

# Средневзвешенное:
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
w_mean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(w_mean)
w_mean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print(w_mean)
