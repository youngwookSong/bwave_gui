import sys
import os
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

        # 왼쪽 메뉴바에서 활성화 된 메뉴 색 변경
        # self.activepage = self.ui.btn_save_2
        # self.activepage.setStyleSheet(active_style)

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

        self.data = os.listdir(personal_res.root)
        self.data.remove('resources.py')
        self.data.remove('__pycache__')
        print(self.data)

        self.row = len(self.data)
        self.ui.tableWidget.setRowCount(self.row)

        self.checkboxList = [] # 체크박스 리스트 저장하기
        self.dataList = [] # 체크박스 인덱스에 맞는 데이터 저장하기

        ## 함수로 만들기
        for row, person in enumerate(self.data):
            self.dataList.append(person)
            with open(os.path.join(personal_res.root, '{}/info.json'.format(person)), 'r', encoding='utf-8') as f:
                info_json_path = json.load(f)
            self.ui.tableWidget.setCellWidget(row, 0, UIFunctions.makeChbox(self, row))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(info_json_path['num']))
            self.ui.tableWidget.item(row, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(info_json_path['name']))
            self.ui.tableWidget.item(row, 2).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(info_json_path['date']))
            self.ui.tableWidget.item(row, 3).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(info_json_path['y_pred_proba']))
            self.ui.tableWidget.item(row, 4).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def control(self):
        # 메뉴 토글 버튼
        # self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 60, True))
        # new file 버튼
        self.ui.btn_new_file.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # add 버튼
        self.ui.btn_add.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # 홈 화면 new file 버튼
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # 삭제 버튼
        self.ui.btn_delete.clicked.connect(lambda: UIFunctions.remove_table_data(self))
        # 로그아웃 버튼
        self.ui.btn_logout.clicked.connect(self.button_logout_action)
        # tablewidget 더블 클릭
        self.ui.tableWidget.doubleClicked.connect(lambda: UIFunctions.table_double_clicked(self))
        # 분석하기 버튼
        self.ui.btn_anal.clicked.connect(lambda: UIFunctions.analysis_result(self))

    def button_logout_action(self): #이거 나중에 main_functions로 옮기기
        self.close()
        self.second = LoginView()
        self.second.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoginView()
    sys.exit(app.exec())