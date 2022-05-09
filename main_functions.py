import shutil
import time
import os

# from PyQt5 import uic
from PySide6.QtWidgets import QTableWidgetItem

from main import *
from dialog.newfile_dialog2 import Ui_Dialog
from dialog.loadingBar import Ui_Dialog_loading, Worker, ThreadClass

from ui.tab_frame import Ui_tabFrame
from ui.tab_frame_pre import Ui_tabFrame_pre

from model_Test.newDataTest import model_test
GLOBAL_STATE = 0

from style import *
import resources as main_res
import personal_data.resources as personal_res
from functions.progress_functions import progress_functions

import json
from collections import OrderedDict

# # toggle close시 아이콘만
# def changeBtnIcon(button):
#     button.setStyleSheet(close_style)
#     button.setText("")
#
# # toggle open시 다 나오게
# def afterChange(button, text):
#     button.setStyleSheet(style)
#     button.setText(text)

class UIFunctions(MainView): #main.py의 클래스를 상속
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # if maximized
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            # self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            # self.ui.drop_frame.setStyleSheet("border-radius: 0px;")
            self.ui.btn_max.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # self.ui.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
            # self.ui.drop_frame.setStyleSheet("border-radius: 10px;")
            self.ui.btn_max.setToolTip("Maximize")

    def uiDefinitions(self):
        #remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MAXIMIZE / RESTORE
        self.ui.btn_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW 나중에 구현해야욈
        # self.sizegrip = QSizeGrip(self.ui.frame_grip)
        # self.sizegrip.setStyleSheet(
        #     "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus(self):
        return GLOBAL_STATE

    ## 토글 메뉴
    # def toggleMenu(self, maxWidth, enable):
    #     if enable:
    #         #get width
    #         width = self.ui.frame_left_menu.width()
    #         maxExtend = maxWidth
    #         standard = 250
    #
    #         #set max width
    #         if self.menu_state == "open":
    #             widthExtended = maxExtend
    #             self.ui.btn_toggle.setIcon(QtGui.QIcon("./icon/menu.png"))
    #             self.ui.btn_toggle.setIconSize(QtCore.QSize(24, 24))
    #             changeBtnIcon(self.ui.btn_toggle)
    #             # changeBtnIcon(self.ui.btn_home)
    #             # changeBtnIcon(self.ui.btn_anal)
    #             changeBtnIcon(self.ui.btn_new_file)
    #             changeBtnIcon(self.ui.btn_open_2)
    #             changeBtnIcon(self.ui.btn_save_2)
    #             changeBtnIcon(self.ui.btn_new_file_2)
    #             self.activepage.setStyleSheet(active_close_style)
    #             self.menu_state = "close"
    #
    #         else:
    #             widthExtended = standard
    #             self.ui.btn_toggle.setIcon(QtGui.QIcon("./icon/left.png"))
    #             self.ui.btn_toggle.setIconSize(QtCore.QSize(24, 24))
    #             afterChange(self.ui.btn_toggle, "  메뉴")
    #             # afterChange(self.ui.btn_home, "  메인 화면")
    #             # afterChange(self.ui.btn_anal, "  진단 결과")
    #             afterChange(self.ui.btn_new_file, "  새로운 파일 열기")
    #             afterChange(self.ui.btn_open_2, "  열기")
    #             afterChange(self.ui.btn_save_2, "  저장")
    #             afterChange(self.ui.btn_new_file_2, "  설정")
    #             self.activepage.setStyleSheet(active_style)
    #             self.menu_state = "open"
    #
    #         #animation
    #         self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
    #         self.animation.setDuration(500)
    #         self.animation.setStartValue(width)
    #         self.animation.setEndValue(widthExtended)
    #         self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #         self.animation.start()

    ## 각 row의 해당하는 고유의 체크박스 만들기
    def makeChbox(self, idx):
        # 고유의 이름을 가지는 체크박스 만들어야되는데 안되네... -> list로 해결
        ckbox = QCheckBox()
        cellWidget = QWidget()
        layoutCB = QHBoxLayout(cellWidget)
        layoutCB.addWidget(ckbox)
        layoutCB.setAlignment(QtCore.Qt.AlignCenter)
        layoutCB.setContentsMargins(0, 0, 0, 0)
        cellWidget.setLayout(layoutCB)
        cellWidget.setStyleSheet(u"border:0px")

        self.checkboxList.append(ckbox)
        return cellWidget

    ## 테이블에 데이터 삭제
    import shutil
    def remove_table_data(self):
        print(len(self.checkboxList))

        print(self.dataList)

        delIdx = []
        for idx, chbox in enumerate(self.checkboxList):
            if chbox.isChecked() == True:
                path = os.path.join(personal_res.root, self.dataList[idx])
                print("path:", path)
                if os.path.exists(path):
                    shutil.rmtree(path)

                self.ui.tableWidget.removeRow(idx)
                del self.checkboxList[idx]
                del self.dataList[idx]
                self.row -= 1
            print(self.dataList)

    ## 테이블 더블 클릭 시 해당 데이터 결과 화면으로 이동
    def table_double_clicked(self):
        row = self.ui.tableWidget.currentIndex().row()
        column = self.ui.tableWidget.currentIndex().column()
        print(row, column)

        with open(os.path.join(personal_res.root, '{}/info.json'.format(self.dataList[row])), 'r', encoding='utf-8') as f:
            info_json_path = json.load(f)

        self.ui.pages.setCurrentWidget(self.ui.anal)
        current_tab = QWidget()
        self.ui.tabWidget.addTab(current_tab, "{} {}".format(info_json_path['num'], info_json_path['name']))
        self.ui.tabWidget.setCurrentWidget(current_tab)

        self._tabFrame = Ui_tabFrame_pre(current_tab, info_json_path['file'], info_json_path['name'],
                                         info_json_path['birth'], info_json_path['num'], info_json_path['date'],
                                         info_json_path['sex'], info_json_path['y_pred'], info_json_path['y_pred_proba'])

            # QMessageBox.information(self, "ERROR", "아직 분석이 안되었습니다. 분석부터 하세요")

    ## 왼쪽 메뉴 누르면 해당 페이지로 이동
    # def set_page(self, page):
    #     self.ui.pages.setCurrentWidget(page)
    #     self.prep_activepage = self.activepage
    #     if page == self.ui.home:
    #         self.activepage = self.ui.btn_home
    #     if page == self.ui.anal:
    #         self.activepage = self.ui.btn_anal
    #
    #     if self.menu_state == "open":
    #         self.prep_activepage.setStyleSheet(style)
    #         self.activepage.setStyleSheet(active_style)
    #
    #     if self.menu_state == "close":
    #         self.prep_activepage.setStyleSheet(close_style)
    #         self.activepage.setStyleSheet(active_close_style)

    ## new_file(인적정보, 파일 업로드) 창 열기 (modal)
    def handleOpenDialog(self):
        self._dialog = Ui_Dialog()

        if self._dialog.exec(): #확인 버튼 눌렀을때

            file, name, birth, num, date, sex = self._dialog.info() #정보 받아오기

            ## table에 새로운 열 추가
            ckbox = QCheckBox()
            cellWidget = QWidget()
            layoutCB = QHBoxLayout(cellWidget)
            layoutCB.addWidget(ckbox)
            layoutCB.setAlignment(QtCore.Qt.AlignCenter)
            layoutCB.setContentsMargins(0, 0, 0, 0)
            cellWidget.setLayout(layoutCB)
            cellWidget.setStyleSheet(u"border:0px")
            self.checkboxList.append(ckbox)
            self.dataList.append('{}_{}'.format(num, name))

            self.row += 1
            self.ui.tableWidget.setRowCount(self.row)
            self.ui.tableWidget.setCellWidget(self.row - 1, 0, cellWidget)
            self.ui.tableWidget.setItem(self.row - 1, 1, QTableWidgetItem(num))
            self.ui.tableWidget.item(self.row - 1, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(self.row - 1, 2, QTableWidgetItem(name))
            self.ui.tableWidget.item(self.row - 1, 2).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(self.row - 1, 3, QTableWidgetItem(date))
            self.ui.tableWidget.item(self.row - 1, 3).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(self.row - 1, 4, QTableWidgetItem('-'))
            self.ui.tableWidget.item(self.row - 1, 4).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

            ## 환자 디렉토리 만들기
            self.directory = os.path.join(personal_res.root, "{}_{}".format(num, name)) #절대 경로
            try:
                if not os.path.exists(self.directory):
                    os.makedirs(self.directory)
            except OSError:
                print('Error: Creating directory. ' + self.directory)

            ## 환자 정보 json만들기
            file_data = OrderedDict()
            file_data['file'] = file
            file_data['name'] = name
            file_data['birth'] = birth
            file_data['num'] = num
            file_data['date'] = date
            file_data['sex'] = sex
            file_data['y_pred_proba'] = '-'

            with open('{}/info.json'.format(self.directory), 'w', encoding='utf-8') as make_file:
                json.dump(file_data, make_file, ensure_ascii=False, indent='\t')

            ## 로딩바 화면 출력
            self._dialog_loading = Ui_Dialog_loading(file, self.directory)  # loading bar 열기 (여기서 알고리즘 돌림 모델에 넣고)
            self._dialog_loading.exec()

            # 탭 추가 및 해당 탭으로 이동
            self.ui.pages.setCurrentWidget(self.ui.anal)
            # cur_idx = self.ui.tableWidget.currentIndex()
            current_tab = QWidget()
            self.ui.tabWidget.addTab(current_tab, "{} {}".format(num, name))
            self.ui.tabWidget.setCurrentWidget(current_tab)

            self.ui.btn_anal.setDisabled(False)

            with open('{}/info.json'.format(self.directory), 'r', encoding='utf-8') as f:
                info_json_path = json.load(f)

            self._tabFrame = Ui_tabFrame_pre(current_tab, file, name, birth, num, date, sex, info_json_path['y_pred'],
                                             info_json_path['y_pred_proba'])
            # self.ui.tabWidget.setCurrentWidget(self._tabFrame)
            # self.ui.tableWidget.setCurrentIndex(cur_idx+1)

        else: #취소 버튼 눌렀을때
            print("cancel")

    def analysis_result(self):
        print("분석하기")
        print(self.ui.tabWidget.currentIndex())
        print(self.ui.tabWidget.currentWidget())
        print(self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()))
        num_name = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()).split()
        print(num_name)

        information = "이름: {}\n환자번호: {}".format(num_name[1], num_name[0])
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Title of MessageBox")
        msgBox.setText("분석을 진행하시겠습니까?")
        msgBox.setInformativeText(information)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)

        result = msgBox.exec()
        if result == QMessageBox.Ok:
            self._tabFrame.tab_pages.setCurrentWidget(self._tabFrame.tabFrame_anal)

            self.pf = progress_functions(self._tabFrame, self._tabFrame.y_pred_proba, self._tabFrame.y_pred)

            # self._tabFrame.circularProgress.setStyleSheet(progress_functions.newStylesheet)

            # with open('{}/info.json'.format(self.directory), 'r', encoding='utf-8') as f:
            #     info_json_path = json.load(f)
            # self.ui.tableWidget.setItem(self.row - 1, 4, QTableWidgetItem(info_json_path['y_pred_proba']))
            # self.ui.tableWidget.item(self.row - 1, 4).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        elif result == QMessageBox.Cancel:
            print("Cancel")

        # self._tabFrame.pushButton_4.clicked.connect(lambda:  self._tabFrame.tab_pages.setCurrentIndex(0))


        # TODO: 만약 탭하나 생성하고 또 다른 탭 생성하고 전 탭가서 분석하기 누를 경우.. self._tabFrame은 최근 탭에 업데이트 되어있다. 분석하기 버튼 누를때 현재 탭 위젯 가지고 오기
