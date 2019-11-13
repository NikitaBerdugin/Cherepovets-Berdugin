from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint

 
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui',self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()
            self.flag = False

    def drawFlag(self, qp):
            qp.setBrush(QColor(255, 255, 0))
            n=randint(0, 255)
            qp.drawEllipse(randint(0, 255), randint(0, 255), n,n)
 

if __name__ == '__main__':
    app = QApplication([])
    w = MyWidget()
    w.show()
    app.exec()

