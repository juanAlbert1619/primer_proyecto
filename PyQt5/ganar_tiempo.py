from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("comboBox/01_combo_box.ui", self)
        self.combo.currentIndexChanged.connect(self.on_cambio)

    def on_cambio(self):
      

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



