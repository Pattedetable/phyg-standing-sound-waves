import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from onde_stationnaire_main_window import Ui_Onde_Sonore_Stat
from dialog import Ui_Dialog


""" Initialize windows """
app = QApplication(sys.argv)
window_Onde = QMainWindow()
dialog = QDialog()

ui_Onde_Sonore_Stat = Ui_Onde_Sonore_Stat()
ui_Dial = Ui_Dialog()

ui_Dial.setupUi(dialog)
ui_Onde_Sonore_Stat.setupUi(window_Onde, dialog)

""" Make main window appear """
window_Onde.show()
sys.exit(app.exec_())
