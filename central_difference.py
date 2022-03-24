#The central difference method is a numerial technique that calcualtes the
#derivative by implimenting the definition of the derivative for small step
#sizes.
#Inputs:
 #  -func: the function being differentiated
 #  -x: position at which the derivative is being determined  
  # -dx: step size 
#Output:
#   - dp: the derivative of func at a point x

import numpy as np
def central_difference(fun, x, dx):
    if abs(dx) < np.finfo(float).eps:
        raise ValueError('dx must be greater than 0')
    return (fun(x+dx) - fun(x-dx)) / (2 * dx)

