import numpy as np
from matplotlib.animation import ImageMagickWriter, ImageMagickFileWriter
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import time

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
        """ Create the file if it does not exist"""
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
    """ Important constants and parameters """
    [nb_nodes, tuyau_ferme] = readParams()

    nb_particules_hor = 30
    longueur = 20
    num_frames = 90
    period = 30
    omega = 2*np.pi/period
    grilley = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]


    """ Create and setup animation """
    oscillation = plt.figure()

    ax = plt.Axes(fig=oscillation, rect=[0.1, 0.1, 0.8, 0.8])
    ax.add_patch(Rectangle((-0.5, 0.85), 21, 0.1, color='k', alpha=1))
    ax.add_patch(Rectangle((-0.5, -0.95), 21, 0.1, color='k', alpha=1))
    ax.axis([-1, longueur + 1, -1, 1])
    ax1 = oscillation.add_axes(ax, autoscale_on=False)
    plt.axis('off')

    # Differences between open and closed pipes
    if tuyau_ferme:
        ax.add_patch(Rectangle((-1, -0.95), 0.5, 1.9, color='k', alpha=1))
        node = 0
        periode = 4*longueur/(1 + 2*nb_nodes)
    else:
        node = longueur/(2*nb_nodes)
        periode = 2*longueur/nb_nodes

    """ Creation of each individual particle """
    intervalle = longueur/(nb_particules_hor)
    k = 2*np.pi/periode
    balls = []
    for i in range(0, nb_particules_hor+1):
        x_eq = i*intervalle
        amplitude = 0.5*np.sin(k*(x_eq - node))
        balls.append(particle.Particule(x_eq, amplitude))


    return oscillation, ax1, periode, num_frames, period, omega, balls, grilley


def animationRealTime():
    """ Initialize animation parameters """
    [oscillation, ax1, periode, num_frames, period, omega, balls, grilley] = initAnimation()

    """ Create each frame of the animation """
    temps = 0
    while True:
        [nb_nodes, tuyau_ferme] = readParams()
        temps += period/num_frames
        x = np.sin(omega*temps)
        frames = []
        for ball in balls:
            position = ball.update_position(x)
            for y in grilley:
                frames.append(ax1.scatter(position, y, color='k'))
        oscillation.savefig("graphique.png")
#        ui.graphicsView.updateScene()

#                for frame in frames:
#                    frame.remove()
        time.sleep(1/(num_frames/3))


def animationGif(ui):

    ui.disableAll(True)

    """ Initialize animation parameters """
    print("Initialisation de l'animation...")
    ui.textBrowser.setText("Initialisation de l'animation...")
    [oscillation, ax1, periode, num_frames, period, omega, balls, grilley] = initAnimation()

#    animation = ImageMagickWriter(fps=num_frames/3) #Uses RAM
    animation = ImageMagickFileWriter(fps=num_frames/3) #Temporary files
    animation.setup(fig=oscillation, outfile="particules.gif", dpi=128)


    """ Create each frame of the animation """
    print("Création de l'animation...")
    ui.textBrowser.setText("Création de l'animation...")
    tempss = np.linspace(0, period, num_frames)
    for temps in tempss:
        x = np.sin(omega*temps)
        frames = []
        for ball in balls:
            position = ball.update_position(x)
            for y in grilley:
                frames.append(ax1.scatter(position, y, color='k'))
        animation.grab_frame()
        for frame in frames:
            frame.remove()
        ui.progressBar.setValue(temps/tempss[-1]*100)

    print("Finalisation de l'animation...")
    ui.textBrowser.setText("Finalisation de l'animation...")
    animation.finish()

    print("Animation terminée!\n")
    ui.textBrowser.setText("Animation terminée!")
    ui.progressBar.setValue(0)
    ui.disableAll(False)

    ui.afficherGif()

    #os.system("eog particules.gif") # For GNOME-based Linux systems
    #os.system("start particules.gif") # For Windows
