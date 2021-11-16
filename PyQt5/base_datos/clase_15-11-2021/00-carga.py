from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QInputDialog
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('00-cargar.ui', self)

        #conectar la base de datos
        self.conexion = sqlite3.connect('00-basee.db')
        self.cursor = self.conexion.cursor()

        #Crea las Columnas
        self.tabla.setColumnCount(4)

        #Nombrar las Columnas
        self.tabla.setHorizontalHeaderLabels(('id', 'Nombre', 'Apellido', 'e-mail'))

        self.btn_carga.clicked.connect(self.on_cargar)

    def on_cargar(self):
        self.cursor.execute('select * from usuarios')
        usuarios = self.cursor.fetchall()

        for usuario in usuarios:
            fila = usuarios.index(usuario) # lee el indice cero del arreglo
            self.tabla.insertRow(fila)
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(usuario[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem(usuario[1]))
            self.tabla.setItem(fila, 2, QTableWidgetItem(usuario[2]))
            self.tabla.setItem(fila, 3, QTableWidgetItem(usuario[3]))


       
    
    
    def closeEvent(self, event):
        self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()