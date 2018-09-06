# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:51:40 2016

@author: semion
"""
from PyQt5 import QtCore, QtGui, Qt
import pyqtgraph as pg

import numpy as np
from scipy.interpolate import UnivariateSpline
from numpy.random import rand
from scipy.interpolate import dfitpack

try:
    dfitpack.sproot(-1, -1, -1)
except Exception as e:
    DFitPackError = type(e)


class ViewBox(pg.ViewBox):
    """
    ViewBox, настроенная для удаления точек при щелчках около них и показа
          меню в противном случае.
    """
    def __init__(self, parent_plot_widget, *args, **kwargs):
        self.parent_plot_widget = parent_plot_widget
        super().__init__(*args, **kwargs)

    def raiseContextMenu(self, event):
        if self.parent_plot_widget.removePoint(event):
            return
        # Если не было выхода из метода из-за отсутствия подходящей
        # точки — показ меню.
        if not self.menuEnabled():
            return
        menu = self.getMenu(event)
        pos = event.screenPos()
        menu.popup(QtCore.QPoint(pos.x(), pos.y()))


class PlBelPlot(pg.PlotWidget):
    def __init__(self, *args, **kwargs):
        super(PlBelPlot, self).__init__(
                    *args, viewBox=ViewBox(parent_plot_widget=self), **kwargs)
        self.distribution = lambda x: np.ones_like(x)

        self.points_x = np.array([])
        self.points_t = np.array([])

        self.distributionPlPlot = pg.PlotCurveItem()
        self.distributionPlPlot.setPen((0, 3))
        self.addItem(self.distributionPlPlot)

        self.distributionBelPlot = pg.PlotCurveItem()
        self.pen = pg.mkPen(color='b')
        self.distributionBelPlot.setPen(self.pen)
        self.addItem(self.distributionBelPlot)

        self.pointsPlot = pg.ScatterPlotItem()
        self.pointsPlot.setSymbol('+')
        self.addItem(self.pointsPlot)
        self.pointsPlot.setData(self.points_x, self.points_t)

        self.setYRange(-0.2, 1.2, padding=0.01)

        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.addItem(self.vLine, ignoreBounds=True)
        self.addItem(self.hLine, ignoreBounds=True)

        self.positionLabel = pg.TextItem(anchor=(1, 0))
        self.addItem(self.positionLabel)
        self.positionLabel.hide()

        self.scene().sigMouseClicked.connect(self.addPoint)
        self.scene().sigMouseMoved.connect(self.moveCrosshair)

        self.k = 1
        self.s = 0
        self.alpha = 1
        self.ResPlot = False
        # это флаг, определяющий, объект ли это для задания
        # распределения правдоподобия и доверия нечёткого
        # параметра, или же это объект, рисующий распределение
        # правдоподобия и доверия следствия
        self.xMin = -0.01  # -2*np.pi
        self.xMax = 8.01  # 2*np.pi
        self.num = 400

        self.pl_grid = np.array([])
        self.bel_grid = np.array([])
        self.plotInterpolation()

    def theta(self, x):  # функция тета, для примера такая
        return (1-x**self.alpha)**(1.0/self.alpha)

    def SetX(self, x):
        self.points_x = x

    def SetT(self, y):
        self.points_t = y

    def addPoint(self, event):
        if not self.ResPlot:
            if event.button() == Qt.Qt.LeftButton:
                pos = self.plotItem.vb.mapToView(event.pos())
                new_x = pos.x()
                new_t = pos.y()
                if (new_x >= self.xMin and
                        new_x <= self.xMax and
                        new_t >= -10 and
                        new_t <= 10):
                    pos = np.searchsorted(self.points_x, new_x)
                    self.addPointPlot(pos, new_x, new_t)
                    event.accept()

    def addPointPlot(self, pos, x, y):
        if y >= -0.1 and y <= 1.1:
            self.points_x = np.insert(self.points_x, pos, x)
            self.points_t = np.insert(self.points_t, pos, y)
            self.pointsPlot.setData(self.points_x, self.points_t)
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()

    def removePoint(self, event):
        if event.button() == Qt.Qt.RightButton:
            pos = self.plotItem.vb.mapToView(event.pos())
            eps_x = pos.x()
            eps_t = pos.y()
            rad = (self.points_x-eps_x)**2+(self.points_t-eps_t)**2
            if rad.size > 0:
                index = np.argmin(rad)
                if rad[index] < (np.fabs(self.xMin-self.xMax))/200:
                    self.removePointPlot(index)
                    event.accept()
                    return True
        return False

    def removePointPlot(self, index):
        self.points_x = np.delete(self.points_x, index)
        self.points_t = np.delete(self.points_t, index)
        self.pointsPlot.setData(self.points_x, self.points_t)
        self.recalcInterpolation(self.k, self.s)
        self.plotInterpolation()

    def moveCrosshair(self, event):
        mousePoint = self.plotItem.vb.mapSceneToView(event)
        self.vLine.setPos(mousePoint.x())
        self.hLine.setPos(mousePoint.y())
        cur_x = mousePoint.x()
        cur_t = mousePoint.y()
        if (cur_x >= self.xMin and
                cur_x <= self.xMax and
                cur_t >= 10 and cur_t <= -10):
            self.positionLabel.setPos(cur_x, cur_t)
            self.positionLabel.setText(
                "x = {:-.3g}\nt = {:-.3g}\nt(x) = {:-.3g}".format(
                    cur_x, cur_t, float(self.distribution(cur_x))), color='k')
            self.positionLabel.show()

    def recalcInterpolation(self, k1, s1):  # изменение cплайна
        distribution_spl = False
        try:
            if k1 > 5:
                raise NotImplementedError(
                                "Поддерживаются сплайны не выше 5 порядка")
            elif k1 in range(1, 6):
                distribution_spl = UnivariateSpline(self.points_x,
                                                    self.points_t, k=k1, s=s1)
            else:
                raise ValueError("Сплайн какого-какого порядка?")
        except (ValueError, TypeError, DFitPackError):
            self.distribution = np.ones_like
        if (distribution_spl):  # распределение правдоподобия, строится
                                # сплайном, ограниченным отрезком [0,1]
            self.distribution = lambda x: np.clip(distribution_spl(x), 0., 1.)

    def plotInterpolation(self):
        if not self.ResPlot:
            x_grid = np.linspace(self.xMin, self.xMax, self.num)
            # сетка по значениям параметра
            t_grid = self.distribution(x_grid)  # распределение правдоподобия
            self.distributionPlPlot.setData(x_grid, t_grid)  # добавим
            self.distributionBelPlot.setData(x_grid, self.theta(t_grid))
            # распределение доверия, согласованное с правдоподобием,
            # полученное с помощью функции тета
        else:
            x_grid = np.linspace(self.xMin, self.xMax, self.num)
            self.distributionPlPlot.setData(x_grid, self.pl_grid)
            self.distributionBelPlot.setData(x_grid, self.bel_grid)

    def changeS(self, s1):
        if s1 > 0.0 and s1 < 1.0:
            self.s = s1
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()

    def changeK(self, k1):
        if k1 > 0.0 and k1 < 6:
            self.k = k1
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()
            self.emit(QtCore.SIGNAL('change()'))

    def changeXmin(self, xmin):
        if xmin < self.xMax:
            self.xMin = xmin
            self.plotInterpolation()
            self.emit(QtCore.SIGNAL('change()'))

    def changeXmax(self, xmax):
        if xmax > self.xMin:
            self.xMax = xmax
            self.plotInterpolation()
            self.emit(QtCore.SIGNAL('change()'))

    def changeNum(self, num):
        if num >= 100 and num <= 5000:
            self.num = num

    @property
    def xMin(self):
        return self.plotItem.viewRange()[0][0]

    @xMin.setter
    def xMin(self, x_lower):
        self.setXRange(x_lower, self.xMax, padding=0.01)

    @property
    def xMax(self):
        return self.plotItem.viewRange()[0][1]

    @xMax.setter
    def xMax(self, x_upper):
        self.setXRange(self.xMin, x_upper, padding=0.01)
