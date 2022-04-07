import numpy as np

# rk45 Function: Alex Peters

def rk4(f, t, y0):
    n = len(t) - 1
    h = t[1] - t[0]
    y = np.empty((2, n+1))
    y[:,0] = y0
    
    for i in range(n):
        k1 = f(t[i], y[:,i])
        k2 = f(t[i] + 0.5*h, y[:,i] + 0.5*h*k1)
        k3 = f(t[i] + 0.5*h, y[:,i] + 0.5*h*k2)
        k4 = f(t[i] + h, y[:,i] + h*k3)
        
        y[:, i+1] = y[:,i] + h*((k1 + 2*k2 + 2*k3 + k4)/6)
    return y, t

"""
Initial Code from lecture #16:
    
for n in range(len(n)):
    k1 = f(x[n], y[n])
    k2 = f(x[n] + 0.5*h, y[n] + 0.5*h*k1)
    k3 = f(x[n] + 0.5*h, y[n] + 0.5*h*k2)
    k4 = f(x[n] + h, y[n] + h*k3)
    x[n+1] = x[n] + h
    y[n+1] = y[n] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    

def rk4(f, x, y0):
    y = np.zeros([np.shape(y0)[0], len(x)])
    y[:,0] =  y0[:,0]
    
    for i in range(len(x)-1):
        
        h = x[i+1] - x[i]
        k1 = h * f(x[i] , y[:,i])
        k2 = h * f(x[i] + 0.5*h , y[:,i] + 0.5*h*k1)
        k3 = h * f(x[i] + 0.5*h , y[:,i] + 0.5*h*k2)
        k4 = h * f(x[i] + h , y[:,i] + h*k3)
        x[i+1] = x[i] + h
        y[:, i+1] = y[:,i] + h*(k1 + 2*k2 + 2*k3 + k4)/6

    return x,y
"""