#熱伝導、下記URL参考
#http://www.thermoelectrics.jp/zata/journal/Download/08-3kouza_takeuchi-3.pdf

##フィッティングに使うもの
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import integrate
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#Bloch-Gruneisen関数のプロット
list_linear_x = range(1,300,1)

array_x = np.array(list_linear_x)

def Kochel(x):
    return (x**3)*np.exp(x)/((np.exp(x)-1)**2)

list_y=[]
for num in array_x:
    p=integrate.quad(Kochel,0,300/num)
    list_y.append(((num/300)**2)*p[0] +np.random.rand()/100)

array_y=np.array(list_y)

plt.plot(array_x, array_y, marker="o")
#plt.plot(array_x, array_y_fit, marker="")
plt.title("minimum thermal conductivity")
plt.xlabel('Temperature(K)')
plt.ylabel('Thermal conductivity(W/m K)')
plt.show()
