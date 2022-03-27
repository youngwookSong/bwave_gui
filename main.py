import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtUiTools, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from dummy_data import dummy_data
import pickle

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

        # with open('data.pickle', 'wb') as f:
        #     pickle.dump([], f)

        ## load dummy data
        with open('data.pickle', 'rb') as f:
            self.data = pickle.load(f)

        print(self.data)

        self.row = len(self.data)
        self.ui.tableWidget.setRowCount(self.row)

        self.checkboxList = [] # 체크박스 리스트 저장하기

        for row, person in enumerate(self.data):
            self.ui.tableWidget.setCellWidget(row, 0, UIFunctions.makeChbox(self,row))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(person["회원ID"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(person["이름"]))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(person["검사일시"]))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(person["점수"]))

        # print(self.ckbox1.checkState())

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def control(self):
        # 메뉴 토글 버튼
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 60, True))
        #
        self.ui.btn_add.clicked.connect(lambda: UIFunctions.add_table_data(self))

        # new file 버튼
        self.ui.btn_new_file.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # 홈 화면 new file 버튼
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.handleOpenDialog(self))
        # 삭제 버튼
        self.ui.btn_delete.clicked.connect(lambda: UIFunctions.remove_table_data(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec())