from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("RadioBoton/radioboton_combinado.ui", self)
        self.btn_aceptar.clicked.connect(self.on_aceptar)

        

    def on_aceptar(self, opcion_num):

        
        opcion_num = ""
        if self.num.op1.isChecked()== True:
            opcion_num = self.mensaje_uno.setText("Se eligie la opcion 1")
            self.mensaje_uno.setText(opcion_num)

        elif self.num.op2.isChecked()== True:
             opcion_num = self.mensaje_uno.setText("Se eligie la opcion 2")
             self.mensaje_uno.setText(opcion_num)
        
        elif self.num.op3.isChecked()== True:
             opcion_num = self.mensaje_uno.setText("Se eligie la opcion 3")
             self.mensaje_uno.setText(opcion_num)
        
        else:
             opcion_num = self.mensaje_uno.setText("No se eligio opcion")


    def on_aceptar(self):

        opcionletras = ""
        if self.rd_opcionA.isChecked()== True:
            opcionletras = self.mensaje_dos.setText("Se eligie la opcion A")
            self.mensaje_uno.setText(opcionletras)

        elif self.rd_opcionB.isChecked()== True:
            opcionletras = self.mensaje_dos.setText("Se eligie la opcion B")
            self.mensaje_uno.setText(opcionletras)
        
        elif self.rd_opcionC.isChecked()== True:
            opcionletras = self.mensaje_dos.setText("Se eligie la opcion C")
            self.mensaje_uno.setText(opcionletras)
        
        else:
            opcionletras = self.mensaje_dos.setText("No se eligio opcion")
            
    
    def on_aceptar(self, opcionletras, opcion_num ):

        self.mensaje_uno.setText(opcionletras + opcion_num )
        

    

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()