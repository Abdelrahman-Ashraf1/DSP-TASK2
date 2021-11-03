from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pathlib
import numpy as np
from matplotlib.figure import Figure
import statistics
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.figure import Figure
from PyPDF2 import PdfFileMerger, PdfFileReader
import pdfkit
from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    added_signals_list = []

        # Signal Composer
        #############################################
        self.sine_wave_figure = Figure()
        self.sine_wave_canvas = FigureCanvas(self.sine_wave_figure)
        self.ui.BasisFunctionLayout.addWidget(self.sine_wave_canvas)
        empty_list = []
        self.sinusoidal_wave_summation = np.empty(empty_list)
        self.set_slider_ranges()
        # Sliders Moved:
        self.ui.phaseslider.valueChanged.connect(self.draw_sine_wave)
        self.ui.freqslider.valueChanged.connect(self.draw_sine_wave)
        self.ui.magslider.valueChanged.connect(self.draw_sine_wave)
        self.ui.rangeslider.valueChanged.connect(self.draw_sine_wave)
        # Buttons:
        self.ui.ShowButton.clicked.connect(self.show_initialized_graph)
        self.ui.AddButton.clicked.connect(self.add_signal_plot)
        #############################################
        # Signal Composer

        ############################################################
        # Main Window
        self.original_signal = Figure()
        self.original_signal_canvas = FigureCanvas(self.original_signal)
        self.ui.verticalLayout.addWidget(self.original_signal_canvas)

        self.reconstructed_signal = Figure()
        self.reconstructed_signal_canvas = FigureCanvas(self.reconstructed_signal)
        self.ui.verticalLayout_2.addWidget(self.reconstructed_signal_canvas)



        # Main Window
        ############################################################


    #############################################
    # Signal Composer

    def set_slider_ranges(self):
        self.ui.phaseslider.setMinimum(0)
        self.ui.phaseslider.setMaximum(360)

        self.ui.magslider.setMinimum(2)
        self.ui.magslider.setMaximum(20)

        self.ui.freqslider.setMinimum(1)
        self.ui.freqslider.setMaximum(30)

        self.ui.rangeslider.setMinimum(1)
        self.ui.rangeslider.setMaximum(4000)

    def read_slider_values(self):
        self.phase = self.ui.phaseslider.value()
        self.magnitude = self.ui.magslider.value()
        self.frequency = self.ui.freqslider.value()
        self.range = self.ui.rangeslider.value()
        # print(f"{self.phase} {self.magnitude} {self.frequency} {self.range}")

    def draw_sine_wave(self):
        self.read_slider_values()
        time_range = np.arange(0, self.range, 0.2)
        self.sine_wave = self.magnitude * np.sin((2 * np.pi * self.frequency * time_range / 4000) + ((np.pi / 180) * self.phase))
        axes = self.sine_wave_figure.gca()
        #self.sine_wave_figure.set_facecolor((1, 0.6, 0.5))
        axes.cla()
        axes.grid(True)
        axes.set_facecolor((1, 1, 1))
        axes.plot(time_range, self.sine_wave)
        self.sine_wave_canvas.draw()
        self.sine_wave_canvas.flush_events()
        return self.sine_wave

    def show_initialized_graph(self):
        axes = self.sine_wave_figure.gca()
        axes.cla()
        axes.grid(True)
        axes.set_facecolor((1, 1, 1))
        self.sine_wave_canvas.draw()
        self.sine_wave_canvas.flush_events()

    def add_signal_plot(self):
        #self.sinusoidal_wave_summation += self.draw_sine_wave()
        self.ui.comboBox.addItem(f"sine wave: {self.magnitude}Amp,{self.frequency}HZ,and {self.phase}˚ phase")


    ############################################################
    # Signal Composer

    ############################################################
    # Main Window


    # Main Window
    ############################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


