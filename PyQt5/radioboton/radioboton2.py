from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("RadioBoton/radioboton_combinado.ui", self)
        self.btn_aceptar.clicked.connect(self.on_aceptar)

    def on_aceptar(self):
        mensaje = ""

        if self.op1.isChecked():
            mensaje = "opcion1 \n "

        if self.op2.isChecked():
            mensaje = "opcion2 \n "

        if self.op3.isChecked():
            mensaje = "opcion3 \n "

        if self.rd_opcionA.isChecked():
            mensaje = mensaje + "opcion A \n "

        if self.rd_opcionB.isChecked():
            mensaje = mensaje + "opcion B \n "

        if self.rd_opcionC.isChecked():
            mensaje = mensaje + "opcion C \n "

        self.mensaje_dos.setText(mensaje)


    

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()