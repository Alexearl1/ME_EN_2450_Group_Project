import matplotlib.pyplot as plt
import numpy as np
import Newton_Raphson_AID2 as nr
from Mullers_AID2 import *
import Bisection_AID2 as bi
from Train_Class import *
from F_t_AID2 import *
from Train_mass_AID2 import *


def Train_Motion2(v,params):   
    
    #tspan = np.arange(0,11,1)
    g = params[0]       # m/s^2
    rho = params[1]     # kg/m^3
    m = params[2]       # kg
    A = params[3]       # m^2
    CD = params[4]      # N/a
    Crr = params[5]     # N/a
    Fp = params[6]      # N
        
    FD = (rho * CD * A * v**2)/2
    Frr = m*g*Crr
    #a = lambda v:  (Fp - (.5*rho * CD * A * v**2) - Frr)/m
    a = (Fp - FD - Frr)/m
    return a
"""
m1 = TrainMass(.2, 10, Hardware = 0, Density = 1440)
m2 = TrainMass(.3, 10, Hardware = 0, Density = 1440)
m3 = TrainMass(.4, 10, Hardware = 0, Density = 1440)
m4 = TrainMass(.5, 10, Hardware = 0, Density = 1440)

t1 = train(50, 10, .1, .025)
t2 = train(40, m1, .2, .02)
t3 = train(60, m2, .3, .03)
t4 = train(80, m3, .4, .035)
t5 = train(100, m4, .5, .04)
m = np.array([10,m1,m2,m3,m4])
"""
maxIters = 1000
tol = 0.0001
a = 7
b = 10
x0 = 5
x1 = 6
x2 = 7

params_t = [40,.05,.2,.02]
m = TrainMass(params_t[2], 10, Hardware = 0, Density = 1440)
params = [9.8,1.0,m,0.05,0.4,0.002,1.0]

F_t = F_thrust(params_t)
v = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#v = np.arange(1,11,1)
#y = np.zeros((1,np.size(v)))

for i in range(len(v)):
        
    y[i] = Train_Motion2(v[i],params)
        
v0_nr = nr.newton(Train_Motion2, 2, .001, 1*10**5)      # 6 iters
v0_bi = bi.Bisection_AID2(Train_Motion2, a, b, tol=0.001, maxIters=10, plot_Intervals=False) # 10 iters
v0_mu= Muller_Method_AID2(Train_Motion2,x0,x1,x2,maxIters,tol)  # 1 iters
print(v0_nr)
print(v0_bi)
print(v0_mu)


"""
1st Train: params_t = [50,.025,.1,.01]
Roots(nr,Iter):(8.966604708588346, 6)
Roots(bi,Iter):(8.96728515625, 10)
Roots(mu,Iter):(8.966604708583956, 1)

2nd Train: 
Roots(nr,Iter):
Roots(bi,Iter):
Roots(mu,Iter):
    
3rd Train: 
Roots(nr,Iter):
Roots(bi,Iter):
Roots(mu,Iter):
4th Train:
Roots(nr,Iter):
Roots(bi,Iter):
Roots(mu,Iter):
5th Train:
Roots(nr,Iter):
Roots(bi,Iter):
Roots(mu,Iter):

"""


