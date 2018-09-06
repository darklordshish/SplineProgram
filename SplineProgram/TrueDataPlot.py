# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrueDataPlot.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np


class TrueDataPlot(PlotWidget):
    """
    """
    def __init__(self,):
        """
        """
        super().__init__()
        self.x = np.linspace(0, 10, 100)
        self.y = np.ones(100)
        self.setBackground('w')

        self.scatter_data_plot = pg.PlotDataItem(self.x, self.y)
        self.scatter_data_plot.setSymbol('star')
        self.brush = pg.mkBrush(0, 0, 50, 10)
        self.data_range = pg.LinearRegionItem([np.median(self.x)*0.4,
                                               np.median(self.x)*1.4],
                                              brush = self.brush)

        self.addItem(self.scatter_data_plot)
        self.addItem(self.data_range)
        self.Plotting()

    def RegionInd(self,):
        """
        data get from the current region
        """
        "index of low bound"
        self.il = (np.abs(self.x - self.data_range.getRegion()[0])).argmin()
        "index of higher bound"
        self.ih = (np.abs(self.x - self.data_range.getRegion()[1])).argmin()
        return self.il, self.ih

    def Plotting(self):
        """
        Now, We try to make arrays for ploting our splines,
        and after this We set the arrays in PlotCurveItemes
        """
        self.scatter_data_plot.setData(self.x, self.y)

    def ChangeData(self, x, y):
        """
        """
        try:
            if len(x) == len(y):
                self.x = x
                self.y = y
                self.Plotting()
            else:
                raise ValueError("data must be the same size")
        except (ValueError, TypeError):
            print("bad data. give me different, good data")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TrueDataPlot()
    window.show()
    sys.exit(app.exec_())
