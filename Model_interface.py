# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Model.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys
import os
import importlib as im
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np

from scipy.optimize import brentq

import dill as pickle
from PlBelPlot import PlBelPlot
import Model
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

def load_module_by_path(module_path):
    """
    Загрузка модуля по пути к нему.
    """
    directory, module_name = os.path.split(module_path)
    module_name = os.path.splitext(module_name)[0]

    path = list(sys.path)
    sys.path.insert(0, directory) # Добавление директории с модулем в PATH на первое место
    try:
        module = im.import_module(module_name)
    except ImportError:#, TypeError, SyntaxError, NameError,AttributeError):
        raise
    finally:
        sys.path[:] = path # Восстановление исходного PATH
    return module

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(880, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName(_fromUtf8("widget"))

        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 851, 501))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
#################
###Вкладка модели
#################



        self.Model = QtGui.QWidget()
        self.Model.setObjectName(_fromUtf8("Model"))

        self.verticalLayoutWidget = QtGui.QWidget(self.Model)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 471))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))

        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.FunctionPlot =gl.GLViewWidget()
        self.FunctionPlot.opts['distance'] = 40
        self.FunctionPlot.setObjectName(_fromUtf8("FunctionPlot"))
##############################
###Задание модели по умолчанию
##############################
        self.Main_part_of_model=Model.Model()
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.FunctionPlot.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.FunctionPlot.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.FunctionPlot.addItem(gz)
        print(self.Main_part_of_model.greed,self.Main_part_of_model.Results[0].meaning)
        md=np.array([self.Main_part_of_model.greed[0],self.Main_part_of_model.greed[1],self.Main_part_of_model.Results[0].meaning])
        m1 = gl.GLScatterPlotItem(pos=md)
        m1.setGLOptions('additive')
        self.FunctionPlot.addItem(m1)


        self.verticalLayout.addWidget(self.FunctionPlot)

        self.gridLayoutWidget_4 = QtGui.QWidget(self.Model)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(540, 0, 301, 471))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))

        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))

        self.number_of_relsults = QtGui.QLabel(self.gridLayoutWidget_4)
        self.number_of_relsults.setObjectName(_fromUtf8("number_of_relsults"))

        self.gridLayout_5.addWidget(self.number_of_relsults, 5, 0, 1, 2)

        self.discription_of_the_model = QtGui.QLabel(self.gridLayoutWidget_4)
        self.discription_of_the_model.setObjectName(_fromUtf8("discription_of_the_model"))

        self.gridLayout_5.addWidget(self.discription_of_the_model, 0, 0, 1, 3)

        self.ResNumBox = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.ResNumBox.setMinimum(1)
        self.ResNumBox.setMaximum(10)
        self.ResNumBox.setProperty("value", 1)
        self.ResNumBox.setObjectName(_fromUtf8("ResNumBox"))

        self.gridLayout_5.addWidget(self.ResNumBox, 5, 2, 1, 1)

        self.ModelDiscription = QtGui.QTextBrowser(self.gridLayoutWidget_4)
        self.ModelDiscription.setObjectName(_fromUtf8("ModelDiscription"))
        self.ModelDiscription.isEnabled()

        self.gridLayout_5.addWidget(self.ModelDiscription, 1, 0, 1, 3)

        self.ParamNumBox = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.ParamNumBox.setMinimum(1)
        self.ParamNumBox.setMaximum(10)
        self.ParamNumBox.setProperty("value", 2)
        self.ParamNumBox.setObjectName(_fromUtf8("ParamNumBox"))

        self.gridLayout_5.addWidget(self.ParamNumBox, 2, 2, 1, 1)

        self.number_of_parameters = QtGui.QLabel(self.gridLayoutWidget_4)
        self.number_of_parameters.setObjectName(_fromUtf8("number_of_parameters"))

        self.gridLayout_5.addWidget(self.number_of_parameters, 2, 0, 1, 2)

        self.OptionsButton = QtGui.QToolButton(self.gridLayoutWidget_4)
        self.OptionsButton.setObjectName(_fromUtf8("OptionsButton"))

        self.gridLayout_5.addWidget(self.OptionsButton, 6, 2, 1, 1)

        self.options = QtGui.QLabel(self.gridLayoutWidget_4)
        self.options.setObjectName(_fromUtf8("options"))

        self.gridLayout_5.addWidget(self.options, 6, 1, 1, 1)

        self.LoadFunction = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.LoadFunction.setObjectName(_fromUtf8("LoadFunction"))

        self.gridLayout_5.addWidget(self.LoadFunction, 6, 0, 1, 1)
