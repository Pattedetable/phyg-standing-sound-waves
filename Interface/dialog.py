# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pattedetable/Python/Projet/Interface/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(497, 168)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "À propos"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Auteur :</span> Manuel Barrette</p><p><span style=\" font-weight:600;\">Année :</span> 2017</p><p><span style=\" font-weight:600;\">Code source</span> disponible sur <a href=\"https://github.com/Pattedetable/onde-sonore-stationnaire\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p><p><span style=\" font-weight:600;\">Licence : </span><a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU GPLv3</span></a></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Fermer"))

