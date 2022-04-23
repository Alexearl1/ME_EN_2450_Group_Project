import warnings
import numpy as np

# Train Motion Function: Alex Peters
#   - Code from Lab9 was used as a starting point.

def train_Motion(t, y, const_params, var_params):
    """
    a = d^2x/dt^2 = (Fp - FD - Frr)/m
    Fp = Force of Thrust
    FD = Force of Drag
    Fr = Force of Rolling Resistance
    """
    # Initializing Variables:
    x = y[0]
    v = y[1]
    g = 9.81
    
    rho_a,P_a,CD,Cr,mu,rw,mw,rho = const_params
    Lt,ro,P0,rg,Lr,rp = var_params
    
    # Initializing Needed Equations using Variables:
    A_t = np.pi*(ro**2)
    A_p = np.pi*(rp**2)
    ri = ro/1.15
    Lp = 1.5*Lr
    V0 = np.pi*(rp**2)                   # Volume of inner chamber of piston.
    m_tube = (((np.pi * (ro**2) * Lt) - (np.pi * (ri**2) * Lt)) *rho)
    m_pist = 1250 * A_p * Lp
    mt = m_pist + m_tube + (2*mw)
    
    # Calculating Forces:
    La = Lr*(rw/rg)
    Fr = mt*g*Cr
    Fd = 0.5 * rho_a*CD*A_t*(v**2)
    
    x_transition = Lp * rw/rg
    Ft = ((rg*A_p)/rw) * ((((P0+P_a)*V0)/(V0 + (A_p*(rg/rw)*x_transition))) - P_a)
    
    # Checking for Design Constraints:
    w_slip = mu*(mt/2)*g
    
    #print(P, P0, P_a, V, A_p, rg, rw, x)
    
    # Acceleration/Deceleration:
    if x <= La:
        #print(Ft, Fr,Fd)
        dvdt = (1/(mt + 2*mw)) * (Ft - Fd -Fr)
        dxdt = v
        dydt = [dxdt,dvdt]
    else:
        dvdt = (-Fd - Fr)/mt
        dxdt = v
        dydt = [dxdt,dvdt]
    
    if Ft - (mw*dvdt)> w_slip:
        warnings.warn('Error: Wheel Slippage occurs.')
        return np.array([np.nan,np.nan])
    
    return np.array(dydt)
