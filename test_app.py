import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Application(QWidget):
    x = 0

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 12))
	
        self.setToolTip('This is an unused space')

        plus_one = QPushButton('+=1', self)
        plus_one.setToolTip('This is the main button')
        plus_one.setGeometry(200, 150, 200, 60)
        plus_one.move(50, 50)
        plus_one.clicked.connect(self.plus_one_click)

        plus_one.setIcon(QIcon('pepe.jpg'))
    
        div_by_two = QPushButton('//=2', self)
        div_by_two.setToolTip('This is an additional button')
        div_by_two.setGeometry(200, 150, 200, 60)
        div_by_two.move(50, 120)
        div_by_two.clicked.connect(self.div_by_two_click)
        div_by_two.setIcon(QIcon('trollface.jpg'))

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('The_counter')
        self.show()

    def plus_one_click(self):
        self.x += 1
        print(f'Now x = {self.x}')
   
    def div_by_two_click(self):
        self.x //= 2
        print(f'From that moment x = {self.x}')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    x = Application()
    sys.exit(app.exec_())
