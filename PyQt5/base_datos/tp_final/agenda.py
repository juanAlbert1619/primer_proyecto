from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QInputDialog
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('00-agenda_completa.ui', self)

        #conectar la base de datos
        self.conexion = sqlite3.connect('00-basee.db')
        self.cursor = self.conexion.cursor()
       
       
        self.btn_nuevo.clicked.connect(self.on_nuevo_reg)
        #self.btn_editar.clicked.connect(self.on_editar_reg)
        #self.btn_eliminar.clicked.connect(self.on_eliminar_reg)
        #self.btn_aceptar.clicked.connect(self.on_aceptar_reg)
        #self.btn_cancelar.clicked.connect(self.on_cancelar_reg)

    # def on_cargar(self):
    #     self.cursor.execute('select * from usuarios')
    #     usuarios = self.cursor.fetchall()

        


    def on_nuevo_reg(self): 

       
        self.nombre.setText("")
        self.apellido.setText("")
        self.email.setText("")
        self.telefono.setText("")
        self.direccion.setText("")
        self.fechaNac.setText("")
        self.altura.setText("")
        self.peso.setText("")

        self.nuevo.setEnabled(False)


    # def on_editar_reg(self): 
    #      pass  

    # def on_aceptar_reg(self): 
    #     self.conexion = sqlite3.connect('00-basee.db')
    #     self.cursor = self.conexion.cursor() 

    # #Datos
    #     self.nombre = str(self.nombre.text())
    #     self.apellido = str(self.apellido.text())
    #     self.email = str(self.email.text())
    #     self.telefono= str(self.telefono.text())
    #     self.direccion= str(self.direccion.text())
    #     self.fechaNac= str(self.fechaNac.text())
    #     self.altura= str(self.altura.text())
    #     self.peso = str(self.peso.text())
    #     self.registroDatos = (self.nombre, self.apellido, self.email, self.telefono, self.direccion, self.fechaNac, self.altura, self.peso)

    # #Insertamos los datos en una tabla de campos
    #     self.curso.execute('INSER INTO campos (nombre, apellido, email, telefono, direccion, fechaNac, altura, peso) VALUE(?, ?, ?, ?, ?, ?, ?, ?)', self.registroDatos)
    #     self.conexion.commit()

    #     self.conexion.close()

        

    # def on_eliminar_reg(self): 
    #     self.cursorEliminar = conexion.cursor()
    #     consulta = 'delete from contactos where nombre = ?'

    #     cursorEliminar.execute(consulta,'')
    #     cursorEliminar.commit()
    #     cursorEliminar.close
        

    # def on_cancelar_reg(self): 
    #      pass  
    
    
    # def closeEvent(self, event):
    #     self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()