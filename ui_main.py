# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test5lNtcnu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 811)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.drop_frame = QFrame(self.centralwidget)
        self.drop_frame.setObjectName(u"drop_frame")
        self.drop_frame.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(190, 190, 190);")
        self.drop_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_frame.setFrameShadow(QFrame.Raised)
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
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(54, 54, 54);")
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
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.btn_toggle = QPushButton(self.frame_5)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(0, 40))
        self.btn_toggle.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_toggle)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.top_menus = QFrame(self.frame_left_menu)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMaximumSize(QSize(16777215, 230))
        self.top_menus.setFrameShape(QFrame.NoFrame)
        self.top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.top_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 2, 5, 2)
        self.btn_home = QPushButton(self.top_menus)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_anal = QPushButton(self.top_menus)
        self.btn_anal.setObjectName(u"btn_anal")
        self.btn_anal.setMinimumSize(QSize(0, 40))
        self.btn_anal.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_anal)

        self.btn_new_file = QPushButton(self.top_menus)
        self.btn_new_file.setObjectName(u"btn_new_file")
        self.btn_new_file.setMinimumSize(QSize(0, 40))
        self.btn_new_file.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_new_file)


        self.verticalLayout_2.addWidget(self.top_menus)

        self.frame_4 = QFrame(self.frame_left_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.top_menus_2 = QFrame(self.frame_left_menu)
        self.top_menus_2.setObjectName(u"top_menus_2")
        self.top_menus_2.setMaximumSize(QSize(16777215, 200))
        self.top_menus_2.setFrameShape(QFrame.NoFrame)
        self.top_menus_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.top_menus_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 2, 5, 2)
        self.btn_open_2 = QPushButton(self.top_menus_2)
        self.btn_open_2.setObjectName(u"btn_open_2")
        self.btn_open_2.setMinimumSize(QSize(0, 40))
        self.btn_open_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_open_2)

        self.btn_save_2 = QPushButton(self.top_menus_2)
        self.btn_save_2.setObjectName(u"btn_save_2")
        self.btn_save_2.setMinimumSize(QSize(0, 40))
        self.btn_save_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_save_2)

        self.btn_new_file_2 = QPushButton(self.top_menus_2)
        self.btn_new_file_2.setObjectName(u"btn_new_file_2")
        self.btn_new_file_2.setMinimumSize(QSize(0, 40))
        self.btn_new_file_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(129, 129, 129);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(152, 255, 140);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_new_file_2)


        self.verticalLayout_2.addWidget(self.top_menus_2)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(7, 0, 0, 0)
        self.title_bar = QFrame(self.content_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setStyleSheet(u"background-color: rgb(143, 143, 143);")
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
        self.verticalLayout_6 = QVBoxLayout(self.frame_title)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Franklin Gothic Heavy")
        font.setPointSize(14)
        self.label_title.setFont(font)

        self.verticalLayout_6.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(150, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_min = QPushButton(self.frame_btns)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(40, 20))
        self.btn_min.setMaximumSize(QSize(40, 20))
        self.btn_min.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btns)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(40, 20))
        self.btn_max.setMaximumSize(QSize(40, 20))
        self.btn_max.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(40, 20))
        self.btn_close.setMaximumSize(QSize(40, 20))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(255, 0, 0);\n"
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
        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.logo)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.pages.addWidget(self.anal)

        self.verticalLayout_4.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.content_frame)


        self.verticalLayout_5.addWidget(self.content)


        self.layout.addWidget(self.drop_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"toggle", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_anal.setText(QCoreApplication.translate("MainWindow", u"ANALYSIS", None))
        self.btn_new_file.setText(QCoreApplication.translate("MainWindow", u"NEW FILE", None))
        self.btn_open_2.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.btn_save_2.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.btn_new_file_2.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"title", None))
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\uc18c\ud654", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.btn_max.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300\ud654", None))
#endif // QT_CONFIG(tooltip)
        self.btn_max.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

