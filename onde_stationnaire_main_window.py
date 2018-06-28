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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pattedetable/Python/Projet/Interface/Onde_stationnaire.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import onde_stationnaire_animation as onde

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import subprocess
import particle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 2)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 40))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 2, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 3)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 1, 1, 2)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 6, 1)
        picture = QtGui.QPixmap("graphique_initial.png") # Graphique
        self.label_3.setPixmap(picture)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 25))
        self.menubar.setObjectName("menubar")
        self.menu_aide = QtWidgets.QMenu(self.menubar)
        self.menu_aide.setObjectName("menu_aide")
        MainWindow.setMenuBar(self.menubar)
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)
        self.menubar.addAction(self.menu_aide.menuAction())

        self.horizontalSlider.setValue(self.readParams()[0])
        self.comboBox.setCurrentIndex(self.readParams()[1])
#        self.sentinelle = QFileSystemWatcher()
#        self.sentinelle.addPath("graphique.png")
#        temps_reel = Popen(["python", "animationRealTime.py"], ) # Temps réel

        self.retranslateUi(MainWindow)
#        self.sentinelle.fileChanged.connect(lambda: self.afficherGraphique())
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.lcdNumber.display(self.horizontalSlider.value())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.lcdNumber.display(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.writeParams(self.horizontalSlider.value(), self.comboBox.currentIndex()))
#        self.pushButton_2.clicked.connect(lambda: temps_reel.terminate()) # Temps réel
        self.pushButton_2.clicked.connect(lambda: Dialog.close())
        self.pushButton_2.clicked.connect(lambda: MainWindow.close())
        self.pushButton.clicked.connect(lambda: self.animationGif())
        self.comboBox.currentIndexChanged['QString'].connect(lambda: self.writeParams(self.horizontalSlider.value(), self.comboBox.currentIndex()))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Onde sonore stationnaire"))
        self.pushButton_2.setText(_translate("MainWindow", "Quitter"))
        self.pushButton.setText(_translate("MainWindow", "Générer GIF"))
        self.label.setText(_translate("MainWindow", "Type de tuyau"))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cliquer pour sélectionner le tuyau</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tuyau ouvert"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuyau fermé"))
        self.lcdNumber.setToolTip(_translate("MainWindow", "<html><head/><body><p>Numéro du mode</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Numéro du mode"))
        self.textBrowser.setToolTip(_translate("MainWindow", "<html><head/><body><p>Messages système</p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "En attente..."))
        self.horizontalSlider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Glisser pour sélectionner le mode</p></body></html>"))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Progression de la création de l\'animation</p></body></html>"))
        self.menu_aide.setTitle(_translate("MainWindow", "Aide"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))

    def afficherGif(self):
        movie = QtGui.QMovie("particules.gif")
        movie.setScaledSize(self.label_3.size())
        self.label_3.setMovie(movie)
        movie.start()

    def afficherGraphique(self, graphique):
        self.label_3.clear()
        self.label_3.setPixmap(QtGui.QPixmap(graphique))

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
        self.comboBox.setDisabled(boolean)
        self.menu_aide.setDisabled(boolean)

    def readParams(self):
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
            self.writeParams(1, 0)
            return 1, False


    def writeParams(self, nb_nodes, tuyau_ferme_num):
        """ Writes important parameters to a file """
        with open('params.dat', 'w') as file_object:
            file_object.write("nb_nodes " + str(nb_nodes) + "\n")
            if tuyau_ferme_num == 1:
                file_object.write("tuyau_ferme True")
            else:
                file_object.write("tuyau_ferme False")


    def initAnimation(self):
        """ Define parameters and setup the base graphic """
        # Important parameters
        [nb_nodes, tuyau_ferme] = self.readParams()

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


    def animationGif(self):
        """ Create a GIF animation according to the specified parameters """

        self.disableAll(True)

        # Initialize animation parameters
        print("Initialisation de l'animation...")
        self.textBrowser.setText("Initialisation de l'animation...")
        [oscillation, ax1, ax2, ax3, periode, num_frames, period, omega, balls, grilley, grillex, node] = self.initAnimation()

        compteur = 9

        # Displacement and pressure functions

        deplacement_pos = np.sin(2*np.pi/periode*(grillex - node))
        pressure_pos = np.cos(2*np.pi/periode*(grillex - node))

        # Plot maximum and minimum curves
        ax2.plot(grillex, deplacement_pos, 'b--')
        ax2.plot(grillex, -deplacement_pos, 'b--')
        ax3.plot(grillex, pressure_pos, 'r--')
        ax3.plot(grillex, -pressure_pos, 'r--')

        graph2, = ax2.plot(grillex, 0*deplacement_pos, color='k')
        graph3, = ax3.plot(grillex, 0*pressure_pos, color='k')

        # Create each frame of the animation
        print("Création de l'animation...")
        self.textBrowser.setText("Création de l'animation...")
        tempss = np.linspace(0, period-period/num_frames, num_frames)
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
            self.afficherGraphique(nom_fig)
            for frame in frames_particles:
                frame.remove()
            self.progressBar.setValue(temps/tempss[-1]*100)

        print("Finalisation de l'animation...")
        self.textBrowser.setText("Finalisation de l'animation...")
    #    CREATE_NO_WINDOW = 0x08000000 # Compiled Windows version
    #    subprocess.call('.\ImageMagick-7.0.7-22-portable-Q16-x64\convert.exe -delay 4 -loop 0 _tmp* particules.gif', creationflags=CREATE_NO_WINDOW) # Compiled Windows version
        os.system('convert -delay 4 -loop 0 _tmp* particules.gif') # With script
        files = os.listdir('.')
        for file in files:
            if file.startswith('_tmp'):
                os.remove(file)

        print("Animation terminée!\n")
        self.textBrowser.setText("Animation terminée!")
        self.progressBar.setValue(0)
        self.disableAll(False)

        self.afficherGif()

        plt.close()
