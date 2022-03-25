import math as m

#Nathan Vance - AID2
#Train Mass Calculator
#Imputs mass in kg and length in m
#Outputs kg

def TrainMass(r_p, IL, Hardware = 0, Density = 1440):
    wallTHK = r_p*.06        #Approximate wall thickness to be 6% of the r_p
    OD = r_p + (2*wallTHK)   #Assuming 
    OL = IL + wallTHK
    vInner = m.pi*((r_p)**2) * IL
    vOuter = m.pi*((OD)**2) * OL
    vShell = vOuter - vInner
    mTrain = (vShell*Density) + Hardware
    
    return mTrain


"""
#10cm Long Pipe with 10cm r_p
print(TrainMass(.1,.1))

#Tank Mass (additional hardware mass = 0)
print(TrainMass(.1,.1,0))
"""
