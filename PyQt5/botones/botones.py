from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('botones.ui', self)
        self.btn1.clicked.connect(self.on_boton1_clicked)
        self.btn2.clicked.connect(self.on_boton2_clicked)

    def on_boton1_clicked(self):
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(True)

    def on_boton2_clicked(self):
        self.btn2.setEnabled(False)
        self.btn1.setEnabled(True)

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()


