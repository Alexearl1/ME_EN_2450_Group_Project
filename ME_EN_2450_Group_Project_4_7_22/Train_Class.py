from math import pi

class train:
    def __init__(self, piston_stroke_length, wheel_radius, piston_radius, acceleration_gravity, wheel_mass, tank_pressure, 
                 air_density, train_mass, frontal_area, coeff_static_friction):
        self.p_l = piston_stroke_length
        self.w_r = wheel_radius
        self.p_r = piston_radius
        self.g = acceleration_gravity
        self.w_m = wheel_mass
        self.p_0 = tank_pressure
        self.a_d = air_density
        self.t_m = train_mass
        self.f_a = frontal_area
        self.u_s = coeff_static_friction
   

    # "Error: Non-default argument follows default argument."
    """
    def TrainMass (ID, IL, Hardware = 0, Density):
        wallTHK = ID*.06        #Approximate wall thickness to be 6% of the ID
        OD = ID + (2*wallTHK)   #Assuming 
        OL = IL + wallTHK
        vInner = pi*((ID/2)**2) * IL
        vOuter = pi*((OD/2)**2) * OL
        vShell = vOuter - vInner
        mTrain = (vShell*Density) + Hardware
        
        return mTrain
    """
#t1 = train(p_l, w_r, p_r, g, w_m, p_0, a_d, t_m, f_a, u_s)
