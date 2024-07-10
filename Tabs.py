# -------------------------------------------------------------------------------
# Name:             Tabs.py
# Purpose:          Simple example of Tab Widgets
#
# Author:           Jeffreaux
#
# Created:          10July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QAction,
    QLineEdit,
    QTabBar,
    QLabel,
    QTabWidget,
)
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Tabs_GUI.ui", self)

        # define Widgets ##########################################################################
        self.btnExit = self.findChild(QPushButton, "btnExit")

        self.txtInputName = self.findChild(QLineEdit, "txtInputName")

        self.lblName = self.findChild(QLabel, "lblName")

        self.actExit = self.findChild(QAction, "actExit")

        self.tabWidget = self.findChild(QTabWidget, "tabWidget")

        # Define the actions#######################################################################
        self.btnExit.clicked.connect(self.closeEvent)
        self.txtInputName.returnPressed.connect(self.update_name) # Runs function when Enter is pressed

        self.actExit.triggered.connect(self.closeEvent)

        # Show the app ############################################################################
        self.show()

    def update_name(self):
        # Takes input from the second tab and updates the name label on the first tab when
        # enter is pressed.
        self.lblName.setText(self.txtInputName.text())
        self.txtInputName.clear()  # Clears entry box
        self.tabWidget.setCurrentIndex(0)  # Changes to Home (index 0) Tab to display results

    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
