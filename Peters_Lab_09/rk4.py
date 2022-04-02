import numpy as np

def rk4(f, y0, tspan):
    h = tspan[1]-tspan[0]
    n = len(tspan)
    x = np.zeros(n+1)
    v = np.zeros(n+1)
    x[0], v[0] = y0[0], y0[1,0]
    print(n)
    
    """
    for i in range(len(n)):
        k1 = f(x[i], v[i])
        k2 = f(x[i] + 0.5*h, v[i] + 0.5*h*k1)
        k3 = f(x[i] + 0.5*h, v[i] + 0.5*h*k2)
        k4 = f(x[i] + h, v[i] + h*k3)
        x[i+1] = x[i] + h
        v[i+1] = v[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    """
    for i in range(n):
        k1 = f(x[i], v[i])
        k2 = f(x[i] + 0.5*h, v[i] + 0.5*h*k1)
        k3 = f(x[i] + 0.5*h, v[i] + 0.5*h*k2)
        k4 = f(x[i] + h, v[i] + h*k3)
        x[i+1] = x[i] + h
        print(x[i])
        print(x[i+1])
        v[i+1] = v[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    
    
    
    return x, v
