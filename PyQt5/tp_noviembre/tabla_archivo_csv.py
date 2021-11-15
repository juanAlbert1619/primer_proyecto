from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QInputDialog
from PyQt5 import uic
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tabla_archivo_csv.ui', self)

        #Cantidad de Columnas
        self.tabla.setColumnCount(3)
        self.tabla.setColumnCount(3)
        self.tabla.setColumnWidth(0,100)
        self.tabla.setColumnWidth(1,100)
        self.tabla.setColumnWidth(2,150)

        #Cabecera

        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail'))

        self.filas = 0
        self.btn_agregar.clicked.connect(self.on_agregar)
        self.btn_carga.clicked.connect(self.on_cargar)
        self.btn_guardar.clicked.connect(self.on_guardar)
        self.btn_eliminar.clicked.connect(self.on_eliminar)


    def on_agregar(self):
        fila = 0
        fila = self.filas
        self.tabla.insertRow(fila)

        #  Agrega items de txt a tabla

        nombre = self.txt_nombre.text()
        self.tabla.setItem(fila,0,QTableWidgetItem(nombre))
        self.txt_nombre.setText("")
        apellido = self.txt_apellido.text()
        self.tabla.setItem(fila,1,QTableWidgetItem(apellido))
        self.txt_apellido.setText("")
        email = self.txt_e_mail.text()
        self.tabla.setItem(fila,2,QTableWidgetItem(email))
        self.txt_e_mail.setText("")

        self.filas = self.filas + 1

    def on_cargar(self):
        fila = self.filas
        
        self.filas = self.filas

        archivo = open('datos.csv')
        lector = csv.reader(archivo, delimiter = ',', quotechar = '"')

        for f in lector:
            fila = self.filas
            self.tabla.insertRow(fila)
            
            self.tabla.setItem(fila, 0, QTableWidgetItem('{0}'.format(f[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem('{0}'.format(f[1])))
            self.tabla.setItem(fila, 2, QTableWidgetItem('{0}'.format(f[2])))

        archivo.close()
    
    def on_guardar(self):

        archivo = open('datos-guardados.csv', 'w', newline='')
        escritor = csv.writer(archivo, delimiter=',', quotechar='"')

        numRow = self.tabla.rowCount()

        for f in range(numRow):
            
            datos_tabla = [self.tabla.item(f,0).text(), self.tabla.item(f,1).text(), self.tabla.item(f,2).text()]
            escritor.writerow(datos_tabla)

        archivo.close()

        
    def on_eliminar(self):

        msg = QMessageBox()
        msg.setWindowTitle('Quitar Fila')
        msg.setText('Quieres eliminar la \n fila seleccionada?')

        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        

        filaseleccionada = self.tabla.selectedItems()
        resultado = msg.exec_()
        if resultado == QMessageBox.Ok:
            fila = filaseleccionada[0].row()
            self.tabla.removeRow(fila)
            self.tabla.clearSelection()
        else:
            QMessageBox.critical(self, 'Eliminar fila', 'Seleccione una fila', QMessageBox.Ok)

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()



