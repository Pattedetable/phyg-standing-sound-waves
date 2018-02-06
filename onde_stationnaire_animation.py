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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import subprocess

import particle


def readParams():
    """ Read parameters from a file """
    try:
        with open("params.dat") as file_object:
            lines = file_object.readlines()
            nb_nodes = int(lines[0].split()[1])
            bool_list = ['True', 'true']
            if lines[1].split()[1] in bool_list:
                tuyau_ferme = True
            else:
                tuyau_ferme = False
        return nb_nodes, tuyau_ferme
    except FileNotFoundError:
        # Create the file if it does not exist
        print("Création d'un nouveau fichier de paramètres...")
        writeParams(1, 0)
        return 1, False


def writeParams(nb_nodes, tuyau_ferme_num):
    """ Writes important parameters to a file """
    with open('params.dat', 'w') as file_object:
        file_object.write("nb_nodes " + str(nb_nodes) + "\n")
        if tuyau_ferme_num == 1:
            file_object.write("tuyau_ferme True")
        else:
            file_object.write("tuyau_ferme False")


def initAnimation():
    """ Define parameters and setup the base graphic """
    # Important parameters
    [nb_nodes, tuyau_ferme] = readParams()

    nb_particules_hor = 30
    longueur = 20
    num_frames = 45
    period = 30
    omega = 2*np.pi/period
    grilley = [-0.5, -0.25, 0, 0.25, 0.5]
#    grilley = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]

    grillex = np.linspace(0, longueur, 100)

    # Create and setup animation
#    oscillation = plt.figure()
#
#    ax = plt.Axes(fig=oscillation, rect=[0.1, 0.1, 0.8, 0.8])
#    ax.add_patch(Rectangle((-0.5, 0.85), 21, 0.1, color='k', alpha=1))
#    ax.add_patch(Rectangle((-0.5, -0.95), 21, 0.1, color='k', alpha=1))
#    ax.axis([-1, longueur + 1, -1, 1])
#    ax1 = oscillation.add_axes(ax, autoscale_on=False)
#    plt.axis('off')


    oscillation, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    ax1.add_patch(Rectangle((-0.5, 0.85), 21, 0.1, color='k', alpha=1))
    ax1.add_patch(Rectangle((-0.5, -0.95), 21, 0.1, color='k', alpha=1))
    ax1.axis([-1, longueur + 1, -1, 1])

    ax2.axis([-1, longueur + 1, -1, 1])
    ax3.axis([-1, longueur + 1, -1, 1])

    ax1.set_ylabel('Particules')
    ax2.set_ylabel('Déplacement')
    ax3.set_ylabel('Pression')

    ax1.yaxis.set_label_coords(-0.1, 0.5)
    ax2.yaxis.set_label_coords(-0.1, 0.5)
    ax3.yaxis.set_label_coords(-0.1, 0.5)

    ax1.set_yticks([])
    ax2.set_yticks([0])
    ax3.set_yticks([0])

    ax2.set_yticklabels([r"$0$"])
    ax3.set_yticklabels([r"$p_{atm}$"])

    ax2.grid(True)
    ax3.grid(True)

    ax3.set_xticks([])

    # Differences between open and closed pipes
    if tuyau_ferme:
        ax1.add_patch(Rectangle((-1, -0.95), 0.5, 1.9, color='k', alpha=1))
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

    return oscillation, ax1, ax2, ax3, periode, num_frames, period, omega, balls, grilley, grillex, node


def animationGif(ui):
    """ Create a GIF animation according to the specified parameters """

    ui.disableAll(True)

    # Initialize animation parameters
    print("Initialisation de l'animation...")
    ui.textBrowser.setText("Initialisation de l'animation...")
    [oscillation, ax1, ax2, ax3, periode, num_frames, period, omega, balls, grilley, grillex, node] = initAnimation()

    compteur = 9

    # Displacement and pressure functions

    deplacement_pos = np.sin(2*np.pi/periode*(grillex - node))
    pressure_pos = np.cos(2*np.pi/periode*(grillex - node))

    graph2, = ax2.plot(grillex, 0*deplacement_pos, color='k')
    graph3, = ax3.plot(grillex, 0*pressure_pos, color='k')

    # Create each frame of the animation
    print("Création de l'animation...")
    ui.textBrowser.setText("Création de l'animation...")
    tempss = np.linspace(0, period, num_frames)
    for temps in tempss:
        compteur += 1
        nom_fig = "_tmp" + str(compteur) + ".png"
        x = np.sin(omega*temps)
        frames_particles = []
        deplacement = np.sin(omega*temps)*deplacement_pos
        pressure = -np.sin(omega*temps)*pressure_pos
        graph2.set_ydata(deplacement)
        graph3.set_ydata(pressure)
        for ball in balls:
            position = ball.update_position(x)
            for y in grilley:
                frames_particles.append(ax1.scatter(position, y, color='k'))
        oscillation.savefig(nom_fig)
        ui.afficherGraphique(nom_fig)
        for frame in frames_particles:
            frame.remove()
        ui.progressBar.setValue(temps/tempss[-1]*100)

    print("Finalisation de l'animation...")
    ui.textBrowser.setText("Finalisation de l'animation...")
#    CREATE_NO_WINDOW = 0x08000000 # Compiled Windows version
#    subprocess.call('.\ImageMagick-7.0.7-22-portable-Q16-x64\convert.exe -delay 4 -loop 0 _tmp* particules.gif', creationflags=CREATE_NO_WINDOW) # Compiled Windows version
    os.system('convert -delay 4 -loop 0 _tmp* particules.gif') # With script
    files = os.listdir('.')
    for file in files:
        if file.startswith('_tmp'):
            os.remove(file)

    print("Animation terminée!\n")
    ui.textBrowser.setText("Animation terminée!")
    ui.progressBar.setValue(0)
    ui.disableAll(False)

    ui.afficherGif()
