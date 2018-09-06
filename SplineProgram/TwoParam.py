# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TwoParam.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PlBelPlot import PlBelPlot
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget


class TwoParam(QWidget):
    """

    """
    def __init__(self,):
        super().__init__()
        self.setupUi()

    def setupUi(self,):
        self.setObjectName("TwoParam")
        self.resize(683, 555)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ParamPlot_1 = PlBelPlot(self)
        self.ParamPlot_1.setObjectName("Param1")
        self.gridLayout.addWidget(self.ParamPlot_1, 0, 0, 1, 1)

        self.ParamPlot_2 = PlBelPlot(self)
        self.ParamPlot_2.setObjectName("Param2")
        self.gridLayout.addWidget(self.ParamPlot_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        # self.retranslateUi(TwoParam)
        QtCore.QMetaObject.connectSlotsByName(self)

        """Slots and Signals"""
        self.ParamPlot_1.xLine.sigLineXPos[float].connect(
                            self.ParamPlot_2.changeXlinePosition)
        self.ParamPlot_2.xLine.sigLineXPos[float].connect(
                            self.ParamPlot_1.changeXlinePosition)

    """Methods"""
    def changeXmin(self, xmin):
        if xmin < self.ParamPlot_1.xMax:
            self.ParamPlot_1.xMin = xmin
            self.ParamPlot_2.xMin = xmin
            self.ParamPlot_1.plotInterpolation()
            self.ParamPlot_2.plotInterpolation()

    def changeXmax(self, xmax):
        if xmax > self.ParamPlot_1.xMin:
            self.ParamPlot_1.xMax = xmax
            self.ParamPlot_2.xMax = xmax
            self.ParamPlot_1.plotInterpolation()
            self.ParamPlot_2.plotInterpolation()

    def changeNum(self, num):
        if num >= 100 and num <= 10000:
            self.ParamPlot_1.num = num
            self.ParamPlot_2.num = num

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
    app = QtWidgets.QApplication(sys.argv)
    window = TwoParam()
    window.show()
    sys.exit(app.exec_())
