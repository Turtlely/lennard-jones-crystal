# Various potentials to expose particles to
import numpy as np
import config

# Basic LJ potential
def V(a,b):
    r = np.linalg.norm(np.array(a.loc)-np.array(b.loc))
    return 4*config.e*(np.power(config.sigma/r,12)-np.power(config.sigma/r,6))

def V(r):
    #r = np.linalg.norm(np.array(a.loc)-np.array(b.loc))
    return 4*config.e*(np.power(config.sigma/r,12)-np.power(config.sigma/r,6))


def F(a,b):
    r = np.linalg.norm(np.array(a.loc)-np.array(b.loc))
    return -24*config.e*np.power(config.sigma,6)*((2*np.power(config.sigma,6)/np.power(r,13))-np.power(r,-7))