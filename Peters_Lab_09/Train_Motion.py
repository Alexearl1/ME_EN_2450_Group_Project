import numpy as np


def train_Motion(t, y, params):
    """
    a = d^2x/dt^2 = (Fp - FD - Frr)/m
    Fp = Force of Thrust
    FD = Force of Drag
    Fr = Force of Rolling Resistance
    """
    x = y[0]
    v = y[1]
    g = params[0]
    rho = params[1]
    mt = params[2]
    A = params[3]
    CD = params[4]
    Cr = params[5]
    mw = params[6]
    rw = params[7]
    rg = params[8]
    P = params[9]
    rp = params[10]
    Ls = params[11]
    La = params[12]
    Fp = params[13]
    
    # Forces:
    T = rg * Fp
    Fd = 0.5 * (rho*CD*A*pow(v,2))
    Fr = mt*g*Cr
    
    # Acceleration/Deceleration:
    if x <= La:
        dvdt = (1/(mt + 2*mw)) * ((T/rw) - Fd -Fr)
        dxdt = v
        dydt = [dxdt,dvdt]
    else:
        dvdt = (-Fd - Fr)/mt
        dxdt = v
        dydt = [dxdt,dvdt]
    
    return np.array(dydt)
