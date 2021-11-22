

from sqlite3.dbapi2 import Cursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QInputDialog
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tp_final\00-agenda_completa.ui', self)

        #conectar la base de datos
        self.conexion = sqlite3.connect('contactos.db')
        self.cursor = self.conexion.cursor()

        
       
       
        self.btn_nuevo.clicked.connect(self.on_nuevo_reg)
        #self.btn_editar.clicked.connect(self.on_editar_reg)
        #self.btn_eliminar.clicked.connect(self.on_eliminar_reg)
        self.btn_aceptar.clicked.connect(self.on_aceptar_reg)
        #self.btn_cancelar.clicked.connect(self.on_cancelar_reg)

    def on_aceptar_reg(self):

        pass
       
    def on_nuevo_reg(self): 
       
        self.btn_nuevo.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_cancelar.setEnabled(True)

        self.nombre.setText("")
        self.nombre.setEnabled(True)
        self.apellido.setText("")
        self.apellido.setEnabled(True)
        self.email.setText("")
        self.email.setEnabled(True)
        self.telefono.setText("")
        self.telefono.setEnabled(True)
        self.direccion.setText("")
        self.direccion.setEnabled(True)
        self.fechaNac.setText("")
        self.fechaNac.setEnabled(True)
        self.altura.setText("")
        self.altura.setEnabled(True)
        self.peso.setText("")
        self.peso.setEnabled(True)

        

    # def on_editar_reg(self): 
    #      pass  

    

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
    #     self.curso.execute('INSER INTO contactos (nombre, apellido, email, telefono, direccion, fechaNac, altura, peso) VALUE(?, ?, ?, ?, ?, ?, ?, ?)', self.registroDatos)
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