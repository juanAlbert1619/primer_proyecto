import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.boton_desactivar.setEnabled(False)
        self.boton_activar.clicked.connect(self.fn_activar)
        self.boton_desactivar.clicked.connect(self.fn_desactivar)

    def fn_activar(self):
        self.boton_desactivar.setEnabled(True)
        self.boton_activar.setEnabled(False)
        self.etiqueta.setText("ACTIVADO")

    def fn_desactivar(self):
        self.boton_desactivar.setEnabled(False)
        self.boton_activar.setEnabled(True)
        self.etiqueta.setText("DESACTIVADO")

  
        


app = QApplication([])
win = ejemplo_GUI()
win.show()
app.exec_()

