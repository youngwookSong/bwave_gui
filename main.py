import sys
import os
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtUiTools, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pickle

#imort gui file
from ui.ui_main import Ui_MainWindow
from ui.ui_loginScreen import Ui_LoginWindow

#import gui functions
from main_functions import *

#import stylesheet
from style import *
import resources as main_res
import personal_data.resources as personal_res

from dialog.product import Ui_Dialog_product

import json
from multiprocessing import freeze_support

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dragPos = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.control()
        self.user = None

        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)

        # self._dialog_product = Ui_Dialog_product()
        # self._dialog_product.show()

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def control(self):
        # login 버튼
        self.ui.btn_login.clicked.connect(self.button_login_action)

    def button_login_action(self): #이거 나중에 main_functions로 옮기기
        ## user ID 저장
        self.user = self.ui.IDInput.text()
        print(self.user)

        ## 로그인 화면 닫기
        self.close()
        self.second = MainView(self.user) ## 해당 id 전송
        self.second.show()


class MainView(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()
        self.ui.UserID.setText(user) # 해당 id 받아옴 text 바꿔줌
        # self.ui.btn_anal.setDisabled(True)
        self._tabFrame = None
        self._dialog = None # new file의 dialog

        self.prep_activepage = None
        self.menu_state = "open"

        # move window with title bar
        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)

        UIFunctions.reset_table(self) #테이블에 데이터 넣기

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def control(self):
        # 메뉴 토글 버튼
        # self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 60, True))
        # new file 버튼
        self.ui.btn_new_file.clicked.connect(lambda: UIFunctions.handleOpenDialog(self, 'new'))
        # add 버튼
        self.ui.btn_add.clicked.connect(lambda: UIFunctions.handleOpenDialog(self, "add"))
        # 홈 화면 new file 버튼
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # date search 버튼
        self.ui.pushButton_3.clicked.connect(lambda: UIFunctions.date_search(self))
        # Today 버튼
        self.ui.btn_today.clicked.connect(lambda: UIFunctions.search_today(self))
        # Week 버튼
        self.ui.btn_week.clicked.connect(lambda: UIFunctions.search_week(self))
        # Month 버튼
        self.ui.btn_month.clicked.connect(lambda: UIFunctions.search_month(self))
        # 검색 버튼
        self.ui.btn_search.clicked.connect(lambda: UIFunctions.search_table_data(self))
        # reset 버튼
        self.ui.btn_reset.clicked.connect(lambda: UIFunctions.reset_table(self))
        # 삭제 버튼
        self.ui.btn_delete.clicked.connect(lambda: UIFunctions.remove_table_data(self))
        # 로그아웃 버튼
        self.ui.btn_logout.clicked.connect(self.button_logout_action)
        # tablewidget 더블 클릭
        self.ui.tableWidget.doubleClicked.connect(lambda: UIFunctions.table_double_clicked(self))
        # 분석하기 버튼
        self.ui.btn_anal.clicked.connect(lambda: UIFunctions.analysis_result(self))

    def button_logout_action(self):
        self.close()
        self.second = LoginView()
        self.second.show()

if __name__ == '__main__':
    # freeze_support()
    app = QApplication(sys.argv)
    main = LoginView()
    sys.exit(app.exec())