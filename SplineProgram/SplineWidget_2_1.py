# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplineWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplineWidget(object):

    def setupUi(self, SplineWidget):

        SplineWidget.setObjectName("SplineWidget")
        SplineWidget.resize(640, 540)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
                            SplineWidget.sizePolicy().hasHeightForWidth())

        SplineWidget.setSizePolicy(sizePolicy)
        SplineWidget.setSizeIncrement(QtCore.QSize(1, 1))

        self.gridLayout_2 = QtWidgets.QGridLayout(SplineWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridWidget = QtWidgets.QWidget(SplineWidget)
        self.gridWidget.setObjectName("gridWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)

        self.alpha_label = QtWidgets.QLabel(self.gridWidget)
        self.alpha_label.setAutoFillBackground(True)
        self.alpha_label.setObjectName("alpha_label")
        self.gridLayout.addWidget(self.alpha_label, 11, 6, 1, 1)

        self.PlBl_button = QtWidgets.QToolButton(self.gridWidget)
        self.PlBl_button.setObjectName("PlBl_button")
        self.gridLayout.addWidget(self.PlBl_button, 2, 3, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 10, 6, 1, 1)

        self.Model_plot = GraphicsLayoutWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.Model_plot.sizePolicy().hasHeightForWidth())
        self.Model_plot.setSizePolicy(sizePolicy)
        self.Model_plot.setObjectName("Model_plot")
        self.gridLayout.addWidget(self.Model_plot, 1, 8, 12, 3)

        self.min_s_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.min_s_box.setMaximum(9999.99)
        self.min_s_box.setObjectName("min_s_box")
        self.gridLayout.addWidget(self.min_s_box, 2, 1, 1, 1)

        self.s_label = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.s_label.setFont(font)
        self.s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s_label.setAutoFillBackground(True)
        self.s_label.setWordWrap(False)
        self.s_label.setObjectName("s_label")
        self.gridLayout.addWidget(self.s_label, 3, 5, 1, 1)

        self.alpha_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.alpha_box.setMaximum(10.0)
        self.alpha_box.setSingleStep(0.1)
        self.alpha_box.setProperty("value", 1.5)
        self.alpha_box.setObjectName("alpha_box")
        self.gridLayout.addWidget(self.alpha_box, 12, 6, 1, 1)

        self.spline_model_label = QtWidgets.QLabel(self.gridWidget)
        self.spline_model_label.setObjectName("spline_model_label")
        self.gridLayout.addWidget(self.spline_model_label, 0, 8, 1, 3)

        self.s_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.s_box.setObjectName("s_box")
        self.gridLayout.addWidget(self.s_box, 3, 6, 1, 1)

        self.PlBel_plot = PlotWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(
                            QtWidgets.QSizePolicy.Expanding,
                            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
                            self.PlBel_plot.sizePolicy().hasHeightForWidth())
        self.PlBel_plot.setSizePolicy(sizePolicy)
        self.PlBel_plot.setObjectName("PlBel_plot")
        self.gridLayout.addWidget(self.PlBel_plot, 1, 0, 1, 7)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 13, 9, 1, 1)

        self.pl_bel_label = QtWidgets.QLabel(self.gridWidget)
        self.pl_bel_label.setObjectName("pl_bel_label")
        self.gridLayout.addWidget(self.pl_bel_label, 0, 0, 1, 7)

        self.save_model_button = QtWidgets.QPushButton(self.gridWidget)
        self.save_model_button.setObjectName("save_model_button")
        self.gridLayout.addWidget(self.save_model_button, 15, 10, 1, 1)

        self.max_s_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.max_s_box.setMaximum(999.99)
        self.max_s_box.setProperty("value", 100.0)
        self.max_s_box.setObjectName("max_s_box")
        self.gridLayout.addWidget(self.max_s_box, 2, 6, 1, 1)

        self.load_data_button = QtWidgets.QPushButton(self.gridWidget)
        self.load_data_button.setObjectName("load_data_button")
        self.gridLayout.addWidget(self.load_data_button, 13, 8, 1, 1)

        self.num_label = QtWidgets.QLabel(self.gridWidget)
        self.num_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.num_label.setAutoFillBackground(True)
        self.num_label.setObjectName("num_label")
        self.gridLayout.addWidget(self.num_label, 13, 6, 1, 1)

        self.load_model_button = QtWidgets.QPushButton(self.gridWidget)
        self.load_model_button.setObjectName("load_model_button")
        self.gridLayout.addWidget(self.load_model_button, 13, 10, 1, 1)

        self.max_s_label = QtWidgets.QLabel(self.gridWidget)
        self.max_s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.max_s_label.setAutoFillBackground(True)
        self.max_s_label.setObjectName("max_s_label")
        self.gridLayout.addWidget(self.max_s_label, 2, 5, 1, 1)

        self.min_s_label = QtWidgets.QLabel(self.gridWidget)
        self.min_s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.min_s_label.setAutoFillBackground(True)
        self.min_s_label.setObjectName("min_s_label")
        self.gridLayout.addWidget(self.min_s_label, 2, 0, 1, 1)

        self.line = QtWidgets.QFrame(self.gridWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 7, 16, 1)

        self.num_box = QtWidgets.QSpinBox(self.gridWidget)
        self.num_box.setMinimum(100)
        self.num_box.setMaximum(10000)
        self.num_box.setSingleStep(50)
        self.num_box.setProperty("value", 400)
        self.num_box.setObjectName("num_box")
        self.gridLayout.addWidget(self.num_box, 15, 6, 1, 1)

        self.k_label = QtWidgets.QLabel(self.gridWidget)
        self.k_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.k_label.setAutoFillBackground(True)
        self.k_label.setObjectName("k_label")
        self.gridLayout.addWidget(self.k_label, 3, 0, 1, 1)

        self.k_box = QtWidgets.QSpinBox(self.gridWidget)
        self.k_box.setMinimum(1)
        self.k_box.setMaximum(5)
        self.k_box.setObjectName("k_box")
        self.gridLayout.addWidget(self.k_box, 3, 1, 1, 1)

        self.result_button = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.result_button.sizePolicy().hasHeightForWidth())
        self.result_button.setSizePolicy(sizePolicy)
        self.result_button.setObjectName("result_button")
        self.gridLayout.addWidget(self.result_button, 15, 8, 1, 1)

        self.options_button = QtWidgets.QPushButton(self.gridWidget)
        self.options_button.setObjectName("options_button")
        self.gridLayout.addWidget(self.options_button, 15, 9, 1, 1)

        self.graphicsView = PlotWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
                        self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 6, 0, 10, 6)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 6, 3, 1)

        self.checkBox = QtWidgets.QCheckBox(self.gridWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 6, 1, 1)

        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        self.retranslateUi(SplineWidget)
        QtCore.QMetaObject.connectSlotsByName(SplineWidget)
        SplineWidget.setTabOrder(self.PlBel_plot, self.Model_plot)
        SplineWidget.setTabOrder(self.Model_plot, self.max_s_box)
        SplineWidget.setTabOrder(self.max_s_box, self.s_box)
        SplineWidget.setTabOrder(self.s_box, self.save_model_button)

    def retranslateUi(self, SplineWidget):
        _translate = QtCore.QCoreApplication.translate
        SplineWidget.setWindowTitle(_translate("SplineWidget",
                                               "SplineProgram"))
        self.alpha_label.setText(_translate("SplineWidget", "a:"))
        self.PlBl_button.setText(_translate("SplineWidget", "..."))
        self.s_label.setText(_translate("SplineWidget", "s:"))
        self.spline_model_label.setText(_translate("SplineWidget",
                                                   "Spline Model"))
        self.pl_bel_label.setText(_translate("SplineWidget",
                                             "Plausibility and Believability"))
        self.save_model_button.setText(_translate("SplineWidget",
                                                  "Save Model "))
        self.load_data_button.setText(_translate("SplineWidget",
                                                 "Load Data"))
        self.num_label.setText(_translate("SplineWidget",
                                          "Number of steps:"))
        self.load_model_button.setText(_translate("SplineWidget",
                                                  "Load Model"))
        self.max_s_label.setText(_translate("SplineWidget",
                                            "max s:"))
        self.min_s_label.setText(_translate("SplineWidget",
                                            "min s:"))
        self.k_label.setText(_translate("SplineWidget",
                                        "k:"))
        self.result_button.setText(_translate("SplineWidget",
                                              "Result"))
        self.options_button.setText(_translate("SplineWidget",
                                               "Options"))
        self.checkBox.setText(_translate("SplineWidget",
                                         "detailed"))

from pyqtgraph import GraphicsLayoutWidget, PlotWidget
