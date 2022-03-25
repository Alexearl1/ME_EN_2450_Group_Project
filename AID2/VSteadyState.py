from math import sqrt

def VSteadyState(params):
    g = params[0]
    rho = params[1]
    m = params[2]
    A = params[3]
    CD = params[4]
    Cr = params[5]
    F_t = params[6]
    
    EQ1 = ((F_t/m) - (Cr*g))
    EQ2 = 2*m/(rho*A*CD)
    vSteadyState = sqrt(EQ1*EQ2)
    
    return vSteadyState

""" Testing
g = 9.8     # m/s^2
rho = 1.0   # kg/m^3
m = 10      # kg
A = .05     # m^2
CD = .4     # N/a
Crr = .002  # N/a
Fp = 1.0    # N force traction
params = [g,rho,m,A,CD,Crr,Fp]

print(VSteadyState(params))
"""