#####################
###Вкладка параметров
#####################
        self.tabWidget.addTab(self.Model, _fromUtf8(""))

        self.Parameters_2 = QtGui.QWidget()
        self.Parameters_2.setObjectName(_fromUtf8("Parameters_2"))

        self.horizontalLayoutWidget = QtGui.QWidget(self.Parameters_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 401))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.Parameters = QtGui.QTabWidget(self.horizontalLayoutWidget)
        self.Parameters.setObjectName(_fromUtf8("Parameters"))

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 831, 371))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.PlPlot = PlBelPlot(self.horizontalLayoutWidget_2)
        self.PlPlot.setObjectName(_fromUtf8("PlPlot"))

        self.horizontalLayout_2.addWidget(self.PlPlot)

        self.BelPlot = PlBelPlot(self.horizontalLayoutWidget_2)
        self.BelPlot.setObjectName(_fromUtf8("BelPlot"))

        self.horizontalLayout_2.addWidget(self.BelPlot)

        self.Parameters.addTab(self.tab_3, _fromUtf8(""))

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.tab_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 831, 371))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))

        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        self.PlPlot_2 = PlBelPlot(self.horizontalLayoutWidget_4)
        self.PlPlot_2.setObjectName(_fromUtf8("PlPlot_2"))

        self.horizontalLayout_4.addWidget(self.PlPlot_2)

        self.BelPLot = PlBelPlot(self.horizontalLayoutWidget_4)
        self.BelPLot.setObjectName(_fromUtf8("BelPLot"))

        self.horizontalLayout_4.addWidget(self.BelPLot)

        self.Parameters.addTab(self.tab_4, _fromUtf8(""))

        self.horizontalLayout.addWidget(self.Parameters)

        self.gridLayoutWidget = QtGui.QWidget(self.Parameters_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 410, 841, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))

        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        self.spline_degree = QtGui.QLabel(self.gridLayoutWidget)
        self.spline_degree.setObjectName(_fromUtf8("spline_degree"))

        self.gridLayout_2.addWidget(self.spline_degree, 0, 8, 1, 1)

        self.BoxK = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BoxK.setMinimum(1)
        self.BoxK.setMaximum(5)
        self.BoxK.setObjectName(_fromUtf8("BoxK"))

        self.gridLayout_2.addWidget(self.BoxK, 0, 9, 1, 1)

        self.min = QtGui.QLabel(self.gridLayoutWidget)
        self.min.setObjectName(_fromUtf8("min"))

        self.gridLayout_2.addWidget(self.min, 0, 0, 1, 1)

        self.MinX = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.MinX.setMinimum(-10000.0)
        self.MinX.setMaximum(10000.0)
        self.MinX.setObjectName(_fromUtf8("MinX"))

        self.gridLayout_2.addWidget(self.MinX, 0, 1, 1, 1)

        self.MaxX = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.MaxX.setMinimum(-10000.0)
        self.MaxX.setMaximum(10000.0)
        self.MaxX.setProperty("value", 1.0)
        self.MaxX.setObjectName(_fromUtf8("MaxX"))

        self.gridLayout_2.addWidget(self.MaxX, 0, 3, 1, 1)

        self.max = QtGui.QLabel(self.gridLayoutWidget)
        self.max.setObjectName(_fromUtf8("max"))

        self.gridLayout_2.addWidget(self.max, 0, 2, 1, 1)

        self.number_of_steps = QtGui.QLabel(self.gridLayoutWidget)
        self.number_of_steps.setObjectName(_fromUtf8("number_of_steps"))

        self.gridLayout_2.addWidget(self.number_of_steps, 0, 6, 1, 1)

        self.BoxNum = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BoxNum.setMinimum(100)
        self.BoxNum.setMaximum(5000)
        self.BoxNum.setSingleStep(100)
        self.BoxNum.setProperty("value", 400)
        self.BoxNum.setObjectName(_fromUtf8("BoxNum"))

        self.gridLayout_2.addWidget(self.BoxNum, 0, 7, 1, 1)

        self.CoordDistr = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CoordDistr.setChecked(True)
        self.CoordDistr.setObjectName(_fromUtf8("CoordDistr"))

        self.gridLayout_2.addWidget(self.CoordDistr, 0, 4, 1, 2)

        self.Calculation = QtGui.QPushButton(self.gridLayoutWidget)
        self.Calculation.setObjectName(_fromUtf8("Calculation"))

        self.gridLayout_2.addWidget(self.Calculation, 4, 4, 1, 2)

        self.CleaningPl = QtGui.QPushButton(self.gridLayoutWidget)
        self.CleaningPl.setObjectName(_fromUtf8("CleaningPl"))

        self.gridLayout_2.addWidget(self.CleaningPl, 4, 2, 1, 1)

        self.CleaningBel = QtGui.QPushButton(self.gridLayoutWidget)
        self.CleaningBel.setObjectName(_fromUtf8("CleaningBel"))

        self.gridLayout_2.addWidget(self.CleaningBel, 4, 7, 1, 1)
