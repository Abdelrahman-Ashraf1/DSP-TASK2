# self.set_slider_ranges()
#         self.pushButton_3.clicked.connect(self.read_slider_ranges)
#
#         # Signal Composer
#
#     def set_slider_ranges(self):
#         self.phaseslider.setMinimum(0)
#         self.phaseslider.setMaximum(360)
#
#         self.magslider.setMinimum(0)
#         self.magslider.setMaximum(20)
#
#         self.freqslider.setMinimum(0)
#         self.freqslider.setMaximum(20)
#
#         self.rangeslider.setMinimum(0)
#         self.rangeslider.setMaximum(20)
#
#     def read_slider_ranges(self):
#         print(self.phaseslider.value())
#         print(self.freqslider.value())
#         print(self.rangeslider.value())
#         print(self.magslider.value())
#
#
# self.figure_1 = Figure()
# self.figure_canvas_1 = FigureCanvas(self.figure_1)
# self.verticalLayout.addWidget(self.figure_canvas_1)
# self.draw()
#
#
# def draw(self):
#     ax = self.figure_1.gca()
#     ax.grid(True)
#     ax.set_facecolor((1, 1, 1))