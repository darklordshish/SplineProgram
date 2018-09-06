# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplineWidget_3.0.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import importlib as im
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from SplineWidget_2_0 import Ui_SplineWidget

class Ui_SplineWidget_3_0(object):
    def setupUi(self, SplineWidget_3_0):
        SplineWidget_3_0.setObjectName("SplineWidget_3_0")
        SplineWidget_3_0.resize(633, 458)
        self.gridLayout_2 = QtWidgets.QGridLayout(SplineWidget_3_0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.MainWidget = QtWidgets.QTabWidget(SplineWidget_3_0)
        self.MainWidget.setObjectName("MainWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NextStepButton = QtWidgets.QPushButton(self.tab)
        self.NextStepButton.setObjectName("NextStepButton")
        self.gridLayout_3.addWidget(self.NextStepButton, 1, 0, 1, 1)
        self.widget = Ui_SplineWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.MainWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.MainWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(SplineWidget_3_0)
        self.MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SplineWidget_3_0)

    def retranslateUi(self, SplineWidget_3_0):
        _translate = QtCore.QCoreApplication.translate
        SplineWidget_3_0.setWindowTitle(_translate("SplineWidget_3_0",
                                                   "Form"))
        self.NextStepButton.setText(_translate("SplineWidget_3_0",
                                               "Next Step"))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab),
                                   _translate("SplineWidget_3_0", "Tab 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplineWidget_3_0 = QtWidgets.QWidget()
    ui = Ui_SplineWidget_3_0()
    ui.setupUi(SplineWidget_3_0)
    SplineWidget_3_0.show()
    sys.exit(app.exec_())

