from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lista3a.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
      
    def on_agregar(self):
        self.lista1.addItem(self.nombre.text())
        self.nombre.setText('')

    # def on_eliminar(self):
    #    self.lista1.setText(self.lista.currentItem().text())
    #    self.lista2.addItem(self.lista1.currentItem().Text())
    #    self.lista1.setText('')

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



