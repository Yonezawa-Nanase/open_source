import sys
from PyQt5 import QtWidgets, QtGui

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()

    label = QtWidgets.QLabel(windowExample)
    label.setText('python課題')

    windowExample.setWindowTitle('練習１')
    windowExample.setGeometry(100, 100, 400, 200)

    windowExample.show()
    sys.exit(app.exec_())