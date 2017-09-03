import numpy as np

""" Simulate the movement of a particle as part of a sound wave """

class Particule():

    def __init__(self, x_eq, amplitude):
        """ Define the starting position of the particle """
        self.x_eq = x_eq
        self.amplitude = amplitude

    def update_position(self, x):
        """ Calculate the new position of the particle """
        position = self.x_eq + self.amplitude*x
        return position
