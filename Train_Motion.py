import numpy as np


def train_Motion_AID2(tspan,y,params):
    """
    d^2x/dt^2 = a = (Fp - FD - Frr)/m
    Fp = Constant
    FD = (rho * CD * A * v^2)/2
    Frr = m*g*Crr
    """
    
    x,v = y[0], y[1]
    
    g = params[0]
    rho = params[1]
    m = params[2]
    A = params[3]
    CD = params[4]
    Cr = params[5]
    F_t = params[6]
    
    FD = (rho * CD * A * v**2)/2
    Frr = m*g*Cr
    
    a = (F_t - FD - Frr)/m
    dydt = np.array([[v],[a]]).reshape((-1,1)) # array , [0] = velocity, [1] = acceleration.
    
    return dydt.flatten()







