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


from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from onde_stationnaire_animation import Animation

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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # Exporter GIF
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 3)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget) # Type de tuyau
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
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

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget) # Numéro du mode
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 3, 0, 1, 3)

        self.canvas = FigureCanvas(self.figure) # Graphique
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)
        self.menubar.addAction(self.menu_aide.menuAction())

        # Initial parameters
        self.horizontalSlider.setValue(1)
        self.comboBox.setCurrentIndex(0)

        # Start animation
        self.anim = Animation()
        self.anim.animationTempsReel(self.canvas, self.figure, self.horizontalSlider.value(), self.comboBox.currentIndex())

        self.retranslateUi(MainWindow)
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.lcdNumber.display(self.horizontalSlider.value())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.anim.stopAnim())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.lcdNumber.display(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.anim.animationTempsReel(self.canvas, self.figure, self.horizontalSlider.value(), self.comboBox.currentIndex()))
        self.comboBox.currentIndexChanged['QString'].connect(lambda: self.anim.stopAnim())
        self.comboBox.currentIndexChanged['QString'].connect(lambda: self.anim.animationTempsReel(self.canvas, self.figure, self.horizontalSlider.value(), self.comboBox.currentIndex()))
        self.pushButton.clicked.connect(lambda: self.anim.stopAnim())
        self.pushButton.clicked.connect(lambda: self.anim.exporterAnimation(self.canvas, self.figure, self.horizontalSlider.value(), self.comboBox.currentIndex()))
        self.pushButton_2.clicked.connect(lambda: plt.close())
        self.pushButton_2.clicked.connect(lambda: self.fermerEtAfficher(MainWindow, parent))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Onde sonore stationnaire"))
        self.pushButton_2.setText(_translate("MainWindow", "Quitter"))
        self.pushButton.setText(_translate("MainWindow", "Exporter en vidéo (.mp4)"))
        self.label.setText(_translate("MainWindow", "Type de tuyau"))
        self.comboBox.setToolTip(_translate("MainWindow", "Cliquer pour sélectionner le tuyau"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tuyau ouvert"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuyau fermé"))
        self.lcdNumber.setToolTip(_translate("MainWindow", "Numéro du mode"))
        self.label_2.setText(_translate("MainWindow", "Numéro du mode"))
        self.horizontalSlider.setToolTip(_translate("MainWindow", "Glisser pour sélectionner le mode"))
        self.menu_aide.setTitle(_translate("MainWindow", "Aide"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
        self.pushButton.setDisabled(boolean)
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
