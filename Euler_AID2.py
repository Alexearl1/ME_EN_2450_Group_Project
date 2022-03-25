import numpy as np

def euler(odefun, tspan, y0):
    
    y = np.zeros((2,tspan.shape[0]))
    
    y[:,0] = y0.flatten()
    
    for i in range(1,tspan.shape[0]):
        h = tspan[i] - tspan[i-1]
        
        y[:,i] = y[:,i-1] + h * odefun(tspan[i-1],y[:,i-1])
    
    return y
