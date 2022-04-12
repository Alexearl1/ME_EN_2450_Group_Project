import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import Bounds
from scipy.optimize import minimize

from rk4 import *
from Train_Motion import *
from plot_results import *

# Initialize Givens/Parameters:
    # Code from Lab9 was used as a starting point.
x0 = 0
v0 = 0
y0 = [x0,v0]

rw = 0.02    # m         1
g = 9.81     # m/s^2
mw = 0.1     # Kg        1
P_a = 101325 # Pa        1
rho = 1.0    # kg/m^3    1
mt = 10      # kg
A = 0.05     # m^2
mu = 0.7     # N/a       1
CD = 0.8     # N/a       1
Cr = 0.03    # N/a       1

#ri = ro/1.15
#Lp = 1.5*Ls
#Mp = 1250 * (np.pi*(rp**2)*Lp)
    
Lt = (.2,.3)        # m
ro = (0.05, 0.2)    # m
rho_t = {'PVC':1400, 'acrylic':1200, 'galvanized_steel':7700, 'stainless_steel':8000,
          'titanium':4500, 'copper':8940, 'aluminium':2700}   # kg/m^3
P0 = (70000,20000)  # Pa
rg = (0.002,0.01)   # m
Ls = (0.1,0.5)      # m         
rp = (0.02, 0.05)   # m
x0 = [0.25, 0.115, 96000, 0.005, 0.3, 0.032]
bounds = (Lt, ro, P0, rg, Ls, rp)

for rho in rho_t.values():
    
    rp = bounds[5]
    rg = bounds[3]
    print(type(rp))
    print(rp)

    phys_params = [mt, mw, rw, rg, La, Fr, Fd_coeff, P0, Ap, P_a, g, mu, rho]

    res = minimize(f, x0, bounds, method='Nelder-Mead')




# Function/Calls: Alex
#   - and calculating necessary stepsize needed for convergence: Alex Peters and Shawn Haymore
"""
for i in range(500):
    if i== 0:
        tspan = np.linspace(0,10)
    else:
        n = 1/(i*2)
        tspan = np.arange(0,10,n)
        
    f = lambda t, y : train_Motion(tspan, y, phys_params)
    y, t = rk4(f, tspan, y0)
    
    ans = np.empty(y.shape)
    ans = np.array(y[0,i+1] - y[0,i])
    tol = 0.01
    # print(ans)        # To check what output of y is at each iter.
    if ans < tol:
        #print(i)       # To check # of iters.
        print('The rk4 function converges at a step size of:',n)
        break
"""

# Plotting: Alex Peters
"""
x = y[0,:]
v = y[1,:]

plt.plot(t, x, 'r-', label='Position')
plt.plot(t, v, 'b-', label='Velocity')
plt.title('Position & Velocity')
plt.xlabel('Time (s)')
plt.legend(['Position','Velocity'],loc = 'upper left')
plt.grid(True)
plt.show()
#plt.savefig('Position_&_Velocity.pdf')     # Wasn't working, only output a blank white graph. 
"""