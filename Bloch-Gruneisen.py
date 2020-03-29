#フォノンによる電気抵抗の計算

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

def Bloch(x):
    return (x**5)/((np.exp(x)-1)*(1-np.exp(-1*x)))

#Bloch-Gruneisen関数の配列
list_y=[]
for num in array_x:
    p=integrate.quad(Bloch,0,300/num)
    list_y.append(((num/300)**5)*p[0] +np.random.rand()/100)

array_y=np.array(list_y)

#ここから最小自乗によるフィッティング
def Bloch_fit(parameter,xs,ys):
    a=parameter[0]
    b=parameter[1]
    
    fxs=[(b*(x/a)**5)*integrate.quad(Bloch,0,a/x)[0] for x in xs]
    residual=ys-fxs  
    return residual

#フィッティングの初期値
parameter0=[300,1]
result=optimize.leastsq(Bloch_fit,parameter0,args=(array_x,array_y))
print(result)
a_fit=result[0][0]
b_fit=result[0][1]

#フィッティングパラメータを使用した関数の配列
list_y_fit=[]
for num in array_x:
    p=integrate.quad(Bloch,0,a_fit/num)
    list_y_fit.append((b_fit*(num/a_fit)**5)*p[0] )

array_y_fit=np.array(list_y_fit)

#フィッティング結果のプロット
plt.plot(array_x, array_y, marker="o",label="Numerical calculation")
plt.plot(array_x, array_y_fit, marker="",label="Fitting")
plt.title("Bloch-Gruneisen")
plt.xlabel('Temperature(K)')
plt.ylabel('resistivity(mOhm cm)')
plt.legend()
plt.savefig('Bloch-Gruneisen')
plt.show()
