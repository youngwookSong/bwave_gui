# Import PySide2 classes
import sys
import os
# from PySide2 import QtCore, QtWidgets
from PySide6 import QtUiTools, QtGui
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QMainWindow)
from PySide2.QtCore import Slot, Qt

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load(resource_path("test5.ui"))
        self.setupUI()

    def say_hello(self):
        print("button pressed")

    def addtab_new(self):
        print()

    def setupUI(self):
        #---------------------TOGGLE MENU----------------------
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        UI_set.pushButton.clicked.connect(self.say_hello)
        UI_set.label_7.setFont(QFont('Times', 20))

        #------------------------show--------------------------
        self.setCentralWidget(self.ui)
        self.setWindowTitle("UI TEST")
        # self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        # self.resize(1000, 700)
        self.show()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("test3.ui"))


        # UI_set.tabWidget.addTab

        self.setCentralWidget(UI_set)
        self.setWindowTitle("UI TEST")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        self.resize(1000, 700)
        self.show()

# 파일 경로
# pyinstaller로 원파일로 압축할때 경로 필요함
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("../gui"), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)#QApplication : 프로그램을 실행시켜주는 클래스
    main = MainView()#WindowClass의 인스턴스 생성
    # main.show()#프로그램 화면을 보여주는 코드
    sys.exit(app.exec())#프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드