import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtUiTools, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

#imort gui file
from ui_main import Ui_MainWindow

#import gui functions
from ui_funtions import *

#import stylesheet
from style import *

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()

        # self.logoFile = QPixmap()
        # self.logoFile.load("icon/bwave_logo_2.png")
        # # self.logoFile = self.logoFile.scaledToWidth(500)
        # # self.logoFile = self.logoFile.scaled(QSize(600,400), aspectMode=Qt.IgnoreAspectRatio)
        # self.ui.logo.setPixmap(self.logoFile)
        # self.ui.logo.setScaledContents(True)
        # self.ui.logo.setAlignment(Qt.AlignCenter)

        self._dialog = None # new file의 dialog

        # 왼쪽 메뉴바에서 활성화 된 메뉴 색 변경
        self.activepage = self.ui.btn_home
        self.activepage.setStyleSheet(active_style)

        self.prep_activepage = None
        self.menu_state = "open"

        #move window with title bar
        # def moveWindow(event):
        #     if UIFunctions.returnStatus(self) == 1:
        #         UIFunctions.maximize_restore(self)
        #
        #     if event.buttons() == Qt.LeftButton:
        #         self.move(self.pos() + event.globalPos() - self.dragPos)
        #         self.dragPos = event.globalPos()
        #         event.accept()
        #
        # self.ui.title_bar.mouseMoveEvent = moveWindow
        # UIFunctions.uiDefinitions(self)

        self.show()

    # def mousePressEvent(self, event):
    #     self.dragPos = event.globalPos()

    def control(self):
        # 메뉴 토글 버튼
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 60, True))
        # home 버튼
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.set_page(self, self.ui.home))
        # analysis 버튼
        self.ui.btn_anal.clicked.connect(lambda: UIFunctions.set_page(self, self.ui.anal))
        # new file 버튼
        self.ui.btn_new_file.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # 홈 화면 new file 버튼
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec())