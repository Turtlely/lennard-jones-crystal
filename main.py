# Generic particle simulation with boundaries
from render import Renderer
import particle

# Create set of locations
import numpy as np
import config

# Grid of evenly spaced points
grid = np.dstack(np.meshgrid(np.linspace(config.xsimlim[0]+1,config.xsimlim[1]-1,int(np.sqrt(config.n))), np.linspace(config.ysimlim[0]+1,config.ysimlim[1]-1,int(np.sqrt(config.n))), indexing='ij'))

jobs = []

# Create set of n particles
for x in range(int(np.sqrt(config.n))):
    for y in range(int(np.sqrt(config.n))):
        jobs.append(particle.Particle(loc=(grid[x][y][0],grid[x][y][1]),m=1))

# Begin simulation

# Simulation loop

# Graphs
import potential
import matplotlib.pyplot as plt
x = np.linspace(0,10,20)
y = potential.V(x)
plt.plot(x,y)
plt.show()
quit()
renderer = Renderer(jobs)
renderer.update()