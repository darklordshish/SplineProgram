# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowParametr.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_WindiwParametrPlot(QWidget):
    """
    """
    def __init__(self,):
        super().__init__()
        self.setupUi()

    def setupUi(self, ):
        """
        """
        self.setObjectName("WindiwParametrPlot")

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MainGrid = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(
                                           QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(
                             self.MainGrid.sizePolicy().hasHeightForWidth())
        self.MainGrid.setSizePolicy(sizePolicy)
        self.MainGrid.setSizeIncrement(QtCore.QSize(0, 0))
        self.MainGrid.setObjectName("MainGrid")
        self.gridLayout = QtWidgets.QGridLayout(self.MainGrid)
        self.gridLayout.setSizeConstraint(
                                      QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.MinBox = QtWidgets.QDoubleSpinBox(self.MainGrid)
        self.MinBox.setObjectName("MinBox")
        self.gridLayout.addWidget(self.MinBox, 3, 0, 1, 1)
        self.LabelValue = QtWidgets.QLabel(self.MainGrid)
        self.LabelValue.setObjectName("LabelValue")
        self.gridLayout.addWidget(self.LabelValue, 2, 4, 1, 1)
        self.LabelMax = QtWidgets.QLabel(self.MainGrid)
        self.LabelMax.setObjectName("LabelMax")
        self.gridLayout.addWidget(self.LabelMax, 2, 1, 1, 1)
        self.MaxBox = QtWidgets.QDoubleSpinBox(self.MainGrid)
        self.MaxBox.setProperty("value", 1.0)
        self.MaxBox.setObjectName("MaxBox")
        self.gridLayout.addWidget(self.MaxBox, 3, 1, 1, 1)
        self.ValueBox = QtWidgets.QDoubleSpinBox(self.MainGrid)
        self.ValueBox.setObjectName("ValueBox")
        self.gridLayout.addWidget(self.ValueBox, 3, 4, 1, 1)
        self.BelPlot = QtWidgets.QOpenGLWidget(self.MainGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(
                              self.BelPlot.sizePolicy().hasHeightForWidth())
        self.BelPlot.setSizePolicy(sizePolicy)
        self.BelPlot.setObjectName("BelPlot")
        self.gridLayout.addWidget(self.BelPlot, 0, 3, 1, 2)
        self.AlphaBox = QtWidgets.QDoubleSpinBox(self.MainGrid)
        self.AlphaBox.setMaximum(1.0)
        self.AlphaBox.setSingleStep(0.001)
        self.AlphaBox.setProperty("value", 0.5)
        self.AlphaBox.setObjectName("AlphaBox")
        self.gridLayout.addWidget(self.AlphaBox, 3, 3, 1, 1)
        self.PlPlot = QtWidgets.QOpenGLWidget(self.MainGrid)
        sizePolicy = QtWidgets.QSizePolicy(
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(
                                self.PlPlot.sizePolicy().hasHeightForWidth())
        self.PlPlot.setSizePolicy(sizePolicy)
        self.PlPlot.setMinimumSize(QtCore.QSize(0, 0))
        self.PlPlot.setSizeIncrement(QtCore.QSize(3, 1))
        self.PlPlot.setAutoFillBackground(True)
        self.PlPlot.setObjectName("PlPlot")
        self.gridLayout.addWidget(self.PlPlot, 0, 0, 1, 2)
        self.LabelMin = QtWidgets.QLabel(self.MainGrid)
        self.LabelMin.setObjectName("LabelMin")
        self.gridLayout.addWidget(self.LabelMin, 2, 0, 1, 1)
        self.CheckBoxAgreed = QtWidgets.QCheckBox(self.MainGrid)
        self.CheckBoxAgreed.setCheckable(True)
        self.CheckBoxAgreed.setChecked(True)
        self.CheckBoxAgreed.setObjectName("CheckBoxAgreed")
        self.gridLayout.addWidget(self.CheckBoxAgreed, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.MainGrid, 0, 1, 1, 1)

        self.retranslateUi()

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.LabelValue.setText(_translate("WindiwParametrPlot", " x:"))
        self.LabelMax.setText(_translate("WindiwParametrPlot", "max x:"))
        self.LabelMin.setText(_translate("WindiwParametrPlot", "min x:"))
        self.CheckBoxAgreed.setText(_translate("WindiwParametrPlot",
                                               "agreed, a"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_WindiwParametrPlot()
    window.show()
    sys.exit(app.exec_())
