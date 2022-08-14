#
# Copyright 2017-2020 Manuel Barrette
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


from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as anim
import os, platform
import particle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, parent):

        self.figure = plt.figure()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # Quitter
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 3)

#        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # Exporter vidéo
#        self.pushButton.setObjectName("pushButton")
#        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 3)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget) # Type de tuyau
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 40))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget) # Numéro du mode
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 3, 0, 1, 3)

        self.canvas = FigureCanvas(self.figure) # Graphique
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 3, 9, 1)

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
        self.action_propos = QtGui.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)
        self.menubar.addAction(self.menu_aide.menuAction())

        # Initial parameters
        self.horizontalSlider.setValue(1)
        self.comboBox.setCurrentIndex(0)

#        # Operating system detection
#        self.systeme_exploitation = platform.system()
#        if self.systeme_exploitation == "Darwin":
#            self.pushButton.setDisabled(True)

        self.retranslateUi(MainWindow)

        # Start animation
        self.animationTempsReel()


        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.lcdNumber.display(self.horizontalSlider.value())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.lcdNumber.display(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.comboBox.currentIndexChanged['int'].connect(lambda: self.stopAnim())
        self.comboBox.currentIndexChanged['int'].connect(lambda: self.animationTempsReel())
#        self.pushButton.clicked.connect(lambda: self.stopAnim())
#        self.pushButton.clicked.connect(lambda: self.exporterAnimation())
        self.pushButton_2.clicked.connect(lambda: plt.close())
        self.pushButton_2.clicked.connect(lambda: self.fermerEtAfficher(MainWindow, parent))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Onde sonore stationnaire"))
        self.pushButton_2.setText(self._translate("MainWindow", "Quitter"))
#        self.pushButton.setText(self._translate("MainWindow", "Exporter en vidéo (.mp4)"))
        self.label.setText(self._translate("MainWindow", "Type de tuyau"))
        self.comboBox.setToolTip(self._translate("MainWindow", "Cliquer pour sélectionner le tuyau"))
        self.comboBox.setItemText(0, self._translate("MainWindow", "Tuyau ouvert"))
        self.comboBox.setItemText(1, self._translate("MainWindow", "Tuyau fermé"))
        self.lcdNumber.setToolTip(self._translate("MainWindow", "Numéro du mode"))
        self.label_2.setText(self._translate("MainWindow", "Numéro du mode"))
        self.horizontalSlider.setToolTip(self._translate("MainWindow", "Glisser pour sélectionner le mode"))
        self.menu_aide.setTitle(self._translate("MainWindow", "Aide"))
        self.action_propos.setText(self._translate("MainWindow", "À propos"))

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
#        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
#        self.pushButton_3.setDisabled(boolean)
        self.comboBox.setDisabled(boolean)
        self.menu_aide.setDisabled(boolean)
        self.label.setDisabled(boolean)
        self.label_2.setDisabled(boolean)
        self.lcdNumber.setDisabled(boolean)

    def fermerEtAfficher(self, MainWindow, window_autre):
#        if window_autre:
#            window_autre.show()
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()

    def stopAnim(self):
        self.oscillation.event_source.stop()

    def enregistrer(self):
        if self.systeme_exploitation == 'Windows':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOMEPATH'), 'Vidéos (*.mp4)')
        elif self.systeme_exploitation == 'Darwin' or 'Linux':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOME'), 'Vidéos (*.mp4)')
        else:
            print("Système non supporté officiellement.  Enregistrement dans le dossier de travail sous le nom 'animation.mp4'.")
            fichier = ['animation', None]
        return fichier[0]

    def exporterAnimation(self):
        nom_anim = self.enregistrer()
        if nom_anim[-4:] != ".mp4":
            nom_anim = nom_anim + ".mp4"
        self.oscillation.save(nom_anim)
        self.animationTempsReel()


    def initAnimation(self):
        """ Define parameters and setup the base graphic """

        self.figure.clear()

        # Important parameters
        nb_nodes = self.horizontalSlider.value()
        if self.comboBox.currentIndex() == 1:
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

        self.ax1.set_ylabel(self._translate("MainWindow", "Particules"))
        self.ax2.set_ylabel(self._translate("MainWindow", "Déplacement"))
        self.ax3.set_ylabel(self._translate("MainWindow", "Pression"))

#        self.ax1.yaxis.set_label_coords(-0.06, 0.5)
        self.ax1.yaxis.set_label_coords(-0.1, 0.5)
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


    def animationTempsReel(self):
        """ Display the animation in real time """

        [periode, num_frames, period, omega, balls, grilley, grillex, node] = self.initAnimation()

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
        self.canvas.draw()
