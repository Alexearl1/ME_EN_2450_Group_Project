import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import solve_ivp
from scipy.optimize import Bounds
from scipy.optimize import minimize
from tempfile import TemporaryFile

from rk4 import *
from Train_Motion import *
from plot_results import *

# Assumed position of piston would be behind the train, so total length is length_piston + length_train
time_start = time.process_time()
rho_t = {'PVC':1400, 'acrylic':1200, 'galvanized_steel':7700, 'stainless_steel':8000,
          'titanium':4500, 'copper':8940, 'aluminium':2700}   # kg/m^3

def Drive(var_params_i, rho_key):
    x0 = 0
    v0 = 0
    y0 = [x0,v0]
    tspan = np.linspace(0,20,1000)
    
    rw = 0.02    # m         
    mw = 0.1     # Kg        
    P_a = 101325 # Pa        
    rho_a = 1.0  # kg/m^3    
    mu = 0.7     # N/a       
    CD = 0.8     # N/a       
    Cr = 0.03    # N/a       
    
    const_params = [rho_a, P_a, CD, Cr, mu, rw, mw, rho_t[rho_key]]
    
    f = lambda tspan, y: train_Motion(tspan, y, const_params, var_params_i)
    t, y, t_final = rk4(f, tspan, y0)
    
    if t_final == np.inf:
        return t_final    
    else:
        l_track = 10
        l_runout = 2
        plot_results(t, x, v, l_track, l_runout, filename=None, title=None, interactive=False)
    
        return t_final

if __name__ == '__main__':
    
    Lt = (.2,.3)        # m
    ro = (0.05, 0.2)    # m
    P0 = (70000,200000)  # Pa
    rg = (0.002,0.01)   # m
    Ls = (0.1,0.5)      # m         
    rp = (0.02, 0.05)   # m
    
    #x0 = (0.25, 0.115, 96000, 0.005, 0.3, 0.032)   # Given Bounds Guess
    x0 = (0.2, 0.05, 70000, 0.002, 0.1, 0.02)      # Lower Bounds Guess
    #x0 = (.3, 0.2, 200000, 0.01, 0.5, 0.05)         # Upper Bounds Guess 
    bounds = (Lt, ro, P0, rg, Ls, rp)
    
    keys = rho_t.keys()
    times = []
    for key in keys:
        
        drive = lambda Input: Drive(Input, key)
        res = minimize(drive, x0, bounds = bounds, method='Nelder-Mead')
        times.append(drive(res.x))
        
        print("The outputs of the minimizatin is:\n", x0, '\n', times, file=open("output.txt","a"))
    
    print('\nThe viable materials for our train to be made out of are: Galvanized Steel, Stainless Steel, and Copper.')
    time_elapsed = (time.process_time()-time_start) 
    print('Computation Time:',time_elapsed, ' seconds.')
    
    