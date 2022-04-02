import numpy as np


def train_Motion(tspan,y,params):
    """
    d^2x/dt^2 = (Fp - FD - Frr)/m
    Fp = Constant
    FD = (rho * CD * A * v^2)/2
    Frr = m*g*Crr
    """
    
    x,v = y[0], y[1,0]
    
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
    dydt = np.array([[v],[a]]).reshape((-1,1))
    
    return dydt.flatten()




