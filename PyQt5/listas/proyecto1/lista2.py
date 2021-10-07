from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto1/lista2.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.editar.clicked.connect(self.on_editar)
        self.eliminar.clicked.connect(self.on_eliminar)
        self.eliminartodo.clicked.connect(self.on_eliminartodo)
        
        
    def on_agregar(self):
        self.lista.addItem(self.nombre.text())
        self.nombre.setText('')

    def on_editar(self):
        texto_item = self.lista.currentItem().text()
        nuevo_texto, ok = QInputDialog.getText(self, 'Editar', 'Ingrese nuevo nombre', text = texto_item)
        if ok:
            self.lista.currentItem().setText(nuevo_texto) 

    def on_eliminar(self):
        self.lista.takeItem(self.lista.currentRow())
        

    def on_eliminartodo(self):
        self.lista.clear()

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()