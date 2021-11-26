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

        self.tabla.clear()


        for fila in filas:
           self.tabla.addItem(f'nombre: {fila[0]} apellido: {fila[1]} email: {fila[2]} telefono: {fila[3]} direccion: {fila[4]} fechaNac {fila[5]}  altura: {fila[6]} peso: {fila[7]}')

        #conectar la base de datos
        self.conexion = sqlite3.connect('contactos.db')
        self.cursor = self.conexion.cursor()

        self.btn_nuevo.setEnabled(True)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)

        #limpiando QlineEdit
        self.nombre.setText('')
        self.apellido.setText('')
        self.email.setText('')
        self.telefono.setText('')
        self.direccion.setText('')
        self.fechaNac.setText('')
        self.altura.setText('')
        self.peso.setText('')

        #Deshabilitados QlineEdit

        self.nombre.setEnabled(False)
        self.apellido.setEnabled(False)
        self.email.setEnabled(False)
        self.telefono.setEnabled(False)
        self.direccion.setEnabled(False)
        self.fechaNac.setEnabled(False)
        self.altura.setEnabled(False)
        self.peso.setEnabled(False)
       

       
        self.btn_nuevo.clicked.connect(self.on_nuevo_reg)
        #self.btn_editar.clicked.connect(self.on_editar_reg)
        self.btn_eliminar.clicked.connect(self.on_eliminar_reg)
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

       

    # Datos

        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        telefono = self.telefono.text()
        direccion = self.direccion.text()
        fechaNac = self.fechaNac.text()
        altura = self.altura.text()
        peso = self.peso.text()
        self.tabla.addItem(str('Nombre: '+ nombre +   ' -    Apellido: ' +   apellido +   ' -  email: '  +   email +   ' -  Telefono: '   +   telefono +   ' -  Direccion: '   +   direccion +   ' -  Fecha Nac.: '   +   fechaNac +   ' -  Altura: '   +   altura +   ' -  Peso: '   +   peso))

  
        
        self.nombre = str(self.nombre.text())
        self.apellido = str(self.apellido.text())
        self.email = str(self.email.text())
        self.telefono = str(self.telefono.text())
        self.direccion = str(self.direccion.text())
        self.fechaNac = str(self.fechaNac.text())
        self.altura = str(self.altura.text())
        self.peso = str(self.peso.text())
        self.registros = (self.nombre, self.apellido,  self.email, self.telefono, self.direccion, self.fechaNac,  self.altura, self.peso)


    # Insertar los datos en la tabla de campos
        self.cursor.execute("INSERT INTO contactos (nombre, apellido, email, telefono, direccion, fechaNac,  altura, peso) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", self.registros)
        self.conexion.commit()

        self.conexion.close()

       
    def on_nuevo_reg(self): 

        self.nombre.setEnabled(True)
        self.apellido.setEnabled(True)
        self.email.setEnabled(True)
        self.telefono.setEnabled(True)
        self.direccion.setEnabled(True)
        self.fechaNac.setEnabled(True)
        self.altura.setEnabled(True)
        self.peso.setEnabled(True)
                
        self.btn_nuevo.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_cancelar.setEnabled(True)

        


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

        msg = QMessageBox()
        msg.setWindowTitle('Quitar Registro')
        msg.setText('Quieres eliminar el \n registro que seleccionaste?')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok )
        
        
        resultado = msg.exec_()
        if resultado == QMessageBox.Ok:
            id = self.tabla.selectedItem()[0]
            contacto = self.tabla.currentRow()

            self.tabla.takeItem(contacto)
            self.cursor.execute('Delete from contacto Where id= ?' + id.text()[0])
            self.conexion.commit()
        

       
        
        

    # def on_cancelar_reg(self): 
    #      pass  
    
    
    # def closeEvent(self, event):
    #     self.conexion()    


app = QApplication([])
win = MiVentana()
win.show()

app.exec_()