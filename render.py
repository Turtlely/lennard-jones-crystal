# Plotting utils

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import config

class Renderer():
    def __init__(self,jobs):
        # List of particles to plot
        self.jobs = jobs

        # Create figure
        
        fig, ax = plt.subplots()

        # Window
        ax.set_xlim(config.xlim)
        ax.set_ylim(config.ylim)
        ax.set_aspect('equal')

        # Draw in boundaries

        #draw simulation boundaries
        ax.add_patch(Rectangle((config.xsimlim[0], config.ysimlim[0]), (config.xsimlim[1]-config.xsimlim[0]), (config.ysimlim[1]-config.ysimlim[0]),
                    edgecolor = 'black',
                    facecolor='white',
                    fill=False,
                    lw=2))

    def update(self):
        for p in self.jobs:
            plt.scatter(p.loc[0],p.loc[1])

        plt.show()