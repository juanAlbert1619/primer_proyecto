# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Usuario\Desktop\primer_proyecto\PyQt5\checkBox\ejercicio01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.chbox_jamon = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_jamon.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.chbox_jamon.setObjectName("chbox_jamon")
        self.chbox_tomates = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_tomates.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.chbox_tomates.setObjectName("chbox_tomates")
        self.chbox_huevos = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_huevos.setGeometry(QtCore.QRect(20, 110, 121, 21))
        self.chbox_huevos.setObjectName("chbox_huevos")
        self.precio_extra = QtWidgets.QLabel(self.centralwidget)
        self.precio_extra.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.precio_extra.setObjectName("precio_extra")
        self.btn_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(40, 180, 241, 41))
        self.btn_calcular.setObjectName("btn_calcular")
        self.lbl_consumoFinal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_consumoFinal.setGeometry(QtCore.QRect(150, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_consumoFinal.setFont(font)
        self.lbl_consumoFinal.setText("")
        self.lbl_consumoFinal.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_consumoFinal.setObjectName("lbl_consumoFinal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Elija extras:"))
        self.chbox_jamon.setText(_translate("MainWindow", "Jamon $20"))
        self.chbox_tomates.setText(_translate("MainWindow", "Tomate Asados $50"))
        self.chbox_huevos.setText(_translate("MainWindow", "Huevos $10"))
        self.precio_extra.setText(_translate("MainWindow", "Precio extras:"))
        self.btn_calcular.setText(_translate("MainWindow", "Calcular"))
