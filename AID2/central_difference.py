
import numpy as np
def central_difference(fun, x, dx):
    if abs(dx) < np.finfo(float).eps:
        raise ValueError('dx must be greater than 0')
    return (fun(x+dx) - fun(x-dx)) / (2 * dx)



