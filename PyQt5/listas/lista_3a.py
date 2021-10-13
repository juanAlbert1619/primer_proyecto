from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto1/lista3a.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.btn_izq_clicked.connect(self.on_btn_izq)

        win.show()
       

    def on_agregar(self):
        self.lista1.addItem(self.nombre.text())
        self.nombre.setText('')

    def on_btn_izq(self):
       self.lista1.setText("Hello")

app = QApplication([])
win = MiVentana()


app.exec_()


