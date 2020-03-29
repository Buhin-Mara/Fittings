#電子相関によるフェルミ液体の電気抵抗のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#温度の配列
list_linear_x = range(1,50,2)

array_x = np.array(list_linear_x)

#電気抵抗の配列
list_y=[]
for num in array_x:
    list_y.append( 1.0 + 0.1*num*num + np.random.rand()/10)

array_y=np.array(list_y)

#フェルミ液体的電気抵抗のフィッティング
def Fermiliquid_fit(x,a,b):
    return a + b * x * x  

param, cov=curve_fit(Fermiliquid_fit,array_x,array_y)

list_y_fit=[]
for num in array_x:
    list_y_fit.append(param[0] + param[1] * num * num)

array_y_fit=np.array(list_y_fit)

#フィッティング結果のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="Fitting")
plt.title("Fermi-liquid")
plt.xlabel('temperature (K)')
plt.ylabel('resistivity(mohm cm)')
plt.legend()
plt.savefig('Fermi-liquid')
plt.show()
