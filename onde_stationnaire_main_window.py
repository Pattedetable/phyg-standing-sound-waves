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
import onde_stationnaire_animation as onde


class Ui_Onde_Sonore_Stat(object):
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
        picture = QtGui.QPixmap("graphique_initial.png")
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

        self.horizontalSlider.setValue(onde.readParams()[0])
        self.comboBox.setCurrentIndex(onde.readParams()[1])
#        temps_reel = subprocess.Popen(["python", "animationRealTime.py"], )

        self.retranslateUi(MainWindow)
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.lcdNumber.display(self.horizontalSlider.value())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.lcdNumber.display(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: onde.writeParams(self.horizontalSlider.value(), self.comboBox.currentIndex()))
#        self.pushButton_2.clicked.connect(lambda: temps_reel.terminate())
        self.pushButton_2.clicked.connect(lambda: Dialog.close())
        self.pushButton_2.clicked.connect(lambda: MainWindow.close())
        self.pushButton.clicked.connect(lambda: onde.animationGif(self))
        self.comboBox.currentIndexChanged['QString'].connect(lambda: onde.writeParams(self.horizontalSlider.value(), self.comboBox.currentIndex()))
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

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
        self.comboBox.setDisabled(boolean)
        self.menu_aide.setDisabled(boolean)
