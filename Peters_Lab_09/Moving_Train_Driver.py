import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from rk4 import *
from Train_Motion import *

# Initialize Givens/Parameters:
    # Code from AID2 was used as a starting point.

Ls = 0.1    # m
rw = 0.025  # m
rg = 0.01   # m
rp = 0.01   # m
g = 9.81    # m/s^2
mw = 0.1    # Kg
P = 100e3   # kPa
rho = 1.0   # kg/m^3
mt = 10     # kg
A = 0.05    # m^2
mu = 0.7    # N/a
CD = 0.8    # N/a
Cr = 0.03   # N/a
a = (np.pi*pow(rp,2))
Fp = P * a  # N
La = (Ls*rw)/rg
params = [g, rho, mt, A, CD, Cr, mw, rw, rg, P, rp, Ls, La, Fp]

x0 = 0
v0 = 0
y0 = [x0,v0]

# Function/Calls: Alex
#   - and calculating necessary stepsize needed for convergence: Alex Peters and Shawn Haymore

for i in range(500):
    if i== 0:
        tspan = np.linspace(0,10)
    else:
        n = 1/(i*2)
        tspan = np.arange(0,10,n)
        
    f = lambda t, y : train_Motion(tspan, y, params)
    y, t = rk4(f, tspan, y0)
    
    ans = np.empty(y.shape)
    ans = np.array(y[0,i+1] - y[0,i])
    tol = 0.01
    # print(ans)        # To check what output of y is at each iter.
    if ans < tol:
        #print(i)       # To check # of iters.
        print('The rk4 function converges at a step size of:',n)
        break

# Plotting: Alex Peters

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
