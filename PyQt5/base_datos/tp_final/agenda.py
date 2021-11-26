from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QInputDialog
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('00-agenda_completa.ui', self)

        conexion = sqlite3.connect('contactos.db')
        cursor = conexion.cursor()

        cursor.execute('select nombre, apellido, email, telefono, direccion, fechaNac,  altura, peso from contactos')
        filas = cursor.fetchall()

        self.lista.clear()


        for fila in filas:
           self.lista.addItem(f'nombre: {fila[0]} apellido: {fila[1]} email: {fila[2]} telefono: {fila[3]} direccion: {fila[4]} fechaNac {fila[5]}  altura: {fila[6]} peso: {fila[7]}')

        #conectar la base de datos
        self.conexion = sqlite3.connect('contactos.db')
        self.cursor = self.conexion.cursor()

        
       
       
        self.btn_nuevo.clicked.connect(self.on_nuevo_reg)
        #self.btn_editar.clicked.connect(self.on_editar_reg)
        #self.btn_eliminar.clicked.connect(self.on_eliminar_reg)
        self.btn_aceptar.clicked.connect(self.on_aceptar_reg)
        #self.btn_cancelar.clicked.connect(self.on_cancelar_reg)

    def on_aceptar_reg(self):

        self.conexion = sqlite3.connect('contactos.db')
        self.cursor = self.conexion.cursor()

    # Botones habilitados

        self.btn_nuevo.setEnabled(True)
        self.btn_editar.setEnabled(True)
        self.btn_eliminar.setEnabled(True)
        self.btn_aceptar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)


        self.nombre.setText("")
        self.nombre.setEnabled(False)
        self.apellido.setText("")
        self.apellido.setEnabled(False)
        self.email.setText("")
        self.email.setEnabled(False)
        self.telefono.setText("")
        self.telefono.setEnabled(False)
        self.direccion.setText("")
        self.direccion.setEnabled(False)
        self.fechaNac.setText("")
        self.fechaNac.setEnabled(False)
        self.altura.setText("")
        self.altura.setEnabled(False)
        self.peso.setText("")
        self.peso.setEnabled(False)

    # Datos

        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        telefono = self.telefono.text()
        direccion = self.direccion.text()
        fechaNac = self.fechaNac.text()
        altura = self.altura.text()
        peso = self.peso.text()
        self.lista.addItem(str('Nombre: '+ nombre +   ' -    Apellido: ' +   apellido +   ' -  email: '  +   email +   ' -  Telefono: '   +   telefono +   ' -  Direccion: '   +   direccion +   ' -  Fecha Nac.: '   +   fechaNac +   ' -  Altura: '   +   altura +   ' -  Peso: '   +   peso))

  
        
        self.nombre = self.nombre.text()
        self.apellido = self.apellido.text()
        self.email = self.email.text()
        self.telefono = self.telefono.text()
        self.direccion = self.direccion.text()
        self.fechaNac = self.fechaNac.text()
        self.altura = self.altura.text()
        self.peso = self.peso.text()
        self.registros = (self.nombre, self.apellido,  self.email, self.telefono, self.direccion, self.fechaNac,  self.altura, self.peso)


    # Insertar los datos en la tabla de campos
        self.cursor.execute("INSERT INTO contactos (nombre, apellido, email, telefono, direccion, fechaNac,  altura, peso) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", self.registros)
        self.conexion.commit()
        
        #conexion.commit()

        self.conexion.close()

       
    def on_nuevo_reg(self): 

        
       
        self.btn_nuevo.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_cancelar.setEnabled(True)

        self.nombre.setText("")
        self.nombre.setDisabled(False)
        self.apellido.setText("")
        self.apellido.setDisabled(False)
        self.email.setText("")
        self.email.setDisabled(False)
        self.telefono.setText("")
        self.telefono.setDisabled(False)
        self.direccion.setText("")
        self.direccion.setDisabled(False)
        self.fechaNac.setText("")
        self.fechaNac.setDisabled(False)
        self.altura.setText("")
        self.altura.setDisabled(False)
        self.peso.setText("")
        self.peso.setDisabled(False)

        

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

        

    def on_eliminar_reg(self):

       
        self.conexion = sqlite3.connect('contactos.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute("DELETE FROM contactos  WHERE id = " + self.id_contacto)
        self.conexion.commit()
        self.lista.clear()
        self.cursor = self.conexion.cursor()
        self.cursor.execute('select * from contactos')

       
        
        

    # def on_cancelar_reg(self): 
    #      pass  
    
    
    # def closeEvent(self, event):
    #     self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()