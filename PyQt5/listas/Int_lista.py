from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto1/lista_lista.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.btn_derecha.clicked.connect(self.on_boton_derecha)

    def on_agregar(self):
        self.lista_izq.addItem(self.nombre.text())
        self.nombre.setText("")

    def on_boton_derecha(self):
        self.lista_derecha.addItem(self.lista_izq.text())
        self.lista_izq.takeItem("")





app = QApplication([])
win = MiVentana()
win.show()

app.exec_()