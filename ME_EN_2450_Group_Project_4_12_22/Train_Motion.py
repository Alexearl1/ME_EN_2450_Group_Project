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
    
    rho_a, P_a, CD, Cr, mu, rw, mw, rho = const_params
    Lt, ro, P0, rg, Lr, rp = var_params
    g = 9.81
    
    A_t = np.pi*(ro**2)
    A_p = np.pi*(rp**2)
    ri = ro/1.15
    Lp = 1.5*Lr
    V = (Lp - Lr) * A_p                   # Volume of inner chamber of piston.
    m_tube = rho * Lt * np.pi*((ro**2)-(ri**2))
    m_pist = 1250 * (np.pi*(rp**2)*Lp)
    mt = m_pist + m_tube
    
    # Checking Initial Constraints:
    if  ro > .2:
        warnings.warn('Error: Train dimensions not acceptable.')
        return np.nan
    if Lp+Lt > 1.5:
        warnings.warn('Error: Train length not acceptable.')
        return np.nan
    if rg > rw:
        warnings.warn('Error: Pinion gear cannot be larger than wheel.')
        return np.nan
    
    # Forces: Alex Peters
    La = Lr*(rw/rg)
    Fr = mt*g*Cr
    
    Fd_coeff = 0.5 * rho_a*CD*A_t
    Fd = Fd_coeff*(v**2)
    
    P0 += P_a
    P = (P0*V)/(V + A_p*(rg/rw)*x)
    Ft = (A_p*rg/rw)*(P-P_a)
    
    # Checking for Dynamic Restraints:
    w_slip = mu*(mt/2)*g
    #print(Ft)
    #print(w_slip)
    
    if Ft > w_slip:
        warnings.warn('Error: Wheel Slippage.')
        return np.nan
    
    if x > 12.5:
        warnings.warn('Error: Train traveled too far.')
        return np.nan
    
    # Acceleration/Deceleration: Alex Peters
    if x <= La:
        #print(Ft, Fr,Fd)
        dvdt = (1/(mt + 2*mw)) * (Ft - Fd -Fr)
        dxdt = v
        dydt = [dxdt,dvdt]
    else:
        dvdt = (-Fd - Fr)/mt
        dxdt = v
        dydt = [dxdt,dvdt]
    #   if v == 0:
    
    return np.array(dydt)
