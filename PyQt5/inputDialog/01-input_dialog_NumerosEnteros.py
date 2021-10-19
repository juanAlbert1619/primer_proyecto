from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inputDialog/01-input_dialog.ui", self)
        self.btn_ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        # Ingresar un texto          Nombre de la ventana - Texto que aparece sobre el line Edit - numMinimo, numMax, incrementa de 2 en 2
        entero, ok = QInputDialog.getInt(self, 'Ingresar', 'Ingresa un numero entero', value=5, min = 0, max=100, step=2)
        if ok:
            self.entrada.setText(str(entero))


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



