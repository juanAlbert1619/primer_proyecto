import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
form PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Intercambio/appIntercambio, self")
        self.btnNombre.clicked.connect(self.on_btNombre)
        self.btnAgregar.clicked.connect(self.on_btAgregar)
        self.btnizquierda.clicked.connect(self.on_btIzquierda)
        self.btnDerecha.clicked.connect(self.on_btDerecha)
        self.btnEditar.clicked.connect(self.on_btEditar)
        self.btnEliminar.clicked.connect(self.on_btEliminar)

    def on_btnNombre(self):
        self.

      
