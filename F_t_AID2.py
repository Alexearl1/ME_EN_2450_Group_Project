import math
def F_thrust(params):
    p_0 = params[0]
    r_w = params[1]
    r_p = params[2]
    r_g = params[3]
    
    #Assuming r_w,r_p & r_g given in meters, p_0 in psi
    
    #Convert p_0 to Pa
    
    p_0 = p_0 * 6894.76
    
    F_rack = p_0 *math.pi*r_p**2
    F_t = (F_rack*r_g)/r_w
    
    return(F_t)
    
    
