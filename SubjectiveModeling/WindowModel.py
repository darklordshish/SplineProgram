# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowModel.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from pyqtgraph.parametertree import Parameter, ParameterTree
from pyqtgraph.parametertree import ParameterItem, registerParameterType


class Ui_WindowModel(QWidget):
    """
    """
    def __init__(self,):
        super().__init__()
        self.setupUi()

    def setupUi(self, ):
        """
        """
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridGeneral = QtWidgets.QGridLayout()
        self.gridGeneral.setObjectName("gridGeneral")
        self.toolBox = QtWidgets.QToolBox(self)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toolBox.setObjectName("toolBox")
        self.model = QtWidgets.QWidget()
        self.model.setGeometry(QtCore.QRect(0, 0, 558, 451))
        self.model.setObjectName("model")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.model)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridModel = QtWidgets.QGridLayout()
        self.gridModel.setContentsMargins(5, 5, 5, 5)
        self.gridModel.setSpacing(5)
        self.gridModel.setObjectName("gridModel")
        self.line = QtWidgets.QFrame(self.model)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridModel.addWidget(self.line, 0, 1, 1, 1)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.model)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridModel.addWidget(self.openGLWidget, 0, 2, 1, 1)
        self.ModelDescriptionTree = ParameterTree(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.ModelDescriptionTree.sizePolicy().hasHeightForWidth())
        self.ModelDescriptionTree.setSizePolicy(sizePolicy)
        self.ModelDescriptionTree.setObjectName("ModelDescriptionTree")
        self.gridModel.addWidget(self.ModelDescriptionTree, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridModel, 0, 1, 1, 1)
        self.toolBox.addItem(self.model, "")
        self.param = QtWidgets.QWidget()
        self.param.setGeometry(QtCore.QRect(0, 0, 558, 451))
        self.param.setObjectName("param")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.param)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridParam = QtWidgets.QGridLayout()
        self.gridParam.setContentsMargins(5, 5, 5, 5)
        self.gridParam.setSpacing(5)
        self.gridParam.setObjectName("gridParam")
        self.ParametersTree = ParameterTree(self.param)
        self.ParametersTree.setObjectName("ParametersTree")
        self.gridParam.addWidget(self.ParametersTree, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridParam, 0, 0, 1, 1)
        self.toolBox.addItem(self.param, "")
        self.result = QtWidgets.QWidget()
        self.result.setObjectName("result")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.result)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridRes = QtWidgets.QGridLayout()
        self.gridRes.setContentsMargins(5, 5, 5, 5)
        self.gridRes.setSpacing(5)
        self.gridRes.setObjectName("gridRes")
        self.ResTree = ParameterTree(self.result)
        self.ResTree.setObjectName("ResTree")
        self.gridRes.addWidget(self.ResTree, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridRes, 0, 0, 1, 1)
        self.toolBox.addItem(self.result, "")
        self.gridGeneral.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridGeneral, 0, 0, 1, 1)

        self.retranslateUi(self)
        self.toolBox.setCurrentIndex(2)

    def retranslateUi(self, WindowModel):
        _translate = QtCore.QCoreApplication.translate
        self.toolBox.setItemText(self.toolBox.indexOf(self.model),
                 _translate("WindowModel",
                            "General information about the subjective model"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.param),
                 _translate("WindowModel",
                            "Detailed description of the parameters"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.result),
                 _translate("WindowModel",
                            "Detailed description of the resultes "))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_WindowModel()
    window.show()
    sys.exit(app.exec_())
