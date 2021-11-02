from os import close, name
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01_tabla_profe_matias.ui", self)
        # crear las columnas
        self.tabla.setColumnCount(3)
        self.tabla.setColumnWidth(0,100)
        self.tabla.setColumnWidth(1,100)
        self.tabla.setColumnWidth(2,150)
        self.btn_agregar.clicked.connect(self.on_agregar)
         
        # Nombra las columnas
        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail'))

    row = 0
    
    def on_agregar(self):
  
        self.tabla.insertRow(0)

        self.tabla.setItem( 0,  0, QTableWidgetItem(self.txt_nombre.text()))
        self.txt_nombre.setText("")
        self.tabla.setItem( 0,  1, QTableWidgetItem(self.txt_apellido.text()))
        self.txt_apellido.setText("")
        self.tabla.setItem( 0, 2, QTableWidgetItem(self.txt_e_mail.text()))
        self.txt_e_mail.setText("")

    row = row + 1
 
app = QApplication([])
win = MiVentana()
win.show()

app.exec_()