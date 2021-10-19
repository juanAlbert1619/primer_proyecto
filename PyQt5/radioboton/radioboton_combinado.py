from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("radioboton/radioboton.ui", self)
        #self.aceptar.clicked.connect(self.on_aceptar)
        self.rb_opcion1.toggled.connect(self.on_aceptar)
        self.rb_opcion2.toggled.connect(self.on_aceptar)
        self.rb_opcion3.toggled.connect(self.on_aceptar)

    def on_aceptar(self):
        print("Cambio de opcion")
        if self.rb_opcion1.isChecked():
            self.mensaje.setText("Se elige la opcion 1")
        elif self.rb_opcion2.isChecked():
            self.mensaje.setText("Se elige la opcion 2")
        elif self.rb_opcion3.isChecked():
            self.mensaje.setText("Se elige la opcion 3")
        else:
            self.mensaje.setText("No se eligio opcion")

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()