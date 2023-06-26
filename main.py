# simulation of a gas of particles obeying the lennard jones potential

'''Imports'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation 
from itertools import permutations

'''Configuration'''
# Lennard Jones constants
a = 5
b = 10

# parameter step size used in solving differential equation (Sympletic Euler Method is used)
tstep = 0.0001

# Window size
window = (10,20)

# List encoding the particle properties
#particles = [([0,0],0,10,[0,-0]),([1,0],1,10,[0, 0]),([1,1],2,10,[0, 0]),([0,1],3,10,[0, 0]),([0.5,3],4,100,[0, -200])] #((x,y),id,m,(vx,vy))

'''Functions'''

# Create particles
def createParticles(n,r):
    # Random position and velocity
    return [(r*np.random.randn(1,2)[0],i,1,[0,0]) for i in range(n)]

def createParticlesGrid(n,r):
    grid_2D = np.mgrid[-5:5:5j, -5:5:5j]
    points_2D = grid_2D.reshape(2, -1).T
    return [(point,n,1,[0,0]) for point,n in zip(points_2D,range(n**2))]

# Calculate the distance between every set of two particles, for x and y components
def distance(particles):
    p = [(i[0],i[1]) for i in particles]

    dx = np.zeros((len(particles),len(particles)))
    dy = np.zeros((len(particles),len(particles)))

    # Distance matrix for x and y
    for i in permutations(p,2):
        dx[i[0][1]][i[1][1]] = i[1][0][0]-i[0][0][0]
        dy[i[0][1]][i[1][1]] = i[1][0][1]-i[0][0][1]

    # Magnitude of the forces
    mag = np.sqrt(dx**2+dy**2)

    # Calculate unit vectors and return
    return np.nan_to_num(dx/mag), np.nan_to_num(dy/mag), mag

# Calculate the acceleration each particle experiences
def force(particles):
    # Distance matrix
    ux, uy, mag = distance(particles)
    
    force_magnitude_matrix = -1*np.nan_to_num(24*a*(b**6)*(mag**-7 - 2*b**2 * mag**-13))

    fx = force_magnitude_matrix*ux
    fy = force_magnitude_matrix*uy

    return fx.sum(axis=0),fy.sum(axis=0)

# Calculate the resulting displacement of the particles after tstep
def displace(particles):

    fx_vector,fy_vector = force(particles)

    mass_vector = np.array([i[2] for i in particles])

    ax_vector = fx_vector/mass_vector
    ay_vector = fy_vector/mass_vector

    vx_vector = ax_vector * tstep
    vy_vector = ay_vector * tstep

    #x += dx_vector
    #y += dy_vector

    # Calculate new particle positions
    for i,vx,vy in zip(particles,vx_vector,vy_vector):
        # Update velocity
        i[3][0] += vx
        i[3][1] += vy

        # update position
        i[0][0] += i[3][0] * tstep
        i[0][1] += i[3][1] * tstep

        # Keep within simulation bounds
        if i[0][0] < -window[0]/2 or i[0][0] > window[0]/2:
            i[3][0] *= -1

        if i[0][1] < -window[1]/2 or i[0][1] > window[1]/2:
            i[3][1] *= -1

    # Update particle positions
    x  = [i[0][0] for i in particles]
    y  = [i[0][1] for i in particles]

    v = [np.sqrt(i[0][0]**2 + i[0][1]**2) for i in particles]
    return x, y, ax_vector, ay_vector, v

fig = plt.figure()
ax = plt.axes(xlim=(-window[0]/2,window[0]/2),ylim=(-window[1]/2,window[1]/2))

particles=createParticlesGrid(5,10)
particles.append(([0,10],25,1,[100,-500]))
print(particles)
def animate(i):
    ax.clear()
    x,y,Ax,Ay,v = displace(particles)
    # Particle positions
    ax.scatter(x,y)
    ax.scatter(np.average(x),np.average(y))
    # Particle accelerations
    ax.quiver(x,y,Ax,Ay)
    plt.grid()
    plt.xlim([-window[0]/2,window[0]/2])
    plt.ylim([-window[1]/2,window[1]/2])
    ax.set_aspect('equal', adjustable='box')

ani = FuncAnimation(fig,animate,interval=0.00000000001)
plt.show()