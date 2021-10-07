from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/lista.ui",self)
        self.lista.itemClicked.connect(self.on_item_clicked)

    def on_item_changed(self, actual, anterior):
        self.etiqueta.setText(actual.Text)