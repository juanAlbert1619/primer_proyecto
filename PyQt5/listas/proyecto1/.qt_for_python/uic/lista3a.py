# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Usuario\Desktop\primer_proyecto\PyQt5\listas\proyecto1\lista3a.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_nombreitem = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_nombreitem.setObjectName("lb_nombreitem")
        self.horizontalLayout.addWidget(self.lb_nombreitem)
        self.nombre = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nombre.setObjectName("nombre")
        self.horizontalLayout.addWidget(self.nombre)
        self.btn_izq_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_izq_2.setObjectName("btn_izq_2")
        self.horizontalLayout.addWidget(self.btn_izq_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lista1 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lista1.setObjectName("lista1")
        self.horizontalLayout_4.addWidget(self.lista1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_izq = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_izq.setObjectName("btn_izq")
        self.verticalLayout_2.addWidget(self.btn_izq)
        self.regresar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.regresar.setObjectName("regresar")
        self.verticalLayout_2.addWidget(self.regresar)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.lista2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lista2.setObjectName("lista2")
        self.horizontalLayout_4.addWidget(self.lista2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editar.setObjectName("editar")
        self.horizontalLayout_2.addWidget(self.editar)
        self.eliminar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout_2.addWidget(self.eliminar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_nombreitem.setText(_translate("MainWindow", "Nombre Item"))
        self.btn_izq_2.setText(_translate("MainWindow", "Agregar"))
        self.btn_izq.setText(_translate("MainWindow", ">>"))
        self.regresar.setText(_translate("MainWindow", "<<"))
        self.editar.setText(_translate("MainWindow", "Editar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
