#線形関数のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#x軸の配列
list_linear_x = range(0,20,2)

array_error = np.random.normal(size=len(list_linear_x))

array_x = np.array(list_linear_x)

#y軸の配列
array_y = array_x + array_error 

#フィッティング
def linear_fit(x,a,b):
    return a*x+b

param, cov=curve_fit(linear_fit,array_x,array_y)

array_y_fit=param[0]*array_x + param[1]

#フィッティング結果のプロット
plt.plot(array_x, array_y,marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="Fitting")
plt.savefig('linear')
plt.legend()
plt.show()
