def Muller_Method_AID2(f,x0,x1,x2,maxIters,tol):
    for i in range(maxIters):
        h0 = x1-x0
        h1 = x2-x1
        delta0 = (f(x1) - f(x0))/(x1-x0)
        delta1 = (f(x2) - f(x1))/(x2-x1)
        
        a = (delta1 - delta0)/(h1 + h0)
        b = a*h1 + delta1
        c = f(x2)
        
        d = (b**2 - 4*a*c)
        D = d ** (.5)
        
        if b < 0:
            D = -D
        x3 = x2 + (-2*c)/(b+D)
        
        if abs(x3-x2) < tol:
            break
    
        x0,x1,x2 = x1, x2,x3
        
    else:
        raise RuntimeError('Failed to find root')
    #print('The root is {0:f}'.format(x3))
    
    return x3, i