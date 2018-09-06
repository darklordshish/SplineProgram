# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlBel.ui'
#
# Created: Wed Mar  9 08:24:22 2016
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import importlib as im
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np

from scipy.optimize import brentq

import dill as pickle
from PlBelPlot import PlBelPlot

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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(851, 674)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(False)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.ParamPlBel = PlBelPlot(Form)
        self.ParamPlBel.setGeometry(QtCore.QRect(0, 10, 381, 281))

        self.ResPlBel = PlBelPlot(Form)
        self.ResPlBel.setGeometry(QtCore.QRect(470, 10, 381, 281))
        self.ResPlBel.ResPlot = True

        self.convertButton = QtGui.QPushButton(Form)
        self.convertButton.setGeometry(QtCore.QRect(400, 20, 51, 31))

        self.loadButton = QtGui.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(540, 300, 121, 25))

        self.FunctionPlot = PlotWidget(Form)
        self.FunctionPlot.setGeometry(QtCore.QRect(0, 340, 851, 331))
        self.FunctionPlot.setObjectName(_fromUtf8("FunctionPlot"))
        self.FunctionPlot.function_curve_plot = pg.PlotCurveItem()
        self.FunctionPlot.function_curve_plot.setPen((5, 6))
        self.FunctionPlot.addItem(self.FunctionPlot.function_curve_plot)

        self.spline_degree = QtGui.QSpinBox(Form)
        self.spline_degree.setGeometry(QtCore.QRect(90, 310, 55, 24))
        self.spline_degree.setMinimum(1)
        self.spline_degree.setMaximum(5)

        self.label_k = QtGui.QLabel(Form)
        self.label_k.setGeometry(QtCore.QRect(70, 300, 16, 16))

        self.steps = QtGui.QSpinBox(Form)
        self.steps.setGeometry(QtCore.QRect(790, 300, 55, 24))
        self.steps.setMinimum(100)
        self.steps.setMaximum(5000)
        self.steps.setProperty("value", 400)

        self.label_steps = QtGui.QLabel(Form)
        self.label_steps.setGeometry(QtCore.QRect(680, 300, 111, 31))

        self.x_min = QtGui.QDoubleSpinBox(Form)
        self.x_min.setGeometry(QtCore.QRect(190, 310, 62, 24))
        self.x_min.setProperty("value", self.ParamPlBel.xMin)
        self.x_min.setMinimum(-100000.0)
        self.x_min.setMaximum(100000.0)
        self.x_min.setProperty("value", self.ParamPlBel.xMin)

        self.x_max = QtGui.QDoubleSpinBox(Form)
        self.x_max.setGeometry(QtCore.QRect(310, 310, 62, 24))
        self.x_max.setProperty("value", self.ParamPlBel.xMax)
        self.x_max.setMinimum(-100000.0)
        self.x_max.setMaximum(100000.0)
        self.x_max.setProperty("value", self.ParamPlBel.xMax)

        self.label_x_min = QtGui.QLabel(Form)
        self.label_x_min.setGeometry(QtCore.QRect(150, 300, 41, 16))

        self.label_xmax = QtGui.QLabel(Form)
        self.label_xmax.setGeometry(QtCore.QRect(260, 300, 41, 16))

        self.clear_PlBel_res = QtGui.QPushButton(Form)
        self.clear_PlBel_res.setGeometry(QtCore.QRect(480, 300, 51, 25))

        self.clear_PlBel_param = QtGui.QPushButton(Form)
        self.clear_PlBel_param.setGeometry(QtCore.QRect(10, 300, 51, 25))

        self.ParamToRes = QtGui.QRadioButton(Form)
        self.ParamToRes.setGeometry(QtCore.QRect(400, 70, 51, 20))
        self.ParamToRes.setCheckable(True)
        self.ParamToRes.setChecked(True)

        self.ResToParam = QtGui.QRadioButton(Form)
        self.ResToParam.setGeometry(QtCore.QRect(400, 100, 51, 20))
        self.ResToParam.setChecked(False)

        self.SaveButton = QtGui.QPushButton(Form)
        self.SaveButton.setGeometry(QtCore.QRect(400, 260, 51, 25))

        self.LoadButton = QtGui.QPushButton(Form)
        self.LoadButton.setGeometry(QtCore.QRect(400, 230, 51, 25))

        self.f_module = None
        self.num = 400
        self.PlotFunction()

        self.convertButton.clicked.connect(self.ConvertPlBel)
        self.loadButton.clicked.connect(self.changing_function)
        self.SaveButton.clicked.connect(self.save_model)
        self.LoadButton.clicked.connect(self.load_model)
        self.clear_PlBel_param.clicked.connect(self.ClearParamPlBel)
        self.clear_PlBel_res.clicked.connect(self.ClearResPlBel)
        self.spline_degree.valueChanged[int].connect(self.ParamPlBel.changeK)
        self.spline_degree.valueChanged[int].connect(self.ResPlBel.changeK)
        self.x_min.valueChanged[float].connect(self.ParamPlBel.changeXmin)
        self.x_max.valueChanged[float].connect(self.ParamPlBel.changeXmax)
        self.steps.valueChanged[int].connect(self.changeNum)

        self.retranslateUi(Form)

    @staticmethod
    def f(x):
        """
        функция,для значений которой мы расчитываем правдоподобие и доверие
        """
        return x/(x + 1)*np.exp(-1.58*x/(x + 1))  # np.sin(2*x)*(x**2-5*x+2)

    def PlotFunction(self):
        x_grid = np.linspace(self.ParamPlBel.xMin,
                             self.ParamPlBel.xMax,
                             self.num)
        y_grid = self.f(x_grid)
        self.FunctionPlot.function_curve_plot.setData(x_grid, y_grid)

    def changeNum(self, num):
        if num >= 100 and num <= 5000:
            self.num = num
            self.ParamPlBel.changeNum(num)
            self.ResPlBel.changeNum(num)

    def ClearParamPlBel(self):
        self.ParamPlBel.pl_grid = np.ones(self.ResPlBel.num)
        self.ParamPlBel.bel_grid = np.zeros(self.ResPlBel.num)
        self.ParamPlBel.points_x = np.array([])
        self.ParamPlBel.points_t = np.array([])
        self.ParamPlBel.pointsPlot.clear()
        self.ParamPlBel.distributionPlPlot.clear()
        self.ParamPlBel.distributionBelPlot.clear()
        self.ParamPlBel.distribution = lambda x: np.ones_like(x)
        self.ParamPlBel.plotInterpolation()

    def ClearResPlBel(self):
        self.ResPlBel.pl_grid = np.ones(self.ResPlBel.num)
        self.ResPlBel.bel_grid = np.zeros(self.ResPlBel.num)
        self.ResPlBel.points_x = np.array([])
        self.ResPlBel.points_t = np.array([])
        self.ResPlBel.distributionPlPlot.clear()
        self.ResPlBel.distributionBelPlot.clear()
        self.ResPlBel.distribution = lambda x: np.ones_like(x)
        self.ResPlBel.plotInterpolation()

    def changing_function(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
                     QtWidgets.QWidget(), "Open file")
        # создаём диалог выбора файла,
        # на выходе имеем имя файла
        print(fname)
        # пробуем поменять функцию собственную f(.) на функцию f(.) из файла,
        # возвращённого диалоговым окном выбора файла
        try:
            fn = load_module_by_path(fname[0])
            self.f = fn.f  # собственно, меняем
            self.f_module = fname
        except (ValueError('Is it function?'), TypeError('May be not?'),
                SyntaxError, NameError, AttributeError):
            # если не получилось поменять и выскочила ошибка
            print("function f(x) not found!")
            # пишем в консоли, что функция
            # f(.) не найдена
        self.PlotFunction()
        self.ConvertPlBel()

    def save_model(self):
        data = {"function": self.f,
                "alpha": self.ParamPlBel.alpha,
                "ParamDistribution": [self.ParamPlBel.points_x,
                                      self.ParamPlBel.points_t],
                "ResDistribution": [self.ResPlBel.points_x,
                                    self.ResPlBel.points_t],
                "Spline": [self.ParamPlBel.k, self.ParamPlBel.s],
                "minX": self.ParamPlBel.xMin,
                "maxX": self.ParamPlBel.xMax,
                "number_of_steps": self.num}
        print(data)
        fname = QtWidgets.QFileDialog.getOpenFileName(
                     QtWidgets.QWidget(), "Open file", filter="*.pickle")
        with open(fname[0] + "2", "wb") as save_file2:
            pickle.dump(self.f_module, save_file2)
        with open(fname[0], 'wb') as save_file:
            pickle.dump(data, save_file)

    def load_model(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
                     QtWidgets.QWidget(), "Open file", filter="*.pickle")
        with open(fname[0] + "2", "rb") as load_file2:
            _ = load_module_by_path(pickle.load(load_file2))
        with open(fname[0], 'rb') as load_file:
            new_data = pickle.load(load_file)
        self.f = new_data['function']
        self.ParamPlBel.alpha = new_data['alpha']
        self.ResPlBel.alpha = new_data['alpha']
        self.num = new_data['number_of_steps']
        self.ParamPlBel.num = new_data['number_of_steps']
        self.ResPlBel.num = new_data['number_of_steps']
        self.ParamPlBel.points_x = new_data['ParamDistribution'][0]
        self.ParamPlBel.points_t = new_data['ParamDistribution'][1]
        self.ResPlBel.points_x = new_data['ResDistribution'][0]
        self.ResPlBel.points_t = new_data['ResDistribution'][1]
        self.ParamPlBel.k = new_data['Spline'][0]
        self.ParamPlBel.s = new_data['Spline'][1]
        self.ResPlBel.k = new_data['Spline'][0]
        self.ResPlBel.s = new_data['Spline'][1]
        self.ParamPlBel.xMin = new_data['minX']
        self.ParamPlBel.xMax = new_data['maxX']
        self.ParamPlBel.pointsPlot.setData(self.ParamPlBel.points_x,
                                           self.ParamPlBel.points_t)
        self.ResPlBel.pointsPlot.setData(self.ResPlBel.points_x,
                                         self.ResPlBel.points_t)
        self.ConvertPlBel()
        self.PlotFunction()

    def ConvertPlBel(self):
        if self.ParamToRes.isChecked() is True:
            self.SetParamToRes()
            self.ResPlBelPlot()
        elif self.ResToParam.isChecked() is True:
            self.SetResToParam()
            self.ParPlBelPlot()

    def ResPlBelPlot(self):
        """
        посчитаем распределение правдоподобия и доверия значений функции f(x)
        """
        # построим сетку на области
        # определения функции
        x_grid = np.linspace(self.ParamPlBel.xMin,
                             self.ParamPlBel.xMax,
                             self.num)
        # вычислим значения функции в точках сетки
        y = self.f(x_grid)
        # установим для расчёта распределения
        # правдоподобия и доверия значений функции
        self.ResPlBel.xMin = np.min(y)
        # максимальное и минимальное значения
        # из вычисленных на сетке параметра х
        self.ResPlBel.xMax = np.max(y)
        # построим сетку в области
        # значений функции
        y_iterate = np.linspace(self.ResPlBel.xMin,
                                self.ResPlBel.xMax,
                                self.num)
        # обновим распределение правдоподобия
        self.ResPlBel.pl_grid = np.array([])
        # и доверия
        self.ResPlBel.bel_grid = np.array([])
        # начнём вычисления
        for j in range(self.num):
            """
            найдём для каждого y из все х, которые его доставляют, построим
            новую функцию g(x) и будем искать её корни
            """
            g = lambda x: self.f(x) - y_iterate[j]
            roots = g(x_grid)  # сетка значений новой функции g(x)
            sign_roots = np.sign(roots)  # знаки значений функции
            x_pos = np.array([])  # создадим массив корней функции g(x)
            for i in range(self.num-1):
                k = 0  # счётчик позиции для вставки найденного корня
                # если знак значений функции на концах интервала разный,
                # значит на нём есть корень, хотя бы один
                if sign_roots[i]+sign_roots[i+1] == 0:
                    x0 = brentq(g, x_grid[i], x_grid[i + 1])  # найдём корень
                    # вставим корень в массив
                    # корней на позицию k
                    x_pos = np.insert(x_pos, k, x0)
                    k = k + 1  # увеличим счётчик корней на один
            if np.size(x_pos) == 0:  # если корней нет, то
                # правдоподобие значения y_iterate[j] равно нулю
                self.ResPlBel.pl_grid = np.append(self.ResPlBel.pl_grid, 0.0)
                # а доверие  единице
                self.ResPlBel.bel_grid = np.append(self.ResPlBel.bel_grid,
                                                   self.ParamPlBel.theta(0.0))
            else:  # если корни есть, тогда
                self.ResPlBel.pl_grid = np.append(
                    self.ResPlBel.pl_grid,
                    np.max(self.ParamPlBel.distribution(x_pos)))
                # находим из корней тот, правдоподобие которого
                # максимально и приравниваем его правдоподобие
                # правдоподобию соответствующего значения функции
                self.ResPlBel.bel_grid = np.append(
                    self.ResPlBel.bel_grid,
                    np.min(
                        self.ParamPlBel.theta(
                            self.ParamPlBel.distribution(x_pos))))
                # находим из корней тот, доверие которого
                # минимально и приравниваем его доверие доверию
                # соостветствующего значения функции
        self.ResPlBel.plotInterpolation()  # рисуем

    def ParPlBelPlot(self):
        x_grid = np.linspace(self.ParamPlBel.xMin,
                             self.ParamPlBel.xMax,
                             self.num)
        y = self.f(x_grid)
        self.ResPlBel.xMin = np.min(y)
        self.ResPlBel.xMax = np.max(y)
        self.ParamPlBel.pl_grid = self.ResPlBel.distribution(y)
        self.ParamPlBel.bel_grid = self.ResPlBel.theta(
                                                self.ResPlBel.distribution(y))
        self.ParamPlBel.plotInterpolation()

    def SetParamToRes(self):
        self.ParamPlBel.ResPlot = False
        self.ResPlBel.ResPlot = True

    def SetResToParam(self):
        self.ParamPlBel.ResPlot = True
        self.ResPlBel.ResPlot = False

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "PlBel", None))
        self.convertButton.setText(_translate("Form", "<=>", None))
        self.loadButton.setText(_translate("Form", "Load function", None))
        self.label_k.setText(_translate("Form", "k:", None))
        self.label_steps.setText(_translate("Form", "number of steps:", None))
        self.label_x_min.setText(_translate("Form", "X min:", None))
        self.label_xmax.setText(_translate("Form", "X max:", None))
        self.clear_PlBel_res.setText(_translate("Form", "Clear", None))
        self.ParamToRes.setText(_translate("Form", "=>", None))
        self.ResToParam.setText(_translate("Form", "<=", None))
        self.SaveButton.setText(_translate("Form", "Save", None))
        self.LoadButton.setText(_translate("Form", "Load", None))
        self.clear_PlBel_param.setText(_translate("Form", "Clear", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
