# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:51:40 2016

@author: semion
"""
from PyQt5 import QtCore, Qt, QtWidgets
import pyqtgraph as pg
from pyqtgraph import ViewBox
from pyqtgraph import InfiniteLine
from pyqtgraph import PlotWidget
import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import dfitpack


try:
    dfitpack.sproot(-1, -1, -1)
except Exception as e:
    DFitPackError = type(e)


class myViewBox(ViewBox):
    """
    ViewBox, настроенная для удаления точек при щелчках около них и показа
          меню в противном случае.
    """
    def __init__(self, parent_plot_widget, *args, **kwargs):
        self.parent_plot_widget = parent_plot_widget
        super(myViewBox, self).__init__(*args, **kwargs)

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


class infiniteLine(InfiniteLine):
    """
    InfinitLine настроенный для излучения
     сигнала о смене позиции при перемещении
    """
    sigLineXPos = QtCore.pyqtSignal(float, name="lineXPos")

    def __init__(self, *args, **kwargs):
        super(infiniteLine, self).__init__(*args, **kwargs)
        self.sigPositionChangeFinished.connect(self.getLineXPos)
        self.sigDragged.connect(self.getLineXPos)

    def getLineXPos(self):
        xPos = self.getXPos()
        self.sigLineXPos.emit(xPos)


class PlBelPlot(PlotWidget):
    """
    """
    sigChangePoints = QtCore.pyqtSignal(list,
                                        name="oldPoints")
    sigChangeDistribution = QtCore.pyqtSignal(
                                        name="updeteDistribution")

    def __init__(self, *args, **kwargs):
        super(PlBelPlot, self).__init__(
                 *args, viewBox=myViewBox(parent_plot_widget=self), **kwargs)
        self.distribution = lambda x: np.ones_like(x)

        self.points_x = np.array([])
        self.points_t = np.array([])
        self.addLegend()
        self.distributionPlPlot = pg.PlotCurveItem(name="Plausibility")
        self.distributionPlPlot.setPen((0, 3))
        self.addItem(self.distributionPlPlot)

        self.distributionBelPlot = pg.PlotCurveItem(name="Belief")
        self.pen = pg.mkPen(color='b')
        self.distributionBelPlot.setPen(self.pen)
        self.addItem(self.distributionBelPlot)

        self.pointsPlot = pg.ScatterPlotItem()
        self.pointsPlot.setSymbol('+')
        self.addItem(self.pointsPlot)
        self.pointsPlot.setData(self.points_x, self.points_t)

        self.pointsErrPlot = pg.ErrorBarItem(x=self.points_x,
                                             y=self.points_t,
                                             beam=0.1)
        self.addItem(self.pointsErrPlot)

        self.setYRange(-0.2, 1.2, padding=0.01)
        self.xLine = infiniteLine(angle=90, movable=True, pen=pg.mkPen('c'))
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.addItem(self.xLine)
        self.addItem(self.vLine, ignoreBounds=True)
        self.addItem(self.hLine, ignoreBounds=True)

        self.positionLabel = pg.TextItem(anchor=(0, 1))
        self.addItem(self.positionLabel)

        self.scene().sigMouseClicked.connect(self.addPoint)
        self.scene().sigMouseMoved.connect(self.moveCrosshair)
        self.setBackground('w')
        self.k = 1
        self.s = 0
        self.alpha = 1.5
        self.Discrete = False
        self.ResPlot = False
        # это флаг, определяющий, объект ли это для задания
        # распределения правдоподобия и доверия нечёткого
        # параметра, или же это объект, рисующий распределение
        # правдоподобия и доверия следствия
        self.xMin = 10.01  # -2*np.pi
        self.xMax = 12  # 2*np.pi
        self.num = 400

        self.pl_grid = np.ones(self.num)
        self.bel_grid = np.zeros(self.num)
        self.plotInterpolation()

    def theta(self, x):
        """
        функция тета, для примера такая
        """
        return (1-x**self.alpha)**(1.0/self.alpha)

    def SetX(self, x):
        self.points_x = x

    def SetT(self, y):
        self.points_t = y

    def addPoint(self, event):
        if not self.ResPlot:
            if event.button() == Qt.Qt.LeftButton:
                pos = self.plotItem.vb.mapToView(event.pos())
                if self.Discrete:
                    new_x = round(pos.x())
                else:
                    new_x = pos.x()
                new_t = pos.y()
                if (new_x >= self.xMin and
                        new_x <= self.xMax and
                        new_t >= -2 and
                        new_t <= 2):
                    pos = np.searchsorted(self.points_x, new_x)
                    self.addPointPlot(pos, new_x, new_t)
                    event.accept()

    def addPointPlot(self, pos, x, y):
        if y >= -0.1 and y <= 1.1 and x >= -0.5:
            self.points_x = np.insert(self.points_x, pos, x)
            self.points_t = np.insert(self.points_t, pos, y)
            self.pointsPlot.setData(self.points_x, self.points_t)
            self.pointsErrPlot.setData(x=self.points_x, y=self.points_t,
                                       height=0.1*np.ones(
                                                    np.size(self.points_x)))

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
        self.pointsErrPlot.setData(x=self.points_x, y=self.points_t,
                                   height=0.1*np.ones(np.size(self.points_x)))
        self.recalcInterpolation(self.k, self.s)
        self.plotInterpolation()

    def moveCrosshair(self, event):
        mousePoint = self.plotItem.vb.mapSceneToView(event)
        cur_x = mousePoint.x()
        cur_t = mousePoint.y()
        self.positionLabel.setPos(cur_x, cur_t)
        self.positionLabel.setText("x=%f,   y=%f "
                                   % (cur_x, cur_t))
        self.vLine.setPos(mousePoint.x())
        self.hLine.setPos(mousePoint.y())
        if (cur_x >= self.xMin and
                cur_x <= self.xMax and
                cur_t >= 10 and
                cur_t <= -10):
            self.positionLabel.setPos(cur_x, cur_t)
            self.positionLabel.setText(
                "x = {:-.3g}\nt = {:-.3g}\nt(x) = {:-.3g}".format(
                    cur_x, cur_t, float(self.distribution(cur_x))), color='k')
            self.positionLabel.show()

    def changeXlinePosition(self, x_value):
        try:
            if (x_value >= self.xMin and
                    x_value <= self.xMax):
                self.xLine.setPos(x_value)
            else:
                    raise ValueError("value gets out of borders ")
        except ValueError:
            print("set different value")

    def recalcInterpolation(self, k1=1, s1=0):  # изменение cплайна
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
            self.sigChangeDistribution.emit()
        if (distribution_spl):  # распределение правдоподобия, строится
                                # сплайном, ограниченным отрезком [0,1]
            self.distribution = lambda x: np.clip(distribution_spl(x), 0., 1.)
            self.sigChangeDistribution.emit()

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

    def changeScatterPlotData(self, new_x_t):
        try:
            old_data = [self.points_x, self.points_t]
            self.sigChangePoints.emit(old_data)
            self.points_x = new_x_t[0]
            self.points_t = new_x_t[1]
            self.pointsPlot.setData(self.points_x, self.points_t)
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()
        except IndexError:
            print("index erro. Can't change distribution of Pl and Bel")

    def changeS(self, s1):
        if s1 > 0.0 and s1 <= 1.0:
            self.s = s1
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()

    def changeK(self, k1):
        if k1 > 0.0 and k1 < 6:
            self.k = k1
            self.recalcInterpolation(self.k, self.s)
            self.plotInterpolation()

    def changeXmin(self, xmin):
        if xmin < self.xMax:
            self.xMin = xmin
            self.plotInterpolation()

    def changeXmax(self, xmax):
        if xmax > self.xMin:
            self.xMax = xmax
            self.plotInterpolation()

    def changeNum(self, num):
        if num >= 100 and num <= 10000:
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


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PlBelPlot()
    window.show()
    sys.exit(app.exec_())
