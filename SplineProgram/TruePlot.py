#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:58:20 2017

@author: semion
"""

import pyqtgraph as pg
from pyqtgraph import GraphicsLayoutWidget
import numpy as np
from scipy.interpolate import UnivariateSpline
from numpy.random import randn
from scipy.interpolate import dfitpack

try:
    dfitpack.sproot(-1, -1, -1)
except Exception as e:
    DFitPackError = type(e)


class TruePlot(GraphicsLayoutWidget):
    """
    The data and it's spline
    plotes and it's spline
    """

    def __init__(self, *args, **kwargs):
        super(TruePlot, self).__init__(*args, **kwargs)
        """
        default data
        """
        self.spline = np.ones_like
        self.err_spline = np.ones_like
        self.k = 3
        self.s = 10.3
        self.x = np.linspace(0, 200, 200)
        self.y = self.func_rand(self.func, self.x)
        self.setBackground('w')
        self.UpdateSplines()
        self.err_y = self.y - self.spline(self.x)

        self.brush = pg.mkBrush(0, 0, 50, 10)
        self.scatter_data_plot = pg.PlotDataItem()
        self.scatter_data_plot.setSymbol('star')

        self.spline_plot = pg.PlotCurveItem(pen=pg.mkPen('k'))

        self.data_range = pg.LinearRegionItem([np.median(self.x)*0.4,
                                               np.median(self.x)*1.4],
                                              brush=self.brush)

        self.data_plot = self.addPlot()
        self.data_plot.addItem(self.scatter_data_plot)
        self.data_plot.addItem(self.spline_plot)
        self.data_plot.addItem(self.data_range)

        self.nextRow()

        self.err_scatter_data_plot = pg.PlotDataItem()
        self.err_scatter_data_plot.setSymbol('star')

        self.err_spline_plot = pg.PlotCurveItem(pen=pg.mkPen('k'))

        self.err_data_range = pg.LinearRegionItem([np.median(self.x)*0.4,
                                                   np.median(self.x)*1.4],
                                                  brush=self.brush)

        self.err_data_plot = self.addPlot()
        self.err_data_plot.addItem(self.err_scatter_data_plot)
        self.err_data_plot.addItem(self.err_spline_plot)
        self.err_data_plot.addItem(self.err_data_range)

        self.Plotting()

        "Signals and Slots"
        self.data_range.sigRegionChanged.connect(self.ChangeDataRegion)
        self.err_data_range.sigRegionChanged.connect(self.ChangeErrRegion)

    def func(self, x):
        """
        модельная функция
        """
        y = 0.79*(np.sin(2*np.pi/24*x) +
                np.exp(-(x - 70)**2/100) +
                np.exp(-(x - 130)**2/130) +
                0.5*np.sin(np.heaviside(x-96, 76)*2*np.pi/27.4*x) +
                np.exp(-(np.heaviside(x-57,1)*x - 200)**2/200)*np.sin(0.01*x)+
                0.01*np.heaviside(157-x, 1)*np.sin(2*np.pi*x/365)) + 20
        return y

    def func_rand(self, func, x):
        """
        модель измерения с шумом
        """
        y = func(x) + np.random.randn(np.size(x))*0.20
        return y

    def UpdateSplines(self,):
        """
        We use UnivariateSpline from scipy for making our spline's model
        """
        distribution_spl = False
        try:
            if self.k in range(1, 6):
                distribution_spl = UnivariateSpline(x=self.x, y=self.y,
                                                    k=self.k, s=self.s)
                distribution_spl_err = UnivariateSpline(
                        x=self.x, y=self.y-distribution_spl(self.x),
                        k=self.k, s=self.s)
            elif self.k > 5:
                raise ValueError("The value of k is too large")
            else:
                raise ValueError("WTF?")
        except (ValueError, TypeError, DFitPackError):
            print("Can't update splines, they have not changed")
        if (distribution_spl):
            self.spline = distribution_spl
            self.err_spline = distribution_spl_err

    def Plotting(self):
        """
        Now, We try to make arrays for ploting our splines,
        and after this We set the arrays in PlotCurveItemes
        """
        self.plot = False
        try:
            self.x_plot = np.linspace(np.min(self.x),
                                      np.max(self.x),
                                      np.size(self.x)*100)
            # self.y_plot = self.spline(self.x_plot)
            self.y_plot = self.func(self.x_plot)
            self.err_y_plot = self.err_spline(self.x_plot)
            self.plot = True
        except (ValueError, TypeError):
            print("can't make data for plotting splines")
        if self.plot:
            self.err_y = self.y - self.func(self.x)
            self.scatter_data_plot.setData(self.x, self.y)
            self.spline_plot.setData(self.x_plot, self.y_plot)
            self.err_scatter_data_plot.setData(self.x, self.err_y)
            self.err_spline_plot.setData(self.x_plot, self.err_y_plot)

    def RegionInd(self,):
        """
        data get from the current region
        """
        "index of low bound"
        self.il = (np.abs(self.x - self.data_range.getRegion()[0])).argmin()
        "index of higher bound"
        self.ih = (np.abs(self.x - self.data_range.getRegion()[1])).argmin()
        return self.il, self.ih

    def ChangeDataRegion(self,):
        """
        """
        self.err_data_range.setRegion(self.data_range.getRegion())

    def ChangeErrRegion(self,):
        """
        """
        self.data_range.setRegion(self.err_data_range.getRegion())

    def ChangeS(self, s):
        """
        It changes smooth factor
        """
        try:
            if s >= 0:
                self.s = s
                self.UpdateSplines()
                self.err_y = self.y - self.spline(self.x)
                self.Plotting()
            else:
                raise ValueError('smouth factor should be positive ')
        except Exception:
            print('Some exception in method ChangeS')

    def ChangeK(self, k):
        """
        It changes spline's degre
        """
        k = round(k)
        try:
            if k in range(1, 6):
                self.k = k
                self.UpdateSplines()
                self.err_y = self.y - self.spline(self.x)
                self.Plotting()
            else:
                raise ValueError("WTF? Spline's degree should be less then 6")
        except Exception:
            print('Some exception in method ChangeK')

    def ChangeData(self, x, y):
        """
        """
        try:
            if len(x) == len(y):
                self.x = x
                self.y = y
                self.UpdateSplines()
                self.err_y = self.y - self.spline(self.x)
                self.Plotting()
            else:
                raise ValueError("data must be the same size")
        except (ValueError, TypeError, DFitPackError):
            print("bad data. give me different, good data")


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    app = QtGui.QApplication(sys.argv)
    a = TruePlot()
    a.show()
    sys.exit(app.exec_())
