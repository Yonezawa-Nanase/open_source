#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.click = 0
        self.text = ""


    def initUI(self):      

        btn1 = QPushButton("確認", self)

        # クリックされたらbuttonClickedの呼び出し
        btn1.clicked.connect(self.buttonClicked)            

        self.statusBar()

        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('練習2')
        self.show()


    def buttonClicked(self):
        self.click += 1

        # ステータスバーへメッセージの表示
        if self.click == 1:
            self.text = "python課題"
        elif self.click > 1:
            self.text = "確認済み"
        else :
            self.text = ""

        self.statusBar().showMessage(self.text)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())