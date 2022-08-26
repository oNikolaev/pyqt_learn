from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Learn PyQt 5")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
