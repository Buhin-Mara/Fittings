#光学伝導のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#周波数の配列
list_linear_x = np.arange(1,200,0.2)

array_x = np.array(list_linear_x)

#Drude-Lorentz関数の配列
list_y=[]
for num in array_x:
    list_y.append( 1.0 + 1/(1+num**2) \
    + num**2/(5*num**2+((100*100-num**2)**2))\
    + np.random.rand()/60)

array_y=np.array(list_y)


#Drude-Lorentz関数のフィッティング
def Drude_Lorentz_fit(x,a,b):
    return a + 1/(1+x**2) + x**2/(5*x**2+(b**2-x**2)**2)  

#初期値の設定,ローレンツピークの位置を指定しないと上手くいかない
a_initial=1
b_initial=100
param, cov=curve_fit(Drude_Lorentz_fit,array_x,array_y,[a_initial,b_initial])

list_y_fit=[]
for num in array_x:
    list_y_fit.append( param[0] + 1/(1.0+num**2) \
    + num**2/(5*num**2+(param[1]**2-num**2)**2))

array_y_fit=np.array(list_y_fit)

#光学伝導度のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="", label="Fitting")
plt.title("Drude-Lorentz")
plt.xlabel('frequency (cm^-1)')
plt.ylabel('conductivity(Ohm^-1 cm^-1)')
plt.legend()
plt.savefig('Drude')
plt.show()
