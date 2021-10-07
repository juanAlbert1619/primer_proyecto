from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto1/lista3a.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
       

      #  self.lista1.currentItemChanged.connect(self.on_item_changed)

       # self.show

   # def agregar(Self):
    #    lista1 = self.lista1.currentItemChanged()

    #    for lista1 in list(lista2):
    #        Self

    def on_agregar(self):
        self.lista1.addItem(self.nombre.text())
        self.nombre.setText('')

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



