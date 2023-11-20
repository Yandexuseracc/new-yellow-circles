import io
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QPushButton
from PyQt5.QtGui import QColor


class Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.createButton.clicked.connect(self.paintCircle)

    def paintCircle(self):
        self.ui.scene.clear()
        diameter = random.randint(100, 500)
        yellow_circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        yellow_circle.setRect(0, 0, diameter, diameter)
        yellow_circle.setBrush(QColor('yellow'))
        self.ui.view.centerOn(yellow_circle)
        self.ui.scene.addItem(yellow_circle)
        self.ui.scene.update()


class Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(990, 500)
        self.scene = QGraphicsScene(MainWindow)
        self.view = QGraphicsView(self.scene, MainWindow)
        self.view.setSceneRect(-150, -150, 500, 500)
        MainWindow.setCentralWidget(self.view)
        MainWindow.createButton = QPushButton('Создать круг', MainWindow)
        MainWindow.createButton.move(100, 200)
        MainWindow.layout().addWidget(MainWindow.createButton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())
