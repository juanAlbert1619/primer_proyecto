from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01_tabla_profe_matias.ui", self)
        # crear las columnas
        self.tabla.setColumnCount(3)
         
        # Nombra las columnas
        self.tabla.setHorizontalHeaderLabels(('Nonbre', 'Apellido', 'e-mail'))

        self.filas = 0
        self.btn_agregar.clicked.connect(self.on_agregar)

    def on_agregar(self):

        # Agregar fila en blanco
        fila = self.filas
        self.tabla.insertRow(fila)
    
        # Agrega items de la fila
        nombre = self.txt_nombre.text()
                        # fila- column- item
        self.tabla.setItem(fila,  0, QTableWidgetItem(nombre))
        self.txt_nombre.setText("")
        apellido = self.txt_apellido.text()
        self.tabla.setItem(0, 1, QTableWidgetItem(apellido))
        self.txt_apellido.setText("")
        email = self.txt_e_mail.text()
        self.tabla.setItem(0, 2, QTableWidgetItem(email))
        self.txt_e_mail.setText("")
       

        self.filas = self.filas + 1

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()