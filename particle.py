
# Particle
class Particle():
    def __init__(self,loc,m):
        # Location of a particle encoded in a list of form [x,y]
        self.loc = loc
        
        # Mass of each particle
        self.m = m
        
        self.v = [0,0]
        self.a = [0,0]