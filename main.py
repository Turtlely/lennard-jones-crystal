from concurrent.futures.process import _global_shutdown
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import particle
import numpy as np
import config
import potential
from solver import timestep
import time
import matplotlib.animation as animation


# Create a set of 10 particles, at random positions between bounds
locset = config.C * np.random.rand(config.n,2)
# Set of particles
pset = [particle.Particle(loc=p,Fvect=[0.0,0.0],m=0.01) for p in locset]

# Check each particle, calculate the net vector force on it
for p in pset:
    netForce = np.array([0.0,0.0])
    for a in filter(lambda a: a != p, pset):
        Fscale, r = potential.calculateForce(p.loc,a.loc)
        vect = Fscale * (a.loc - p.loc)/r
        netForce += vect
    p.Fvect = netForce

# Color each particle depending on its net force
for p in pset:
    m = np.linalg.norm(p.Fvect)
    plt.scatter(p.loc[0],p.loc[1],c='black')

# Simulate

def animate(i):
    for particle in pset:
        timestep(particle)
        ax.scatter(particle.loc[0],particle.loc[1],c='black')    

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
