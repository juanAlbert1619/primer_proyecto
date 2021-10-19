from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("checkBox/ejercicio01.ui", self)
        self.btn_calcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        subtotal = 0

        if self.chbox_jamon.isChecked():
           subtotal = (20)
        if self.chbox_tomates.isChecked():
            subtotal = subtotal + (50)
        if self.chbox_huevos.isChecked():
            subtotal = subtotal + (10)
        subtotal = "$ " + str(subtotal)
        self.lbl_consumoFinal.setText(subtotal)


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



