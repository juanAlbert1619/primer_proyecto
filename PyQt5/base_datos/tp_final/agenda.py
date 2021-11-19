from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QInputDialog
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tp_final/00-agenda_completa.ui', self)

        #conectar la base de datos
        self.conexion = sqlite3.connect('00-basee.db')
        self.cursor = self.conexion.cursor()

        #Crea las Columnas
        self.tabla.setColumnCount(4)

        #Nombrar las Columnas
        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail', 'Telefono', 'Direccion', 'Fecha Nacimiento', 'Altura', 'Peso'))

        self.nuevo.clicked.connect(self.on_nuevo_reg)
        self.btn_editar.clicked.connect(self.on_editar_reg)
        self.btn_guardar.clicked.connect(self.on_guardar_reg)
        self.btn_eliminar.clicked.connect(self.on_eliminar_reg)

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
            self.tabla.setItem(fila, 4, QTableWidgetItem(usuario[4]))
            self.tabla.setItem(fila, 5, QTableWidgetItem(usuario[5]))
            self.tabla.setItem(fila, 6, QTableWidgetItem(usuario[6]))
            self.tabla.setItem(fila, 7, QTableWidgetItem(usuario[7]))
            self.tabla.setItem(fila, 8, QTableWidgetItem(usuario[8]))


    def on_nuevo_reg(self): 
         pass  

    def on_editar_reg(self): 
         pass  

    def on_guardar_reg(self): 
         pass  

    def on_eliminar_reg(self): 
         pass  
    
    
    def closeEvent(self, event):
        self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()