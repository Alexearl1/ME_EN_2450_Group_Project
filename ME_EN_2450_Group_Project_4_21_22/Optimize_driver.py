import sys
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp
from scipy.optimize import Bounds
from scipy.optimize import minimize


from rk4 import *
from Train_Motion import *
from plot_results import *

# Assumed position of piston would be behind the train, so total length is length_piston + length_train
rho_t = {'PVC':1400, 'acrylic':1200, 'galvanized_steel':7700, 'stainless_steel':8000,
          'titanium':4500, 'copper':8940, 'aluminium':2700}   # kg/m^3
    

def wrapper_train_motion(const_params, var_params, t_final=20, n=200, return_only_time=True):
    
    rho_a,P_a,CD,Cr,mu,rw,mw,rho = const_params
    Lt,ro,P0,rg,Lr,rp = var_params
    Lp = 1.5*Lr
    
    y0 = np.zeros(2)
    odefun = lambda t,y: train_Motion(t, y, const_params, var_params)
    
    # Checking Ranges for Physical Constraints:
    if  ro > .2:
        warnings.warn('Error: Train dimensions not acceptable.')
        return np.nan
    if Lp+Lt > 1.5:
        warnings.warn('Error: Train length not acceptable.')
        return np.nan
    if rg > rw:
        warnings.warn('Error: Pinion gear cannot be larger than wheel.')
        return np.nan
   
    tspan = np.linspace(0,t_final,n)
    t, y = rk4(odefun, tspan, y0)
    
    if y[:,0].max() > 12.5 and y[:,0].max() < 10:
        warnings.warn('Error: Train traveled too far.')
        return np.nan
    
    if return_only_time is True:
        return t[-1]
    return t, y
    
    
if __name__ == '__main__':
    
    Lt = (.2,.3)        # m
    ro = (0.05, 0.2)    # m
    P0 = (70000,200000)  # Pa
    rg = (0.002,0.01)   # m
    Ls = (0.1,0.5)      # m         
    rp = (0.02, 0.05)   # m
    
    x0 = (0.25, 0.115, 105000.0, 0.005, 0.3, 0.032)   # Given Bounds Guess
    #x0 = (0.2, 0.05, 70000, 0.002, 0.1, 0.02)       # Lower Bounds Guess
    #x0 = (.3, 0.2, 200000, 0.01, 0.5, 0.05)        # Upper Bounds Guess 
    bounds = (Lt, ro, P0, rg, Ls, rp)
    
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
    
    Lt=0.25
    ro= 0.115
    P0= 115000.0
    rg= 0.005
    Lr= 0.3
    rp= 0.032
    var_params = np.array([Lt, ro, P0, rg, Lr, rp])
    const_params = [rho_a, P_a, CD, Cr, mu, rw, mw, rho_t['stainless_steel']]
    t,y = wrapper_train_motion(const_params, var_params, return_only_time=False)
    
    plt.plot(t,y[:,0])
    plt.plot(t,y[:,1])
    plt.show()
    
    keys = rho_t.keys()
    times = []
    for key in keys:
        
        const_params = [rho_a, P_a, CD, Cr, mu, rw, mw, rho_t[key]]
        
        drive = lambda var_params: wrapper_train_motion(const_params, var_params, return_only_time=True)
        
        res = minimize(drive, x0, bounds = bounds, method='Nelder-Mead')
        times.append(drive(res.x))
        
        print("The outputs of the minimizatin is:\n", x0, '\n', times, file=open("output.txt","a"))
        
        
    #print('\nThe viable materials for our train to be made out of are: Galvanized Steel, Stainless Steel, and Copper.')

    