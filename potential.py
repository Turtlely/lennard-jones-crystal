# Function to calculate the lennard jones potential of two particles
import numpy as np
import config

def calculatePotential(a,b):
    r = np.linalg.norm(a.loc - b.loc)
    return (config.A/np.power(r,12))-(config.B/np.power(r,6))

def calculateForce(a,b):
    r = np.linalg.norm(a - b)
    return -12 * config.A * np.power(r,-13) + 6 * config.B * np.power(r,-7), r
