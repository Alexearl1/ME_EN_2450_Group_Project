import matplotlib.pyplot as plotter
from central_difference import central_difference
def newton(fun, x0, tol, maxiter, fprime = None):
    
    if fun(x0) == 0:
        return(x0)
    
    if fprime is None:
        fprime = lambda x: central_difference(fun, x, 1e-4)     
    
    

    count = 1
    while True:
        
        if fprime(x0) == 0:            
            print("Warning! zero derivative!")
            break        
        if count == 1:
            dx = -fun(x0)/fprime(x0)
            x = x0 + dx
            eApprox = (x - x0)/x0
        else:
            dx = -fun(xPrev)/fprime(xPrev)
            x = xPrev + dx
            eApprox = (x - xPrev)/xPrev 
        if count > maxiter:
            raise RuntimeError("Exceeded max iter")             
        if abs(dx) <= tol or abs(eApprox) <= tol:
            break
        print(eApprox)
        
        plotter.plot(x,fun(x),'.r')
        xPrev = x
        count += 1
    plotter.show()
    print("# steps:",count)
    return(x)
            
            
        
