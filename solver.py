# calculate position of each particle

tstep = 0.01

def timestep(particle):
    # Calculate acceleration
    a = particle.Fvect/particle.m

    # Calculate velocity
    particle.v += a*tstep

    # Calculate position
    particle.loc += particle.v*tstep