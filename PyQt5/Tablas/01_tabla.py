from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01_Tabla.ui", self)
        # crear las columnas
        self.tabla.setColumnCount(3)
         
        # Nombra las columnas
        self.tabla.setHorizontalHeaderLabels(('Nonbre', 'Apellido', 'e-mail'))


        # Agregar fila en blanco
       
        self.tabla.insertRow(0)
        self.tabla.insertRow(1)
        

        # Agrega items de la fila
                        # fila- column- item
        self.tabla.setItem( 0,  0, QTableWidgetItem('Pepe'))
        self.tabla.setItem(0, 1, QTableWidgetItem('Sanchez'))
        self.tabla.setItem(0, 2, QTableWidgetItem('rj@gmail.com'))
        self.tabla.setItem( 1,  0, QTableWidgetItem('Reyes'))
        self.tabla.setItem(1, 1, QTableWidgetItem('Suaez'))
        self.tabla.setItem(1, 2, QTableWidgetItem('sm@gmail.com'))
       









app = QApplication([])
win = MiVentana()
win.show()

app.exec_()