####################
###Вкладка следствий
####################
        self.tabWidget.addTab(self.Parameters_2, _fromUtf8(""))

        self.Results = QtGui.QWidget()
        self.Results.setObjectName(_fromUtf8("Results"))

        self.gridLayoutWidget_2 = QtGui.QWidget(self.Results)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 841, 401))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))

        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        self.Results_2 = QtGui.QTabWidget(self.gridLayoutWidget_2)
        self.Results_2.setObjectName(_fromUtf8("Results_2"))

        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))

        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_6)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 831, 371))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.PlPlot_3 = PlBelPlot(self.horizontalLayoutWidget_3)
        self.PlPlot_3.setObjectName(_fromUtf8("PlPlot_3"))

        self.horizontalLayout_3.addWidget(self.PlPlot_3)

        self.BelPlot_2 = PlBelPlot(self.horizontalLayoutWidget_3)
        self.BelPlot_2.setObjectName(_fromUtf8("BelPlot_2"))

        self.horizontalLayout_3.addWidget(self.BelPlot_2)

        self.Results_2.addTab(self.tab_6, _fromUtf8(""))

        self.gridLayout_3.addWidget(self.Results_2, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QtGui.QWidget(self.Results)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 410, 831, 71))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))

        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))

        self.number_of_steps_2 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.number_of_steps_2.setObjectName(_fromUtf8("number_of_steps_2"))

        self.gridLayout_4.addWidget(self.number_of_steps_2, 0, 0, 1, 1)

        self.spline_degree_2 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.spline_degree_2.setObjectName(_fromUtf8("spline_degree_2"))

        self.gridLayout_4.addWidget(self.spline_degree_2, 0, 3, 1, 1)

        self.BoxK_2 = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.BoxK_2.setObjectName(_fromUtf8("BoxK_2"))

        self.gridLayout_4.addWidget(self.BoxK_2, 0, 4, 1, 1)

        self.CoordDistr_2 = QtGui.QCheckBox(self.gridLayoutWidget_3)
        self.CoordDistr_2.setChecked(True)
        self.CoordDistr_2.setObjectName(_fromUtf8("CoordDistr_2"))

        self.gridLayout_4.addWidget(self.CoordDistr_2, 0, 2, 1, 1)

        self.BoxNUm = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.BoxNUm.setObjectName(_fromUtf8("BoxNUm"))

        self.gridLayout_4.addWidget(self.BoxNUm, 0, 1, 1, 1)

        self.Calculation_2 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.Calculation_2.setObjectName(_fromUtf8("Calculation_2"))

        self.gridLayout_4.addWidget(self.Calculation_2, 1, 2, 1, 1)

        self.CleaningPl_2 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.CleaningPl_2.setObjectName(_fromUtf8("CleaningPl_2"))

        self.gridLayout_4.addWidget(self.CleaningPl_2, 1, 1, 1, 1)

        self.CleaningBel_2 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.CleaningBel_2.setObjectName(_fromUtf8("CleaningBel_2"))

        self.gridLayout_4.addWidget(self.CleaningBel_2, 1, 3, 1, 1)

        self.tabWidget.addTab(self.Results, _fromUtf8(""))

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
#######
###Меню
#######
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_model = QtGui.QAction(MainWindow)
        self.actionCreate_model.setObjectName(_fromUtf8("actionCreate_model"))

        self.actionLoad_Model = QtGui.QAction(MainWindow)
        self.actionLoad_Model.setObjectName(_fromUtf8("actionLoad_Model"))

        self.actionSave_Model = QtGui.QAction(MainWindow)
        self.actionSave_Model.setObjectName(_fromUtf8("actionSave_Model"))

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.menuMenu.addAction(self.actionCreate_model)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionLoad_Model)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSave_Model)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)

        self.menubar.addAction(self.menuMenu.menuAction())



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.Parameters.setCurrentIndex(0)
        self.Results_2.setCurrentIndex(0)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def SetModel(self, Model):
        return 0

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.number_of_relsults.setText(_translate("MainWindow", "Кол-во н.о. следствий:", None))
        self.discription_of_the_model.setText(_translate("MainWindow", "                    Описание Модели", None))
        self.number_of_parameters.setText(_translate("MainWindow", "Кол-во н.о. параметров:", None))
        self.OptionsButton.setText(_translate("MainWindow", "...", None))
        self.options.setText(_translate("MainWindow", "      Настройки:", None))
        self.LoadFunction.setText(_translate("MainWindow", "Загрузка Функции", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Model), _translate("MainWindow", "Модель", None))
        self.Parameters.setTabText(self.Parameters.indexOf(self.tab_3), _translate("MainWindow", "1 ", None))
        self.Parameters.setTabText(self.Parameters.indexOf(self.tab_4), _translate("MainWindow", "2", None))
        self.spline_degree.setText(_translate("MainWindow", "Степень сплайна, k:", None))
        self.min.setText(_translate("MainWindow", " Min. :", None))
        self.max.setText(_translate("MainWindow", "Max.:", None))
        self.number_of_steps.setText(_translate("MainWindow", "Число шагов:", None))
        self.CoordDistr.setText(_translate("MainWindow", "Соглас. распред.", None))
        self.Calculation.setText(_translate("MainWindow", "Расчёт", None))
        self.CleaningPl.setText(_translate("MainWindow", "Очистка", None))
        self.CleaningBel.setText(_translate("MainWindow", "Очистка", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Parameters_2), _translate("MainWindow", "Н.о. параметры", None))
        self.Results_2.setTabText(self.Results_2.indexOf(self.tab_6), _translate("MainWindow", "1", None))
        self.number_of_steps_2.setText(_translate("MainWindow", "          Число шагов:", None))
        self.spline_degree_2.setText(_translate("MainWindow", "Степень сплайна, k:", None))
        self.CoordDistr_2.setText(_translate("MainWindow", "согласованные распределения", None))
        self.Calculation_2.setText(_translate("MainWindow", "Расчёт", None))
        self.CleaningPl_2.setText(_translate("MainWindow", "Очистка", None))
        self.CleaningBel_2.setText(_translate("MainWindow", "Очистка", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), _translate("MainWindow", "Следствия модели", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Меню", None))
        self.actionCreate_model.setText(_translate("MainWindow", "Новая модель", None))
        self.actionCreate_model.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionLoad_Model.setText(_translate("MainWindow", "Загрузить модель", None))
        self.actionLoad_Model.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave_Model.setText(_translate("MainWindow", "Сохранить модель", None))
        self.actionSave_Model.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Выход", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X", None))


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui= Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
