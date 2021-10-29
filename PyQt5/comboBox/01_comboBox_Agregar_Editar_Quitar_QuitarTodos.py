from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ComboBox/combo_agregar_editar_quitar_quitarTodos.ui", self)
        self.btn_agregar.clicked.connect(self.on_agregar)
        self.btn_editar.clicked.connect(self.on_editar)
        self.btn_quitar.clicked.connect(self.on_quitar)
        self.btn_quitarTodos.clicked.connect(self.on_quitarTodo)
        self.combo.currentIndexChanged.connect(self.on_cambio)
        #self.combo.currentIndexChanged.connect(self.on_agregar)
        

    def on_agregar(self):

        # Ingresamos un texto
        texto, ok = QInputDialog.getText(self, 'Ingresar', 'Ingrese un texto', text = 'Texto por defecto' )
        if ok and texto:
            self.combo.addItem(texto)
    
    def on_cambio(self):
        self.etiqueta.setText(self.combo.currentText())

    def on_editar(self, index):
        
        content = self.combo.currentText()
        nuevo_texto, ok = QInputDialog.getText(self, 'Editar', 'Ingrese nuevo nombre', text = content)
        if ok and nuevo_texto:
            indice = self.combo.currentIndex()
            self.combo.setItemText(indice, nuevo_texto) 


    def on_quitar(self):
        msg = QMessageBox()
        msg.setWindowTitle('Quitar Item')
        msg.setText('Quieres eliminar el \n elemento seleccionado')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok )
        
        
        resultado = msg.exec_()
        if resultado == QMessageBox.Ok:
            indice = self.combo.currentIndex()
            self.combo.removeItem(indice)
        




    
    def on_quitarTodo(self):
        msg = QMessageBox()
        msg.setWindowTitle('Quitar Item')
        msg.setText('Quieres eliminar los \n elementos del listado')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok )
        
        
        resultado = msg.exec_()
        if resultado == QMessageBox.Ok:
           self.combo.clear() 
        

      
app = QApplication([])
win = MiVentana()
win.show()

app.exec_()