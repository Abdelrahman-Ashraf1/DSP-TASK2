from PyQt5 import QtWidgets , uic
from PyQt5.QtWidgets import *
from pyqtgraph import *
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pathlib
import numpy as np
from MainWindow import Ui_MainWindow

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('task2.ui', self)
        self.show()

    def set_slider_ranges(self):
        self.phaseslider.set
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()        