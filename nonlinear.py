#非線形関数のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#x軸の配列
list_linear_x = range(0,20,2)

array_x = np.array(list_linear_x)

#y軸の配列
list_y=[]
for num in array_x:
    list_y.append( 1.0*np.exp(num/(1.0+num))+np.random.rand()/10)

array_y=np.array(list_y)

#非線形関数のフィッティング
def nonlinear_fit(x,a,b):
    return b * np.exp(x / (a+x)  )

param, cov=curve_fit(nonlinear_fit,array_x,array_y)

list_y_fit=[]
for num in array_x:
    list_y_fit.append(param[1]*np.exp(num/(param[0]+num)))

array_y_fit=np.array(list_y_fit)

#フィッティング結果のプロット
plt.plot(array_x, array_y,marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="Fitting")
plt.legend()
plt.savefig('nonlinear')
plt.show()