#Fermi-Dirac関数のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#エネルギーの配列
list_linear_x = range(1,100,1)

array_x = np.array(list_linear_x)

#FD関数の配列
list_y=[]
for num in array_x:
    list_y.append( 1/(np.exp(2*(num-50))+1) + np.random.rand()/60)

array_y=np.array(list_y)

#FD関数のフィッティング
def Fermi_Dirac_fit(x,a,b):
    return  1/(np.exp(a*(x-b))+1)  

param, cov=curve_fit(Fermi_Dirac_fit,array_x,array_y)

list_y_fit=[]
for num in array_x:
    list_y_fit.append( 1/(np.exp(param[0]*(num-param[1]))+1))

array_y_fit=np.array(list_y_fit)

#フィッティング結果のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="Fitting")
plt.title("Fermi-Dirac")
plt.xlabel('Energy (meV)')
plt.ylabel('f(E)(a. u. )')
plt.legend()
plt.savefig('Fermi-Dirac')
plt.show()
