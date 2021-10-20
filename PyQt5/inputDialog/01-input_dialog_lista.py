from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inputDialog/01-input_dialog.ui", self)
        self.btn_ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        
        item = ['Rojo', 'Azul', 'Verde']
        item, ok = QInputDialog.getItem(self, 'Ingresar', 'Elija un item', item, 1, False)
        if ok:
            self.entrada.setText(item)


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



