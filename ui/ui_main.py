# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test5pJsFeF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# from PySide6 import QtGui
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from style import *

def changeBtnIcon(button, iconFile, size):
    button.setIcon(QtGui.QIcon(iconFile))
    button.setIconSize(QtCore.QSize(size, size))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.btn_cmm = 20
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1350, 900)
        MainWindow.setMinimumSize(QSize(1350, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.drop_frame = QFrame(self.centralwidget)
        self.drop_frame.setObjectName(u"drop_frame")
        self.drop_frame.setStyleSheet(u"border-radius:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.drop_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_frame.setFrameShadow(QFrame.Raised)
        # self.drop_frame.setStyleSheet(u"background-color: rgb(53,56,69);")
        self.verticalLayout_5 = QVBoxLayout(self.drop_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.drop_frame)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(350, 0))
        self.frame_left_menu.setMaximumSize(QSize(350, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(40, 40, 45);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_left_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setStyleSheet(u"background-color: rgb(53,56,69);")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)

        self.btn_toggle = QPushButton(self.frame_5)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 40))
        self.btn_toggle.setMaximumSize(QSize(45, 40))
        self.btn_toggle.setStyleSheet(style)

        self.horizontalLayout_18.addWidget(self.btn_toggle)

        self.frame_37 = QFrame(self.frame_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_37)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9,0,0,0)
        self.label_18 = QLabel(self.frame_37)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255,255,255);\n"
                                    "font-style: bold;\n"
                                    "font-size: 16px")

        self.verticalLayout_9.addWidget(self.label_18)

        self.horizontalLayout_18.addWidget(self.frame_37)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.top_menus = QFrame(self.frame_left_menu)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMaximumSize(QSize(16777215, 130))
        self.top_menus.setFrameShape(QFrame.NoFrame)
        self.top_menus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.top_menus)
        # ifndef Q_OS_MAC
        self.horizontalLayout_13.setSpacing(20)
        # endif
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(12, 30, 12, 12)
        self.btn_new_file = QPushButton(self.top_menus)
        self.btn_new_file.setObjectName(u"btn_new_file")
        sizePolicy.setHeightForWidth(self.btn_new_file.sizePolicy().hasHeightForWidth())
        self.btn_new_file.setSizePolicy(sizePolicy)
        self.btn_new_file.setMinimumSize(QSize(0, 40))
        self.btn_new_file.setStyleSheet(btn_style)

        self.horizontalLayout_13.addWidget(self.btn_new_file)

        self.btn_add = QPushButton(self.top_menus)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QSize(0, 40))
        self.btn_add.setStyleSheet(btn_style)

        self.horizontalLayout_13.addWidget(self.btn_add)

        self.btn_open = QPushButton(self.top_menus)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QSize(0, 40))
        self.btn_open.setStyleSheet(btn_style)

        self.horizontalLayout_13.addWidget(self.btn_open)

        self.verticalLayout_2.addWidget(self.top_menus)

        self.frame_4 = QFrame(self.frame_left_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12,0,12,0)
        self.frame_32 = QFrame(self.frame_4)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 60))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(12, 0, 12, 0)
        self.dateEdit = QDateEdit(self.frame_32)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_14.addWidget(self.dateEdit)

        self.label_17 = QLabel(self.frame_32)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.dateEdit_2 = QDateEdit(self.frame_32)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QDate.currentDate())

        self.horizontalLayout_14.addWidget(self.dateEdit_2)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, 0, -1)
        self.pushButton_3 = QPushButton(self.frame_36)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet(btn_style)

        self.horizontalLayout_17.addWidget(self.pushButton_3)

        self.horizontalLayout_14.addWidget(self.frame_36)

        self.verticalLayout_3.addWidget(self.frame_32)

        self.frame_35 = QFrame(self.frame_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 50))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_today = QPushButton(self.frame_35)
        self.btn_today.setObjectName(u"btn_today")
        sizePolicy.setHeightForWidth(self.btn_today.sizePolicy().hasHeightForWidth())
        self.btn_today.setSizePolicy(sizePolicy)
        self.btn_today.setStyleSheet(btn_style)

        self.horizontalLayout_16.addWidget(self.btn_today)

        self.btn_week = QPushButton(self.frame_35)
        self.btn_week.setObjectName(u"btn_week")
        sizePolicy.setHeightForWidth(self.btn_week.sizePolicy().hasHeightForWidth())
        self.btn_week.setSizePolicy(sizePolicy)
        self.btn_week.setStyleSheet(btn_style)

        self.horizontalLayout_16.addWidget(self.btn_week)

        self.btn_month = QPushButton(self.frame_35)
        self.btn_month.setObjectName(u"btn_month")
        sizePolicy.setHeightForWidth(self.btn_month.sizePolicy().hasHeightForWidth())
        self.btn_month.setSizePolicy(sizePolicy)
        self.btn_month.setStyleSheet(btn_style)

        self.horizontalLayout_16.addWidget(self.btn_month)

        self.verticalLayout_3.addWidget(self.frame_35)

        self.frame_33 = QFrame(self.frame_4)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 60))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        # self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setContentsMargins(0, 6, 0, 6)
        self.lineEdit = QLineEdit(self.frame_33)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 2px solid;\n"
                                    "height: 30px;\n"
                                    "background-color: rgb(255, 255, 255)")
        self.lineEdit.setClearButtonEnabled(True)
        self.horizontalLayout_15.addWidget(self.lineEdit)

        self.btn_search = QPushButton(self.frame_33)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QSize(40, 0))
        self.btn_search.setMaximumSize(QSize(40, 40))
        self.btn_search.setStyleSheet(btn_style)

        self.horizontalLayout_15.addWidget(self.btn_search)

        self.btn_delete = QPushButton(self.frame_33)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setMinimumSize(QSize(40, 0))
        self.btn_delete.setMaximumSize(QSize(40, 40))
        self.btn_delete.setStyleSheet(btn_style)

        self.horizontalLayout_15.addWidget(self.btn_delete)

        self.verticalLayout_3.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_34)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_34)
        self.tableWidget.setStyleSheet(u"border: 2px solid;\n"
                                       "color: rgb(153, 153, 153);\n"
                                       "text-align: center;")
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        if (self.tableWidget.columnCount() < 5):
                self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem.setTextAlignment(QtCore.Qt.AlignCenter)

        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem1.setTextAlignment(QtCore.Qt.AlignCenter)

        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        # self.tableWidget.setColumnWidth(-1, 30)
        # self.tableWidget.setColumnWidth(0, 45)
        # self.tableWidget.setColumnWidth(1, 70)
        # self.tableWidget.setColumnWidth(2, 55)
        # self.tableWidget.setColumnWidth(3, 70)
        # self.tableWidget.setColumnWidth(4, 55)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # edit 금지 모드


        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_21.addWidget(self.tableWidget)

        self.verticalLayout_3.addWidget(self.frame_34)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.top_menus_2 = QFrame(self.frame_left_menu)
        self.top_menus_2.setObjectName(u"top_menus_2")
        self.top_menus_2.setMaximumSize(QSize(16777215, 100))
        self.top_menus_2.setFrameShape(QFrame.NoFrame)
        self.top_menus_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.top_menus_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.btn_save_2 = QPushButton(self.top_menus_2)
        self.btn_save_2.setObjectName(u"btn_save_2")
        self.btn_save_2.setMinimumSize(QSize(0, 40))
        self.btn_save_2.setStyleSheet(btn_style)

        self.verticalLayout_8.addWidget(self.btn_save_2)

        self.verticalLayout_2.addWidget(self.top_menus_2)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.content_frame.setStyleSheet(u"background-color: rgb(53,56,69);")
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.title_bar = QFrame(self.content_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setStyleSheet(u"background-color: rgb(53,56,69);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 0))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_19.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"color: rgb(153, 153, 153)")
        font = QFont()
        font.setFamily(u"Franklin Gothic Heavy")
        font.setPointSize(14)
        self.label_title.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_title)

        self.UserID = QLabel(self.frame_title)
        self.UserID.setObjectName(u"UserID")
        self.UserID.setStyleSheet(u"margin-right: 15px;\n"
                                  "color:rgb(255,255,255);")
        self.UserID.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.UserID.setMargin(0)

        self.horizontalLayout_19.addWidget(self.UserID)

        self.btn_logout = QPushButton(self.frame_title)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setStyleSheet(btn_style)

        self.horizontalLayout_19.addWidget(self.btn_logout)

        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(120, 0))
        self.frame_btns.setMaximumSize(QSize(120, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.btn_min = QPushButton(self.frame_btns)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        # self.btn_min.setMinimumSize(QSize(40, 30))
        # self.btn_min.setMaximumSize(QSize(40, 30))
        self.btn_min.setIcon(QtGui.QIcon("./icon/mini.png"))
        self.btn_min.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_min.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btns)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setSizePolicy(sizePolicy)
        # self.btn_max.setMinimumSize(QSize(40, 20))
        # self.btn_max.setMaximumSize(QSize(40, 20))
        self.btn_max.setIcon(QtGui.QIcon("./icon/maxi.png"))
        self.btn_max.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_max.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setSizePolicy(sizePolicy)
        # self.btn_close.setMinimumSize(QSize(40, 20))
        # self.btn_close.setMaximumSize(QSize(40, 20))
        self.btn_close.setIcon(QtGui.QIcon("./icon/close.png"))
        self.btn_close.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(255,0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout_4.addWidget(self.title_bar)

        self.pages = QStackedWidget(self.content_frame)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout = QVBoxLayout(self.home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(230, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_24)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.logo = QLabel(self.frame_24)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"image:url(./icon/bwave_logo_2.png)")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.logo)

        self.horizontalLayout_4.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(230, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_23)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_19 = QFrame(self.home)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 150))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.pushButton = QPushButton(self.frame_21)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(main_btn_style)


        self.verticalLayout_19.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.frame_21)
        self.pushButton_2.setObjectName(u"pushButton")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(main_btn_style)
        self.verticalLayout_19.addWidget(self.pushButton_2)

        self.horizontalLayout_8.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_22)

        self.verticalLayout.addWidget(self.frame_19)

        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.pages.addWidget(self.home)
        self.anal = QWidget()
        self.anal.setObjectName(u"anal")
        self.verticalLayout_7 = QVBoxLayout(self.anal)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.anal)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_current_tab)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.pages.addWidget(self.anal)

        self.verticalLayout_4.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.content_frame)


        self.verticalLayout_5.addWidget(self.content)


        self.layout.addWidget(self.drop_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        changeBtnIcon(self.btn_toggle, "./icon/left.png", 24)
        # changeBtnIcon(self.btn_home, "./icon/home.png", 24)
        # changeBtnIcon(self.btn_anal, "./icon/report.png", 24)
        # changeBtnIcon(self.btn_new_file, "./icon/new_file.png", 24)
        # changeBtnIcon(self.btn_open_2, "./icon/open_file.png", 24)
        # changeBtnIcon(self.btn_save_2, "./icon/save.png", 24)
        # changeBtnIcon(self.btn_new_file_2, "./icon/setting.png", 24)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def close_current_tab(self, i):
            if self.tabWidget.count() < 2:
                    return

            self.tabWidget.removeTab(i)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u" 메뉴", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Maumgyeol-Depression   ver. 1.0.0"))
        # self.btn_home.setText(QCoreApplication.translate("MainWindow", u"  메인 화면", None))
        # self.btn_anal.setText(QCoreApplication.translate("MainWindow", u"  진단 결과", None))
        self.btn_new_file.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"검색", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uae30", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))

        self.btn_save_2.setText(QCoreApplication.translate("MainWindow", u"분석하기", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Bwave Pro", None))
        self.btn_today.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.btn_week.setText(QCoreApplication.translate("MainWindow", u"This Week", None))
        self.btn_month.setText(QCoreApplication.translate("MainWindow", u"This Month", None))
        self.UserID.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc544\uc6c3", None))
        #if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\uc18c\ud654", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText("")
#if QT_CONFIG(tooltip)
        self.btn_max.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300\ud654", None))
#endif // QT_CONFIG(tooltip)
        self.btn_max.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.logo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\uc0c8\ub85c\uc6b4 \ud30c\uc77c\ub85c \ud658\uc790 \uc9c4\ub2e8\ud558\uae30",
                                                           None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                             u"\uae30\uc874\uc758 \uc800\uc7a5\ub41c \uc9c4\ub2e8 \ud30c\uc77c \uc5f4\uae30",
                                                             None))
        __qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        __qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None));
        __qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        __qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ud658\uc790ID", None));
        __qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        __qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None));
        __qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        __qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0ac\uc77c\uc2dc", None));
        __qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        __qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc810\uc218", None));

    #TODO: pushButton 코드봐서 정리하고 logo도 정리

    # retranslateUi

