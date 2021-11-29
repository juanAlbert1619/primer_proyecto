from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("agenda.ui", self)

        self.conexion = sqlite3.connect('agenda.db')
        self.cursor = self.conexion.cursor()

        self.on_cargar()
        self.on_reset()
        self.flag = True

        self.btn_cancelar.clicked.connect(self.on_cancelar)
        self.btn_eliminar.clicked.connect(self.on_eliminar)
        self.btn_nuevo.clicked.connect(self.on_nuevo)
        self.btn_editar.clicked.connect(self.on_editar)
        self.btn_aceptar.clicked.connect(self.on_aceptar)


    def qlineEdit_vacio(self):
        self.nombre.setText(str(""))
        self.apellido.setText(str(""))
        self.email.setText(str(""))
        self.telefono.setText(str(""))
        self.direccion.setText(str(""))
        self.fechaNac.setText(str(""))
        self.altura.setText(str(""))
        self.peso.setText(str(""))

    def on_reset(self):
        self.btn_nuevo.setEnabled(True)
        self.btn_editar.setEnabled(True)
        self.btn_eliminar.setEnabled(True)
        self.btn_aceptar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)
        self.nombre.setDisabled(True)
        self.apellido.setDisabled(True)
        self.email.setDisabled(True)
        self.telefono.setDisabled(True)
        self.direccion.setDisabled(True)
        self.fechaNac.setDisabled(True)
        self.altura.setDisabled(True)
        self.peso.setDisabled(True)

    def on_cancelar(self):
        self.qlineEdit_vacio()
        self.on_reset()

    def on_recargar_tabla(self):
        self.tabla.clear()
        self.on_cargar()

    

    def on_nuevo(self):
        self.flag = True
        self.btn_nuevo.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_cancelar.setEnabled(True)
        self.nombre.setDisabled(False)
        self.apellido.setDisabled(False)
        self.email.setDisabled(False)
        self.telefono.setDisabled(False)
        self.direccion.setDisabled(False)
        self.fechaNac.setDisabled(False)
        self.altura.setDisabled(False)
        self.peso.setDisabled(False)

    def on_editar(self):
        self.btn_nuevo.setEnabled(False)
        self.btn_editar.setEnabled(True)
        self.btn_eliminar.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_cancelar.setEnabled(True)
        self.nombre.setDisabled(False)
        self.apellido.setDisabled(False)
        self.email.setDisabled(False)
        self.telefono.setDisabled(False)
        self.direccion.setDisabled(False)
        self.fechaNac.setDisabled(False)
        self.altura.setDisabled(False)
        self.peso.setDisabled(False)
        self.flag=False
        print(self.flag)
        ids = self.tabla.selectedItems()[0]

        escribir = self.cursor.execute("SELECT * FROM contactos WHERE id=" + ids.text()[0] )

        for fila in escribir:
            self.nombre.setText(fila[1])
            self.apellido.setText(fila[2])
            self.email.setText(fila[3])
            self.direccion.setText(fila[4])
            self.telefono.setText(fila[5])
            self.fechaNac.setText(fila[6])
            self.peso.setText(str(fila[8]))
            self.altura.setText(str(fila[7]))

    def update(self):
        self.flag=False
        ids = self.tabla.selectedItems()[0]
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        telefono = str(self.telefono.text())
        direccion = str(self.direccion.text())
        fechaNac = str(self.fechaNac.text())
        altura = (self.altura.text())
        peso = (self.peso.text())

        self.tabla.addItem(str(nombre  + "   " + apellido ))

        self.qlineEdit_vacio()
        self.cursor.execute("UPDATE contactos SET nombre='"+nombre+"', apellido='"+apellido+"', email='"+email+"', telefono='"+telefono+"', direccion='"+direccion+"', fechaNac='"+fechaNac+"', altura='"+altura+"', peso='"+peso +"' WHERE id="+ids.text()[0])
        self.conexion.commit()

    def on_eliminar(self):
        msg = QMessageBox()
        msg.setWindowTitle('Eliminar Registro')
        msg.setIcon(QMessageBox.Warning)
        msg.setText('¿Seguro que deseas eliminar el objeto seleccionado?')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        resultado = msg.exec()
        if resultado == QMessageBox.Ok:
            ids = self.tabla.selectedItems()[0]
            contacto = self.tabla.currentRow()

            self.tabla.takeItem(contacto)
            self.cursor.execute("DELETE FROM contactos WHERE id = " + ids.text()[0])
            self.conexion.commit()
            self.on_reset()
        elif resultado == QMessageBox.Cancel:
            self.on_reset()
        self.on_recargar_tabla()

    def on_cargar(self):
        self.cursor.execute('select * from contactos')
        contactos = self.cursor.fetchall()
        for contacto in contactos:
            id = str(contacto[0])
            nombre = contacto[1]
            apellido = contacto[2]
           
            self.tabla.addItem(str(id+"   "+nombre  + "   " + apellido  ))

    def on_aceptar(self):
        print(self.flag)
        if self.flag == True:
            self.on_crear()
            self.on_recargar_tabla()
        elif self.flag == False:
            self.update()
            self.on_recargar_tabla()

        self.btn_nuevo.setEnabled(True)
        self.btn_editar.setEnabled(True)
        self.btn_eliminar.setEnabled(True)
        self.btn_aceptar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)

    def on_crear(self):
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        telefono = str(self.telefono.text())
        direccion = str(self.direccion.text())
        fechaNac = str(self.fechaNac.text())
        altura = str(self.altura.text())
        peso = str(self.peso.text())

        self.tabla.addItem(str(nombre  + "   " + apellido + "   " + email + "   " + telefono + "   " + direccion + "   " + fechaNac+ "   " + altura+ "   " + peso ))

        self.nombre.setText(str(""))
        self.apellido.setText(str(""))
        self.email.setText(str(""))
        self.telefono.setText(str(""))
        self.direccion.setText(str(""))
        self.fechaNac.setText(str(""))
        self.altura.setText(str(""))
        self.peso.setText(str(""))

            # Agregar usuario
        self.cursor.execute("insert into contactos (nombre, apellido, email, direccion, telefono, fechaNac, altura, peso) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(nombre, apellido, email, telefono,direccion,fechaNac,altura,peso))
        self.conexion.commit()



    def closeEvent(self, event):
        self.conexion.close()

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()