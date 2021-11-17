from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lista_lista.ui", self)
        

        self.agregar.clicked.connect(self.on_agregar)
        self.editar.clicked.connect(self.on_editar)
        self.eliminar.clicked.connect(self.on_eliminar)
        self.btn_derecha.clicked.connect(self.on_derecho)
        self.regresar.clicked.connect(self.on_izquierdo)

        self.current_textbox = None
        QApplication.instance().focusChanged.connect(self.on_focusChanged)

    def on_focusChanged(self, old, new):
        if isinstance(new, QLineEdit) and new != self.current_textbox:
            self.current_textbox = new
            self.listbox1.clear()
            self.listbox1.addItems(textbox_items[new.objectName()])
    
    
    
    def on_agregar(self):
        self.lista_izq.addItem(self.nombre.text())
        self.nombre.setText("")

    def on_eliminar(self):
        self.lista_izq.takeItem(self.lista_izq.currentRow())

    def on_derecho(self):
        #texto_izq = self.lista_izq.currentItem().text()
        self.lista_derecha.addItem(self.lista_izq.currentItem().text())
        self.lista_izq.takeItem(self.lista_izq.currentRow())

    def on_izquierdo(self):
        self.lista_izq.addItem(self.lista_derecha.currentItem().text())
        self.lista_derecha.takeItem(self.lista_derecha.currentRow())

    
    def on_editar(self):
        self.nombre(self.lista_izq.currentItem().text())
       
    
    
    
    
    # def on_editar(self):
    #     texto_item = self.lista_derecha.currentItem().text()
    #     nuevo_texto, ok = QInputDialog.getText(self, 'titulo', 'texto para la accion', text=texto_item)
    #     if ok:
    #         self.lista_derecha.currentItem().setText(nuevo_texto)






      

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()