# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:23:34 2022

@author: u1095484
"""

import math as m

#Nathan Vance - AID2
#Train Mass Calculator
#Imputs mass in kg and length in cm
#Outputs kg

def TrainMass (ID, ILength, Hardware = .5, Density = .00144):
    wallTHK = ID*.06 #Approximate wall thickness to be 6% of the ID
    OD = ID + (2*wallTHK) #Assuming 
    OLength = ILength + wallTHK
    vInner = m.pi*((ID/2)**2) * ILength
    vOuter = m.pi*((OD/2)**2) * OLength
    vShell = vOuter - vInner
    mTrain = (vShell*Density) + Hardware
    
    return mTrain

#%% Testing

#10cm Long Pipe with 10cm ID
print(TrainMass(10,10))

#Tank Mass (additional hardware mass = 0)
print(TrainMass(10,10,0))

