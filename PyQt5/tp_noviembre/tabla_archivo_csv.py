from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5 import uic
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tabla_archivo_csv.ui', self)

        #Cantidad de Columnas
        self.tabla.setColumnCount(3)

        #Cabecera

        self.tabla.serHorizontalHeaderLabels('Nombre', 'Apellido', 'e-mail' )

        self.fila = 0
        self.btn_agregar.clicked.connect(self.on_agregar)
        self.btn_carga.clicked.connect(self.on_cargar)
        self.btn_guardar.clicked.connect(self.on_guardar)
        self.btn_eliminar.clicked.connect(self.on_eliminar)


    def on_agregar(self):
        fila = 0
        fila = self.filas
        self.tabla.insertRow(fila)

        #  Agrega items de txt a tabla

        nombre = self.txt._nombre.text()
        self.tabla.setItem(fila,0,QTableWidgetItem(nombre))
        self.txt_nombre.setText('')
        apellido = self.txt_apellido.text()
        self.tabla.setItem(fila,0,QTableWidgetItem(apellido))
        self.txt_apellido.setText('')
        email = self.txt_e_mail.text()
        self.tabla.setItem(fila,0,QTableWidgetItem(email))
        self.txt_e_mail.setText('')

        self.filas = self.filas + 1

    def on_carga(self):
        fila = self.filas
        self.tabla.insertRow(fila)
        self.filas = self.filas

        archivo = open('datos.csv')
        lector = csv.reader(archivo, delimiter = ',', quopetchar = '"')

        for f in lector:
            fila = self.filasself.tabla.insertRow(fila)
            
            self.tabla.setItem(fila, 0, QTableWidgetItem('{0}'.format(f[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem('{0}'.format(f[1])))
            self.tabla.setItem(fila, 2, QTableWidgetItem('{0}'.format(f[2])))

        archivo.close()
    
    def on_guardar(self):

        archivo = open('datos.csv', 'W', newline='')
        guardar = csv.writer(archivo, delimiter =',', quotechar='"')

        numRow = self.tablarowCount()

        for f in range(numRow):
            datos_tabla = [self.tabla.item(f, 0).text(), self.tabla.item(f, 1).text(), self.tabla.item(f, 2).text()]
            guardar.writerows(datos_tabla)

        archivo.close()

    
    def on_eliminar(self):

        msg = QMessageBox()
        msg.setWindowTitle('Quitar Fila')
        msg.setText('Quieres eliminar la \n fila seleccionada?')

        msg.setIcon(QMessageBox.Warning)
        msg.setStandarButtons(QMessageBox.Ok)

        filaseleccionada = self.tabla.selectedItem()
        resultado = msg.exec_()
        if resultado == QMessageBox.ok:
            fila = filaseleccionada[0].row()
            self.tabla.removeRow(fila)
            self.tabla.clearSelection()
        else:
            QMessageBox.critical(self, 'Eliminar fila', 'Seleccione una fila', QMessageBox.Ok)



