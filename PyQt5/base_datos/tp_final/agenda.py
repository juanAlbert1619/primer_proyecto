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
        self.nuevo.clicked.connect(self.on_nuevo_reg)
        self.btn_editar.clicked.connect(self.on_editar_reg)
        self.btn_guardar.clicked.connect(self.on_guardar_reg)
        self.btn_eliminar.clicked.connect(self.on_eliminar_reg)

    def on_cargar(self):
        self.cursor.execute('select * from usuarios')
        usuarios = self.cursor.fetchall()

        


    def on_nuevo_reg(self): 

        self.lista.addItem(self.nombre.text())
        self.nombre.setText("")
        self.lista.addItem(self.apellido.text())
        self.apellido.setText("")
        self.lista.addItem(self.email.text())
        self.email.setText("")
        self.lista.addItem(self.telefono.text())
        self.telefono.setText("")
        self.lista.addItem(self.direccion.text())
        self.direccion.setText("")
        self.lista.addItem(self.fechaNac.text())
        self.fechaNac.setText("")
        self.lista.addItem(self.altura.text())
        self.altura.setText("")
        self.lista.addItem(self.peso.text())
        self.peso.setText("")


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