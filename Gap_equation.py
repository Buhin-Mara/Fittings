##超伝導ギャップの温度依存性の計算

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


#超伝導ギャップの温度依存性の計算
list_gap=[]
for num in array_T:
    def f(d):
        def gap(x):
           return np.tanh(1/num*np.sqrt(x**2+d**2))/np.sqrt(x**2+d**2)
            
        fxs=integrate.quad(gap,0,500)
        residual=3-fxs[0]  
        return residual
    
    p=optimize.fsolve(f,0)
    list_gap.append(p[0])

array_gap=np.array(list_gap)

#近似式の計算(T=Tc近傍のみ)
list_gap_fit=[]
for num in array_T:
    p=50*np.sqrt(1-num/56.9548)
    list_gap_fit.append(p)

array_gap_fit=np.array(list_gap_fit)

#超伝導ギャップの温度依存性のプロット
plt.plot(array_T, array_gap, marker="", label="Numerical calculation")
plt.plot(array_T, array_gap_fit, marker="o", label="(1-T/Tc)^(1/2)")
plt.title("Gap Equation")
plt.xlabel('Temperature(K)')
plt.ylabel('Gap(meV)')
plt.legend()
plt.savefig('Gap(T)')
plt.show()

