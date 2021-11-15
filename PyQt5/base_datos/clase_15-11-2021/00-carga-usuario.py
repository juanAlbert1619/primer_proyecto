from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QInputDialog
from PyQt5 import uic
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('00-carga_usuario.ui', self)

        #conectar la base de datos
        self.conexion = sqlite3.connect('00-carga_usuario.ui')
        self.cursor = self.conexion.cursor()

        #Crea las Columnas
        self.tabla.setColumnCount(4)

        #Nombrar las Columnas
        self.tabla.setHorizontalHeaderLabels(('id', 'Nombre', 'Apellido', 'e-mail'))

        self.btn_carga.clicked.connect(self.on_cargar)

    def on_cargar(self):
        self.cusor.execute('select * from usuarios')
        usuarios = self.cursor.fetchall()

        for usuario in usuarios:
            fila = usuarios.index(usuario)
            self.tabla.insertRow(fila)
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(usuario[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem(usuario[1]))
            self.tabla.setItem(fila, 2, QTableWidgetItem(usuario[2]))
            self.tabla.setItem(fila, 3, QTableWidgetItem(usuario[3]))


    def on_agregar(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()

        # Agrega Usuario
        self.cursor.execute("insert into usuarios (nombre,apellido,email) values ('{0} ','{1} ','{2}')".format(nombre, apellido,email))
        self.conexion.commit()

        #Vaciar y volver a cargar
        self.tabla.setRowCount(0)
        self.on_cargar()
    
    
    def closeEvent(self, event):
        self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()