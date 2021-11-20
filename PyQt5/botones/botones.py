from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadVi('botones.ui', self)
        self.boton1.clicked.connect(self.on_boton1_clicked)
        self.boton2.clicked.connect(self.on_boton2_clicked)

    def on_boton1_clicked(self):
        self.boton1.setEnabled(False)
        self.boton2.setEnabled(True)

    def on_boton2_clicked(self):
        self.boton2.setEnabled(False)
        self.boton1.setEnabled(True)

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()


