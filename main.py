import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from Ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.draw_start = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.draw_start = True
        self.update()

    def paintEvent(self, event):
        if self.draw_start:
            qp = QPainter()

            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        rad = randint(30, 200)
        qp.setBrush(QColor(*[randint(i - i, 255) for i in range(3)]))
        cen_x = randint(0, self.width() - rad - self.pushButton.width())
        cen_y = randint(self.pushButton.width() + rad, self.height() - rad)
        qp.drawEllipse(cen_x, cen_y, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
