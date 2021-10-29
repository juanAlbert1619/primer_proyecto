from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("creaTabla.ui", self)









app = QApplication([])
win = MiVentana()
win.show()

app.exec_()