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
	
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('+1', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.setGeometry(200, 150, 100, 30)
        btn.move(50, 50)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('The_counter')
        
        btn.clicked.connect( self.clickme)
        btn.setIcon(QIcon('pepe.jpg'))

        self.show()

    def clickme(self):
        self.x += 1
        print(f'Now x = {self.x}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    x = Application()
    sys.exit(app.exec_())
