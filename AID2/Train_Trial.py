import matplotlib.pyplot as plt
import numpy as np
import Newton_Raphson_AID2 as nr
from Mullers_AID2 import *
import Bisection_AID2 as bi
from Train_Class import *
from F_t_AID2 import *
from Train_mass_AID2 import *
from VSteadyState import *

def Train_Motion2(v):   
    
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

t1 = train(50, 10, .025, .1, .01)
t2 = train(40, 20, .05, .2, .02)
t3 = train(60, 30, .045, .3, .03)
t4 = train(80, 40, .035, .4, .04)
t5 = train(100, 50, .03, .5, .05)
m = np.array([10,m1,m2,m3,m4])
"""
maxIters = 100
tol = 0.0001
a = 7
b = 10
x0 = 5
x1 = 6
x2 = 7

params_t = [80,.035,.4,.04]
#m = TrainMass(params_t[2], 10, Hardware = 0, Density = 1440)
#print(m)

params = [9.8,1.0,50,0.05,0.4,0.002,1.0]
F_t = F_thrust(params_t)
v = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#v = np.arange(1,11,1)
#y = np.zeros((1,np.size(v)))

for i in range(len(v)):
        
    y[i] = Train_Motion2(v[i])
        
v0_nr, nr_iters = nr.newton(Train_Motion2, 2, .001, 1*10**5)      # 6 iters
v0_bi, bi_iters = bi.Bisection_AID2(Train_Motion2, a, b, tol=0.001, maxIters=10, plot_Intervals=False) # 10 iters
v0_mu, mu_iters = Muller_Method_AID2(Train_Motion2,x0,x1,x2,maxIters,tol)  # 1 iters


V_true = VSteadyState(params)

Nr_er = (V_true-v0_nr)
Bi_er = (V_true-v0_bi)
Mu_er = (V_true-v0_mu)
#print('VSteadyState is:',V_true)
#print('True - Newton approx is:',Nr_er)
#print('True - Bisection approx is:',Bi_er)
#print('True - Mullers approx is:',Mu_er)

"""
1st Train: params_t = [50,.025,.1,.01]
Roots(nr,Iter):(8.966604708588346, 6)
Roots(bi,Iter):(8.96728515625, 10)
Roots(mu,Iter):(8.966604708583956, 1)


2nd Train: params_t = [40,.05,.2,.02]
Roots(nr,Iter):(7.797436271885866, 5)
Roots(bi,Iter):(7.79833984375, 10)
Roots(mu,Iter):(7.797435475847171, 1)
    
3rd Train: params_t = [60,.045,.3,.03]
Roots(nr,Iter):(6.418722628480977, 5)
Roots(bi,Iter):(9.99853515625, 10)
Roots(mu,Iter):(6.418722614352485, 1)

4th Train:params_t = [80,.035,.4,.04]
Roots(nr,Iter):(4.647580015450393, 5)
Roots(bi,Iter):(9.99853515625, 10)
Roots(mu,Iter):(4.6475800154488995, 1)

5th Train:params_t = [100,.03,.5,.05]
Roots(nr,Iter):(1.4142135623746857, 4)
Roots(bi,Iter):(9.99853515625, 10)
Roots(mu,Iter):(1.414213562373091, 1)

True - Newton approx is: -1.5949463971764999e-12
True - Bisection approx is: -8.58432159387691
True - Mullers approx is: -2.220446049250313e-16
"""


