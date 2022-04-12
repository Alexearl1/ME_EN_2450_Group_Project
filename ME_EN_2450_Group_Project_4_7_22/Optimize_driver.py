import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import Bounds
from scipy.optimize import minimize

from rk4 import *
from Train_Motion import *
from plot_results import *

rho_t = {'PVC':1400, 'acrylic':1200, 'galvanized_steel':7700, 'stainless_steel':8000,
          'titanium':4500, 'copper':8940, 'aluminium':2700}   # kg/m^3

def drive(var_params_i, rho_key='PVC'):

    x0 = 0
    v0 = 0
    y0 = [x0,v0]
    n = 0.2
    tspan = np.arange(0,20.2, n)
    
    rw = 0.02    # m         1
    mw = 0.1     # Kg        1
    P_a = 101325 # Pa        1
    rho_a = 1.0    # kg/m^3    1
    mu = 0.7     # N/a       1
    CD = 0.8     # N/a       1
    Cr = 0.03    # N/a       1
        
    const_params = [rho_a, P_a, CD, Cr, mu, rw, mw, rho_t[rho_key]]
    
    f = lambda tspan, y: train_Motion(tspan, y, const_params, var_params_i)
    t, y = rk4(f, tspan, y0)
    #import pdb;pdb.set_trace()
    
    return t[-1]

if __name__ == '__main__':
    
    Lt = (.2,.3)        # m
    ro = (0.05, 0.2)    # m
    P0 = (70000,20000)  # Pa
    rg = (0.002,0.01)   # m
    Ls = (0.1,0.5)      # m         
    rp = (0.02, 0.05)   # m
    
    x0 = [0.25, 0.115, 96000, 0.005, 0.3, 0.032]
    bounds = (Lt, ro, P0, rg, Ls, rp)
    
    print(drive(x0))
    
    #res = minimize(f, x0, bounds, method='Nelder-Mead')
    
    """
    if  ro > .2:
        raise ValueError('Error: Train dimensions not acceptable.')
    
    if Lp+Lt > 1.5:
        raise ValueError('Error: Train length not acceptable.')
        
    if rg > rw:
        raise ValueError('Error: Pinion gear cannot be larger than wheel.')
    """
    
    