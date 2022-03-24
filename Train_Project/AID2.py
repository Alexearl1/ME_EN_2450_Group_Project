import numpy as np

from Train_Class import *

r_p = 10    # cm
r_g = 1.0   # cm
r_w = 2.5   # cm
p_0 = 50    # psig
Cr = 0.03   # N/a
#Cd =       # Aerodynamic drag coeff.
#v =        # Velocity of Train - Use root finding method (Bisection, Newton-Raphson, Muller's)


#t1 = train(p_0, m, r_p, r_g)

# eq for velocity and position: 
#   m * d^2x/dt^2 = F_t - (.5*rho*A*Cd*v^2) - (Cr*m*g)
#   ==> d^2x/dt^2 = (F_t - (.5*rho*A*Cd*v^2) - (Cr*m*g))/m:






