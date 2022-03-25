import numpy as np
import matplotlib.pyplot as plt

from Train_Class import *
from Euler_AID2 import *
from Train_Motion_AID2 import *
from F_t_AID2 import *
from Train_mass_AID2 import *
from Newton_Raphson_AID2 import *
from Mullers_AID2 import *
from Bisection_AID2 import *

#t1 = train(p_0, m, r_p, r_g)

# eq for velocity and position: 
#   m * d^2x/dt^2 = F_t - (.5*rho*A*Cd*v^2) - (Cr*m*g)
#   ==> d^2x/dt^2 = (F_t - (.5*rho*A*Cd*v^2) - (Cr*m*g))/m:

r_p = .1     # m radius of piston
r_g = .1    # m radius of pinion gear 
r_w = .25   # m radius of wheel
p_0 = 50    # psig Pressure of Tank
Cr = 0.03   # N/a Rolling resistance coeff.
CD = .82    # N/a Aerodynamic drag coeff.
#v =        # Velocity of Train - Use root finding method (Bisection, Newton-Raphson, Muller's)

g = 9.8     # m/s^2 --> Accel. due to Gravity
rho = 1.2   # kg/m^3 --> Density of air @20 Celsius
m = 10      # kg --> Mass of Train
A = .05     # m^2 --> Frontal Area of Train
F_t = 1     # N --> From part a?

l = 10      # length of inner chamber
h = 0      # Kg --> Mass of addition components
Density = 1440 #Kg/m^3 --> density of 40 PVC

m = TrainMass(r_p,l,h,Density)

param_t = [p_0,r_w,r_p, r_g]
F_t = F_thrust(param_t)

params = [g,rho,m,A,CD,Cr,F_t]

y0 = np.array([0,0]).reshape((-1,1))
tspan = np.arange(0,11,1)

# find: a, b, x0, x1, x2, x0,:

f = lambda t,y: train_Motion_AID2(tspan,y,params)
maxIters = int(100)
tol = 0.001
y = euler(f, tspan, y0)

a = y[1,2]
b = y[1,6] 

x0 = a
x1 = y[1,3]
x2 = y[1,4]

#Bi = Bisection_AID2(f, a, b, tol=0.001, maxIters=10, plot_Intervals=False)
Mull = Muller_Method_AID2(f,x0,x1,x2,maxIters,tol)
N_R = newton(fun, x0, tol, maxiter, fprime = None)

print(Mull)








plt.plot(tspan,y[0,:], label = 'Position')
plt.plot(tspan,y[1,:], label = 'Velocity')
plt.title('Train Position / Velocity')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend(['Position','Velocity'],loc = 'upper left')
plt.grid(True)
plt.show()


