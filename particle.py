#
# Copyright 2017-2018 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

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
