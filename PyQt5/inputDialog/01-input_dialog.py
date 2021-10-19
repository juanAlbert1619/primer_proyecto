from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inputDialog/01-input_dialog.ui", self)
        self.btn_ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        # Ingresar un texto
        texto, ok = QInputDialog.getText(self, 'Ingresar', 'Ingresa un texto', text='Texto por defecto')
        if ok and texto:
            self.entrada.setText(texto)


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



