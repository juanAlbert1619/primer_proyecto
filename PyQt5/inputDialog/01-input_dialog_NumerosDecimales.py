from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01-input_dialog.ui", self)
        self.btn_ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        # Ingresar un texto          Nombre de la ventana -                    numPorDefecto  min  max  decimales
        decimal, ok = QInputDialog.getInt(self, 'Ingresar', 'Ingresa un numero decimal', 1.5 , 0, 100 , 3)
        if ok:
            self.entrada.setText(str(decimal))


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



