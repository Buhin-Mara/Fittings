##磁化率のキュリー則のフィッティング

##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#温度Tの配列
list_linear_x = range(1,100,1)

array_x = np.array(list_linear_x)

#磁化率キュリー則の温度依存性
list_y=[]
for num in array_x:
    list_y.append( 1.0 + 1/num + np.random.rand()/10)

array_y=np.array(list_y)

#キュリー則のフィッティング
def Curie_fit(x,a,b):
    return a + b/x  

param, cov=curve_fit(Curie_fit,array_x,array_y)

list_y_fit=[]
for num in array_x:
    list_y_fit.append(param[0] + param[1] /num)

array_y_fit=np.array(list_y_fit)

#キュリー則のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="fitting")
plt.title("Curie law")
plt.xlabel('temperature (K)')
plt.ylabel('magnetization(emu)')
plt.legend()
plt.savefig('Curie')
plt.show()
