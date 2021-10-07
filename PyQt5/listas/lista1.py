from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto1/lista1.ui", self)

       #self.lista.currentItemChanged.connect(self.on_item_changed)

       #trabajatemos con la funsion Clicked
        self.lista.itemClicked.connect(self.on_item_clicked)



    def on_item_changed(self, actual, anterior):
        self.lb_texto.setText(actual.text())
        if anterior:
            print(anterior.text())

    def on_item_clicked(self):
        self.lb_texto.setText(self.lista.currentItem().text())
        

app = QApplication([])
win = MiVentana()
win.show()

app.exec_()

        