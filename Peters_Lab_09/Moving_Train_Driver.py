import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from rk4 import *
from Train_Motion import *

g = 9.8     # m/s^2
rho = 1.0   # kg/m^3
m = 10      # kg
A = .05     # m^2
CD = .4     # N/a
Crr = .002  # N/a
Fp = 1.0    # N
params = [g,rho,m,A,CD,Crr,Fp]

y0 = np.array([0,0]).reshape((-1,1))

tspan = np.arange(0,11,1)

f = lambda t,y: train_Motion(tspan,y0,params)
y = rk4(f, y0, tspan)

plt.plot(tspan,y[0,:], label = 'Position')
plt.plot(tspan,y[1,:], label = 'Velocity')
plt.title('Train Position / Velocity')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend(['Position','Velocity'],loc = 'upper left')
plt.grid(True)
plt.show()


ans_check = solve_ivp(fun, tspan, y0)