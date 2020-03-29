##デバイ比熱の計算(積分)

##フィッティングに使うもの
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import integrate
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt


#温度の配列
list_linear_x = range(1,300,1)

array_x = np.array(list_linear_x)

#デバイ比熱の配列
def Debye(x):
    return (x**4)*np.exp(x)/((np.exp(x)-1)**2)

list_y=[]
for num in array_x:
    p=integrate.quad(Debye,0,300/num)
    list_y.append(((num/300)**3)*p[0] +np.random.rand()/100)

array_y=np.array(list_y)

#デバイ比熱のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
#plt.plot(array_x, array_y_fit, marker="")
plt.title("Debye")
plt.xlabel('Temperature(K)')
plt.ylabel('Specific heat(J/K)')
plt.legend()
plt.savefig('Debye')
plt.show()
