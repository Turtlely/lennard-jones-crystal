
# Particle
class Particle():
    def __init__(self,loc,Fvect,m):
        # Location of a particle encoded in a list of form [x,y]
        self.loc = loc
        
        # Force vector on a particle
        self.Fvect = Fvect

        # Mass of each particle
        self.m = m

        # Velocity of each particle
        self.v = [0,0]