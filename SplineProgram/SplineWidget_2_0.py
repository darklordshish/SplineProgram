# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplineWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import dill
import importlib as im
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from SplineAndErrorPlotWidget import SplineAndErrorPlotWidget
from PlBelPlot import PlBelPlot
from TruePlot import TruePlot
from TwoParam import TwoParam
from TrueDataPlot import TrueDataPlot


def load_module_by_path(module_path):
    """
    Загрузка модуля по пути к нему.
    """
    directory, module_name = os.path.split(module_path)
    print(module_name)
    module_name = os.path.splitext(module_name)[0]
    print(module_name)
    path = list(sys.path)
    sys.path.insert(0, directory)
    # Добавление директории с модулем в PATH на
    # первое место
    try:
        module = im.import_module(module_name)
        return module
    except ImportError:  # TypeError, SyntaxError, NameError,AttributeError):
        raise
    finally:
        sys.path[:] = path  # Восстановление исходного PATH


class Ui_SplineWidget(QWidget):
    """
    Spline widget. You can add your data in the program and make subjective
    analisis of the data. It'll help you build distributions of
    Plausibility and Believability
    """
    def __init__(self,):
        super().__init__()
        self.setupUi()

    def setupUi(self,):
        """
        """
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridWidget = QtWidgets.QWidget(self)
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

        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 13, 9, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 6, 3, 1)

        self.spline_model_label = QtWidgets.QLabel(self.gridWidget)
        self.spline_model_label.setObjectName("spline_model_label")
        self.gridLayout.addWidget(self.spline_model_label, 0, 8, 1, 3)

        self.pl_bel_label = QtWidgets.QLabel(self.gridWidget)
        self.pl_bel_label.setObjectName("pl_bel_label")
        self.gridLayout.addWidget(self.pl_bel_label, 0, 0, 1, 7)

        self.PlBel_plot_k = PlBelPlot(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.PlBel_plot_k.sizePolicy().hasHeightForWidth())
        self.PlBel_plot_k.setSizePolicy(sizePolicy)
        self.PlBel_plot_k.setObjectName("PlBel_plot_k")
        self.gridLayout.addWidget(self.PlBel_plot_k, 6, 0, 10, 6)
        self.PlBel_plot_k.Discrete = True

        self.PlBel_plot_s = PlBelPlot(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
            self.PlBel_plot_s.sizePolicy().hasHeightForWidth())
        self.PlBel_plot_s.setSizePolicy(sizePolicy)
        self.PlBel_plot_s.setObjectName("PlBel_plot_s")
        self.gridLayout.addWidget(self.PlBel_plot_s, 1, 0, 1, 7)

        self.PlBl_button = QtWidgets.QToolButton(self.gridWidget)
        self.PlBl_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PlBl_button.setAutoFillBackground(True)
        self.PlBl_button.setObjectName("PlBl_button")
        self.gridLayout.addWidget(self.PlBl_button, 2, 3, 1, 1)

        self.two_param_check = QtWidgets.QCheckBox(self.gridWidget)
        self.two_param_check.setObjectName("detailed")
        self.gridLayout.addWidget(self.two_param_check, 6, 6, 1, 1)

        self.s_label = QtWidgets.QLabel(self.gridWidget)
        self.s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s_label.setAutoFillBackground(True)
        self.s_label.setWordWrap(False)
        self.s_label.setObjectName("s_label")
        self.gridLayout.addWidget(self.s_label, 3, 5, 1, 1)

        self.s_box = QtWidgets.QDoubleSpinBox(self.gridWidget, decimals=5)
        self.s_box.setValue(100)
        self.s_box.setMaximum(1000000)
        self.s_box.setObjectName("s_box")
        self.gridLayout.addWidget(self.s_box, 3, 6, 1, 1)

        self.max_s_label = QtWidgets.QLabel(self.gridWidget)
        self.max_s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.max_s_label.setAutoFillBackground(True)
        self.max_s_label.setObjectName("max_s_label")
        self.gridLayout.addWidget(self.max_s_label, 2, 5, 1, 1)

        self.max_s_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.max_s_box.setMaximum(1000000)
        self.max_s_box.setProperty("value", 150.0)
        self.max_s_box.setObjectName("max_s_box")
        self.gridLayout.addWidget(self.max_s_box, 2, 6, 1, 1)

        self.min_s_label = QtWidgets.QLabel(self.gridWidget)
        self.min_s_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.min_s_label.setAutoFillBackground(True)
        self.min_s_label.setObjectName("min_s_label")
        self.gridLayout.addWidget(self.min_s_label, 2, 0, 1, 1)

        self.min_s_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.min_s_box.setMaximum(1000000)
        self.min_s_box.setMinimum(0)
        self.min_s_box.setValue(0)
        self.min_s_box.setObjectName("min_s_box")
        self.gridLayout.addWidget(self.min_s_box, 2, 1, 1, 1)

        self.alpha_label = QtWidgets.QLabel(self.gridWidget)
        self.alpha_label.setAutoFillBackground(True)
        self.alpha_label.setObjectName("alpha_label")
        self.gridLayout.addWidget(self.alpha_label, 11, 6, 1, 1)

        self.alpha_box = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.alpha_box.setMaximum(10.0)
        self.alpha_box.setSingleStep(0.1)
        self.alpha_box.setProperty("value", 1.5)
        self.alpha_box.setObjectName("alpha_box")
        self.gridLayout.addWidget(self.alpha_box, 12, 6, 1, 1)

        self.num_label = QtWidgets.QLabel(self.gridWidget)
        self.num_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.num_label.setAutoFillBackground(True)
        self.num_label.setObjectName("num_label")
        self.gridLayout.addWidget(self.num_label, 13, 6, 1, 1)

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
        self.k_box.setValue(5)
        self.k_box.setObjectName("k_box")
        self.k = 5
        self.gridLayout.addWidget(self.k_box, 3, 1, 1, 1)

        self.Model_plot = SplineAndErrorPlotWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Model_plot.sizePolicy().hasHeightForWidth())
        self.Model_plot.setSizePolicy(sizePolicy)
        self.Model_plot.setObjectName("Model_plot")
        self.gridLayout.addWidget(self.Model_plot, 1, 8, 12, 3)

        self.data_plot_button = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.data_plot_button.sizePolicy().hasHeightForWidth())
        self.data_plot_button.setSizePolicy(sizePolicy)
        self.data_plot_button.setObjectName("data_plot_button")
        self.gridLayout.addWidget(self.data_plot_button, 15, 8, 1, 1)

        self.options_button = QtWidgets.QPushButton(self.gridWidget)
        self.options_button.setObjectName("options_button")
        self.gridLayout.addWidget(self.options_button, 15, 9, 1, 1)

        self.next_step_button = QtWidgets.QPushButton(self.gridWidget)
        self.next_step_button.setObjectName("next_step_button")
        self.gridLayout.addWidget(self.next_step_button, 13, 9, 1, 1)

        self.load_model_button = QtWidgets.QPushButton(self.gridWidget)
        self.load_model_button.setObjectName("load_model_button")
        self.gridLayout.addWidget(self.load_model_button, 13, 10, 1, 1)

        self.save_model_button = QtWidgets.QPushButton(self.gridWidget)
        self.save_model_button.setObjectName("save_model_button")
        self.gridLayout.addWidget(self.save_model_button, 15, 10, 1, 1)

        self.load_data_button = QtWidgets.QPushButton(self.gridWidget)
        self.load_data_button.setObjectName("load_data_button")
        self.gridLayout.addWidget(self.load_data_button, 13, 8, 1, 1)

        self.line = QtWidgets.QFrame(self.gridWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 7, 13, 1)

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

        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        """Castom"""
        self.pointsPlBel_s = {1: [np.array([]), np.array([])],
                              2: [np.array([]), np.array([])],
                              3: [np.array([]), np.array([])],
                              4: [np.array([]), np.array([])],
                              5: [np.array([]), np.array([])]
                              }
        self.number_of_steps = 0
        self.windowTrueExample = TruePlot()
        self.windowTrueExample.setWindowTitle("Data")

        self.windowTrueData = TrueDataPlot()
        self.windowTrueData.setWindowTitle("Data")

        self.x = np.load("data_x_2.npy")  # np.linspace(0, 200, 200)
        self.y = np.load("data_y_2.npy")  # self.func_rand(self.x)

        self.example_model = True
        self.NextSplineModel = None
        self.Detailed = TwoParam()
        self.Detailed.setWindowTitle("Two Param")

        self.retranslateUi()

        self.PlBel_plot_s.changeXmin(self.min_s_box.value())
        self.PlBel_plot_s.changeXmax(self.max_s_box.value())
        self.PlBel_plot_s.changeXlinePosition(self.s_box.value())
        self.Model_plot.ChangeData(self.x, self.y)
        self.Model_plot.ChangeK(self.k_box.value())
        self.Model_plot.ChangeS(self.s_box.value())
        self.windowTrueExample.ChangeData(self.x, self.y)
        self.windowTrueExample.func = self.func
        self.windowTrueData.ChangeData(self.x, self.y)
        self.Detailed.changeXmin(self.min_s_box.value())
        self.Detailed.changeXmax(self.max_s_box.value())
        self.Detailed.ParamPlot_1.changeXlinePosition(self.s_box.value())
        self.Detailed.ParamPlot_2.changeXlinePosition(self.s_box.value())

        """Slots and signals"""
        self.k_box.valueChanged[int].connect(self.Model_plot.ChangeK)
        self.PlBel_plot_k.xMin = self.k_box.minimum()
        self.PlBel_plot_k.xMax = self.k_box.maximum()
        self.PlBel_plot_k.xLine.setPos(self.k_box.value())
        self.k_box.valueChanged[int].connect(
            self.PlBel_plot_k.changeXlinePosition)
        self.PlBel_plot_k.xLine.sigLineXPos[float].connect(self.k_box.setValue)
        self.k_box.valueChanged[int].connect(self.switchPlBel_s)

        self.s_box.valueChanged[float].connect(self.Model_plot.ChangeS)
        self.s_box.valueChanged[float].connect(
            self.PlBel_plot_s.changeXlinePosition)
        self.PlBel_plot_s.xLine.sigLineXPos[float].connect(self.s_box.setValue)

        self.min_s_box.valueChanged[float].connect(
            self.PlBel_plot_s.changeXmin)
        self.max_s_box.valueChanged[float].connect(
            self.PlBel_plot_s.changeXmax)

        self.min_s_box.valueChanged[float].connect(
            self.Detailed.changeXmin)
        self.max_s_box.valueChanged[float].connect(
            self.Detailed.changeXmax)

        self.load_data_button.clicked.connect(self.load_data)

        self.PlBel_plot_s.sigChangePoints[list].connect(
            self.saveOldPoints)
        self.data_plot_button.clicked.connect(self.true_plot)

        self.next_step_button.clicked.connect(self.next_step)

        self.windowTrueExample.data_range.sigRegionChanged.connect(
                                                            self.RegionData)
        self.windowTrueData.data_range.sigRegionChanged.connect(
                                                            self.RegionData)
        self.two_param_check.clicked.connect(self.two_param_state)
        self.PlBl_button.clicked.connect(self.two_param)
        self.Detailed.ParamPlot_1.xLine.sigLineXPos[float].connect(
                                                        self.s_box.setValue)
        self.s_box.valueChanged[float].connect(
                              self.Detailed.ParamPlot_1.changeXlinePosition)
        self.Detailed.ParamPlot_2.xLine.sigLineXPos[float].connect(
                                                        self.s_box.setValue)
        self.s_box.valueChanged[float].connect(
                              self.Detailed.ParamPlot_2.changeXlinePosition)
        self.Detailed.ParamPlot_1.sigChangeDistribution.connect(
                                           self.pl_bel_plot_co_distribution)
        self.Detailed.ParamPlot_2.sigChangeDistribution.connect(
                                           self.pl_bel_plot_co_distribution)
        self.save_model_button.clicked.connect(self.save_model)
        self.load_model_button.clicked.connect(self.load_model)
        self.options_button.clicked.connect(self.show_result)

    """Methods"""
    def func(self, x):
        """
        модельная функция
        """
        y = (0.79*(np.sin(2*np.pi/24*x) +
             np.exp(-(x - 70)**2/100) +
             np.exp(-(x - 130)**2/130) +
             0.5*np.sin(np.heaviside(x-96, 76)*2*np.pi/27.4*x) +
             np.exp(-(np.heaviside(x-57, 1)*x - 200)**2/200)*np.sin(0.01*x) +
             0.01*np.heaviside(157-x, 1)*np.sin(2*np.pi*x/365)) + 20)
        return y

    def func_rand(self, func, x):
        """
        модель измерения с шумом
        """
        y = func(x) + np.random.randn(np.size(x))*0.20
        return y

    def switchPlBel_s(self, k):
        """
        переключение степени сплайна
        """
        self.PlBel_plot_s.changeScatterPlotData(self.pointsPlBel_s[k])

    def saveOldPoints(self, old_data):
        """
        сохранение распределения сглаивающего параметра
        для предыдущего значения степени сплайна
        """
        self.pointsPlBel_s[self.k] = old_data
        self.k = self.k_box.value()

    def RegionData(self,):
        """
        выделение части данных
        """
        if self.example_model:
            i, j = self.windowTrueExample.RegionInd()
        else:
            i, j = self.windowTrueData.RegionInd()
        self.Model_plot.ChangeData(self.x[i:j], self.y[i:j])

    def load_data(self, ):
        """
        Загрузка данных из файла
        """
        data_name = QtWidgets.QFileDialog.getOpenFileName(
                     QtWidgets.QWidget(), "Open file")
        try:
            dn = load_module_by_path(data_name[0])
            self.x = dn.x
            self.y = dn.y
            self.Model_plot.ChangeData(self.x, self.y)
            self.windowTrueData.ChangeData(self.x, self.y)
            self.example_model = False
        except (NameError, ValueError,
                AttributeError, TypeError,
                FileNotFoundError):  # V,
            print("Your data's name should be x and y")

    def true_plot(self, ):
        """
        Открытие окна с данными
        (и возможность выделить часть данных для обработки)
        """
        if self.example_model:
            self.windowTrueExample.show()
        else:
            self.windowTrueData.show()

    def two_param_state(self,):
        """
        Изменение состояния для построения совместного распределения
        """
        if self.two_param_check.isChecked():
            self.PlBel_plot_s.ResPlot = True
        else:
            self.PlBel_plot_s.ResPlot = False

    def two_param(self,):
        """
        It's opened TwoParam window
        """
        if self.two_param_check.isChecked():
            self.Detailed.show()
        else:
            pass

    def pl_bel_plot_co_distribution(self,):
        """
        построение совместного распределения
        """
        def codistribution(x):
            return np.minimum(self.Detailed.ParamPlot_1.distribution(x),
                              self.Detailed.ParamPlot_2.distribution(x))

        x_plot = np.linspace(self.PlBel_plot_s.xMin,
                             self.PlBel_plot_s.xMax,
                             self.PlBel_plot_s.num)
        t_plot = codistribution(x_plot)
        self.PlBel_plot_s.pl_grid = t_plot/np.max(t_plot)
        self.PlBel_plot_s.bel_grid = self.PlBel_plot_s.theta(
                                                self.PlBel_plot_s.pl_grid)
        self.PlBel_plot_s.plotInterpolation()

    def next_step(self):
        """
        открытие окна для следующего шага моделирования
        """
        self.number_of_steps
        y = self.Model_plot.err_y
        x = self.Model_plot.x
        try:
            if self.NextSplineModel is None:
                self.NextSplineModel = Ui_SplineWidget()
                self.NextSplineModel.x = x
                self.NextSplineModel.y = y
                self.NextSplineModel.Model_plot.ChangeData(x, y)
                self.NextSplineModel.number_of_steps = self.number_of_steps + 1
                self.NextSplineModel.setWindowTitle(
                                        "Spline Model, step: %d"
                                        % self.NextSplineModel.number_of_steps)
                self.NextSplineModel.s_box.setValue(self.s_box.value())
                self.NextSplineModel.k_box.setValue(self.k_box.value())
                self.NextSplineModel.show()
            else:
                # self.NextSplineModel.x = x
                # self.NextSplineModel.y = y
                # self.NextSplineModel.Model_plot.ChangeData(x, y)
                # self.NextSplineModel.s_box.setValue(self.s_box.value())
                # self.NextSplineModel.k_box.setValue(self.k_box.value())
                self.NextSplineModel.show()
        except AttributeError:
            print("AttributeError in next step method")

    def show_result(self):
        if self.number_of_steps == 0:
            x = self.Model_plot.x_plot
            y = self.Model_plot.y_plot
            win = self.NextSplineModel
            while win is not None:
                y += win.Model_plot.y_plot
                win = win.NextSplineModel
            self.windowResult = pg.plot(x, y)
            self.windowResult.setBackground('w')
            self.windowResult.show()
        else:
            pass

    def save_dict(self):
        """
        It method make dict of spline model's data
        """
        self.switchPlBel_s(self.k_box.value())
        data = {"pointsPlBel_s": self.pointsPlBel_s,
                "number_of_steps": self.number_of_steps,
                "x": self.x,
                "y": self.y,
                "s": self.s_box.value(),
                "k": self.k_box.value(),
                "example_model": self.example_model,
                "Detailed": {"x_1": self.Detailed.ParamPlot_1.points_x,
                             "t_1": self.Detailed.ParamPlot_1.points_t,
                             "x_2": self.Detailed.ParamPlot_2.points_x,
                             "t_2": self.Detailed.ParamPlot_2.points_t
                             },
                "k_points": {"x": self.PlBel_plot_k.points_x,
                             "t": self.PlBel_plot_k.points_t
                             }
                }
        try:
            if self.NextSplineModel is not None:
                data["NextSplineModel"] = self.NextSplineModel.save_dict()
            else:
                print("It's last step %d" % self.number_of_steps)
        except AttributeError:
            print("Something went wrong")
        return data

    def save_model(self):
        """
        It saves model's data
        """
        data = self.save_dict()
        print(data)
        try:
            fname = QtWidgets.QFileDialog.getSaveFileName(
                         QtWidgets.QWidget(), "Save file", filter="*.pickle")
            with open(fname[0], 'wb') as save_file:
                dill.dump(data, save_file)
        except (FileNotFoundError, FileExistsError):
            print("File is not selected")

    def load_dict(self, new_data):
        """
        It method load dict of spline model's data
        """
        try:
            self.pointsPlBel_s = new_data["pointsPlBel_s"]
            self.x = new_data["x"]
            self.y = new_data["y"]
            self.k_box.setValue(new_data["k"])
            self.s_box.setValue(new_data["s"])
            self.number_of_steps = new_data["number_of_steps"]
            self.example_model = new_data["example_model"]
            self.PlBel_plot_k.points_x = new_data["k_points"]["x"]
            self.PlBel_plot_k.points_t = new_data["k_points"]["t"]
            self.Detailed.ParamPlot_1.points_x = new_data["Detailed"]["x_1"]
            self.Detailed.ParamPlot_1.points_t = new_data["Detailed"]["t_1"]
            self.Detailed.ParamPlot_2.points_x = new_data["Detailed"]["x_2"]
            self.Detailed.ParamPlot_2.points_t = new_data["Detailed"]["t_2"]
            self.PlBel_plot_k.recalcInterpolation()
            self.PlBel_plot_k.plotInterpolation()
            self.PlBel_plot_s.recalcInterpolation()
            self.PlBel_plot_s.plotInterpolation()
            self.Detailed.ParamPlot_1.recalcInterpolation()
            self.Detailed.ParamPlot_1.plotInterpolation()
            self.Detailed.ParamPlot_2.recalcInterpolation()
            self.Detailed.ParamPlot_2.plotInterpolation()
            self.Model_plot.ChangeData(self.x, self.y)
            self.windowTrueData.ChangeData(self.x, self.y)
            self.switchPlBel_s(self.k_box.value())
        except KeyError:
            print("There is wrong file, it's not a subjective model's data")
        try:
            next_step_data = new_data["NextSplineModel"]
            if self.NextSplineModel is not None:
                self.NextSplineModel.load_dict(next_step_data)
            else:
                self.NextSplineModel = Ui_SplineWidget()
                self.NextSplineModel.load_dict(next_step_data)
                self.NextSplineModel.setWindowTitle(
                                        "Spline Model, step: %d"
                                        % self.NextSplineModel.number_of_steps)
        except KeyError:
            print("There is no more steps. It's last %d"
                  % self.number_of_steps)

    def load_model(self):
        """
        It's load model's data from file
        """
        fname = QtWidgets.QFileDialog.getOpenFileName(
                     QtWidgets.QWidget(), "Open file", filter="*.pickle")
        try:
            with open(fname[0], 'rb') as load_file:
                new_data = dill.load(load_file)
            self.load_dict(new_data)
        except (FileNotFoundError, FileExistsError):
            print("File was not loaded")

    def retranslateUi(self,):
        _translate = QtCore.QCoreApplication.translate
        self.s_label.setText(_translate("SplineWidget", "s:"))
        self.spline_model_label.setText(_translate("SplineWidget",
                                                   "Spline Model"))
        self.alpha_label.setText(_translate("SplineWidget", "a:"))
        self.pl_bel_label.setText(_translate("SplineWidget",
                                             "Plausibility and Belief"))
        self.save_model_button.setText(_translate("SplineWidget",
                                                  "Save Model "))
        self.load_data_button.setText(_translate("SplineWidget",
                                                 "Load Data"))
        self.num_label.setText(_translate("SplineWidget", "Number of steps:"))
        self.load_model_button.setText(_translate("SplineWidget",
                                                  "Load Model"))
        self.max_s_label.setText(_translate("SplineWidget", "max s:"))
        self.min_s_label.setText(_translate("SplineWidget", "min s:"))
        self.data_plot_button.setText(_translate("SplineWidget", "Data Plot"))
        self.k_label.setText(_translate("SplineWidget", "k:"))
        self.two_param_check.setText(_translate("SplineWidget",
                                                "detailed"))
        self.options_button.setText(_translate("SplineWidget",
                                               "Show result"))
        self.next_step_button.setText(_translate("SplineWidget",
                                                 "Next Step"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_SplineWidget()
    window.show()
    sys.exit(app.exec_())
