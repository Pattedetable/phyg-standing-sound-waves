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

""" Initialize windows and make the main window appear """
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import onde_stationnaire_main_window
import dialog_onde


# Initialize windows
app = QApplication(sys.argv)
window_Onde = QMainWindow()
dialog = QDialog()

ui_Onde_Sonore_Stat = onde_stationnaire_main_window.Ui_MainWindow()
ui_Dial = dialog_onde.Ui_Dialog()

ui_Dial.setupUi(dialog)
ui_Onde_Sonore_Stat.setupUi(window_Onde, dialog)

# Make main window appear
window_Onde.show()
sys.exit(app.exec_())
