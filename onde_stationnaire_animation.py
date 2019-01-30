#
# Copyright 2017-2019 Manuel Barrette
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

from PyQt5 import QtWidgets
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.animation as anim
import os, platform
import particle


class Animation():
    def stopAnim(self):
        self.oscillation.event_source.stop()

    def enregistrer(self):
        systeme_exploitation = platform.system()
        if systeme_exploitation == 'Windows':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, 'Enregister sous...', os.getenv('HOMEPATH'), 'Vidéos (*.mp4)')
        elif systeme_exploitation == 'Darwin' or 'Linux':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, 'Enregister sous...', os.getenv('HOME'), 'Vidéos (*.mp4)')
        else:
            print("Système non supporté officiellement.  Enregistrement dans le dossier de travail sous le nom 'animation.mp4'.")
            fichier = ['animation', None]
        return fichier[0]

    def exporterAnimation(self, canvas, figure, slider, combo):
        nom_anim = self.enregistrer()
        if nom_anim[-4:] != ".mp4":
            nom_anim = nom_anim + ".mp4"
        self.oscillation.save(nom_anim)
        self.animationTempsReel(canvas, figure, slider, combo)


    def initAnimation(self, slider, combo):
        """ Define parameters and setup the base graphic """

        self.figure.clear()

        # Important parameters
        nb_nodes = slider
        if combo == 1:
            tuyau_ferme = True
        else:
            tuyau_ferme = False

        nb_particules_hor = 15
        longueur = 20
        num_frames = 45
        period = 30
        omega = 2*np.pi/period
        grilley = [0]
        #grilley = [-0.5, 0, 0.5]

        grillex = np.linspace(0, longueur, 100)

        self.ax1 = self.figure.add_subplot(311)
        self.ax2 = self.figure.add_subplot(312, sharex=self.ax1)
        self.ax3 = self.figure.add_subplot(313, sharex=self.ax1)

        self.ax1.add_patch(Rectangle((-0.5, 0.85), 21, 0.1, color='k', alpha=1))
        self.ax1.add_patch(Rectangle((-0.5, -0.95), 21, 0.1, color='k', alpha=1))
        self.ax1.axis([-1, longueur + 1, -1, 1])

        self.ax2.axis([-1, longueur + 1, -1, 1])
        self.ax3.axis([-1, longueur + 1, -1, 1])

        self.ax1.set_ylabel('Particules\n dans tuyau')
        self.ax2.set_ylabel('Déplacement')
        self.ax3.set_ylabel('Pression')

        self.ax1.yaxis.set_label_coords(-0.06, 0.5)
        self.ax2.yaxis.set_label_coords(-0.1, 0.5)
        self.ax3.yaxis.set_label_coords(-0.1, 0.5)

        self.ax1.set_yticks([])
        self.ax2.set_yticks([0])
        self.ax3.set_yticks([0])

        self.ax2.set_yticklabels([r"$0$"])
        self.ax3.set_yticklabels([r"$p_{atm}$"])

        self.ax2.grid(True)
        self.ax3.grid(True)

        self.ax3.set_xticks([])

        # Differences between open and closed pipes
        if tuyau_ferme:
            self.ax1.add_patch(Rectangle((-0.7, -0.95), 0.2, 1.9, color='k', alpha=1))
            node = 0
            periode = 4*longueur/(1 + 2*(nb_nodes-1))
        else:
            node = longueur/(2*nb_nodes)
            periode = 2*longueur/nb_nodes

        # Creation of each individual particle
        intervalle = longueur/(nb_particules_hor)
        k = 2*np.pi/periode
        balls = []
        for i in range(0, nb_particules_hor+1):
            x_eq = i*intervalle
            amplitude = 0.5*np.sin(k*(x_eq - node))
            balls.append(particle.Particule(x_eq, amplitude))

        return periode, num_frames, period, omega, balls, grilley, grillex, node


    def animationTempsReel(self, canvas, figure, slider, combo):
        """ Display the animation in real time """

        self.figure = figure

        [periode, num_frames, period, omega, balls, grilley, grillex, node] = self.initAnimation(slider, combo)

        # Displacement and pressure functions

        deplacement_pos = np.sin(2*np.pi/periode*(grillex - node))
        pressure_pos = np.cos(2*np.pi/periode*(grillex - node))

        # Plot maximum and minimum curves
        self.ax2.plot(grillex, deplacement_pos, 'b--')
        self.ax2.plot(grillex, -deplacement_pos, 'b--')
        self.ax3.plot(grillex, pressure_pos, 'r--')
        self.ax3.plot(grillex, -pressure_pos, 'r--')

        graph2, = self.ax2.plot(grillex, 0*deplacement_pos, color='k')
        graph3, = self.ax3.plot(grillex, 0*pressure_pos, color='k')

        tempss = np.linspace(0, period-period/num_frames, num_frames)
        self.frames_particles = []

        def update(i):
            for frame in self.frames_particles:
                frame.remove()
            self.frames_particles = []
            temps = tempss[i]
            x = np.sin(omega*temps)
            deplacement = np.sin(omega*temps)*deplacement_pos
            pressure = -np.sin(omega*temps)*pressure_pos
            graph2.set_ydata(deplacement)
            graph3.set_ydata(pressure)
            for ball in balls:
                position = ball.update_position(x)
                for y in grilley:
                    self.frames_particles.append(self.ax1.scatter(position, y, s=150, color='k'))

        self.oscillation = anim.FuncAnimation(self.figure, update, frames=num_frames, repeat=True, interval=40)
        canvas.draw()
