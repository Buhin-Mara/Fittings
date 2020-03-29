##比熱の温度依存性の計算

##フィッティングに使うもの
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import integrate
import numpy as np

## 図示のために使うもの
import matplotlib.pyplot as plt

#Temperature
list_linear_T = range(1,100,1)
array_T = np.array(list_linear_T)

#gap^2の温度依存性の数値計算
list_gap=[]
for num in array_T:
    def f(d):
        def gap(x):
           return np.tanh(1/num*np.sqrt(x**2+d**2))/np.sqrt(x**2+d**2)

            
        fxs=integrate.quad(gap,0,500)
        residual=3-fxs[0]  
        return residual
    
    p=optimize.fsolve(f,0)
    list_gap.append(p[0]**2)

gap2=np.array(list_gap)

dg2=np.gradient(gap2)

#比熱の温度依存性の計算
list_C=[]
for num in array_T:
    def h(E):
        return (np.exp(np.sqrt(E**2+gap2[num-1])/num))/(np.exp(np.sqrt(E**2+gap2[num-1])/num)+1)**2\
        *(E**2+gap2[num-1]-num/2*dg2[num-1])
    
    p=integrate.quad(h,0,1000)
    list_C.append(2/num/num/num*p[0])

C_gap=np.array(list_C)

#比熱の温度依存性のプロット        
plt.plot(array_T, C_gap, marker="", label="Numerical calculation")
plt.title("Electronic specific heat")
plt.xlabel('Temperature(K)')
plt.ylabel('C_el(J/K)')
plt.legend()
plt.savefig('C_el(T)')
plt.show()

