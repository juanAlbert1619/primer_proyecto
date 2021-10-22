from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MessageBox/00-message_box.ui", self)
        self.btn_mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        msg = QMessageBox()
        msg.setWindowTitle('Titulo del mensaje')
        msg.setIcon()
        msg.exec_()
        


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



