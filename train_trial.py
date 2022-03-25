import matplotlib.pyplot as plt
import numpy as np
import Newton_Raphson_AID2 as nr

def Train_Motion2(v):
    g = 9.8     # m/s^2
    rho = 1.0   # kg/m^3
    m = 10      # kg
    A = .05     # m^2
    CD = .4     # N/a
    Crr = .002  # N/a
    Fp = 1.0    # N
    params = [g,rho,m,A,CD,Crr,Fp]
    #tspan = np.arange(0,11,1)

    g = params[0]
    rho = params[1]
    m = params[2]
    A = params[3]
    CD = params[4]
    Crr = params[5]
    Fp = params[6]
        
    FD = (rho * CD * A * v**2)/2
    Frr = m*g*Crr
        
    a = (Fp - FD - Frr)/m
    return(a)

v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#v = np.arange(1,11,1)
#y = np.zeros((1,np.size(v)))

for i in range(len(v)):
    y[i] = Train_Motion2(v[i])



plt.plot(v,y)
plt.show()
v0 = nr.newton(Train_Motion2, 2, .001, 1*10**5)