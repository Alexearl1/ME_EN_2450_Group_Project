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
    x = y[0]
    v = y[1]
    rho_a, P_a, CD, Cr, mu, rw, mw, rho = const_params
    Lt, ro, P0, rg, Ls, rp = var_params
    g = 9.81
    
    A = np.pi*(ro**2)
    ri = ro/1.15
    Lp = 1.5*Ls
    V = (np.pi*(ri**2)*Lp)              # Volume of inner chamber of piston.
    m_tube = rho * ((ro**2)-(ri**2))
    m_pist = 1250 * (np.pi*(ri**2)*Lp)
    mt = m_pist + m_tube
    
    # Forces: Alex Peters
    
    Ap = np.pi*(rp**2)
    La = Ls*(rw/rg)
    Fr = mt*g*Cr
    
    Fd_coeff = 0.5 * rho*CD*A
    Fd = Fd_coeff*(v**2)
    
    P = (P0*V)/(V + Ap*(rg/rw)*x)
    #import pdb;pdb.set_trace()
    Ft = (Ap*rg/rw)*(P-P_a)

    # Checks for restraints: I think this is wrong:
    """ 
    w_slip = mu*(mt/2)*g
    print('Ft:', Ft)
    print('w_slip:', w_slip)
    
    if Ft > w_slip:
        import pdb;pdb.set_trace()
        raise ValueError('Error: Wheel Slippage.')
    
    if x > 12.5:
        import pdb;pdb.set_trace()
        raise ValueError('Error: Train traveled too far.')
    """
    # Acceleration/Deceleration: Alex Peters
    
    if x <= La:
        dvdt = (1/(mt + 2*mw)) * (Ft - Fd -Fr)
        dxdt = v
        dydt = [dxdt,dvdt]
    else:
        dvdt = (-Fd - Fr)/mt
        dxdt = v
        dydt = [dxdt,dvdt]
        if v == 0:
            return np.array(dydt)
