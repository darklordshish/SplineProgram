# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlBel.ui'
#
# Created: Wed Jul 27 10:23:49 2016
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(851, 671)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(False)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResPlBel = PlotWidget(Form)
        self.ResPlBel.setGeometry(QtCore.QRect(470, 10, 381, 281))
        self.ResPlBel.setObjectName(_fromUtf8("ResPlBel"))
        self.ParamPlBel = PlotWidget(Form)
        self.ParamPlBel.setGeometry(QtCore.QRect(0, 10, 381, 281))
        self.ParamPlBel.setObjectName(_fromUtf8("ParamPlBel"))
        self.convertButton = QtGui.QPushButton(Form)
        self.convertButton.setGeometry(QtCore.QRect(400, 20, 51, 31))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.loadButton = QtGui.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(540, 300, 121, 25))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.FunctionPlot = PlotWidget(Form)
        self.FunctionPlot.setGeometry(QtCore.QRect(0, 340, 851, 331))
        self.FunctionPlot.setObjectName(_fromUtf8("FunctionPlot"))
        self.spline_degree = QtGui.QSpinBox(Form)
        self.spline_degree.setGeometry(QtCore.QRect(90, 310, 55, 24))
        self.spline_degree.setMinimum(1)
        self.spline_degree.setMaximum(5)
        self.spline_degree.setObjectName(_fromUtf8("spline_degree"))
        self.label_k = QtGui.QLabel(Form)
        self.label_k.setGeometry(QtCore.QRect(70, 300, 16, 16))
        self.label_k.setObjectName(_fromUtf8("label_k"))
        self.steps = QtGui.QSpinBox(Form)
        self.steps.setGeometry(QtCore.QRect(790, 300, 55, 24))
        self.steps.setMinimum(100)
        self.steps.setMaximum(5000)
        self.steps.setProperty("value", 400)
        self.steps.setObjectName(_fromUtf8("steps"))
        self.label_steps = QtGui.QLabel(Form)
        self.label_steps.setGeometry(QtCore.QRect(680, 300, 111, 31))
        self.label_steps.setObjectName(_fromUtf8("label_steps"))
        self.x_min = QtGui.QDoubleSpinBox(Form)
        self.x_min.setGeometry(QtCore.QRect(190, 310, 62, 24))
        self.x_min.setMinimum(-100000.0)
        self.x_min.setMaximum(100000.0)
        self.x_min.setProperty("value", 0.3)
        self.x_min.setObjectName(_fromUtf8("x_min"))
        self.x_max = QtGui.QDoubleSpinBox(Form)
        self.x_max.setGeometry(QtCore.QRect(310, 310, 62, 24))
        self.x_max.setMinimum(-100000.0)
        self.x_max.setMaximum(100000.0)
        self.x_max.setProperty("value", 1.0)
        self.x_max.setObjectName(_fromUtf8("x_max"))
        self.label_x_min = QtGui.QLabel(Form)
        self.label_x_min.setGeometry(QtCore.QRect(150, 300, 41, 16))
        self.label_x_min.setObjectName(_fromUtf8("label_x_min"))
        self.label_xmax = QtGui.QLabel(Form)
        self.label_xmax.setGeometry(QtCore.QRect(260, 300, 41, 16))
        self.label_xmax.setObjectName(_fromUtf8("label_xmax"))
        self.clear_PlBel_res = QtGui.QPushButton(Form)
        self.clear_PlBel_res.setGeometry(QtCore.QRect(480, 300, 51, 25))
        self.clear_PlBel_res.setObjectName(_fromUtf8("clear_PlBel_res"))
        self.clear_PlBel_param = QtGui.QPushButton(Form)
        self.clear_PlBel_param.setGeometry(QtCore.QRect(10, 300, 51, 25))
        self.clear_PlBel_param.setObjectName(_fromUtf8("clear_PlBel_param"))
        self.ParamToRes = QtGui.QRadioButton(Form)
        self.ParamToRes.setGeometry(QtCore.QRect(400, 70, 51, 20))
        self.ParamToRes.setCheckable(True)
        self.ParamToRes.setChecked(True)
        self.ParamToRes.setObjectName(_fromUtf8("ParamToRes"))
        self.ResToParam = QtGui.QRadioButton(Form)
        self.ResToParam.setGeometry(QtCore.QRect(400, 100, 51, 20))
        self.ResToParam.setChecked(False)
        self.ResToParam.setObjectName(_fromUtf8("ResToParam"))
        self.SaveButton = QtGui.QPushButton(Form)
        self.SaveButton.setGeometry(QtCore.QRect(400, 260, 51, 25))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.LoadButton = QtGui.QPushButton(Form)
        self.LoadButton.setGeometry(QtCore.QRect(400, 230, 51, 25))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.convertButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ParamPlBel.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "PlBel", None))
        self.convertButton.setText(_translate("Form", "<=>", None))
        self.loadButton.setText(_translate("Form", "Load function", None))
        self.label_k.setText(_translate("Form", "k:", None))
        self.label_steps.setText(_translate("Form", "number of steps:", None))
        self.label_x_min.setText(_translate("Form", "X min:", None))
        self.label_xmax.setText(_translate("Form", "X max:", None))
        self.clear_PlBel_res.setText(_translate("Form", "Clear", None))
        self.clear_PlBel_param.setText(_translate("Form", "Clear", None))
        self.ParamToRes.setText(_translate("Form", "=>", None))
        self.ResToParam.setText(_translate("Form", "<=", None))
        self.SaveButton.setText(_translate("Form", "Save", None))
        self.LoadButton.setText(_translate("Form", "Load", None))

from pyqtgraph import PlotWidget
