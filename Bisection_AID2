import matplotlib.pyplot as plt

# Question #2:

def Bisection_AID2(f, a, b, tol=0.001, maxIters=10, plot_Intervals=False):
    
    iters = 0
    c = (a+b)/2
    while iters < maxIters or f(c)  > tol:
        
        print(f'{f(c)*f(a)}')  
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
        
        c = (a+b)/2    
        iters += 1
        if plot_Intervals == True:
            plt.scatter(a,f(a))
            plt.scatter(b,f(b))
            plt.scatter(c,f(c))
            plt.title('Bisection Points')
            plt.show()
            plt.clf()
        
    return c


